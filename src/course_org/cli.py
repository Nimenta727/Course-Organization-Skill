"""Local metadata, educational alignment and fail-closed release checks.

No AI APIs, cloud uploads, PDF/PPTX extraction, or plagiarism claims.
Run after: python -m pip install -e .
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from .quality import check_teacher_map, check_resource_registry, query_plan


BLOCKED_BINARY_SUFFIXES = {".pdf", ".ppt", ".pptx", ".doc", ".docx",
                           ".zip", ".mp3", ".mp4", ".wav", ".jpg", ".jpeg", ".png"}
ALLOWED_PUBLIC_SUFFIXES = {".md", ".txt", ".json", ".py", ".c", ".h", ".cpp",
                           ".html", ".css", ".js", ".ts", ".svg"}
RIGHTS_OK = {"OWNED", "PERMISSION_PUBLIC", "PUBLIC_DOMAIN", "CC-BY",
             "CC-BY-SA", "CC-BY-NC", "CC-BY-NC-SA"}
CC_RIGHTS = {"CC-BY", "CC-BY-SA", "CC-BY-NC", "CC-BY-NC-SA"}


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"JSON object required: {path}")
    return data


def safe_project_path(root: Path, rel: object) -> Path | None:
    if not isinstance(rel, str) or not rel or Path(rel).is_absolute():
        return None
    root = root.resolve()
    resolved = (root / rel).resolve()
    return resolved if resolved.is_relative_to(root) and resolved != root else None


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def scan(source: Path, out: Path) -> list[str]:
    errors: list[str] = []
    if not source.is_dir():
        return ["INPUT directory does not exist"]
    if out.resolve().is_relative_to(source.resolve()):
        return ["Private inventory output must be OUTSIDE the scanned source directory"]
    destination = out.resolve().parent
    if any((ancestor / ".git").exists() for ancestor in (destination, *destination.parents)):
        return ["Private inventory output must be OUTSIDE every Git worktree"]
    entries = []
    for p in sorted(source.rglob("*")):
        if p.is_symlink() or not p.is_file():
            continue
        if any(part.startswith(".") for part in p.relative_to(source).parts):
            continue
        match = re.search(r"(?:lesson|lecture|week|第)\s*[-_ ]*(\d{1,3})", p.stem, re.I)
        entries.append({
            "path": str(p.relative_to(source)),
            "extension": p.suffix.lower(),
            "bytes": p.stat().st_size,
            "sha256": digest(p),
            "candidate_lesson": match.group(1) if match else None,
            "extraction_status": "NOT_EXTRACTED",
            "rights": "UNKNOWN",
            "external_ai_permission": False,
            "public_release_permission": False,
        })
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        return ["Refusing to overwrite existing inventory: " + str(out)]
    out.write_text(json.dumps({
        "private": True,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_root": str(source.resolve()),
        "files": entries
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return errors


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    cfg = root / "course.json"
    if not cfg.is_file():
        return ["Missing course.json"]
    data = load_json(cfg)
    lessons = data.get("lessons", [])
    if not isinstance(lessons, list) or not lessons:
        return ["course.json needs a nonempty lessons array"]
    seen_lesson_ids: set[str] = set()
    seen_objective_ids: set[str] = set()
    for lesson in lessons:
        if not isinstance(lesson, dict):
            errors.append("Each lesson must be an object")
            continue
        lid = lesson.get("id")
        if not isinstance(lid, str) or not lid:
            errors.append("Lesson is missing id")
            continue
        if lid in seen_lesson_ids:
            errors.append(f"Duplicate lesson id: {lid}")
        seen_lesson_ids.add(lid)
        file = safe_project_path(root, lesson.get("path"))
        if not file or not file.is_file() or file.suffix != ".md":
            errors.append(f"{lid}: missing/unsafe markdown lesson path")
        else:
            content = file.read_text(encoding="utf-8")
            sections = [
                ("learning objectives", ("学习目标", "Learning Objectives")),
                ("explanation", ("知识讲解", "Concept Explanation", "原理讲解")),
                ("examples", ("示例", "Worked Example", "课堂演示")),
                ("misconceptions", ("常见错误", "Misconceptions")),
                ("practice", ("课堂练习", "Practice", "随堂练习")),
                ("review", ("总结", "Recap", "复习")),
            ]
            for label, choices in sections:
                if not any(c.lower() in content.lower() for c in choices):
                    errors.append(f"{lid}: missing lesson section: {label}")
        objs = lesson.get("objectives")
        if not isinstance(objs, list) or not objs:
            errors.append(f"{lid}: no learning objectives")
            continue
        for obj in objs:
            if not isinstance(obj, dict) or not obj.get("id") or not obj.get("statement"):
                errors.append(f"{lid}: objective missing id/statement")
                continue
            oid = obj["id"]
            if oid in seen_objective_ids:
                errors.append(f"Duplicate objective id: {oid}")
            seen_objective_ids.add(oid)
            if not isinstance(obj.get("activities"), list) or not obj["activities"]:
                errors.append(f"{lid}/{oid}: no linked teaching activity")
            if not isinstance(obj.get("assessments"), list) or not obj["assessments"]:
                errors.append(f"{lid}/{oid}: no linked assessment")
    return errors


def audit(root: Path, sources_path: Path | None, teacher_map_path: Path | None = None) -> list[str]:
    errors: list[str] = []
    release_file = root / "provenance" / "release-manifest.json"
    if not release_file.exists():
        return ["Missing provenance/release-manifest.json"]
    release = load_json(release_file)
    if release.get("public_release") is not True:
        errors.append("Explicit public_release: true required")
    if release.get("explicit_publication_approval") is not True:
        errors.append("Missing explicit_publication_approval: true")
    if not str(release.get("reviewed_by") or "").strip():
        errors.append("A named human reviewer is required")
    if not isinstance(release.get("commercial"), bool):
        errors.append("commercial must be true or false")
    license_name = str(release.get("output_license") or "").upper()
    if not license_name:
        errors.append("Missing output_license")
    artifacts = release.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        return errors + ["No release artifacts listed"]
    referenced: set[str] = set()
    for item in artifacts:
        if isinstance(item, dict) and isinstance(item.get("sources_used"), list):
            referenced.update(x for x in item["sources_used"] if isinstance(x, str))
    source_map: dict[str, dict[str, Any]] = {}
    if referenced:
        if sources_path is None:
            errors.append("Private source manifest --sources required for referenced sources")
        elif not sources_path.is_file():
            errors.append("Private source manifest does not exist")
        else:
            source_data = load_json(sources_path)
            for s in source_data.get("sources", []):
                if isinstance(s, dict) and isinstance(s.get("id"), str):
                    source_map[s["id"]] = s
    for item in artifacts:
        if not isinstance(item, dict):
            errors.append("Release artifact must be an object")
            continue
        rel = item.get("path")
        file = safe_project_path(root, rel)
        if not file or not file.is_file():
            errors.append(f"Invalid/missing release artifact: {rel}")
            continue
        if file.suffix.lower() in BLOCKED_BINARY_SUFFIXES or file.suffix.lower() not in ALLOWED_PUBLIC_SUFFIXES:
            errors.append(f"Restricted file type needs a separate manual release process: {rel}")
        for field in ("contains_source_expression", "contains_personal_data"):
            if item.get(field) is not False:
                errors.append(f"{rel}: {field} must be explicitly false")
        if item.get("originality_reviewed") is not True:
            errors.append(f"{rel}: originality_reviewed must be true")
        if item.get("origin") != "independently_authored":
            errors.append(f"{rel}: this conservative release gate supports only independently authored artifacts")
        refs = item.get("sources_used")
        if not isinstance(refs, list):
            errors.append(f"{rel}: sources_used must be a list")
            continue
        for sid in refs:
            source = source_map.get(sid)
            if not source:
                errors.append(f"{rel}: source {sid} missing from private rights manifest")
                continue
            rights = source.get("rights")
            if rights not in RIGHTS_OK:
                errors.append(f"{rel}: source {sid} has blocked/unknown rights: {rights}")
                continue
            if source.get("allow_public_adaptation") is not True:
                errors.append(f"{rel}: {sid} lacks public reuse authorization")
            if not str(source.get("rights_evidence") or "").strip():
                errors.append(f"{rel}: {sid} lacks rights evidence")
            if source.get("personal_data_reviewed") is not True:
                errors.append(f"{rel}: {sid} lacks privacy review")
            if rights in CC_RIGHTS:
                if not str(item.get("attribution") or "").strip():
                    errors.append(f"{rel}: {sid} missing CC attribution")
                for field in ("title", "author", "source_url", "license_url"):
                    if not str(source.get(field) or "").strip():
                        errors.append(f"{rel}: {sid} missing TASL {field}")
            if rights in ("CC-BY-NC", "CC-BY-NC-SA") and release.get("commercial") is not False:
                errors.append(f"{rel}: {sid} NC licence conflicts with commercial use or missing decision")
            if rights == "CC-BY-SA" and not license_name.startswith("CC-BY-SA"):
                errors.append(f"{rel}: {sid} SA requires compatible adaptation licence")
            if rights == "CC-BY-NC-SA" and not license_name.startswith("CC-BY-NC-SA"):
                errors.append(f"{rel}: {sid} NC-SA requires compatible adaptation licence")
    if release.get("teacher_materials_used") is True:
        if teacher_map_path is None:
            errors.append("Teacher materials used: private --teacher-map required")
        else:
            errors.extend(check_teacher_map(teacher_map_path))
    registry = root / "provenance" / "resource-registry.json"
    if registry.exists():
        errors.extend(check_resource_registry(registry))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Private-first course organization checks")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_scan = sub.add_parser("scan", help="Create local-only file metadata inventory")
    p_scan.add_argument("input", type=Path)
    p_scan.add_argument("--out", type=Path, required=True)
    p_validate = sub.add_parser("validate", help="Check lesson structure and objective alignment")
    p_validate.add_argument("course", type=Path)
    p_audit = sub.add_parser("audit", help="Conservative pre-publication gate (NOT legal clearance)")
    p_audit.add_argument("course", type=Path)
    p_audit.add_argument("--sources", type=Path, help="Private source rights manifest, kept outside public Git")
    p_audit.add_argument("--teacher-map", type=Path, help="Private teacher evidence ledger kept outside Git")
    p_teacher = sub.add_parser("teacher-check", help="Validate private teacher evidence mapping")
    p_teacher.add_argument("manifest", type=Path)
    p_resources = sub.add_parser("resource-check", help="Validate researched source registry metadata")
    p_resources.add_argument("registry", type=Path)
    p_plan = sub.add_parser("research-plan", help="Print external-search queries; never performs a search")
    p_plan.add_argument("course", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.cmd == "scan":
            issues = scan(args.input, args.out)
        elif args.cmd == "validate":
            issues = validate(args.course)
        elif args.cmd == "teacher-check":
            p = args.manifest.resolve()
            if any((d / ".git").exists() for d in (p.parent, *p.parents)):
                issues = ["Teacher evidence map must remain OUTSIDE any Git worktree"]
            else:
                issues = check_teacher_map(args.manifest)
        elif args.cmd == "resource-check":
            issues = check_resource_registry(args.registry)
        elif args.cmd == "research-plan":
            print(json.dumps(query_plan(load_json(args.course / "course.json")),
                             ensure_ascii=False, indent=2))
            return 0
        else:
            issues = audit(args.course, args.sources, args.teacher_map)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        issues = [f"Cannot complete check: {exc}"]
    if issues:
        for issue in issues:
            print("BLOCK:", issue)
        return 1
    print("PASS: deterministic checks only; no guarantee of legal safety or factual correctness")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

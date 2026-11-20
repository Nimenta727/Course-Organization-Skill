"""Metadata-only checks for teacher fidelity and researched resources.

Neither check proves teaching fidelity, web accuracy, non-infringement nor legal
rights. They validate declarations; human review is mandatory.
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit


KINDS = {"concept", "demonstration", "board_step", "example", "question",
         "error_demo", "diagram", "emphasis", "assignment", "transition", "other"}
HANDLINGS = {"original_explanation", "private_only", "blocked_rights", "unresolved"}
INTENTS = {"explicit", "hypothesized", "unknown"}
TIERS = {"official_exam", "official_curriculum", "university", "professional_body",
         "peer_reviewed", "oer", "community"}
USAGES = {"link_only", "background_only", "adapt_with_verified_license"}


def read_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("Expected JSON object")
    return value


def check_teacher_map(path: Path) -> list[str]:
    """Inspect private coverage ledger, not unprovided original teacher files."""
    if not path.is_file():
        return [f"Missing teacher evidence map: {path}"]
    data = read_object(path)
    errors = []
    if data.get("private") is not True:
        errors.append("Teacher evidence map must be private=true")
    segments = data.get("segments")
    if not isinstance(segments, list) or not segments:
        return errors + ["Teacher map requires nonempty segments"]
    seen: set[str] = set()
    for idx, seg in enumerate(segments, 1):
        loc = f"segment {idx}"
        if not isinstance(seg, dict):
            errors.append(f"{loc}: expected JSON object")
            continue
        sid = seg.get("id")
        if not isinstance(sid, str) or not sid.strip():
            errors.append(f"{loc}: missing id")
        elif sid in seen:
            errors.append(f"{loc}: duplicate id {sid}")
        else:
            seen.add(sid)
        for field in ("source_id", "location"):
            if not isinstance(seg.get(field), str) or not seg[field].strip():
                errors.append(f"{loc}: missing {field}")
        if seg.get("kind") not in KINDS:
            errors.append(f"{loc}: unknown kind")
        treatment = seg.get("handling")
        if treatment not in HANDLINGS:
            errors.append(f"{loc}: invalid handling")
        if treatment == "unresolved":
            errors.append(f"{loc}: unresolved important source item requires review")
        if treatment == "original_explanation" and not seg.get("lesson_section"):
            errors.append(f"{loc}: independently written explanation needs lesson_section anchor")
        intent = seg.get("teacher_intent")
        if not isinstance(intent, dict) or intent.get("status") not in INTENTS:
            errors.append(f"{loc}: missing or invalid teacher_intent status")
        elif intent["status"] == "hypothesized":
            if not str(intent.get("reason") or "").strip():
                errors.append(f"{loc}: hypothesized intent requires reason")
            if not str(intent.get("alternative") or "").strip():
                errors.append(f"{loc}: hypothesized intent requires alternative interpretation")
        elif intent["status"] == "explicit" and not str(intent.get("evidence") or "").strip():
            errors.append(f"{loc}: explicit intent requires actual evidence")
        if seg.get("kind") == "error_demo":
            if seg.get("error_status") not in {
                "verified_error", "possible_error", "purposeful_counterexample"
            }:
                errors.append(f"{loc}: error demonstration needs uncertainty-aware error_status")
            if not str(seg.get("explanation_or_unresolved") or "").strip():
                errors.append(f"{loc}: error demonstration needs diagnosis or unresolved note")
    return errors


def check_resource_registry(path: Path) -> list[str]:
    """Metadata gate for researched sources; never claims links were actually visited."""
    if not path.is_file():
        return [f"Missing resource registry: {path}"]
    data = read_object(path)
    resources = data.get("resources")
    if not isinstance(resources, list) or not resources:
        return ["Resource registry requires nonempty resources"]
    errors = []
    seen: set[str] = set()
    for idx, r in enumerate(resources, 1):
        loc = f"resource {idx}"
        if not isinstance(r, dict):
            errors.append(f"{loc}: expected object")
            continue
        rid = r.get("id")
        if not isinstance(rid, str) or not rid.strip():
            errors.append(f"{loc}: missing id")
        elif rid in seen:
            errors.append(f"{loc}: duplicate id {rid}")
        else:
            seen.add(rid)
        for field in ("lesson_id", "title", "publisher", "relevance"):
            if not isinstance(r.get(field), str) or not r[field].strip():
                errors.append(f"{loc}: missing {field}")
        if not isinstance(r.get("objective_ids"), list) or not r["objective_ids"]:
            errors.append(f"{loc}: objective_ids required")
        url = r.get("url")
        if not isinstance(url, str):
            errors.append(f"{loc}: valid HTTPS URL required")
        else:
            parsed = urlsplit(url)
            if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
                errors.append(f"{loc}: valid HTTPS URL required")
        if r.get("authority_tier") not in TIERS:
            errors.append(f"{loc}: unknown authority_tier")
        if r.get("usage") not in USAGES:
            errors.append(f"{loc}: invalid usage")
        checked = r.get("verified_at")
        if not isinstance(checked, str):
            errors.append(f"{loc}: verified_at YYYY-MM-DD required")
        else:
            try:
                if date.fromisoformat(checked) > date.today():
                    errors.append(f"{loc}: verified_at cannot be in the future")
            except ValueError:
                errors.append(f"{loc}: invalid verified_at date")
        if r.get("actual_live_check") is not True:
            errors.append(f"{loc}: actual_live_check must be confirmed by operator")
        if r.get("authority_tier") == "official_exam" and r.get("usage") != "link_only":
            errors.append(f"{loc}: official exam contents default to link_only")
        if r.get("usage") == "adapt_with_verified_license":
            if r.get("license_verified") is not True:
                errors.append(f"{loc}: adaptation requires verified license")
            for field in ("license", "license_url", "author", "modification_notice", "rights_evidence"):
                if not isinstance(r.get(field), str) or not r[field].strip():
                    errors.append(f"{loc}: adaptation missing {field}")
    return errors


def query_plan(course: dict) -> dict:
    """Offline discovery queries. This function does not browse the internet."""
    subject = course.get("subject") or course.get("title") or "course"
    plans = []
    for lesson in course.get("lessons", []):
        if not isinstance(lesson, dict):
            continue
        for obj in lesson.get("objectives", []):
            if not isinstance(obj, dict):
                continue
            statement = obj.get("statement")
            if not isinstance(statement, str) or not statement.strip():
                continue
            plans.append({
                "lesson_id": lesson.get("id"),
                "objective_id": obj.get("id"),
                "queries": [
                    f"{subject} {statement} official syllabus examination specifications",
                    f"{subject} {statement} university tutorial open educational resources",
                    f"{subject} {statement} research common misconceptions advanced proof",
                ],
                "source_priority": ["official_curriculum", "official_exam",
                                    "university", "peer_reviewed", "oer"],
                "search_status": "NOT_SEARCHED",
                "reuse_rule": "Link official examination source; write independent problems",
            })
    return {"generated_plan_only": True, "requires_live_web_tools": True, "plans": plans}

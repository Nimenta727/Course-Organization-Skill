"""Build a standalone, allowlist-only Agent Skill ZIP for GitHub releases.

The ZIP includes SKILL.md, license, bilingual READMEs, references and the
course template. It never includes source uploads, course provenance, tests,
private review reports, the Python CLI, or arbitrary repository contents.
The CLI wheel is distributed as a separate release asset.
"""
from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = ("SKILL.md", "LICENSE", "README.md", "README_EN.md")
ALLOW_DIRS = ("references", "assets/course-template")
ALLOW_EXTENSIONS = {".md", ".json", ".yaml", ".yml", ".txt"}
ZIP_ROOT = "course-organization"


def collect_files(root: Path = ROOT) -> list[Path]:
    """Collect only expected Skill assets. Fail on symlinks and missing inputs."""
    paths = [root / name for name in ROOT_FILES]
    if any(not path.is_file() or path.is_symlink() for path in paths):
        raise ValueError("Missing or symlinked mandatory Skill file")
    for directory in ALLOW_DIRS:
        base = root / directory
        if not base.is_dir() or base.is_symlink():
            raise ValueError(f"Missing/unsafe Skill directory: {directory}")
        for entry in sorted(base.rglob("*")):
            if entry.is_symlink():
                raise ValueError(f"Symlink not allowed in Skill bundle: {entry}")
            if not entry.is_file():
                continue
            if entry.suffix.lower() not in ALLOW_EXTENSIONS:
                raise ValueError(f"Unrecognized bundled file type: {entry}")
            if not entry.resolve().is_relative_to(root.resolve()):
                raise ValueError(f"File escapes repository root: {entry}")
            paths.append(entry)
    return sorted(paths, key=lambda p: p.relative_to(root).as_posix())


def detect_version(root: Path = ROOT) -> str:
    package = (root / "src/course_org/__init__.py").read_text(encoding="utf-8")
    match = re.search(r'__version__ = "(\d+\.\d+\.\d+)"', package)
    if not match:
        raise ValueError("Cannot find package version")
    return match.group(1)


def build(output: Path, root: Path = ROOT) -> tuple[Path, str]:
    """Create reproducible ZIP and SHA-256 digest without network access."""
    output = output.resolve()
    inputs = collect_files(root)
    if output in (p.resolve() for p in inputs):
        raise ValueError("Cannot overwrite an input file")
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for file in inputs:
            relative = file.relative_to(root).as_posix()
            info = ZipInfo(f"{ZIP_ROOT}/{relative}", (1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = (0o100644 << 16)
            archive.writestr(info, file.read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)
    return output, hashlib.sha256(output.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a sanitized complete Agent Skill ZIP")
    parser.add_argument("--output", type=Path, help="Archive output file")
    args = parser.parse_args()
    version = detect_version()
    output = args.output or (ROOT / "dist" / f"course-organization-skill-v{version}.zip")
    path, sha = build(output)
    print(f"Built {path}")
    print(f"SHA256 {sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

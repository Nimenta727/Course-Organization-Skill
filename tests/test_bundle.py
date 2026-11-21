"""Offline checks that the release Skill archive is complete and private-safe."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


class SkillBundleTests(unittest.TestCase):
    def test_full_skill_zip_without_private_or_internal_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / "skill.zip"
            cmd = [sys.executable, str(ROOT / "scripts/package_skill.py"),
                   "--output", str(archive)]
            subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=True)
            self.assertTrue(archive.exists())
            with ZipFile(archive) as package:
                files = set(package.namelist())
                for required in (
                    "course-organization/SKILL.md",
                    "course-organization/LICENSE",
                    "course-organization/README.md",
                    "course-organization/README_EN.md",
                    "course-organization/references/student-edition.md",
                    "course-organization/references/subagent-review.md",
                    "course-organization/references/copyright-gate.md",
                    "course-organization/assets/course-template/course.json",
                ):
                    self.assertIn(required, files)
                self.assertFalse(any("/tests/" in name or "/docs/routine/" in name
                                     or "/.github/" in name or "/src/" in name
                                     or "teacher-materials" in name or "/private/" in name
                                     for name in files))
                self.assertTrue(all(name.startswith("course-organization/") for name in files))

    def test_build_is_reproducible(self):
        with tempfile.TemporaryDirectory() as tmp:
            output1, output2 = Path(tmp) / "a.zip", Path(tmp) / "b.zip"
            cmd = [sys.executable, str(ROOT / "scripts/package_skill.py")]
            for dest in (output1, output2):
                subprocess.run(cmd + ["--output", str(dest)], cwd=ROOT,
                               capture_output=True, text=True, check=True)
            self.assertEqual(output1.read_bytes(), output2.read_bytes())

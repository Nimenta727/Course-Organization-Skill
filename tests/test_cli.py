import json
import tempfile
import unittest
from pathlib import Path

from course_org.cli import audit, scan, validate


LESSON_TEXT = """# Lesson 01
## 学习目标
Explain the problem.
## 知识讲解
An independent explanation.
## 示例
A new example.
## 常见错误
An original misconception.
## 课堂练习
Try an original problem.
## 总结
Review the new skills.
"""


class TestCourseCLI(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "course"
        self.root.mkdir()
        file = self.root / "lessons" / "L01" / "lesson.md"
        file.parent.mkdir(parents=True)
        file.write_text(LESSON_TEXT, encoding="utf-8")
        cfg = {
            "course_id": "sample", "title": "Original example",
            "lessons": [{"id": "L01", "path": "lessons/L01/lesson.md",
                         "objectives": [{"id": "LO01", "statement": "Explain a concept",
                                         "activities": ["ACT01"], "assessments": ["ASM01"]}]}]
        }
        (self.root / "course.json").write_text(json.dumps(cfg), encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_validate(self):
        self.assertEqual(validate(self.root), [])

    def test_alignment_missing_assessment(self):
        cfg = json.loads((self.root / "course.json").read_text())
        cfg["lessons"][0]["objectives"][0]["assessments"] = []
        (self.root / "course.json").write_text(json.dumps(cfg))
        self.assertTrue(any("assessment" in e for e in validate(self.root)))

    def write_release(self, **overrides):
        data = {
            "public_release": True, "explicit_publication_approval": True,
            "reviewed_by": "test-reviewer", "commercial": False,
            "output_license": "MIT",
            "artifacts": [{"path": "lessons/L01/lesson.md",
                           "origin": "independently_authored",
                           "sources_used": [], "contains_source_expression": False,
                           "contains_personal_data": False,
                           "originality_reviewed": True, "attribution": ""}]
        }
        data.update(overrides)
        (self.root / "provenance").mkdir(exist_ok=True)
        (self.root / "provenance" / "release-manifest.json").write_text(json.dumps(data))

    def test_audit_explicit_original_pass(self):
        self.write_release()
        self.assertEqual(audit(self.root, None), [])

    def test_audit_no_approval_blocks(self):
        self.write_release(explicit_publication_approval=False)
        self.assertTrue(audit(self.root, None))

    def test_audit_unknown_rights_blocks(self):
        self.write_release()
        p = self.root / "provenance" / "release-manifest.json"
        data = json.loads(p.read_text())
        data["artifacts"][0]["sources_used"] = ["S01"]
        p.write_text(json.dumps(data))
        rights = Path(self.temp.name) / "private-source-manifest.json"
        rights.write_text(json.dumps({"sources": [{"id": "S01", "rights": "UNKNOWN"}]}))
        self.assertTrue(any("blocked/unknown" in e for e in audit(self.root, rights)))

    def test_audit_never_accepts_private_binary(self):
        self.write_release()
        raw = self.root / "source.pdf"
        raw.write_bytes(b"FAKE PRIVATE PDF")
        p = self.root / "provenance" / "release-manifest.json"
        data = json.loads(p.read_text())
        data["artifacts"][0]["path"] = "source.pdf"
        p.write_text(json.dumps(data))
        self.assertTrue(any("Restricted file type" in e for e in audit(self.root, None)))

    def test_scan_blocks_inventory_inside_git_repository(self):
        input_dir = Path(self.temp.name) / "private_inputs"
        input_dir.mkdir()
        (input_dir / "Lesson01.pdf").write_bytes(b"test-source")
        worktree = Path(self.temp.name) / "public_repo"
        (worktree / ".git").mkdir(parents=True)
        output = worktree / "private-index.json"
        issues = scan(input_dir, output)
        self.assertTrue(any("Git worktree" in e for e in issues))
        self.assertFalse(output.exists())

    def test_scan_metadata_only(self):
        input_dir = Path(self.temp.name) / "private_inputs"
        input_dir.mkdir()
        (input_dir / "Lecture02.pptx").write_bytes(b"teacher-only")
        output = Path(self.temp.name) / "private-index.json"
        self.assertEqual(scan(input_dir, output), [])
        manifest = json.loads(output.read_text())
        self.assertTrue(manifest["private"])
        self.assertEqual(manifest["files"][0]["candidate_lesson"], "02")
        self.assertNotIn("teacher-only", output.read_text())


if __name__ == "__main__":
    unittest.main()

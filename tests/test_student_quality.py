"""Deep student lessons and independent audit manifest regression checks.

Synthetic reviewer metadata only: passing this test does NOT mean real subagents
have been run or that any teaching content is legally safe.
"""
import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from course_org.student_quality import (
    REVIEW_ROLES, check_review_gate, check_student_course,
)
from course_org.reviewer_tasks import make_review_plan
from course_org.cli import main

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "examples" / "sample-course"


class StudentDepthTests(unittest.TestCase):
    def setUp(self):
        self.work = tempfile.TemporaryDirectory()
        self.base = Path(self.work.name)
        self.course = self.base / "course"
        shutil.copytree(SAMPLE, self.course)
        self.chapter = self.course / "lessons" / "L01" / "lesson.md"

    def tearDown(self):
        self.work.cleanup()

    def review_report(self):
        sha = hashlib.sha256(self.chapter.read_bytes()).hexdigest()
        plan = make_review_plan(self.course)["lessons"][0]
        tasks_by_role = {t["role"]: t for t in plan["tasks"]}
        entries = [{
            "role": role,
            "reviewer_id": "independent-tester-" + str(i),
            "mode": "subagent",
            "status": "PASS",
            "lesson_sha256": sha,
            "evidence": "Synthetic metadata fixture. The claimed reviewer has independently checked every "
                        "declared knowledge point and question, including topic progression and solved "
                        "answers. This is fake test data, not real audit evidence or approval.",
            "checked_items": tasks_by_role[role]["required_checks"],
            "question_checks": [{
                "id": q, "blind_solved": True, "compared_to_solution": True, "status": "PASS",
                "reasoning": "Synthetic fixture only: pretend-independent reasoning detailed enough "
                             "to test the mandatory JSON structure, not to prove a real check."
            } for q in plan["assignment_ids"]] if role == "assignment_integrity" else [],
            "limitations": ["Synthetic fixture; actual reviewers have not been deployed"],
            "blocking_findings": [],
        } for i, role in enumerate(REVIEW_ROLES)]
        data = {"author_id": "author-fixture", "lesson_reviews": [{
            "lesson_path": "lessons/L01/lesson.md",
            "reviews": entries
        }]}
        report = self.base / "private-independent-review.json"
        report.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        return report

    def test_full_chapter_passes_static_depth_check(self):
        self.assertEqual(check_student_course(self.course), [])
        self.assertEqual(main(["student-check", str(self.course)]), 0)

    def test_one_sentence_intro_blocks(self):
        text = self.chapter.read_text(encoding="utf-8")
        start = text.index("## 本课导读")
        end = text.index("## 预备知识")
        text = text[:start] + "## 本课导读\n本课介绍算法。\n\n" + text[end:]
        self.chapter.write_text(text, encoding="utf-8")
        self.assertTrue(any("本课导读" in e for e in check_student_course(self.course)))

    def test_one_line_knowledge_point_blocks(self):
        text = self.chapter.read_text(encoding="utf-8")
        start = text.index("### K02 ·")
        end = text.index("### K03 ·")
        text = text[:start] + "### K02 · 初始化\n只需初始化。\n\n" + text[end:]
        self.chapter.write_text(text, encoding="utf-8")
        self.assertTrue(any("K02" in e for e in check_student_course(self.course)))

    def test_missing_tier_or_solution_blocks(self):
        text = self.chapter.read_text(encoding="utf-8").replace("### Q05【挑战】", "### Q05【基础】")
        text = text.replace("### Q05 解析", "### Q06 解析")
        self.chapter.write_text(text, encoding="utf-8")
        issues = check_student_course(self.course)
        self.assertTrue(any("挑战" in e for e in issues))
        self.assertTrue(any("Missing/extra homework solutions" in e for e in issues))

    def test_private_producer_heading_blocks(self):
        text = self.chapter.read_text(encoding="utf-8") + "\n### 教师授课主线\n内部内容\n"
        self.chapter.write_text(text, encoding="utf-8")
        self.assertTrue(any("Internal producer heading" in e for e in check_student_course(self.course)))

    def test_seven_independent_role_report_schema(self):
        report = self.review_report()
        self.assertEqual(check_review_gate(self.course, report), [])
        self.assertEqual(main(["ready", str(self.course), "--report", str(report)]), 0)

    def test_stale_sha_invalidates_all_reviews(self):
        report = self.review_report()
        self.chapter.write_text(self.chapter.read_text(encoding="utf-8") + "\n修订后重新审阅。\n", encoding="utf-8")
        errors = check_review_gate(self.course, report)
        self.assertTrue(any("stale lesson digest" in e for e in errors))

    def test_generator_cannot_self_approve(self):
        report = self.review_report()
        data = json.loads(report.read_text(encoding="utf-8"))
        data["lesson_reviews"][0]["reviews"][0]["reviewer_id"] = "author-fixture"
        report.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        self.assertTrue(any("reviewer must differ" in e for e in check_review_gate(self.course, report)))

    def test_missing_review_role_blocks(self):
        report = self.review_report()
        data = json.loads(report.read_text(encoding="utf-8"))
        data["lesson_reviews"][0]["reviews"].pop()
        report.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        self.assertTrue(any("missing independent reviewer roles" in e for e in check_review_gate(self.course, report)))

    def test_unreviewed_course_never_ready(self):
        self.assertNotEqual(main(["ready", str(self.course),
                                  "--report", str(self.base / "not-present.json")]), 0)

    def test_review_plan_is_not_a_real_review(self):
        plan = make_review_plan(self.course)
        self.assertFalse(plan["review_executed"])
        self.assertEqual(plan["review_status"], "REVIEW_PENDING")
        self.assertEqual(len(plan["lessons"][0]["tasks"]), 7)
        self.assertEqual(main(["review-plan", str(self.course)]), 0)

    def test_assignment_reviewer_must_check_every_question(self):
        report = self.review_report()
        data = json.loads(report.read_text(encoding="utf-8"))
        reviews = data["lesson_reviews"][0]["reviews"]
        assignment = next(x for x in reviews if x["role"] == "assignment_integrity")
        assignment["question_checks"].pop()
        report.write_text(json.dumps(data), encoding="utf-8")
        self.assertTrue(any("every assignment" in e for e in check_review_gate(self.course, report)))

    def test_novice_reviewer_must_cover_all_knowledge(self):
        report = self.review_report()
        data = json.loads(report.read_text(encoding="utf-8"))
        novice = next(x for x in data["lesson_reviews"][0]["reviews"] if x["role"] == "novice_readability")
        novice["checked_items"].remove("K02")
        report.write_text(json.dumps(data), encoding="utf-8")
        self.assertTrue(any("incomplete audit coverage" in e for e in check_review_gate(self.course, report)))

    def test_exact_duplicate_assignment_blocks(self):
        text = self.chapter.read_text(encoding="utf-8")
        import re
        a = re.search(r"\*\*任务：\*\*(.*?)(?=\*\*提交内容：\*\*)", text, flags=re.S)
        first = a.group(1)
        starts = list(re.finditer(r"\*\*任务：\*\*(.*?)(?=\*\*提交内容：\*\*)", text, flags=re.S))
        self.assertGreaterEqual(len(starts), 5)
        second = starts[1]
        text = text[:second.start(1)] + first + text[second.end(1):]
        self.chapter.write_text(text, encoding="utf-8")
        self.assertTrue(any("near-duplicate homework" in e for e in check_student_course(self.course)))

    def test_review_report_inside_other_git_worktree_blocks(self):
        report = self.review_report()
        gitroot = self.base / "worktree"
        (gitroot / ".git").mkdir(parents=True)
        unsafe = gitroot / "private-review.json"
        unsafe.write_bytes(report.read_bytes())
        self.assertTrue(any("Git worktree" in e for e in check_review_gate(self.course, unsafe)))


if __name__ == "__main__":
    unittest.main()

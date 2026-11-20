import json
import tempfile
import unittest
from pathlib import Path

from course_org.quality import check_teacher_map, check_resource_registry, query_plan


class TestTeacherResearch(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / "data.json"

    def tearDown(self):
        self.temp.cleanup()

    def write(self, value):
        self.path.write_text(json.dumps(value), encoding="utf-8")

    def seg(self, **kwargs):
        data = {
            "id": "E01", "source_id": "S01", "location": "slide 2",
            "kind": "error_demo", "handling": "original_explanation",
            "lesson_section": "常见错误",
            "teacher_intent": {"status": "hypothesized",
                               "reason": "followed by a correction",
                               "alternative": "could be unintentional"},
            "error_status": "possible_error",
            "explanation_or_unresolved": "Independently explain and correct",
        }
        data.update(kwargs)
        return data

    def src(self, **kwargs):
        data = {
            "id": "R01", "lesson_id": "L01", "objective_ids": ["LO01"],
            "title": "Official syllabus", "publisher": "Exam board",
            "relevance": "Exam topic", "url": "https://example.edu/exams",
            "authority_tier": "official_exam", "usage": "link_only",
            "verified_at": "2026-11-20", "actual_live_check": True
        }
        data.update(kwargs)
        return data

    def test_teacher_intent_uncertainty_valid(self):
        self.write({"private": True, "segments": [self.seg()]})
        self.assertEqual(check_teacher_map(self.path), [])

    def test_teacher_claim_of_explicit_intent_requires_evidence(self):
        self.write({"private": True, "segments": [
            self.seg(teacher_intent={"status": "explicit"})]})
        self.assertTrue(any("requires actual evidence" in x for x in check_teacher_map(self.path)))

    def test_teacher_unresolved_blocks_completion(self):
        self.write({"private": True, "segments": [self.seg(handling="unresolved")]})
        self.assertTrue(check_teacher_map(self.path))

    def test_official_exam_link_only(self):
        self.write({"resources": [self.src()]})
        self.assertEqual(check_resource_registry(self.path), [])

    def test_official_exam_adaptation_blocks(self):
        self.write({"resources": [self.src(usage="adapt_with_verified_license")]})
        self.assertTrue(any("link_only" in x for x in check_resource_registry(self.path)))

    def test_unverified_search_blocks(self):
        self.write({"resources": [self.src(actual_live_check=False)]})
        self.assertTrue(any("actual_live_check" in x for x in check_resource_registry(self.path)))

    def test_unlicensed_adaptation_blocks(self):
        self.write({"resources": [self.src(authority_tier="oer",
                                            usage="adapt_with_verified_license")]})
        self.assertTrue(any("verified license" in x for x in check_resource_registry(self.path)))

    def test_plan_is_not_real_search(self):
        result = query_plan({"subject": "C Programming",
                             "lessons": [{"id": "L01", "objectives": [
                                 {"id": "LO01", "statement": "Explain arrays"}]}]})
        self.assertTrue(result["generated_plan_only"])
        self.assertEqual(result["plans"][0]["search_status"], "NOT_SEARCHED")


if __name__ == "__main__":
    unittest.main()

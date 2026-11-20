"""Independent-review task planner: generates instructions, NOT subagents or approvals.

This module never contacts third-party services, reads teacher originals,
writes reviewer attestations, or publishes content.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROLES = (
    "teacher_coverage", "novice_readability", "subject_accuracy",
    "assignment_integrity", "revision_usefulness", "rights_privacy", "adversarial",
)

ROLE_NOTES = {
    "teacher_coverage": (
        "仅在被授权的私有环境中逐项对照教师证据台账：章节顺序、板书跳步、错误示范、课堂强调。"
        "检查每个 K 知识点如何体现教师教学范围；未知教师意图只能列为假设。不要复制教师独创表达。",
        "Requires authorized private evidence; never send teacher originals to an unapproved model."),
    "novice_readability": (
        "假设学生第一次接触课程：从头独立阅读，指出每个 K 的未解释术语、中间推理遗漏、过快跳步。"
        "在不偷看解析的前提下尝试 Q01、Q02；不能仅凭结构或字数签字。",
        "Review from the perspective of a first-time learner."),
    "subject_accuracy": (
        "对每个知识点与所有作业所涉及的断言独立验算，核对完整例题。"
        "编程须区分标准行为与平台特性，实际无法编译时填写 NOT_RUN，不得编造执行结果。",
        "Verify every core concept and the complete worked example."),
    "assignment_integrity": (
        "不看作者答案，独立解答每道 Q；再逐一与答案比对，验证题意、边界、错误辨析、"
        "任务难度和验收标准，写出每道题独立验算的具体证据。",
        "Blind-solve ALL assignments before inspecting published solutions."),
    "revision_usefulness": (
        "只靠复习速览尝试回忆每个 K 的关键规则与误区；检查自测能否覆盖主要知识，"
        "速览是否简洁、准确、易定位，不应把整课复制一遍。",
        "Test whether the review pocket supports active recall."),
    "rights_privacy": (
        "核查教师资料、第三方图表、官方真题、学生个人资料、引用及许可。"
        "对权属不明的公开改编默认阻断；不要把元数据 PASS 当法律证明。",
        "Check permissions and privacy, report unresolved rights as BLOCK."),
    "adversarial": (
        "主动找敷衍填充、无根据结论、相互矛盾解释、错配题目/答案、"
        "幻觉引用、未完成验证与不适合新手的表达，指出可复现的反例。",
        "Adversarially seek gaps, contradictions and padding."),
}
ROLE_BASE_CHECKS = {
    "teacher_coverage": ("teacher_coverage",),
    "novice_readability": ("本课导读", "预备知识", "Q01", "Q02"),
    "subject_accuracy": ("例题精讲",),
    "assignment_integrity": ("答案与解析", "blind_solve"),
    "revision_usefulness": ("复习速览",),
    "rights_privacy": ("rights_reuse", "privacy_scan", "exam_rights"),
    "adversarial": ("filler", "contradictions", "unsupported_claims"),
}
ROLE_K_COVERAGE = {
    "teacher_coverage", "novice_readability", "subject_accuracy",
    "revision_usefulness", "adversarial",
}
ROLE_Q_COVERAGE = {"subject_accuracy", "assignment_integrity", "adversarial"}
QUESTION_RE = re.compile(r"(?m)^###\s+(Q\d{2})【(?:基础|应用|挑战)】")


def _safe_path(root: Path, rel: object) -> Path | None:
    if not isinstance(rel, str) or not rel or Path(rel).is_absolute():
        return None
    base = root.resolve()
    target = (base / rel).resolve()
    if target == base or not target.is_relative_to(base):
        return None
    return target


def _lessons(course: Path) -> list[dict]:
    config = json.loads((course / "course.json").read_text(encoding="utf-8"))
    if not isinstance(config, dict) or not isinstance(config.get("lessons"), list):
        raise ValueError("course.json requires lessons array")
    return config["lessons"]


def _details(root: Path, lesson: dict) -> tuple[str, str, list[str], list[str]]:
    rel = lesson.get("path")
    path = _safe_path(root, rel)
    if path is None or not path.is_file() or path.suffix != ".md":
        raise ValueError(f"Unsafe or missing student lesson path: {rel}")
    body = path.read_text(encoding="utf-8")
    sha = hashlib.sha256(path.read_bytes()).hexdigest()
    topics = lesson.get("topics", [])
    ks = [k["id"] for k in topics if isinstance(k, dict) and isinstance(k.get("id"), str)]
    qs = list(dict.fromkeys(QUESTION_RE.findall(body)))
    return rel, sha, ks, qs


def required_checks(role: str, knowledge: list[str], questions: list[str]) -> list[str]:
    """Literal checklist tokens required for that independent reviewer."""
    if role not in ROLES:
        return []
    fields = list(ROLE_BASE_CHECKS[role])
    if role in ROLE_K_COVERAGE:
        fields += knowledge
    if role in ROLE_Q_COVERAGE:
        fields += questions
    return list(dict.fromkeys(fields))


def make_review_plan(root: Path) -> dict:
    """Output role-specific work assignments; does NOT execute or approve reviews."""
    plans = []
    for lesson in _lessons(root):
        if not isinstance(lesson, dict):
            raise ValueError("Invalid lesson object")
        rel, sha, ks, qs = _details(root, lesson)
        tasks = []
        for role in ROLES:
            instruction, note = ROLE_NOTES[role]
            tasks.append({
                "role": role,
                "required_checks": required_checks(role, ks, qs),
                "instruction": instruction,
                "boundary": note,
                "must_produce": ["concrete evidence", "checked_items", "limitations",
                                 "blocking_findings", "actual reviewer identity",
                                 "matching lesson_sha256"],
            })
        plans.append({
            "lesson_path": rel,
            "lesson_sha256": sha,
            "knowledge_topic_ids": ks,
            "assignment_ids": qs,
            "tasks": tasks,
        })
    return {
        "type": "independent_review_delegation_plan",
        "review_executed": False,
        "review_status": "REVIEW_PENDING",
        "requires_true_independent_subagents_or_humans": True,
        "private_teacher_data_must_not_be_uploaded_without_permission": True,
        "lessons": plans,
    }

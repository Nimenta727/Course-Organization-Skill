"""Strict student readability and independent-review metadata checks.

Static checks cannot certify educational accuracy, plagiarism, legal rights,
or that named child agents really ran. Human judgment is still required.
"""
from __future__ import annotations
import hashlib
import json
import re
from difflib import SequenceMatcher
from pathlib import Path
from .reviewer_tasks import ROLES as REVIEW_ROLES, required_checks

HEADINGS = ("本课导读", "预备知识", "核心知识详解", "例题精讲",
            "易错点与纠正", "分层作业", "深入理解", "复习速览", "答案与解析")
FLOORS = {
    "本课导读": 120, "预备知识": 130, "核心知识详解": 1100,
    "例题精讲": 420, "易错点与纠正": 330, "分层作业": 700,
    "深入理解": 240, "复习速览": 230, "答案与解析": 650,
}
TOPIC_FIELDS = ("为什么要学", "直观理解", "准确规则", "逐步推演", "检查理解")
EXAMPLE_FIELDS = ("题目", "思路", "逐步推演", "结果", "验证", "变式")
TASK_FIELDS = ("学习目标", "任务", "提交内容", "验收标准", "提示")
ANSWER_FIELDS = ("结论", "推理", "错误辨析")
REVISION_FIELDS = ("必会", "易错", "自测", "联系")
PRIVATE_HEADINGS = ("教师授课主线", "老师可能在想什么", "版权审核",
                    "证据台账", "来源映射", "审计报告", "内部生产流程")
PLACEHOLDERS = ("TODO", "TBD", "待补充", "此处填写", "示例占位", "稍后补充")
K = re.compile(r"(?m)^###\s+(K\d{2})\s*[·｜:—-]\s*(.+?)\s*$")
Q = re.compile(r"(?m)^###\s+(Q\d{2})【(基础|应用|挑战)】\s*(.*?)\s*$")
S = re.compile(r"(?m)^###\s+(Q\d{2})\s+解析\s*$")


def _obj(path: Path) -> dict:
    result = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(result, dict):
        raise ValueError("Expected JSON object: " + str(path))
    return result


def _path(root: Path, rel: object) -> Path | None:
    if not isinstance(rel, str) or not rel or Path(rel).is_absolute():
        return None
    base = root.resolve()
    value = (base / rel).resolve()
    return value if value != base and value.is_relative_to(base) else None


def _prose(text: str) -> int:
    # Remove fenced code before measuring prose; no padding with huge code blocks.
    text = re.sub(r"(?ms)^\s*(?:\x60{3,}|~{3,}).*?^\s*(?:\x60{3,}|~{3,})[^\n]*$", "", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"(?m)^#{1,6}\s+.*$", "", text)
    return len(re.sub(r"[\s\x60*_#>|~\-\[\](){},.:;!?，。；：？！【】“”‘’=+]", "", text))


def _sections(body: str) -> tuple[list[str], dict[str, str]]:
    hs = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", body))
    result = {h.group(1).strip(): body[h.end():hs[i+1].start() if i+1 < len(hs) else len(body)]
              for i, h in enumerate(hs)}
    return [h.group(1).strip() for h in hs], result


def _entries(block: str, expression: re.Pattern) -> list[tuple[re.Match, str]]:
    matches = list(expression.finditer(block))
    return [(m, block[m.end():matches[i+1].start() if i+1 < len(matches) else len(block)])
            for i, m in enumerate(matches)]


def _required_fields(block: str, names: tuple[str, ...], location: str) -> list[str]:
    return [f"{location}: missing label {name}" for name in names
            if not re.search(r"\*\*" + re.escape(name) + r"[：:]\*\*", block)]


def check_lesson(path: Path, expected_topics: list[str]) -> list[str]:
    if not path.is_file():
        return [f"Missing lesson file: {path}"]
    source = path.read_text(encoding="utf-8")
    heading_order, sections = _sections(source)
    errors = []
    if heading_order != list(HEADINGS):
        errors.append("Nine canonical student H2 sections required once and in order")
    for heading, floor in FLOORS.items():
        if _prose(sections.get(heading, "")) < floor:
            errors.append(f"{heading}: non-code explanation shorter than {floor} characters")
    if _prose(source) < 4000:
        errors.append("Full lesson lacks 4000 substantive non-code characters")
    for heading in re.findall(r"(?m)^#{1,4}\s+(.+)$", source):
        if any(private in heading for private in PRIVATE_HEADINGS):
            errors.append(f"Internal producer heading leaked: {heading}")
    for mark in PLACEHOLDERS:
        if mark.lower() in source.lower():
            errors.append(f"Unfinished placeholder: {mark}")

    topics = _entries(sections.get("核心知识详解", ""), K)
    actual_topics = [m.group(1) for m, _ in topics]
    if len(expected_topics) < 2:
        errors.append("course.json needs >=2 real, expanded K knowledge topics")
    if actual_topics != expected_topics:
        errors.append(f"K topic coverage/order mismatch: declared={expected_topics}, found={actual_topics}")
    for m, block in topics:
        loc = m.group(1)
        errors += _required_fields(block, TOPIC_FIELDS, loc)
        if _prose(block) < 300:
            errors.append(f"{loc}: superficial knowledge point, needs >=300 chars")

    errors += _required_fields(sections.get("例题精讲", ""), EXAMPLE_FIELDS, "例题精讲")
    homework = _entries(sections.get("分层作业", ""), Q)
    questions = [(m.group(1), m.group(2)) for m, _ in homework]
    if len(homework) < 5 or len(set(x[0] for x in questions)) != len(homework):
        errors.append("Homework requires >=5 unique numbered substantive tasks")
    for tier, count in (("基础", 2), ("应用", 2), ("挑战", 1)):
        if sum(1 for _, name in questions if name == tier) < count:
            errors.append(f"Homework tier {tier} requires >= {count} tasks")
    task_statements = []
    for m, block in homework:
        errors += _required_fields(block, TASK_FIELDS, m.group(1))
        if _prose(block) < 120:
            errors.append(f"{m.group(1)}: underspecified assignment (<120 chars)")
        statement_match = re.search(r"\*\*任务[：:]\*\*(.*?)(?=\*\*提交内容[：:]\*\*|$)", block, flags=re.S)
        if statement_match:
            norm = re.sub(r"[^\w\u4e00-\u9fff]", "", statement_match.group(1)).lower()
            norm = re.sub(r"\d+", "N", norm)
            task_statements.append((m.group(1), norm))
    for i, (a_id, a) in enumerate(task_statements):
        for b_id, b in task_statements[i+1:]:
            if min(len(a), len(b)) >= 35 and SequenceMatcher(None, a, b).ratio() > 0.92:
                errors.append(f"{a_id}/{b_id}: near-duplicate homework statement; number swaps do not count as original variety")

    answers = _entries(sections.get("答案与解析", ""), S)
    a_ids = [m.group(1) for m, _ in answers]
    q_ids = [q[0] for q in questions]
    if sorted(a_ids) != sorted(q_ids):
        errors.append(f"Missing/extra homework solutions: tasks={q_ids}, solutions={a_ids}")
    for m, block in answers:
        errors += _required_fields(block, ANSWER_FIELDS, m.group(1) + " 解析")
        if _prose(block) < 110:
            errors.append(f"{m.group(1)}: answer lacks >=110 prose characters")
    errors += _required_fields(sections.get("复习速览", ""), REVISION_FIELDS, "复习速览")
    return [str(path) + ": " + e for e in errors]


def check_student_course(root: Path) -> list[str]:
    config = root / "course.json"
    if not config.is_file():
        return ["Missing course.json"]
    data = _obj(config)
    errors = []
    if not isinstance(data.get("lessons"), list) or not data["lessons"]:
        return ["Missing lessons array"]
    for lesson in data["lessons"]:
        if not isinstance(lesson, dict):
            errors.append("Invalid lesson object")
            continue
        path = _path(root, lesson.get("path"))
        if path is None or path.suffix != ".md":
            errors.append("Unsafe lesson Markdown path")
            continue
        topics = lesson.get("topics")
        if not isinstance(topics, list):
            topics = []
            errors.append(str(path) + ": course.json topics array missing")
        topic_ids = []
        for t in topics:
            if not isinstance(t, dict) or not isinstance(t.get("id"), str) or not t.get("title"):
                errors.append(str(path) + ": invalid topic id/title")
            else:
                topic_ids.append(t["id"])
        if len(topic_ids) != len(set(topic_ids)):
            errors.append(str(path) + ": duplicate declared K topic IDs")
        errors.extend(check_lesson(path, topic_ids))
    return errors


def check_review_gate(root: Path, report: Path) -> list[str]:
    if not report.is_file():
        return ["Independent review report missing"]
    if report.resolve().is_relative_to(root.resolve()):
        return ["Private independent review report must be outside course output"]
    location = report.resolve().parent
    if any((ancestor / ".git").exists() for ancestor in (location, *location.parents)):
        return ["Private independent review report must stay OUTSIDE any Git worktree"]
    data = _obj(report)
    author = data.get("author_id")
    if not isinstance(author, str) or not author.strip():
        return ["Review report requires author_id"]
    records = data.get("lesson_reviews")
    if not isinstance(records, list):
        return ["Review report requires lesson_reviews array"]
    found = {r.get("lesson_path"): r for r in records if isinstance(r, dict)}
    issues = []
    for item in _obj(root / "course.json").get("lessons", []):
        rel = item.get("path")
        path = _path(root, rel)
        if path is None or not path.is_file():
            issues.append(f"{rel}: missing lesson for review")
            continue
        review = found.get(rel)
        if not isinstance(review, dict) or not isinstance(review.get("reviews"), list):
            issues.append(f"{rel}: missing review records")
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lesson_topics = [t.get("id") for t in item.get("topics", []) if isinstance(t, dict) and isinstance(t.get("id"), str)]
        lesson_questions = list(dict.fromkeys(Q.findall(path.read_text(encoding="utf-8")))) 
        question_ids = [q[0] for q in lesson_questions]
        seen_roles, seen_reviewers = set(), set()
        for r in review["reviews"]:
            if not isinstance(r, dict):
                issues.append(f"{rel}: invalid reviewer record")
                continue
            role, who = r.get("role"), r.get("reviewer_id")
            if role not in REVIEW_ROLES or role in seen_roles:
                issues.append(f"{rel}: unknown/duplicate reviewer role {role}")
                continue
            seen_roles.add(role)
            if not isinstance(who, str) or not who.strip() or who == author or who in seen_reviewers:
                issues.append(f"{rel}/{role}: reviewer must differ from author and other reviewers")
            else:
                seen_reviewers.add(who)
            if r.get("mode") not in ("subagent", "human"):
                issues.append(f"{rel}/{role}: require independent subagent or human mode")
            if r.get("status") != "PASS" or r.get("blocking_findings") != []:
                issues.append(f"{rel}/{role}: BLOCK / unresolved findings")
            if r.get("lesson_sha256") != digest:
                issues.append(f"{rel}/{role}: stale lesson digest")
            if not isinstance(r.get("evidence"), str) or len(r["evidence"].strip()) < 120:
                issues.append(f"{rel}/{role}: evidence must contain >=120 characters of concrete review findings")
            items = r.get("checked_items")
            if not isinstance(items, list):
                issues.append(f"{rel}/{role}: checked_items must list explicit review targets")
                items = []
            required = set(required_checks(role, lesson_topics, question_ids))
            missing = required - set(x for x in items if isinstance(x, str))
            if missing:
                issues.append(f"{rel}/{role}: incomplete audit coverage, missing {sorted(missing)}")
            if role == "assignment_integrity":
                question_checks = r.get("question_checks")
                if not isinstance(question_checks, list):
                    issues.append(f"{rel}/{role}: blind independent per-question checks required")
                else:
                    by_id = {q.get("id"): q for q in question_checks if isinstance(q, dict)}
                    if set(by_id) != set(question_ids) or len(by_id) != len(question_checks):
                        issues.append(f"{rel}/{role}: every assignment must have exactly one independent check")
                    for qid in question_ids:
                        q = by_id.get(qid, {})
                        if (q.get("blind_solved") is not True or q.get("compared_to_solution") is not True
                                or q.get("status") != "PASS"
                                or not isinstance(q.get("reasoning"), str) or len(q["reasoning"].strip()) < 60):
                            issues.append(f"{rel}/{role}/{qid}: missing blind solve, solution comparison, or concrete reasoning")
            if not isinstance(r.get("limitations"), list):
                issues.append(f"{rel}/{role}: missing limitations list")
        if set(REVIEW_ROLES) != seen_roles:
            issues.append(f"{rel}: missing independent reviewer roles: {sorted(set(REVIEW_ROLES)-seen_roles)}")
    return issues

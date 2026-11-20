# Student-first deep lesson standard / 学生讲义高密度规范

This is the canonical reader-facing contract. Private teacher-evidence analysis, intent hypotheses, source-rights ledgers, reviewer logs and agent workflow belong in internal metadata, never in a student's textbook.

## One lesson, one complete chapter
Use one lessons/Lxx/lesson.md for every class. The student must be able to start from zero, read explanations in order, practice without external files, and revise from a compact pocket inside this SAME chapter. Extra teacher guides and multi-lesson indexes are optional, not a substitute.

## Exact nine H2 headings, in order
1. 本课导读: a motivating concrete problem, why it matters, and study route; substantial introductory prose, not slogans.
2. 预备知识: explain prerequisite terms, symbols and assumptions with a small example for beginners.
3. 核心知识详解: every meaningful topic has an H3 in the form K01 · meaningful title, registered in course.json. Each K topic MUST have the labelled paragraphs **为什么要学：**, **直观理解：**, **准确规则：**, **逐步推演：**, **检查理解：** and substantive reasoning. Preserve the teacher's actually evidenced concept progression; add independent explanations instead of copying unlicensed text.
4. 例题精讲: original worked cases labelled **题目：**, **思路：**, **逐步推演：**, **结果：**, **验证：**, **变式：**; demonstrate the reasoning line by line, test edge cases and name assumptions.
5. 易错点与纠正: mistake, consequence, mechanism, corrected method and prevention. An observed wrong classroom example must be analyzed, never silently deleted; invented teacher intentions must not be asserted.
6. 分层作业: five or more meaningful original Q tasks; at least two 基础, two 应用 and one 挑战, each with 学习目标, 任务, 提交内容, 验收标准 and 提示. See assignment-module.md.
7. 深入理解: proof, invariants, limits, transfer, cross-lesson links or alternative method; discipline-specific rather than disconnected trivia.
8. 复习速览: compact headings 必会, 易错, 自测, 联系; questions are retrieval cues, not copied explanations.
9. 答案与解析: only after the tasks; Q01 etc each have 结论, 推理 and 错误辨析, with actual reasoning and verification.

## Hard editorial constraints
- A definition sentence is NOT enough. A knowledge point must explain why it is introduced, concrete intuition, exact conditions, intermediate steps, failure modes and how to apply it.
- No one-line knowledge explanations. No placeholder content, empty promises to expand later, circular answers or word-count padding.
- No premature answer spoilers before students attempt the homework.
- Student headings must NOT include 教师授课主线, 老师可能在想什么, 版权审核, 证据台账, 来源映射, 审计报告 or 内部生产流程. Real teacher insights may become naturally written examples and classroom tips without revealing private teacher evidence or claiming imagined intent.
- Real programming claims must distinguish C standard guarantees from implementation/platform behavior, plus compiler/options if relevant. Do not claim tests were run unless they were.
- Dense material should still be readable: paragraphs around explanations, expressive code comments, tables for true comparisons, optional ASCII diagrams, headings that reflect real concepts, not dozens of tiny files.

## Conservative static quality floor
The student-check CLI checks for nine sections in order, multiple fully explained knowledge units, worked-case labels, correct homework tiers and answer pairs, no placeholders/internal prose, and sizable NON-CODE explanations.

Defaults: full lesson >= 4000 non-code visible characters; core >= 1100; each K knowledge unit >= 300; worked example >= 420; error diagnosis >= 330; homework section >= 700; each Q >= 120; answers section >= 650; each answer >= 110; deep extension >= 240; revision pocket >= 230; intro >= 120; prerequisites >= 130. These are a FLOOR, not an arbitrary length target. Padding and false facts are rejected by independent semantic reviewers. A short lesson does not waive the requirements; supply deeper intuition, worked cases and practice.

An output is INCOMPLETE until BOTH static student-check and independently verified reviews in subagent-review.md PASS. Copyright publication is a different gate and never automatically passes.

---
name: course-organization
description: Build substantial, student-readable lesson chapters from authorized teacher materials. Preserve evidenced teaching logic, expand every major concept, create tiered homework and fully worked answers, support revision and optional authoritative research, and require independent quality and rights review. Use for course slides, notes, assignments, labs, exam preparation, or course updates.
license: MIT
compatibility: File-capable AI agent; optional Python 3.10+ offline CLI. Web research and true subagents require host support and authorization.
---

# Course Organization Skill / 课程资料整理与深度学习

## Non-negotiable result
**Produce a STUDENT textbook chapter, not a teaching-analysis report.** One class = one rich, coherent `lessons/Lxx/lesson.md`; do not split its concept explanation, examples, homework, mistakes, answers and revision into microfiles. Students must be able to learn from zero and revise from the SAME document.

**No shallow writing.** Explain every significant concept through motivation, intuitive model, precise conditions, step-by-step reasoning, misconception/edge cases and understanding checks. Include original, fully solved examples; at least 2 basic, 2 application and 1 integrative homework task, each with requirements, grading/acceptance conditions, hints and detailed answers. Repetition or padding is NOT depth. Read [student-edition](references/student-edition.md) and [assignment-module](references/assignment-module.md).

**Teacher-led, not copied.** An authorized, PRIVATE evidence map preserves actually observed lesson sequence, boardwork, emphasis, examples, mistakes, omitted transitions and intended teaching functions *when explicitly evidenced*. A guessed teacher intention stays a hypothesis in PRIVATE notes, not a student-facing claim. Never republish unlicensed instructor expression, figures, distinctive questions or private student data. Read [teacher-fidelity](references/teacher-fidelity.md) and [copyright-gate](references/copyright-gate.md).

**No self-approval.** To call lessons independently reviewed, obtain genuine independent child-agent reviews where supported, or human reviews, for all seven roles. The producing agent's sequential self-prompts do NOT count. If unavailable, provide the chapter and `REVIEW_PENDING` with a review plan. Read [subagent-review](references/subagent-review.md).

## Progressive references
Load only what the active task needs:
- Always: [student-edition](references/student-edition.md), [assignment-module](references/assignment-module.md), [copyright-gate](references/copyright-gate.md).
- Intake/planning: [workflow](references/workflow.md), [source-model](references/source-model.md), [teacher-fidelity](references/teacher-fidelity.md).
- Instruction: [subject router](references/subject-profiles.md), then ONLY the relevant [discipline profile](references/subject-profiles/); optionally [pedagogy](references/pedagogy.md).
- Online supplementation: [external discovery](references/external-discovery.md), only with actually available, authorized tools.
- Completion: [quality gates](references/quality-gates.md), [subagent-review](references/subagent-review.md).

## Workflow
1. **Permission and boundary.** Establish private/local vs public goal, authority to analyze teacher files, whether a third-party model may receive them, and rights to adapt/publish. Default to PRIVATE. When unclear, stop unauthorized transfer and restrict deliverables to safe original material.
2. **Inventory.** Scan authorized source metadata, identify sessions and course prerequisites. Only claim OCR or source-page knowledge if actually extracted and verified. Do not commit source files or private indexes.
3. **Private teacher map.** Account for each meaningful classroom item: demonstrated concepts, board steps, examples, mistakes, emphases and transitions. Record observed evidence, location, hypothesis vs fact and handling; do not invent the teacher's quotes, classroom speech or intentions.
4. **Lesson map and preview.** Match teacher-evidenced order to K knowledge IDs, LO outcomes, ACT teaching activities and ASM assessment IDs. Identify gaps/uncertainty and show proposed changes before any destructive rewrite.
5. **Choose subject method.** Computing focuses on prediction → state trace → verification → error repair; math on intuition → formal derivation/proof → counterexample; sciences on phenomena/model/evidence; humanities on claims and sources; languages on communicative input/output; engineering/economics on assumptions and tradeoffs. Do not force one subject's structure onto another.
6. **Research as permitted.** With an authorized browsing tool, look up official/current course specifications, released exam *types*, universities, peer-reviewed sources and rights-cleared OER for each LO. Record actually checked links, dates and licences; cite sources where needed. Official exams: LINK to the original unless actual reuse rights have been separately verified. Without browsing, output `NOT_SEARCHED` plans; never fabricate sources.
7. **Write each full chapter.** Follow the precise student nine-section contract (导读 → 预备 → 详解 → 精讲 → 纠错 → 作业 → 深入 → 速览 → 答案). Keep explanations and homework substantial, accurate, original and within the SAME chapter. Student text must not expose internal source mapping, licence reviews or guessed pedagogy.
8. **Hard deterministic checks.** Run `course-org validate` and `course-org student-check`. Missing paragraphs, unpaired answers, insufficient meaningful length, repeated number-swapped questions, or missing K topics → BLOCK/REWRITE. A static PASS never guarantees semantic quality.
9. **Strict independent review.** Run `course-org review-plan` for seven role-specific K/Q tasks and the current SHA-256. Delegate to genuine independent child agents or people with authorized access; homework reviewers solve every Q before reading draft solutions. Complete private reports, then run `course-org review-gate` and `course-org ready`. Any chapter change invalidates all previous review hashes. If no true reviewers, report `REVIEW_PENDING`.
10. **Release and update.** Public publishing is a distinct action requiring human review of actual expression/permissions/PII, and `course-org audit` on the safe manifest. Metadata PASS is not a legal guarantee. Update changed lessons and dependent work non-destructively. On every GitHub modification add a timestamped `docs/routine/` record: changed files, actual checks, blockers, next steps.

## Human-facing chapter contract
Exact H2 headings required by the current static checker:
`本课导读` · `预备知识` · `核心知识详解` · `例题精讲` · `易错点与纠正` · `分层作业` · `深入理解` · `复习速览` · `答案与解析`.

Within `核心知识详解`, title K01/K02 etc in source order and unpack WHY, intuition, exact rule, fully traced reasoning and understanding check. In homework require Q01–Q05 or more: 2 基础, 2 应用, 1 挑战. Answers go LAST with reasoning and error diagnosis. Follow [student-edition](references/student-edition.md) rather than rendering this internal contract into the student text.

## Optional local CLI (offline, no AI model/network access)
```bash
course-org scan /private/input --out /private/index.json
course-org validate examples/sample-course
course-org student-check examples/sample-course
course-org research-plan examples/sample-course
course-org review-plan examples/sample-course
course-org teacher-check /private/teacher-map.private.json
course-org resource-check /private/resource-registry.json
course-org review-gate COURSE_DIR --report /private/independent-review.json
course-org ready COURSE_DIR --report /private/independent-review.json
course-org audit COURSE_DIR --sources /private/source-manifest.json --teacher-map /private/teacher-map.private.json
```

The fictional example intentionally lacks independent reviewer approvals and public release rights. `review-gate` and `audit` should BLOCK when evidence is absent. These utilities check metadata and structure, not source truth, factual accuracy, actual child-agent execution, plagiarism or legal clearance.

## Stop conditions
- Illegal/unapproved teacher material processing or disclosure, private student data exposure.
- Copying teacher slides/images/questions or restricted exam contents without verified rights; superficial paraphrase/translation is not a workaround.
- Missing teacher evidence represented as observed; fabricated intention, citations, online checks or testing.
- Hollow one-sentence teaching, filler, homework without full reasoning, fragmented student materials.
- Author-agent self-certifying independent review; stale or synthetic review claimed as real; public release without approval.

# Mandatory independent child-agent reviews / 强制严格审计

The authoring agent may draft and self-diagnose but CANNOT approve its own student lesson. When the host supports child agents, DELEGATE seven isolated roles to actual independent child/subagents, ideally using different contexts and blind problem-solving. Where delegation is unavailable, human reviewers may fill those roles; serial prompts run by the same authoring agent are NOT independent approval. Never fake child-agent runs, permissions, tool use, or evidence.

## Seven distinct roles and instructions
1. teacher_coverage: privately compare authorized source ledger with the lesson for every meaningful topic, board jump, demonstration, error, emphasis and transition; report omissions and uncertain teacher-intent claims. Do not send private materials to unapproved providers.
2. novice_readability: inspect only the student lesson (and stated prerequisites), attempt the basic problems before reading solutions; detect unexplained jargon, leaps, shallow one-liners and overloaded sections.
3. subject_accuracy: independently check definitions, equations, computations, programming semantics, edge cases, limitations and references. Actually compile/run when available; otherwise explicitly NOT_RUN.
4. assignment_integrity: solve every Q task independently before consulting the answers; check progression, ambiguity, difficulty labels, originality, scoring and comprehensive solution explanations.
5. revision_usefulness: using only the revision pocket, reconstruct essential concepts and attempt retrieval; ensure it is short, navigable and correct.
6. rights_privacy: review permissions, teacher-protected expression, exam reuse, licensing, copied images, personal information and sharing restrictions; block public release on unresolved rights, even with excellent pedagogy.
7. adversarial: deliberately search for superficial padding, copied paragraphs, hallucinated teacher intent, fake sources, unsupported exam claims, missing cases, contradicting explanations, stale tests and other hidden defects.

## Reviewer output and compulsory gate
The PRIVATE JSON report contains author_id, lesson_path, reviews with seven roles and a UNIQUE reviewer_id per role. Each must have mode subagent or human, status PASS or BLOCK, current lesson_sha256, concrete evidence, checked_items, limitations and blocking_findings. A PASS must have no blocking findings. A self-authored report, repeated reviewer, missing role, stale hash, vague evidence, or any BLOCK means REWRITE / REVIEW_PENDING.

After ANY modification to the chapter, all previous review hashes are invalid and independent reviewers must review again. A reviewer must see the current version and specify the evidence checked.

CLI:
- course-org student-check COURSE_DIR: deterministic chapter density and homework gates, NOT semantic proof.
- course-org review-gate COURSE_DIR --report /private/independent-review.json: independent-review declaration and hash gate (still does not verify that reviewers truly executed their tasks).
- course-org ready COURSE_DIR --report /private/independent-review.json: combines structure, student content quality and independent review status; required before calling a lesson strictly reviewed.

If independent agents are not actually available, do static checks, produce a review task pack and mark REVIEW_PENDING rather than claim "seven subagents approved". Permission-checked human reviewers are acceptable; the main generating agent cannot substitute for them.

PUBLIC release separately requires the copyright/rights audit and explicit human authorization. High student quality does not license redistribution of teacher expression. Never promise zero copyright risk.

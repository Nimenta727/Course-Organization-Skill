---
name: course-organization
description: Create full, deeply explained student-ready course chapters from authorized teacher materials. Preserve evidenced teaching logic, build beginner and revision paths in one lesson, force tiered homework and complete answers, and require independent child-agent or human review plus copyright checks. Use for teaching slides, course notes, revision and assignments.
license: MIT
compatibility: Works with file-capable coding agents. Optional local Python 3.10+ helper; no network required.
---

# Course Organization Skill / 课程资料智能整理

## CRITICAL STUDENT OUTPUT AND INDEPENDENT REVIEW GATES
**The deliverable is a STUDENT TEXTBOOK CHAPTER, not a teacher research report.**
Read and enforce [student edition](references/student-edition.md), [assignment module](references/assignment-module.md), and [independent child-agent audit](references/subagent-review.md) for every lesson. Never settle for a one-sentence description of a knowledge point. Every meaningful concept needs why, intuition, precise rule, full step-by-step derivation and an understanding check. One lesson = one fully self-contained chapter, including homework and worked solutions.

Completion requires course-org student-check AND independent review-gate PASS; these checks are NOT optional. If child-agent delegation is unavailable, request independent human review and report REVIEW_PENDING; the author agent must never certify itself. Student chapter headings must not expose private evidence ledgers, rights reviews or guessed teacher intentions. Public release additionally requires explicit copyright/rights approval.

## Contract
**Teacher-fidelity takes priority:** Reconstruct every meaningful evidenced teaching element, including boardwork, error demonstrations, emphases and skipped reasoning, with honest observed-versus-inferred labels. Then enrich it with independently authored explanations and research. See references/teacher-fidelity.md. Keep any protected expression private unless publication rights are documented.

Organize **by lesson, not by file type**. A lesson is the primary readable unit; cross-lesson labs, assignments, exams, and teacher preparation are linked by learning-objective IDs. Do not merely summarize slides or create a forest of disconnected files. Use original explanations and examples.

**Safety-first publication rule:** Instructor-provided files are private reference material, NOT a grant to reproduce, translate, paraphrase closely, upload to a third-party model, or publish. Never auto-push raw uploads to GitHub. Never claim copyright is guaranteed safe. Consult [copyright-gate](references/copyright-gate.md) before processing and before any publication step.

## Progressive disclosure (read only what the current stage needs)
- Always: this file + [workflow](references/workflow.md) + [copyright-gate](references/copyright-gate.md).
- Student-facing lesson authoring: [student-edition](references/student-edition.md), [assignment-module](references/assignment-module.md), and [reading-and-depth](references/reading-and-depth.md).
- Independent strict review: [subagent-review](references/subagent-review.md); never self-approve.
- Private teacher evidence and interpretation: [teacher-fidelity](references/teacher-fidelity.md).
- Research and authorized exam links: [external-discovery](references/external-discovery.md).
- Planning or curriculum mapping: [pedagogy](references/pedagogy.md) + [source-model](references/source-model.md).
- Developing a particular lesson: read the routing table in [subject-profiles](references/subject-profiles.md), then load ONLY the matching subject reference.
- Reviewing or releasing: [quality-gates](references/quality-gates.md) + [source-model](references/source-model.md).
- Comparing other projects: [research ledger](references/open-source-research.md).

## Execution state machine
1. **INTAKE:** Determine learning audience, course scope and release target (local/private/public). Default to local/private. Identify teacher ownership/consent and any student records. If materials are restricted or permission is unclear, keep them in the controlled private input area and avoid uploading to external AI services.
2. **INVENTORY:** Enumerate files, formats, hashes and candidate lesson numbers. Preserve names and hashes only in local provenance. Extract text/images only with authorized, available tools. Never fabricate OCR, content or citations.
3. **RIGHTS TRIAGE:** For each source record permission, licence, original author, usage scope, licence evidence, and PII flags. Unknown rights are unknown, not public domain. No raw source files are copied into public outputs.
4. **MAP:** Produce a PRIVATE teacher evidence map accounting for meaningful teacher writing, diagram/board steps, emphasis, mistakes and questions. Record observed facts, plausible intentions as hypotheses with alternatives, missing reasoning, and the section where each item is addressed. Validate with teacher-check. Generate course objectives, lesson sequence, knowledge graph, source-to-lesson crosswalk, confidence levels A/B/C/D, and identified gaps. A = directly evidenced; B = corroborated inference; C = independently developed expansion; D = uncertain. Do not represent B/C/D as observed teacher speech.
5. **PLAN/PREVIEW:** Select discipline profile, prepare targeted authoritative research queries and separate teacher-evidenced core from external extensions. Show an ordered plan, expected file tree, proposed changes, copyright blockers, estimated model work and review checkpoints. Never silently replace existing content.
6. **DESIGN:** Backward design: observable outcome -> evidence/assessment -> instruction and practice. Map every objective to one activity and one assessment. Choose pedagogical approach by learning goal rather than using every method blindly.
7. **BUILD:** Load the student-edition contract and assignment-module. Make a fully explained, single-chapter student textbook, not a data-processing report. Include nine complete student H2 sections, per-topic K-ID reasoning, original worked examples, >=5 complete tiered Q assignments and detailed paired solutions; absolutely NO one-line knowledge-point writeups. Each topic must stand on its own for novices while supporting retrieval-based revision. For each lesson use the teacher-evidenced storyline, but never copy protected expression without permission. Write a single rich beginner-and-review document with on-page navigation, original deep explanations, omitted boardwork steps, observed/possibly intended mistakes with correction, multiple useful perspectives, verified external research, harder extensions and a concise recap. Write one complete lesson document per session with goals, prerequisites, original concept explanation, worked example, misconceptions, error demo, guided practice, independent practice, retrieval prompts and next-lesson bridge. Use separate course-level indexes for labs, assignments, exams, revision, and teacher notes. Keep source provenance private.
8. **VERIFY:** After drafting, run student-check; any substantive prose below the enforced threshold, missing key knowledge unit, vague assignments or answer gaps means REWRITE. Delegate seven genuinely independent child-agent reviewers (teacher, novice, fact, homework, revision, rights, adversarial) or seek independent human reviewers where subagents are unavailable. Run review-gate and ready against the latest file digests; never forge approvals or self-certify. For each meaningful evidence segment confirm reviewed handling or a declared blocker. Research real official exam specifications and released questions as LINK-ONLY by default and independently invent exam-style practice; never fabricate references or pretend offline lookup succeeded. Check private teacher-map and resource-registry metadata, then run structural, alignment, factual, code, accessibility, plagiarism-risk, licence, privacy and publication checks. Mark unverified claims and unresolved rights. Do not invent perfect audit results.
9. **RELEASE:** Public release requires explicit approval, a human-reviewed manifest, licence compatibility, citations/attribution when required, no private materials, and successful audit. Any missing evidence -> BLOCK publication and offer private output or original-from-scratch alternative.
10. **UPDATE:** Compare hashes and dependencies. Revise only affected lessons and related assessments; keep old content or a patch for review. When changing GitHub repos, write a dated docs/routine/YYYY-MM-DD-HHMM-summary.md containing change list, verification, blockers and next actions.

## Output contract
- Public course source of truth: course.json + lessons/Lxx/lesson.md.
- Each lesson contains: teacher-evidenced teaching order (without unlicensed expression); novice/revision reading routes; objectives and prerequisites; foundational and advanced original explanations; reconstructed missing steps; verified or explicitly uncertain error demonstrations; complementary explanations; guided and independent original exam-style practice; verified links; review pocket and retrieval prompts.
- Course-level: assignments/, labs/, extensions/, assessments/, teaching/, provenance/ (only **safe metadata**).
- Private working inventory and teacher uploads: outside public Git repository, default separate local directory.
- Source evidence is traced PRIVATELY as observed / inferred / AI-original. Student prose presents concepts naturally; do NOT label every paragraph with producer metadata, speculative teacher intent or copyright review. Never invent a quote, page number or permission.
- Deliver an actionable change summary, blocked items, limits, and next step.

## Local optional helper
- python -m course_org.cli scan INPUT --out LOCAL_PRIVATE_MANIFEST.json
- python -m course_org.cli validate COURSE_DIR
- python -m course_org.cli audit COURSE_DIR
- python -m course_org.cli teacher-check PRIVATE_TEACHER_MAP.json
- python -m course_org.cli resource-check RESOURCE_REGISTRY.json
- python -m course_org.cli research-plan COURSE_DIR  # produces queries, NOT web results
- python -m course_org.cli student-check COURSE_DIR  # hard depth and homework floor
- python -m course_org.cli review-gate COURSE_DIR --report PRIVATE_INDEPENDENT_REVIEW.json
- python -m course_org.cli ready COURSE_DIR --report PRIVATE_INDEPENDENT_REVIEW.json
These are metadata/validation utilities, not file-parsing or plagiarism detection systems. An audit PASS is **not** legal clearance.

## Hard failures
- Teacher originals or student data in a public commit.
- Slide-by-slide paraphrase, copied diagrams/questions/code without verified permission, or translation presented as original.
- Unsupported licence assumptions; assuming credit alone equals permission; claiming fair use guarantees republication.
- Missing review gate or release permission.
- Hallucinated lectures, citations, standards, references, or tests.
- Overfragmented files that require opening many fragments to study one lesson.

## Teacher-led enrichment: mandatory decision order
1. Start with evidenced teacher content and analyze EVERY meaningful writing/error/board step; record coverage in a private ledger.
2. Build one independently written, teacher-sequenced complete lesson; put expanded novice explanations immediately after the relevant concept.
3. Select discipline-specific methods and research each objective using live tools if authorized; cite actually checked reputable sources. If not searchable, mark NOT_SEARCHED.
4. Put deeper connections and official-exam reference links in the same chapter; published exercises must be original, never lightly reworded copies.
5. End with a compact, skimmable revision pocket in the same lesson, not a parallel fragmented course.
6. Preserve teacher characteristics as evidenced pedagogical features, NEVER as unsupported claims of teaching intention or unauthorized copyrighted expression.


## Role-based independent audit / 强制子智能体审计
The generator cannot sign its own work off. Seven independent contexts review coverage, novice clarity, subject truth, assignment solutions, revision usefulness, rights/privacy and adversarial weaknesses. Use true delegated child agents when supported, otherwise distinct humans. Semantic failures require rewrites regardless of token count. Review reports are private, keyed by SHA-256; content change invalidates old reviews. Never present self-review as subagent verification.

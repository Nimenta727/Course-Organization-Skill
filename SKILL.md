---
name: course-organization
description: Organize mixed course materials into a lesson-centered, evidence-grounded, copyright-conscious course project. Use for syllabi, lecture slides, notes, assignments, labs, assessments, curriculum redesign, or continuous course updates. Produces a source inventory, lesson map, original learning materials, assessment alignment, and a reviewable publication plan; never assumes permission to republish instructor materials.
license: MIT
compatibility: Works with file-capable coding agents. Optional local Python 3.10+ helper; no network required.
---

# Course Organization Skill / 课程资料智能整理

## Contract
Organize **by lesson, not by file type**. A lesson is the primary readable unit; cross-lesson labs, assignments, exams, and teacher preparation are linked by learning-objective IDs. Do not merely summarize slides or create a forest of disconnected files. Use original explanations and examples.

**Safety-first publication rule:** Instructor-provided files are private reference material, NOT a grant to reproduce, translate, paraphrase closely, upload to a third-party model, or publish. Never auto-push raw uploads to GitHub. Never claim copyright is guaranteed safe. Consult [copyright-gate](references/copyright-gate.md) before processing and before any publication step.

## Progressive disclosure (read only what the current stage needs)
- Always: this file + [workflow](references/workflow.md) + [copyright-gate](references/copyright-gate.md).
- Planning or curriculum mapping: [pedagogy](references/pedagogy.md) + [source-model](references/source-model.md).
- Developing a particular lesson: [subject-profiles](references/subject-profiles.md) for the relevant subject.
- Reviewing or releasing: [quality-gates](references/quality-gates.md) + [source-model](references/source-model.md).
- Comparing other projects: [research ledger](references/open-source-research.md).

## Execution state machine
1. **INTAKE:** Determine learning audience, course scope and release target (local/private/public). Default to local/private. Identify teacher ownership/consent and any student records. If materials are restricted or permission is unclear, keep them in the controlled private input area and avoid uploading to external AI services.
2. **INVENTORY:** Enumerate files, formats, hashes and candidate lesson numbers. Preserve names and hashes only in local provenance. Extract text/images only with authorized, available tools. Never fabricate OCR, content or citations.
3. **RIGHTS TRIAGE:** For each source record permission, licence, original author, usage scope, licence evidence, and PII flags. Unknown rights are unknown, not public domain. No raw source files are copied into public outputs.
4. **MAP:** Generate course objectives, lesson sequence, knowledge graph, source-to-lesson crosswalk, confidence levels A/B/C/D, and identified gaps. A = directly evidenced; B = corroborated inference; C = independently developed expansion; D = uncertain. Do not represent B/C/D as observed teacher speech.
5. **PLAN/PREVIEW:** Show an ordered plan, expected file tree, proposed changes, copyright blockers, estimated model work and review checkpoints. Never silently replace existing content.
6. **DESIGN:** Backward design: observable outcome -> evidence/assessment -> instruction and practice. Map every objective to one activity and one assessment. Choose pedagogical approach by learning goal rather than using every method blindly.
7. **BUILD:** Write one complete lesson document per session with goals, prerequisites, original concept explanation, worked example, misconceptions, error demo, guided practice, independent practice, retrieval prompts and next-lesson bridge. Use separate course-level indexes for labs, assignments, exams, revision, and teacher notes. Keep source provenance private.
8. **VERIFY:** Run structural, alignment, factual, code, accessibility, plagiarism-risk, licence, privacy and publication checks. Mark unverified claims and unresolved rights. Do not invent perfect audit results.
9. **RELEASE:** Public release requires explicit approval, a human-reviewed manifest, licence compatibility, citations/attribution when required, no private materials, and successful audit. Any missing evidence -> BLOCK publication and offer private output or original-from-scratch alternative.
10. **UPDATE:** Compare hashes and dependencies. Revise only affected lessons and related assessments; keep old content or a patch for review. When changing GitHub repos, write a dated docs/routine/YYYY-MM-DD-HHMM-summary.md containing change list, verification, blockers and next actions.

## Output contract
- Public course source of truth: course.json + lessons/Lxx/lesson.md.
- Each lesson contains: objectives; prerequisites; new explanations; step-by-step example; common errors; teacher-style teaching *approach* without reproducing unique wording; guided/independent practice; formative check; retrieval prompts; recap.
- Course-level: assignments/, labs/, extensions/, assessments/, teaching/, provenance/ (only **safe metadata**).
- Private working inventory and teacher uploads: outside public Git repository, default separate local directory.
- Every generated passage is marked as observed / inferred / AI-original expansion where applicable, with evidence traceable to a local manifest. Never invent a quote, page number or permission.
- Deliver an actionable change summary, blocked items, limits, and next step.

## Local optional helper
- python -m course_org.cli scan INPUT --out LOCAL_PRIVATE_MANIFEST.json
- python -m course_org.cli validate COURSE_DIR
- python -m course_org.cli audit COURSE_DIR
These are metadata/validation utilities, not file-parsing or plagiarism detection systems. An audit PASS is **not** legal clearance.

## Hard failures
- Teacher originals or student data in a public commit.
- Slide-by-slide paraphrase, copied diagrams/questions/code without verified permission, or translation presented as original.
- Unsupported licence assumptions; assuming credit alone equals permission; claiming fair use guarantees republication.
- Missing review gate or release permission.
- Hallucinated lectures, citations, standards, references, or tests.
- Overfragmented files that require opening many fragments to study one lesson.

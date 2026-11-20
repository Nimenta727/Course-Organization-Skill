# Quality gates / 质量验收标准

## Structural
- Lesson documents consolidated by lesson, not scattered by file type.
- Course directory has valid course.json, each referenced lesson file exists.
- Each objective states observable learning and maps to at least one activity and one assessment.
- A teacher can teach, and a learner can study, from each lesson.md without chasing fragments.
- Examples, practice and answers are internally coherent; run code and assertions whenever appropriate.

## Educational
- Backward-design alignment checked at objective level.
- Content starts from prior knowledge and provides original explanations, scaffolded practice, misconception repair, feedback and retrieval.
- Use correct discipline-specific pedagogy instead of copying the same generic format.
- Distinguish curriculum claims supported by teacher evidence (A/B) from AI expansions (C) and uncertain claims (D).
- Provide accessible text equivalents for meaningful images, navigable headings and alternative practice modes where possible.

## Factual and ethical
- No invented teacher quotations, page numbers, lessons, standards, citations, grade requirements or classroom events.
- No secret student assessment answers in publicly visible student handouts.
- Separate copyrighted/private originals from output.
- No copied figures, code, diagrams, teacher-specific distinctive prose or exam questions without rights.

## Publish: hard gates
- Correct source/release manifest, required human reviewer and explicit release intent.
- Unknown/restricted/ND rights never pass for adapted content; NC/commercial conflict never passes; SA licence conflicts never pass.
- All referenced assets have attribution/permission and privacy review; raw source expression in public content is blocked by default.
- Text similarity, complex rights and jurisdictional edge cases require manual review even when static checks pass.
- No auto-publication based solely on a machine PASS.

## Suggested scoring for author review (not automatic legal status)
- Coverage and accuracy: 30%
- Goal/activity/assessment alignment: 25%
- Worked examples/feedback/exercise quality: 20%
- Accessibility and learner fit: 15%
- Source traceability and consistency: 10%
This rubric assesses pedagogy only; copyright and privacy are independent veto gates.


## Teacher-centered & reader-centered hard gates
- All meaningful teacher source segments have a tracked handling decision, including boardwork, apparent errors, emphasis and missing transitions; no silent omissions.
- Teacher intention is explicit only with observed evidence; otherwise label a hypothesis with plausible alternatives or unresolved.
- Each lesson is one substantive standalone chapter with beginner and revision routes, complementary explanations where useful, corrected error cases, advanced extension and quick recall.
- No micro-file explosion; task orchestration may be granular, but reader output is unified.
- Each major independent addition is fact-checked and cited as appropriate; current official exam syllabus and source URLs are verified, or NOT_SEARCHED is declared.
- Link-only official exams are not copied. AI-created practice must be substantively original and independently checked.
- Teacher-fidelity scoring, subject-specific educational quality and legal permission remain SEPARATE dimensions.


## Mandatory student-focused acceptance (v0.2.2)
- student-check passes minimum non-code density, section ordering, knowledge-unit fields, worked example, 2+2+1 assignment levels and all Q answer pairings. Superficial one-liners are blocked.
- ready additionally requires every role from independent child agents or independent humans to PASS on the exact current SHA-256; stale/duplicate/self-review reports BLOCK.
- These mechanical checks cannot detect filler, wrong reasoning or copied protected expression, which independent reviewers must analyze from actual content.
- The student's nine sections MUST NOT include internal teacher-intent hypotheses, sources rights ledger or an agent review log. Student readability has priority; evidence stays private.

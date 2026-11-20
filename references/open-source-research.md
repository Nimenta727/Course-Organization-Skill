# Research ledger / 开源与教学方法研究记录
Research snapshot: 2026-11-20. Links are references, not dependencies or sources copied into this repository. All project-specific wording here is original.

| Reviewed project/source | Lesson adopted as a design principle | Implementation in this repository |
| --- | --- | --- |
| Learning Commons Agent Skills — https://github.com/learning-commons-org/agent-skills | Route by teaching task, subject-specific rules and review workflow | SKILL.md routing + subject-profiles.md |
| Gareth Manning Education Agent Skills — https://github.com/GarethManning/education-agent-skills | Evidence-grounded learning design and modular outcomes | pedagogy.md + quality-gates.md |
| Scibly Instructional Design Skills — https://github.com/twe-nextgen/skills | Didactic reduction, assessment design and editorial review | pedagogy decision rules, validation |
| idstack — https://github.com/savvides/idstack | Objectives -> assessments -> content -> audit chain | Objective/activity/assessment IDs and CLI validate |
| Coursewright — https://github.com/lars-derichter/coursewright | One course markdown source of truth, multiple derived outputs | canonical lesson.md; exporters planned |
| Anthropic Agent Skills — https://github.com/anthropics/skills | Small entrypoint with references loaded only when needed | SKILL.md + references |
| Agent Skills specification — https://agentskills.io/specification | Standard frontmatter and progressive disclosure | skill metadata and linked references |
| Microsoft MarkItDown — https://github.com/microsoft/markitdown | Convert approved formats to structured text | Optional future parser adapter; not bundled |
| MIT Teaching + Learning — https://tll.mit.edu/teaching-resources/course-design/where-to-start-backward-design/ | Reverse planning | Pedagogy and alignment rules |
| CMU Eberly — https://www.cmu.edu/teaching/assessment/basics/alignment.html | Match goals, activities and assessments | CLI objective validation |
| Stanford Teaching Commons — https://teachingcommons.stanford.edu/teaching-guides/foundations-course-design/theory-practice/instructional-design-framework | ADDIE full lifecycle | Workflow phases |
| CAST UDL 3.0 — https://udlguidelines.cast.org/ | Accessibility and learner agency | Lesson outputs and quality gates |
| Learning Scientists research — https://pmc.ncbi.nlm.nih.gov/articles/PMC5780548/ | Spacing, retrieval, interleaving, elaboration, concrete examples, dual coding | Lesson and revision requirements |
| Creative Commons — https://creativecommons.org/cc-licenses/ | Licence-specific reuse rather than generic attribution | Copyright gate and audit rules |
| US Copyright Office — https://www.copyright.gov/fair-use/ | Fair use is contextual; educational use is not automatic permission | Default block on rights uncertainty |
| UNESCO OER — https://www.unesco.org/en/open-educational-resources | Prefer genuinely reusable open resources | Rights triage and evidence tracking |

## Adoption policy
Study public design patterns and documented methodology, not proprietary source code, sample lessons, prompts or copyrighted project templates. Verify each third-party project's licence before copying any text/code (none copied here). External resources can change. This ledger is a bounded literature/repository review, not a claim to exhaust all educational methods on the Internet.

## What our skill adds
1. Per-lesson consolidation with original teaching materials instead of document-type fragmentation.
2. Two separately visible gates: educational quality and rights/privacy/publication.
3. Source evidence grades distinct from legal permission states.
4. Conservative private-by-default workflow and refusal to auto-publish unknown-rights content.
5. Low-token index/cache architecture and deterministic metadata validation.

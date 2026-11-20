# Teacher-led, research-enriched course architecture / 教师主线深度重建

## Goal
The course must be recognizable as the teacher's evidenced pedagogical journey while readable from scratch and useful for revision. AI does not substitute a generic textbook. It reconstructs reasoning, fills gaps, checks misconceptions, deepens explanations, creates independently authored exercises and cites vetted supplementary sources.

## Private evidence layer
A non-public per-item teacher ledger tracks all meaningful teacher writing, boardwork, errors, examples, concept links, emphasis, questions and transitions. Each maps to a chapter section, private-only rights restriction or explicit unresolved flag. Intent is an interpretation with evidence and alternatives, never automatically a fact.

## One reader-facing document per lesson
The canonical artifact is lessons/Lxx/lesson.md. Within that page: two reading routes, 30-second overview, detailed teacher-driven progression, missing-step explanations, multiple learning angles, error demonstration/correction, advanced context, graded practice and review pocket. Do not split a lesson into many tiny Markdown files to make model orchestration easier.

## Open source and authoritative supplementation
With appropriate tools, actively search sources by learning objective. Prefer official curricula/exam descriptions, universities, professional bodies and peer-reviewed/open educational resources. Verify actual source URLs, date, relevance and rights. Reference published official exam questions via links unless reuse permission is explicitly verified; make original exam-style exercises. If research not performed, return a NOT_SEARCHED plan.

## Discipline routing
See references/subject-profiles.md: dedicated profiles for computing, mathematics, sciences, humanities, language arts and economics/engineering. Every subject shares copyright/teacher-fidelity principles but uses its own proof, explanation, exercises and review patterns.

## Guardrails
Distinguish permission to consult privately from permission to transmit, adapt or publish. Fidelity of teaching goals does not authorize copied expressive arrangements or professor's proprietary questions and illustrations. Machine checks validate declared metadata; legal review and original-content inspection still require people.

## Version status
v0.2 implements the instruction workflow, new subject references, a richer lesson example, teacher evidence and source registry schema checks, and offline research-query planning. It does NOT yet parse PDF/PPTX into real teacher evidence or run live web searches from the CLI. Agent-driven browsing is conditional on tools and authorization.

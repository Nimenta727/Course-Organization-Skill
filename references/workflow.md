# Workflow and artifacts / 工作流程

## 0. Input boundary
Use a dedicated local-only directory for teacher originals, class recordings, student work and copyrighted third-party files. Before any external model/connector upload, identify that provider's data handling and ask for permission where appropriate. Never push these inputs into public repos, including as Git history, PR attachments or build artifacts.

## 1. Inventory and evidence
Generate a local inventory with SHA-256, extension, size, candidate lesson, and extraction status. For PDFs/PPTX/DOCX prefer approved local parsers (a converter such as MarkItDown can be evaluated, but is not installed or called by this skill). Record per claim:
- source ID and optional local page/slide reference when **actually observed**
- evidence class: A directly observed; B independently corroborated; C original educational expansion; D unresolved
- confidence and conflict notes

Do not infer the full content of inaccessible slides from filenames.

## 2. Planning output
Produce:
1. Course profile: audience, learning goals, duration, academic integrity requirements.
2. Per-lesson outline: lesson ID, title, goals, associated materials, gaps, source evidence grades.
3. Prerequisite graph, outcomes-to-assessments matrix and proposed workflow.
4. Privacy/licence status of each source; explicit publication blockers.
5. Preview of new, modified, untouched files and plan checkpoints.

Require plan acceptance before a destructive bulk rewrite. If approval is unavailable, create a non-destructive proposed folder or patch.

## 3. Lesson authoring
Single canonical lesson content first; avoid repetitive AI boilerplate. Use:
- lesson rationale, prior knowledge, measurable objectives
- thought-provoking prompt / problem
- explanation with original prose and bounded examples
- a worked solution or demonstration, including common error and repair
- scaffolded practice then independently assessed practice
- concept check with explanations
- retrieval prompts and link to next lesson
- optional teacher notes, accessibility alternatives, extensions

A full lesson should be useful standalone. Preserve course sequence while reorganizing only when pedagogically justified, not mechanically following source slide order. Separate factual teacher evidence from independently proposed teaching choices.

## 4. Assessment alignment
For each objective LO: at least one teaching activity ACT and assessment item A. Vary complexity, formative and summative balance; avoid simply changing numbers in copied teacher exam questions. Answer keys must be independently solved/checked and stored separately from student-facing material.

## 5. Validation and revision
Review source provenance, factual claims, alignment, code compilation where appropriate, UDL/accessibility, licence conditions, meaningful transformation and originality; report UNKNOWN rather than fabricated PASS. Run deterministic validators and create a review report. Limit rework to touched lessons plus dependencies.

## 6. Public repository release
Only safe, permission-cleared output files. No local inventory, teaching originals, private answer keys, class lists, facial images, email addresses or other personal data. A public-facing note states the output is independently written and distinguishes AI additions from teacher-sourced facts; no statement implies endorsement by an instructor.

## GitHub documentation
Every change includes dated docs/routine entry: timestamp, summary, files and behavioral changes, actual test evidence, risks and next plan. Keep documentation bilingual when serving an international audience.


## 7. Teacher-led deep reconstruction / 教师主线深化
After inventory, make a private coverage ledger of every meaningful teacher item, including apparent mistakes, omissions, boardwork, examples, questions and emphases. Mark intended purpose as explicit, hypothesized with alternatives, or unknown. A board slip may be accidental; never invent instructor intentions. The teacher's evidenced teaching order is the spine; AI originality and subject methods fill missing reasoning rather than replace the course.

Use references/teacher-fidelity.md and references/reading-and-depth.md. Each learner-facing lesson remains one complete chapter with novice and revision paths. Separate evidence ledger, caches, rights review and links are internal metadata.

## 8. Open authoritative enrichment / 权威材料自动补充
For each objective, formulate targeted official-exam/official-syllabus, university/OER and advanced research queries. If web tools exist and the use is authorized, actually browse and verify publisher/date/URL/relevance/licence, recording links in resource-registry.json. If no tool, create NOT_SEARCHED plan; never pretend to have performed research. Published questions are linked by default; AI-original tasks can mimic general cognitive demand but not protected expression. See references/external-discovery.md.

## 9. Discipline-sensitive rendering / 分学科生成
Choose one subject reference per lesson. Adapt how proof, debugging, experiment, interpretation, dialogue, or decision modeling is explained. Always retain the single-lesson narrative and review pocket.

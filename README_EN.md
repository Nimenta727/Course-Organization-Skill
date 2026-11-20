# Course Organization Skill

**v0.2.0 — research-informed, privacy-first foundation.** A lesson-centered Agent Skill for rebuilding mixed course materials into an original, coherent teaching and learning project.

## Teacher-led, discipline-aware and research-enriched
The teacher's verified sequence, emphases, boardwork and observed error demonstrations form the instructional backbone. Missing reasoning is independently reconstructed and the intended teaching purpose is labelled observed, hypothesized with alternatives, or unknown. Never invent teacher quotations or copy protected expression.

Every lesson is ONE substantial, readable Markdown chapter for both beginners and revision: orientation, teacher-led narrative, foundations, alternative explanations, corrected errors, advanced extension, original practice and compact retrieval.

The Skill uses approved live web tools, when available, to research authoritative curricula/exam requirements, universities, evidence-based methods and licensed OER per objective. Official exam questions are link-only by default. No browsing tool means a NOT_SEARCHED query plan, not invented source verification. Distinct disciplines route to dedicated profiles.

## Design
- One readable canonical lesson file per lesson, with activities and assessments linked by objective IDs.
- Pedagogy selection: backward design, alignment, ADDIE, Bloom, Merrill, 5E, PBL, retrieval and spaced practice, UDL 3.0 where relevant.
- Evidence labels distinguish direct source evidence, corroborated inference, independently generated enrichment and unknowns.
- Strong safeguards: teacher originals and student information remain private; no automatic publication, no near-paraphrase, no assumptions of permission.
- On-demand reference loading to reduce context waste and deterministic command-line metadata checks.

## Installation
~~~sh
python -m pip install -e .
course-org scan /private/source/folder --out /private/manifest.json
course-org validate examples/sample-course
course-org audit examples/sample-course
course-org research-plan examples/sample-course
# Teacher evidence and source audits (private manifests):
# course-org teacher-check /private/teacher-map.private.json
# course-org resource-check /private/resource-registry.json
python -m unittest discover -s tests -v
~~~

Audit intentionally blocks a project without explicit approval. The local utility **does not extract PDF/PPTX contents, detect plagiarism, access AI services, publish to GitHub or certify legal compliance**.

## Usage
Tell your agent to read SKILL.md and create a non-destructive plan first. Permission to view a source does not imply permission to republish it. Original course content, attribution and human rights review are required.

See [pedagogy](references/pedagogy.md), [copyright rules](references/copyright-gate.md), [implementation roadmap](docs/roadmap.md), and [research ledger](references/open-source-research.md).

## License
Repository-authored code and documentation: MIT (LICENSE). Teacher or third-party content is never relicensed by this repository.

## Additional references
- [Teacher fidelity](references/teacher-fidelity.md)
- [Readability and depth](references/reading-and-depth.md)
- [Authoritative source research](references/external-discovery.md)
- [Discipline routing](references/subject-profiles.md)
- [Design and limitations](docs/teacher-centered-design.md)

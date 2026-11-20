# Course Organization Skill

**v0.1.0 — research-informed, privacy-first foundation.** A lesson-centered Agent Skill for rebuilding mixed course materials into an original, coherent teaching and learning project.

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
python -m unittest discover -s tests -v
~~~

Audit intentionally blocks a project without explicit approval. The local utility **does not extract PDF/PPTX contents, detect plagiarism, access AI services, publish to GitHub or certify legal compliance**.

## Usage
Tell your agent to read SKILL.md and create a non-destructive plan first. Permission to view a source does not imply permission to republish it. Original course content, attribution and human rights review are required.

See [pedagogy](references/pedagogy.md), [copyright rules](references/copyright-gate.md), [implementation roadmap](docs/roadmap.md), and [research ledger](references/open-source-research.md).

## License
Repository-authored code and documentation: MIT (LICENSE). Teacher or third-party content is never relicensed by this repository.

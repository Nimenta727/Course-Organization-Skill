# Course Organization Skill

> **Keep the teacher's evidence-based instructional sequence; use AI to clarify, extend, verify and support revision.**
>
> Teacher-led · Lesson-first · Research-enriched · Copyright-aware

[简体中文](README.md) · [Quick start](docs/QUICKSTART.md) · [Installation](docs/INSTALLATION.md) · [User guide](docs/USAGE.md) · [Roadmap](docs/roadmap.md) · [Contributing](CONTRIBUTING.md)

**Version: v0.2.1 Preview** · Optional local CLI: Python 3.10+ · MIT for repository-authored code and documentation only.

Course Organization Skill is an [Agent Skill](https://agentskills.io/specification) that helps an AI agent transform **authorized** course materials into coherent, **one complete lesson per document** study resources. The teacher's evidenced topic order, emphasis, board reasoning and error demonstrations remain the backbone. The agent fills gaps with independently written explanations, alternate representations, original practice, and—when authorized web tools are available—verified authoritative references.

**Scope statement:** this release ships the Skill, modular pedagogy references, templates and a deterministic local metadata checker. It is **not** yet a standalone full-document PDF/PPT ingestion engine or end-to-end automatic course factory.

## What makes it different?

A conventional file organizer separates slides, worksheets, notes and exams by format. A generic AI summarizer may miss the actual classroom logic or erase useful error demonstrations. This Skill is lesson-centric and teacher-led:

**Observed teacher structure → evidence & gaps → original teaching narrative → subject-specific instruction → vetted enrichment → practice/revision → review.**

The reader gets a full chapter, not dozens of tiny files.

## Principles

1. **Teacher fidelity with evidence.** Preserve the demonstrated learning trajectory, concepts, emphases and misconception types. Label hypotheses about intent as hypotheses, never as quotations or facts.
2. **One lesson, one rich document.** Each `lessons/Lxx/lesson.md` carries prerequisites, teaching narrative, beginner explanations, steps, multiple useful viewpoints, corrected errors, deeper extensions, independent practice and recap.
3. **Two learning routes on the same page.** New learners can read sequentially; revising learners can skim the overview, key claims, pitfalls and retrieval questions.
4. **Subject-aware design.** Computing: runtime tracing and debugging. Math: derivation and proof. Science: models and evidence. Humanities: sources and arguments. Language: usage and feedback. Economics/engineering: assumptions and design trade-offs.
5. **Open, verifiable enrichment.** An equipped and authorized agent may research official syllabi, released exam specifications, reputable universities and licensed OER. Official exam materials are **linked by default**, not copied or superficially rewritten.
6. **Copyright and privacy veto.** Teacher originals, student data and rights manifests remain private. Public release is independent, explicitly reviewed and never presumed lawful from attribution alone.
7. **Progressive loading.** The entry skill points to references loaded by task, reducing irrelevant context. Automated dependency-driven regeneration is future work.

## Capability matrix

| Capability | State in v0.2.1 |
| --- | --- |
| SKILL.md and progressive references | Included |
| Teacher-evidence and error-analysis protocol | Documented + metadata checker; human review required |
| Six discipline-specific profiles | Included |
| Single-chapter beginner/revision template | Included |
| Metadata-only local input scan | Included |
| Objective/activity/assessment structural checker | Included |
| Rights/release declaration audit | Included; not a legal certification |
| Teacher-map and research-registry metadata checks | Included; records are not automatically truth-verified |
| Targeted source query planner | Included; offline only |
| Live web research | Conditional on the host agent's authorized tools |
| PDF/PPTX/DOCX full content extraction | Planned for v0.3 |
| Fully automated batch course writing | Planned for v0.4 |
| Visual dashboard and dependency-aware update engine | Future roadmap |

## Get started

~~~bash
git clone https://github.com/Nimenta727/Course-Organization-Skill.git
cd Course-Organization-Skill
python -m pip install -e .
course-org --help
course-org validate examples/sample-course
course-org research-plan examples/sample-course
python -m unittest discover -s tests -v
~~~

The CLI is optional; the Skill can be used by giving a suitable agent access to `SKILL.md`, `references/`, and `assets/`. See [installation instructions](docs/INSTALLATION.md) for Codex, Claude Code, general Agent Skills usage and platform notes.

Suggested prompt:

> Read Course Organization Skill. Begin by mapping the authorized teacher materials, lesson sequence, key boardwork and possible error demonstrations. Draft a non-destructive plan, provenance decisions and content preview first. Create rich single-document lessons with beginner explanations and a revision pocket. Research external authoritative references only using tools and rights I have authorized. Do not publish or upload original instructor files.

## Example output

~~~text
my-course/
├── course.json
├── README.md
├── lessons/
│   ├── L01/lesson.md
│   └── L02/lesson.md
├── assignments/          # optional linked multi-lesson tasks
├── labs/                 # optional
├── assessments/          # optional
└── provenance/
    └── release-manifest.json   # defaults to no public release
~~~

The [complete fictional sample lesson](examples/sample-course/lessons/L01/lesson.md) is independently authored for demonstration and is not derived from any real instructor materials. The [lesson template](assets/course-template/lessons/L01/lesson.md) shows the recommended sections.

## CLI commands

| Command | Purpose |
| --- | --- |
| `course-org scan INPUT --out /private/index.json` | Inventory filenames, extensions, sizes and hashes; no text extraction |
| `course-org validate COURSE_DIR` | Check lesson paths and declared outcome/activity/assessment links |
| `course-org research-plan COURSE_DIR` | Generate queries without browsing the web |
| `course-org teacher-check /private/teacher-map.private.json` | Check private source coverage metadata |
| `course-org resource-check registry.json` | Check declared resource/rights metadata |
| `course-org audit COURSE_DIR --sources /private/source-manifest.json --teacher-map /private/teacher-map.private.json` | Conservative pre-publication metadata gate |

`course-org audit examples/sample-course` is **expected to fail**: the sample does not authorize public release.

## Copyright, privacy and research

Owning, viewing or receiving a lecture slide does **not** automatically permit redistribution, external AI processing, derivative publication or copying protected figures/assignments. Preserve verified *teaching logic*, but independently author public expressions unless specific rights are documented. Published official exam material may still have restricted reuse; link it by default and produce genuinely original practice.

A local `audit` PASS checks declared metadata only. It **cannot guarantee zero infringement**, discover hidden personal information, or assess all legal permissions. A real human review of the content and rights is mandatory before any public release.

Read [copyright rules](references/copyright-gate.md), [teacher fidelity](references/teacher-fidelity.md) and [SECURITY.md](SECURITY.md).

## Documentation

| Topic | Document |
| --- | --- |
| First session | [Quick start](docs/QUICKSTART.md) |
| Platform setup | [Installation](docs/INSTALLATION.md) |
| Detailed workflows and commands | [User guide](docs/USAGE.md) |
| Teacher evidence | [Teacher fidelity](references/teacher-fidelity.md) |
| Dual-use course documents | [Readability and depth](references/reading-and-depth.md) |
| Research/exams | [External discovery](references/external-discovery.md) |
| Discipline routing | [Subject profiles](references/subject-profiles.md) |
| Pedagogy and review | [Pedagogy](references/pedagogy.md), [Quality gates](references/quality-gates.md) |
| Schemas and architecture | [Source model](references/source-model.md), [Architecture](docs/architecture.md) |
| Developer work | [Development](docs/DEVELOPMENT.md), [Contributing](CONTRIBUTING.md) |
| Limitations and next steps | [FAQ](docs/FAQ.md), [Roadmap](docs/roadmap.md) |
| Release record | [Release notes](docs/releases/v0.2.1.md), [Changelog](CHANGELOG.md) |

## Contributions, safety and license

Contributions are welcome via the [issue templates](.github/ISSUE_TEMPLATE). **Never attach private student records, copyrighted instructor course packs or unreleased examination papers to public issues.** Follow [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

The repository-authored code and documentation are [MIT-licensed](LICENSE). This does **not** relicense third-party educational content, private teacher materials or student work.

Each repository change should be documented in [docs/routine/](docs/routine/) with its date, changes, verification and next actions.

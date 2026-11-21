# Course Organization Skill

[![Unit tests and skill checks](https://github.com/Nimenta727/Course-Organization-Skill/actions/workflows/tests.yml/badge.svg)](https://github.com/Nimenta727/Course-Organization-Skill/actions/workflows/tests.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) ![Preview](https://img.shields.io/badge/release-v0.2.5%20Preview-orange)

**Teacher-led, student-first course organization. One complete, substantial lesson chapter for both first-time learning and revision.**

[中文](README.md) · [Docs hub](docs/INDEX.md) · [Quick start](docs/QUICKSTART.md) · [Install](docs/INSTALLATION.md) · [Guide](docs/USAGE.md) · [Release notes](docs/releases/v0.2.5.md)

**Current: v0.2.5 Preview.** This is a portable Agent Skill, plus an optional *offline* Python 3.10+ metadata/quality CLI. It is **not** a standalone PPT/PDF parser, autonomous course-writing server, browser, copyright-certification service, or subagent executor.

## Why lesson-first?

Traditional file sorters separate lectures, boardwork, worksheets and revision by file type. This project uses the instructor's **actually evidenced** learning sequence, emphasis, missing steps and misconception types as the *internal* planning source, while students receive an independently written, continuous course chapter that explains, demonstrates, corrects, practices and reviews.

Private teacher-intent speculation, original files, source-rights records and reviewer metadata are **not** student headings. Never invent instructor quotations or assume permission to upload or republish supplied materials.

## Student chapter contract: one lesson, one readable file

| Section | Required educational value |
| --- | --- |
| 本课导读 / Overview | Real motivating question, why this lesson matters |
| 预备知识 / Prerequisites | Refresh unexplained terms and novice foundations |
| 核心知识详解 / Deep explanations | For every K topic: **why → intuition → exact rule → worked reasoning → understanding check** |
| 例题精讲 / Worked example | Complete original problem, method, reasoning, result, verification and variant |
| 易错点与纠正 / Misconceptions | Error symptoms, cause, correction and prevention |
| 分层作业 / Tiered homework | At least **2 foundation + 2 application + 1 challenge** with full tasks, deliverables, acceptance criteria and hints |
| 深入理解 / Deepening | Proof, limits, edge cases, transfers or subject-appropriate connections |
| 复习速览 / Revision pocket | Key ideas, error cues, retrieval questions and links between concepts |
| 答案与解析 / Fully worked answers | Separate answers at the end, with reasoning and common wrong approaches for EVERY task |

Substantive explanations are mandatory: one-liners, padding, number-swapped duplicate questions or unexplained answers must be rewritten. The Python quality checker enforces a *minimum static floor*, not factual truth or real instructional depth. [Student standard](references/student-edition.md) · [Homework standard](references/assignment-module.md).

Subject-specific profiles cover **computing, mathematics, natural sciences, humanities, languages, and economics/engineering**. Programming uses predict → trace state → verify behavior → repair errors, whereas math uses stepwise proof, sciences use evidence and models, and humanities use source-based arguments. [Subject router](references/subject-profiles.md).

## Actual capabilities

| Capability | v0.2.5 |
| --- | --- |
| Full Agent Skill and selectively loaded pedagogy references | Included |
| Private teacher-evidence workflow and rights rules | Documented; structural metadata validation available |
| Dense single-chapter student output and example | Contract, template and fictional sample |
| Structural / lesson-depth / homework validation | Offline CLI included; cannot validate meaning |
| Seven-role independent-review plan | Offline role-specific K/Q checklist; **does NOT run reviewers** |
| Reviewer report validation and hash staleness checks | Included; cannot attest reviewer identity or work actually done |
| Private-first publication metadata audit | Included; not legal clearance |
| Curriculum and authoritative source search query plan | Included; `NOT_SEARCHED`, no internet access |
| Full PDF/PPTX/DOCX parsing, actual web research, full course generation | Require external authorized agent tools or future platform implementation |
| Built-in real subagent orchestration | Not implemented |

## Install: complete Skill versus CLI

**Agent Skill package:** Download the full `course-organization-skill-v0.2.5.zip` from [GitHub Releases](https://github.com/Nimenta727/Course-Organization-Skill/releases) if published, or clone the repository. The ZIP contains `SKILL.md`, `references/`, `assets/`, LICENSE and bilingual READMEs. Point a compatible agent to the extracted Skill directory.

**Optional Python CLI:** Install from the repository:

~~~bash
git clone https://github.com/Nimenta727/Course-Organization-Skill.git
cd Course-Organization-Skill
python -m pip install -e .
course-org validate examples/sample-course
course-org student-check examples/sample-course
course-org research-plan examples/sample-course
course-org review-plan examples/sample-course
python -m unittest discover -s tests -v
~~~

The wheel Release asset contains the CLI **only**, not the complete Skill. For installation paths and Windows setup see [INSTALLATION.md](docs/INSTALLATION.md).

`research-plan` does not browse; `review-plan` does not execute child agents. The fictional example intentionally fails the public-release audit and cannot pass a real independent-review gate without authentic reviewers.

## Suggested agent prompt

> Read the Course Organization Skill, then map authorized teacher materials privately, including observed sequence, omitted boardwork steps and possible error demonstrations. Show a non-destructive lesson plan first. Write one rich student chapter per class with novice-friendly explanations, carefully reasoned examples, at least five tiered original tasks, fully explained answers and a compact revision pocket. Use only licensed/authorized external research tools and actually verified references; link restricted official exam material instead of copying it. Run structural/depth checks; delegate genuinely independent reviewers if supported, otherwise report REVIEW_PENDING. Never publish instructor originals or student data.

## Strict review, source rights and publication

Seven distinct independent reviewers (genuine child agents or humans) assess instructor coverage, novice learning, factual claims, blind-solved homework, revision, privacy/rights and adversarial weaknesses. They must cover every assigned K/Q ID with concrete evidence, match the latest lesson digest and be distinct from the author. **A generated checklist or passing metadata report is not proof of completed review.**

Instructor materials and third-party education documents must not be uploaded, rewritten closely or published without the applicable rights. Official exam questions are linked rather than copied by default. Model and deterministic checks **cannot guarantee zero infringement**. Public distribution needs a separate human rights/privacy review. See [copyright gate](references/copyright-gate.md) and [security policy](SECURITY.md).

## Project documentation and community

[Docs index](docs/INDEX.md) · [Quick start](docs/QUICKSTART.md) · [Installation](docs/INSTALLATION.md) · [Usage](docs/USAGE.md) · [Development](docs/DEVELOPMENT.md) · [Architecture](docs/architecture.md) · [Roadmap](docs/roadmap.md) · [Release procedure](docs/RELEASE.md) · [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

The repository's original software/docs are MIT-licensed; teacher works, student data, and other third-party content are not relicensed. Each GitHub change is recorded in [docs/routine/](docs/routine/); superseded documents are retained via Git history, not redundant legacy directories.

**Verified publication:** The [v0.2.5 GitHub Pre-release](https://github.com/Nimenta727/Course-Organization-Skill/releases/tag/v0.2.5) includes the full Skill ZIP, CLI wheel and SHA256SUMS; [CI across Python 3.10/3.11/3.12](https://github.com/Nimenta727/Course-Organization-Skill/actions/runs/44864291167) passed, with 42 tests / OK reported on Python 3.11.

# Roadmap / 开发路线

## Delivered in v0.1.0 (2026-11-20)
- Fully revised SKILL.md: state machine, per-lesson consolidation, phase-specific reference files.
- Evidence-informed pedagogy matrix, subject profiles, alignments and research ledger.
- Rights/attribution/privacy release policy with conservative fail-closed audit.
- Standard JSON course/release schema, sample lesson, metadata-only scan, validation CLI and unit tests.
- Chinese and English entry points, dated maintenance journal, CI scaffold.

## Delivered in v0.2.0 (2026-11-20)
- Teacher-first source coverage rules for observed teaching order, boardwork, emphasis, errors, missing reasoning and uncertain intent.
- Complete dual-use lesson template: novice path + revision pocket in one document.
- Discipline-specific routing for computing, math, natural sciences, humanities, languages, economics and engineering.
- Agent-driven authoritative source search workflow (tool-dependent) and offline research-plan queries with NOT_SEARCHED state.
- Teacher evidence and researched resource metadata validators; strict link-only handling for official exam sources.
- Larger synthetic/independently authored sample, new tests and bilingual documentation.

## v0.3: approved document ingestion
- Local and opt-in parsers for PDF, PPTX, DOCX, images and zip; batch inventories and extraction reports.
- Source-by-page provenance and ambiguous lesson mapping preview.
- Rights evidence capture without leaking original content.

## v0.4: educational content authoring
- Agent-generated complete original lessons, labs, practice, extension and exams using verified objective map.
- Teacher-facing vs learner-facing document separation, original worked examples and independent answer validation.
- Evaluation suite on diverse synthetic and permission-cleared datasets.

## v1.0: production readiness
- Incremental dependency graph, content-hash cache and reproducible runs.
- Stronger semantic similarity and human approval workflow; code tests for generated coursework.
- Export to GitHub/Markdown/PDF/DOCX as permitted. Public release stays opt-in.

## v1.5–v2.0: optional platform
- Course tree, learning progress and edit-diff UI; controlled publish dashboard.
- Multi-course workspace, tool/model routing and token telemetry.
- LMS/document integration only with proper rights/privacy controls.

## Do not overclaim
v0.1 is an instruction-driven skill and deterministic validator, NOT a fully automatic course-authoring service, document parser or legal review solution.

## Important limits
The v0.2 CLI does not crawl the web, OCR files or independently verify a teacher's class. An online-capable agent can search if permission/tooling is present; every result needs source and rights verification. No zero-infringement promise.

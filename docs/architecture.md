# Architecture / 架构设计

## System boundaries
- Skill instructions (SKILL.md): agent policy and workflow, references lazy-loaded by stage.
- Deterministic CLI: scan local metadata, validate objective alignment, audit release metadata. No network or model call.
- Course source of truth: course.json + lessons/Lxx/lesson.md. Cross-lesson indices are optional; do not fragment each lesson.
- Local-only private inputs: teacher originals, private source permissions, student work and local provenance.
- Public release candidate: independently written lesson content plus redacted metadata; explicit rights and human review required.

## Stages and costs
INVENTORY -> RIGHTS TRIAGE -> COURSE MAP -> PREVIEW -> AUTHOR BY LESSON -> EDUCATIONAL QUALITY -> RIGHTS GATE -> HUMAN APPROVAL -> OPTIONAL PUBLISH -> INCREMENTAL UPDATE.
Only send relevant permitted excerpts to approved AI services, when allowed. Use hashes/metadata to avoid repeated analysis. No actual incremental engine implemented yet.

## Data and evidence
Source support A direct evidence, B corroborated inference, C original addition, D unknown; separate legal classifications OWNED, PERMISSION_PUBLIC, PUBLIC_DOMAIN, CC variants, UNKNOWN, RESTRICTED.
Objective map LO -> teaching activity ACT -> assessment ASM.
A static audit PASS means only that declared metadata is consistent with conservative checks; it cannot detect embedded copyrighted expression, factual errors or forged permissions.

## Threat model and mitigations
- Leakage of private lecturer/student files -> keep outside git; gitignore common paths; publish gate blocks binary inputs.
- Unauthorized derivative expression -> source licence gate, mandatory originality review and prohibition on close paraphrase.
- Hallucinated teacher lectures -> evidence grades and uncertainty.
- Too many model requests -> compact skill + on-demand references + future indexed extraction/cache.
- Incorrect answer keys -> independent validation and tests required in future.
- Machine audit overconfidence -> explicit reviewer and approval; no claim of legal certification.

## Future work
Parser adapters (MarkItDown/local PDF/PPTX), structured extraction, cross-course knowledge graph, selective regeneration, exporter adapters and optional UI. None of these are represented as implemented in v0.2.1.


## v0.2 extension: teacher spine and open learning research
- Private source evidence ledger with required handling for each meaningful teacher element and intentionality labelled explicit/hypothesized/unknown.
- Canonical rich lesson page for both novice and revision reading; separate resources remain machine data, not dozens of student pages.
- Discipline router loads only the matching profile and extends pedagogical logic.
- When an approved web tool exists, agent searches primary/official materials by objective, validates sources and rights, then enriches the same lesson; CLI itself only produces query plans.
- teacher-check and resource-check validate declarations, not the original classroom documents or reality of URLs.

# Changelog / 更新记录

本项目使用 `0.x` 预览版本号。旧的 README、未正式发布的版本说明草案、源文件的每次变更都可在 Git 历史中检索；完整开发审计轨迹保留在 [docs/routine/](docs/routine/)。

## [Unreleased]

- Real-world pilot on permission-cleared teaching materials.
- Secure optional document ingestion and actual independent agent/human review orchestration.

## [0.2.5] — 2026-11-21 (Preview patch)

- Corrected escaped Markdown inline-code markers throughout the active user and reference documentation, improving readability in GitHub and packaged Skill README files.
- Added an automated formatting regression test to prevent escaped inline-code delimiters from reappearing in active docs.
- Rebuilt the standalone complete Skill ZIP and independent Python CLI wheel as an immutable patch release, preserving v0.2.4 in its existing GitHub tag and Git history.

## [0.2.4] — 2026-11-21 (Preview)

- Unified the entry Skill and student-first course-design contract, removing redundant version-appendix instructions.
- Rewrote bilingual READMEs and user/developer/docs hub to reflect **current implemented functionality**, not old previews.
- Added an allowlist-only, reproducible **complete Agent Skill ZIP** builder and corresponding packaging tests, alongside the existing separate Python CLI wheel.
- Strengthened nine-section student chapter enforcement, K topic uniqueness and existing deep-homework quality checks.
- Removed superseded *draft* release-note files from the current tree; Git history still retains their exact content.
- Refreshed release process, current-version documentation, copyright/privacy constraints and repository metadata status.
- Prepared controlled v0.2.4 GitHub Pre-release with tests and artifact checks; actual release status must be verified on GitHub.

## Previous development milestones (not separate GitHub Releases)

- **0.2.3:** Strict role-specific K/Q audit planning, blind-solve homework declarations and duplicate-question regression tests.
- **0.2.2:** Deep single-lesson student chapter template, 2+2+1 homework, answer checks and seven-role independent review report format.
- **0.2.1:** Bilingual docs, GitHub issue templates, Topics/labels, CI and packaging groundwork.
- **0.2.0:** Teacher fidelity, differentiated subject teaching, safe authoritative research workflow.
- **0.1.0:** Initial Agent Skill, private source rights and metadata-only CLI.

Earlier patch text is accessible through Git history; the current docs focus on v0.2.4 rather than maintaining parallel archives. **Machine validation is not independent reviewer execution or copyright clearance.**

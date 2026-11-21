# Repository instructions for coding agents

Read [SKILL.md](SKILL.md) for the course-authoring behavior; this file governs repository maintenance.

1. **Current source of truth:** Keep only the active v0.2.4 Preview docs and release instructions in the main tree. Preserve superseded draft documents through Git history, NOT duplicated legacy/archive directories. Retain all \`docs/routine/\` chronological maintenance records.
2. **Student product:** One substantive \`lessons/Lxx/lesson.md\` per class, with novice explanation, original worked example, mistakes, 2+2+1 homework and full answers plus revision. Do not expose internal teacher-intent inference and review logs as student chapter headings.
3. **Privacy and copyright:** Never commit teacher originals, proprietary assignments, student data, private rights/teacher maps or independently reviewed reports. Rights uncertainty blocks public reuse; machine PASS is not legal clearance.
4. **Real capability boundaries:** The CLI doesn't browse, OCR PDFs/PPTs, run large language models or spawn subagents. Do not claim real external research, child-agent execution or scientific correctness from synthetic metadata tests.
5. **Testing:** When modifying behavior, update deterministic tests and examples. Run/verify CI for Python 3.10–3.12, sample lesson validation, student-check and complete Skill ZIP / CLI wheel builds.
6. **Docs:** Keep \`README.md\` / \`README_EN.md\`, \`docs/INDEX.md\`, \`docs/USAGE.md\`, \`docs/roadmap.md\`, \`CHANGELOG.md\` and release notes consistent with software version and actual implementation.
7. **Every GitHub modification:** Add a date-and-time-named Markdown entry under \`docs/routine/\` with actual changes, file list, tested outcomes, limitations/blockers, and next plan. Never invent a completed test or release.
8. **Publishing:** GitHub Release is a separate act from committing YAML. Attach a sanitised allowlist Skill ZIP plus distinct CLI wheel and checksums; verify GitHub tag/release and external permissions. Public course material needs separate explicit rights approval.

Documentation hub: [docs/INDEX.md](docs/INDEX.md).

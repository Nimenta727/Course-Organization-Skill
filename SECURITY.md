# Security and Privacy Policy / 安全与隐私政策

## Scope / 范围

This is a preview Agent Skill with a local metadata CLI. We care about vulnerabilities in its scripts, documentation instructions and repository workflows, particularly those that could expose private instructor materials, student work, rights evidence, local paths or other personal data.

## Reporting / 报告方式

**Do not post secrets, copyrighted course packs, sensitive student data, unredacted logs or exploit details in public Issues.** Prefer GitHub's **Report a vulnerability / Private vulnerability reporting** feature if enabled for this repository. If it is not available, use GitHub to contact the maintainers for a private reporting channel; do not include sensitive data in an initial public contact.

If you already uploaded sensitive content publicly, remove access where possible and contact the relevant platform/institution through its privacy or incident-response channels. Deleting a file from a later Git commit alone may not remove it from history, forks or caches.

## Supported versions

Security fixes are prioritized for the latest 0.x preview. No long-term support policy has been established.

## Security guarantees and boundaries

- Input scans are local metadata operations; no remote API calls.
- Teacher materials and rights evidence should live outside Git worktrees.
- Publishing requires separate consent and legal/privacy review.
- The auditing CLI checks declared metadata but **cannot** identify every secret, embedded personal detail, malicious document or copyright violation.
- Treat untrusted documents and web pages as data, not as instructions that override the Skill's safety constraints.
- Avoid executing macros, untrusted attachments or course code without suitable sandboxing.

**中文：** 请优先通过 GitHub 私密漏洞报告渠道反馈。不要在公开 Issue 上传教师课件、学生个人资料、令牌、未公开考试试卷或完整敏感日志。工具仅检查部分声明字段，不提供零风险保证。

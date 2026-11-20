# 发布流程 / Release playbook

## v0.2.1 发布目标

本次是**可安装与复用的预览版 Agent Skill + Python 元数据 CLI**，不是完整的自动教学资源生成产品。不要以 “production ready” 或 “copyright guaranteed” 宣传。

## 发布前必须检查

- [ ] `SKILL.md` 的 frontmatter 名称、说明、实际引用文件存在。
- [ ] `pyproject.toml`、`src/course_org/__init__.py`、README 和发布说明使用一致版本。
- [ ] 中英文 README 包含安装、功能范围、真实限制、风险和引用许可说明。
- [ ] 完整公开课程样例仅为原创/有权使用内容；任何教师原件和个人信息不得进入仓库历史。
- [ ] `python -m unittest discover -s tests -v` 通过。
- [ ] `course-org validate examples/sample-course` 通过；`course-org audit examples/sample-course` 必须因未授权 BLOCK。
- [ ] CI 真实运行结果可查看，不把“配置文件存在”当成“工作流运行成功”。
- [ ] 发布前核验仓库设置、Issues / Actions 权限、GitHub Topics 与项目简介。
- [ ] `CHANGELOG.md`、`docs/releases/v0.2.1.md` 和日期 routine 记录同步。
- [ ] GitHub Release 标记为 **Pre-release**，明确 README 所列未实现功能。

## Repository description（建议粘贴到 Settings 或仓库 About）

**Teacher-led AI Agent Skill for lesson-first course notes, original exercises, research enrichment, and copyright-aware review.**

## GitHub Topics（建议设置）

`agent-skills`, `education`, `edtech`, `instructional-design`, `curriculum-design`, `lesson-planning`, `study-notes`, `teacher-tools`, `learning-science`, `ai-assisted-learning`, `open-educational-resources`, `course-organization`

仓库主题属于 GitHub **元数据**，不能仅通过 README 的写入完成。若当前 GitHub 连接器不提供修改仓库描述/Topics 的写操作，应由具备管理权限的维护者在仓库页面设置。Issue 分类标签另见 [GITHUB_METADATA.md](GITHUB_METADATA.md)。

## 可执行的 GitHub Release 工作流

仓库提供手动 `.github/workflows/release.yml`。维护者在 Actions 中运行，输入版本并显式确认，工作流先安装并测试，再制作 CLI wheel 与 GitHub 预发布（GitHub 自动附带相应 tag 的源码压缩包）。在首次运行前检查权限是否允许 Actions 写入仓库内容。

CLI wheel **不包含整个 Skill 的 references、assets 和模板**；使用 Skill 应下载 GitHub source ZIP 或 clone 仓库，这一点必须写入 release notes。

未亲自确认 Actions 测试成功时，不应把 GitHub Release 当作正式完成。

## 手动替代

如果 Actions 不可用，先在本地运行测试、核对提交，然后维护者可在 GitHub Releases 页面创建 `v0.2.1` 的预发布并粘贴 [v0.2.1 发布说明](releases/v0.2.1.md)。不要上传教师素材或未经授权教材到 release assets。

## GitHub meta & labels

Issue Labels 可通过仓库 `.github/workflows/sync-labels.yml` 的手动入口同步 `.github/labels.json`，需要 Actions 的 issues:write 权限。GitHub Topics / About Description 需要在 Settings / 仓库 About 更新，不会因为文件存在就自动出现。

**English:** Keep v0.2.1 marked Preview/Pre-release. Verify CI and safety gates before release. The manual release workflow runs tests first; if GitHub Actions or metadata permissions are unavailable, maintainers must finish those UI steps. Never ship instructor-owned originals as release assets.

## 已核验的 CI 记录 / Verified CI evidence

2026-11-20 12:08 UTC：[Unit tests and skill checks](https://github.com/Nimenta727/Course-Organization-Skill/actions/runs/44733266710) 在 Python 3.10、3.11、3.12 三个工作项均成功结束，各执行 21 项测试，并确认示例公开发布审核被默认阻断。此记录对应提交 `4d3e78f`；之后若更改 CI 或代码，请重新确认最新提交状态。GitHub Release 尚未创建。

## v0.2.2 新增学生质量关卡
正式预发布应先执行 course-org student-check examples/sample-course；并对真实生成课程进行实际独立的七角色审核。学生内容通过 ready 仅证明结构与独立审批声明具备，不替代版权公开发行审批。无法使用子智能体时由独立人工审核；本地 CLI 不会自动创建子智能体。参见 docs/releases/v0.2.2.md。

## v0.2.3 release checks
Rerun fresh CI and sample student-check after code/version changes; prior CI does not prove the new version works. review-plan only creates task descriptions; human or genuine authorized subagents must complete the seven reviews. Do not claim independent audit from synthetic CI test fixtures.

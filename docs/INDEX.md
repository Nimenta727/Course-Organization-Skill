# 文档总览 / Documentation hub

> **当前有效版本：v0.2.4 Preview。** 旧的未正式发行版本说明可通过 Git 提交历史查看；此目录只保留当前操作性文档。 `docs/routine/` 始终保留开发审计轨迹。

## 给使用者

| 目的 | 文档 |
| --- | --- |
| 了解项目定位与功能边界 | [中文 README](../README.md) · [English README](../README_EN.md) |
| 快速试用虚构课程 | [快速开始](QUICKSTART.md) |
| 在 Agent / Codex / Claude Code 安装 | [安装指南](INSTALLATION.md) |
| 创建深入、可复习的一课一篇讲义 | [完整使用流程](USAGE.md) |
| 解决常见问题 | [FAQ](FAQ.md) |
| 教师课件与学生讲义的关系 | [教师主线与学生呈现](teacher-centered-design.md) |

## 给课程设计者和审阅者

| 阶段 | 规范 |
| --- | --- |
| 学生正文质量与章节结构 | [Student edition](../references/student-edition.md) |
| 作业与完整答案 | [Assignment module](../references/assignment-module.md) |
| 教师资料证据与误区 | [Teacher fidelity](../references/teacher-fidelity.md) |
| 学科差异化 | [Subject router](../references/subject-profiles.md) |
| 权威在线资料与考试要求 | [External discovery](../references/external-discovery.md) |
| 独立子智能体/人工审阅 | [Independent audit](../references/subagent-review.md) |
| 来源、版权和隐私 | [Copyright gate](../references/copyright-gate.md) |
| 格式化数据 | [Source model](../references/source-model.md) |

## 给开发和维护者

[架构](architecture.md) · [开发与测试](DEVELOPMENT.md) · [路线图](roadmap.md) · [发行手册](RELEASE.md) · [GitHub 设置](GITHUB_METADATA.md) · [当前版本说明](releases/v0.2.4.md) · [维护记录](routine/) · [变更日志](../CHANGELOG.md)

## 目录约定

```text
SKILL.md                      Agent 工作入口
references/                   教育、来源、质量、隐私、审阅的具体规范
references/subject-profiles/  六类学科差异化规范
assets/course-template/       学生课程模板（须补全才能验收）
examples/sample-course/       无教师原件的原创、可验证示例
src/course_org/               Python 离线元数据和质量门禁
scripts/package_skill.py      构建可直接安装的完整 Skill ZIP
tests/                        unittest 回归测试
docs/                         当前文档；routine 为长期开发审计记录
```

**English:** This is the canonical documentation index for v0.2.4 Preview. Historical drafts are preserved by Git history instead of a parallel legacy folder. The Skill creates reader-facing lessons; private source/provenance and review data remain separate. The offline CLI cannot browse, parse full PPT/PDF content or run subagents.

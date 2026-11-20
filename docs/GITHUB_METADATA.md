# GitHub 元数据、Topics 与 Issue Labels

## 仓库 Description

复制以下英文简介进入 GitHub 仓库右上角 About 编辑入口：

> Teacher-led AI Agent Skill for lesson-first course notes, original exercises, research enrichment, and copyright-aware review.

## Topics

在仓库 About → 设置齿轮图标（或相应的编辑入口）中设置以下 12 个 GitHub Topics：

- `agent-skills`
- `education`
- `edtech`
- `instructional-design`
- `curriculum-design`
- `lesson-planning`
- `study-notes`
- `teacher-tools`
- `learning-science`
- `ai-assisted-learning`
- `open-educational-resources`
- `course-organization`

这些是建议的分类标签；**仓库 metadata 是否已生效必须通过 GitHub 页面确认**。

## Issue Labels

Issue 标签定义文件：[`.github/labels.json`](../.github/labels.json)，包含类型（bug/feature/docs）、负责模块（Skill/CLI/教学/版权/外部研究/测试）、优先级、状态及社区协作标签。

手动同步方法：进入 GitHub Actions → **Sync issue labels** → Run workflow。该流程使用仓库的 `GITHUB_TOKEN` 和 `issues: write`；如果 Actions 被关闭或令牌权限受限，请维护者在 GitHub Issues → Labels 页面手动创建。

注意：GitHub 的 **Topics** 是仓库发现标签，**Issue labels** 是问题/任务分类，两者不是同一系统。单纯提交 JSON 和工作流并不代表 GitHub 已设置。

## 推荐发布版本

首次完整整理后的文档版本：`v0.2.1`（**Pre-release**）。参见 [发布流程](RELEASE.md)。不要将 “v1.0 正式版” 用作当前功能状态。

**English:** Repository description/topics are GitHub metadata and require an account-authorized edit, not just a committed file. Issue labels are declared in .github/labels.json and can be created via the manual Sync issue labels workflow when Actions permissions allow it. This project remains a v0.2.1 preview.

# Course Organization Skill · 教师主线课程整理

[![Unit tests and skill checks](https://github.com/Nimenta727/Course-Organization-Skill/actions/workflows/tests.yml/badge.svg)](https://github.com/Nimenta727/Course-Organization-Skill/actions/workflows/tests.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) ![Release](https://img.shields.io/badge/release-v0.2.4%20Preview-orange)

**让教师的课程成为知识主线，让 AI 负责补全推理、深入讲解、设计作业和形成复习材料。最终交付给学生的不是资料分析报告，而是每节课一篇真正能读、能学、能练、能复习的完整讲义。**

[English](README_EN.md) · [文档中心](docs/INDEX.md) · [快速开始](docs/QUICKSTART.md) · [安装](docs/INSTALLATION.md) · [使用指南](docs/USAGE.md) · [版本说明](docs/releases/v0.2.4.md)

> **当前版本：v0.2.4 Preview（预览版）。** 这是可供具备文件访问能力的 AI Agent 使用的 Skill，另附可选 Python 离线 CLI。CLI **不会自行读取 PPT/PDF 全文、访问网络、调用大模型或启动子智能体**；这些能力取决于实际 Agent 工具与使用授权。详见下方功能状态。

## 为什么与普通资料整理不同

课程学习不应该先打开一份 PPT、再寻找几张板书、跳到另一份笔记、最后对照散落的习题答案。这个 Skill 的产物以**课次**为中心：保留老师真实且可核实的教学顺序、强调和错误类型，然后补足新手需要的前置知识、推演和直观解释，提供真正的分层作业、完整答案及考前速览。

它在内部处理教师课件与引用权限，但**不把“老师可能在想什么”“证据台账”“审核记录”混进学生正文**。只在有合法处理和发布权限时引用原有表达；对公开用途，优先独立编写例子、说明和新题。

## 学生的一节课：完整而不碎片化

一节课只要求学生阅读一篇 \`lessons/Lxx/lesson.md\`，按照以下九个层次展开：

| 内容 | 要达到的阅读效果 |
| --- | --- |
| 本课导读 | 这课解决什么实际问题、为什么需要学 |
| 预备知识 | 补齐术语与必要基础，不能一句“自行复习”带过 |
| 核心知识详解 | **为什么学 → 直观理解 → 准确规则 → 逐步推演 → 检查理解**；每个重要知识点必须完整展开 |
| 例题精讲 | 具体题目、思路、过程、结果、验证和变式 |
| 易错点与纠正 | 错误表现、根源、修复方法与防错手段 |
| 分层作业 | 至少 **2 基础 + 2 应用 + 1 挑战**，每题提供完整任务、提交内容、验收标准与提示 |
| 深入理解 | 原理、边界、证明、性能或跨课联系 |
| 复习速览 | 必会、易错、自测和知识联系，支持考前快速回忆 |
| 答案与解析 | **每道作业**的结论、逐步推理与错误辨析，置于讲义末尾，先练后看 |

不是“写够 4,000 个字就过关”：静态内容密度只是**底线**，堆砌废话、重复改数字出题或未经核对的论断会被严格审阅者否决。详情：[学生正文规范](references/student-edition.md) · [强制作业规范](references/assignment-module.md)。

**分学科而非一个模子：** 编程课采用预测 → 状态/内存追踪 → 运行验证 → 错误修复；数学课重推导、条件与证明；科学课重现象、模型与证据；人文课重来源与论证；语言课重理解、表达与反馈；经济和工程课重约束、假设、计算与取舍。[查看全部学科规范](references/subject-profiles.md)。

## 最新功能状态

| 能力 | 当前状态 |
| --- | --- |
| 完整 Agent Skill 及按需加载的参考规范 | 已实现 |
| 教师内容证据映射与课程保真工作流 | 已定义，元数据可检查；真实来源需 Agent/人工核对 |
| 九段式完整学生讲义、强制知识讲解、作业与答案 | 规范、模板和静态检查已实现 |
| 原创编程课示例 | 已提供；未基于任何真实教师课件 |
| \`scan\` 本地哈希/文件名清单 | 已实现，不提取文档正文 |
| \`validate\`、\`student-check\` 和 \`audit\` | 已实现确定性结构/声明门禁，不证明学术或法律正确 |
| \`review-plan\` 七角色审阅清单、\`review-gate\` 和 \`ready\` | 已实现离线规划及报告字段/哈希检查；**不会执行子智能体** |
| \`research-plan\` 权威资料检索计划 | 已实现离线查询，标记 \`NOT_SEARCHED\` |
| 实际在线检索、课程文档解析、生成课件内容 | 依赖宿主 Agent 的工具与授权；独立 CLI 尚不支持 |
| 真正的子智能体调度、实时 OCR/解析、全课程自动生成平台 | 尚未实现，见[路线图](docs/roadmap.md) |

## 安装与首次运行

### 获取完整 Skill（推荐）

从 [Releases](https://github.com/Nimenta727/Course-Organization-Skill/releases) 获取带版本号的 \`course-organization-skill-v0.2.4.zip\`（如已发行），解压后得到具有 \`SKILL.md\`、\`references/\`、\`assets/\` 的完整 Skill 目录；也可以直接克隆：

~~~bash
git clone https://github.com/Nimenta727/Course-Organization-Skill.git
cd Course-Organization-Skill
~~~

在支持 Agent Skills 的客户端中安装**完整目录**，或显式让 Agent 读取 \`SKILL.md\`。Codex、Claude Code、Windows 及一般文件型 Agent 的安装路径见[安装指南](docs/INSTALLATION.md)。

### 可选：本地 Python 质量工具

要求 Python 3.10+：

~~~bash
python -m pip install -e .
course-org validate examples/sample-course
course-org student-check examples/sample-course
course-org research-plan examples/sample-course
course-org review-plan examples/sample-course
python -m unittest discover -s tests -v
~~~

\`research-plan\` 和 \`review-plan\` **只生成计划**，不会联网或实际调用七个子智能体。提供的虚构示例没有真实独立审阅记录，也未获公开审批，因此以下命令应当 **BLOCK**：

~~~bash
course-org audit examples/sample-course
course-org ready examples/sample-course --report /private/nonexistent-review.json
~~~

### 给 Agent 的实用指令

> 请使用 Course Organization Skill 分析我有权让你处理的课程资料。先建立私有教师内容覆盖映射，核对课次顺序、板书跳步、错误示范及重点，并展示制作计划。按学生可读的九段式结构，每节课生成**一篇详尽完整的讲义**：逐知识点讲清动机、直觉、准确规则、推演、自检，独立设计至少两道基础、两道应用和一道挑战作业，附全部答案解析和复习速览。选择适合学科的教学方法；有授权和真实联网工具时查证外部权威资料，官方真题默认只给原站链接。写完先执行静态检查，随后真正委派独立审阅者逐项验证；没有独立审阅时如实返回 REVIEW_PENDING。不要把教师原件或学生私有资料上传/公开。

## 课程成品与两种发行物

~~~text
course/
├── course.json
└── lessons/
    ├── L01/lesson.md    # 第1课完整学生讲义
    └── L02/lesson.md    # 第2课完整学生讲义
~~~

跨课实验、课程项目可以额外提供链接，但**学生不应为读懂一节课而跳十几个文件**。[阅读原创完整示例](examples/sample-course/lessons/L01/lesson.md)。

本仓库发行两类制品：
- **Agent Skill ZIP**：完整 \`SKILL.md\` + \`references/\` + \`assets/\` + 许可证/README，适合安装到 Agent；
- **Python wheel**：仅包含可选的离线 \`course-org\` 工具，不包含整个 Skill。两者不能混淆。

## 七角色严格审阅，并不冒充实际执行

\`review-plan\` 会为每节课生成独立审阅任务：教师覆盖、新手可读性、学科正确性、作业逐题盲解、复习有效性、版权隐私及对抗性检查。审核报告必须完整覆盖各 K 知识点、各 Q 练习和当前 SHA-256。**真正独立**的子智能体或人工审阅未完成时，不得声称课程已经通过严格审核。详见[独立审计规范](references/subagent-review.md)。

## 版权和数据安全

查看老师 PPT/板书、官方已公开考试题或教育用途，并不自动授予上传第三方模型、改编或公开传播的权利。未知权限不公开；教师原件、课堂录音和学生个人资料置于私有环境。发布前要独立核查文字、图像、题目、引用许可和个人信息。自动 \`audit\` PASS **无法保证零侵权风险**。详见[版权规则](references/copyright-gate.md)与[安全政策](SECURITY.md)。

## 开发、文档和贡献

[完整文档索引](docs/INDEX.md) · [CLI 使用指南](docs/USAGE.md) · [FAQ](docs/FAQ.md) · [开发指南](docs/DEVELOPMENT.md) · [项目架构](docs/architecture.md) · [发布说明](docs/releases/v0.2.4.md) · [发布流程](docs/RELEASE.md) · [贡献指南](CONTRIBUTING.md) · [更新记录](CHANGELOG.md)

仓库遵守 [MIT License](LICENSE)，仅对本仓库原创代码/文档生效，不覆盖教师或第三方教材。每次仓库代码修改都会在 [docs/routine/](docs/routine/) 留下时间、变更、验证、风险和下一步。旧版内容由 Git 历史保留，当前树不设冗余 legacy 目录。

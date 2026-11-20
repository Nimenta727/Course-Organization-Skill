# Course Organization Skill

> **让教师的课程成为主线，让 AI 帮助解释、补全、深化与复习。**
>
> **Teacher-led · Lesson-first · Research-enriched · Copyright-aware**

[English](README_EN.md) · [快速开始](docs/QUICKSTART.md) · [安装指南](docs/INSTALLATION.md) · [功能说明](docs/USAGE.md) · [开发路线](docs/roadmap.md) · [参与贡献](CONTRIBUTING.md)

**当前版本：v0.2.3 Preview（预览版）** · Python 3.10+（可选本地工具） · MIT（仅限本仓库原创代码与文档）

Course Organization Skill 是面向课程整理与教学资料重建的 [Agent Skill](https://agentskills.io/specification)。它以真实教师可核验的授课顺序、教学重点、板书思路和错误示范为基础，指导 AI 将有权使用的课程资料组织为**每节课一篇完整、易于阅读的讲义**，同时帮助补全基础解释、拓展学科知识、设计原创练习，并在获得许可且联网工具可用时检索权威参考资源。

**注意：** v0.2.1 主要包含 Skill 规范、教学与版权规则、课程模板及本地元数据校验工具。它**不是**开箱即用的 PDF/PPT 自动全文提取或完整课程自动生成服务器。实际教学内容重建需要具有文件访问权限的 AI Agent，外部检索需要该 Agent 具备相应联网工具。详细说明见[功能状态表](#功能状态)和[限制说明](#当前限制)。

![CI](https://github.com/Nimenta727/Course-Organization-Skill/actions/workflows/tests.yml/badge.svg)

## 为什么需要它？

传统资料整理常常以文件格式为中心：一节课的 PPT、课堂笔记、板书、代码、作业和考试知识点被放在不同目录，学习时不断跳转。通用 AI 摘要又容易忽略老师真正强调的内容，省略板书中的推理，甚至误把教师的错误示范当成正确答案。

本项目反过来组织内容：

**教师授课主线 → 逐项证据与缺口 → 原创详细讲解 → 学科适配 → 权威资料补充 → 练习与复习 → 审核**

最终输出不是一堆摘要，而是能给初学者从头学、也能给复习者快速回顾的连续课程讲义。

## 关键设计

1. **教师内容为主。** 保存可验证的知识顺序、重点、板书推理和错误类型；推测教学意图时必须标注为假设，而非杜撰教师原话。
2. **一课一文。** 每课在一个 `lessons/Lxx/lesson.md` 中容纳教师主线、基础概念、详细推导、多角度讲解、错误修正、难点拓展、练习和复习速览。
3. **新手与复习双路线。** 同一篇讲义既能连续学习，也能按页内目录快速定位知识结论、易错点和考点。
4. **学科独立方法。** 编程强调可运行示例、追踪与调试；数学强调推导与证明；科学强调模型与证据；人文强调材料与论证；语言强调表达与纠错；经济和工程强调假设与建模。
5. **开放但审慎的权威补充。** 可调用 Agent 的联网能力检索官方课程标准、大学资料、开放教材和官方已公开考试要求；**正式真题默认链接到原站，而不是复制或轻改题目。**
6. **版权与隐私安全边界。** 教师原件、学生数据、来源权限记录默认在私有环境，不进入公开仓库；公开发布要求单独核查授权、原创性和人工审批。
7. **降低无效 Token 开销。** SKILL.md 作为入口，按任务需要加载相关 references；确定性元数据处理交给本地脚本。真正的增量依赖引擎仍在路线图中。

## 功能状态

| 功能 | v0.2.1 状态 | 说明 |
| --- | --- | --- |
| Agent Skill 与按需参考规则 | ✅ 已提供 | `SKILL.md` + `references/` |
| 教师证据/错误示范保真流程 | ✅ 规范 + 元数据检查 | 需要真实材料和人工内容复核 |
| 六类学科差异化策略 | ✅ 已提供 | 按学科路由加载 |
| 一课一文、初学/复习双通道模板 | ✅ 已提供 | 附原创示例课程 |
| 本地文件元数据扫描 | ✅ 已提供 | SHA-256、大小、文件类型，不抽取正文 |
| 课程结构与目标对齐校验 | ✅ 已提供 | 检查目标→活动→评价的声明完整性 |
| 版权/隐私发布清单检查 | ✅ 已提供 | 严格阻断缺省发布；不等于法律意见 |
| 教师证据台账和资料登记校验 | ✅ 已提供 | 校验元数据，不校验实际网页真实性 |
| 按目标生成检索查询 | ✅ 已提供 | **离线计划，不执行网络搜索** |
| 学生讲义深度与分层作业强制检测 | ✅ 已提供 | 九大章节、K 知识点、Q 题目与逐题解析，需达到有意义的内容密度 |
| 七角色独立子智能体 / 人工审核 | ✅ 审核规范 + 报告门禁 | 必须由实际独立审阅者执行；本 CLI 不会自行启动子智能体 |
| 完成交付总门禁 | ✅ 已提供 | ready 检查课程结构、学生质量和独立审核的当前文件哈希 |
| 联网检索权威资料 | ◐ 依赖 Agent 能力 | 工具与授权齐备时遵循检索规范 |
| 自动解析 PPT/PDF/DOCX 正文和图片 | ⏳ 规划中 | v0.3 |
| 端到端批量生成整门课程 | ⏳ 规划中 | v0.4 |
| 可视化平台、增量缓存和自动发布 | ⏳ 规划中 | v1.0+；公开发布始终需人工审批 |

## 30 秒开始

### 1. 获得 Skill

~~~bash
git clone https://github.com/Nimenta727/Course-Organization-Skill.git
cd Course-Organization-Skill
~~~

将这个目录作为 Agent 可读取的 Skill 目录（含 `SKILL.md`、`references/` 和 `assets/`），或在相应 Agent 的 Skills 目录中放入该目录的副本或符号链接。Codex 和 Claude Code 的具体路径及 Windows 说明参见[安装指南](docs/INSTALLATION.md)。

### 2. 让 Agent 先制定整理计划

> 请使用 Course Organization Skill，围绕我有权使用的课程资料建立“教师证据—课次—学习目标”映射。先输出课程规划、拟生成文件、教师板书/错误示范待核对事项，以及版权与隐私限制；未经确认不要覆盖原文档、上传源资料或公开发布。之后按每课一篇详细讲义的结构生成原创讲解与练习，并在已授权的环境中检索权威来源。

不要将未获授权的教师材料发送给外部 AI 服务。**本地文件可读取，不意味着可以公开分享或上传模型。**

### 3. 安装可选的本地校验器

~~~bash
python -m pip install -e .
course-org --help
course-org validate examples/sample-course
course-org student-check examples/sample-course
# 只有真正具备七名独立审核者、且报告在仓库外时才可：
# course-org ready examples/sample-course --report /private/independent-review.json
course-org research-plan examples/sample-course
python -m unittest discover -s tests -v
~~~

示例课程是独立创作的虚构教材。下面这条命令**预期返回 BLOCK / 非零退出码**，因为示例没有获得公开发布审批：

~~~bash
course-org audit examples/sample-course
~~~

## 一节课最终长什么样？

~~~text
course/
├── course.json                     # 课程元数据和目标映射
├── README.md                       # 课程入口
├── lessons/
│   ├── L01/
│   │   └── lesson.md               # 第 1 课：完整可读讲义
│   └── L02/
│       └── lesson.md               # 第 2 课：完整可读讲义
├── assignments/                    # 跨课作业（按需）
├── labs/                           # 实验（按需）
├── assessments/                    # 阶段练习和评价（按需）
└── provenance/
    └── release-manifest.json       # 默认不允许公开发布
~~~

每篇 `lesson.md` 按“本课导读 → 预备知识 → 核心知识详解 → 例题精讲 → 易错点与纠正 → 分层作业 → 深入理解 → 复习速览 → 答案与解析”组织。每个核心知识点必须充分解释为什么、直觉、准确规则、完整推演及自检，不能只给一句定义。作业至少包含 2 基础 + 2 应用 + 1 挑战，逐题具备验收标准和详尽答案。学生章节不显示教师意图分析、版权台账和 AI 审计过程。技术上的证据切片可以细分，但人读的课程章节不会被拆散。

阅读[完整原创示例](examples/sample-course/lessons/L01/lesson.md)或[课程模板](assets/course-template/lessons/L01/lesson.md)。

## 本地命令速查

| 命令 | 用途 | 是否联网 |
| --- | --- | --- |
| `course-org scan INPUT --out /private/index.json` | 扫描文件名、大小、类型和哈希 | 否 |
| `course-org validate COURSE_DIR` | 检查课程路径、讲义章节和目标对齐 | 否 |
| `course-org research-plan COURSE_DIR` | 输出待执行的权威检索查询 | 否 |
| `course-org teacher-check /private/teacher-map.private.json` | 检查私有教师证据台账 | 否 |
| `course-org resource-check registry.json` | 检查外部资源登记声明 | 否 |
| `course-org audit COURSE_DIR --sources /private/source-manifest.json --teacher-map /private/teacher-map.private.json` | 发布前元数据阻断检查 | 否 |

**这些命令只验证它们明示的内容，不负责判断复杂法律权利、语义抄袭或课程学术正确性。**

## 保护教师版权和学生隐私

- 获取教师 PPT、课堂录音、原创试题或学生作业，**不自动获得**上传模型、翻译、改编或公开传播的权利。
- 保留教师课程**可核验的教学特点**，不默认为其独创文本、插图、编排和受保护习题获得再许可。无法公开的表达可留在私有证据层，公开教材另行独立编写。
- 官方发布真题也可能限制复制，默认提供可信原站链接，并独立设计新题。
- 涉及教师材料的公开内容必须通过来源授权、隐私、原创性和人工审核。自动 `audit` PASS **不能**保证法律上的零侵权风险。

详见[版权门禁](references/copyright-gate.md)、[安全政策](SECURITY.md)和[常见问题](docs/FAQ.md)。

## 文档导航

| 希望完成什么 | 阅读文档 |
| --- | --- |
| 第一次使用 | [快速入门](docs/QUICKSTART.md)、[安装/集成](docs/INSTALLATION.md) |
| 理解完整工作流 | [使用指南](docs/USAGE.md)、[架构设计](docs/architecture.md) |
| 保留教师课堂特点 | [教师证据保真](references/teacher-fidelity.md)、[整体设计](docs/teacher-centered-design.md) |
| 让新手和复习者都能读 | [完整讲义规范](references/reading-and-depth.md) |
| 匹配不同学科 | [学科路由](references/subject-profiles.md) |
| 搜索权威资料和考题 | [外部检索规则](references/external-discovery.md) |
| 理解教育方法 | [教学法决策矩阵](references/pedagogy.md)、[开源研究记录](references/open-source-research.md) |
| 课程数据与发布审核 | [数据契约](references/source-model.md)、[质量关卡](references/quality-gates.md) |
| 开发与贡献 | [开发指南](docs/DEVELOPMENT.md)、[贡献规范](CONTRIBUTING.md)、[更新记录](CHANGELOG.md) |
| 查看版本 | [路线图](docs/roadmap.md)、[发布说明](docs/releases/v0.2.1.md) |

## 当前限制

这是可以供 Agent 使用的 **Skill + 本地工具预览版**，不是独立课程管理网站。它不会自动调用未配置的模型/搜索工具，也没有实现 OCR、PPT 全文解析、语义查重或学生学习进度平台。外部联网补充只在 Agent 本身具备工具、资料使用许可和可实际核验的来源时进行。

## 参与和许可证

欢迎使用 [Issue 模板](.github/ISSUE_TEMPLATE)反馈错误、教学问题和功能需求；请**勿上传真实教师原始资料或学生信息到公开 Issue**。提交代码前阅读 [CONTRIBUTING.md](CONTRIBUTING.md)和[安全政策](SECURITY.md)。

本仓库由项目作者原创的代码与文档按 [MIT License](LICENSE) 发布；第三方教育项目、教师课件和学生资料**不受此授权覆盖**。引用或借鉴其他开源项目的思想不等于复制其代码或授课材料。

**项目维护记录：** 每次 GitHub 代码修改都在 [docs/routine/](docs/routine/) 中留存日期、变更、验证与下一步计划。

## 强制禁止敷衍与子智能体审计（v0.2.3）
生成器写完并不等于交付成功。**course-org student-check** 会阻断篇幅空洞、知识点只写一句话、缺完整例题、分层作业不足、答案缺失的课程章节。**course-org ready** 在此基础上，还要求七个互相独立的审核角色（教师覆盖、初学可读性、专业正确性、作业解题、复习有效性、版权隐私、对抗审阅）对当前文件 SHA-256 全部通过。无真实子智能体能力时必须进行独立人工审核，不能把自我复核冒充子智能体。自动字段检查只是下限，人工/独立模型必须检查内容有没有凑字数、事实错误和版权风险。

- [学生讲义强制写作标准](references/student-edition.md)
- [完整分层作业与答案要求](references/assignment-module.md)
- [子智能体独立严格审计](references/subagent-review.md)

## v0.2.3 逐项独立审阅
新增 course-org review-plan examples/sample-course：为每课创建七类角色任务和全部 K/Q 检查目标，但不会自动启动子智能体。review-gate 要求每位实际独立审阅者完成指定内容核查；作业审阅者逐题先独立解答、再核对解析，留下 question_checks。缺项或过期报告阻断验收。没有真正的独立审阅时状态为 REVIEW_PENDING。

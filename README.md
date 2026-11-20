# Course Organization Skill / 课程资料智能整理 Skill

**当前版本 v0.2.0 — 研究增强与版权防护的基础实现。** 将课件、讲义、课堂笔记、作业、实验和考试信息组织成“按课次聚合”的完整课程项目。以原创解释和可核验学习目标为核心，并默认保护教师原件与学生隐私。

> This project does NOT guarantee zero copyright risk or automatically authorize any teacher content for redistribution.

## 为什么做这个项目？
普通资料整理工具经常只按 PDF/PPT/Word 分类，导致一课的内容散落在多个目录。我们的 Skill 采用 **课程 → 课次 → 学习目标 → 活动 → 评价** 的统一结构；作业、实验、扩展、考试和备课内容通过学习目标与课次关联。

## v0.2 教师主线重建与开放检索
**教师是课程主线，AI 负责解释、补全和深化。** 逐项审阅教师写过的知识、板书、变量跳步、示例、重点与可能的错误；推测教学意图时必须标为推测并列出替代解释。完整课程以一课一篇讲义呈现，不把一节课拆成十几个碎片。

每课同时服务新手和复习：30 秒速览、教师主线、先修知识、基础推理、多角度讲解、错误诊断、深入延伸、原创练习、考题类型与复习速览，都在同一篇 lesson.md 中。

Skill 在可用且获许可的在线研究环境中，**按每课学习目标主动搜索**官方课程标准、权威考试信息、大学研究和开放教育资源，确认出处、适用范围和授权。官方真题优先提供原站链接，AI 生成新问题而不是复制/换数字改写受保护考题。无联网工具时输出明确的 NOT_SEARCHED 检索计划，绝不虚称完成检索。

不同学科有不同教学策略：编程追踪与调试、数学推导与证明、科学实验与模型、人文证据与论证、语言表达与反馈、经济和工程建模与边界条件。

## 核心能力
- **按课次组织：** 一课一篇可独立阅读的 lesson.md，包含概念讲解、原创示例、错误分析、练习和总结。
- **教学研究驱动：** ADDIE、逆向设计、建构性对齐、Bloom、Merrill、5E、PBL、间隔复习、检索练习、UDL 3.0；按教学任务选用，不机械堆砌。
- **来源和推断分离：** 教师资料的直接证据、可靠推断、独立扩展及未知内容分级，杜绝伪称教师原话。
- **版权与隐私关卡：** 未经确认的材料不复制、不随意上传、不公开；手动审查 + 本地静态发布检查。
- **低 Token 开销：** 使用索引和按需参考文档，课程内容增量处理（自动依赖图/缓存仍在规划）。
- **本地辅助工具：** 文件元数据扫描、课程目标一致性验证、严格发布清单审核。v0.1 不解析课件正文、不做文本相似度或法律鉴定。

## Quick Start / 快速开始
1. 将本仓库的 SKILL.md 和 references/ 作为可读取的 Agent Skill，或在 Agent 中指向本仓库的 SKILL.md。
2. 仅在**获得许可的私有环境**中向 Agent 提供课程大纲/资料；首先输出课程规划与版权清单。
3. 可选安装本地校验器（Python 3.10+）：

~~~bash
python -m pip install -e .
course-org scan /path/to/private/inputs --out /path/outside/repo/private-index.json
course-org validate examples/sample-course
course-org audit examples/sample-course
course-org research-plan examples/sample-course
# 使用私有证据台账时：course-org teacher-check /private/teacher-map.private.json
# 资料经实际在线核验后：course-org resource-check /private/resource-registry.json
python -m unittest discover -s tests -v
~~~

scan 只保存文件名、哈希、大小、粗略课次匹配等元数据，**不读取正文、不调用外部模型，也不会将资料复制进项目**。例子中的 audit 默认 BLOCK，因为示例没有授予真实公开发布审批。

## 使用时的提示词
“使用 Course Organization Skill，先盘点私有资料并给出课程结构、来源权利状况及课程制作计划。请以每课为一个完整教学单元，创建原创解释、案例、练习、实验与考试关联。不要复制教师课件和题目，不要假定教师已许可公开；修改文件前展示差异，发布前执行严格版权与隐私审核。”

## Repo structure
- SKILL.md: Agent 入口和执行状态机
- references/: 工作流、教学法矩阵、版权边界、数据模型和质量关卡
- src/course_org/: 可选、本地、无网络依赖的扫描/验证 CLI
- assets/course-template/: 课程项目模板
- examples/sample-course/: 完全虚构的安全示例
- tests/: 自动化测试
- docs/: 架构、研究、规划与 docs/routine/ 持续开发记录

## 版权与公开发布
教师讲义、课件、录音、私有习题和学生数据不能因为“用于教学”“AI 改写了”或“注明出处”就自动公开。该 Skill 对授权不明、许可不兼容、含原始表达或隐私数据的产物默认阻止发布。**版权审查不是法律意见，自动审计 PASS 也不是法律安全保证。** 详细规则见 references/copyright-gate.md。

## 文档
- [English README](README_EN.md)
- [研究借鉴清单](references/open-source-research.md)
- [架构与质量约束](docs/architecture.md)
- [版本计划](docs/roadmap.md)
- [开发记录](docs/routine/)

## Licence
本仓库原创代码和说明以 MIT 许可证发布（详见 LICENSE）。外部教师资料、学生数据及第三方教材不属于本仓库许可证的授权范围。

## 关键文档入口
- [教师证据与板书保真](references/teacher-fidelity.md)
- [初学/复习双路线一课一文](references/reading-and-depth.md)
- [权威外部资料检索与真题使用规则](references/external-discovery.md)
- [按学科选择教学 Skill](references/subject-profiles.md)
- [本轮具体改动与后续规划](docs/routine/2026-11-20-03-teacher-led-open-research-course-depth.md)

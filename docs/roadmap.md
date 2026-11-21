# 路线图 / Roadmap

> **v0.2.4 Preview 是当前发布目标。** 此页面只维护当前能力、未解决事项和后续版本；早期独立版本草案由 Git 历史与 CHANGELOG 保存，不在当前目录堆放重复过时文档。

## 已实现：v0.2.4

- **可移植 Skill：** SKILL.md + 渐进加载参考文档、学科 profiles、课程模板和完全原创的编程示例。
- **教师证据优先：** 实际课堂知识顺序、板书、错误示范及跳步推理的私有映射协议与元数据校验。
- **学生可读的一课一文：** 严格九章节格式，K 知识点必须详解，Q 作业至少 2+2+1 并附逐题推理、完整例题与复习速览。
- **本地确定性工具：** scan、validate、student-check、teacher-check、resource-check、research-plan、review-plan、review-gate、ready、audit。
- **严谨但有限的审阅机制：** 七角色离线任务与按 K/Q 检查目标、声明、独立盲解记录和 SHA-256 门禁；并未内建真实子智能体执行。
- **发布工程：** 双语 README、完整文档索引、贡献/安全政策、Issue/PR 模板、三版本 CI、GitHub Topics 与 Issue 标签、完整 Skill ZIP/CLI wheel 构建与发布准备。

## 优先级 P0：真实课程实例验收

1. 使用**具备适当授权**的真实编程课材料，逐页登记 K 目标、板书、错误示范和权利状况。
2. 测试学生从零读是否能学会：核查定义、关键推理、边界条件、例题和答案，拒绝以字数替代实质。
3. 真正独立的学科、作业与新手审阅，记录错误及修改后重新审查；如果没有独立审阅，保持 REVIEW_PENDING。
4. 评估学生完成 2+2+1 作业与复习检索时的困惑，建立可追踪的改进清单。

## v0.3：获许可资料的离线抽取与来源映射

- PDF/PPTX/DOCX 适配器和合理的本地 OCR/图片理解，必须处理隐私和版权。
- 真实来源页面/幻灯片定位、变更预览和课程目标覆盖清单。
- 教师板书/错误示范的准确性检验与权限状态分离。
- 合成与明确授权的回归数据集；不在公开测试仓库放老师原件。

## v0.4：可验证的逐课内容生成

- 具有独立来源核对的原创详解、例题、练习、答案和深入拓展管线。
- 可选联网权威资料检索器，强制记录真实 URL/日期/使用许可，不能伪造。
- 编程练习可执行测试，数学推导与学科事实单独审阅。
- 真实可授权的子智能体编排适配器与审核证据归档。

## v1.0：稳定课程生产工具

- 增量依赖图、内容变更差异、缓存和 token 使用指标。
- 实质性相似度风险提示及可人工处理的版权/隐私放行流程。
- 逐学科教学质量评估、完整文档导出、可重复生成和健壮的错误恢复。

## v1.5+：可选可视化平台

- 课程树/学习路线、来源差异审核、教学质量报告与发布面板。
- 多课程工作区与受授权约束的 LMS/文档工具集成。

**边界：** 不承诺零版权风险、无授权的第三方模型数据处理、真实子智能体自动执行，也不把还在规划的解析/生成能力标成已实现。

**English:** v0.2.4 ships a substantial Agent Skill, synthetic sample, offline validators, review checklists, bilingual documentation and release packaging. Real document ingestion, authenticated subagents, automatic content generation and publication approval workflows remain next steps.

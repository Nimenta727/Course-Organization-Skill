# 系统架构 / Architecture

## 产品边界

\`Course Organization Skill\` 是**Agent 的行为与生成规范**，不是自带大模型的独立课程平台。输入为经授权使用的课程/课堂材料；输出是按课次组织的、可供初学与复习的一篇篇学生讲义。具体读取 PDF/PPT/OCR、联网搜索及执行子智能体取决于宿主 Agent 的工具与权限。

\`\`\`text
Private authorized input
  ├─ teacher originals / boardwork / lecture notes (NEVER public by default)
  ├─ rights basis and allowed tool/provider processing
  └─ source evidence ledger (observed facts vs uncertain intent)
            │
            ▼
Agent with Course Organization Skill
  ├─ source inventory & teacher coverage mapping
  ├─ curriculum / lesson K + LO + ACT + ASM planning
  ├─ subject-specific original detailed instruction
  ├─ optional actually verified authoritative research
  └─ one complete student chapter per lesson
            │
            ▼
Offline CLI: validate → student-check → review-plan
            │
            ▼
Real independent agents/humans (outside CLI; permission-gated)
            │
            ▼
Offline CLI: review-gate → ready
            │
            ├─ student-ready (not automatically public)
            ▼
Independent human rights/privacy approval + audit
            │
            ▼
Opt-in publication
\`\`\`

## 两层数据：课程正文与私有证据

**公开候选正文：** \`course.json\` 和 \`lessons/Lxx/lesson.md\`，每课九个紧密连贯的学生章节，解释和答案必须充分、原创。课程层实验、跨课项目允许链接，但不能替代本课的学习材料。

**内部数据：** 老师材料、板书图片、页面/幻灯片定位、意图假设、许可证证据、真实审阅报告、课程更新缓存等。保持在受控私有目录，不放进 public Git worktree。学生不应看到这层内容。

## 质量门禁和局限

| 层 | 可以做 | 不能证明 |
| --- | --- | --- |
| \`validate\` | 课程路径和 LO→ACT/ASM 声明 | 实际课堂覆盖或教育效果 |
| \`student-check\` | 九段式、非代码最低密度、逐题答案、重复练习启发式 | 文字真实深度、概念正确性 |
| \`review-plan\` | 七角色审阅任务、K/Q 范围、SHA | 真正启动审阅者 |
| \`review-gate\` / \`ready\` | 审阅记录格式、覆盖和当前文件摘要 | 独立身份、真实盲解行为 |
| \`audit\` | 部分权利/公开授权元数据的保守规则 | 复杂版权问题或法律许可 |

## 低 Token 和分学科路由

入口只加载必要参考规范；不同学科分别选择专业结构，避免同时加载全部文档。将简单扫描、哈希、文件路径/结构检查留在 Python 中，较昂贵的理解、创作、事实核查交给有权限的 Agent。计划中的增量缓存与真实子智能体编排尚未实现。

## 发行安全

完整 ZIP 由 \`scripts/package_skill.py\` 在允许列表内收集 \`SKILL.md\`、\`references/\`、\`assets/course-template/\`、README 和 LICENSE；排除源教师资料、独立审计报告、测试与开发日志。Python wheel 仅含 CLI。GitHub 源码自动压缩包用于开发者。任何实际公开课程内容仍必须单独进行权利审核。

参考：[学生规范](../references/student-edition.md) · [版权门禁](../references/copyright-gate.md) · [开发指南](DEVELOPMENT.md)。

**English:** A portable agent workflow and an offline Python CLI, with teacher evidence private, one self-contained learner chapter per lesson, deterministic student quality checks, genuinely independent human/subagent reviews where supported, and separate publication permission.

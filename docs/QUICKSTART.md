# 快速开始 / Quick start

这是可独立使用的 **Agent Skill + 可选 Python 离线检查器**，不是自动上传教师课件的服务。本示例使用仓库原创数据，不需要任何真实老师文件。

## 1. 下载与测试

~~~bash
git clone https://github.com/Nimenta727/Course-Organization-Skill.git
cd Course-Organization-Skill
python -m pip install -e .
course-org validate examples/sample-course
course-org student-check examples/sample-course
course-org research-plan examples/sample-course
course-org review-plan examples/sample-course
~~~

预计 `validate`、`student-check` 返回 PASS。后两条输出 JSON 计划，不联网也不启动智能体。你的 GitHub Release 如果附有 `course-organization-skill-v0.2.5.zip`，可直接解压作为 Agent Skill；只装 Python wheel 得到的则是离线 CLI。

## 2. 在 Agent 中使用

将完整仓库或 Skill ZIP 解压目录提供给支持文件读取的 Agent，要求读取 `SKILL.md`。建议直接发送：

> 使用 Course Organization Skill。在授权范围内先分析课程文件，确认教师讲授顺序、板书、知识点和错误示范，生成私有证据映射和非破坏性计划。每节课只给学生一篇完整的 `lesson.md`，逐知识点充分解释动机、直觉、规则、推演和自检；附至少 2 基础 + 2 应用 + 1 挑战的完整原创作业以及逐题详细答案，适合新手阅读和考前速览。只在确有联网工具和资料使用权限时检索权威来源。写完执行学生质量检查，并由真实独立审阅者逐项审计；如果没有子智能体，请如实标记 REVIEW_PENDING。不要复制或公开教师原件。

## 3. 验收与边界

在资料/版权权限不明确时先保持私有，不把文件上传到第三方模型，也不把教师课件放进 GitHub。

~~~bash
course-org audit examples/sample-course
course-org ready examples/sample-course --report /private/missing-review.json
~~~

上面两条在示例上应输出 BLOCK：**没有发布授权，也没有真实独立审阅报告**。这是正确的保护措施，不是软件损坏。

## 4. 判断学生讲义是否成功

- 学生不需要打开多个文件就能从头理解一节课。
- 重要知识点不是一句定义；有为什么、准确条件、完整中间步骤和反例。
- 练习有完整题目、输入/背景、交付物、验收标准、提示和逐题推理。
- 速览能帮助学生闭卷回忆；不能充当缺失的正文。
- 真实教师内容有私有来源覆盖记录；公开章节只有合规、独立的表达。
- 没有真实子智能体或独立人工审核时，任何“全部严格审计通过”都是不真实的。

下一步：[安装](INSTALLATION.md) · [实际使用与数据格式](USAGE.md) · [全部文档](INDEX.md)。

**English:** Clone or download the complete Skill ZIP, optionally install the offline CLI, test the fictional sample, and give a file-capable authorized agent the Skill. Review and publication gates intentionally BLOCK when independent approval or rights evidence is absent.

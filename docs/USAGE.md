# 使用指南 / Usage guide

## 场景一：零基础学习用的完整课次讲义

**目标：** 从已授权的课程资料重建一课，忠实反映课堂的知识顺序和难点；补足省略的推导，配套原创练习，在末尾加入可快速浏览的复习速览。

建议 Agent 工作顺序：

1. **资料和权限盘点**：确定可私下读取、是否可传入模型、是否可改编或公开的权限，缺失则保留私有。
2. **教师证据映射**：对课程知识点、板书中间步骤、案例、错误、反复强调与问题转场建立私有台账。
3. **内容计划**：围绕教师有证据的授课顺序设计章节和缺口补写；把“教师实际写了什么”与“AI 判断可能为什么写”分开。
4. **教学深化**：按学科加载正确的 profile，加入适合新手的解释、完整过程、不同视角、错误修正和更深入的原理。
5. **资料补充**：在可用且获授权的联网环境中，查找真实官方课程标准、大学资料和进阶参考，核实出处及授权。
6. **交付和审查**：每节课为一个完整的 `lesson.md`，保留复习速览；先展示预览和来源差异，经过许可审核后决定能否公开。

## 场景二：已有课程的考试复习

同一课保留完整正文，不另存一套容易漂移的“轻量版”。在文档顶部给出复习路径，末尾提供概念框架、常见错误、考试涉及能力、五分钟闭卷检索和间隔回顾问题。官方考试材料优先引用原始网页；只生成独立设计的模拟题。

## 场景三：本地扫描课程资料（不读取正文）

~~~bash
course-org scan /private/teacher-inputs \
  --out /private/course-organization/private-index.json
~~~

结果包括相对文件名、扩展名、大小、SHA-256、粗略课次猜测及默认 UNKNOWN 权利状态；**不包括 PDF/PPT 正文**。输出不可放在 Git 仓库或源资料目录内。请勿将清单上传到公共 Issue 或 PR。

## 场景四：验证课程项目

~~~bash
course-org validate examples/sample-course
~~~

该命令读取 `course.json`，确认课次路径、安全的 Markdown 文件、目标与活动/评价 ID 是否存在。它只能验证结构，无法判断内容是否准确、是否真实对应教师讲课或是否存在抄袭。

### 课程元数据最小形式

~~~json
{
  "course_id": "sample",
  "title": "Independent example course",
  "subject": "computing",
  "lessons": [{
    "id": "L01",
    "path": "lessons/L01/lesson.md",
    "objectives": [{
      "id": "LO01",
      "statement": "Explain a new algorithm",
      "activities": ["ACT01"],
      "assessments": ["ASM01"]
    }]
  }]
}
~~~

参见 [source-model.md](../references/source-model.md) 和 [sample-course](../examples/sample-course/)。

## 场景五：准备权威资料的检索计划

~~~bash
course-org research-plan examples/sample-course
~~~

这是一个**不联网**的检索计划，标记 `NOT_SEARCHED`。将这些查询交给具备授权和真实网页访问能力的 Agent，在每条参考资源中记录原始 URL、出版方、查询日期、相关性以及引用/改编许可。不得把模型记忆中的网页内容冒充已经核验的资料。

### 来源与版权使用

- 实际官方课程标准与考试范围：验证地区、年份、版本。
- 官方公开真题：通常仅提供官方链接，未经明确许可不复制受限题干和配图。
- 大学与开放教材：核验文章/图像/题目各自的许可，不假定整站均可自由复制。
- 非权威论坛：可以发现易错问题，但不能单独支撑重要科学或考试结论。

## 场景六：检查私有教师内容映射

~~~bash
course-org teacher-check /private/teacher-map.private.json
~~~

需要私有台账（示例数据结构见 [source-model.md](../references/source-model.md)）：每个有意义的来源片段要说明来源位置、类型、处理结果和教学意图状态。意图可以显式有据、假设有替代解释或未知。

## 场景七：检查引用登记和公开发布资格

~~~bash
course-org resource-check /private/resource-registry.json
course-org audit /path/to/course \
  --sources /private/source-manifest.json \
  --teacher-map /private/teacher-map.private.json
~~~

若没有使用教师材料，可按实际情况不提供 `--teacher-map`；不能为了绕过检查把真实来源错误标记为未使用。只有真实的授权证据和人工审查，才可能支持合法的公开发布。

**重要：** `audit` 默认 BLOCK，且只检查声明元数据。绝不能以它代替对正文、图片、试题、引用许可证与隐私的真实审查。

## 常见错误

- 把教师讲义直接转成公共 Markdown → **不合格**；访问权限不等于再发布权。
- 看到一行错误板书就说“老师故意出的陷阱” → **不合格**；必须区分观察与推测。
- 将一课拆成概念、错误、作业、代码的十余个独立文件 → **不合格**；一课一文。
- 只列出外部资料名称，没有实际打开网页 → **不合格**；标记 NOT_SEARCHED。
- 修改官方真题的几个数字就发布 → **不合格**；应原创设计新问题。

**English summary:** Keep a private source/evidence map, design complete lesson-based content, use separate subject-specific pedagogies, run web research only with real authorized tools, and retain human legal/quality review. CLI commands only check metadata and layout; they neither ingest teacher documents nor establish copyright clearance.

## v0.2.2 强制学生讲义与子智能体审核

旧版示例中的“教师授课主线”“教师可能想表达什么”等是内部生产规则，**不可作为学生讲义的章节标题**。学生正文统一采用九个标准标题：本课导读、预备知识、核心知识详解、例题精讲、易错点与纠正、分层作业、深入理解、复习速览、答案与解析。核心知识每个 K 编号均需完整动机、直观、准确规则、逐步推演与检查理解。作业最低两基础、两应用、一挑战，均有任务、验收、提示和详细配对答案。

运行：

~~~bash
course-org student-check examples/sample-course
# 以下命令必须提供由真正独立的子智能体/人工审阅者填写的私有报告，不能伪造：
course-org review-gate YOUR_COURSE --report /private/independent-review.json
course-org ready YOUR_COURSE --report /private/independent-review.json
~~~

ready 将结构、学生内容密度及七名独立审核角色的最新 SHA-256 合并检查；修改课程后旧的审阅报告自动失效。任何未经过实际审核的内容必须标记 REVIEW_PENDING；通过只说明元数据完整且关联最新文本，不代表版权可以公开发布。详见 references/student-edition.md、assignment-module.md、subagent-review.md。

## v0.2.3 七角色逐题审计
本地命令依次是 course-org student-check COURSE_DIR、course-org review-plan COURSE_DIR、course-org review-gate COURSE_DIR --report PRIVATE_REPORT.json 和 course-org ready COURSE_DIR --report PRIVATE_REPORT.json。review-plan 只输出检查清单、章节 SHA 和七类角色指令，不会启动子智能体。每个实际独立审阅角色必须核对指定的 K 知识点、Q 作业。作业角色先不看答案独立解题，然后逐题核对，记录 question_checks。文件改动后旧报告失效。无真正子智能体或独立人工审核时必须写 REVIEW_PENDING，不得伪造审核完成。

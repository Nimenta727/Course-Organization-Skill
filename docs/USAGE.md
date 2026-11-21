# 使用指南 / Usage

## 一、按老师的知识顺序制作学生教材

**第一步：确认使用权限。** 区分“能在本地查看”“允许发给第三方模型”“允许改编”“允许公开发布”四件不同的事情。默认私有处理，未知权限不公开。

**第二步：私下建立教师证据映射。** 逐一核对知识顺序、板书过程、跳步推理、错误示范、老师明确强调的条件及课次衔接。老师的*真实讲解事实*和 AI 对意图的*假设*必须分开；学生讲义不应出现“老师可能在想什么”。

**第三步：课程计划。** 从课程大纲与实际课次确定各课 K 知识点、LO 学习目标、ACT 教学活动和 ASM 练习评价。重要来源片段要能追踪覆盖情况。先展示预计生成文件及差异。

**第四步：按学科深入讲解。** 编程类课程可采用“预测运行结果 → 精确模型 → 逐行追踪 → 真实编译/验证 → 错误修复 → 新问题”；数学、实验科学、人文、语言等使用匹配的专业规范。每课主文件只做一篇完整学生章节，不能把例题、易错点、复习和作业拆散。

**第五步：权威资料补充。** Agent 有实际联网能力且获得相应许可时，可搜索官方考试大纲、大学讲义、研究论文、授权开放教材并逐条核查。官方真题通常优先提供链接；新练习应在情境和推理上真正独立。无联网工具使用 \`research-plan\` 生成 \`NOT_SEARCHED\` 清单，不能伪造已检索资料。

## 二、学生正文的九段式结构

\`lessons/Lxx/lesson.md\` 必须包含：\`本课导读\` → \`预备知识\` → \`核心知识详解\` → \`例题精讲\` → \`易错点与纠正\` → \`分层作业\` → \`深入理解\` → \`复习速览\` → \`答案与解析\`。

所有 K 知识点必须讲清五件事：**为什么学、直观理解、准确规则、逐步推演、检查理解**。作业每课至少 Q01/Q02 基础、Q03/Q04 应用、Q05 挑战，每题写清学习目标、任务、提交内容、验收标准、提示。最后所有 Q 对应一段真正的答案推理和错误辨析。

详见 [学生教材格式](../references/student-edition.md)、[作业规范](../references/assignment-module.md)与[完整原创示例](../examples/sample-course/lessons/L01/lesson.md)。

## 三、本地 CLI 命令

| 命令 | 真实作用 | 不做什么 |
| --- | --- | --- |
| \`course-org scan INPUT --out /private/index.json\` | 文件名、大小、哈希、课次猜测 | 不读 PDF/PPT 正文 |
| \`course-org validate COURSE_DIR\` | 路径、课程目标、教学活动与评价声明 | 不审查知识真实性 |
| \`course-org student-check COURSE_DIR\` | 九段结构、最低讲解密度、作业与答案配对、重复题检测 | 不判断所有语义/教学质量 |
| \`course-org research-plan COURSE_DIR\` | 输出授权研究查询计划 \`NOT_SEARCHED\` | 不联网 |
| \`course-org review-plan COURSE_DIR\` | 为七类审核者生成按 K/Q 逐项清单和 SHA-256 | **不运行子智能体** |
| \`course-org teacher-check PRIVATE_MAP.json\` | 私有课堂证据台账字段检查 | 不读取真实课堂判断意图 |
| \`course-org resource-check REGISTRY.json\` | 外部资料登记字段/许可声明 | 不验证网页真实与可用 |
| \`course-org review-gate COURSE_DIR --report PRIVATE_REPORT.json\` | 检查七角色独立报告各项覆盖、盲解、有效哈希 | 不证明审核者实际独立完成工作 |
| \`course-org ready COURSE_DIR --report PRIVATE_REPORT.json\` | 合并课程结构、学生正文与独立报告门禁 | 不授权公开发布 |
| \`course-org audit COURSE_DIR --sources PRIVATE_SOURCES.json --teacher-map PRIVATE_MAP.json\` | 保守的公开发布权限*声明*检查 | 不是法律审查或零侵权保证 |

## 四、课程数据最小示例

~~~json
{
  "course_id": "programming",
  "title": "编程思维",
  "subject": "computing",
  "lessons": [{
    "id": "L01",
    "path": "lessons/L01/lesson.md",
    "topics": [{"id": "K01", "title": "算法步骤"}, {"id": "K02", "title": "边界条件"}],
    "objectives": [{
      "id": "LO01",
      "statement": "解释算法及其适用条件",
      "activities": ["ACT01"],
      "assessments": ["ASM01"]
    }]
  }]
}
~~~

\`source-manifest\`、\`teacher-map\` 和真实审核报告只存于 Git 仓库以外的受控位置。格式见[数据说明](../references/source-model.md)。

## 五、七角色审阅的实际顺序

1. 完成真实且符合许可的学生章节。
2. \`validate\` 和 \`student-check\` 均 PASS；缺少深度或作业答案则先重写。
3. 用 \`review-plan\` 得到按章节 SHA-256 的各角色必审 K/Q 列表。
4. **真正**委派独立子智能体或独立人工审阅教师覆盖、新手可读性、学科正确性、作业盲解、复习效果、版权隐私和对抗性问题。作业审阅者先独立解 Q，再核对答案。
5. 把包含具体检查依据的报告存在私有目录；修复后所有报告应对最新版本重做。
6. \`review-gate\` 和 \`ready\` 检查报告完整性。若没有独立审阅能力，不要伪造 PASS，明确返回 \`REVIEW_PENDING\`。
7. 要公开发布时，另外核验每个资料/题目/图片的权利，取得必要批准；\`audit\` 的结构 PASS 不等于法务批准。

## 六、识别不合格产物

“一个知识点只写一句定义”“一题只给一个数字”“换几个参数造五道重复题”“报告中说有七个子智能体却没有独立记录”“把老师的猜测意图写给学生”“声称编译了但没运行”都属于需要修正的缺陷。

**English:** Verify rights, privately map teacher evidence, plan by lesson and subject, write one substantive chapter, check it structurally, arrange actual independent reviews, and separately clear public rights. The offline CLI performs deterministic planning/validation only.

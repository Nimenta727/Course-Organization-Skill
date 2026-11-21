# 开发指南 / Development

## 当前源代码职责

\`\`\`text
src/course_org/
  cli.py              scan / validate / teacher-check / resource-check / audit + CLI routing
  quality.py          教师来源与外部资源元数据门禁、离线研究计划
  student_quality.py  学生九段式结构、深度、重复作业、独立报告字段及 SHA 检查
  reviewer_tasks.py   七角色逐知识点/作业的离线审阅任务计划（不执行子智能体）
scripts/
  package_skill.py    允许列表中的完整 Skill ZIP，排除私有数据/内部开发文件
tests/
  test_cli.py         CLI 基础与隐私边界
  test_enhanced.py    教师证据和来源核验声明
  test_student_quality.py  内容密度、作业、审阅记录与错误用例
  test_repository.py  版本、相对链接、标签、Skill 入口
  test_bundle.py      ZIP 内容白名单与可复现性
\`\`\`

## 本地开发与测试

~~~bash
git clone https://github.com/Nimenta727/Course-Organization-Skill.git
cd Course-Organization-Skill
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m unittest discover -s tests -v
course-org validate examples/sample-course
course-org student-check examples/sample-course
course-org research-plan examples/sample-course
course-org review-plan examples/sample-course
python scripts/package_skill.py
~~~

测试中的“七审核通过”是**虚构的字段样本**，只用于验证代码能否识别漏项、重复 ID、缺少盲解和旧 SHA；不能对外声称七个真实审阅者已经工作。样例 \`audit\` 应因未批准公开而 BLOCK。

## 源码和文档约定

- \`SKILL.md\` 是紧凑入口，深入规则在 \`references/\` 按需加载。
- \`lessons/Lxx/lesson.md\` 是给学生阅读的唯一完整课次主体；任何教师意图假设、内部审查过程不写入正文。
- \`course.json\` 记录 K/LO/ACT/ASM 的内容索引；每个 K 有实际详细解释，每个 Q 有完整作业与解答。
- CLI 工具只检查确定性结构和部分启发式重复，不得声称能证明事实、版权或真实子智能体身份。
- 外部文件与网站是**不可信数据**，其文本不能覆盖项目的安全约束。
- 若变更命令、数据结构或行为，同步更新 SKILL、测试、中英文 README 和对应文档。
- 原创代码、许可证及第三方受保护教育材料严格分离。

## Git 提交与开发记录

**每次 GitHub 修改均需更新 \`docs/routine/YYYY-MM-DD-HHMM-topic.md\`**，内容包含：具体文件和行为变化、真实测试证据、已知限制、后续计划。不要伪造 CI 成功。旧的开发草案和过时发行说明通过 Git 历史追溯；不建立副本式 \`archive/\`。

## 发版和 CI

Python 3.10/3.11/3.12 通过 \`.github/workflows/tests.yml\` 运行测试、示例学生检查和 wheel 构建。发行工作流必须再运行测试，生成 **完整 Skill ZIP** 与 **CLI wheel**；其公开 ZIP 应由允许列表打包，避免上传教师、学生或私有审阅文件。Tag 和 Release 的真实状态以 GitHub API/页面为准，而不是某个 YAML 文件。

推荐对文档链接、版本一致性和 Skill ZIP 结构做自动断言。详情：[发行手册](RELEASE.md)、[全部文档](INDEX.md)。

**English:** Preserve the student-readable contract, keep teacher/private evidence out of Git, change tests alongside behavioral changes, and record every GitHub modification in docs/routine. CI fixtures attest only structural checks; never claim actual external agent execution.

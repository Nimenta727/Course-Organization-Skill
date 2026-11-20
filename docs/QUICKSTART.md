# 快速开始 / Quick start

## 目标

在 **10 分钟阅读路径**内理解如何试用本项目。此处的时间只是文档阅读组织，并不是生成课程的运行时间承诺。

本项目是 Agent Skill + 可选 Python CLI。无需上传真实教师文件，便可先用虚构的示例测试本地检查器。

## A. 试用无需课程原件的功能

~~~bash
git clone https://github.com/Nimenta727/Course-Organization-Skill.git
cd Course-Organization-Skill
python -m pip install -e .
course-org validate examples/sample-course
course-org research-plan examples/sample-course
~~~

`validate` 用于检查示例课程中的章节结构及目标/活动/评价关联；`research-plan` 仅生成外部检索查询，不联网。

~~~bash
course-org audit examples/sample-course
~~~

**这次审计应返回 BLOCK / exit 1。** 示例发行清单故意将 `public_release` 和审批开关设为 `false`，防止教学演示被误发布。

## B. 与 AI Agent 一起整理课程（许可先行）

在 Agent 支持 Skill 的环境中，将本仓库作为一个可读取的 Skill 目录。文件访问、网页搜索和生成能力取决于 Agent；具体安装参见 [INSTALLATION.md](INSTALLATION.md)。

给 Agent 的完整提示词：

> 使用 Course Organization Skill 整理我已经获得必要处理许可的《课程名称》资料。先审计资料类型、来源权限、课次与知识点关系。教师讲授的概念顺序、板书跳步、错误示范和重点是课程主线，请为每项建立证据与解释，不要猜造老师说过的话。每课只生成一篇充实的 Markdown 讲义，让新手能从零理解，让复习者能通过速览和检索练习复习。根据学科采用不同教学法；通过授权的联网工具检索官方考试范围、大学教学资料及进阶知识，核实出处与权限，官方真题默认仅链接原站。先给出计划和文件差异，不覆盖或发布任何教师原件。

## C. 检查试用成果

检查是否真的符合以下原则：

- [ ] 每一课只有一篇完整的人类阅读入口。
- [ ] 教师课堂事实与 AI 推测明确区分。
- [ ] 板书步骤、错误示范及纠正被保留为教学知识。
- [ ] 初学者能独立理解中间推理；复习者能快速找到重点。
- [ ] 外部考题和资料有真实可访问出处，没有复制受保护内容。
- [ ] 原始教师文件和含个人信息的记录不在公开目录。
- [ ] 没有把自动审计的通过误说成法律审核通过。

## D. 下一步 / Next

阅读 [USAGE.md](USAGE.md) 了解私有清单和具体命令；阅读 [FAQ.md](FAQ.md) 了解为什么 CLI 不会自己搜索网络或读取 PPT 正文。

**English:** Clone the repository, optionally install the Python CLI, run the fictional sample's `validate` and `research-plan`, and confirm that `audit` blocks publication by default. To create new course lessons, attach the Skill to an authorized, file-capable Agent and request a non-destructive plan before generation.

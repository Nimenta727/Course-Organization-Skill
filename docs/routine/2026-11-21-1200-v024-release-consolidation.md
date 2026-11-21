# 2026-11-21 12:00 — 全量整理 v0.2.4 Preview 并准备 GitHub Release

## 本次代码和文件修改
- 重写 SKILL.md，合并学生九段详解、教师真实教学主线、分学科补写、分层作业、子智能体实际独立审查与版权边界；去除多版本重复追加指令。
- 重写中英文 README、文档索引、安装、快速开始、使用、FAQ、架构、开发、发布、路线图、教师主线说明及 GitHub 元数据说明。
- 整理 references 学生内容密度、作业、七角色审核、质量关卡、完整工作流与部分来源数据描述，确保执行规范没有过时版本附录。
- 增加 scripts/package_skill.py 的 allowlist 完整 Skill ZIP 构建器、可复现性测试 tests/test_bundle.py；Python CLI wheel 仍单独发行。
- 更新 student_quality.py：九个 H2 严格顺序与 K 知识点唯一性，并更新自动测试。
- 统一 pyproject.toml、__version__、CITATION、CHANGELOG、README 和 Release 说明到 v0.2.4。
- 将 docs/releases/v0.2.1.md、v0.2.2.md、v0.2.3.md 从当前树中移除，历史保留在 Git 提交中；历次真实开发记录 docs/routine 保持不变。
- GitHub Actions 发布步骤新增完整 Skill ZIP、CLI wheel、SHA256SUMS 文件、打包内容验证、版权默认拒绝测试与 GitHub Pre-release；由明确的当前版本发行资料变更触发发布。

## 版权、审阅和真实性声明
- 当前发行不包含教师原件、学生信息、正式受限考试题或私有子智能体报告。
- review-plan 只给审阅角色分配任务，不启动子智能体；review-gate 只校验审阅记录声明而不能证明真实审阅发生。
- 自动版权审计不是法律意见，不能保证零侵权风险。

## 已知测试事实与待核实事项
- 修改前最后一个已核验成功 CI：44783162958（v0.2.3、Python 3.10/3.11/3.12；3.11 日志为 37 tests）。这不代表 v0.2.4 已验收。
- 本次提交后的 GitHub Actions 才可证明新单元测试、Skill ZIP、wheel 构建和 Pre-release 是否成功。
- 仓库 Description 和 12 个 Topics 已实际通过 GitHub API 核查存在。

## 下一步
1. 检查最新 Actions 和 GitHub Release/tag 真实状态；失败即定位修复并追加 routine 记录。
2. 对发布资产 ZIP、wheel 和校验和检查文件名、内容与对应 commit。
3. 使用获许可真实课程评估“完整讲解、逐题答案、复习速览、教师核心覆盖”，不把长度作为实质质量证明。
4. 后续开发受控课件解析和实际子智能体委派。

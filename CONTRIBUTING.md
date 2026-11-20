# Contributing / 参与贡献

感谢对教师主线课程整理、学习科学和隐私安全的改进建议。请先阅读 README、[开发者指南](docs/DEVELOPMENT.md)、[教学规范](references/pedagogy.md)及[版权门禁](references/copyright-gate.md)。

## 欢迎的贡献

- 经过授权或完全原创的样例课程、错误示范、不同学科测试案例。
- 教师板书/课次映射、学习目标与考核的质量评估方法。
- Python CLI 校验、文档交叉链接、双语说明、可访问性。
- 安全的本地解析适配器（不自动上传来源）与性能优化。

## 提 Issue 前

使用相应模板，说明版本、期待行为、实际行为、最小重现步骤及测试信息。请**不要**公开发布真实教师课件、学生作业、个人联系方式、学校账户信息、闭卷考试题目或未经授权的受版权保护内容。敏感安全问题见 [SECURITY.md](SECURITY.md)。

## Pull Request 流程

1. Fork 或创建功能分支，小步提交，说明对教师保真、课程结构和版权边界的影响。
2. 新增/修改行为尽可能配套测试。运行 `python -m unittest discover -s tests -v`、`course-org validate examples/sample-course`。
3. 修改 Skill 时核对对应的 `references/`、README.md 和 README_EN.md；不把规划功能写成已实现。
4. 每一次 GitHub 修改都写一篇 `docs/routine/YYYY-MM-DD-HHMM-summary.md`：日期、改动文件、行为变化、实际测试、限制、下一步。
5. PR 说明风险、验证记录；如果没有实际跑测试必须明示。
6. 在获得明确授权并经过评审前，不公开发布真实教师素材或将个人信息提交进仓库历史。

## 双语规范

面向用户的关键变更尽量同时维护简体中文与英文。技术术语可保留英文，但避免在两种 README 中出现相互矛盾的功能状态。

## Licensing and originality

提交者需有权许可其原创贡献，并遵守仓库 MIT License。不要将外部开源项目的提示词、模板、代码或课程练习直接复制进来而不核查许可证和要求。外部教育资源的使用权与我们仓库的 MIT 并不自动一致。

## Code of Conduct

见 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。讨论问题时尊重教师、学生和贡献者，针对具体事实和设计提出建议。

**English:** Submit original or appropriately licensed contributions, avoid private teacher/student data, run available tests, keep Chinese/English docs aligned, and include a dated docs/routine entry for every repository change.

# 2026-11-21 — 修复 v0.2.2 CI：新命令注册被旧 CLI 覆盖

## 真实问题
- 初次 v0.2.2 提交 a2cfe01 的 GitHub Actions [run 44780511324](https://github.com/Nimenta727/Course-Organization-Skill/actions/runs/44780511324) 在 Python 3.10、3.11、3.12 均失败。
- 单元测试日志明确指出 ready 不在 argparse 的可识别命令列表；原因是第二轮打包文档修改时基于旧 main 分支的 cli.py 覆盖了已暂存的新命令版本。
- student-check 与 review-gate 也遭到相同覆盖；另需将新的学生章节名加入原结构验证器。

## 本次修复
- 从本轮已创建且可查验的 Git blob 恢复含 student-check、review-gate、ready 的 CLI。
- 保留新增的九章学生版对应的结构验证兼容项：核心知识详解、例题精讲、易错点与纠正、分层作业。
- 没有添加教师原始课件、私有审核报告或学生资料。

## 当前验证与下一步
- 代码已重新提交；CI 是否通过须读取本次新提交对应的实际 Actions 状态，不将旧失败测试改写为成功。
- 下一步检查最新所有测试、样例学生深度门禁、wheel 打包以及默认不授权发布的安全预期；若仍有报错将继续修复。

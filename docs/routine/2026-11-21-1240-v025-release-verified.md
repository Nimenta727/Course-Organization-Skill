# 2026-11-21 12:40 — 最终 v0.2.5 Pre-release 及全部测试结果

## GitHub 发行实证
- 发布版本：https://github.com/Nimenta727/Course-Organization-Skill/releases/tag/v0.2.5
- GitHub Release API 返回 tag=v0.2.5, draft=false, prerelease=true, tag 对应 c9be0334f8f1689ce8cc291892686320117d125e。
- 实际资产：
  - course-organization-skill-v0.2.5.zip，50,022 bytes，完整可安装 Agent Skill（allowlist）
  - course_organization_skill-0.2.5-py3-none-any.whl，23,267 bytes，可选离线 Python CLI
  - SHA256SUMS.txt，218 bytes，前两项的校验清单
- GitHub 发布 workflow 44864291143 = success：版本核对、unittest、课程深度检查、版权示例 BLOCK、打包、ZIP 安全内容核查、创建 Release 均完成。
- GitHub CI 44864291167 = success，三个 Python job（3.10、3.11、3.12）的测试、完整 Skill ZIP 和 CLI wheel 都成功；Python 3.11 日志为 Ran 42 tests / OK。

## 本次文档修改
- README.md、README_EN.md、docs/INDEX.md、docs/RELEASE.md、docs/GITHUB_METADATA.md、CHANGELOG.md 补齐实际可核对的发行与测试链接；不是“准备发布”的空泛描述。
- 完成已知 Markdown 格式缺陷修复，v0.2.4 旧版仍保存在原始 GitHub Release 和标签中，不强推、不抹掉 Git 历史。
- 当前 docs/releases 只保留 v0.2.5 的活动说明；旧版源文件在对应 tag 和提交历史中可追溯。

## 质量/版权能力边界
- 42 个测试和发布成功表明工程文件/断言通过，不代表学生真的学会、老师内容全被独立核实，或七个真实子智能体审阅已经执行。
- review-plan 只创建独立审阅任务，review-gate 仅验证审阅记录字段；没有真实审阅必须保持 REVIEW_PENDING。
- 所有教师受版权保护资料、学生隐私、官方受限考试题公开使用均需独立合法授权。机器审核不能提供零版权风险保证。

## 下一步
1. 使用取得处理许可的真实课程做逐页教师内容覆盖评测，验证学生可读性、讲解深度、作业与答案真实性。
2. 增加真实独立审阅执行的权限控制与可验证证据，而不是使用虚构审阅报告。
3. 继续推进本地 PPTX/PDF/DOCX 文档抽取、增量课程更新和学科差异化测试。

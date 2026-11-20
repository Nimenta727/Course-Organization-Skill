# 2026-11-20 — 测试矩阵、标签同步、版本打包与预发布流水线

## 本轮变更
- 新增 .github/workflows/sync-labels.yml，在 GitHub Actions 权限允许时同步 .github/labels.json 中的分类标签。
- 改进 tests.yml：Python 3.10、3.11、3.12 矩阵，运行 unittest、示例课程验证、离线检索计划和默认版权 BLOCK。
- 新增 release.yml：需由维护者输入 RELEASE，执行一致性检查、测试及 wheel 构建，再创建 GitHub Pre-release。
- 新增 tests/test_repository.py：检查版本、Skill 入口、README 相对链接、发布门禁和 labels.json。
- 将 pyproject.toml、源代码版本更新为 0.2.1，补充打包元信息；CITATION 去除未实际完成发布的日期标记。
- 修复发布文档里转义的 Markdown 代码标记，使 README 与指南正常显示。

## 验证情况
- 已提交自动化测试定义与断言。是否实际通过，取决于 GitHub Actions 执行结果，尚不能仅依据 YAML 文件存在宣称测试成功。
- Source ZIP 包含完整 Skill；wheel 仅提供 Python CLI，不是完整 Skill 发行包。
- Release 工作流需人工明确触发，不由这次代码提交自动创建 tag 或 Release。

## 风险、限制
- 当前连接器未提供直接修改仓库 About / Topics 的接口；需要维护者在 GitHub UI 应用。
- GitHub Actions 是否启用、issues:write 和 contents:write 是否生效都需实际确认。
- 自动审核工具不提供任何零版权风险或人工内容质量保证。

## 下一步
1. 读取 Actions 运行记录，核实测试和标签同步，修复异常。
2. 在仓库 About 中设置 Description 与 Topics，核实显示。
3. 完成发布门禁的真实审核后，由维护者手动创建 v0.2.1 Pre-release。
4. 开始 v0.3 获授权课程资料的本地抽取与教师证据映射。

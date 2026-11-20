# 2026-11-20 — 加强私有索引的 Git 边界

## 本次变更
- 复查首次完整提交后的目录与代码。
- 修复 scan：即使输出路径位于原始资料目录之外，只要仍在 Git worktree 内，也禁止写入包含私有资料文件名的索引。
- .gitignore 明确忽略 source-manifest.json、private-source-manifest.json、private-index.json。
- 添加单元测试验证扫描器拒绝在 Git 仓库内写入敏感索引。

## 当前验证
- GitHub 仓库文件结构已验证；测试工作流已有配置。
- 检查时 GitHub Actions 尚无工作流运行记录，不能宣称测试通过。
- 新规则仍不能避免用户主动绕过或使用 git add -f 提交敏感数据；需人工审查。

## 下一步
- 核查 GitHub Actions 是否启用，运行 unittest 并处理失败。
- 扩展权限矩阵、字段校验与安全测试。
- 实现获许可资料的本地文档解析和课次证据映射。

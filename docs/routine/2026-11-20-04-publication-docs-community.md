# 2026-11-20 — 发布资料体系、双语 README 与社区治理

## 本轮修改内容
- 重写 README.md、README_EN.md，系统介绍项目定位、特色、功能状态、安装、课程样例、CLI、版权界限和开发路线。
- 新增 docs/QUICKSTART.md、INSTALLATION.md、USAGE.md、FAQ.md、DEVELOPMENT.md、RELEASE.md、GITHUB_METADATA.md。
- 新增 CHANGELOG.md、CONTRIBUTING.md、CODE_OF_CONDUCT.md、SECURITY.md、CITATION.cff 和 docs/releases/v0.2.1.md。
- 统一文档中的 v0.2.1 Preview 版本定位，不将规划中的自动文件解析、联网 CLI 或全课程生成误写为已完成。
- 准备 GitHub Description、Topics、Issue Labels 的详细设置说明（真正的仓库元数据修改需独立权限和动作）。

## 主要调整
- 强调教师主线、一课一文、初学与复习结合、学科差异化。
- 区分可移植 Skill 与本地 Python CLI 两种安装路径。
- 强调真实来源权限、私有教师材料与人类版权审核门禁。
- 明确示例 course-org audit 默认 BLOCK 是正确行为。

## 验证记录
- 当前阶段为文档内容和链接结构整理；GitHub Actions 实际测试状况需随后检查。
- 所有新增文档均为本项目原创编辑，未导入教师材料或复制第三方项目课程内容。

## 未解决问题
- 当前 GitHub 连接器没有编辑 Repository Description / Topics 或直接创建 Release 的写入接口；仅提供可执行说明和后续工作流配置。
- 仍需要在 GitHub Actions 或本地 Python 环境实际运行完整测试并确认成功。

## 下一步计划
1. 创建项目 Issue/PR 模板、标签定义和可控同步工作流。
2. 添加发布检查/构建工作流，核对 Skill frontmatter 与文档链接。
3. 使 pyproject / CLI / 更新记录的版本一致，验证结果后制作 v0.2.1 预发布。
4. 继续 v0.3 获授权文件解析与证据映射引擎。

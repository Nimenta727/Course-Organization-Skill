# v0.2.5 Preview 发布手册 / Release playbook

## 发行范围

这是**预览版 Agent Skill + 离线 Python CLI**，不是已支持自动解析所有教师 PPT/PDF、全课程自动生成或真实子智能体调度的产品。不能宣传成“版权安全得到绝对保证”，也不能将任何教师课件或学生数据混进发行物。

预发布版本号统一为 `v0.2.5`，Python 包为 `0.2.4`。对应 [发布说明](releases/v0.2.5.md)。

## 发行文件

| 制品 | 含义 |
| --- | --- |
| `course-organization-skill-v0.2.5.zip` | **完整可安装 Skill**：SKILL.md、references、assets/course-template、双语 README、LICENSE |
| `course_organization_skill-0.2.4-*.whl` | **仅 Python CLI**（不包含完整 Skill 指令和模板） |
| `SHA256SUMS.txt` | 上述 ZIP/wheel 的哈希，供下载核对 |
| GitHub 自动 Source code ZIP / tar.gz | 完整仓库源码、测试、文档和工作流 |

`scripts/package_skill.py` 严格按允许列表生成 ZIP，不打包未经授权教师资料、私有审阅记录、测试和 `docs/routine/`。GitHub 自动源码压缩包包含仓库全部已提交文件，仍需维护者审阅 Git 历史隐私风险。

## 强制发布前检查

- [ ] 仓库无教师原件、私人证据台账、学生资料、密钥或受限考试文件（包括可能的 Git 历史）。
- [ ] `SKILL.md` frontmatter、references、课程模板与 README 的命令真实一致。
- [ ] `pyproject.toml`、源码 `__version__`、CITATION、发布说明、README 全部为 `0.2.4`。
- [ ] `python -m unittest discover -s tests -v` 实际通过；Python 3.10、3.11、3.12 CI 成功。
- [ ] `course-org validate` 与 `student-check` 对虚构示例 PASS。
- [ ] `course-org audit examples/sample-course` 因示例未授权公开而 BLOCK。
- [ ] Skill ZIP 的源文件允许列表与可复现构建测试通过；wheel 可构建。
- [ ] 最新 `CHANGELOG` 和 `docs/routine/` 已记载真实行为变更与测试。
- [ ] Release 标记为 **Pre-release**，且明确区分独立审核、网络研究和版权审查的已实现/未实现状态。

## 手动与自动流程

`.github/workflows/release.yml` 包含显式批准、版本匹配校验、单元测试、CLI 结构/学生质量检查、版权示例默认拒绝、Skill ZIP/wheel 构建和 SHA-256 清单，再创建 GitHub Pre-release。若发行操作由获批准的 `main` 推送触发，需具有受限 `contents:write` 权限，依然要跑完整测试后才允许发布。已有同名版本不得覆盖，应该核实内容而非重写历史。

**注意：** 一个 GitHub 工作流文件的存在不等于已经发布；以 [Releases](https://github.com/Nimenta727/Course-Organization-Skill/releases) 和最新 Actions 的实际状态为准。如果权限或执行器未允许直接发布，应留下真实失败原因，不声称成功。

### 本地准备

~~~bash
python -m pip install -e .
python -m unittest discover -s tests -v
course-org validate examples/sample-course
course-org student-check examples/sample-course
course-org research-plan examples/sample-course
course-org review-plan examples/sample-course
python scripts/package_skill.py
python -m pip wheel . --no-deps --wheel-dir dist
sha256sum dist/*.zip dist/*.whl
~~~

`audit` 示例应 BLOCK；既不应改为 PASS，也不应将虚构审阅测试数据包装为真实审核报告。

## GitHub 元数据

仓库 About Description 与 12 Topics 已经过 API 核实存在；16 个 Issue labels 由此前 Actions 同步。见 [GITHUB_METADATA.md](GITHUB_METADATA.md)。这些标签设置与真正的版本 Release 是不同的操作。

## 发布后

检查 GitHub tag/Release URL 与对应提交、ZIP/wheel 名称、校验和、Releases 标题/Pre-release 状态、下载包内部目录以及 README 版本。将真实结果补充到 `docs/routine/` 的新记录；若失败修复后应使用新的提交，不能仅凭发布脚本“理论可运行”汇报发行成功。

**English:** v0.2.5 Preview includes a complete Skill ZIP, separate CLI wheel and checksums. Automated release must run tests and keep user-owned course material private. Do not claim publication until a GitHub release/tag actually exists.

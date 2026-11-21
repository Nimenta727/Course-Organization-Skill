# 安装与集成 / Installation

## 发行物的区别

| 文件 | 适合谁 | 包含什么 |
| --- | --- | --- |
| `course-organization-skill-v0.2.5.zip` | AI Agent 用户 | 完整 SKILL.md、references、assets、许可证、中英 README |
| `course_organization_skill-0.2.4-*.whl` | Python 用户 | `course-org` 离线扫描、课程质量和审阅记录检查 |
| GitHub 源码 ZIP / clone | 开发者 | 完整仓库、tests、docs、GitHub 配置、打包脚本 |

GitHub Release 制品如果尚未出现，请先从 [仓库](https://github.com/Nimenta727/Course-Organization-Skill) clone。Skill ZIP 不含 CLI；wheel 也不含完整教学 Skill。需要两者可分别安装。

## 一、安装 Skill

### 通用 Agent

解压完整 Skill 包，确认顶层目录里有 `SKILL.md`、`references/` 和 `assets/`。将目录放在宿主支持的 Skills 路径，或明确指示 Agent 按需读取 SKILL.md 中的引用。**Skill 不是模型权重，也不自动授权对本地文件和网页的访问。**

### Codex（macOS / Linux 示例）

~~~bash
git clone https://github.com/Nimenta727/Course-Organization-Skill.git \
  "$HOME/.local/share/course-organization-skill"
mkdir -p "$HOME/.agents/skills"
ln -s "$HOME/.local/share/course-organization-skill" \
  "$HOME/.agents/skills/course-organization"
~~~

客户端的实际发现机制可能调整，参见[官方 Skills 文档](https://developers.openai.com/api/docs/guides/tools-skills)。

### Claude Code（macOS / Linux 示例）

先 clone 到上面的本地目录，再建立相应链接：

~~~bash
mkdir -p "$HOME/.claude/skills"
ln -s "$HOME/.local/share/course-organization-skill" \
  "$HOME/.claude/skills/course-organization"
~~~

[Claude Code Skills 文档](https://code.claude.com/docs/en/skills)为当前路径要求的权威参考。已存在的目录/链接不要无意覆盖。

### Windows

可将完整解压目录复制到客户端的项目级或用户级 Skills 目录，必要时使用 PowerShell 复制命令。具体位置取决于宿主，不能假定每个 AI App 支持自动发现。任何情况下都**不要把教师原件/学生资料放进 Skill 的安装目录**。

## 二、安装 Python CLI（可选）

支持 Python 3.10、3.11、3.12；更新的 Python 版本尚未纳入本项目的 CI 矩阵。

~~~bash
git clone https://github.com/Nimenta727/Course-Organization-Skill.git
cd Course-Organization-Skill
python -m venv .venv
# macOS / Linux:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
python -m pip install -e .
course-org --help
~~~

也可以先下载 GitHub Release 的 wheel 并使用 `python -m pip install /path/to/file.whl`。这只安装 CLI，不会注册 Agent Skill。

## 三、验证安装

~~~bash
python -m unittest discover -s tests -v
course-org validate examples/sample-course
course-org student-check examples/sample-course
course-org research-plan examples/sample-course
course-org review-plan examples/sample-course
~~~

示例的 `audit` 与无有效报告的 `ready` **预期 BLOCK**。详细解释见 [快速开始](QUICKSTART.md)。

## 四、更新与卸载

更新 clone 的 Skill 时先确认没有未提交修改，然后 `git pull --ff-only`。升级可选 CLI 可重新 `python -m pip install -e .`；卸载为 `python -m pip uninstall course-organization-skill`。删除自己创建的 Skill 链接或副本即可移除其注册，不要误删其他项目共享目录。

**English:** The Skill ZIP and CLI wheel are separate distribution formats. Extract/install the full Skill directory for compatible agents, and optionally install the CLI on Python 3.10–3.12. The CLI cannot access the web, run AI models, parse PPT/PDF contents, or independently establish copyright clearance.

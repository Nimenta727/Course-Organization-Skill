# 安装与集成 / Installation and integration

## 先看：两种安装是独立的

1. **安装 Agent Skill**：让支持 Agent Skills 的 AI 读取 `SKILL.md` 和所需 `references/`，帮助规划与创作课程。无需 Python 包。
2. **安装本地 CLI**：获得确定性的 `course-org` 元数据扫描、课程结构检查和发布声明审核。CLI 本身不能生成完整课程，也不能联网搜索。

确保运行环境有使用课程资料的权限；不要把教师 PPT、录音和学生作品放进公开 Git 仓库。

## 一、获取仓库 / Clone

~~~bash
git clone https://github.com/Nimenta727/Course-Organization-Skill.git
cd Course-Organization-Skill
~~~

不必将此仓库放在教师原始资料目录中。建议把教师资料放在另一个有适当访问控制的私有路径中。

## 二、Agent Skill 安装 / Agent Skills

### 方案 A：让任意具备文件读取能力的 Agent 直接读取

向 Agent 提供本仓库 `SKILL.md` 的路径，并确保它可以按需读取 `references/` 和 `assets/`。推荐先要求“查看计划、不做不可逆文件操作”。

### 方案 B：Codex (project or user level)

示例为 macOS/Linux 的 **用户级**安装。先复制或克隆仓库到私有的常规工具目录：

~~~bash
mkdir -p "$HOME/.local/share"
git clone https://github.com/Nimenta727/Course-Organization-Skill.git \
  "$HOME/.local/share/course-organization-skill"
mkdir -p "$HOME/.agents/skills"
ln -s "$HOME/.local/share/course-organization-skill" \
  "$HOME/.agents/skills/course-organization"
~~~

如果该链接已存在，不要覆盖，先检查是否指向旧版本。项目级 Skills 通常放在项目的 `.agents/skills/` 中。客户端版本可能调整发现规则，请以[官方 OpenAI Skills 文档](https://developers.openai.com/api/docs/guides/tools-skills)及客户端说明为准。

### 方案 C：Claude Code

同样可以在用户级 Skills 目录放入完整的 Skill：

~~~bash
mkdir -p "$HOME/.claude/skills"
ln -s "$HOME/.local/share/course-organization-skill" \
  "$HOME/.claude/skills/course-organization"
~~~

前提是上一步已克隆到该地址。项目级 Skills 通常位于 `.claude/skills/`。请参见[Claude Code Skills 文档](https://code.claude.com/docs/en/skills)。

### Windows 提示

在 PowerShell 中可将仓库目录复制到受支持的用户级或项目级 Skills 目录（无需创建符号链接）。路径和刷新步骤由对应客户端决定。不要把教师原始文件复制到 Skills 安装目录。

### 注意事项

- 这是一个可移植的 Agent Skill，并非已发布在各家官方插件目录中的插件。
- 如果 Agent 不支持自动 Skill 发现，可以显式提示它读取 `SKILL.md`。
- 即使 Skill 正确安装，也不能自动赋予 Agent 访问个人文件、网络或第三方应用的权限。
- 对教师资料是否允许传入模型，应遵守学校要求、相关许可及服务条款。

## 三、可选 Python CLI

要求 Python 3.10 或更新版本：

~~~bash
python --version
python -m pip install -e .
course-org --help
python -m unittest discover -s tests -v
~~~

此步骤安装本地实用程序，不会安装模型权重、调用在线 API 或自动同步课程文件。可在虚拟环境中执行：

~~~bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
~~~

Windows 激活示例：

~~~powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -e .
~~~

如需只试用不安装，位于仓库根目录时通常可通过设置 `PYTHONPATH=src` 执行 `python -m course_org.cli --help`。

## 四、更新与卸载

更新源仓库：在 **无未提交改动**时执行 `git pull --ff-only`；将版本变更记录与教学规范一并审阅。CLI 可重复执行 `python -m pip install -e .`。

移除 CLI：`python -m pip uninstall course-organization-skill`。移除 Skill：删除自己创建的符号链接或副本；不要误删与其他项目共享的源目录。

## 五、验证安装

~~~bash
course-org validate examples/sample-course
course-org research-plan examples/sample-course
course-org audit examples/sample-course
~~~

最后一个命令预期阻止发布。它返回非零不代表安装失败，而是版权审批默认没有放行。

**English overview:** Clone the repository. Install the entire directory as a supported Agent Skill (Codex: `~/.agents/skills/`, Claude Code: `~/.claude/skills/`, subject to current client behavior). Optionally run `python -m pip install -e .` to get the local metadata CLI. Do not place copyrighted course originals or private student information inside the repository.

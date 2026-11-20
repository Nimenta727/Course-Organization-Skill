# 开发者指南 / Developer guide

## 代码分层

\`\`\`text
SKILL.md                   Agent 入口：任务路由、流程、强制安全边界
references/                按教学阶段和学科加载的规范（真正的课程规则）
assets/course-template/    课程项目生成模板
src/course_org/
  cli.py                   stdlib Python CLI：scan/validate/audit
  quality.py               教师证据台账与资料元数据校验、离线检索计划
examples/sample-course/    原创课程测试样本
tests/                     unittest
docs/routine/              每次 GitHub 修改的日期、事项、测试、下一步
\`\`\`

大部分工作是 Agent 运行时的**行为规范**，不是 Python 引擎。不要把不存在的网络调用、PDF 解析、词向量索引或版权算法误写成已实现。

## 本地开发

~~~bash
git clone https://github.com/Nimenta727/Course-Organization-Skill.git
cd Course-Organization-Skill
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m unittest discover -s tests -v
course-org validate examples/sample-course
course-org research-plan examples/sample-course
~~~

示例的发布审计应阻断：

~~~bash
if course-org audit examples/sample-course; then
  echo "ERROR: sample was accidentally approved for public release"
  exit 1
fi
~~~

## PR 标准

- 修改 Skill 行为时同时更新 \`SKILL.md\`、对应 \`references/\`、双语 README 或相关指南，以及测试/示例。
- 变更必须在 \`docs/routine/YYYY-MM-DD-HHMM-description.md\` 中写明日期、修改内容、文件、实际验证、风险、下一步。
- 涉及教师内容需带可核验的人工模拟/许可齐全示例，避免将真实来源直接纳入 git。
- 在 PR 描述中分别列出“已执行测试”和“无法验证的事项”，不要虚构运行结果。
- 内容输出必须遵守一课一篇、老师主线、推理/误区补全、不同学科策略、来源不造假及版权默认审慎。
- 不要在静态审计器中做出“零侵权保证”，不要从别人的开源项目直接复制未经确认许可的模板或提示词。

## 版本策略

- 目前 \`0.x\` 为预览阶段。文档/打包修复增加 patch 版本，兼容的能力增加 minor 版本，重大工作流变化通过变更记录公告。
- 正式发布流程见 [RELEASE.md](RELEASE.md)；\`docs/releases/\` 保存各版本说明。
- 未完成的功能应留在 Roadmap，而不是 README 的“已实现”表格。

## 潜在技术扩展

依次考虑离线抽取器（PDF/PPTX/DOCX，严格本地授权）、逐段来源识别和哈希、增量依赖图、课程目标覆盖自动评估、原创新题独立求解、结构化引用登记、人工审核界面。每一步先证明权限、可追溯性与可维护性。

**English:** Keep the Skill instructions, deterministic CLI, examples and public docs in sync. Run unittest and sample checks, record every GitHub modification under docs/routine/, preserve privacy and copyright vetoes, and do not claim functionality or verification not actually observed.

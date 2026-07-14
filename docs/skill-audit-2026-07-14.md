# 现有 Skill 审计报告（2026-07-14）

## 结论摘要

本次审计覆盖仓库原有 18 个顶层 Skill。结论如下：

- `recommended`：2 个，当前内容和上游一致或仍适合作为默认选择。
- `maintained`：2 个，仍有独特价值，但需要本仓库继续维护。
- `deprecated`：13 个，不建议从本仓库安装，改用官方插件或活跃上游。
- `unverified`：1 个，缺少可核验的来源和许可证。

`deprecated` 表示停止新装，不等于文件立即删除。仓库先记录替代品、迁移理由和来源；涉及大量文件、许可证或历史清理的删除，单独提交并在 PR 中明确说明。

## 审计方法

1. 检查每个目录是否包含 `SKILL.md`，并用当前 `skill-creator` 校验器检查 frontmatter。
2. 扫描本机绝对路径、可疑远程执行命令、占位符和相对引用。
3. 对同名本机 Skill、Codex 官方/精选插件缓存和可信上游执行文件或目录差异比较。
4. 通过 GitHub API 核对官方仓库的归档状态、许可证、最近推送和最新 Release。
5. 替代判断优先考虑官方支持、更新机制、许可证、Codex 兼容性和功能完整度，不以 Star 数单独决策。

静态结果：18 个目录均有 `SKILL.md`；16 个通过当前 `skill-creator` 结构校验。`drawio-skill` 使用了当前校验器不接受的顶层 frontmatter 字段，`planning-with-files` 2.37.0 使用了 Codex 不消费的 Claude hooks 字段。未发现真实本机绝对路径或凭据；扫描到的 Windows 路径只出现在跨平台路径转换示例中。

## 逐项结论

| Skill | 状态 | 证据与问题 | 替代或维护决定 |
|---|---|---|---|
| `brainstorming` | deprecated | 与本机 Superpowers 6.1.1 版本存在显著差异，包含脚本和工作流更新。 | 改用 Codex 官方插件市场中的 **Superpowers**；不再单独安装此副本。 |
| `code-review-and-quality` | unverified | 结构有效，但仓库内没有上游、作者或许可证信息，无法确认来源和维护状态。 | 暂不默认推荐。代码审查优先用 Superpowers 的 `requesting-code-review`，安全审查另用 `security-best-practices`。 |
| `docx` | deprecated | `LICENSE.txt` 明确禁止从服务中提取、长期保留、复制和向第三方分发；公开仓库不应继续把它作为可安装副本宣传。 | Codex 中改用官方 **Documents** 插件。当前副本列入许可证清理清单，不再由安装器提供。 |
| `drawio-skill` | deprecated | 仓库版标记 1.5.2，官方最新 Release 为 1.32.0；当前校验器还会拒绝其额外顶层 frontmatter 字段。 | 从 [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) 安装最新版。 |
| `hatch-pet` | maintained | 属于本机自有工作流；仓库副本明显落后于本机版本，本机版本增加了方向一致性、色边清理和自动化测试。 | 保留本仓库维护，后续以经过验证的本机版本同步，不依赖不明第三方上游。 |
| `mcp-builder` | recommended | 本地 `SKILL.md` Git blob 与 [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) 当前上游一致，许可证为 Apache-2.0。 | 保留。适合设计 MCP Server；协议细节仍应以 [Model Context Protocol 官方文档](https://modelcontextprotocol.io/) 为准。 |
| `planning-with-files` | deprecated | 仓库版 2.37.0，本机版 3.1.3，官方最新 Release 已为 3.5.0；仓库版 frontmatter 带 Codex 不消费的 hooks。 | 从 [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) 安装最新版，不再维护旧镜像。 |
| `ppt-master` | deprecated | `SKILL.md` 与上游当前文件哈希不一致；上游最新 Release 为 3.1.0，仍在高频更新。仓库副本超过 1.2 万文件，直接复制会快速失去同步。 | 改用 `npx skills add hugohe3/ppt-master`，并按上游说明安装 Python 依赖。 |
| `project-memory` | maintained | 结构有效、体量小、无外部执行依赖；与 `planning-with-files` 的任务态记录不同，它保存跨会话的长期项目约束。 | 保留为轻量长期记忆层；进入 Multica 后可逐步迁移到平台知识与记忆服务。 |
| `systematic-debugging` | deprecated | 本机 Superpowers 6.1.1 已包含新版和 Codex 插件元数据。 | 改用 Superpowers 插件版本。 |
| `test-driven-development` | deprecated | 本机 Superpowers 6.1.1 已包含新版和 Codex 插件元数据。 | 改用 Superpowers 插件版本。 |
| `ui-ux-pro-max` | deprecated | 仓库描述仍为 50+ 风格、10 个技术栈；官方最新 Release 2.11.0 已扩展能力并要求通过 CLI 生成对应 Agent 版本。 | 使用官方 `uipro-cli` 安装 Codex 版本，来源为 [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)。 |
| `using-superpowers` | deprecated | 当前官方实现已改为 Codex 原生插件分发，仓库副本缺少完整插件生命周期和同套 Skill。 | 在 Codex 插件市场安装完整 Superpowers，不单装引导 Skill。 |
| `verification-before-completion` | deprecated | 本机 Superpowers 6.1.1 已包含带 Codex 元数据的版本。 | 改用 Superpowers 插件版本。 |
| `webapp-testing` | deprecated | 文件与 Anthropic 当前上游一致且为 Apache-2.0，但其主要流程是临时编写 Python Playwright 脚本；Codex 当前已有持久浏览器交互与专用网页测试 Skill。 | 交互式调试优先 `playwright-interactive`，可重复网页自动化优先 `playwright`，轻量浏览器操作可选 `agent-browser`。 |
| `web-design-guidelines` | recommended | `SKILL.md` Git blob 与 [Vercel 上游](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) 完全一致。 | 保留；每次执行会拉取远程最新规则，应将远程内容视为不可信输入并审查变更。 |
| `writing-plans` | deprecated | 本机 Superpowers 6.1.1 增加了上下文隔离、计划审查和 Codex 插件元数据。 | 改用 Superpowers 插件版本。 |
| `xlsx` | deprecated | 与 `docx` 相同，许可证明确限制复制、保留与分发；不适合作为公开仓库内可安装副本。 | Codex 中改用官方 **Spreadsheets** 插件。当前副本列入许可证清理清单，不再由安装器提供。 |

## 推荐的迁移顺序

1. 在 Codex 插件市场安装或保留 **Superpowers**，停止分别安装六个旧副本。
2. 用上游最新版替代 `planning-with-files`、`drawio-skill`、`ui-ux-pro-max` 和 `ppt-master`。
3. 用 Codex 的 Documents、Spreadsheets 插件替代 `docx`、`xlsx`，并单独处理旧文件和 Git 历史中的许可证风险。
4. 网页测试迁移到 `playwright-interactive` / `playwright` / `agent-browser`，按持久交互、可重复测试和轻量操作区分使用。
5. 保留 `mcp-builder`、`web-design-guidelines`、`hatch-pet` 和 `project-memory`；其中 `hatch-pet` 后续同步本机已验证版本。

## 一手来源

- [Superpowers 仓库](https://github.com/obra/superpowers)；[v6.1.1 Release](https://github.com/obra/superpowers/releases/tag/v6.1.1)
- [planning-with-files 仓库](https://github.com/OthmanAdi/planning-with-files)；[v3.5.0 Release](https://github.com/OthmanAdi/planning-with-files/releases/tag/v3.5.0)
- [PPT Master 仓库](https://github.com/hugohe3/ppt-master)；[v3.1.0 Release](https://github.com/hugohe3/ppt-master/releases/tag/v3.1.0)
- [UI/UX Pro Max 仓库](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)；[v2.11.0 Release](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases/tag/v2.11.0)
- [drawio-skill 仓库](https://github.com/Agents365-ai/drawio-skill)；[v1.32.0 Release](https://github.com/Agents365-ai/drawio-skill/releases/tag/v1.32.0)
- [Anthropic Skills 仓库](https://github.com/anthropics/skills)
- [Vercel Agent Skills 仓库](https://github.com/vercel-labs/agent-skills)

以上版本和维护状态核验于 2026-07-14。外部项目可能随时更新，目录中的 `verified_on` 用于触发后续复查。

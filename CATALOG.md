# Codex Skill 精选目录

核验日期：2026-07-29。结构化事实源为 [`catalog/skills.yaml`](catalog/skills.yaml)；本页为方便阅读的摘要。外部项目会变化，安装前仍应打开上游确认最新版说明。

## 快速选择

| 想做什么 | 首选 | 何时换用其他工具 |
|---|---|---|
| 系统化网络调研 | `deep-research` | 需要真实登录态和人工式浏览时加 `kimi-webbridge`；做周期生态扫描时用 `scouting-ai-ecosystem`。 |
| 控制真实浏览器 | `kimi-webbridge` | 需要可重复 CLI 自动化时用 `agent-browser`；调试本地 Web/Electron 时用 `playwright-interactive`。 |
| 查最新开发文档 | `find-docs` | Context7 缺失或安全关键时，回到产品官方文档。 |
| 软件工程全流程 | `superpowers` | 超过五次工具调用、需要跨会话状态时叠加 `planning-with-files-upstream`。 |
| 交付任务包 | `task-package-delivery` | 单纯问答、小改动或只读诊断无需触发任务包流程。 |
| 协调审查—修复闭环 | `coordinate-review-repair-loops` | 单一实施或单次审查直接使用对应执行/审查流程。 |
| 决策级调研 | `research-governance` + `deep-research` | 前者管理证据、Gate 和决策边界，后者负责外部发现与核验。 |
| 项目知识收尾 | `neat-freak` | 纯代码重构、普通数据整理或无项目知识语境的“整理”不使用。 |
| 压力测试方案 | `grill-me` | 已有完整批准规格时直接进入计划或执行。 |
| 架构改进 | `improve-codebase-architecture` | 先补领域模型和 ADR，再授权具体重构。 |
| MCP Server | `mcp-builder` | 协议、SDK 与安全边界以 MCP 官方文档为准。 |
| Word / Excel | `openai-documents` / `openai-spreadsheets` | 不再安装仓库内 `docx`、`xlsx` 旧副本。 |
| PPT | Codex Presentations 插件 | 需要高度可编辑 SVG、模板复刻和动画流水线时选 `ppt-master-upstream`。 |
| UI/UX 设计与审查 | `ui-ux-pro-max-upstream` + `web-design-guidelines` | 前者做设计系统，后者做界面规则审查。 |

## 仓库内可安装 Skill

| Skill | 状态 | 用途 | 安装 | 主要风险 |
|---|---|---|---|---|
| `scouting-ai-ecosystem` | recommended | 定期发现并评估 Agent、Skill、MCP、RAG 与 AI Native 项目 | `./scripts/install-skill.ps1 -Name scouting-ai-ecosystem` | 调研具有时效性，必须核对一手来源。 |
| `mcp-builder` | recommended | 设计、实现、测试和评估 MCP Server | `./scripts/install-skill.ps1 -Name mcp-builder` | MCP 可能获得外部系统读写权限。 |
| `web-design-guidelines` | recommended | 审查 UI、UX 和可访问性 | `./scripts/install-skill.ps1 -Name web-design-guidelines` | 会读取远程最新规则，应防范提示注入。 |
| `hatch-pet` | maintained | 生成并校验 Codex 动画宠物图集 | `./scripts/install-skill.ps1 -Name hatch-pet` | 图像、品牌和商标素材需要授权。 |
| `project-memory` | maintained | 保存轻量跨会话项目记忆 | `./scripts/install-skill.ps1 -Name project-memory` | 记忆文件可能含内部信息。 |
| `task-package-delivery` | recommended | 按范围与验收合同实施、验证、审查并有界收敛 | `./scripts/install-skill.ps1 -Name task-package-delivery` | 不自动扩大提交、发布或破坏性操作权限。 |
| `research-governance` | recommended | 将调研转成可审计的证据、Gate 与决策记录 | `./scripts/install-skill.ps1 -Name research-governance` | 调研通过不等于实施、采购或生产授权。 |
| `coordinate-review-repair-loops` | maintained | 事件驱动协调实施、复审、修复和控制面收口 | `./scripts/install-skill.ps1 -Name coordinate-review-repair-loops` | 必须先冻结任务范围、权限和停止条件。 |

macOS/Linux 将命令替换为：

```bash
./scripts/install-skill.sh <skill-id>
```

## 外部推荐与维护项

| 条目 | 状态 | 官方来源 | 推荐安装方式 | 注意事项 |
|---|---|---|---|---|
| `superpowers` | recommended | [obra/superpowers](https://github.com/obra/superpowers) | Codex **Plugins** 页面搜索 Superpowers | 不要再分别安装仓库里的六个旧副本。 |
| `planning-with-files-upstream` | recommended | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | `npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g -a codex` | 会写项目计划文件，网页内容只作为数据。 |
| `drawio-skill-upstream` | recommended | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | `npx skills add Agents365-ai/drawio-skill -g -a codex` | 需要 Draw.io Desktop CLI。 |
| `ppt-master-upstream` | maintained | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | `npx skills add hugohe3/ppt-master -g -a codex` | 还需按上游安装 Python 依赖，云 API 可能接触业务材料。 |
| `ui-ux-pro-max-upstream` | recommended | [uupm.cc](https://uupm.cc) / [GitHub](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `npm install -g uipro-cli`，再运行 `uipro init --ai codex` | CLI 会在当前目录生成平台文件。 |
| `openai-documents` | recommended | [OpenAI Skills](https://github.com/openai/skills) | Codex **Plugins** 页面安装 Documents | 文档敏感数据需遵守组织数据策略。 |
| `openai-spreadsheets` | recommended | [OpenAI Skills](https://github.com/openai/skills) | Codex **Plugins** 页面安装 Spreadsheets | 交付前检查公式、链接和宏。 |
| `kimi-webbridge` | recommended | [产品页](https://www.kimi.com/zh-cn/features/webbridge) / [安装指南](https://www.kimi.com/zh-cn/help/kimi-webbridge/kimi-webbridge-introduction) | 按官方指南安装本地服务，并从 [Chrome 商店](https://chromewebstore.google.com/detail/kimi-webbridge/fldmhceldgbpfpkbgopacenieobmligc) 或 [Edge 商店](https://microsoftedge.microsoft.com/addons/detail/kimi-webbridge/bnlffdbcfnanfbknnlaflhlhkocccckg) 安装扩展 | 可控制真实登录态；提交、付款、发布前再次确认。 |
| `deep-research` | recommended | [ByteDance DeerFlow](https://github.com/bytedance/deer-flow/tree/main/skills/public/deep-research) | `npx skills add bytedance/deer-flow --skill deep-research -g -a codex` | 搜索结果要回到一手来源交叉验证。 |
| `agent-browser` | recommended | [agent-browser.dev](https://agent-browser.dev) / [GitHub](https://github.com/vercel-labs/agent-browser) | `npm install -g agent-browser`，再运行 `agent-browser install` | 浏览器配置、登录态和云提供商凭据属于敏感数据。 |
| `find-docs` | recommended | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs) | `npm install -g ctx7@latest`，再安装 Skill | 第三方索引不替代官方文档。 |
| `grill-me` | maintained | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) | `npx skills add mattpocock/skills --skill grill-me -g -a codex` | 会增加交互轮次。 |
| `improve-codebase-architecture` | maintained | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) | `npx skills add mattpocock/skills --skill improve-codebase-architecture -g -a codex` | 诊断结果不等于授权重构。 |
| `security-best-practices` | recommended | [OpenAI Skills](https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices) | Codex **Plugins** 页面安装 | 只覆盖部分语言和框架，不替代威胁建模与渗透测试。 |
| `playwright-interactive` | recommended | [OpenAI Skills](https://github.com/openai/skills/tree/main/skills/.curated/playwright-interactive) | Codex **Plugins** 页面安装，并按说明启用 `js_repl` | 当前可能要求降低沙箱限制，只在可信项目中使用。 |
| `markdown-writer` | maintained | [TerminalSkills/skills](https://github.com/TerminalSkills/skills/tree/main/skills/markdown-writer) | `npx skills add TerminalSkills/skills --skill markdown-writer -g -a codex` | 示例命令和 URL 只是模板，发布前必须替换和验证。 |
| `open-code-review-delegate` | recommended | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 安装 `@alibaba-group/open-code-review`，再按上游 Delegation Mode 文档安装 Skill | OCR 只确定范围与规则，最终结论仍需宿主 Agent 独立复核。 |
| `neat-freak` | maintained | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills/tree/main/neat-freak) | `npx skills add KKKKhazix/khazix-skills --skill neat-freak -g -a codex` | 上游采用 MIT；发现清理候选不等于获得删除授权。 |

## 弃用与迁移

仓库安装器会拒绝以下条目。

| 旧条目 | 替代品 | 原因 |
|---|---|---|
| `brainstorming` | `superpowers` | 单独旧副本缺少完整插件生命周期。 |
| `docx` | `openai-documents` | 许可证限制复制和再分发，Codex 已有官方插件。 |
| `drawio-skill` | `drawio-skill-upstream` | 仓库 1.5.2，官方已到 1.32.0。 |
| `planning-with-files` | `planning-with-files-upstream` | 仓库 2.37.0，官方已到 3.5.0。 |
| `ppt-master` | `ppt-master-upstream` | 大型镜像已偏离高频更新的官方 3.1.0。 |
| `systematic-debugging` | `superpowers` | 插件版更新且带 Codex 元数据。 |
| `test-driven-development` | `superpowers` | 应与完整工程工作流一起安装。 |
| `ui-ux-pro-max` | `ui-ux-pro-max-upstream` | 官方 2.11.0 已显著扩展并改用 CLI 生成。 |
| `using-superpowers` | `superpowers` | Codex 原生插件已取代手工引导安装。 |
| `verification-before-completion` | `superpowers` | 插件版与评审和分支完成流程协同。 |
| `webapp-testing` | `playwright-interactive` | 当前持久会话更适合迭代功能与视觉 QA。 |
| `writing-plans` | `superpowers` | 新版包含上下文隔离和计划审查。 |
| `xlsx` | `openai-spreadsheets` | 许可证限制复制和再分发，Codex 已有官方插件。 |

## 待核验

| 条目 | 缺口 | 当前建议 |
|---|---|---|
| `code-review-and-quality` | 缺少可核验上游、作者和许可证 | 不新装；一般审查用 Superpowers，安全审查用 `security-best-practices`。 |
| `style-alchemy` | 本机自有，尚未公开，需核验样本和版权边界 | 完成脱敏、许可证和模仿风险审查后再发布。 |
| `work-reporting` | 本机自有，包含组织与个人数据假设 | 去除个人路径、组织规则和敏感信息后再发布。 |

完整字段、依赖和风险说明见 [`catalog/skills.yaml`](catalog/skills.yaml)。

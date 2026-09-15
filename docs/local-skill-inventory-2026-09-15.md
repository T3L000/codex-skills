# 本机 Skill 同步清单（2026-09-15）

本次从 Codex 与 Agents 的本机用户技能目录盘点出 92 个去重后的普通 Skill。公开仓库只同步许可证明确允许再分发的 19 个 Skill；其余条目仅记录名称，不在本次操作中复制或更新正文。

## 同步范围

- 来源目录：用户级 `.codex/skills` 与 `.agents/skills`。
- `dws` 在两处来源中的 161 个文件逐项哈希一致，因此只保留一份。
- 排除 Codex 托管的 `.system` 目录及其中 6 个系统 Skill。
- 排除 `__pycache__`、`.pyc`、`.env`、`.env.*`、管理标记、嵌套 `.git`、`node_modules` 和本机压缩包。
- 静态凭据扫描未发现私钥、真实 GitHub Token、AWS Access Key 或本次项目曾使用的 API Key。

## 已同步正文（19）

| Skill | 许可证 | 备注 |
|---|---|---|
| `audience-adapter` | MIT | 本机副本，来源待核验 |
| `cloudflare-deploy` | Apache-2.0 | 上游快照，暂不建议从镜像安装 |
| `deep-probe` | MIT | 作者信息存在，具体上游待核验 |
| `dws` | Apache-2.0 | 两处本机副本去重 |
| `hatch-pet` | Apache-2.0 | 更新仓库已有副本 |
| `idea-to-prd` | MIT | 本机副本，来源待核验 |
| `jupyter-notebook` | Apache-2.0 | 上游快照 |
| `mcp-builder` | Apache-2.0 | 与仓库已有副本一致 |
| `netlify-deploy` | Apache-2.0 | 上游快照 |
| `pdf` | Apache-2.0 | 上游快照 |
| `playwright` | Apache-2.0 | 上游快照 |
| `playwright-interactive` | Apache-2.0 | 上游快照 |
| `render-deploy` | Apache-2.0 | 上游快照 |
| `screenshot` | Apache-2.0 | 上游快照 |
| `security-best-practices` | Apache-2.0 | 上游快照 |
| `security-ownership-map` | Apache-2.0 | 上游快照 |
| `security-threat-model` | Apache-2.0 | 上游快照 |
| `vercel-deploy` | MIT | 具体上游待核验 |
| `weighted-scoring` | MIT | 本机副本，来源待核验 |

除仓库原先已维护的 `hatch-pet` 和 `mcp-builder` 外，本次加入或改为镜像分发的条目统一标记为 `unverified`，安装器不会把它们当作推荐或维护中的可安装项。

## 未在本次同步正文（73）

以下 Skill 缺少目录内明确许可证、属于更适合从活跃上游安装的外部项目，或仓库中已有独立治理版本。本次没有复制或覆盖它们的本机正文：

`academic-writing`、`agent-browser`、`ai-writing-detox`、`amazon-asin-monitor`、`analyze-content`、`api-tester`、`ask-matt`、`build-graph`、`code-review`、`codebase-design`、`codex-task-messenger`、`coordinate-review-repair-loops`、`data-analysis`、`data-journalism`、`data-validator`、`debug-issue`、`deep-research-modes`、`diagnosing-bugs`、`docker-helper`、`domain-modeling`、`ebilibili-video-download`、`eli5`、`excel-processor`、`execute-spec-in-fork`、`explore-codebase`、`find-docs`、`goal-crafter`、`grill-me`、`grill-with-docs`、`grilling`、`handoff`、`implement`、`improve-codebase-architecture`、`kimi-webbridge`、`log-analyzer`、`markdown-writer`、`neat-freak`、`newsroom-style`、`open-code-review`、`open-code-review-delegate`、`pdf-analyzer`、`planning-with-files`、`plotly`、`prompt-tester`、`prototype`、`refactor-safely`、`resolving-merge-conflicts`、`review-changes`、`review-delta`、`review-pr`、`sandaki-image-api`、`scouting-ai-ecosystem`、`setup-matt-pocock-skills`、`spec-executor`、`sql-optimizer`、`style-alchemy`、`systematic-debugging`、`tabbit`、`task-package-delivery`、`tdd`、`teach`、`technical-writer`、`to-goal`、`to-questionnaire`、`to-spec`、`to-tickets`、`triage`、`wait-what`、`watch`、`wayfinder`、`wizard`、`work-reporting`、`writing-for-agents`。

要公开同步其中任一正文，需要先确认作者、上游地址、当前许可证和再分发条件。仅仅安装在本机不构成公开再分发授权。

## 审计限制

本次使用文件名、扩展名、常见凭据模式、reparse point、文件大小与许可证文件进行静态检查。静态扫描不能证明所有示例数据均为虚构，也不能替代逐项上游许可证审计。

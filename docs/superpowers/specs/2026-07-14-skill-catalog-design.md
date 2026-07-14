# Codex 实用 Skill 目录设计

## 目标

将 `T3L000/codex-skills` 建设成一个可维护的个人 Codex Skill 目录。读者能够快速了解某个 Skill 的用途，找到可信的一手来源，安全地完成安装，并明确区分仓库内维护的 Skill 与外部维护的第三方 Skill。

## 当前情况

- 仓库当前在 `skills/` 下保存了 18 个 Skill。
- 仓库约有 1.2 万个文件、26 MB 内容，主要是文档和演示文稿类 Skill 包含了较多模板与资源文件。
- 当前 README 只列出 Skill 名称和手动复制方法，没有记录上游项目、官网、许可证、依赖、更新方法及核验日期。
- 本机 Codex 约有 47 个非系统 Skill，来源包括个人创建、官方、精选插件和第三方仓库。

## 采用方案

采用“精选目录 + 自有 Skill 入库”的混合方案：

1. 保留当前已经入库的 Skill，不做无关重构。
2. 只复制由本仓库作者创建或明确决定在本仓库维护的 Skill。
3. 第三方 Skill 只记录可信上游来源和安装方式；未完成来源与许可证核验时，不复制其代码。
4. 同时提供方便人阅读的文档和方便程序处理的结构化元数据。
5. 定期审计仓库现有 Skill；发现失效、重复、上游停更或出现明显更优替代品时，更新记录并提供迁移方案。

这种方式既能将仓库作为个人备份和安装入口，也能避免仓库变成来源不清、更新滞后的第三方代码镜像。

## 仓库结构

```text
README.md
CATALOG.md
catalog/
  skills.yaml
docs/
  selection-policy.md
  superpowers/specs/2026-07-14-skill-catalog-design.md
scripts/
  install-skill.ps1
  install-skill.sh
skills/
  <已有 Skill>
  scouting-ai-ecosystem/
```

### 文件职责

- `README.md`：仓库简介、快速安装、目录入口和维护方式。
- `CATALOG.md`：按类别展示精选 Skill，记录用途、来源、官网、安装方式和维护状态。
- `catalog/skills.yaml`：保存规范化的 Skill 元数据，作为后续检查与自动化的唯一结构化数据源。
- `docs/selection-policy.md`：说明收录、来源、许可证、安全和维护规则。
- `scripts/install-skill.ps1`：安装仓库内 Skill 的 Windows 脚本。
- `scripts/install-skill.sh`：安装仓库内 Skill 的 macOS/Linux 脚本。
- `skills/scouting-ai-ecosystem/`：首个新增的自有 Skill，从本机 Codex Skill 目录同步。

## 首批收录范围

首批从本机 Skill 中精选约 20 个高价值项目，分为以下类别：

- Agent 工作流与规划
- 调研与浏览器自动化
- 代码质量与调试
- 安全
- 文档与数据处理
- 技术写作与中文写作
- 部署与 GitHub 工作流

仓库内已有 Skill 继续列入目录。外部 Skill 只有在能够确认可信上游来源和有效安装方式时才进入首批目录。

## Skill 目录记录格式

`catalog/skills.yaml` 中的每条记录采用以下结构：

```yaml
- id: kimi-webbridge
  name: Kimi WebBridge
  category: research-browser
  distribution: external
  purpose: 通过浏览器扩展和本地服务，让 Agent 控制用户的真实浏览器。
  upstream: https://www.kimi.com/zh-cn/features/webbridge
  repository: null
  install:
    windows: "官方安装命令或文档链接"
    macos_linux: "官方安装命令或文档链接"
  license: "未声明"
  status: recommended
  replaced_by: null
  replacement_reason: null
  dependencies:
    - Chrome 或 Edge 扩展
    - Kimi WebBridge 本地服务
  risk_notes: 可控制带有登录状态的真实浏览器，需要关注账号和数据权限。
  verified_on: 2026-07-14
```

必填字段包括 `id`、`name`、`category`、`distribution`、`purpose`、`upstream`、`install`、`license`、`status`、`risk_notes` 和 `verified_on`。

`distribution` 只有两种取值：

- `vendored`：代码已经保存在 `skills/<id>`，可以使用本仓库脚本安装。
- `external`：本仓库只提供上游安装方法，安装脚本不会安装或执行第三方内容。

`status` 采用以下取值：

- `recommended`：当前优先推荐。
- `maintained`：仍可使用，但不是同类首选。
- `deprecated`：已不建议新装，并提供替代品或迁移说明。
- `unverified`：尚未完成来源、兼容性或实际可用性核验。

## 现有 Skill 审计与替代规则

首次建设目录时，对仓库已有 18 个 Skill 进行静态审计和上游核验；后续维护时重复这一流程。

审计维度包括：

- `SKILL.md` 是否符合当前 Agent Skill 结构，引用文件是否存在。
- 本机和当前 Codex 环境是否仍能发现、加载并执行该 Skill。
- 上游仓库、官方产品或插件是否仍在维护。
- 是否存在功能覆盖更完整、来源更可信或安全边界更清晰的替代品。
- 安装依赖、远程脚本、权限和许可证是否仍然合理。

处理方式：

- 仓库自有 Skill 出现可修复问题时，直接更新并验证。
- 外部 Skill 出现新版时，优先更新目录中的上游链接和安装说明；许可证允许且本仓库明确维护时才同步代码。
- 出现明显更优替代品时，将旧项标为 `deprecated`，填写 `replaced_by`、`replacement_reason` 和迁移说明。
- 存在严重安全、许可证或数据风险时，从默认推荐列表移除；是否删除已入库代码需要在变更记录中明确说明。
- 不因为 Star 数量或宣传文章单独做替换决定，至少结合一手文档、维护活跃度和功能差异。

## 安装方案

### 仓库内 Skill

安装脚本接收一个 Skill 标识，检查 `skills/<id>/SKILL.md` 是否存在，拒绝路径穿越，并将整个 Skill 目录复制到用户的 Codex Skill 目录。目标位置已有同名 Skill 时，必须显式使用覆盖参数。

默认安装位置：

- Windows：`%USERPROFILE%\.codex\skills`
- macOS/Linux：`${CODEX_HOME:-$HOME/.codex}/skills`

### 外部 Skill

`CATALOG.md` 提供上游安装命令或官方安装文档。本仓库安装脚本不执行第三方远程脚本，也不自动安装浏览器扩展。

## 来源与安全规则

- 优先使用作者仓库、产品官方文档或官方应用商店页面。
- 按上游公开信息如实记录许可证；无法确认时标为“未声明”。
- 本机已安装不等于允许再次分发，不能据此推断第三方 Skill 可以复制到本仓库。
- 记录权限、数据访问、账号认证、远程脚本和破坏性操作等风险。
- 每条记录保存明确的核验日期，因为安装命令和产品页面可能变化。
- 不提交凭据、Cookie、Token、运行缓存或本机绝对路径。

## 验证要求

需要验证：

- 每个 `vendored` 记录都存在对应的 `skills/<id>/SKILL.md`。
- Skill ID 不重复，所有必填字段都有值。
- `deprecated` 记录必须提供 `replaced_by` 或明确的停止使用原因。
- README 和 CATALOG 中的本地链接有效。
- PowerShell 与 shell 安装脚本都能把测试 Skill 安装到临时目录。
- 安装脚本会拒绝未知 Skill，并且在没有覆盖参数时拒绝替换已有目录。
- 变更中不包含密钥、本地凭据或运行缓存。
- Markdown 标题层级正确，安装命令可以直接复制执行。

## 发布方式

所有变更在 `agent/catalog-useful-skills` 分支完成，只提交与目录建设有关的文件。验证通过后推送分支，并向 `main` 创建草稿 PR。PR 说明采用中文，解释混合收录方案、首批 Skill 范围和实际执行的验证命令。

# Codex 实用 Skills

这是一个面向中文用户的 Codex Skill 精选目录，同时保存少量由本仓库维护的 Skill。目标不是囤积文件，而是回答三个问题：这个 Skill 有什么用、从哪里安全安装、现在是否仍值得使用。

仓库当前收录 37 条记录，包括 19 个外部项目和 18 个原有仓库条目。旧版、来源不明或已有更好替代品的条目不会被悄悄删除，而是明确标为弃用或待核验，并给出迁移方向。

## 从这里开始

- [可读目录](CATALOG.md)：按用途选择 Skill，查看官网、安装方法、风险和替代关系。
- [结构化目录](catalog/skills.yaml)：自动化和校验使用的事实源。
- [现有 Skill 审计](docs/skill-audit-2026-07-14.md)：原有 18 个 Skill 的逐项判断和证据。
- [收录与更新策略](docs/selection-policy.md)：项目如何进入、更新、弃用和移除。

## 快速安装仓库内 Skill

仓库安装器只允许安装同时满足以下条件的条目：

- `distribution: vendored`
- `status: recommended` 或 `maintained`
- `skills/<id>/SKILL.md` 实际存在

安装器会拒绝未知 ID、路径穿越、外部 Skill、弃用 Skill 和未核验 Skill。目标已存在时也会拒绝覆盖，除非显式传入覆盖参数。

### Windows

前置条件：Python 3、PyYAML 和 PowerShell 5.1 或更高版本。

```powershell
git clone https://github.com/T3L000/codex-skills.git
cd codex-skills
python -m pip install PyYAML
.\scripts\install-skill.ps1 -Name scouting-ai-ecosystem
```

确认替换已有同名 Skill：

```powershell
.\scripts\install-skill.ps1 -Name scouting-ai-ecosystem -Force
```

### macOS / Linux

```bash
git clone https://github.com/T3L000/codex-skills.git
cd codex-skills
python3 -m pip install PyYAML
./scripts/install-skill.sh scouting-ai-ecosystem
```

确认替换已有同名 Skill：

```bash
./scripts/install-skill.sh scouting-ai-ecosystem --force
```

默认安装到 `${CODEX_HOME:-$HOME/.codex}/skills`。Windows 默认安装到 `%CODEX_HOME%\skills`；未设置 `CODEX_HOME` 时使用 `%USERPROFILE%\.codex\skills`。两种脚本都支持指定其他目标目录。

## 外部 Skill 怎么安装

外部条目不会由本仓库脚本代装，也不会自动执行第三方远程脚本。请在 [CATALOG.md](CATALOG.md) 中找到官方仓库、官网和当前安装命令，再从上游安装。

常见方式包括：

```bash
npx skills add <owner/repo> --skill <skill-name> -g -a codex
```

Codex 官方或精选插件则在应用的 **Plugins** 页面安装。浏览器扩展必须从官方应用商店或产品文档安装。

## 状态含义

| 状态 | 含义 |
|---|---|
| `recommended` | 当前同类首选，已核验来源、安装方式和主要风险。 |
| `maintained` | 仍有价值，但不是通用首选，或需要本仓库持续维护。 |
| `deprecated` | 不建议新装；目录提供替代品和迁移理由。 |
| `unverified` | 来源、许可证、兼容性或实际可用性尚未完成核验。 |

## 维护与验证

修改目录或安装器后运行：

```powershell
python -m unittest discover -s tests -v
python scripts/validate-catalog.py catalog/skills.yaml
```

目录更新遵循以下原则：

- 优先使用作者仓库、官方文档、官方应用商店和 Release。
- 发现明显更好的替代品时更新状态和迁移说明，不靠 Star 数单独判断。
- 第三方内容只有在许可证允许且本仓库明确承担维护责任时才复制进来。
- 不提交 Token、Cookie、凭据、运行缓存、个人数据或本机绝对路径。
- `verified_on` 到期或安装方式变化时重新核验。

## 许可证说明

仓库中的 Skill 可能来自不同上游，各自受其目录内许可证或上游条款约束。本仓库目录和脚本的存在不代表第三方内容可以自由再分发。`docx` 与 `xlsx` 旧副本已被审计为存在明确再分发限制，当前仅保留迁移记录，不再由安装器提供；后续需要单独完成文件和 Git 历史的许可证清理。

提交新条目前，请先阅读[收录与更新策略](docs/selection-policy.md)。

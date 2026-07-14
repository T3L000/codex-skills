# Codex 实用 Skill 目录实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**目标：** 将现有仓库升级为中文、可安装、可核验、可标记替代关系的 Codex Skill 精选目录。

**架构：** 保留 `skills/` 中已有内容，将 `catalog/skills.yaml` 作为结构化事实源，使用 `CATALOG.md` 和 `README.md` 服务读者。仓库安装脚本只处理 `vendored` Skill；第三方项目记录上游安装方式。通过 Python 校验器和集成测试约束目录字段、替代关系和安装行为。

**技术栈：** Markdown、YAML、Python 3.11+、PyYAML、PowerShell 5.1+、POSIX shell、GitHub CLI。

## 全局约束

- 面向用户的文档、目录说明和 PR 描述使用中文。
- 命令、字段名、Skill ID 和上游项目名保留英文。
- 第三方 Skill 未核验许可证时不得复制代码，许可证未知时写“未声明”。
- 所有外部安装方式必须来自作者仓库、官方文档或官方应用商店。
- 已入库 Skill 不静默删除；弃用时记录替代品、原因和迁移说明。
- 不提交 Token、Cookie、凭据、缓存或本机绝对路径。

---

### 任务 1：建立目录校验器的失败测试

**文件：**
- 新建：`tests/test_validate_catalog.py`
- 新建：`scripts/validate-catalog.py`

**接口：**
- 输入：仓库根目录和 `catalog/skills.yaml`。
- 输出：退出码 `0` 表示有效；退出码 `1` 并打印错误列表表示无效。
- 提供函数：`validate_catalog(repo_root: Path, catalog_path: Path) -> list[str]`。

- [ ] **步骤 1：编写失败测试**

测试覆盖：缺少必填字段、重复 ID、未知状态、`deprecated` 无替代说明、`vendored` 缺少 `SKILL.md`、正常目录通过。

- [ ] **步骤 2：运行测试并确认失败**

运行：

```powershell
python -m unittest tests.test_validate_catalog -v
```

预期：因为 `scripts/validate-catalog.py` 尚不存在而失败。

- [ ] **步骤 3：实现最小校验器**

使用 `yaml.safe_load` 读取列表，验证设计文档中的必填字段和枚举；对 `vendored` 检查 `skills/<id>/SKILL.md`；对 `deprecated` 要求 `replaced_by` 或非空 `replacement_reason`。

- [ ] **步骤 4：运行测试并确认通过**

运行：

```powershell
python -m unittest tests.test_validate_catalog -v
```

预期：全部测试通过。

- [ ] **步骤 5：提交**

```powershell
git add tests/test_validate_catalog.py scripts/validate-catalog.py
git commit -m "test: validate skill catalog metadata"
```

### 任务 2：审计仓库现有 Skill

**文件：**
- 新建：`docs/skill-audit-2026-07-14.md`

**接口：**
- 输入：`skills/*/SKILL.md`、引用文件、本机当前版本、可信上游信息。
- 输出：每个现有 Skill 的结论：`recommended`、`maintained`、`deprecated` 或 `unverified`。

- [ ] **步骤 1：执行静态检查**

检查 18 个顶层目录是否包含 `SKILL.md`，扫描失效的相对引用、本机绝对路径、缓存、可疑远程执行命令和缺失许可证。

- [ ] **步骤 2：比较本机当前版本**

对本机或插件缓存中存在同名 Skill 的项目运行目录差异比较，记录仓库版本是否落后及具体差异。重点比较 `brainstorming`、`systematic-debugging`、`test-driven-development`、`using-superpowers`、`verification-before-completion`、`writing-plans`、`hatch-pet`、`planning-with-files` 和 `web-design-guidelines`。

- [ ] **步骤 3：调研替代品**

使用 `deep-research`，优先查阅官方仓库、文档和 Release。重点核验：

- `docx` 与当前 Documents 插件；
- `xlsx` 与当前 Spreadsheets 插件；
- `ppt-master` 与当前 Presentations 插件；
- `webapp-testing` 与 `playwright`、`playwright-interactive`、`agent-browser`；
- `project-memory` 与 `planning-with-files`、Multica；
- `mcp-builder` 与当前插件/MCP 创建工具；
- `ui-ux-pro-max`、`drawio-skill`、`code-review-and-quality` 的可信上游与维护状态。

- [ ] **步骤 4：写审计报告**

每项记录当前状态、证据、问题、替代品、迁移建议和核验日期。不能确认来源时标为 `unverified`。

- [ ] **步骤 5：检查并提交**

```powershell
rg -n "TBD|TODO|待定" docs/skill-audit-2026-07-14.md
git diff --check
git add docs/skill-audit-2026-07-14.md
git commit -m "docs: audit existing skills"
```

### 任务 3：建立机器可读 Skill 目录

**文件：**
- 新建：`catalog/skills.yaml`
- 修改：`tests/test_validate_catalog.py`

**接口：**
- 每条记录使用设计文档规定字段。
- `distribution`：`vendored` 或 `external`。
- `status`：`recommended`、`maintained`、`deprecated` 或 `unverified`。

- [ ] **步骤 1：增加真实目录测试**

测试直接加载 `catalog/skills.yaml` 并断言目录通过校验、至少覆盖全部现有顶层 Skill、至少包含一个 `external` 和一个带替代关系的记录。

- [ ] **步骤 2：运行测试并确认失败**

运行：

```powershell
python -m unittest tests.test_validate_catalog -v
```

预期：`catalog/skills.yaml` 不存在而失败。

- [ ] **步骤 3：填写首批目录**

先覆盖 18 个现有 Skill，再收录本机高价值外部或自有 Skill：`scouting-ai-ecosystem`、`kimi-webbridge`、`deep-research`、`agent-browser`、`find-docs`、`grill-me`、`improve-codebase-architecture`、`style-alchemy`、`work-reporting`、`security-best-practices`、`playwright-interactive` 和 `markdown-writer`。

每项填写真实上游、官网、安装方法、许可证、依赖、风险、状态与 `2026-07-14` 核验日期。没有证据时使用 `unverified`，不猜测。

- [ ] **步骤 4：运行校验**

```powershell
python -m unittest tests.test_validate_catalog -v
python scripts/validate-catalog.py catalog/skills.yaml
```

预期：全部通过，校验器输出目录有效。

- [ ] **步骤 5：提交**

```powershell
git add catalog/skills.yaml tests/test_validate_catalog.py
git commit -m "docs: add structured skill catalog"
```

### 任务 4：同步仓库自有情报 Skill

**文件：**
- 新建：`skills/scouting-ai-ecosystem/SKILL.md`
- 新建：`skills/scouting-ai-ecosystem/agents/openai.yaml`
- 新建：`skills/scouting-ai-ecosystem/references/sources-and-rubric.md`

**接口：**
- 来源：当前用户 Codex Skill 目录中的 `scouting-ai-ecosystem`，但提交内容中不得出现本机绝对路径。
- 目标：`skills/scouting-ai-ecosystem`。

- [ ] **步骤 1：复制完整 Skill**

保留 `SKILL.md`、`agents/openai.yaml` 和引用文件，不复制缓存或运行状态。

- [ ] **步骤 2：验证 Skill**

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills/scouting-ai-ecosystem
rg -n "C:\\Users|Token|Cookie" skills/scouting-ai-ecosystem
```

预期：Skill 有效，敏感信息扫描无匹配。

- [ ] **步骤 3：重新运行目录校验并提交**

```powershell
python scripts/validate-catalog.py catalog/skills.yaml
git add skills/scouting-ai-ecosystem catalog/skills.yaml
git commit -m "feat: add AI ecosystem scouting skill"
```

### 任务 5：实现安全安装脚本

**文件：**
- 新建：`scripts/install-skill.ps1`
- 新建：`scripts/install-skill.sh`
- 新建：`tests/test_installers.py`

**接口：**
- PowerShell：`./scripts/install-skill.ps1 -Name <id> [-Destination <path>] [-Force]`
- shell：`./scripts/install-skill.sh <id> [--destination <path>] [--force]`
- 只安装 `skills/<id>/SKILL.md` 存在的仓库内 Skill。

- [ ] **步骤 1：编写集成测试**

测试成功安装到临时目录、拒绝未知 Skill、拒绝 `../`、无覆盖参数时拒绝替换、带覆盖参数时成功替换。shell 不可用时只跳过 shell 子测试并给出原因。

- [ ] **步骤 2：运行测试并确认失败**

```powershell
python -m unittest tests.test_installers -v
```

预期：安装脚本不存在而失败。

- [ ] **步骤 3：实现 PowerShell 和 shell 脚本**

解析规范化 Skill ID，只允许小写字母、数字和连字符；解析源目录后确认仍位于仓库 `skills` 下；复制前检查 `SKILL.md`；默认拒绝覆盖。

- [ ] **步骤 4：运行测试并提交**

```powershell
python -m unittest tests.test_installers -v
git add scripts/install-skill.ps1 scripts/install-skill.sh tests/test_installers.py
git commit -m "feat: add safe skill installers"
```

### 任务 6：编写中文目录与选择政策

**文件：**
- 新建：`CATALOG.md`
- 新建：`docs/selection-policy.md`
- 修改：`README.md`

**接口：**
- `CATALOG.md` 与 `catalog/skills.yaml` 的状态、来源、安装方式和替代关系一致。
- README 提供 Windows 与 macOS/Linux 快速安装示例。

- [ ] **步骤 1：编写 CATALOG**

按类别列出 Skill。每项包含用途、分发方式、当前状态、官网/上游、安装、风险和替代说明。将 `deprecated` 项集中列入迁移区。

- [ ] **步骤 2：编写选择政策**

说明收录门槛、可信来源顺序、许可证规则、状态生命周期、替代判定标准、更新频率和安全要求。

- [ ] **步骤 3：重写 README**

保留仓库目标，增加目录入口、安装方法、状态含义、维护流程和贡献说明；避免复制完整目录内容。

- [ ] **步骤 4：检查文档**

```powershell
rg -n "TBD|TODO|待定|C:\\Users" README.md CATALOG.md docs/selection-policy.md catalog/skills.yaml
git diff --check
python scripts/validate-catalog.py catalog/skills.yaml
```

预期：无占位符或本机路径，目录有效。

- [ ] **步骤 5：提交**

```powershell
git add README.md CATALOG.md docs/selection-policy.md
git commit -m "docs: publish Chinese skill catalog"
```

### 任务 7：完整验证并发布草稿 PR

**文件：**
- 检查：所有变更文件。

- [ ] **步骤 1：运行完整验证**

```powershell
python -m unittest discover -s tests -v
python scripts/validate-catalog.py catalog/skills.yaml
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills/scouting-ai-ecosystem
git diff --check origin/main...HEAD
git status -sb
```

预期：全部测试和校验通过，工作区干净。

- [ ] **步骤 2：检查提交范围**

```powershell
git diff --stat origin/main...HEAD
git log --oneline origin/main..HEAD
```

确认只有设计、计划、目录、审计、安装器、测试和自有 Skill 变更。

- [ ] **步骤 3：推送分支**

```powershell
git push -u origin agent/catalog-useful-skills
```

- [ ] **步骤 4：创建中文草稿 PR**

使用 GitHub 创建从 `agent/catalog-useful-skills` 到 `main` 的草稿 PR。正文说明：采用混合目录的原因、现有 Skill 审计结论、替代关系、安装安全边界和验证命令。

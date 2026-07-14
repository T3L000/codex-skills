# Useful Codex Skills Catalog Design

## Goal

Turn `T3L000/codex-skills` into a maintainable personal catalog of useful Codex skills. Readers should be able to understand why a skill matters, find its authoritative source, install it safely, and distinguish repository-owned copies from externally maintained skills.

## Current State

- The repository vendors 18 skills under `skills/`.
- The repository contains roughly 12,000 files and 26 MB of tracked content, largely because document and presentation skills include substantial assets.
- The README lists skill names and manual copy instructions but does not record upstream projects, official websites, licenses, dependencies, update methods, or verification dates.
- The local Codex installation contains about 47 non-system skills from personal, official, curated, and third-party sources.

## Selected Approach

Use a hybrid catalog:

1. Keep the existing vendored skills intact.
2. Vendor only skills authored or intentionally maintained in this repository.
3. Catalog third-party skills by linking to their authoritative upstream source instead of copying code without a provenance and license review.
4. Provide both human-readable documentation and machine-readable metadata.

This avoids turning the repository into an unreviewed mirror while preserving a convenient backup and installer for repository-owned skills.

## Repository Structure

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
  <existing vendored skills>
  scouting-ai-ecosystem/
```

### File Responsibilities

- `README.md`: concise repository introduction, quick installation, catalog links, and contribution/update workflow.
- `CATALOG.md`: categorized, reader-friendly list of selected skills with purpose, source, official site, installation, and status.
- `catalog/skills.yaml`: canonical structured records used for consistency checks and future automation.
- `docs/selection-policy.md`: inclusion, provenance, licensing, security, and maintenance rules.
- `scripts/install-skill.ps1`: Windows installer for vendored skills only.
- `scripts/install-skill.sh`: macOS/Linux installer for vendored skills only.
- `skills/scouting-ai-ecosystem/`: first new repository-owned skill copied from the local Codex installation.

## Catalog Scope

The first release will curate approximately 20 high-value local skills across these categories:

- Agent workflow and planning
- Research and browser automation
- Code quality and debugging
- Security
- Documents and data
- Technical and Chinese writing
- Deployment and GitHub workflow

Existing vendored skills remain listed. External skills are included only when an authoritative upstream source and a credible installation path can be verified.

## Catalog Record

Each `catalog/skills.yaml` record contains:

```yaml
- id: kimi-webbridge
  category: research-browser
  distribution: external
  purpose: Control a real browser through the Kimi WebBridge extension and local daemon.
  upstream: https://www.kimi.com/zh-cn/features/webbridge
  repository: null
  install:
    windows: "Official command or documentation URL"
    macos_linux: "Official command or documentation URL"
  license: "Not stated"
  dependencies:
    - Chrome or Edge extension
    - Local Kimi WebBridge daemon
  risk_notes: Browser control can access active authenticated sessions.
  verified_on: 2026-07-14
```

Required fields are `id`, `category`, `distribution`, `purpose`, `upstream`, `install`, `license`, `risk_notes`, and `verified_on`.

`distribution` has two values:

- `vendored`: code exists under `skills/<id>` and can be installed by repository scripts.
- `external`: the catalog links to the upstream installation method; repository scripts refuse to install it.

## Installation Design

### Vendored Skill

The scripts accept one skill identifier, verify `skills/<id>/SKILL.md`, refuse path traversal, copy the complete directory to the user's Codex skill directory, and require an explicit force option before replacing an existing installation.

Default destinations:

- Windows: `%USERPROFILE%\.codex\skills`
- macOS/Linux: `${CODEX_HOME:-$HOME/.codex}/skills`

### External Skill

`CATALOG.md` shows the upstream command or official installation guide. The repository installer does not execute third-party remote scripts or install browser extensions.

## Source and Safety Rules

- Prefer the author's repository, product documentation, or official marketplace page.
- Record the license exactly as published; use `Not stated` when it cannot be verified.
- Never infer that a local copy may be redistributed merely because it is installed.
- Include permission, data-access, authentication, remote-script, and destructive-operation risks.
- Pin verification to an explicit date because installation commands and product pages change.
- Do not store credentials, cookies, tokens, generated caches, or local machine paths.

## Validation

Validation must confirm:

- every vendored record has `skills/<id>/SKILL.md`;
- every catalog ID is unique;
- every required field is populated;
- README and CATALOG links resolve locally;
- PowerShell and shell installers install a test skill into a temporary destination;
- installers reject an unknown skill and refuse overwrite without force;
- no secrets or local credential files are added;
- the Markdown has a valid heading hierarchy and copyable commands.

## Publishing

Work on branch `agent/catalog-useful-skills`, commit only catalog-related files, push the branch, and open a draft pull request against `main`. The PR will explain the hybrid provenance policy and list the validation commands used.

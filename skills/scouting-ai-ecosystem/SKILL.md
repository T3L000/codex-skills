---
name: scouting-ai-ecosystem
description: Use when the user asks to discover, monitor, compare, or report recent AI Agent, Agent Skill, MCP, plugin, browser automation, coding-agent, RAG, digital-employee, or AI-native platform projects, including recurring intelligence briefs and watchlist updates.
---

# Scouting AI Ecosystem

## Overview

Produce an evidence-backed radar of projects that may improve the user's AI workflow or company platform. Optimize for decision value, not news volume.

**REQUIRED SUB-SKILL:** Use `deep-research` for the research methodology. Prefer `kimi-webbridge` when the user's real browser is connected; otherwise use available web research tools and disclose the fallback.

Read [references/sources-and-rubric.md](references/sources-and-rubric.md) before searching.

## Workflow

1. Set the time window. Default to the previous seven days; use the actual current date.
2. Read `.ai-intel/state.json` when it exists. Treat it only as prior-run memory, not as evidence.
3. Search at least four source classes: specialized directories, builder communities, GitHub, and technical publications. Include at least one Chinese source.
4. Normalize project names and URLs. Merge duplicate announcements, forks, mirrors, and reposts.
5. Shortlist no more than ten items. Open primary repositories, release notes, documentation, or maintainer posts for every shortlisted item.
6. Distinguish a new project from a meaningful update. Ignore routine marketing, minor version bumps, and unsupported claims.
7. Score each candidate with the reference rubric. Record permissions, data handling, license, deployment, maintenance, and compatibility risks.
8. Save the final candidate state to `.ai-intel/state.json` only after the brief is complete. Preserve `first_seen`, update `last_seen`, and store canonical URLs and the latest material change.

## Output Contract

Return these sections in order:

1. **结论** — three to five sentences with the strongest signal.
2. **本期候选** — table: 项目、变化、价值、证据、评分、建议.
3. **行动分组** — `建议试用`, `继续观察`, `暂不关注`.
4. **风险与缺口** — security, privacy, license, maintenance, unavailable sources.
5. **下周观察项** — explicit watchlist changes and concrete follow-ups.

Link evidence next to each claim. If no material change is found, say so directly. Never recommend installation from search snippets alone.

## Common Mistakes

- Ranking by stars without checking recency, releases, issues, or independent use.
- Treating multiple articles about one launch as multiple discoveries.
- Mixing official claims with verified behavior.
- Omitting the time window or silently changing scoring criteria.
- Installing or enabling a candidate when the user asked only for research.

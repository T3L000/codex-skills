# Sources and scoring rubric

## Source classes

Use current URLs and replace dead sources with equivalent primary or community sources.

### Specialized directories

- Agent Skills: https://skills.sh/ — check Trending, Hot, topics, installs, and audits.
- MCP ecosystem: https://smithery.ai/ — check usage, publisher, authentication, and tool descriptions.
- Product launches: https://www.producthunt.com/categories/ai-agents and `/ai-coding-agents`; use as leads, not proof.

### Builder communities

- Show HN: https://news.ycombinator.com/show — read launch comments and objections.
- V2EX AI/OpenAI node: https://www.v2ex.com/go/ai — use for Chinese user experience and failures.
- Project Discord, Discussions, and issue trackers — use for adoption and unresolved problems.

### GitHub

- Weekly Trending: https://github.com/trending?since=weekly
- Topics and repository search: `ai-agent`, `model-context-protocol`, `agent-skills`, `browser-automation`, `rag`, `multi-agent`.
- Verify README, releases, commit activity, contributors, issues, discussions, license, security policy, install and uninstall instructions.

### Technical publications and Chinese curation

- Latent Space / AINews: https://www.latent.space/about
- Simon Willison AI: https://simonwillison.net/tags/ai/
- Hugging Face Daily Papers: https://huggingface.co/papers
- HelloGitHub AI: https://hellogithub.com/
- 阮一峰科技爱好者周刊: https://www.ruanyifeng.com/blog/weekly/

## Search themes

- Agent Skill, MCP server, plugin, browser automation, coding agent
- multi-agent coordination, managed agents, digital employee, AI-native team platform
- enterprise knowledge base, RAG, GraphRAG, memory, evaluation, observability, sandbox
- self-hosted, local-first, privacy, permission, audit, enterprise integration

## Candidate scoring (100)

| Dimension | Weight | Evidence |
|---|---:|---|
| User relevance | 25 | Fits Codex, Kimi WebBridge, Multica, enterprise knowledge, or digital employees |
| Material novelty | 15 | New capability or consequential update inside the window |
| Evidence quality | 15 | Primary source plus independent confirmation when available |
| Maturity | 15 | Releases, documentation, real users, deployment path |
| Maintenance | 10 | Recent commits, responsive issues, active maintainers |
| Integration fit | 10 | MCP, Skill, API, CLI, self-hosting, or existing platform compatibility |
| Risk posture | 10 | Permissions, data boundaries, license, rollback and uninstall clarity |

Interpretation: `80–100` suggest a controlled trial, `65–79` watch closely, `<65` do not prioritize. A severe security, license, or data-boundary risk overrides the numeric score.

## State schema

Store valid UTF-8 JSON at `.ai-intel/state.json`:

```json
{
  "last_run": "YYYY-MM-DDTHH:mm:ss+08:00",
  "window_days": 7,
  "projects": {
    "canonical-project-id": {
      "name": "Project",
      "url": "https://primary.example/project",
      "first_seen": "YYYY-MM-DD",
      "last_seen": "YYYY-MM-DD",
      "latest_material_change": "Concise evidence-backed summary",
      "decision": "trial|watch|ignore",
      "score": 0
    }
  }
}
```

If state is missing or invalid, run a fresh baseline and disclose that continuity is unavailable.

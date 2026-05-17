---
name: project-memory
description: Maintain a concise project memory markdown file in the current workspace so future Codex conversations can resume with project context. Use at the start of the first project-related turn in a new Codex conversation, when opening or resuming a folder/project, when the user asks to remember or summarize project information, when important preferences/decisions/constraints are discovered, or when a new conversation should stay aligned with prior work.
---

# Project Memory

## Overview

Keep a durable, compact project memory in the repository or workspace so new Codex sessions can recover the user's context, decisions, preferences, constraints, and current status without rereading the whole conversation history.

The memory file is `CODEX_PROJECT_MEMORY.md`.

## Startup Workflow

On the first project-related assistant turn in a new conversation, run this startup workflow before making project decisions:

1. Locate the project root. Prefer the Git repository root when available; otherwise use the current working directory.
2. Check for `CODEX_PROJECT_MEMORY.md` at the project root.
3. If it exists, read it before making project decisions and use it as supporting context.
4. If it does not exist and the current task is project-related, create it before or during the first meaningful update.
5. If creating the file, keep the initial version short and mark unknown sections as `Unknown` instead of inventing details.
6. Treat this startup check as already done for the rest of the current conversation unless the user switches projects or asks to refresh memory.

## Memory Template

Use this structure for new files:

```markdown
# Codex Project Memory

## Project Snapshot
- Purpose: Unknown
- Main stack: Unknown
- Important commands: Unknown
- Current focus: Unknown

## User Preferences
- Unknown

## Stable Decisions
- Unknown

## Project Conventions
- Unknown

## Known Risks And Gotchas
- Unknown

## Current State
- Unknown

## Recent Notes
- Unknown
```

## What To Record

Record durable information that will help a future session stay aligned:

- The project's purpose, product direction, domain, audience, or important user goals.
- Tech stack, package manager, runtime assumptions, setup commands, test commands, and build commands.
- User preferences about style, language, workflow, review strictness, file locations, naming, or tools.
- Decisions the user made and the reason when it matters.
- Constraints, known bugs, fragile areas, environment quirks, failed approaches, and things not to repeat.
- Current task status, remaining work, and verification already performed.

## What Not To Record

Keep the file useful rather than exhaustive:

- Do not store secrets, tokens, credentials, private keys, API keys, passwords, or personal data.
- Do not record speculative ideas unless the user confirms them or they affect current work.
- Do not paste long logs, command output, stack traces, or full code blocks. Summarize the useful lesson.
- Do not duplicate information already obvious from `README.md`, package files, or source code unless it is a decision or gotcha.
- Do not update the file for every minor message. Batch meaningful updates.

## Update Rules

Update `CODEX_PROJECT_MEMORY.md` when:

- The user explicitly says to remember, record, summarize, or keep context.
- A stable decision, preference, constraint, command, or gotcha becomes clear.
- A task ends with meaningful status that a future session should know.
- The current file is missing, stale, or contradicts newly verified information.

When updating:

- Preserve existing useful content.
- Replace `Unknown` items once real information is known.
- Prefer concise bullets with dates only when chronology matters.
- Move stale information to current wording instead of appending contradictory notes.
- Keep `Recent Notes` short; promote long-lived items into the appropriate stable section.

## Interaction Pattern

When the memory affects the answer, briefly mention that it was read or updated. If the user gives information that may or may not be worth saving, use judgment and update only when it is likely to matter in future sessions.

If the user asks whether project memory is active, inspect the project root and report whether `CODEX_PROJECT_MEMORY.md` exists.

---
name: coordinate-review-repair-loops
description: Coordinate multiple user-owned implementation and independent-review tasks through repeated review, repair, delta review, integration, PR/CI/merge, and control-plane closeout. Use when the user asks Codex to supervise, babysit, monitor, or continue a set of tasks until they reach auditable terminal states or a resource threshold; especially for “审完再修、修完再审”, “盯着这些任务”, multi-thread delivery loops, or a final report after all tasks finish. Do not use for a single implementation, one isolated review, or passive status reporting without loop authority.
---

# Coordinate Review and Repair Loops

Run a bounded project-control loop. Coordinate existing task threads; do not become a second implementer or reviewer.

## Compose existing skills

- Require `task-package-delivery` in implementation and review work that has a prepared acceptance contract.
- Require `open-code-review-delegate` for independent Git code review when project rules call for it.
- Use project-specific memory, WBS, `AGENTS.md`, architecture contracts, and remote facts as authority.
- Do not duplicate implementation or code-review procedures in this skill.

## 1. Freeze the authority envelope

Before dispatching anything, record:

- objective and task set;
- task priority and dependencies;
- existing implementation and review thread IDs;
- allowed writes and external actions: edit, commit, push, create/update PR, publish review, merge, update WBS/memory, clean up;
- model/reasoning policy and heavy-test concurrency;
- stop conditions: terminal states, resource floor, deadline, repeated blocker, or user input;
- final report requirements.

Do not infer authority from “finish”, “babysit”, or “keep going”. These extend persistence, not permissions. Keep destructive cleanup, force operations, permission changes, production actions, and unapproved external communication out of scope.

If the envelope is materially ambiguous, ask once before the affected transition. Continue independent read-only work where possible.

## 2. Build one coordination ledger

Keep one task row per task. Use the project’s existing control artifact when available. If the user authorizes a new local ledger, use the structure in [references/ledger.md](references/ledger.md) and validate it with:

```powershell
python scripts\validate_loop_ledger.py <ledger.json>
```

Each row must distinguish:

1. code/artefact implementation complete;
2. independent review passed;
3. PR mergeable;
4. merged into the target branch;
5. WBS/control plane backfilled.

Also record exact snapshot identity, unresolved P0/P1, current thread owner, next transition, blocker evidence, and last fresh verification. Never compress these into one `completed` flag.

Treat task-thread summaries, colleague statements, screenshots, local tests, uncommitted work, and green CI as evidence candidates—not terminal truth.

## 3. Reuse task lanes

Use one implementation writer and one independent reviewer per task.

- Search for existing threads before creating or dispatching.
- Resume the original implementation thread for P0/P1 repair.
- Resume the original review thread for delta review.
- Create a new user-owned thread only when the user explicitly asks and no safe lane exists.
- Never ask a reviewer to repair its own findings.
- Never start a second implementation lane against the same files.
- Keep WBS/memory updates in the project-controller lane unless project rules say otherwise.

Thread IDs, cursors, commit SHAs, PR IDs, and other remote identifiers are opaque. Copy them exactly.

## 4. Dispatch only the next valid transition

Read dynamic facts immediately before dispatch. Use the compact prompts in [references/prompts.md](references/prompts.md).

### Implementation candidate

Send the original acceptance contract, current base, frozen file boundary, permissions, verification gates, and stop conditions. Implementation self-review is not independent review.

### Independent review

Freeze the current head/file hashes and complete diff. Require read-only review, fresh evidence, actionable findings, and an explicit `APPROVE`, `REQUEST_CHANGES`, or `BLOCKED` result. For Git code, apply the project’s `task-package-delivery + open-code-review-delegate` rule.

### Repair

Send only confirmed P0/P1 findings, exact failing evidence, allowed files, regression conditions, and current snapshot. Do not restate the entire original prompt unless the task thread lost it.

### Delta review

Review the repair delta and all old findings that could regress. Do not mechanically repeat the first full review or full test suite when no integration uncertainty exists.

### Integration and remote landing

An approval binds one snapshot. If the base or candidate changes, mark the approval stale and require the proportionate integration/delta review before PR readiness.

Commit, push, PR, review publication, merge, and control-plane writes require the recorded authority and fresh remote checks. A mergeability flag or green CI alone does not override unresolved P0/P1 or a negative review.

## 5. Wait by events, not narration

- Use task/thread wait tools rather than repeatedly reading live commentary.
- Wait on completion or attention events; do not poll unchanged state.
- Leave approval and user-input requests for the user.
- Serialize full test suites and other heavy shared-resource work.
- Parallelize only independent light checks or task lanes with disjoint files and no shared heavy resource.
- Re-read a completed task once, then route its next transition.

Do not consume tokens merely to announce that nothing changed.

## 6. Escalate instead of looping forever

Stop local repair and escalate when any condition holds:

- the same finding class appears in two tasks;
- a task reaches the project’s repeated-P1 threshold;
- the fix crosses two or more public owners;
- safe completion requires a new architecture, dependency, permission, production action, or threat-model decision;
- implementation and review disagree on a material contract boundary;
- the same blocking condition reaches the user-defined repeat threshold;
- the resource floor or deadline is reached.

Route shared mechanism failures to the existing architecture/governance task when one exists. Do not silently create a new WBS task or weaken acceptance criteria.

P2 findings do not drive an endless repair loop. Record them unless the task contract or user explicitly promotes them.

## 7. Apply terminal gates

A code task may be called fully closed only when:

- current-snapshot implementation evidence exists;
- independent review has no unresolved P0/P1;
- required integration review is current;
- PR checks, review state, and topology permit landing;
- merge is verified on the target branch;
- authorized WBS/control-plane projections are reconciled.

For non-code tasks, mark non-applicable gates explicitly rather than inventing commits or PRs.

Stop the coordination run when all tasks are in auditable terminal states or a declared stop condition fires. Do not mark work complete because the token budget is low.

## 8. Deliver the run report

Report:

- objective, authority envelope, start/end time, and stop trigger;
- per-task transition timeline and thread reuse;
- findings opened, repaired, regressed, escalated, and closed;
- fresh test/CI/review/merge evidence;
- five-state table;
- resource usage when available, otherwise `unavailable`;
- remaining blockers, owner, minimum next evidence, and recommended single next step;
- any external or destructive action actually taken.

Lead with the outcome. Separate verified fact, task-thread claim, inference, and pending evidence.

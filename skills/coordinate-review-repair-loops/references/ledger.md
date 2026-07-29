# Coordination ledger

Use this only when the project has no existing coordination artifact and the user authorizes a local ledger.

## Minimal JSON shape

```json
{
  "schema_version": 1,
  "objective": "Close selected tasks or stop at the resource floor",
  "authority": {
    "edit": true,
    "commit": false,
    "push": false,
    "create_or_update_pr": false,
    "publish_review": false,
    "merge": false,
    "update_control_plane": false,
    "cleanup": false
  },
  "resource_policy": {
    "budget_floor_percent": 60,
    "current_remaining_percent": null,
    "max_parallel_heavy_tests": 1
  },
  "stop_conditions": [
    "all_tasks_terminal",
    "budget_floor_reached",
    "material_user_decision_required"
  ],
  "tasks": [
    {
      "task_id": "TASK-01",
      "priority": 1,
      "implementation_thread_id": "opaque-id",
      "review_thread_id": "opaque-id",
      "state": "candidate_ready",
      "snapshot": {
        "base": "exact-ref-or-null",
        "head": "exact-ref-or-null",
        "file_digest": "sha256-or-null"
      },
      "unresolved_findings": [],
      "five_state": {
        "implementation_complete": true,
        "independent_review": "not_started",
        "pr_mergeable": "unknown",
        "merged_target": false,
        "control_plane_backfilled": false
      },
      "blocker": null,
      "next_transition": "dispatch_review"
    }
  ]
}
```

## Workflow states

Use one of:

- `planned`
- `implementation_running`
- `candidate_ready`
- `review_running`
- `changes_requested`
- `repair_running`
- `delta_review_ready`
- `approved`
- `integration_pending`
- `integration_review_ready`
- `pr_pending`
- `ci_pending`
- `merge_ready`
- `merged`
- `control_plane_pending`
- `closed`
- `blocked`

## Finding states

Each unresolved finding contains:

```json
{
  "id": "P1-01",
  "severity": "P1",
  "state": "open",
  "snapshot": "exact-head-or-digest",
  "evidence": "short reproducible evidence pointer"
}
```

Allowed severities: `P0`, `P1`, `P2`. Allowed states: `open`, `repairing`, `ready_for_delta_review`, `closed`, `escalated`.

Never close a finding solely because the implementation thread says it is fixed. Closure comes from the independent review lane on the relevant snapshot.

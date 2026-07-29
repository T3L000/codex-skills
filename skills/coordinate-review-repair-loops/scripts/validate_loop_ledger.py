#!/usr/bin/env python3
"""Validate a coordinate-review-repair-loops JSON ledger."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


WORKFLOW_STATES = {
    "planned",
    "implementation_running",
    "candidate_ready",
    "review_running",
    "changes_requested",
    "repair_running",
    "delta_review_ready",
    "approved",
    "integration_pending",
    "integration_review_ready",
    "pr_pending",
    "ci_pending",
    "merge_ready",
    "merged",
    "control_plane_pending",
    "closed",
    "blocked",
}
AUTHORITY_KEYS = {
    "edit",
    "commit",
    "push",
    "create_or_update_pr",
    "publish_review",
    "merge",
    "update_control_plane",
    "cleanup",
}
REVIEW_STATES = {"not_started", "changes_requested", "approved", "blocked"}
MERGEABLE_STATES = {True, False, "unknown", "not_applicable"}
FINDING_STATES = {
    "open",
    "repairing",
    "ready_for_delta_review",
    "closed",
    "escalated",
}
SEVERITIES = {"P0", "P1", "P2"}


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_task(task: Any, index: int, errors: list[str]) -> str | None:
    prefix = f"tasks[{index}]"
    expect(isinstance(task, dict), f"{prefix} must be an object", errors)
    if not isinstance(task, dict):
        return None

    task_id = task.get("task_id")
    expect(isinstance(task_id, str) and bool(task_id.strip()), f"{prefix}.task_id is required", errors)
    expect(task.get("state") in WORKFLOW_STATES, f"{prefix}.state is invalid", errors)
    expect(isinstance(task.get("priority"), int) and task["priority"] >= 0, f"{prefix}.priority must be a non-negative integer", errors)

    for field in ("implementation_thread_id", "review_thread_id"):
        value = task.get(field)
        expect(value is None or isinstance(value, str), f"{prefix}.{field} must be a string or null", errors)
    if task.get("implementation_thread_id") and task.get("review_thread_id"):
        expect(
            task["implementation_thread_id"] != task["review_thread_id"],
            f"{prefix} implementation and review threads must be different",
            errors,
        )

    five = task.get("five_state")
    expect(isinstance(five, dict), f"{prefix}.five_state must be an object", errors)
    if isinstance(five, dict):
        expect(isinstance(five.get("implementation_complete"), bool), f"{prefix}.five_state.implementation_complete must be boolean", errors)
        expect(five.get("independent_review") in REVIEW_STATES, f"{prefix}.five_state.independent_review is invalid", errors)
        expect(five.get("pr_mergeable") in MERGEABLE_STATES, f"{prefix}.five_state.pr_mergeable is invalid", errors)
        expect(isinstance(five.get("merged_target"), bool), f"{prefix}.five_state.merged_target must be boolean", errors)
        expect(
            isinstance(five.get("control_plane_backfilled"), bool)
            or five.get("control_plane_backfilled") == "not_applicable",
            f"{prefix}.five_state.control_plane_backfilled is invalid",
            errors,
        )

    findings = task.get("unresolved_findings")
    expect(isinstance(findings, list), f"{prefix}.unresolved_findings must be an array", errors)
    blocking_open = False
    if isinstance(findings, list):
        finding_ids: set[str] = set()
        for finding_index, finding in enumerate(findings):
            finding_prefix = f"{prefix}.unresolved_findings[{finding_index}]"
            expect(isinstance(finding, dict), f"{finding_prefix} must be an object", errors)
            if not isinstance(finding, dict):
                continue
            finding_id = finding.get("id")
            expect(isinstance(finding_id, str) and bool(finding_id), f"{finding_prefix}.id is required", errors)
            if isinstance(finding_id, str):
                expect(finding_id not in finding_ids, f"{finding_prefix}.id is duplicated", errors)
                finding_ids.add(finding_id)
            severity = finding.get("severity")
            state = finding.get("state")
            expect(severity in SEVERITIES, f"{finding_prefix}.severity is invalid", errors)
            expect(state in FINDING_STATES, f"{finding_prefix}.state is invalid", errors)
            if severity in {"P0", "P1"} and state not in {"closed", "escalated"}:
                blocking_open = True

    if task.get("state") in {"approved", "integration_pending", "integration_review_ready", "pr_pending", "ci_pending", "merge_ready", "merged", "control_plane_pending", "closed"}:
        expect(not blocking_open, f"{prefix} cannot advance with an open P0/P1", errors)
    if task.get("state") in {"approved", "integration_pending", "integration_review_ready", "pr_pending", "ci_pending", "merge_ready", "merged", "control_plane_pending", "closed"} and isinstance(five, dict):
        expect(five.get("independent_review") == "approved", f"{prefix} advanced state requires approved independent review", errors)
    if task.get("state") in {"merged", "control_plane_pending", "closed"} and isinstance(five, dict):
        expect(five.get("merged_target") is True, f"{prefix} merged/closed state requires merged_target=true", errors)
    if task.get("state") == "closed" and isinstance(five, dict):
        expect(
            five.get("control_plane_backfilled") in {True, "not_applicable"},
            f"{prefix} closed state requires control-plane completion or not_applicable",
            errors,
        )
    return task_id if isinstance(task_id, str) else None


def validate(data: Any) -> list[str]:
    errors: list[str] = []
    expect(isinstance(data, dict), "ledger must be a JSON object", errors)
    if not isinstance(data, dict):
        return errors

    expect(data.get("schema_version") == 1, "schema_version must be 1", errors)
    expect(isinstance(data.get("objective"), str) and bool(data["objective"].strip()), "objective is required", errors)

    authority = data.get("authority")
    expect(isinstance(authority, dict), "authority must be an object", errors)
    if isinstance(authority, dict):
        expect(set(authority) == AUTHORITY_KEYS, f"authority keys must be exactly {sorted(AUTHORITY_KEYS)}", errors)
        for key in AUTHORITY_KEYS:
            expect(isinstance(authority.get(key), bool), f"authority.{key} must be boolean", errors)

    resources = data.get("resource_policy")
    expect(isinstance(resources, dict), "resource_policy must be an object", errors)
    if isinstance(resources, dict):
        floor = resources.get("budget_floor_percent")
        current = resources.get("current_remaining_percent")
        expect(isinstance(floor, (int, float)) and 0 <= floor <= 100, "budget_floor_percent must be 0..100", errors)
        expect(current is None or isinstance(current, (int, float)) and 0 <= current <= 100, "current_remaining_percent must be null or 0..100", errors)
        expect(
            isinstance(resources.get("max_parallel_heavy_tests"), int)
            and resources["max_parallel_heavy_tests"] >= 1,
            "max_parallel_heavy_tests must be >= 1",
            errors,
        )

    expect(isinstance(data.get("stop_conditions"), list) and bool(data["stop_conditions"]), "stop_conditions must be a non-empty array", errors)
    tasks = data.get("tasks")
    expect(isinstance(tasks, list) and bool(tasks), "tasks must be a non-empty array", errors)
    if isinstance(tasks, list):
        task_ids: set[str] = set()
        for index, task in enumerate(tasks):
            task_id = validate_task(task, index, errors)
            if task_id:
                expect(task_id not in task_ids, f"tasks[{index}].task_id is duplicated", errors)
                task_ids.add(task_id)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.ledger.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [f"unable to read ledger: {type(exc).__name__}"]}, ensure_ascii=False))
        return 2

    errors = validate(data)
    print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())

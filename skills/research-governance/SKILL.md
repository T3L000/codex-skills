---
name: research-governance
description: Run auditable enterprise or project research that must inform a roadmap, WBS, architecture decision, vendor gate, or executive recommendation. Use when a research result needs explicit scope, primary-source evidence, dynamic-fact snapshots, stop conditions, decision gates, a research receipt, and independent review; use alongside deep-research for external discovery.
---

# Research Governance

Turn research into a decision record without turning an unverified report into implementation authority.

## Start with the right contract

1. State whether the work is targeted, representative, or landscape research.
2. State the decision the work can influence and what it cannot authorize.
3. Identify dynamic inputs (for example code, WBS, project memory, whitepaper, vendor pricing, and remote state). Record read time, source/ref, and digest where practical. Treat them as point-in-time observations, not frozen truth, unless the task explicitly freezes them.
4. Separate current project facts, primary external evidence, maintainer claims, and inference. Do not let a report repeat an old snapshot as current fact.

For external research, load and follow `deep-research` and its required `kimi-webbridge` companion. This skill adds governance; it does not replace their discovery, primary-source validation, counterevidence, or saturation requirements.

## Keep decision layers separate

Use the narrowest conclusion that the evidence supports:

- **Research/report contract accepted**: the analysis and its boundaries are sound.
- **Experiment permitted**: a bounded test has an explicit fixture, safety, budget, owner, and acceptance oracle.
- **Technology selected**: comparative evidence supports a named choice for the stated context.
- **Implementation, pilot, procurement, or production authorized**: requires its own project and business approvals.

Never infer a later layer from an earlier one. A green CI run, merged PR, vendor claim, benchmark, or accepted report does not alone authorize the next layer.

When evaluation is involved, separate:

- **Engineering Gold Set**: questions, qrels, exact locators, PermissionContext, corpus snapshot, adjudication, and versioning; used for technical comparisons.
- **Business-value Gold Set**: business-owner-confirmed workflow, baseline, outcome, window, and attribution; used for value and launch judgments.

Do not require the second set merely to design the first, and never use the first as a substitute for business approval.

## Run the research receipt

Before synthesis, maintain a compact receipt containing:

- scope tree, exclusions, query families, and candidate ledger;
- discovery channel and primary-source validation channel, including degraded-mode failures;
- source class, access date, version/release date, and evidence state for material claims;
- counterevidence, rejected candidates, and unresolved evidence;
- dynamic-input snapshot and changes that invalidate or merely age a conclusion;
- browser/session hygiene evidence when browser work is used and the user has authorized closing pages;
- original processing, cache-input, and quota/goal accounting when available; label unavailable values rather than estimating them.

Use two materially different expansion rounds with no important new category or candidate before calling a landscape search saturated. For targeted work, state why broader saturation is not claimed.

## Build gates before scores

1. List hard gates first: permissions, legal/data egress, license, owner, auditability, rollback, security, cost/budget, and exit.
2. Mark a candidate `NO-GO`, `DEFER`, `CONTRACT-ONLY`, or `INSUFFICIENT-EVIDENCE` when a hard gate is unmet; do not average it into a winner.
3. If scoring remains meaningful, publish the 1/3/5 anchors, source pointer, factual basis, judgment, weights, formula, and sensitivity check for each scored cell.
4. Describe the stopping condition and the minimum next evidence that could change the decision.

## Review and change control

For material conclusions, bind the final report to a SHA-256 or equivalent immutable revision and use a reviewer who did not author the report. A later edit invalidates prior acceptance until a delta review binds the new revision.

When control files disagree, correct only current-state summaries; preserve historical reports and label them as historical. Do not rewrite WBS, code, project memory, whitepapers, or remote state without explicit authority.

## Deliverables

Produce, in proportion to scope:

1. decision-oriented report with evidence and limitations;
2. research receipt and candidate/source ledger;
3. gate, stop-condition, owner, and next-evidence table;
4. independent review record for material decisions;
5. a concise final status distinguishing report acceptance from implementation authorization.

Use clear prose. Do not delete evidence, numbers, counterarguments, or gates merely to make the report shorter or less mechanical.

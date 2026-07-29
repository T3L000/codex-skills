# Compact transition prompts

These are skeletons. Point to the authoritative project contract instead of copying stable rules.

## Resume implementation for repair

```text
Continue the original <task> implementation lane. Read the original contract and the latest
independent-review result. Fix only <finding IDs> on snapshot <head/digest>.

Allowed files: <boundary>.
Required regression evidence: <commands/oracles>.
Authority: <edit/test only, or explicitly approved external actions>.
Stop if: <cross-owner, dependency, threat-model, or user-decision boundary>.

Return exact delta, fresh evidence, final snapshot, unresolved risk, and five-state receipt.
Do not perform or claim independent review.
```

## Resume independent delta review

```text
Continue the original <task> review lane. Review only the repair delta from
<old snapshot> to <new snapshot>, while rechecking old findings <IDs> and their regression paths.
The implementation claim is a lead, not evidence.

Freeze the full candidate file list/digests at start and end. Use the original acceptance
contract and required review skills. Do not repair, commit, push, or change the control plane.

Return actionable findings and APPROVE / REQUEST_CHANGES / BLOCKED, plus the five states.
```

## Integration gate

```text
The candidate was approved on <snapshot>. Re-read the latest target branch and remote PR state.
If integration changes the candidate or relevant dependencies, produce a new frozen snapshot
and stop for proportionate delta review. Do not transfer an old approval to changed bytes.
Only perform commit/push/PR/merge actions explicitly allowed by the authority envelope.
```

## Control-plane closeout

```text
Verify remote merge and current target-branch identity. Reconcile the five states from auditable
facts, then update only the authorized control-plane sources in their required direction.
Do not turn local work, CI, or a report acceptance into merged/production completion.
Return the final receipt and any cleanup candidates; do not delete without explicit approval.
```

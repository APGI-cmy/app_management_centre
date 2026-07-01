# PR-Scoped Gate Evidence Canon

Status: Approved governance pattern
Applies to: App Management Centre implementation pull requests

## Purpose

Implementation PRs must not overwrite singleton/current-wave admin evidence files. Singleton evidence creates merge conflicts, stale state, and cross-PR admin loops.

## Required pattern

For any implementation-like PR, delegation evidence must be stored at:

```text
.agent-admin/control/delegation-orders/pr-<PR_NUMBER>.json
```

The legacy singleton file is not valid merge evidence for implementation PRs:

```text
.agent-admin/control/delegation-order.json
```

## Gate behavior

The AMC Builder Delegation Order Gate must:

1. Detect implementation-like file changes.
2. Reject implementation PRs that modify `.agent-admin/control/delegation-order.json`.
3. Prefer PR-scoped evidence at `.agent-admin/control/delegation-orders/pr-<PR_NUMBER>.json`.
4. Validate that the evidence `pr_number` matches the current PR number.
5. Validate ordered proof: IAA pre-brief commit before builder appointment commit before first implementation commit.
6. Fail closed with STOP_AND_FIX guidance if evidence is missing or invalid.

## Agent instruction

Agents must create PR-specific evidence files for each implementation PR. Do not repurpose or overwrite singleton/current-wave files to satisfy merge gates.

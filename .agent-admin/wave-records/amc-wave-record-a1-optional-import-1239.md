# AMC Wave Record — A1 Optional Import Repair — PR #1239

Issue: #1237
PR: #1239
Wave: amc-a1-optional-import-1237
Branch: builder/issue-1237-a1-optional-imports
Base: ff5ec09024210789c2d2941a4aa6fe1ddb166515
Package head: 49e5afec461cc2aca3afee50f980ba093e2c2389
Substantive implementation head: a9173f4d5dcc6057d7f201b0b1a78087f1e3559c
Foreman QP head: 49e5afec461cc2aca3afee50f980ba093e2c2389

Verdict: PENDING_CI
PHASE: A1_REPAIR

## Scope reviewed

Bounded A1 repair — four `Optional` import additions in Foreman domain models:
- `foreman/domain/task.py`
- `foreman/domain/program.py`
- `foreman/domain/wave.py`
- `foreman/domain/blocker.py`

Parent: Issue #1233 baseline regression debt.
Parent QA lane: Issue #1226 / PR #1232 (Stage 6 re-entry — parked pending this merge).

## Disposition

- Phase 1 attestation: PASS — first builder commit after Foreman appointment control
- Production diff: PASS — four Optional import additions only
- Direct imports: PASS — EXIT_CODE: 0 all four modules
- Anti-dodging: PASS — no UTC, test, marker, workflow or dependency change
- Evidence completeness: PASS — all 10 required artifacts present
- Foreman QP: CONDITIONAL_PASS — pending CI re-run on updated head
- ECAP: PASS
- IAA final assurance: PENDING_CI

## Assurance bindings

Foreman QP: CONDITIONAL_PASS — `.agent-admin/quality/amc-a1-optional-import-1237-foreman-qp.md`
ECAP: PASS / ADMIN_VALIDATED — `.agent-admin/prehandover/ecap-reconciliation-1239.md`
IAA: PENDING_CI — `.agent-admin/assurance/iaa-wave-record-amc-a1-optional-import-1237.md`

## Next steps

1. PR #1239 marked ready for review → CI runs on head `49e5afec`
2. CI GREEN confirmed
3. IAA final assurance token `IAA-A1-1239-FINAL-PASS` issued
4. CS2 merge decision
5. After merge: unblock PR #1232 (Stage 6 qa-builder lane)

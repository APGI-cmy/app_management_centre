# API Builder Phase 1 Attestation — Issue #1237 A1

I attest that I am executing the bounded A1 appointment for Issue #1237 under the following frozen bindings:

- Role: `api-builder`
- Base commit: `ff5ec09024210789c2d2941a4aa6fe1ddb166515`
- Branch: `builder/issue-1237-a1-optional-imports`
- Contract blob: `f5d6c7789134600592343bd0fab0dc68d7d6fa30`
- IAA pre-brief blob: `f30dd3adaa9ad9be4b6bff2fe4bcd6b378a02d34`

## Authorized production scope

Add only the missing `Optional` typing import in:

- `foreman/domain/task.py`
- `foreman/domain/program.py`
- `foreman/domain/wave.py`
- `foreman/domain/blocker.py`

## Stop conditions acknowledged

HALT and report if any of the following occurs:

- binding mismatch (base/branch/blob drift)
- requested work outside allowlist or bounded A1 scope
- need to repair `UTC` or any non-A1 defect class
- unexpected failure class not attributable to bounded A1 `Optional` import repair

## Explicit prohibitions acknowledged

- no `UTC` import or datetime repair
- no test, marker, discovery, workflow, dependency, lock, config, infrastructure, deployment, credential, or Production changes
- no skip/xfail/ignore/deselection/assertion weakening
- no refactor or formatting churn
- no A2-T, A2-R, B1, or PR #1232 synchronization
- no modification of `qa/evidence/issue-1237/FOREMAN_APPOINTMENT_CONTROL.md`

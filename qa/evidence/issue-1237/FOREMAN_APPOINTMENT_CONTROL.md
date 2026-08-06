# Foreman Appointment Control — AMC A1 Optional Imports

## Identity

| Field | Value |
|---|---|
| Governing issue | #1237 |
| Parent blocker | #1233 |
| Task ID | `AMC-A1-OPTIONAL-IMPORT-1237` |
| Appointed role | `api-builder` |
| Appointment authority | Johan Ras, CS2, exercised through expressly authorised proxy |
| Appointment issue comment | `5103035549` |
| Appointment base | `ff5ec09024210789c2d2941a4aa6fe1ddb166515` |
| Appointment branch | `builder/issue-1237-a1-optional-imports` |
| Builder contract | `.github/agents/api-builder.md` |
| Contract blob | `f5d6c7789134600592343bd0fab0dc68d7d6fa30` |
| Canonical pre-brief | `.agent-admin/assurance/iaa-wave-record-amc-a1-optional-import-1237.md` |
| Pre-brief blob | `f30dd3adaa9ad9be4b6bff2fe4bcd6b378a02d34` |
| Integration builder | NOT APPOINTED |
| Merge authority | NOT GRANTED |

## Frozen target blobs

- `foreman/domain/task.py` — `6994d9713058afbb69805ccb1fb6f74ea6ba92bf`
- `foreman/domain/program.py` — `7ed374bac9b756df66f9bfde37f4713a0b552381`
- `foreman/domain/wave.py` — `2adabd64317c0c80c87adc370c50b5012100df1a`
- `foreman/domain/blocker.py` — `0433571718f52878b84d0240281940137de9b72e`

## Builder first-commit requirement

Before any runtime file change, the builder must complete Phase 1 and commit:

```text
qa/evidence/issue-1237/API_BUILDER_PHASE1_ATTESTATION.md
```

The attestation must bind the exact base, branch, contract blob and pre-brief blob above and acknowledge the four-file `Optional`-import-only scope and all stop conditions.

## Exact implementation boundary

The builder may add only the missing `Optional` typing import to:

```text
foreman/domain/task.py
foreman/domain/program.py
foreman/domain/wave.py
foreman/domain/blocker.py
```

No `UTC` import, datetime repair, test/configuration/workflow/dependency change, refactor, formatting churn, A2 work, B1 work or PR #1232 synchronisation is authorised.

## Read-only status

This Foreman appointment-control artifact is read-only to the builder. Alteration or deletion invalidates the appointment.

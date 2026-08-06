# Foreman Appointment Control — AMC A2-R UTC Runtime Repair

## Identity

| Field | Value |
|---|---|
| Governing issue | #1233 |
| Parent QA issue | #1226 |
| Task ID | `AMC-A2R-UTC-IMPORT-1233` |
| Appointed role | `api-builder` |
| Appointment authority | Johan Ras, CS2, exercised through expressly authorised proxy |
| Appointment issue comment | `5204208854` |
| Appointment branch | `builder/issue-1233-a2r-utc-imports` |
| Builder contract | `.github/agents/api-builder.md` |
| Canonical pre-brief | `.agent-admin/assurance/iaa-wave-record-amc-a2r-utc-import-1233.md` |
| Integration builder | NOT APPOINTED |
| Merge authority | NOT GRANTED |

## Builder first-commit requirement

Before any runtime file change, the builder must complete Phase 1 and commit:

```text
qa/evidence/issue-1233/API_BUILDER_PHASE1_ATTESTATION_A2R.md
```

The attestation must bind the exact branch, contract blob, and pre-brief blob
and acknowledge the runtime-only `UTC`-import scope and all stop conditions.

## Exact implementation boundary

The builder may add only the missing `UTC` import to:

```text
fm/orchestration/build_authorization_gate.py
fm/runtime/watchdog/alert_reader.py
fm/runtime/watchdog/escalation_reporter.py
foreman/analytics/cost_tracker.py
foreman/analytics/metrics_engine.py
foreman/analytics/storage.py
foreman/analytics/usage_analyzer.py
foreman/domain/blocker.py
foreman/domain/program.py
foreman/domain/task.py
foreman/domain/wave.py
foreman/flows/flow_executor.py
foreman/intent/approval_manager.py
foreman/intent/intake_handler.py
python_agent/memory_proposal_client.py
```

No test edits, no Stage 6 test work, no workflow/dependency/infrastructure
change, no refactor, no formatting churn, no Optional repair, and no A2-T/B1
authority is authorised.

## Read-only status

This Foreman appointment-control artifact is read-only to the builder.
Alteration or deletion invalidates the appointment.

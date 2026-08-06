# API Builder Phase 1 Attestation — A2-R UTC Import Repair

## Identity and appointment binding

- Governing issue: #1233
- Parent QA issue: #1226
- Task ID: `AMC-A2R-UTC-IMPORT-1233`
- Appointed role: `api-builder`
- Appointment branch (authoritative): `builder/issue-1233-a2r-utc-imports`
- Working branch (local session branch): `apgi-cmy-issue-1233-a2r-utc-imports`
- Appointment-control artifact: `qa/evidence/issue-1233/FOREMAN_APPOINTMENT_CONTROL_A2R_UTC.md`
- Appointment/base HEAD (at attestation): `d8fb71a33540d7a5e25380949fa9b6e74ff0c5f4`

## Blob bindings (exact)

- Builder contract path: `.github/agents/api-builder.md`
- Builder contract blob SHA: `f5d6c7789134600592343bd0fab0dc68d7d6fa30`
- Canonical pre-brief path: `.agent-admin/assurance/iaa-wave-record-amc-a2r-utc-import-1233.md`
- Canonical pre-brief blob SHA: `148f5dae046619277431d8daa28192faeb55b1ac`

## Scope attestation

I attest that A2-R implementation is constrained to import-only repair for the exact runtime allowlist:

1. `fm/orchestration/build_authorization_gate.py`
2. `fm/runtime/watchdog/alert_reader.py`
3. `fm/runtime/watchdog/escalation_reporter.py`
4. `foreman/analytics/cost_tracker.py`
5. `foreman/analytics/metrics_engine.py`
6. `foreman/analytics/storage.py`
7. `foreman/analytics/usage_analyzer.py`
8. `foreman/domain/blocker.py`
9. `foreman/domain/program.py`
10. `foreman/domain/task.py`
11. `foreman/domain/wave.py`
12. `foreman/flows/flow_executor.py`
13. `foreman/intent/approval_manager.py`
14. `foreman/intent/intake_handler.py`
15. `python_agent/memory_proposal_client.py`

No non-allowlisted production/runtime file will be changed.

## Prohibition attestation

I attest I will not:

- modify `tests/**` (including Stage 6 paths),
- modify workflows, dependencies, lock files, infrastructure, deployment, environment, credential, Supabase, Vercel, migration, or production settings,
- perform Optional import repair, intentional-RED lifecycle work, behavioural workaround, refactor, or formatting churn,
- alter Foreman appointment-control semantics beyond evidence required for this lane.

## Stop-condition attestation

I will halt and escalate if any required change falls outside import-only runtime UTC repair in the bounded A2-R allowlist.

# Issue #1235 — B0 Regression Population and Outcome Freeze

## Authority

- Governing issue: #1235
- Parent blocker: #1233
- Parent QA issue: #1226
- Parked draft PR: #1232
- Merged inventory PR: #1234
- Accepted B0 base: `eaf9ced583e61b2392a3772a1bea09944ee71439`
- Parent Stage 6 evidence head: `ebadbe0a25f8d8e88bfe154bb4e488c3a23dbd8d`
- Authoritative Stage 6 branch: `qa/issue-1226-stage6-executable-red-r2`
- Stage 6 test blob: `71bc3d0428e0ac2594ea53f72adfa3c10de01728`
- Parent non-wave0 log blob: `3a1984f46f51a884d7bae538656ea7f3694b5778`
- Parent wave0 log blob: `8bbd91e9596c221815cf81b70ac3cf17d161a984`
- Accepted `pytest.ini` blob: `13621e46ce44818368b3688e867f2f6a2f114848`

This is a governance and evidence record only. No repair builder is appointed and no test or runtime change is authorised.

## Frozen environment preparation

```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements-test.txt
```

Any dependency or pytest-configuration change after this freeze requires Foreman review before relying on population membership or counts.

## P1 — Wave0 ordinary population

### Commands

```bash
python -m pytest tests/ --collect-only -q -m wave0 --ignore=tests/amc/stage6
python -m pytest tests/ -v -m wave0 --ignore=tests/amc/stage6
```

### Frozen node manifest — 13 nodes

```text
tests/wave0_minimum_red/test_integration_sanity.py::TestTaskLifecycleTransitions::test_task_created_to_assigned_transition
tests/wave0_minimum_red/test_integration_sanity.py::TestTaskLifecycleTransitions::test_task_assigned_to_in_progress_transition
tests/wave0_minimum_red/test_integration_sanity.py::TestTaskLifecycleTransitions::test_task_in_progress_to_completed_transition
tests/wave0_minimum_red/test_integration_sanity.py::TestTaskLifecycleTransitions::test_task_cannot_skip_states
tests/wave0_minimum_red/test_integration_sanity.py::TestTaskLifecycleTransitions::test_task_state_transitions_are_logged
tests/wave0_minimum_red/test_integration_sanity.py::TestTaskLifecycleTransitions::test_task_lifecycle_validates_prerequisites
tests/wave0_minimum_red/test_integration_sanity.py::TestObservableFailureStates::test_task_failure_creates_explicit_failed_state
tests/wave0_minimum_red/test_integration_sanity.py::TestObservableFailureStates::test_failure_includes_explicit_reason
tests/wave0_minimum_red/test_integration_sanity.py::TestObservableFailureStates::test_failure_includes_diagnostic_information
tests/wave0_minimum_red/test_integration_sanity.py::TestObservableFailureStates::test_failure_state_creates_blocker
tests/wave0_minimum_red/test_integration_sanity.py::TestObservableFailureStates::test_failure_observable_in_program_status
tests/wave0_minimum_red/test_integration_sanity.py::TestObservableFailureStates::test_failure_triggers_escalation_notification
tests/wave0_minimum_red/test_integration_sanity.py::TestObservableFailureStates::test_failure_recovery_path_is_documented
```

Required final outcome: exactly `13 passed`, with zero failures, errors, skips or xfails. Collection must match the manifest exactly.

## P2 — Ordinary non-wave0 regression population

### Commands

```bash
python -m pytest tests/ --collect-only -q -m 'not wave0' \
  --ignore=tests/amc/stage6 \
  --ignore=tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py \
  --ignore=tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py

python -m pytest tests/ -v -m 'not wave0' \
  --ignore=tests/amc/stage6 \
  --ignore=tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py \
  --ignore=tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py
```

### Immutable population definition

P2 is not frozen by count alone. Its authoritative membership is the ordered non-wave0 node list recorded in immutable Git blob:

```text
3a1984f46f51a884d7bae538656ea7f3694b5778
```

Derive the exact P2 manifest by taking every collected node in that blob and removing only the exact 25 P3 node IDs frozen below. The resulting ordered manifest contains exactly `957` nodes.

The existing repository-level exclusion `tests/wave0_minimum_red/RED_QA` remains inherited from accepted `pytest.ini` blob `13621e46ce44818368b3688e867f2f6a2f114848`.

No substitution is permitted: a node removal paired with an added node is drift even when the total remains 957. Before B1, collection output must be compared node-for-node against the immutable derived manifest. Any difference requires file-by-file Foreman disposition.

Required final outcome: all exact P2 nodes passed, with zero failures, errors, skips or xfails.

## P3 — Retained expected-RED population

### Commands

```bash
python -m pytest \
  tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py \
  tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py \
  --collect-only -q

python -m pytest \
  tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py \
  tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py \
  -vv
```

### Frozen node manifest — 25 nodes

```text
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestAdvancedFlowScenarios::test_qa_211_state_persistence_across_flow
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestAdvancedFlowScenarios::test_qa_212_evidence_generation_across_flow
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestAdvancedFlowScenarios::test_qa_213_authorization_checks_across_flow
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestAdvancedFlowScenarios::test_qa_214_timeout_handling_in_flow
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestAdvancedFlowScenarios::test_qa_215_flow_cancellation
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestEscalationFlow::test_qa_216_escalation_end_to_end
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestEscalationFlow::test_qa_217_escalation_trigger_detection
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestEscalationFlow::test_qa_218_escalation_creation
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestEscalationFlow::test_qa_219_escalation_routing
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestEscalationFlow::test_qa_220_escalation_presentation
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestEscalationFlow::test_qa_221_escalation_decision
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestEscalationFlow::test_qa_222_escalation_resolution
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestEscalationFlow::test_qa_223_escalation_timeout
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestEscalationFlow::test_qa_224_multiple_concurrent_escalations
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py::TestEscalationFlow::test_qa_225_escalation_error_handling
tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py::TestPrioritizationFeatures::test_qa_416_assign_priority
tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py::TestPrioritizationFeatures::test_qa_417_sort_by_priority
tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py::TestPrioritizationFeatures::test_qa_418_priority_change_workflow
tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py::TestPrioritizationFeatures::test_qa_419_priority_escalation
tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py::TestPrioritizationFeatures::test_qa_420_priority_display
tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py::TestBulkOperations::test_qa_421_bulk_select
tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py::TestBulkOperations::test_qa_422_bulk_priority_update
tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py::TestBulkOperations::test_qa_423_bulk_archive
tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py::TestBulkOperations::test_qa_424_bulk_export
tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py::TestBulkOperations::test_qa_425_bulk_error_handling
```

Required final outcome: exactly `25 failed`, zero passed, errors, skips or xfails. Every failure must remain `NotImplementedError` for the frozen QA ID and owning subwave.

## P4 — Issue #1226 Stage 6 population

P4 does not exist on accepted B0 base `eaf9ced583e61b2392a3772a1bea09944ee71439`. It is pinned to PR #1232 branch `qa/issue-1226-stage6-executable-red-r2`, evidence head `ebadbe0a25f8d8e88bfe154bb4e488c3a23dbd8d`, and test blob `71bc3d0428e0ac2594ea53f72adfa3c10de01728`.

Before P4 collection or B1 execution, PR #1232 must be synchronised with the repaired `main` while preserving the pinned Stage 6 test blob and all authorised Issue #1226 evidence. B1 executes on that exact synchronised PR #1232 head, not on plain `main`.

### Commands — on the synchronised PR #1232 checkout

```bash
python -m pytest tests/amc/stage6 --collect-only -q
python -m pytest tests/amc/stage6 -vv
python -m pytest tests/amc/stage6 -vv
```

### Frozen node manifest — 19 nodes

```text
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_deploy_001_required_workflow_family_exists
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_deploy_002_production_jobs_use_protected_environment
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_deploy_003_non_production_jobs_cannot_reference_production_secrets
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_deploy_004_migration_command_is_frozen
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_deploy_006_required_runtime_and_workflow_variables_exist_in_env_example
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_deploy_007_health_and_smoke_evidence_exists
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_deploy_010_placeholder_evidence_is_rejected
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_config_001_startup_fails_if_any_required_env_is_missing
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_config_002_startup_error_names_missing_variable_explicitly
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_config_003_all_required_env_vars_are_individually_validated
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_des001_001_frontend_deploy_ownership_is_exclusive
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_des001_002_db_migration_ownership_is_exclusive
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_des002_001_ci_runner_is_ubuntu_latest
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_des003_001_no_workflow_uses_self_hosted_runner
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_des004_001_db_migrate_uses_exact_command
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_des005_001_db_migrate_trigger_is_manual_only
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_des006_001_frontend_workflow_has_no_db_mutation_step
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_des007_001_frontend_production_job_has_protected_environment
tests/amc/stage6/test_issue_1226_stage6_red.py::test_qa_des008_001_missing_next_public_supabase_url_fails_explicitly
```

Required outcome for each run: exactly `19 failed`, zero passed, errors, skips or xfails, with identical IDs and intended reasons.

## Frozen B1 evidence paths

```text
qa/evidence/issue-1235/b1/01_P1_COLLECTION.txt
qa/evidence/issue-1235/b1/02_P1_EXECUTION.txt
qa/evidence/issue-1235/b1/03_P2_COLLECTION.txt
qa/evidence/issue-1235/b1/04_P2_EXECUTION.txt
qa/evidence/issue-1235/b1/05_P3_COLLECTION.txt
qa/evidence/issue-1235/b1/06_P3_EXPECTED_RED.txt
qa/evidence/issue-1235/b1/07_P4_COLLECTION.txt
qa/evidence/issue-1235/b1/08_P4_RED_RUN1.txt
qa/evidence/issue-1235/b1/09_P4_RED_RUN2.txt
qa/evidence/issue-1235/b1/10_CHANGED_FILES.txt
qa/evidence/issue-1235/b1/11_ANTI_HIDING_SCAN.txt
qa/evidence/issue-1235/b1/B1_VALIDATION_SUMMARY.md
```

## Anti-hiding and anti-weakening controls

Prohibited unless a new Foreman disposition explicitly changes this freeze:

- modifying `pytest.ini`, any `conftest.py`, discovery patterns, markers or dependencies to alter membership;
- adding or removing skip, xfail, ignore, deselection, `-k`, file filters, `--maxfail` or early-exit behaviour;
- deleting, renaming, moving or weakening tests;
- changing expected-RED tests to pass, error, skip or xfail;
- changing Stage 6 tests or their expected reasons;
- hiding node substitution, count drift or changed failure reasons;
- mixing P1, P2, P3 or P4 evidence;
- implementing QA-211..225 or QA-416..425 under Issue #1233;
- appointing a repair builder before B0 merge and successor pre-brief approval.

## Changed-file controls

For this B0 PR, the exact control is:

```bash
git diff --name-status eaf9ced583e61b2392a3772a1bea09944ee71439...HEAD
```

Each successor issue must declare its own literal accepted-base commit and freeze the corresponding command before appointment. Placeholders are not permitted.

## Authoritative successor order

```text
B0 merge
  -> A1 missing Optional repair
  -> A2-T test-side UTC import repair
  -> A2-R runtime-side UTC import repair
  -> synchronise PR #1232 with repaired main while preserving pinned Stage 6 suite
  -> B1 execute P1-P4 on the exact synchronised PR #1232 head
  -> refresh PR #1232 evidence as part of B1
  -> Foreman QP
  -> ECAP
  -> independent IAA
  -> CS2 merge disposition
```

## B0 disposition

```text
P1 population: FROZEN
P2 population: FROZEN BY IMMUTABLE SOURCE BLOB AND DERIVATION RULE
P3 population: FROZEN
P4 population: FROZEN AND EXECUTION SOURCE PINNED
Commands: FROZEN
Expected outcomes: FROZEN
Evidence paths: FROZEN
Anti-hiding controls: FROZEN
Repair builder appointment: NOT AUTHORISED
PR #1232: OPEN / DRAFT / PARKED UNTIL REPAIRS LAND
Stage 6 acceptance: NO-GO
Stage 11: NO-GO
Stage 12: BLOCKED
```

# AMC A2-R UTC Import Repair — IAA Wave Record

## Identity

| Field | Value |
|---|---|
| Wave / job ID | `AMC-A2R-UTC-IMPORT-1233` |
| Governing issue | #1233 |
| Parent QA issue | #1226 |
| Parent draft PR | #1232 |
| Upstream predecessor | PR #1239 merged |
| Proposed delegated role | `api-builder` |
| Integration builder | **NOT APPOINTED** |
| ECAP applicability | REQUIRED — administrative only |
| Pre-brief disposition | `PREFLIGHT_BRIEF_COMPLETE` |
| Implementation authority | true on exact bounded scope only |

## PRE-BRIEF

IAA_PREFLIGHT_BRIEF

### Exact job

Repair only the runtime-side missing-`UTC` import defect class evidenced under
Issue #1233 by adding the minimal required `UTC` import to exact runtime files
that already call `datetime.now(UTC)` without importing `UTC`.

### Exact implementation scope

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

### Exact write allowlist

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
qa/evidence/issue-1233/**
PREHANDOVER_PROOF_A2R_1233.md
```

### Permitted change type

Import-only. The builder may add the minimal missing `UTC` import where required.
No other semantic, behavioural, control-flow, formatting, cleanup, refactor, or
cross-lane change is authorised.

### Mandatory exclusions

- no test-file changes of any kind (`tests/**` remains A2-T authority);
- no workflow, dependency, lock-file, environment, deployment, migration,
  Supabase, Vercel, credential, Production or infrastructure change;
- no `Optional` repair, no intentional-RED lifecycle work, no Stage 6 test
  mutation, no PR #1232 synchronisation, no A2-T expansion;
- no skip, xfail, ignore, warning suppression, assertion weakening, fixture
  rewrite, hidden deselection, mocking-away or behavioural workaround.

### Mandatory validation

```bash
python -m compileall -q fm foreman python_agent
python -m pytest tests/ --collect-only -q -m wave0 --ignore=tests/amc/stage6
python -m pytest tests/ -v -m wave0 --ignore=tests/amc/stage6
python -m pytest tests/ -v -m 'not wave0' --ignore=tests/amc/stage6
rg -n "from datetime import|datetime.now\\(UTC\\)|timezone.utc|pytest\\.skip|xfail|TODO|FIXME|NotImplemented" fm foreman python_agent qa/evidence/issue-1233 PREHANDOVER_PROOF_A2R_1233.md
git diff --name-only <appointment-base>...HEAD
```

### Foreman QP focus

1. Changed-file scope is confined to the exact runtime allowlist plus evidence.
2. Production/runtime diffs are import-only.
3. The targeted `UTC` defect class is removed without unrelated behaviour change.
4. No A2-T, B1, Stage 6, workflow, dependency or governance boundary collapse.
5. The final exact-head evidence remains independently reviewable.

### ECAP applicability

ECAP is REQUIRED and administrative only. ECAP may validate bindings, paths,
artifacts, timestamps and changed-file inventories, but may not decide repair
adequacy, readiness, assurance sufficiency, Stage 6 acceptance or merge
authority.

### Final independent IAA focus

Final IAA must verify exact-head binding, allowlist compliance, import-only diff,
zero boundary collapse into A2-T or B1, zero behavioural broadening, command
output completeness, QP integrity and ECAP role separation. A PASS may accept
only the bounded A2-R lane; it may not accept Stage 6, reverify Stages 7–10,
appoint `integration-builder`, or grant Stage 12 authority.

### Stop conditions

HALT and escalate on any need to modify test files, protected-path policy,
workflow/dependency/environment surfaces, intentional-RED test lifecycle,
unexpected non-import runtime change, ambiguous root cause, credential access,
Production mutation, or evidence that some failing `UTC` paths belong outside
the exact allowlist.

## Foreman disposition

```text
Sub-lane: A2-R runtime UTC import repair
Pre-brief: COMPLETE
Builder role: api-builder
Integration builder: NOT APPOINTED
Protected-path authority: NOT EXPANDED
Stage 6 acceptance: NOT GRANTED
Merge authority: NOT GRANTED
```

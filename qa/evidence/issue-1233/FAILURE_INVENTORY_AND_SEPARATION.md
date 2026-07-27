# Issue #1233 — Failure Inventory and Separation

## Authority and evidence base

- Governing issue: #1233
- Parent QA issue: #1226
- Parent draft PR: #1232
- Accepted repository base: `1d93459509abb92467f91deb4eefb879c1497362`
- Exact evidence head reviewed: `ebadbe0a25f8d8e88bfe154bb4e488c3a23dbd8d`
- Evidence logs:
  - `qa/evidence/issue-1226/COMMAND_LOG_05_REGRESSION_NOT_WAVE0.txt`
  - `qa/evidence/issue-1226/COMMAND_LOG_06_REGRESSION_WAVE0.txt`

No repair builder is appointed by this document.

## Reconciled execution totals

### `not wave0`

```text
69 failed
893 passed
13 deselected
20 errors
```

### `wave0`

```text
13 selected
13 errors
```

## Root-cause reconciliation

The result set reconciles exactly into three classes:

| Class | Count in `not wave0` | Count in `wave0` | Classification |
|---|---:|---:|---|
| Missing `UTC` imports | 44 failures | 0 | Genuine runtime/test defects |
| Missing `Optional` import in `foreman/domain/task.py` | 20 errors | 13 errors | Genuine import/runtime defect |
| Explicit `NotImplementedError` QA-to-RED obligations | 25 failures | 0 | Historical intentional RED obligations |
| **Total** | **69 failures + 20 errors** | **13 errors** | Reconciled |

## Class A — Genuine import/runtime defects

### A1. Missing `Optional` import

**Root cause:** `foreman/domain/task.py` references `Optional` in type annotations without importing it.

**Observed impact:**

- all 13 selected `wave0` tests error during fixture setup;
- 20 tests in the broad `not wave0` run error during shared fixture setup;
- failures occur before the intended test behaviours execute.

**Disposition:** genuine defect, suitable for a very small bounded repair lane.

**Proposed write allowlist:**

- `foreman/domain/task.py`
- dedicated reproduction/evidence paths for the repair issue

**Required proof:**

- import/compile proof;
- targeted wave0 collection and execution;
- no test modification;
- rerun of both parent regression commands.

### A2. Missing `UTC` imports

**Root cause:** production and test modules call `datetime.now(UTC)` but do not import `UTC` from `datetime`.

**Observed affected surfaces include:**

- `fm/orchestration/build_authorization_gate.py`
- `python_agent/memory_proposal_client.py`
- `fm/runtime/watchdog/alert_reader.py`
- `fm/runtime/watchdog/escalation_reporter.py`
- `foreman/analytics/metrics_engine.py`
- `foreman/analytics/cost_tracker.py`
- `foreman/analytics/usage_analyzer.py`
- `foreman/flows/flow_executor.py`
- `foreman/intent/intake_handler.py`
- `foreman/intent/approval_manager.py`
- affected test modules that themselves call `datetime.now(UTC)` without importing `UTC`

**Observed impact:** 44 ordinary test failures.

**Disposition:** genuine defects, but broader than A1. They must be inventoried file-by-file before appointment and corrected without behavioural changes beyond restoring the intended timezone symbol.

**Proposed write allowlist:** exact files proven to reference `UTC` without importing it, plus dedicated evidence files. No unrelated refactor.

**Required proof:**

- static inventory of every affected file;
- per-file import-only diff unless a different root cause is proven;
- focused tests for each owning subsystem;
- both parent regression commands rerun.

## Class B — Historical intentional QA-to-RED obligations

These failures are explicit, designed RED tests and must not be treated as accidental regressions.

### B1. Subwave 2.5 — Advanced Flow Scenarios

- File: `tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py`
- Markers: `wave2`, `subwave_2_5`
- QA range: `QA-211` through `QA-225`
- Count: 15
- Authority stated in file: BL-020 Corrective Action
- Each test explicitly raises `NotImplementedError` and states that the corresponding capability is not implemented yet.

**Disposition:** retained intentional RED. These tests may not be fixed, skipped, xfailed, renamed, deleted, or reclassified inside Issue #1233.

### B2. Subwave 2.2 — Parking Station Advanced

- File: `tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py`
- Markers: `wave2`, `subwave_2_2`
- QA range: `QA-416` through `QA-425`
- Count: 10
- Authority stated in file: BL-019 Emergency Corrective Action Plan
- Each test explicitly raises `NotImplementedError` and assigns later implementation ownership.

**Disposition:** retained intentional RED. These tests may not be fixed, skipped, xfailed, renamed, deleted, or reclassified inside Issue #1233.

## Canonical regression interpretation for Issue #1226

The broad command `-m 'not wave0'` mixes:

1. ordinary regression tests that should be GREEN; and
2. 25 explicitly intentional wave2 RED obligations.

Therefore, it cannot truthfully serve as a pure all-GREEN regression gate until governance explicitly defines how retained intentional RED suites are separated from the GREEN regression population.

This is not authority to hide or exclude debt. A canonical separation must:

- keep all intentional RED tests executable and visible;
- preserve their existing wave/subwave ownership;
- run them in a separately named expected-RED lane with evidence;
- keep the ordinary regression lane fully GREEN;
- prohibit blanket ignore, skip, xfail, deletion, or marker manipulation merely to obtain a passing result.

## Recommended governed sequence

1. **Repair Lane A1:** missing `Optional` import only.
2. Rerun `wave0` and broad collection to confirm setup errors are removed.
3. **Repair Lane A2:** exact missing-`UTC` import inventory and import-only corrections.
4. Rerun ordinary regressions and record remaining failures.
5. **Governance Lane B:** define the canonical expected-RED execution lane for the 25 retained wave2 obligations without weakening or hiding them.
6. Rerun:
   - ordinary GREEN regression population;
   - retained expected-RED population with exact expected failure IDs;
   - Issue #1226 Stage 6 suite twice RED.
7. Only after all three outcomes are proven may Issue #1226 Foreman QP resume.

## Prohibitions

- No repair builder appointment from this inventory alone.
- No modifications to `tests/amc/stage6/**`.
- No blanket skip, xfail, ignore, deselection, marker removal, or test deletion.
- No implementation of QA-211..225 or QA-416..425 under Issue #1233.
- No broad refactor while correcting import defects.
- No Stage 6 acceptance or downstream progression while the genuine defect lanes and canonical RED/GREEN separation remain unresolved.

## Foreman disposition

```text
Failure inventory: COMPLETE
Root-cause separation: COMPLETE
Genuine defect classes: A1 and A2
Historical intentional RED classes: B1 and B2
Repair builder appointment: NOT AUTHORISED
Issue #1226 Foreman QP: BLOCKED
PR #1232: DRAFT / NOT MERGE-READY
Stages 7–10: BLOCKED
Stage 11: NO-GO
integration-builder: NOT APPOINTED
Stage 12: BLOCKED
```

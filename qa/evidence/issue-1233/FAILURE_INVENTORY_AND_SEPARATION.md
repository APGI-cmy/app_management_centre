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
- rerun of all frozen populations defined by B0.

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

**Disposition:** genuine defects, but broader than A1 and spanning two authority surfaces. A2 is therefore split into two separately governed repair lanes.

#### A2-T — Test-side `UTC` import repair

**Authority surface:** exact affected test files only.

**Proposed role:** QA-builder.

**Write boundary:** exact test files proven to reference `UTC` without importing it, plus dedicated evidence files.

**Permitted change type:** import-only. No assertion, fixture, marker, expected-result, control-flow or behavioural changes.

**Required proof:**

- static file-by-file inventory;
- import-only diff;
- targeted test execution;
- rerun of all frozen populations defined by B0.

#### A2-R — Runtime-side `UTC` import repair

**Authority surface:** exact affected production/runtime files only.

**Proposed role:** appropriate Python/runtime builder, appointed only after B0 and a bounded pre-brief.

**Write boundary:** exact runtime files proven to reference `UTC` without importing it, plus dedicated evidence files.

**Permitted change type:** import-only unless a different root cause is independently proven and separately authorised. No refactor or behavioural expansion.

**Required proof:**

- static file-by-file inventory;
- import-only diff;
- focused subsystem tests for each owning surface;
- rerun of all frozen populations defined by B0.

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
- prohibit blanket ignore, skip, xfail, deletion, marker manipulation or undisclosed deselection merely to obtain a passing result.

## B0 — Regression population and outcome freeze

B0 is the mandatory first successor lane and is governance/evidence work only. It must complete before any repair builder is appointed.

B0 must freeze four exact populations:

1. **Wave0 ordinary population**
   - exact node manifest and command;
   - required final outcome: GREEN.

2. **Ordinary non-wave0 regression population**
   - exact node/file manifest and command;
   - may exclude only the separately frozen retained expected-RED node set;
   - required final outcome: GREEN.

3. **Retained expected-RED population**
   - exactly QA-211 through QA-225 and QA-416 through QA-425;
   - exact node manifest and command;
   - required final outcome: exactly 25 failures for the frozen intentional reasons.

4. **Issue #1226 Stage 6 population**
   - exactly the 19 tests in `tests/amc/stage6/test_issue_1226_stage6_red.py`;
   - exact command;
   - required final outcome: RED twice with the same exact test IDs and intended reasons.

B0 must also freeze:

- success and stop criteria for every population;
- anti-hiding controls;
- changed-file and marker controls;
- evidence log names and retention paths;
- the prohibition on blanket skip, xfail, ignore, deletion, marker removal, test renaming or undisclosed deselection.

## Authoritative governed sequence

1. **Accept this Issue #1233 inventory and separation record.**
2. **B0 — Regression population and outcome freeze.** No repair builder appointment before B0 acceptance.
3. **A1 — Missing `Optional` import repair.** One production file plus evidence only.
4. Rerun wave0 and broad collection to prove the setup-error class is removed.
5. **A2-T — Test-side missing-`UTC` import repair.** Exact affected test files, import-only.
6. **A2-R — Runtime-side missing-`UTC` import repair.** Exact affected runtime files, import-only.
7. **B1 — Final governed execution of the frozen populations:**
   - wave0 ordinary population GREEN;
   - ordinary non-wave0 regression population GREEN;
   - retained 25-test expected-RED population RED for exactly the frozen reasons;
   - Issue #1226 19-test suite RED twice for exactly the frozen reasons.
8. Refresh PR #1232 evidence and complete Foreman QP, ECAP and independent IAA bound to the final exact head.
9. Only after those controls pass may Stage 6 acceptance and Stages 7–10 reverification resume.

## Prohibitions

- No repair builder appointment from this inventory alone.
- No repair builder appointment before B0 is accepted.
- No modifications to `tests/amc/stage6/**` under Issue #1233.
- No blanket skip, xfail, ignore, deletion, marker removal, test renaming or undisclosed deselection.
- No implementation of QA-211..225 or QA-416..425 under Issue #1233.
- No broad refactor while correcting import defects.
- No mixing of A2-T and A2-R authority surfaces in one builder allowlist.
- No Stage 6 acceptance or downstream progression while the genuine defect lanes and canonical RED/GREEN separation remain unresolved.

## Foreman disposition

```text
Failure inventory: COMPLETE
Root-cause separation: COMPLETE
Authoritative sequence: B0 -> A1 -> A2-T -> A2-R -> B1
Genuine defect classes: A1, A2-T and A2-R
Historical intentional RED classes: B1 and B2
Repair builder appointment: NOT AUTHORISED before B0 acceptance
Issue #1226 Foreman QP: BLOCKED
PR #1232: DRAFT / NOT MERGE-READY
Stages 7–10: BLOCKED
Stage 11: NO-GO
integration-builder: NOT APPOINTED
Stage 12: BLOCKED
```

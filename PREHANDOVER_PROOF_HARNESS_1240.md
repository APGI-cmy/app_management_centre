# PREHANDOVER PROOF — HARNESS CORRECTION #1240

**PR:** #1241  
**Issue:** #1240  
**Branch:** `foreman/issue-1240-harness-yaml-marker`  
**Exact validation head:** `45d7f1ed44fb8a63425ef04de2768f658cb4c7f1`  
**Accepted base:** `ff5ec09024210789c2d2941a4aa6fe1ddb166515`  
**A1 triggering PR:** #1239  
**A1 head for combined proof:** `cf6b276898d8e9d761f8c38f5c4ee421c1d5a122`  
**UTC:** 2026-07-29T10:55:00Z  
**Merge authority:** NOT GRANTED  

---

## Implementation Summary

PR #1241 applies exactly two harness corrections to unblock the frozen P1 commands:

| Commit | File | Change |
|--------|------|--------|
| `70c26e5` | `requirements.txt` | Added `PyYAML>=6.0` |
| `ebd43e9` | `pytest.ini` | Added `subwave_3_3: Subwave 3.3 Governance Dashboard V2 tests` |
| `45d7f1e` | `qa/evidence/issue-1240/FOREMAN_HARNESS_CORRECTION_CONTROL.md` | Foreman control record |

---

## Part A — Exact-head Validation (PR #1241 head `45d7f1ed`)

### Environment
- Python 3.12.3 / pytest 9.1.1 / PyYAML 6.0.3
- Clean venv `.venv-harness-1240`
- `pip check`: No broken requirements found

### Harness acceptance checks

| Check | Result |
|-------|--------|
| HEAD = `45d7f1ed44fb8a63425ef04de2768f658cb4c7f1` (no drift) | ✅ PASS |
| `PyYAML>=6.0` in requirements.txt | ✅ PASS |
| `import yaml` succeeds, version 6.0.3 | ✅ PASS |
| No `ModuleNotFoundError: yaml` | ✅ PASS |
| `subwave_3_3` registered in pytest.ini | ✅ PASS |
| No `subwave_3_3 not found in markers` error | ✅ PASS |
| `--strict-markers` retained in addopts | ✅ PASS |
| P1 collection: exactly 13 nodes, 0 errors | ✅ PASS |
| No skip/xfail/PYTEST_ADDOPTS/narrowing | ✅ PASS |

### P1 execution — exact head
```
13 selected / 13 errors / exit 1
All errors: NameError: name 'Optional' is not defined
  foreman/domain/task.py:86: def get_by_id(cls, task_id: str) -> Optional['Task']
```
**Classification:** `EXPECTED SEPARATE A1 DEFECT — PR #1239 NOT YET MERGED`  
Not a regression. Harness correction is not the cause.

---

## Part B — Isolated Combined-State Proof

Disposable worktree at A1 head `cf6b276898d8e9d761f8c38f5c4ee421c1d5a122`.  
Harness deltas applied via cherry-pick (no-commit).  
No combined branch pushed. Worktree removed after evidence capture.

### Combined-state acceptance checks

| Check | Result |
|-------|--------|
| P1 collection: exactly 13 nodes | ✅ PASS |
| Zero collection errors | ✅ PASS |
| Zero `Optional` NameError | ✅ PASS (PR #1239 repair present) |
| Zero YAML import failure | ✅ PASS |
| Zero strict-marker failure | ✅ PASS |
| No skip/xfail/config override | ✅ PASS |
| Disposable worktree removed | ✅ PASS |

### P1 execution — combined state
```
13 selected / 13 failed / exit 1
All failures: NameError: name 'UTC' is not defined
  foreman/domain/task.py:76: self.created_at = datetime.now(UTC)
```
**Classification:** `RETAINED UTC A2-R DEFECT — SEPARATELY FROZEN`  
All remaining RED maps exclusively to the UTC A2-R defect class.  
No new failure class introduced.

---

## Anti-Dodging Scan

| Pattern | Found in | Assessment |
|---------|----------|-----------|
| `PyYAML` | `requirements.txt:9` only | Correct — declared once |
| `subwave_3_3` | `pytest.ini:50`, test file decorators | Correct — marker declared, tests consume it |
| `--strict-markers` | `pytest.ini:17` | Retained — strict enforcement active |
| `PYTEST_ADDOPTS` | Not found in scope | PASS |
| `pytest.skip` | Not found in scope | PASS |
| `xfail` | Not found in scope | PASS |

---

## Changed Files (vs accepted base `ff5ec09`)

```
M  requirements.txt
M  pytest.ini
A  qa/evidence/issue-1240/FOREMAN_HARNESS_CORRECTION_CONTROL.md
```
(plus evidence files within declared allowlist)

---

## Final Verdict

| Domain | Verdict |
|--------|---------|
| Harness: PyYAML install & yaml import | ✅ PASS |
| Harness: subwave_3_3 strict-marker | ✅ PASS |
| Harness: strict enforcement retained | ✅ PASS |
| P1 collection: 13 nodes, 0 errors | ✅ PASS |
| A1 Optional defect classified | ✅ CLASSIFIED (expected, PR #1239) |
| Combined-state: 13 nodes, 0 collection errors | ✅ PASS |
| Combined-state UTC A2-R defect classified | ✅ CLASSIFIED (separately frozen) |
| Scope and anti-dodging | ✅ PASS |
| No test/application/runtime edits | ✅ CONFIRMED |
| No merge authority exercised | ✅ CONFIRMED |

---

## READY FOR FOREMAN QP

# Issue #1233 — Durable Regression Evidence Snapshot

## Source authority

- Parent issue: #1226
- Parent PR: #1232
- Exact parent evidence head: `ebadbe0a25f8d8e88bfe154bb4e488c3a23dbd8d`
- Parent branch: `qa/issue-1226-stage6-executable-red-r2`
- Source log blob — non-wave0: `3a1984f46f51a884d7bae538656ea7f3694b5778`
- Source log blob — wave0: `8bbd91e9596c221815cf81b70ac3cf17d161a984`

This snapshot is committed with PR #1234 so the inventory remains independently reviewable after merge even if the parent branch changes.

## Environment preparation

```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements-test.txt
```

Both installation commands completed successfully before the recorded regression runs.

## Command A — broad non-wave0 regression execution

```bash
python -m pytest tests/ -v -m 'not wave0' --ignore=tests/amc/stage6
```

### Recorded session summary

```text
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/runner/work/app_management_centre/app_management_centre
configfile: pytest.ini
collected 995 items / 13 deselected / 982 selected
69 failed, 893 passed, 13 deselected, 20 errors
```

### Exact reconciliation

```text
44 failures: missing UTC imports
25 failures: explicit historical NotImplementedError QA-to-RED obligations
20 errors: missing Optional import in foreman/domain/task.py
```

### Missing `Optional` signature

```text
foreman/domain/task.py:86
    def get_by_id(cls, task_id: str) -> Optional['Task']:
NameError: name 'Optional' is not defined
```

This one import defect caused 20 non-wave0 setup errors.

### Missing `UTC` signature

Representative trace:

```text
fm/orchestration/build_authorization_gate.py:145
    timestamp=datetime.now(UTC).isoformat() + 'Z'
NameError: name 'UTC' is not defined
```

The same root-cause pattern was observed across build authorisation, memory proposals, watchdog, analytics, flow and intent surfaces, plus affected tests that themselves call `datetime.now(UTC)` without importing `UTC`.

### Exact retained intentional-RED node ranges

#### Subwave 2.5 — Advanced Flow Scenarios

File:

```text
tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py
```

Exact IDs:

```text
QA-211
QA-212
QA-213
QA-214
QA-215
QA-216
QA-217
QA-218
QA-219
QA-220
QA-221
QA-222
QA-223
QA-224
QA-225
```

Each test explicitly raises `NotImplementedError` and identifies Subwave 2.5 implementation ownership.

#### Subwave 2.2 — Parking Station Advanced

File:

```text
tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py
```

Exact IDs:

```text
QA-416
QA-417
QA-418
QA-419
QA-420
QA-421
QA-422
QA-423
QA-424
QA-425
```

Each test explicitly raises `NotImplementedError` and identifies later UI-builder implementation ownership.

## Command B — wave0 execution

```bash
python -m pytest tests/ -v -m wave0 --ignore=tests/amc/stage6
```

### Recorded session summary

```text
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/runner/work/app_management_centre/app_management_centre
configfile: pytest.ini
collected 995 items / 982 deselected / 13 selected
13 errors
```

All 13 errors share the same root cause:

```text
foreman/domain/task.py:86
    def get_by_id(cls, task_id: str) -> Optional['Task']:
NameError: name 'Optional' is not defined
```

## Audit conclusion

The evidence supports exactly three classes:

| Class | Non-wave0 | Wave0 | Disposition |
|---|---:|---:|---|
| Missing `UTC` imports | 44 failures | 0 | genuine defects |
| Missing `Optional` import | 20 errors | 13 errors | genuine defect |
| Explicit retained `NotImplementedError` obligations | 25 failures | 0 | intentional RED |

No skip, xfail, deletion, marker removal, renaming or hidden deselection is authorised by this snapshot.

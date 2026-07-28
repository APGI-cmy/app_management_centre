# PREHANDOVER PROOF — A1 Optional Imports (Issue #1237)

## Bound identifiers

- Issue: `#1237`
- Base: `ff5ec09024210789c2d2941a4aa6fe1ddb166515`
- Branch: `builder/issue-1237-a1-optional-imports`
- Contract blob: `f5d6c7789134600592343bd0fab0dc68d7d6fa30`
- Pre-brief blob: `f30dd3adaa9ad9be4b6bff2fe4bcd6b378a02d34`

## Authorized production delta

Added missing `Optional` typing import only in:

- `foreman/domain/task.py`
- `foreman/domain/program.py`
- `foreman/domain/wave.py`
- `foreman/domain/blocker.py`

## Mandatory validation evidence

### 1) Compile targeted modules

Command:

```bash
python -m compileall -q foreman/domain/task.py foreman/domain/program.py foreman/domain/wave.py foreman/domain/blocker.py
```

Result: **PASS** (exit 0)

### 2) Import targeted modules

Command:

```bash
python -c "import foreman.domain.task, foreman.domain.program, foreman.domain.wave, foreman.domain.blocker"
```

Result: **PASS** (exit 0)

### 3) P1 collect-only check

Command:

```bash
python -m pytest tests/ --collect-only -q -m wave0 --ignore=tests/amc/stage6
```

Result: **BLOCKED IN ENVIRONMENT** (exit 2)

Observed blockers:

- `ModuleNotFoundError: No module named 'flask'`
- `ModuleNotFoundError: No module named 'sqlalchemy'`
- marker config failure: `'subwave_3_3' not found in markers`

Collection line remained:

- `collected 905 items / 4 errors / 892 deselected / 13 selected`

### 4) P1 execution check

Command:

```bash
python -m pytest tests/ -v -m wave0 --ignore=tests/amc/stage6
```

Result: **BLOCKED IN ENVIRONMENT** (exit 2)

Observed blockers are the same 4 collection errors above.

### 5) Scope and token scan

Command:

```bash
rg -n "(pytest\.skip|xfail|TODO|FIXME|NotImplemented|from typing import|from datetime import)" foreman/domain/task.py foreman/domain/program.py foreman/domain/wave.py foreman/domain/blocker.py qa/evidence/issue-1237 PREHANDOVER_PROOF_A1_1237.md
```

Result: **PASS** (run output captured in final validation step)

### 6) Diff against frozen base

Command:

```bash
git diff --name-status ff5ec09024210789c2d2941a4aa6fe1ddb166515...HEAD
```

Result captured after final commit.

## A1 boundary statement

- No `UTC` import or datetime repair performed.
- No test/config/workflow/dependency/infra/production changes made.
- Production change class stayed import-only for `Optional` in the 4 authorized files.

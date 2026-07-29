# Foreman Harness Correction Control — Issue #1240

## Identity

- Governing issue: `#1240`
- Triggering blocked lane: PR `#1239` / Issue `#1237`
- Owner: AMC Foreman
- Branch: `foreman/issue-1240-harness-yaml-marker`
- Base branch: `main`
- Merge authority: **NOT GRANTED**

## Exact defects corrected

1. `tests/test_modular_agent_loading.py` imports `yaml`, while `requirements.txt` did not declare PyYAML.
2. Strict marker enforcement was active while `pytest.ini` omitted the marker used by the suite: `subwave_3_3`.

## Exact implementation

- `requirements.txt`
  - added `PyYAML>=6.0`
- `pytest.ini`
  - added `subwave_3_3: Subwave 3.3 Governance Dashboard V2 tests`

## Boundary

No test, application/runtime, workflow, migration, infrastructure, credential, deployment or Production file is authorised in this lane.

No `UTC` repair is included.

PR #1239 remains open, draft and blocked until this harness correction is independently validated, merged with explicit CS2 approval, and then synchronised into its branch.

## Required validation

```bash
python -m venv .venv-harness-1240
. .venv-harness-1240/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pytest
python -m pip check
python -c "import yaml; print(yaml.__version__)"
python -m pytest tests/ --collect-only -q -m wave0 --ignore=tests/amc/stage6
python -m pytest tests/ -v -m wave0 --ignore=tests/amc/stage6
rg -n "PyYAML|subwave_3_3" requirements.txt pytest.ini
git diff --name-status main...HEAD
```

## Acceptance target

- dependency installation succeeds;
- `import yaml` succeeds;
- strict-marker collection no longer errors for `subwave_3_3`;
- exact frozen P1 population remains 13 selected nodes;
- remaining P1 RED, if any, is exclusively the separately frozen `UTC` A2-R defect class;
- no scope expansion.

# Foreman Plan — Baseline Regression Harness Recovery

## Parent authority

- Governing issue: #1226
- Parent PR: #1232
- Parent head at diagnosis: `45cf847326d1b2c7d4e35d3280b12f1a18b741fb`
- Purpose: unblock the two mandatory non-target regression commands without weakening the Stage 6 RED suite.

## Confirmed diagnosis

1. `Flask>=3.0.0` and `SQLAlchemy>=2.0.0` are already declared in root `requirements.txt`.
2. The failed regression session did not install the declared repository requirements before collection.
3. `tests/wave2_0_qa_infrastructure/test_enhanced_dashboard.py` uses `@pytest.mark.subwave_3_3`.
4. Root `pytest.ini` enables `--strict-markers` but does not register `subwave_3_3`.

## Bounded repair

- Add only the missing `subwave_3_3` marker registration to `pytest.ini`.
- Before rerunning regressions, execute:

```bash
python -m pip install -r requirements.txt
```

- Do not modify `requirements.txt`, dependency versions, Stage 6 tests, runtime code, workflows, infrastructure or Production configuration.

## Required reruns

```bash
python -m pytest tests/ -v -m 'not wave0' --ignore=tests/amc/stage6
python -m pytest tests/ -v -m wave0 --ignore=tests/amc/stage6
```

Preserve unedited outputs and refresh the Issue #1226 validation summary and PREHANDOVER proof.

## Stop conditions

Stop on any additional missing dependency not declared in repository manifests, new collection defect, unrelated failing test, need to weaken/exclude tests, or requirement to modify any path outside the approved harness/evidence scope.

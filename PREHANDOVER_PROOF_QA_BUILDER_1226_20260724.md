# PRE-HANDOVER Proof — QA Builder Issue #1226 Stage 6 Re-entry

## Scope and boundary

- Role: `qa-builder`
- Branch: `qa/issue-1226-stage6-executable-red-r2`
- Accepted base: `1d93459509abb92467f91deb4eefb879c1497362`
- Allowed writes respected: `tests/amc/stage6/**`, `qa/evidence/issue-1226/**`, this prehandover file

## Delivery produced

- Added bounded executable Stage 6 RED suite: `tests/amc/stage6/test_issue_1226_stage6_red.py`
- Produced required phase-1 attestation file
- Captured two reproducible target RED executions
- Captured compile/collect and regression command outputs
- Produced test-ID failure mapping summary

## Command evidence index

- `qa/evidence/issue-1226/COMMAND_LOG_01_COMPILEALL.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_02_COLLECT_ONLY.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_03_STAGE6_RED_RUN1.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_04_STAGE6_RED_RUN2.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_04A_PIP_INSTALL.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_05_REGRESSION_NOT_WAVE0.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_06_REGRESSION_WAVE0.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_07_ANTI_DODGING_SCAN.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_08_CHANGED_FILES.txt`
- `qa/evidence/issue-1226/STAGE6_VALIDATION_SUMMARY.md`

## Stop condition encountered

After Foreman baseline harness recovery, declared dependencies were installed and both required non-target regression commands were rerun. Both suites reached normal execution but are still not GREEN:

- `python -m pytest tests/ -v -m 'not wave0' --ignore=tests/amc/stage6` ended `69 failed, 893 passed, 13 deselected, 20 errors`
- `python -m pytest tests/ -v -m wave0 --ignore=tests/amc/stage6` ended with `13` errors
- recurring blocking error: `NameError: name 'Optional' is not defined` from `foreman/domain/task.py`

This remains a hard-stop condition because the mandatory non-target regression requirement is not yet GREEN.

## W1/W7 ownership preservation

No runtime/workflow/migration/deployment/infrastructure implementation was added. Missing W7 targets remain RED guards only.

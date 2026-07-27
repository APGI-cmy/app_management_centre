# Issue #1226 Stage 6 — Executable RED Validation Summary

## Run posture

- Suite path: `tests/amc/stage6/test_issue_1226_stage6_red.py`
- Collection: GREEN (`19` tests collected)
- Target run 1: RED (`19` failed)
- Target run 2: RED (`19` failed)
- Reproducibility: same failing test IDs and same intended unmet reasons across both runs

## Test-ID to intended RED reason map

| Test ID | Intended RED reason | Run 1 | Run 2 |
|---|---|---|---|
| QA-DEPLOY-001 | Required workflow family missing (`ci.yml`, `deploy-frontend.yml`, `db-migrate.yml`) | RED | RED |
| QA-DEPLOY-002 | Protected-production validation blocked because `deploy-frontend.yml`/`db-migrate.yml` are absent | RED | RED |
| QA-DEPLOY-003 | PR/staging production-secret isolation validation blocked because `ci.yml` is absent | RED | RED |
| QA-DEPLOY-004 | Migration command freeze validation blocked because `db-migrate.yml` is absent | RED | RED |
| QA-DEPLOY-006 | `.env.example` missing required `SUPABASE_PROJECT_REF` workflow/runtime variable | RED | RED |
| QA-DEPLOY-007 | Deployment health/smoke evidence artifact absent | RED | RED |
| QA-DEPLOY-010 | Placeholder evidence disposition artifact absent | RED | RED |
| QA-CONFIG-001 | Runtime startup validation for required W1 variable set is absent | RED | RED |
| QA-CONFIG-002 | Runtime startup explicit named missing-variable error handling is absent | RED | RED |
| QA-CONFIG-003 | Full required startup-variable validation set not implemented (`0/12`) | RED | RED |
| QA-DES001-001 | Frontend deploy workflow ownership unmet because `deploy-frontend.yml` absent | RED | RED |
| QA-DES001-002 | DB migration workflow ownership unmet because `db-migrate.yml` absent | RED | RED |
| QA-DES002-001 | CI runner policy unmet because `ci.yml` absent | RED | RED |
| QA-DES003-001 | Repository-wide runner validation blocked because required workflows are absent | RED | RED |
| QA-DES004-001 | Exact migration command validation blocked because `db-migrate.yml` absent | RED | RED |
| QA-DES005-001 | Manual-only migration trigger validation blocked because `db-migrate.yml` absent | RED | RED |
| QA-DES006-001 | Frontend no-db-mutation validation blocked because `deploy-frontend.yml` absent | RED | RED |
| QA-DES007-001 | Frontend protected-production environment validation blocked because `deploy-frontend.yml` absent | RED | RED |
| QA-DES008-001 | Startup explicit `NEXT_PUBLIC_SUPABASE_URL` fail-fast validation path absent | RED | RED |

## Non-target regression execution result

Both required regression commands exited during collection with unrelated environment/baseline errors:

- `ModuleNotFoundError: No module named 'flask'`
- `ModuleNotFoundError: No module named 'sqlalchemy'`
- marker registration error: `'subwave_3_3' not found in markers configuration`

Per hard-stop contract, this is recorded as an encountered stop condition.

## Evidence log paths

- `qa/evidence/issue-1226/COMMAND_LOG_01_COMPILEALL.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_02_COLLECT_ONLY.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_03_STAGE6_RED_RUN1.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_04_STAGE6_RED_RUN2.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_05_REGRESSION_NOT_WAVE0.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_06_REGRESSION_WAVE0.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_07_ANTI_DODGING_SCAN.txt`
- `qa/evidence/issue-1226/COMMAND_LOG_08_CHANGED_FILES.txt`

# AMC W1 RED-Test and Evidence Map

## Status

| Field | Value |
|---|---|
| Issue | #1205; corrected by #1222 |
| PR | #1206; correction carrier PR #1229 |
| Candidate | `integration-builder` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Status | ✅ Corrected / Binding for pre-appointment traceability — executable intended-RED evidence remains unproduced |

The canonical meanings below come from the Stage 6
`functional-delivery-red-test-expansion-matrix.md` and the Stage 6 QA/DES
traceability pack. This correction replaces the earlier mismatched labels for
`QA-DEPLOY-002/003/004/006/007/010`.

## Exact pre-appointment RED inventory

Creating an executable RED before appointment does not reassign the later GREEN
implementation owner. Cross-wave guards may be deliberately RED before W1, while
their implementation and GREEN exit remain W7 obligations.

| Test / control | Canonical failure focus | Pre-`integration-builder` RED posture | GREEN implementation / exit owner |
|---|---|---|---|
| `QA-DEPLOY-001` | `ci.yml`, `deploy-frontend.yml`, or `db-migrate.yml` missing/renamed without CS2 disposition | Mandatory cross-wave executable guard. It may be RED because `db-migrate.yml` is not yet produced. | W1: `ci.yml` and `deploy-frontend.yml`; W7: `db-migrate.yml`. Full test becomes GREEN only when all applicable wave outputs exist. |
| `QA-DEPLOY-002` | Production deployment or migration job lacks protected `production` environment | Mandatory executable protected-production guard; evaluate each production job that exists. | W1: frontend production job; W7: migration production job. |
| `QA-DEPLOY-003` | PR or staging job can access Production secrets | Mandatory W1 executable isolation guard. | W1 secret/environment boundary. |
| `QA-DEPLOY-004` | Migration uses a command other than `supabase db push --project-ref $SUPABASE_PROJECT_REF`, or uses linked/hardcoded drift | Mandatory cross-wave executable guard, expected RED/absent-target until the W7 migration workflow exists. It must not require W1 to create `db-migrate.yml`. | W7 migration execution. |
| `QA-DEPLOY-006` | Required runtime/workflow variable is absent from `.env.example` | Mandatory W1 executable configuration-contract guard. | W1 environment template. |
| `QA-DEPLOY-007` | Deployment evidence lacks app/API/Supabase/realtime health or smoke validation | Mandatory cross-wave evidence-contract RED. It must not be presented as W1 health/smoke GREEN. | W7 deployment execution and health/smoke evidence. |
| `QA-DEPLOY-010` | Placeholder evidence is accepted as completed deployment proof | Mandatory executable anti-placeholder evidence guard. | Applies to W1 evidence and every later wave. |
| `QA-CONFIG-001/002/003` | Startup accepts missing required variables, hides the variable name, or omits variables from the required set | Mandatory W1 executable runtime-configuration guards. | W1 runtime/environment contract. |
| `QA-DES001-001` | A workflow other than `deploy-frontend.yml` owns frontend deployment | Mandatory W1 executable workflow-ownership guard. | W1. |
| `QA-DES001-002` | A workflow other than `db-migrate.yml` owns database migration | Mandatory cross-wave executable guard; target owner remains deferred. | W7. |
| `QA-DES002-001` | `ci.yml` does not use `ubuntu-latest` | Mandatory W1 executable runner guard. | W1. |
| `QA-DES003-001` | Any workflow uses self-hosted/custom runners | Mandatory W1 executable repository-wide runner guard. | W1 and ongoing. |
| `QA-DES004-001` | `db-migrate.yml` does not use the exact approved migration command | Mandatory cross-wave executable guard; expected RED/absent-target before W7. | W7. |
| `QA-DES005-001` | `db-migrate.yml` has a trigger other than `workflow_dispatch` | Mandatory cross-wave executable guard; expected RED/absent-target before W7. | W7. |
| `QA-DES006-001` | `deploy-frontend.yml` contains database mutation | Mandatory W1 executable no-Production-side-effect guard. | W1. |
| `QA-DES007-001` | Frontend production job lacks `environment: production` | Mandatory W1 executable protected-environment guard. | W1. |
| `QA-DES008-001` | Startup without `NEXT_PUBLIC_SUPABASE_URL` does not fail explicitly | Mandatory W1 executable fail-fast configuration guard. | W1. |

## W1 versus W7 boundary

- Stage 8 keeps `db-migrate.yml`, migration command proof, rollback and
  health/smoke execution in W7.
- CS2-authorized Issue #1226 may delegate a bounded Stage 6 QA-remediation role to
  create executable RED guards for those future obligations. This is not a Stage 11
  appointment; Stage 11 remains unavailable until Stage 6 is corrected and dependent
  Stages 7–10 are reverified.
- A RED guard does not authorize W1 implementation of its target and is not a W1
  GREEN exit requirement where the table assigns W7.
- `integration-builder` remains unappointed until the executable suite has been
  observed failing for the intended, correctly classified reasons and accepted
  through QP, ECAP, IAA and CS2.

## Evidence classes required from W1

1. Exact `ci.yml` and `deploy-frontend.yml` paths and ownership.
2. Runtime and package/tool version contract.
3. Root `.env.example` variable contract without real secrets.
4. CI, type, lint, test and schema-validation logs.
5. Preview project URL or governed project reference where applicable.
6. Preview/staging/Production environment separation evidence.
7. No-Production-side-effect evidence for PR CI.
8. Secret-boundary evidence without exposing values.
9. Protected frontend-production approval evidence.
10. Dependency and environment ownership evidence.
11. Visible failure/blocking evidence when required resources are unavailable.
12. Tracker/index and wave-evidence linkage.

Migration command, rollback and health/smoke GREEN evidence remain W7 exit
evidence; their executable RED guards may be created earlier under the bounded
QA-builder lane.

## Prohibited proof

The following cannot satisfy the pre-appointment requirement:

- workflow names without repository paths or owner;
- screenshots containing secret values;
- a successful documentation-only gate used as proof of implementation-gate readiness;
- skipped, todo, stub-only, placeholder or trivially passing tests;
- warnings ignored or suppressed;
- preview using Production credentials or Production data;
- manual assertions without reproducible evidence;
- changing tests to match an implementation shortcut;
- treating a W7 target as a W1 implementation obligation merely because its RED guard exists.

## Current result

The earlier W1 map contained six incorrect canonical labels; Issue #1222 and IAA
finding `IAA-1229-B1-TRACE-001` corrected them and made the W1/W7 split explicit.
Executable tests and observed intended-RED evidence are still not committed.
Supabase develop and Vercel configuration are not independently visible through
the current connectors, and the bootstrap control is not operational in the
current session.

**Current result: BLOCKING for `integration-builder` appointment pending Issues
#1226, #1227 and #1228.**

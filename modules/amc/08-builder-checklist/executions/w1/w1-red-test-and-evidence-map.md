# AMC W1 RED-Test and Evidence Map

## Status

| Field | Value |
|---|---|
| Issue | #1205 |
| PR | #1206 |
| Candidate | `integration-builder` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Status | ✅ Defined / Binding for W1 — candidate comprehension accepted in merged PR #1216; executable intended-RED evidence remains unproduced |

---

## W1 RED Obligations

| Test / control | W1 intent | Required later GREEN evidence | Candidate comprehension |
|---|---|---|---|
| `QA-DEPLOY-001` | Required deployment workflow family exists and is owned | Full-path workflow definitions and owner evidence | COMPREHENSION ACCEPTED — executable RED pending |
| `QA-DEPLOY-002` | PR CI has no production side effects | Workflow/test evidence proving no production mutation | COMPREHENSION ACCEPTED — executable RED pending |
| `QA-DEPLOY-003` | Preview/staging resources are separated from production | Environment/project isolation evidence | COMPREHENSION ACCEPTED — executable RED pending |
| `QA-DEPLOY-004` | Secret boundaries prevent production secret exposure | Secret-source/environment mapping without values | COMPREHENSION ACCEPTED — executable RED pending |
| `QA-DEPLOY-006` | Production action remains protected/manual | Protected-environment/approval evidence | COMPREHENSION ACCEPTED — executable RED pending |
| `QA-DEPLOY-007` | Migration execution uses approved protected path | Workflow and command contract evidence | COMPREHENSION ACCEPTED — executable RED pending |
| `QA-DEPLOY-010` | Runtime/deployment configuration is complete and non-placeholder | CI/configuration validation logs | COMPREHENSION ACCEPTED — executable RED pending |
| Applicable QA-CONFIG | Environment and runtime configuration are explicit and valid | Config inventory and validation output | COMPREHENSION ACCEPTED — executable RED pending |
| Applicable QA-DES | Deployment execution follows approved Stage 5a design | Traceability from Stage 5a to workflow/configuration | COMPREHENSION ACCEPTED — executable RED pending |

---

## Evidence Classes Required from W1

1. Exact workflow paths and ownership.
2. Runtime and package/tool version contract.
3. Root `.env.example` variable contract without real secrets.
4. CI, type, lint, test and schema-validation logs.
5. Preview project URL or governed project reference where applicable.
6. Preview/staging/production environment separation evidence.
7. No-production-side-effect evidence for PR CI.
8. Secret-boundary evidence without exposing values.
9. Protected production approval evidence.
10. Dependency and environment ownership evidence.
11. Visible failure/blocking evidence when required resources are unavailable.
12. Tracker/index and wave-evidence linkage.

---

## Prohibited Proof

The following cannot satisfy W1:

- workflow names without repository paths or owner;
- screenshots containing secret values;
- a successful documentation-only gate used as proof of implementation-gate readiness;
- skipped, todo, stub-only, placeholder or trivially passing tests;
- warnings ignored or suppressed;
- preview using production credentials or production data;
- manual assertions without reproducible evidence;
- changing tests to match an implementation shortcut.

---

## Current Result

The W1 test and evidence obligations are mapped and candidate comprehension was accepted in merged PR #1216. Issue #1222 confirmed that executable W1 tests and observed intended-RED evidence are not committed, Supabase develop and Vercel configuration are not independently visible through the current connectors, and the bootstrap control is not operational in the current session.

**Current result: BLOCKING for `integration-builder` appointment pending Issues #1226, #1227 and #1228.**

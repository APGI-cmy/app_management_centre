# Implementation Plan - Stage 8

**Stage**: 8 - Implementation Plan  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: ✅ CS2 Approved with Conditions  
**Issue**: app_management_centre#1199  
**Disposition**: app_management_centre#1201 / merged PR #1202  
**Wave**: amc-stage8-implementation-plan-20260702

---

## 1. Purpose

This Stage 8 artifact converts the approved AMC pre-build pack into a governed plan for later delivery.

It is a planning artifact only. It does not create downstream stage work.

---

## 2. Binding Inputs

Stage 8 imports:

1. `cs2-decision-record-stages-5-5a-6-7.md`.
2. Stage 5 route, action, state, audit, and degraded-mode map.
3. Stage 5a deployment validation matrix.
4. Stage 6 QA-FD and QA-DEPLOY rows.
5. Stage 7 PBFAG blocker rows.
6. First E2E `/alerts` acknowledgement path.
7. Placeholder and stub rejection rule.
8. Production approval gates and secret separation.
9. Supabase migration command freeze.
10. Rollback planning.
11. Runtime health and smoke validation.
12. Dependency readiness and visible degraded-mode behavior.
13. Complete delivery evidence package.
14. Tracker and artifact-index updates.

---

## 3. Stage 5a Deployment Inheritance

Stage 8 explicitly inherits the Stage 5a Deployment Execution Strategy at:

`modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` v1.0

The later delivery wave structure must remain consistent with that strategy. No later wave may silently substitute a different deployment or operational model.

| Deployment surface | Stage 8 wave destination | Execution posture |
|---|---|---|
| `ci.yml` | W1 and W8 | Automated CI evidence required before later delivery can claim completion |
| `deploy-frontend.yml` | W1 and W7 | Preview/staging deployment planning required; production execution remains protected/manual where required by governance |
| `db-migrate.yml` | W7 | Migration command and migration evidence planning required; production database mutation remains protected/manual where required by governance |
| Secret/environment separation | W1 and W7 | PR, preview, staging, and production secrets must remain separated |
| Health/smoke validation | W7 and W8 | Health and smoke evidence required before release readiness may be claimed |
| Rollback/recovery | W7 | Rollback or recovery proof must be planned before release readiness may be claimed |

Stage 9 may not weaken this mapping. Stage 9 must convert it into checklist items only after CS2 accepts Stage 8.

---

## 4. Planned Delivery Waves

| Wave | Scope | Required controls |
|---|---|---|
| W1 | Runtime foundation and environment setup | CI, preview, secret, and environment boundaries |
| W2 | Auth, tenant, authority, and audit baseline | Authority checks, state ownership, audit events |
| W3 | Core AMC routes and material surfaces | Route/action/state/audit/degraded-mode mapping |
| W4 | `/alerts` first E2E path | UI, API, authority, state, audit, realtime, visible result |
| W5 | ARC, approvals, interventions, and workflow surfaces | ARC model, authority, state, audit, evidence |
| W6 | AIMC, AIMCC, KUC, knowledge, Foreman, specialist, and push integrations | Service-token boundaries, dependency readiness, degraded mode |
| W7 | Deployment execution and release controls | Migration command, rollback, health, smoke, evidence |
| W8 | QA-to-Green consolidation | QA-FD, QA-DEPLOY, PBFAG rows, no placeholder proof |

---

## 5. Red-Test Coverage by Wave

Stage 8 requires each later delivery wave to carry matching red-test coverage. W8 consolidates the proof, but W1-W7 must not proceed without their own planned red-test obligations.

| Wave | Required red-test coverage |
|---|---|
| W1 | CI, preview isolation, environment separation, secret boundary, and no production side effect tests |
| W2 | Auth, tenant isolation, authority middleware, RLS/tenant access, and audit baseline tests |
| W3 | Core route availability, visible actions, state mutation, audit event, and degraded-mode tests |
| W4 | First E2E `/alerts` acknowledgement path tests covering UI, API, authority, state, audit, realtime, and visible result |
| W5 | ARC, approvals, interventions, executive workflow, authority, state, and audit tests |
| W6 | AIMC, AIMCC, KUC, knowledge, Foreman, specialist, push integration, service-token, dependency readiness, and degraded-mode tests |
| W7 | Deployment, migration command, rollback, health, smoke, preview/staging, and protected production gate tests |
| W8 | Cross-wave QA-FD, QA-DEPLOY, PBFAG, tracker/index, and evidence-package consolidation tests |

Stage 9 must preserve this per-wave test map when it creates any later checklist.

---

## 6. Evidence Expectations

Later delivery waves must produce evidence for:

- user-visible behavior;
- API behavior;
- state changes;
- audit/provenance events;
- authority checks;
- degraded-mode behavior;
- deployment or preview URL where applicable;
- test logs;
- health and smoke checks;
- rollback or recovery where applicable.

---

## 7. Stage 8 Exit Criteria

Stage 8 was accepted by CS2 with conditions in the decision record merged by PR #1202 after confirming:

1. every CS2 condition is mapped to a delivery wave;
2. the `/alerts` first E2E path is planned;
3. deployment, QA, dependency, and evidence duties are planned;
4. Stage 5a deployment inheritance is explicit;
5. red-test coverage is mapped to every later delivery wave;
6. Stage 9 inputs are clear;
7. later stages remain gated until separately authorized.

---

## 8. Boundary

This artifact does not create builder checklist, IAA pre-brief, builder appointment, source code, build evidence, or build work.

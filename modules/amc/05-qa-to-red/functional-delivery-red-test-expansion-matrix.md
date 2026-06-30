# AMC Stage 6 Functional Delivery RED Test Expansion Matrix

**Stage**: 6 — QA-to-Red expansion matrix  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: Produced for CS2 review  
**Wave**: amc-stage6-qa-to-red-retrofit-20260629  
**Issue**: app_management_centre#1191  
**Authority basis**: PR #1186, PR #1188, PR #1190, Stage 5 architecture map, Stage 5a deployment execution validation matrix  
**Non-scope**: This matrix does not start Stage 7, Stage 8, builder checklist, IAA pre-brief, builder appointment, or implementation work.

---

## 1. Purpose

This matrix extends the existing Stage 6 red-test catalog with the functional-delivery and deployment-execution failure classes introduced by the Stage 1-5a retrofit chain.

It does not implement tests. It defines the mandatory RED conditions that later test implementation must satisfy.

---

## 2. Functional Delivery Test Expansion

| Test ID | Source obligation | Scenario | Expected RED/fail condition | Expected GREEN/pass condition | Severity | Blocker | Evidence type |
|---|---|---|---|---|---|---|---|
| QA-FD-001 | Stage 5 no-dead-CTA control | Every material CTA has a target | CTA exists with no API route, service contract, or explicit read-only declaration | Every CTA maps to a route/service/read-only declaration in the Stage 5 map | HIGH | YES | static-analysis + UI route inventory |
| QA-FD-002 | Stage 5 frontend/backend closure | API exists and is surfaced | API route exists but no visible UI state or journey uses it | API response is bound to a visible state or explicitly classified backend-only with CS2 disposition | HIGH | YES | integration + UI verification |
| QA-FD-003 | Stage 5 state ownership | Consequential action persists or declares projection | Action completes with no state owner/table/projection effect | State mutation/projection boundary is documented and testable | HIGH | YES | integration |
| QA-FD-004 | FR-1900 / TR-1900 audit coverage | Consequential action produces audit/provenance | Action returns success without audit/provenance event | Audit/provenance event is created before success is returned | CRITICAL | YES | integration |
| QA-FD-005 | Authority gate | Reserved/delegated action bypasses server authority | Action side effect occurs before server-side authority approval | Server rejects or blocks side effect until required authority state exists | CRITICAL | YES | integration/security |
| QA-FD-006 | Degraded-mode visibility | Dependency failure hidden from user | Dependency unavailable returns success/no-op or silent blank UI | User-visible degraded/unavailable/stale state appears with source/timestamp where applicable | HIGH | YES | integration + UI |
| QA-FD-007 | Placeholder leakage | Placeholder counted complete | Placeholder/stub CTA or route is counted as complete without CS2 disposition | Placeholder is absent or explicitly registered and excluded from completion | HIGH | YES | static-analysis + artifact review |
| QA-FD-008 | Route/event drift | Stage 2 matrix and TRS/Stage 5 names conflict | Test/code uses non-canonical route/event name where TRS defines another | Canonical route/event is used or CS2 drift disposition exists | HIGH | YES | static-analysis + contract review |
| QA-FD-009 | Omitted material route | Material Stage 5 route absent from QA traceability | `/agent-oversight`, `/maintenance-reports`, `/estate-config`, or other Stage 5 material route lacks QA mapping | Every material Stage 5 route appears in QA traceability or has CS2 disposition | HIGH | YES | traceability review |
| QA-FD-010 | First E2E path | `/alerts` acknowledgement journey incomplete | `/alerts` acknowledgement cannot be proven from UI to API to state to audit to visible result | Full `/alerts` acknowledgement evidence path passes end-to-end | CRITICAL | YES | e2e + audit proof |
| QA-FD-011 | AIMC boundary | AI action bypasses AIMC | Any AMC route calls model provider directly or uses non-AIMC action path | All AI actions route through AIMC and expose AIMC degraded state when unavailable | CRITICAL | YES | static-analysis + integration |
| QA-FD-012 | KUC/AIMCC boundary | Upload bypasses KUC or uses AIMCC ingestion directly | Upload submission posts to AIMCC ingestion or other non-KUC target | Upload submission posts only to KUC and surfaces KUC failure/rejection | CRITICAL | YES | static-analysis + integration |
| QA-FD-013 | Knowledge provenance | Knowledge shown without provenance | Knowledge result displayed without source/provenance/stale marker | Knowledge display includes provenance and stale/TTL marker where applicable | HIGH | YES | integration + UI |
| QA-FD-014 | ARC canonical model | ARC trigger model reintroduced | `arc_triggers`, `/api/arc/triggers`, or `ARC_TRIGGER_*` appears as canonical | Canonical `arc_classifications`, `/api/arc/{id}` action family, and `ARC_ITEM_*` events are used | CRITICAL | YES | static-analysis + contract review |
| QA-FD-015 | Quota override lifecycle | Temporary override lacks lifecycle event | Override request has no expiry or no activation/expiry event path | `adjustment_type: temporary_override`, expiry, activation, and expiry lifecycle events are testable | HIGH | YES | integration + audit proof |

---

## 3. Deployment Execution Test Expansion

| Test ID | Source obligation | Scenario | Expected RED/fail condition | Expected GREEN/pass condition | Severity | Blocker | Evidence type |
|---|---|---|---|---|---|---|---|
| QA-DEPLOY-001 | Stage 5a workflow ownership | Required workflow names missing | `ci.yml`, `deploy-frontend.yml`, or `db-migrate.yml` missing or renamed without CS2 disposition | Required workflow family exists or CS2-approved amended name is recorded | HIGH | YES | static workflow review |
| QA-DEPLOY-002 | Protected production environment | Production job ungated | Production deploy or migration job lacks protected `production` environment | Production job requires protected environment approval | CRITICAL | YES | workflow review |
| QA-DEPLOY-003 | Production secret isolation | PR/staging can access production secrets | PR or staging job exposes production credentials | Production secrets scoped only to production environment | CRITICAL | YES | workflow/env review |
| QA-DEPLOY-004 | Migration command freeze | Migration uses non-approved command | Workflow uses command other than `supabase db push --project-ref $SUPABASE_PROJECT_REF` without CS2 disposition | Approved command is used and no `supabase link` drift is present | HIGH | YES | workflow review |
| QA-DEPLOY-005 | Rollback evidence | Migration lacks rollback path | DB migration change has no rollback/revert/restore note | Rollback/revert/restore evidence is recorded for affected migration | HIGH | YES | artifact review |
| QA-DEPLOY-006 | Environment template | Runtime variable missing from `.env.example` | Required variable used by code/workflow is absent from `.env.example` | Required variable is listed with placeholder, purpose, and no secret value | HIGH | YES | static-analysis |
| QA-DEPLOY-007 | Runtime health smoke | No health/smoke validation | Deployment evidence lacks app/API/Supabase/realtime health check | Health/smoke result is captured or explicitly not applicable with reason | HIGH | YES | deployment evidence |
| QA-DEPLOY-008 | Dependency readiness | External dependency readiness hidden | AIMC/AIMCC/KUC/knowledge/Foreman/specialist/push dependency unavailable with no visible degraded result | Dependency readiness or degraded-mode evidence is captured | HIGH | YES | integration + evidence |
| QA-DEPLOY-009 | Deployment evidence package | Feature closure lacks evidence bundle | Feature marked complete without deployed URL/API/state/audit/evidence record | Evidence package contains required deployment, API, state, audit, env, dependency, and visual/log proof | HIGH | YES | evidence review |
| QA-DEPLOY-010 | No placeholder evidence | Placeholder counted as deployment proof | Screenshot/log shows placeholder and is accepted as complete | Placeholder is rejected or recorded with CS2 disposition and excluded from completion | HIGH | YES | evidence review |

---

## 4. Existing Test Reuse / Expansion Rule

| Existing family | Reuse posture | Required expansion |
|---|---|---|
| QA-ARCH | Reuse for boundary tests | Add QA-FD-001 to QA-FD-015 for route/action/journey closure |
| QA-AUDIT | Reuse for audit table behavior | Add QA-FD-004 and QA-FD-010 for consequential action and full journey proof |
| QA-AUTH | Reuse for authority middleware | Add QA-FD-005 for side-effect-before-authority prevention |
| QA-DEGRADE | Reuse for dependency behavior | Add QA-FD-006 and QA-DEPLOY-008 for user-visible degraded/dependency readiness proof |
| QA-CONFIG | Reuse for config validation | Add QA-DEPLOY-006 for `.env.example` coverage drift |
| QA-DES | Reuse for DES field coverage | Add QA-DEPLOY-001 to QA-DEPLOY-010 for deployment execution controls |

---

## 5. Stage 7 Import Requirement

Stage 7 must treat this matrix as a Stage 6 disposition input. Any missing `QA-FD-*` or `QA-DEPLOY-*` row is a Stage 7 blocker unless CS2 explicitly disposes it.

---

## 6. Verdict

This matrix provides the missing RED expansion layer required for Stage 6 to test the fully functional delivery and deployment-execution controls introduced by PR #1186, PR #1188, and PR #1190.

It is not a test implementation and does not authorize build work.

# Architecture and DES to QA Traceability — Stage 6

**Stage**: 6 — QA-to-Red
**Module**: App Management Centre (AMC)
**Version**: 1.0
**Status**: 🟡 Produced — Approval Pending (CS2)
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: app_management_centre#1141
**Governing Delivery Issue**: app_management_centre#1141
**Wave**: amc-stage6-qa-to-red-20260427
**Date**: 2026-04-27
**Upstream Sources**:
- Stage 5 Architecture: `modules/amc/04-architecture/architecture-specification.md` v1.0
- Stage 5a DES: `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` v1.0
- Stage 5a Surface Table: `modules/amc/05a-deployment-execution-strategy/deployment-surface-ownership-table.md` v1.0
- Stage 5a Runner Constraints: `modules/amc/05a-deployment-execution-strategy/runner-and-environment-constraints.md` v1.0
**Canonical Location**: `modules/amc/05-qa-to-red/architecture-and-des-to-qa-traceability.md`

---

> **STAGE ENTRY CONDITION NOTICE**
> Stage 5 and Stage 5a are produced approval-pending. This traceability artifact is conditional on
> Stage 5 and Stage 5a receiving CS2 approval before Stage 7 proceeds. Authorized for production
> now per CS2 issue #1141.

---

## Purpose

This traceability matrix demonstrates that:
1. Every major Stage 5 Architecture commitment is covered by at least one Stage 6 red test
2. Every Stage 5a DES field (DES-001 through DES-008) is covered by at least one Stage 6 red test
3. No critical Architecture or DES family has been silently omitted
4. Intentional deferrals beyond Stage 6 are explicitly documented

---

## Table of Contents

1. [Stage 5 Architecture to Stage 6 QA Traceability](#1-stage-5-architecture-to-stage-6-qa-traceability)
2. [Stage 5a DES to Stage 6 QA Traceability](#2-stage-5a-des-to-stage-6-qa-traceability)
3. [Stage 5a Sub-Artifact Traceability](#3-stage-5a-sub-artifact-traceability)
4. [Omission Register — Explicitly Deferred Items](#4-omission-register--explicitly-deferred-items)
5. [Coverage Completeness Verdict](#5-coverage-completeness-verdict)

---

## 1. Stage 5 Architecture to Stage 6 QA Traceability

### 1.1 Coverage Summary

| Architecture Domain | Architecture Section | Stage 6 Coverage Family | Red Test IDs | Covered? |
|---|---|---|---|---|
| Cross-system boundary preservation | §2, §5.6 | §7.1 (Cross-System Boundary Preservation) | QA-ARCH-001 to QA-ARCH-006 | ✅ Covered |
| ARC first-class domain | §4.1 | §7.2 (ARC Domain Explicitness) | QA-ARC-001 to QA-ARC-008 | ✅ Covered |
| Dynamic quota management console | §4.2 | §7.3 (Quota Management Console) | QA-QUOTA-001 to QA-QUOTA-008 | ✅ Covered |
| State ownership and consistency | §6.1, §3.4 | §7.4 (State Ownership and Consistency) | QA-STATE-001 to QA-STATE-005 | ✅ Covered |
| Audit and provenance | §4.4, §6.3 | §7.5 (Audit/Provenance Expectations) | QA-AUDIT-001 to QA-AUDIT-006 | ✅ Covered |
| Trust and authority boundaries | §7, §3.3 | §7.6 (Trust/Authority Boundary) | QA-AUTH-001 to QA-AUTH-006 | ✅ Covered |
| Degraded-mode and dependency-loss | §6.4, §5.1–5.5 | §7.7 (Degraded-Mode Behavior) | QA-DEGRADE-001 to QA-DEGRADE-008 | ✅ Covered |
| Alert delivery and escalation | §4.3 | §7.8 (Alert Delivery and Escalation) | QA-ALERT-001 to QA-ALERT-005 | ✅ Covered |
| Session restore and cross-device | §6.2 | §7.9 (Session Restore) | QA-SESSION-001 to QA-SESSION-003 | ✅ Covered |
| Real-time architecture | §3.5 | §7.10 (Real-Time Architecture) | QA-RT-001 to QA-RT-004 | ✅ Covered |
| Configuration validation at startup | §3.3 | §7.11 (Configuration Validation) | QA-CONFIG-001 to QA-CONFIG-003 | ✅ Covered |
| Background scheduler | §3.6 | §7.12 (Background Scheduler) | QA-SCHED-001 to QA-SCHED-003 | ✅ Covered |

**Total Architecture domains: 12. Covered: 12. Not covered: 0.**

### 1.2 Detailed Architecture Traceability

#### Cross-System Boundary Preservation (Architecture §2, §5.6)

| Architecture Commitment | Source | Stage 6 Test IDs | Notes |
|---|---|---|---|
| AI SDK prohibition — no model provider SDK in `package.json` | §2 TR-BOUNDARY-001 | QA-ARCH-001 | Enforced at CI dependency scan gate |
| No direct AIMCC ingestion endpoint calls from AMC | §2 TR-BOUNDARY-002 | QA-ARCH-002 | All submissions via KUC API only |
| No AMC table storing canonical knowledge content | §2 TR-BOUNDARY-003 | QA-ARCH-003 | No knowledge content columns in AMC tables |
| All outbound calls include `Authorization: Bearer` | §2 TR-BOUNDARY-004 | QA-ARCH-004 | Service token on every outbound call |
| `BOUNDARY_BYPASS_ATTEMPTED` audit event on bypass detection | §5.6 | QA-ARCH-005 | Runtime bypass detection |
| Knowledge uploads POST to KUC API only | §5.3 | QA-ARCH-006 | Not to AIMCC ingestion path |

#### ARC Domain Architecture (Architecture §4.1)

| Architecture Commitment | Source | Stage 6 Test IDs | Notes |
|---|---|---|---|
| `arc_classifications` is a distinct table | §4.1 | QA-ARC-001 | Not a view or derived table |
| `/api/arc/` namespace separate from `/api/alerts/` | §4.1 | QA-ARC-002 | Dedicated API namespace |
| `/arc` frontend route accessible from navigation | §4.1 | QA-ARC-003 | Dedicated route |
| `amc_arc_{user_id}` Realtime channel subscribed separately | §4.1 | QA-ARC-004 | Dedicated channel |
| ARC state transitions require correct POST endpoints | §4.1 | QA-ARC-005 | State machine: open → in_resolution → resolved |
| Boundary-bypass ARC item requires Johan Ras human actor | §4.1 | QA-ARC-006 | HTTP 403 on unauthorized actor |
| ARC staleness detection via `amc-arc-staleness-scheduler` | §4.1 | QA-ARC-007 | Not inline alert code |
| Audit events written on each ARC state transition | §4.1 | QA-ARC-008 | `ARC_ITEM_CLASSIFIED`, `ARC_ITEM_STATE_CHANGED`, `ARC_ITEM_RESOLVED` |

#### Dynamic Upload Quota Management (Architecture §4.2)

| Architecture Commitment | Source | Stage 6 Test IDs | Notes |
|---|---|---|---|
| `POST /api/aimcc/quota/request-adjustment` is sole quota initiation path | §4.2 | QA-QUOTA-001 | No other path |
| Quota adjustment requires `reserved_matter` approval record | §4.2 | QA-QUOTA-002 | No quota change without completed approval |
| Quota change without approval record → HTTP 422 | §4.2 | QA-QUOTA-003 | Server-side enforcement |
| AIMCC notified via `POST {AIMCC_API_BASE_URL}/governance/decision` only | §4.2 | QA-QUOTA-004 | No other AIMCC notification path |
| Temporary override requires `override_expiry_at` field | §4.2 | QA-QUOTA-005 | Missing expiry rejected |
| Quota threshold transitions generate alerts and audit events | §4.2 | QA-QUOTA-006 | `ok → warning → critical` state machine |
| Quota thresholds read from environment variables | §4.2 | QA-QUOTA-007 | Not hardcoded |
| Quota history reconstructable from `audit_events` | §4.2 | QA-QUOTA-008 | No separate quota history table required |

#### State Ownership and Consistency (Architecture §6.1, §3.4)

| Architecture Commitment | Source | Stage 6 Test IDs | Notes |
|---|---|---|---|
| Every AMC-owned table has `organisation_id` in RLS | §3.4, §6.1 | QA-STATE-001 | Tenant isolation enforced |
| No external service directly writes AMC-owned tables | §6.1 | QA-STATE-002 | All external mutations via validated callbacks |
| State mutations propagate via Realtime within 2 seconds | §6.1 | QA-STATE-003 | `amc_executive_state_{user_id}` channel |
| Action + audit event in single database transaction | §6.1 | QA-STATE-004 | If audit fails, action rolled back |
| Approval idempotency: already-processed → HTTP 409 | §6.1 | QA-STATE-005 | No double-processing |

#### Audit and Provenance (Architecture §4.4, §6.3)

| Architecture Commitment | Source | Stage 6 Test IDs | Notes |
|---|---|---|---|
| `audit_events` table INSERT-only via RLS | §4.4, §6.3 | QA-AUDIT-001 | UPDATE/DELETE return permission denied |
| Every consequential action produces audit event before success | §4.4 | QA-AUDIT-002 | Audit-first atomicity |
| Audit event INSERT failure → action rolled back | §4.4 | QA-AUDIT-003 | Atomicity contract |
| `actor` and `actor_type` from JWT/service token only | §4.4 | QA-AUDIT-004 | Not from caller-supplied data |
| Knowledge display includes provenance metadata | §6.3 | QA-AUDIT-005 | No anonymous knowledge display |
| Missing provenance → audit event generated | §6.3 | QA-AUDIT-006 | Provenance gap detection |

#### Trust and Authority Boundaries (Architecture §7, §3.3)

| Architecture Commitment | Source | Stage 6 Test IDs | Notes |
|---|---|---|---|
| API routes enforce Auth → Actor → Authority-Domain sequence | §3.3, §7 | QA-AUTH-001 | Server-side middleware chain |
| `reserved_matter`: non-human or non-Johan actor → HTTP 403 | §7.2 | QA-AUTH-002 | Server-side enforcement |
| `delegated`: out-of-scope `ai_executive` → HTTP 403 | §7.2 | QA-AUTH-003 | Via `authority_domain_config` |
| Authority enforcement is server-side (not client-side-only) | §7 | QA-AUTH-004 | Direct API call bypass is prevented |
| Inbound callbacks require valid service token | §7.1 | QA-AUTH-005 | Missing/invalid → HTTP 401 |
| Service token identity cannot be elevated by caller | §7.1 | QA-AUTH-006 | No token escalation path |

#### Degraded-Mode Behavior (Architecture §6.4, §5.1–5.5)

| Architecture Commitment | Source | Stage 6 Test IDs | Notes |
|---|---|---|---|
| AIMC unavailable → HTTP 503 on all AIMC endpoints | §5.1, §6.4 | QA-DEGRADE-001 | No fallback AI call path |
| Maturion Proactive Panel renders exact required string | §5.1 | QA-DEGRADE-002 | Exact string match required |
| AIMCC unavailable → stale cache with `stale: true, stale_since` | §5.2, §6.4 | QA-DEGRADE-003 | Not served as current data |
| AIMCC unavailable → governance actions remain `pending` | §5.2 | QA-DEGRADE-004 | Not auto-processed |
| Knowledge system unavailable → HTTP 503 + unavailable indicator | §5.4, §6.4 | QA-DEGRADE-005 | All knowledge surfaces show indicator |
| Foreman unavailable → HTTP 503 + `{ status: "unavailable", last_known_at }` | §5.5, §6.4 | QA-DEGRADE-006 | Explicit response structure |
| Every degraded mode entry writes `system_health_events` row | §6.4 | QA-DEGRADE-007 | And dependency-specific audit event |
| Recovery resets degraded state via health poll | §6.5 | QA-DEGRADE-008 | Not via manual reset endpoint |

#### Alert Delivery and Escalation (Architecture §4.3)

| Architecture Commitment | Source | Stage 6 Test IDs | Notes |
|---|---|---|---|
| Critical/High/Medium cannot be dismissed without `dismiss_reason` | §4.3 | QA-ALERT-001 | HTTP 422 on server-side enforcement |
| Alert escalation is sequential (L1 before L2, no skip) | §4.3 | QA-ALERT-002 | Level-skipping prohibited |
| Alert INSERT retry with exponential back-off | §4.3 | QA-ALERT-003 | 3 retries then fallback sink |
| Push failure does not block alert creation | §4.3 | QA-ALERT-004 | Failure recorded, not blocking |
| SLA breach writes `ALERT_DELIVERY_DELAYED` audit event | §4.3 | QA-ALERT-005 | Event-driven SLA monitoring |

#### Session Restore and Cross-Device (Architecture §6.2)

| Architecture Commitment | Source | Stage 6 Test IDs | Notes |
|---|---|---|---|
| Session restore fetches 5 defined API endpoints | §6.2 | QA-SESSION-001 | All listed endpoints required |
| Failed session-restore fetch → explicit error indicator | §6.2 | QA-SESSION-002 | No silent fallback |
| All critical state server-side (not client-local-only) | §6.2 | QA-SESSION-003 | Server-side persistence |

#### Real-Time Architecture (Architecture §3.5)

| Architecture Commitment | Source | Stage 6 Test IDs | Notes |
|---|---|---|---|
| Alert changes broadcast within ≤2s of INSERT commit | §3.5 | QA-RT-001 | SLA requirement |
| ARC updates broadcast within ≤2s of referenced alert ack | §3.5 | QA-RT-002 | SLA requirement |
| Subscriptions created on mount, cleaned up on unmount | §3.5 | QA-RT-003 | No subscription leak |
| Component state updates immediately on Realtime event | §3.5 | QA-RT-004 | No contradictory stale state |

#### Configuration Validation at Startup (Architecture §3.3)

| Architecture Commitment | Source | Stage 6 Test IDs | Notes |
|---|---|---|---|
| Startup fails if any required env var absent | §3.3, TR-1505 | QA-CONFIG-001 | Explicit startup error |
| Error names the missing variable explicitly | §3.3 | QA-CONFIG-002 | Not a generic error |
| All 12 required env vars cause startup failure if absent | §3.3 | QA-CONFIG-003 | Full required list |

#### Background Scheduler Architecture (Architecture §3.6)

| Architecture Commitment | Source | Stage 6 Test IDs | Notes |
|---|---|---|---|
| Scheduled jobs implemented as Edge Functions (not inline API code) | §3.6 | QA-SCHED-001 | Supabase Edge Functions |
| Scheduler failure generates Critical alert with function name | §3.6 | QA-SCHED-002 | `source_system: "amc_scheduler"` |
| All thresholds and timeouts read from env vars | §3.6 | QA-SCHED-003 | No hardcoded values |

---

## 2. Stage 5a DES to Stage 6 QA Traceability

### 2.1 DES Fields Coverage Summary

| DES Field | DES Reference | Stage 6 Coverage Family | Red Test IDs | Covered? |
|---|---|---|---|---|
| DES-001 — Workflow Surface Ownership | §3.1 | §8.1 (Surface Ownership Boundaries) | QA-DES001-001 to QA-DES001-005 | ✅ Covered |
| DES-002 — GitHub-Hosted Runner Authorization | §3.2 | §8.2 (Runner Authorization Boundaries) | QA-DES002-001 to QA-DES002-003 | ✅ Covered |
| DES-003 — Self-Hosted Runner Prohibition | §3.3 | §8.2 (Runner Authorization Boundaries) | QA-DES003-001 to QA-DES003-002 | ✅ Covered |
| DES-004 — Migration Execution Path | §3.4 | §8.3 (Migration Execution Path) | QA-DES004-001 to QA-DES004-008 | ✅ Covered |
| DES-005 — CI/Preview/Production Execution Boundaries | §3.5 | §8.4 (Trigger Boundaries) | QA-DES005-001 to QA-DES005-005 | ✅ Covered |
| DES-006 — Safety Classification | §3.6 | §8.5 (Frontend Workflow DB Mutation Prohibition) | QA-DES006-001 to QA-DES006-005 | ✅ Covered |
| DES-007 — Manual/Protected Approval Boundaries | §3.7 | §8.6 (Protected Environment Approval) | QA-DES007-001 to QA-DES007-005 | ✅ Covered |
| DES-008 — Environment/Network Assumption Validation | §3.8 | §8.7 (Pre-Flight Fail-Safe Behavior) | QA-DES008-001 to QA-DES008-007 | ✅ Covered |

**Total DES fields: 8. Covered: 8. Not covered: 0.**

### 2.2 Detailed DES Traceability

#### DES-001 — Workflow Surface Ownership

| DES Commitment | DES Reference | Stage 6 Test IDs | Notes |
|---|---|---|---|
| `deploy-frontend.yml` owns frontend deploy; no other workflow deploys frontend | §3.1 | QA-DES001-001 | Single owner per surface |
| `db-migrate.yml` owns DB migration; no other workflow migrates DB | §3.1 | QA-DES001-002 | Single owner per surface |
| `ci.yml` owns schema verification on PRs | §3.1 | QA-DES001-003 | Read-only verification |
| Live operational validation is manual (no automated workflow) | §3.1 | QA-DES001-004 | Manual process only |
| No surface owned by more than one workflow | §3.1 (Ownership Invariant) | QA-DES001-005 | Ownership invariant enforcement |

#### DES-002/DES-003 — Runner Authorization

| DES Commitment | DES Reference | Stage 6 Test IDs | Notes |
|---|---|---|---|
| `ci.yml` uses `runs-on: ubuntu-latest` | §3.2, §3.3 | QA-DES002-001 | GitHub-hosted only |
| `deploy-frontend.yml` uses `runs-on: ubuntu-latest` | §3.2, §3.3 | QA-DES002-002 | GitHub-hosted only |
| `db-migrate.yml` uses `runs-on: ubuntu-latest` | §3.2, §3.3 | QA-DES002-003 | GitHub-hosted only |
| No self-hosted runner label in any workflow file | §3.3 | QA-DES003-001 | Explicit prohibition |
| Introducing self-hosted runner detected and fails CI | §3.3 | QA-DES003-002 | Configuration check |

#### DES-004 — Migration Execution Path

| DES Commitment | DES Reference | Stage 6 Test IDs | Notes |
|---|---|---|---|
| `db-migrate.yml` uses `supabase db push --project-ref $SUPABASE_PROJECT_REF` | §3.4 | QA-DES004-001 | Exact approved command |
| No `psql` direct connection in any workflow | §3.4 | QA-DES004-002 | Prohibited mechanism |
| No manual SQL execution step in `db-migrate.yml` | §3.4 | QA-DES004-003 | Prohibited mechanism |
| No local developer machine migration script path | §3.4 | QA-DES004-004 | Prohibited mechanism |
| `SUPABASE_ACCESS_TOKEN` from env var; not hardcoded | §3.4 | QA-DES004-005 | Secret hygiene |
| `SUPABASE_PROJECT_REF` from env secret; not hardcoded | §3.4 | QA-DES004-006 | Env scoping |
| `supabase db push --linked` flag NOT used | §3.4 | QA-DES004-007 | Stateful link prohibited |
| Migrations live under `supabase/migrations/` only | §3.4 | QA-DES004-008 | Standard path |

#### DES-005 — Execution Boundaries

| DES Commitment | DES Reference | Stage 6 Test IDs | Notes |
|---|---|---|---|
| `ci.yml` triggered on `pull_request` | §3.5 | QA-DES005-001 | CI gate on PRs |
| `deploy-frontend.yml` NOT triggered on `pull_request` | §3.5 | QA-DES005-002 | No PR deployment |
| `db-migrate.yml` uses `workflow_dispatch` only (no auto-trigger) | §3.5 | QA-DES005-003 | Manual-only trigger |
| DB migration does NOT run on PR under any workflow | §3.5 | QA-DES005-004 | Trigger boundary |
| `deploy-frontend.yml` depends on `ci.yml` success | §3.5 | QA-DES005-005 | Workflow dependency |

#### DES-006 — Safety Classification / Frontend DB Mutation Prohibition

| DES Commitment | DES Reference | Stage 6 Test IDs | Notes |
|---|---|---|---|
| `deploy-frontend.yml` contains NO `supabase db push` step | §3.6 | QA-DES006-001 | Mutation prohibition |
| `deploy-frontend.yml` contains NO `psql` step | §3.6 | QA-DES006-002 | Mutation prohibition |
| `deploy-frontend.yml` does NOT reference `SUPABASE_SERVICE_ROLE_KEY` | §3.6 | QA-DES006-003 | Production DB write prohibition |
| `ci.yml` schema verification is read-only (no DB mutation) | §3.6 | QA-DES006-004 | CI-safe classification |
| PR adding DB mutation to `deploy-frontend.yml` fails CI and QP | §3.6 | QA-DES006-005 | Anti-drift enforcement |

#### DES-007 — Protected Environment Approval

| DES Commitment | DES Reference | Stage 6 Test IDs | Notes |
|---|---|---|---|
| `deploy-frontend.yml` production job references `environment: production` | §3.7 | QA-DES007-001 | Protected env gate |
| `db-migrate.yml` production job references `environment: production` | §3.7 | QA-DES007-002 | Protected env gate |
| Removing `environment: production` is detected and fails | §3.7 | QA-DES007-003 | Anti-drift gate |
| No un-gated automated production deployment occurs | §3.7 | QA-DES007-004 | Gate invariant |
| No rollback of production environment without human gate | §3.7 | QA-DES007-005 | Automation prohibition |

#### DES-008 — Environment / Network Pre-Flight Fail-Safe

| DES Commitment | DES Reference | Stage 6 Test IDs | Notes |
|---|---|---|---|
| Startup: missing `NEXT_PUBLIC_SUPABASE_URL` → explicit error | §3.8 | QA-DES008-001 | Names the missing variable |
| Startup: missing `AIMC_API_BASE_URL` → explicit error | §3.8 | QA-DES008-002 | Names the missing variable |
| `db-migrate.yml`: missing `SUPABASE_ACCESS_TOKEN` → abort immediately | §3.8 | QA-DES008-003 | No DB connection attempted |
| `db-migrate.yml`: missing `SUPABASE_PROJECT_REF` → abort immediately | §3.8 | QA-DES008-004 | No DB connection attempted |
| `deploy-frontend.yml`: missing `VERCEL_TOKEN` → abort immediately | §3.8 | QA-DES008-005 | No deploy attempted |
| No silent-continue past any failed pre-flight check | §3.8 | QA-DES008-006 | "Fail loudly, fail early" |
| Project ref mismatch → migration aborts | §3.8 | QA-DES008-007 | Cross-environment contamination prevention |

---

## 3. Stage 5a Sub-Artifact Traceability

### 3.1 Deployment Surface Ownership Table (`deployment-surface-ownership-table.md`)

The deployment surface ownership table defines 5 surfaces (SURF-001 through SURF-005). Each surface maps to DES-001 test coverage:

| Surface ID | Surface Name | Owning Workflow | Stage 6 Test Reference |
|---|---|---|---|
| SURF-001 | Frontend deploy | `deploy-frontend.yml` | QA-DES001-001 |
| SURF-002 | Backend/API routes deploy | `deploy-frontend.yml` (unified) | QA-DES001-001 |
| SURF-003 | DB migration | `db-migrate.yml` | QA-DES001-002 |
| SURF-004 | Schema verification | `ci.yml` | QA-DES001-003 |
| SURF-005 | Live operational validation | Manual process | QA-DES001-004 |

**No ownership gap**: All 5 surfaces are accounted for. QA-DES001-005 tests the ownership invariant.

### 3.2 Runner and Environment Constraints (`runner-and-environment-constraints.md`)

| Constraint Family | Constraint | Stage 6 Test Reference |
|---|---|---|
| Runner type for all CI gate stages | `ubuntu-latest` (GitHub-hosted) | QA-DES002-001 |
| Runner type for preview deploy (PR) | `ubuntu-latest` (GitHub-hosted) | QA-DES002-002 |
| Runner type for frontend + API routes production deploy | `ubuntu-latest` (GitHub-hosted) | QA-DES002-002 |
| Runner type for DB migration (staging) | `ubuntu-latest` (GitHub-hosted) | QA-DES002-003 |
| Runner type for DB migration (production) | `ubuntu-latest` (GitHub-hosted) | QA-DES002-003 |
| Self-hosted runner prohibition | No self-hosted runner | QA-DES003-001, QA-DES003-002 |
| Protected environment (`production`) configuration | Required for production steps | QA-DES007-001, QA-DES007-002 |
| Supabase CLI version pinned | Pre-flight check in `db-migrate.yml` | QA-DES008-003 (covered under pre-flight fail-safe) |

---

## 4. Omission Register — Explicitly Deferred Items

The following items are intentionally deferred beyond Stage 6 and are NOT omissions:

| Deferred Item | Reason for Deferral | Stage Where Addressed |
|---|---|---|
| Column-level DDL tests | Dependency on schema-builder implementation | Stage 12 (schema-builder qa) |
| React component tree rendering tests | Dependency on ui-builder component implementation | Stage 12 (ui-builder qa) |
| Full CI workflow YAML implementation tests | Dependency on actual workflow file production | Stage 12 (api-builder / integration-builder) |
| Load testing and performance benchmarking | Outside Stage 6 scope; operational testing | Post-build operational testing |
| End-to-end user journey tests | Dependency on full stack implementation | Stage 12 (qa-builder E2E suite) |
| Supabase Edge Function scheduling intervals (cadence accuracy) | Dependency on Edge Function implementation | Stage 12 (qa-builder integration tests) |
| Push notification device registration behavior | Dependency on push notification subsystem implementation | Stage 12 (qa-builder integration tests) |
| Conversation continuity multi-device behavior | Dependency on full Realtime implementation | Stage 12 (qa-builder integration tests) |

**Critical items NOT deferred** (all represented in Stage 6 red coverage):
- All 4 TR-BOUNDARY invariants (§2) — covered in QA-ARCH-001 to QA-ARCH-006
- All 8 DES fields (DES-001 through DES-008) — covered in QA-DES001 through QA-DES008 families
- All CRITICAL audit/authority/state ownership commitments — covered in QA-AUDIT, QA-AUTH, QA-STATE families
- All deployment trigger and runner prohibition invariants — covered in DES families
- All literal-operability workflow defect patterns — covered in QA-LITOP family (see `red-test-catalog.md`)

---

## 5. Coverage Completeness Verdict

### 5.1 Stage 5 Architecture Coverage

| Domain | Coverage | Finding |
|---|---|---|
| Cross-System Boundaries (§2) | ✅ COVERED — QA-ARCH-001 to QA-ARCH-006 | All 4 TR-BOUNDARY invariants plus 2 additional boundary tests |
| ARC Domain (§4.1) | ✅ COVERED — QA-ARC-001 to QA-ARC-008 | 8 tests covering all ARC structural and behavioral commitments |
| Quota Management Console (§4.2) | ✅ COVERED — QA-QUOTA-001 to QA-QUOTA-008 | All quota management architectural rules |
| State Ownership & Consistency (§6.1, §3.4) | ✅ COVERED — QA-STATE-001 to QA-STATE-005 | Tenant isolation, Realtime broadcast, transaction atomicity, idempotency |
| Audit & Provenance (§4.4, §6.3) | ✅ COVERED — QA-AUDIT-001 to QA-AUDIT-006 | Append-only, atomicity, actor identity, provenance |
| Trust & Authority Boundaries (§7, §3.3) | ✅ COVERED — QA-AUTH-001 to QA-AUTH-006 | Middleware chain, reserved_matter, delegated, service token validation |
| Degraded-Mode & Recovery (§6.4, §5.1–5.5) | ✅ COVERED — QA-DEGRADE-001 to QA-DEGRADE-008 | All 4 dependency degraded modes + recovery |
| Alert Delivery & Escalation (§4.3) | ✅ COVERED — QA-ALERT-001 to QA-ALERT-005 | Dismissal enforcement, escalation sequence, retry, push failure, SLA monitoring |
| Session Restore & Cross-Device (§6.2) | ✅ COVERED — QA-SESSION-001 to QA-SESSION-003 | All 5 session-restore endpoints, error handling, server-side state |
| Real-Time Architecture (§3.5) | ✅ COVERED — QA-RT-001 to QA-RT-004 | SLA, subscription lifecycle, component state update |
| Configuration Validation (§3.3) | ✅ COVERED — QA-CONFIG-001 to QA-CONFIG-003 | Startup failure, variable naming, full list |
| Background Scheduler (§3.6) | ✅ COVERED — QA-SCHED-001 to QA-SCHED-003 | Edge Functions, failure alerts, env var config |

**Stage 5 Architecture coverage: 12/12 domains covered. Zero silently omitted.**

### 5.2 Stage 5a DES Coverage

| DES Field | Coverage | Finding |
|---|---|---|
| DES-001 (Surface Ownership) | ✅ COVERED — QA-DES001-001 to QA-DES001-005 | All 5 surfaces traced |
| DES-002 (GitHub-Hosted Runner Authorization) | ✅ COVERED — QA-DES002-001 to QA-DES002-003 | All 3 workflows covered |
| DES-003 (Self-Hosted Runner Prohibition) | ✅ COVERED — QA-DES003-001 to QA-DES003-002 | Prohibition and detection |
| DES-004 (Migration Execution Path) | ✅ COVERED — QA-DES004-001 to QA-DES004-008 | All 8 migration constraints |
| DES-005 (Execution Boundaries) | ✅ COVERED — QA-DES005-001 to QA-DES005-005 | All trigger boundary rules |
| DES-006 (Safety Classification) | ✅ COVERED — QA-DES006-001 to QA-DES006-005 | Frontend mutation prohibition |
| DES-007 (Protected Approval Boundaries) | ✅ COVERED — QA-DES007-001 to QA-DES007-005 | Protected env gate for both production workflows |
| DES-008 (Environment/Network Validation) | ✅ COVERED — QA-DES008-001 to QA-DES008-007 | All pre-flight checks |

**Stage 5a DES coverage: 8/8 fields covered. Zero silently omitted.**

### 5.3 Overall Verdict

**COVERAGE COMPLETE**: All Stage 5 Architecture domains and all Stage 5a DES fields are covered by Stage 6 red test cases. No critical family is silently omitted. Intentional deferrals are explicitly documented in Section 4.

This traceability matrix meets the Stage 7 PBFAG verification requirement that "no critical Architecture or DES family was silently omitted" per the issue #1141 acceptance criteria.

---

*AMC Architecture and DES to QA Traceability v1.0 — 2026-04-27 — governing delivery issue: app_management_centre#1141 — CS2 authorization: app_management_centre#1141*

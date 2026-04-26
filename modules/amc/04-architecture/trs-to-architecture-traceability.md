# TRS to Architecture Traceability — Stage 5

**Stage**: 5 — Architecture Traceability Artifact
**Module**: App Management Centre (AMC)
**Version**: 1.0
**Status**: 🟡 Produced — Approval Pending (CS2)
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: app_management_centre#1131
**Governing Issue**: app_management_centre#1131
**Wave**: amc-stage5-architecture-20260426
**Date**: 2026-04-26
**TRS Source**: `modules/amc/03-trs/technical-requirements-specification.md` v1.1 (treated as approved per #1131)
**Architecture Target**: `modules/amc/04-architecture/architecture-specification.md` v1.0
**Canonical Location**: `modules/amc/04-architecture/trs-to-architecture-traceability.md`

---

> **PURPOSE STATEMENT**
> This document demonstrates that every approved Stage 4 TRS requirement family is architecturally realized in Stage 5 Architecture, and that no approved Stage 4 requirement family was silently dropped. It shows where TRS requirements are resolved in the architecture and what is deferred onward to Stage 6 QA-to-Red rather than resolved in Stage 5. This artifact supports CS2 approval verification and downstream Stage 6 QA-to-Red derivation.

---

## Table of Contents

1. [TRS Requirement Family Coverage Matrix](#1-trs-requirement-family-coverage-matrix)
2. [Individual TRS Family Traceability](#2-individual-trs-family-traceability)
3. [Stage 5 Deferred Items Register](#3-stage-5-deferred-items-register)
4. [TRS Deferred-to-Stage-5 Resolution Status](#4-trs-deferred-to-stage-5-resolution-status)
5. [Cross-System Boundary Preservation Check](#5-cross-system-boundary-preservation-check)
6. [Coverage Completeness Verification](#6-coverage-completeness-verification)

---

## 1. TRS Requirement Family Coverage Matrix

This matrix shows every TRS requirement family from Stage 4 and confirms it is architecturally realized in Stage 5. No family was silently dropped.

| TRS Family | TRS IDs | Architecture Section | Architecture Coverage | Status |
|---|---|---|---|---|
| Executive Estate Oversight | TR-101 to TR-104 | §3.2, §3.3, §3.8 | Route architecture, dashboard summary API, health domain computation, session restore | ✅ Realized |
| Alert Management | TR-201 to TR-209 | §3.4, §4.3, §6.1 | Alert table, delivery pipeline, timing SLA architecture, retry architecture, two-level escalation chain, class-based dismissal enforcement | ✅ Realized |
| Approval Workflow | TR-301 to TR-304 | §3.3, §3.4, §4.5, §5.1, §5.2 | Approvals table, API contract, post-approval dispatch, blocking gate, authority enforcement, downstream dispatch | ✅ Realized |
| Intervention | TR-401 to TR-404 | §3.3, §3.4, §5.5, §6.1 | Interventions table, dispatch API, status callback, cancel contract, Foreman integration | ✅ Realized |
| AI-Routed Actions (AIMC) | TR-501 to TR-504 | §3.3, §3.4, §4.3, §5.1, §5.6 | AIMC action log table, AIMC API call contract, callback endpoint, non-bypass enforcement at dependency + runtime layers | ✅ Realized |
| AIMCC / KUC Supervision | TR-601 to TR-609 | §3.2, §3.3, §3.4, §4.2, §5.2, §5.3 | Upload status read, quota data read, governance action, KUC non-bypass, quota adjustment console, quota override, quota threshold state machine, quota authorization, quota audit | ✅ Realized |
| Memory-Aware / Knowledge-Aware View | TR-701 to TR-703 | §3.4, §5.4, §6.3 | Knowledge retrieval API, retrieval log table, non-ownership enforcement, cache TTL, provenance requirement | ✅ Realized |
| Executive Conversation | TR-801 to TR-805 | §3.2, §3.4, §3.5, §5.1 | Conversation messages table, conversation API, AIMC conversation callback, proactive message push, cross-device continuity via Realtime | ✅ Realized |
| Specialist Agent Workspace Oversight | TR-901 to TR-902 | §3.3, §5.5 | Workspace status API, termination approval gate, Specialist Agent integration architecture | ✅ Realized |
| Maintenance & Assurance Reporting | TR-1001 to TR-1002 | §3.3 | Reports surface API, critical finding alert auto-generation | ✅ Realized |
| Estate Configuration & Wellbeing | TR-1101 to TR-1102 | §3.3, §5.5 | Foreman reporting feed contract, configuration change approval enforcement | ✅ Realized |
| Mobile Continuity | TR-1201 to TR-1203 | §3.2, §3.7, §6.2 | Responsive layout architecture (≤768px breakpoint), push notification architecture (FCM/APNs/Web Push), cross-device state synchronization via Realtime | ✅ Realized |
| Audit & Provenance | TR-1301 to TR-1305 | §4.4, §6.1, §6.3 | Append-only audit_events, required event types, provenance enforcement, cross-system linkage, audit delivery atomicity via database transaction | ✅ Realized |
| Authentication & Authorization | TR-1401 to TR-1405 | §3.3, §4.5, §7.1, §7.2 | Supabase Auth JWT, MFA requirement, RLS, actor type model, authority-domain enforcement middleware, inter-service trust boundary | ✅ Realized |
| Cross-System Integration | TR-1501 to TR-1505 | §5.1–§5.5, §3.3 | AIMC/AIMCC/Knowledge health polling, service token management per external dependency, environment-variable-configured base URLs, startup validation | ✅ Realized |
| Degraded-Mode Behavior | TR-1601 to TR-1604 | §3.6, §6.4, §6.5 | Health events table, AIMC degraded behavior, AIMCC degraded behavior, knowledge system degraded behavior, recovery detection and signaling | ✅ Realized |
| State & Persistence | TR-1701 to TR-1703 | §4.6, §6.1, §6.2 | Canonical state ownership table confirmed architecture-binding, state consistency via Realtime broadcast, session restore API re-fetch protocol | ✅ Realized |
| **ARC Technical Domain** | **TR-1801 to TR-1806** | **§4.1, §3.2, §3.4, §3.5, §3.6** | **ARC as first-class domain: arc_classifications table, /api/arc/ namespace, /arc route, ARC triggering architecture, ARC state machine, ARC authority enforcement, ARC audit family, ARC Realtime subscription** | **✅ Realized** |

**Result: 18 TRS requirement families. 18 families architecturally realized in Stage 5. 0 silently dropped.**

---

## 2. Individual TRS Family Traceability

This section traces each TRS family to its Stage 5 architectural realization, noting items deferred to Stage 6.

### TR-100 Family: Executive Estate Oversight

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-101 | `GET /api/dashboard/summary` endpoint contract; response payload structure; partial-availability flag | Architecture §3.3: API endpoint bound; Next.js API route; §3.8: per-domain health computation rules defined (System/Execution/Governance/Security/Compliance domains) | Health domain computation UI component layout → ui-builder |
| TR-102 | `GET /api/dashboard/health/{domain_id}` contract; unavailability response | Architecture §3.3: Endpoint bound in API namespace; unavailability response pattern established | Per-domain drill-down UI → ui-builder |
| TR-103 | AIMC `proactive_summary` dispatch contract; polling interval; degraded string | Architecture §5.1: AIMC interaction pattern; polling via Supabase Edge Function health scheduler; §6.4: degraded string enforcement | None |
| TR-104 | Named routes list; navigation must not depend on AIMC/AIMCC availability | Architecture §3.2: Full route list defined including `/arc`; route guard architecture (Next.js middleware, server-side) | Route guard code implementation → api-builder |

### TR-200 Family: Alert Management

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-201 | `alerts` table schema requirements; `GET /api/alerts` priority ordering; error on fetch failure | Architecture §3.4: Table defined in AMC-owned table set; §4.3: alert delivery pipeline; append-only for dismissed/resolved (retained for history) | Column DDL → schema-builder |
| TR-202 | `POST /api/alerts/{id}/acknowledge` contract; actor auth; audit event | Architecture §3.3: API route; §4.5: actor resolution middleware; §6.3: audit atomicity | None |
| TR-203 | `POST /api/alerts/{id}/escalate` contract; manual and timeout escalation | Architecture §4.3: Two-level escalation chain architecture; §3.6: scheduler function `amc-alert-escalation-scheduler` | None |
| TR-204 | Server-side dismissal class enforcement; HTTP 422 for Critical/High/Medium | Architecture §3.3: API middleware enforces class-based dismissal; §4.3: enforcement explicitly called out | None |
| TR-205 | `POST /api/alerts/{id}/link-approval` contract; audit event | Architecture §3.3: API endpoint; §3.4: FK relationship `approvals.source_alert_id` | None |
| TR-206 | Background scheduler contract; query pattern; scheduler failure alert | Architecture §3.6: `amc-alert-escalation-scheduler` Edge Function defined; failure generates Critical alert | Scheduler code implementation → api-builder |
| TR-207 | Alert timing SLAs (trigger→INSERT ≤5s; INSERT→Realtime ≤2s; INSERT→push ≤5s) | Architecture §4.3: Alert delivery pipeline with SLA timing; §3.6: `amc-alert-timing-sla-monitor` component | SLA monitor implementation → api-builder |
| TR-208 | 3-retry exponential back-off on alert INSERT failure | Architecture §4.3: Retry architecture defined (1s, 3s, 10s) | Retry implementation → api-builder |
| TR-209 | Two-level escalation chain with distinct audit events per level | Architecture §4.3: Full escalation chain architecture (Level 0/1/2, default timeouts, terminal conditions) | None |

### TR-300 Family: Approval Workflow

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-301 | `approvals` table schema; `GET /api/approvals` endpoint | Architecture §3.4: Table defined; §3.8: approval queue ordering (reserved_matter first, then deadline) | Column DDL → schema-builder; approval detail UI → ui-builder |
| TR-302 | `POST /api/approvals/{id}/decide` contract; basis/reason enforcement; race condition idempotency | Architecture §3.3: Endpoint bound; §6.1: idempotency enforcement (HTTP 409) | None |
| TR-303 | Post-approval downstream dispatch; approval persistence on dispatch failure | Architecture §3.3: Atomic post-commit dispatch architecture; approval record persists on dispatch failure | None |
| TR-304 | Server-side approval blocking gate; HTTP 423 | Architecture §3.3: API middleware blocking gate | None |

### TR-400 Family: Intervention

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-401 | `interventions` table schema | Architecture §3.4: Table defined in AMC-owned table set | Column DDL → schema-builder |
| TR-402 | Intervention dispatch API to Foreman / Specialist Agent | Architecture §5.5: Foreman/Specialist Agent interaction architecture; governed auth token; HTTP 202 acknowledgment | None |
| TR-403 | `POST /api/interventions/{id}/status-update` callback contract | Architecture §5.5: Callback endpoint defined; §4.5: service token validation required | None |
| TR-404 | `POST /api/interventions/{id}/cancel`; abort signal to executing agent | Architecture §3.3: API endpoint; §5.5: abort signal dispatch to executing agent | None |

### TR-500 Family: AI-Routed Actions (AIMC)

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-501 | `aimc_action_log` table schema | Architecture §3.4: Table defined in AMC-owned table set | Column DDL → schema-builder |
| TR-502 | All AI action dispatches via AIMC API; no model provider SDK | Architecture §5.1: AIMC integration pattern; §5.6: non-bypass enforcement at dependency + runtime layers; §3.3: API layer | AIMC client code → api-builder |
| TR-503 | `POST /api/aimc/callback` contract; service identity validation | Architecture §5.1: Callback endpoint defined; §4.5: service token validation; §7.1: trust boundary | None |
| TR-504 | Non-bypass enforcement: `package.json` check, `BOUNDARY_BYPASS_ATTEMPTED` audit event | Architecture §5.6: Three-layer enforcement (CI dependency scan, startup validation, runtime detection) | CI dependency scan implementation → Stage 12 |

### TR-600 Family: AIMCC / KUC Supervision

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-601 | AIMCC upload status read; stale data handling | Architecture §5.2: AIMCC interaction; §6.4: AIMCC degraded stale data with `stale: true` marker | None |
| TR-602 | Quota data read from AIMCC; TTL cache | Architecture §4.2: Quota Management Console architecture; §6.4: AIMCC degraded fallback | None |
| TR-603 | AIMCC governance action creation via approval; governance decision notification | Architecture §4.2: Quota console → approval workflow; §5.2: governance decision notification pattern | None |
| TR-604 | KUC non-bypass enforcement | Architecture §5.3: KUC exclusive submission path; §5.6: runtime bypass detection | None |
| TR-605 | `POST /api/aimcc/quota/request-adjustment` console action | Architecture §4.2: Quota Management Console; operational console capability | None |
| TR-606 | Temporary quota override with `override_expiry_at` | Architecture §4.2: Override contract; §3.6: `amc-quota-override-reminder` scheduler | None |
| TR-607 | Quota threshold state machine (ok/warning/critical); configurable thresholds | Architecture §4.2: State machine architecture; §3.6: `amc-quota-threshold-monitor` | None |
| TR-608 | Quota authorization rules (reserved_matter for adjustments) | Architecture §4.2: Authorization rules; §4.5: authority-domain enforcement middleware | None |
| TR-609 | Quota audit events and observability | Architecture §4.4: Quota event category; history reconstructable from `audit_events` | None |

### TR-700 Family: Memory-Aware / Knowledge-Aware View

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-701 | Knowledge retrieval API contract; `require_provenance: true` | Architecture §5.4: Knowledge system interaction; §6.3: provenance enforcement | None |
| TR-702 | `knowledge_retrieval_log` table schema (no knowledge content) | Architecture §3.4: Table defined in AMC-owned table set | Column DDL → schema-builder |
| TR-703 | No knowledge content stored in AMC tables; 5-minute TTL cache | Architecture §4.6: State ownership — knowledge system writes prohibited; §5.4: cache architecture | Knowledge view UI → ui-builder |

### TR-800 Family: Executive Conversation

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-801 | `conversation_messages` table schema | Architecture §3.4: Table defined in AMC-owned table set | Column DDL → schema-builder |
| TR-802 | Conversation API contracts (GET history, POST message, AIMC dispatch) | Architecture §3.3: Endpoint bound; §5.1: AIMC conversation dispatch | None |
| TR-803 | AIMC conversation callback contract; `response_type` validation | Architecture §5.1: Conversation callback endpoint defined; §4.5: service token validation | None |
| TR-804 | Proactive message push contract; alert creation from `alert_class` | Architecture §5.1: Proactive message endpoint; §3.4: FK to alerts table | None |
| TR-805 | Cross-device conversation continuity via server-side storage + Realtime | Architecture §6.2: Cross-device continuity architecture; §3.5: `amc_conversation_{session_id}` channel | None |

### TR-900 Family: Specialist Agent Workspace Oversight

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-901 | Workspace status API; `sandbox_isolation_indicator` required | Architecture §5.5: Specialist Agent interaction; workspace data display rules | None |
| TR-902 | Workspace termination approval gate | Architecture §3.3: Termination endpoint; §5.5: approval-gated termination | None |

### TR-1000 Family: Maintenance & Assurance Reporting

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-1001 | `GET /api/reports` contract; IAA report filter | Architecture §3.3: Reports API endpoint | Report surface UI → ui-builder |
| TR-1002 | Critical finding auto-alert generation | Architecture §3.3: Alert creation trigger on critical report receipt | None |

### TR-1100 Family: Estate Configuration & Wellbeing

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-1101 | Foreman reporting feed contract; unavailability display | Architecture §5.5: Foreman integration; §3.8: reporting feed format defined | None |
| TR-1102 | Configuration change approval enforcement | Architecture §3.3: Config change endpoint; approval-gated | None |

### TR-1200 Family: Mobile Continuity

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-1201 | Responsive ≤768px layout; critical alerts immediate on mobile load | Architecture §3.2: Responsive breakpoint architecture; mobile layout requirements | Mobile UI component implementation → ui-builder |
| TR-1202 | Critical alert push notification (FCM/APNs/Web Push); failure handling | Architecture §3.7: Push notification architecture defined; platform selection decided | Push client implementation → integration-builder |
| TR-1203 | Cross-device state synchronization | Architecture §6.2: Cross-device continuity; §3.5: Realtime subscription architecture | None |

### TR-1300 Family: Audit & Provenance

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-1301 | `audit_events` append-only table | Architecture §3.4: Table defined; §4.4: append-only architectural enforcement at RLS and API layers | Column DDL → schema-builder |
| TR-1302 | Required audit event types | Architecture §4.4: Full audit event categories table with required fields per category | None |
| TR-1303 | `GET /api/audit-events` access endpoint | Architecture §3.3: Endpoint in API namespace | None |
| TR-1304 | Cross-system audit linkage (`cross_system_ref`) | Architecture §6.3: Cross-system audit linkage architecture | None |
| TR-1305 | Audit delivery atomicity — action + audit event in single transaction | Architecture §6.1: Transactional integrity; §6.3: Audit atomicity via database transaction | None |

### TR-1400 Family: Authentication & Authorization

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-1401 | Supabase Auth JWT; MFA; httpOnly cookie token storage | Architecture §4.5: Authentication architecture; Supabase Auth decision confirmed | None |
| TR-1402 | Supabase PostgreSQL RLS on all tables | Architecture §3.4: RLS on all AMC-owned tables; `organisation_id` tenant isolation key | RLS policy DDL → schema-builder |
| TR-1403 | Actor type model; resolution at API layer from JWT / service token | Architecture §4.5: Actor type architecture; resolution middleware | None |
| TR-1404 | Authority-domain enforcement as server-side middleware | Architecture §4.5: Authority boundary enforcement middleware architecture; §7.2: authority boundary map | Middleware code implementation → api-builder |
| TR-1405 | Inter-service trust boundary; callback validation; token rotation; no trust escalation | Architecture §4.5: Inter-service trust architecture; §7.1: trust boundary map | None |

### TR-1500 Family: Cross-System Integration

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-1501 | AIMC health check polling; degraded mode on failure | Architecture §3.6: `amc-health-poll-scheduler` Edge Function; §6.4: AIMC degraded mode behavior | None |
| TR-1502 | AIMCC health check polling; degraded mode | Architecture §3.6: Scheduler; §6.4: AIMCC degraded mode | None |
| TR-1503 | Knowledge System health check polling; cache invalidation | Architecture §3.6: Scheduler; §6.4: Knowledge system degraded mode | None |
| TR-1504 | Service token management per dependency (env vars) | Architecture §3.3: Environment variable token configuration; §4.5: trust architecture | None |
| TR-1505 | External API base URL environment variables; startup validation on missing config | Architecture §3.3: Startup config validation architecture; all URLs env-var-configured; listed required env vars | Startup check implementation → api-builder |

### TR-1600 Family: Degraded-Mode Behavior

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-1601 | `system_health_events` table schema | Architecture §3.4: Table defined in AMC-owned table set | Column DDL → schema-builder |
| TR-1602 | AIMC degraded mode technical behavior | Architecture §6.4: Full AIMC degraded mode behavior rules; §5.1: degraded mode from AIMC interaction | None |
| TR-1603 | AIMCC degraded mode technical behavior | Architecture §6.4: Full AIMCC degraded mode behavior rules | None |
| TR-1604 | Knowledge system degraded mode technical behavior | Architecture §6.4: Full knowledge system degraded mode behavior rules | None |

### TR-1700 Family: State & Persistence

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-1701 | Canonical state ownership table (architecture-binding) | Architecture §4.6: Full state ownership table confirmed and reproduced as architecture-binding | None |
| TR-1702 | State mutations propagate via Supabase Realtime; no stale-while-revalidate | Architecture §6.1: State consistency via Realtime broadcast; §3.5: channel architecture | Realtime subscription code → api-builder |
| TR-1703 | Session restore re-fetch protocol | Architecture §6.2: Session restore architecture; all 5 required re-fetch calls defined | None |

### TR-1800 Family: ARC Technical Domain

| TRS ID | TRS Requirement Summary | Architecture Realization | Deferred to Stage 6 |
|---|---|---|---|
| TR-1801 | ARC as distinct technical domain; `arc_classifications` table; `/api/arc/` namespace; `/arc` route | Architecture §4.1: ARC as first-class architectural domain; dedicated table, API namespace, route all defined | ARC UI component implementation → ui-builder |
| TR-1802 | ARC triggering model (5 conditions); server-side classification | Architecture §4.1: Triggering architecture; §3.6: `amc-arc-staleness-scheduler` and `amc-approval-arc-timeout-checker` | Classification logic code → api-builder |
| TR-1803 | ARC authority path (reserved_matter = Johan Ras only) | Architecture §4.1: ARC authority enforcement; §4.5: authority-domain middleware | None |
| TR-1804 | ARC state machine (open → in_resolution → resolved / externally_escalated) | Architecture §4.1: Full state machine architecture with transition rules; stale alert via `amc-arc-staleness-scheduler` | State machine implementation → api-builder |
| TR-1805 | ARC audit requirements; required ARC audit event types | Architecture §4.4: ARC lifecycle events category; audit atomicity applies | None |
| TR-1806 | ARC architecture requirements (distinct table, /api/arc/ namespace, Realtime subscription, DDL deferred) | Architecture §4.1: All TR-1806 requirements satisfied; §3.5: `amc_arc_{user_id}` Realtime channel; §9: DDL deferred to schema-builder | `arc_classifications` DDL → schema-builder; ARC Realtime wiring → api-builder |

---

## 3. Stage 5 Deferred Items Register

The following items are explicitly deferred from Stage 5 Architecture to Stage 6 QA-to-Red and beyond. These are Stage 6 and builder responsibilities. They are NOT descoped — Stage 5 has defined the architectural constraints that govern their realization.

| Deferred Item | TRS Deferral Reference | Stage 6 / Builder Responsibility | Architecture Constraint Applied |
|---|---|---|---|
| Database column types and index DDL for all tables | TRS §25 | schema-builder | Column names and minimum sets defined in TRS §4–§21; Architecture §3.4 defines all tables; DDL must implement exactly |
| React component tree and UI component design | TRS §25 | ui-builder | Routes defined (§3.2); responsive breakpoints defined (§3.2); surface-level requirements from TRS TR-104, TR-1201 |
| CI script implementation | TRS §25 | Stage 12 Build | CI gate structure defined (§3.8); dependency scan gate required |
| API code implementation | TRS §25 | api-builder | All API contracts from TRS §22 are binding; architecture defines middleware layers (§3.3) |
| Realtime channel subscription implementation | TRS §25 | api-builder | Channel names and event patterns defined (§3.5) |
| Test specifications | — | Stage 6 QA-to-Red | Architecture defines all boundaries for test derivation |
| Push notification device registration implementation | TRS §25 | integration-builder | Architecture defines platform pattern (§3.7); `push_device_registrations` ancillary table noted |
| `arc_classifications` table DDL | TRS §25 | schema-builder | Minimum column set defined in TRS TR-1806; architecture confirms requirement |
| ARC surface UI/UX design | TRS §25 | ui-builder | Route `/arc`, sidebar navigation, Realtime subscription defined |
| ARC Realtime subscription wiring | TRS §25 | api-builder | Channel `amc_arc_{user_id}` defined (§3.5) |
| Alert timing SLA breach self-monitoring | TRS §25 | api-builder | Architecture defines `amc-alert-timing-sla-monitor` component role (§4.3) |
| Quota threshold configuration storage and runtime reload | TRS §25 | Architecture resolved: env vars (`QUOTA_WARNING_THRESHOLD_PERCENT`, `QUOTA_CRITICAL_THRESHOLD_PERCENT`) | Architecture §3.6 resolves this deferral |
| ARC stale-item alert scheduling | TRS §25 | Architecture resolved: `amc-arc-staleness-scheduler` Edge Function defined (§3.6) | Architecture §3.6 resolves this deferral |
| Background scheduler implementation mechanism | TRS §25 | Architecture resolved: Supabase Edge Functions with cron triggers | Architecture §3.6 resolves this deferral |
| API server framework selection | TRS §25 | Architecture resolved: Next.js App Router API Routes | Architecture §3.3 resolves this deferral |
| Push notification service provider selection | TRS §25 | Architecture resolved: Web Push + FCM + APNs | Architecture §3.7 resolves this deferral |
| Per-domain health status computation algorithm | TRS §25 | Architecture resolved: computation rules per domain defined | Architecture §3.8 resolves this deferral |
| Authority delegated-domain configuration storage format | TRS §25 | Architecture resolved: `authority_domain_config` Supabase table | Architecture §3.6 resolves this deferral |
| Approval queue priority/deadline ordering | TRS §25 | Architecture resolved: `reserved_matter` → deadline → `delegated` → `operational` | Architecture §3.8 resolves this deferral |
| Alert history view API endpoint | TRS §25 | Architecture resolved: `GET /api/alerts?status=all` query parameter | Architecture §3.8 resolves this deferral |
| Deferral reminder scheduling | TRS §25 | Architecture resolved: `amc-approval-arc-timeout-checker` function handles follow-up reminders | Architecture §3.6 resolves this deferral |
| Foreman reporting feed format details | TRS §25 | Architecture resolved: format defined (§3.8) | Architecture §3.8 resolves this deferral |
| `push_device_registrations` DDL | Not in TRS §25 (ancillary) | schema-builder | Architecture §3.7 notes this ancillary table |
| RLS policy DDL for all tables | Not explicitly in TRS §25 | schema-builder | Architecture §3.4 defines all RLS requirements (tenant-scoped per `organisation_id`) |

---

## 4. TRS Deferred-to-Stage-5 Resolution Status

TRS §25 listed 16 items deferred to Stage 5 Architecture. This section confirms their resolution status.

| TRS §25 Deferred Item | Resolution Status | Architecture Section |
|---|---|---|
| Database column types and index DDL | ⬜ NOT RESOLVED HERE — deferred to schema-builder | §3.4 defines tables; DDL deferred onward |
| Frontend React component tree | ⬜ NOT RESOLVED HERE — deferred to ui-builder | §3.2 defines routes and breakpoints; component tree deferred |
| API server framework selection | ✅ RESOLVED — Next.js App Router API Routes | §3.3, §3.8 |
| Realtime channel subscription implementation details | ⬜ NOT RESOLVED HERE — deferred to api-builder | §3.5 defines channels and event patterns; wiring code deferred |
| CI/CD pipeline and deployment infrastructure | ✅ RESOLVED (architecture level) — Vercel + CI gate structure | §3.8 |
| Push notification service provider selection | ✅ RESOLVED — Web Push API + FCM + APNs | §3.7, §3.8 |
| AIMC health check failure retry logic | ✅ RESOLVED — No retry before degraded mode entry; degraded mode entered immediately on non-200 | §6.4 |
| Per-domain health status computation algorithm | ✅ RESOLVED — Five-domain computation rules defined | §3.8 |
| Authority delegated-domain configuration storage format | ✅ RESOLVED — `authority_domain_config` Supabase table | §3.6, §4.5 |
| Foreman reporting event feed format details | ✅ RESOLVED — Format defined | §3.8, §5.5 |
| Background scheduler implementation mechanism | ✅ RESOLVED — Supabase Edge Functions with cron triggers | §3.6 |
| `arc_classifications` table DDL | ⬜ NOT RESOLVED HERE — deferred to schema-builder | §4.1 defines minimum columns; DDL deferred |
| ARC surface UI/UX design and component tree | ⬜ NOT RESOLVED HERE — deferred to ui-builder | §4.1 defines ARC architectural structure; UI design deferred |
| ARC Realtime subscription wiring | ⬜ NOT RESOLVED HERE — deferred to api-builder | §3.5 defines `amc_arc_{user_id}` channel; wiring code deferred |
| Alert timing SLA breach self-monitoring implementation | ⬜ NOT RESOLVED HERE — deferred to api-builder | §4.3 defines `amc-alert-timing-sla-monitor` role; code deferred |
| Quota threshold configuration storage and runtime reload | ✅ RESOLVED — Environment variables (`QUOTA_WARNING_THRESHOLD_PERCENT`, `QUOTA_CRITICAL_THRESHOLD_PERCENT`) | §3.6, §4.2 |
| ARC stale-item alert scheduling implementation | ✅ RESOLVED — `amc-arc-staleness-scheduler` Edge Function | §3.6 |

**Summary**: 9 TRS §25 deferred items resolved in Stage 5 Architecture. 8 items appropriately deferred onward to schema-builder (DDL), ui-builder (UI design), and api-builder (code implementation). 0 items silently dropped.

---

## 5. Cross-System Boundary Preservation Check

This section verifies that the approved cross-system boundary model from Stage 1 and Stage 4 TRS §2 is preserved in Stage 5 Architecture without reassignment, softening, or contradiction.

| Boundary Rule | TRS Source | Architecture Enforcement | Status |
|---|---|---|---|
| AMC does not call any AI model SDK | TR-BOUNDARY-001 | §5.6: three-layer enforcement (CI dependency scan, startup check, runtime detection) | ✅ PRESERVED |
| AMC does not call AIMCC ingestion endpoints | TR-BOUNDARY-002 | §5.3: KUC exclusive submission; §5.6: runtime detection | ✅ PRESERVED |
| AMC does not write to knowledge/memory system | TR-BOUNDARY-003 | §4.6: state ownership; §5.4: read-only architecture | ✅ PRESERVED |
| AMC does not maintain canonical knowledge records | TR-BOUNDARY-003 | §5.4: 5-minute TTL cache only; no content columns in schema | ✅ PRESERVED |
| All outbound AMC API calls include service token | TR-BOUNDARY-004 | §4.5: service token management; §5.1–§5.5: per-integration auth | ✅ PRESERVED |
| AMC = executive supervisory operating surface | Stage 1 §1 | Architecture introduces no AI model invocation, no knowledge write, no ingestion trigger | ✅ PRESERVED |
| AIMC = sole AI execution gateway | Stage 1 §1 | §5.1: AIMC as exclusive AI gateway; §5.6: no direct model provider calls | ✅ PRESERVED |
| AIMCC = knowledge ingestion / memory operations layer | Stage 1 §1 | §5.2: AMC reads AIMCC status/quota only; does not call ingestion | ✅ PRESERVED |
| KUC = governed upload entry point | Stage 1 §1 | §5.3: all upload submissions POST to KUC API exclusively | ✅ PRESERVED |
| Knowledge/memory system = persistent knowledge substrate | Stage 1 §1 | §5.4: AMC is read-only consumer; §4.6: no ownership of knowledge content | ✅ PRESERVED |
| Foreman = orchestration reporting/dispatch | Stage 1 §1 | §5.5: AMC reads Foreman reporting feed only; dispatches interventions only | ✅ PRESERVED |
| AMC is sole writer to AMC-owned tables | TR-1405 | §4.5: inter-service trust boundary; all external writes via callback validation | ✅ PRESERVED |
| No external service directly writes AMC tables | TR-1405 | §7.1: trust boundary; all callbacks validated before processing | ✅ PRESERVED |

**Cross-system boundary preservation result**: All 13 boundary rules from Stage 1 and TRS are preserved in Stage 5 Architecture. No boundary was reassigned, softened, or contradicted.

---

## 6. Coverage Completeness Verification

### 6.1 TRS Requirement Family Coverage Summary

| Count | Item |
|---|---|
| 18 | Total TRS requirement families (TR-100 through TR-1800) |
| 18 | TRS families architecturally realized in Stage 5 |
| 0 | TRS families silently dropped |
| 0 | TRS families with no architecture section reference |

**Verdict: 100% TRS requirement family coverage. No silent drops. ✅**

### 6.2 Mandatory Architecture Inclusions Verification

The issue requirements specified 5 mandatory architecture inclusion areas. Coverage verification:

| Mandatory Inclusion | Issue Requirement | Architecture Section | Status |
|---|---|---|---|
| **Core architecture structure** | Major components, frontend/backend/orchestration/integration boundaries, state ownership, trust boundaries, deployment-shaping | §3 (Core Architecture Structure), §7 (Trust Boundaries), §8 (Deployment-Shaping Decisions) | ✅ COVERED |
| **AMC domain recognition** | ARC as named first-class domain; Dynamic Upload Quota Management as operational console; contract-level control surfaces for alert/escalation/audit/state/auth | §4.1 (ARC), §4.2 (Quota Management), §4.3 (Alert/Escalation), §4.4 (Audit), §4.5 (Auth/Auth), §4.6 (State) | ✅ COVERED |
| **Cross-system interaction architecture** | AMC ↔ AIMC, AIMCC, KUC, knowledge/memory, Foreman/agents; direction of responsibility; routing; non-bypass | §5 (all subsections) | ✅ COVERED |
| **State, audit, and resilience architecture** | State ownership; cross-device continuity; audit/provenance recording; degraded-mode; recovery/stale-data signaling | §6 (all subsections) | ✅ COVERED |
| **Traceability** | TRS requirement families realized; no silent Stage 4 family drop; Stage 6 deferrals disclosed | §1–§4 of this document | ✅ COVERED |

### 6.3 Issue Acceptance Criteria Verification

| Acceptance Criterion | Architecture Evidence | Status |
|---|---|---|
| `architecture-specification.md` exists | Created at `modules/amc/04-architecture/architecture-specification.md` v1.0 | ✅ |
| `trs-to-architecture-traceability.md` exists | This document — `modules/amc/04-architecture/trs-to-architecture-traceability.md` v1.0 | ✅ |
| Architecture preserves AMC ↔ AIMC ↔ AIMCC ↔ KUC ↔ knowledge/memory boundaries | §5 and §5 Cross-System Boundary Preservation Check | ✅ |
| ARC explicitly recognizable as its own domain | §4.1: dedicated table, API namespace, route, audit family, Realtime channel | ✅ |
| Dynamic Upload Quota Management as operational console capability | §4.2: Quota Management Console architecture | ✅ |
| Alert/escalation/audit/state/auth contract-level control surfaces reflected | §4.3–§4.6, §7 | ✅ |
| Traceability shows no silent Stage 4 family drop | §1: 18/18 families covered; §6.1: 0 dropped | ✅ |
| `BUILD_PROGRESS_TRACKER.md` updated | Updated in TASK-5-03 (see tracker) | ✅ |
| Stage 6 remains blocked pending Stage 5 approval | Tracker Stage 6 marked BLOCKED; Architecture §10 sign-off section | ✅ |
| Stage 5 artifact set contains CS2 sign-off section | Architecture §10 | ✅ |

---

*End of TRS to Architecture Traceability — Stage 5 v1.0. Produced by foreman-v2-agent under POLC_ORCHESTRATION. CS2 approval required before Stage 6 QA-to-Red derivation begins.*

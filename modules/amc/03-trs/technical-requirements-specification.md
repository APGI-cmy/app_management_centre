# Technical Requirements Specification — Stage 4

**Stage**: 4 — Technical Requirements Specification (TRS)
**Module**: App Management Centre (AMC)
**Version**: 1.0
**Status**: 🟡 Produced Approval-Ready — 2026-04-23
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: harmonization issue (CS2-opened, 2026-04-23)
**Upstream Sources**:
- Stage 1 App Description: `modules/amc/00-app-description/app-description.md` v1.1
- Stage 2 UX Workflow & Wiring Spec: `modules/amc/01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md` v1.1
- Stage 3 FRS: `modules/amc/02-frs/functional-requirements-specification.md` v1.1
**Canonical Location**: `modules/amc/03-trs/technical-requirements-specification.md`

---

> **DERIVATION DECLARATION**
> This document derives from the approved Stage 3 FRS, Stage 2 UX Wiring Spec, and Stage 1 App Description. It translates functional requirements into explicit technical obligations and constraints. No technical obligation may be introduced without a traceable upstream FRS source. All technology stack choices are constrained by Stage 1 §8.1 Technology Stack Baseline.

---

## Table of Contents

1. [Purpose & Scope](#1-purpose--scope)
2. [Technology Stack Baseline](#2-technology-stack-baseline)
3. [TR-100: Frontend Technical Requirements](#3-tr-100-frontend-technical-requirements)
4. [TR-200: Backend API Technical Requirements](#4-tr-200-backend-api-technical-requirements)
5. [TR-300: ARC Technical Domain](#5-tr-300-arc-technical-domain)
6. [TR-400: Alert Timing & Escalation Technical Contracts](#6-tr-400-alert-timing--escalation-technical-contracts)
7. [TR-500: Audit Technical Contracts](#7-tr-500-audit-technical-contracts)
8. [TR-600: State & Persistence Technical Contracts](#8-tr-600-state--persistence-technical-contracts)
9. [TR-700: Authentication & Authorization Technical Contracts](#9-tr-700-authentication--authorization-technical-contracts)
10. [TR-800: Operational Quota Management Technical Contracts](#10-tr-800-operational-quota-management-technical-contracts)
11. [TR-900: Cross-System Integration Technical Contracts](#11-tr-900-cross-system-integration-technical-contracts)
12. [TR-1000: Degraded-Mode Technical Requirements](#12-tr-1000-degraded-mode-technical-requirements)
13. [TR-1100: Mobile Technical Requirements](#13-tr-1100-mobile-technical-requirements)
14. [Technical Non-Negotiables Summary](#14-technical-non-negotiables-summary)

---

## 1. Purpose & Scope

### 1.1 Purpose

The TRS translates the approved FRS into explicit technical obligations and constraints. It defines what the AMC system must do technically — including infrastructure constraints, API contracts, data contracts, timing contracts, security contracts, and integration contracts — to correctly implement the functional requirements.

### 1.2 Scope

This TRS covers: frontend (React 18/TypeScript/Vite), backend API (Supabase Edge Functions), ARC Governance Console technical domain (TR-300), alert timing/escalation contracts (TR-400), audit contracts (TR-500), state/persistence contracts (TR-600), auth/authorization contracts (TR-700), operational quota management contracts (TR-800), cross-system integration contracts (TR-900), degraded-mode technical requirements (TR-1000), mobile technical requirements (TR-1100).

### 1.3 Non-Negotiable Derivation Rule

The TRS must not dilute upstream FRS requirements into vague technical aspiration. Every technical contract must be specific enough to be tested and verified.

---

## 2. Technology Stack Baseline

> Stage 1 Traceability: §8.1 Technology Stack Baseline, §8.2 Cross-System Platform Dependencies

| Layer | Technology | Constraint |
|---|---|---|
| **Frontend Framework** | React 18 + Vite | React 18.x; Vite latest stable |
| **Language** | TypeScript 5.x | All frontend and edge code |
| **State Management** | React Context / Zustand | Auth state and UI state |
| **Database** | Supabase (PostgreSQL 15+) | Tenant-isolated; RLS required |
| **Auth** | Supabase Auth | JWT-based; identity separation required |
| **Backend Logic** | Supabase Edge Functions (Deno) | Serverless orchestration boundary |
| **AI Integration** | AIMC Gateway only | Direct provider calls prohibited |
| **Deployment** | Vercel | Governed deployment |
| **CI/CD** | GitHub Actions | Foreman-governed pipeline |
| **Notification/UX** | react-hot-toast | Executive feedback surface |

**Inviolable constraint**: No AMC component may call an AI model provider directly. All AI interactions must route through AIMC. This is a technical enforcement requirement.

---

## 3. TR-100: Frontend Technical Requirements

> FRS Traceability: FR-100 to FR-1200, FR-1400

### TR-101 — React Component Architecture

| Field | Value |
|---|---|
| **Requirement ID** | TR-101 |
| **Technical Obligation** | AMC frontend implemented as a single React 18 + Vite + TypeScript 5.x application. No plain JS files in src/. Each named AMC domain from Stage 1 §4 AMC Technical/Operating Domain Declaration (including ARC Governance Console and Quota Management Console) must have a corresponding named TypeScript surface component. No domain surface absorbs another domain silently. |
| **Verification** | All named AMC surfaces implemented as named TypeScript components. |

### TR-102 — Authority-Aware UI State

| Field | Value |
|---|---|
| **Requirement ID** | TR-102 |
| **Technical Obligation** | All UI actions with an authority constraint must perform an authority check before the action is surfaced as available. Actions outside the current actor's authority must be rendered disabled/hidden — not rejected after submission. Authority state derives from authenticated session JWT. |
| **Verification** | Component authority check tests. Unauthorized actor cannot access action buttons. |

### TR-103 — Response Type Labeling

| Field | Value |
|---|---|
| **Requirement ID** | TR-103 |
| **Technical Obligation** | All AI-generated content rendered in AMC UI must carry a visible response type label: `Observation`, `Recommendation`, `Request`, `Decision`, or `Alert` (FR-803). `response_type` is a non-nullable field on `conversation_messages`. Missing response type renders explicit "unlabeled" indicator — not neutral text. |
| **Verification** | `response_type` non-nullable. Labels rendered for all response types in UI tests. |

### TR-104 — Degraded-Mode Banner Enforcement

| Field | Value |
|---|---|
| **Requirement ID** | TR-104 |
| **Technical Obligation** | When any upstream dependency (AIMC, AIMCC, Knowledge/Memory System, ARC execution endpoint) is in degraded state, the relevant UI surface must render a mandatory, persistent degraded-mode banner until recovery event is received. Degraded mode state tracked via centralized `system_health_events` observable. |
| **Verification** | Health state simulation tests confirm banners render on degradation and clear on recovery. |

---

## 4. TR-200: Backend API Technical Requirements

> FRS Traceability: All FR families with API routes in Stage 2 §7

### TR-201 — Edge Function API Architecture

| Field | Value |
|---|---|
| **Requirement ID** | TR-201 |
| **Technical Obligation** | All AMC backend API routes implemented as Supabase Edge Functions (Deno). No server-side routes in Vercel serverless functions or client-side code. All routes defined in Stage 2 §7 Wiring Model must have corresponding Edge Function implementations. Routes must enforce auth token validation before any data access or mutation. |
| **Verification** | All Stage 2 §7 wiring routes have Edge Function implementations. Route-level auth check tests pass. |

### TR-202 — API Auth Enforcement

| Field | Value |
|---|---|
| **Requirement ID** | TR-202 |
| **Technical Obligation** | Every API route that reads or mutates data must validate the caller's JWT before processing. Unauthenticated → 401 Unauthorized. Unauthorized (authenticated but insufficient authority) → 403 Forbidden with no data disclosure. |
| **Verification** | API integration tests confirm 401/403 on all routes. |

### TR-203 — Audit Event Atomicity

| Field | Value |
|---|---|
| **Requirement ID** | TR-203 |
| **Technical Obligation** | Every mutating API endpoint for consequential actions must produce an audit event record in `audit_events` as part of the same database transaction. Audit event and data mutation succeed or fail together — partial writes are not permitted. |
| **Verification** | Transactional tests verify atomicity. Rollback simulation confirms no partial commits. |

---

## 5. TR-300: ARC Technical Domain

> FRS Traceability: FR-1801 to FR-1807
> Stage 1 Traceability: §4 AMC Technical/Operating Domain Declaration (ARC Governance Console)
> Stage 2 Traceability: §4.4.1 ARC Governance Console Journey, §7.4.1 ARC Governance Console Wiring

> **ARC is an explicitly named, technically distinct AMC domain.** ARC is NOT implemented as a subset of the generic intervention system. It has its own data schema, API routes, and UI surface.

### TR-301 — ARC Data Schema

| Field | Value |
|---|---|
| **Requirement ID** | TR-301 |
| **Technical Obligation** | `arc_events` table implemented as a separate named table (not a `type` field on `interventions`). Required columns: `arc_event_id` (UUID PK), `triggering_condition` (text, not null), `proposed_response` (text, not null), `current_state` (enum: pending_review/approved/rejected/escalated/deferred, not null), `priority_level` (enum: critical/high/medium/low, not null), `detected_at` (timestamptz, not null), `decided_by` (UUID FK, nullable), `decided_at` (timestamptz, nullable), `decision_basis` (text, nullable — required when decided_by not null), `impact_scope` (jsonb, not null), `arc_service_ref` (text, nullable). |
| **Constraint** | RLS enabled. Only service role and authenticated Johan sessions may write. |
| **Verification** | Migration creates table with all required columns. RLS policy tests pass. |

### TR-302 — ARC Audit Log Schema

| Field | Value |
|---|---|
| **Requirement ID** | TR-302 |
| **Technical Obligation** | `arc_audit_log` table: `arc_audit_id` (UUID PK), `arc_event_id` (UUID FK → arc_events), `action_type` (enum: ARC_ACTION_APPROVED/ARC_ACTION_REJECTED/ARC_EVENT_ESCALATED/ARC_EVENT_DEFERRED, not null), `actor` (UUID, not null), `timestamp` (timestamptz, not null), `detail` (jsonb). Append-only: no UPDATE or DELETE permitted. |
| **Constraint** | RLS: authenticated users may SELECT; only service role may INSERT. UPDATE/DELETE blocked. |
| **Verification** | UPDATE/DELETE attempts on arc_audit_log fail in tests. |

### TR-303 — ARC API Routes

| Field | Value |
|---|---|
| **Requirement ID** | TR-303 |
| **Technical Obligation** | The following ARC API routes implemented as dedicated Edge Functions (not reusing intervention endpoints): `GET /api/arc/events`, `GET /api/arc/events/{id}/detail`, `POST /api/arc/events/{id}/decide`, `POST /api/arc/events/{id}/escalate`, `POST /api/arc/events/{id}/defer`. Each validates auth, checks authority, produces audit event. |
| **Verification** | All 5 ARC routes exist as distinct Edge Functions. Integration tests for 200/401/403/422. |

### TR-304 — ARC Execution Integration

| Field | Value |
|---|---|
| **Requirement ID** | TR-304 |
| **Technical Obligation** | On ARC action approval: AMC notifies ARC execution endpoint via governed API call. Payload includes: `arc_event_id`, `approved_by`, `approved_at`, `decision_basis`. AMC records response status as `execution_notification_status` on `arc_events`. AIMCC execution endpoint unavailability does NOT prevent approval from being recorded — approval stands; execution is queued pending recovery. |
| **Verification** | ARC execution notification tests. Degraded execution endpoint test confirms approval still recorded. |

---

## 6. TR-400: Alert Timing & Escalation Technical Contracts

> FRS Traceability: FR-201 to FR-209, BR-ALERT-001 to BR-ALERT-004

### TR-401 — Alert Severity Enum

| Field | Value |
|---|---|
| **Requirement ID** | TR-401 |
| **Technical Obligation** | `alerts.severity` column enforces enum at database level: `critical`, `high`, `medium`, `low`, `informational`. No free-text severity. Any severity change must be recorded in audit trail. |
| **Verification** | Schema migration enforces enum. Invalid severity values fail with constraint error. |

### TR-402 — Auto-Escalation Timing Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-402 |
| **Technical Obligation** | Unacknowledged Critical alerts auto-escalate after configurable timeout (default: 30 minutes, via `amc_config.critical_alert_escalation_timeout_minutes`). Background job fires within timeout + 5 minutes acceptable jitter. Auto-escalation creates record in `escalations` with `source: auto_escalation`. Must NOT fire if alert acknowledged before timeout. |
| **Verification** | Scheduler tests confirm auto-escalation fires within timeout window. Acknowledged alert test confirms no auto-escalation. |

### TR-403 — Alert State Machine

| Field | Value |
|---|---|
| **Requirement ID** | TR-403 |
| **Technical Obligation** | `alerts.status` enforces valid state machine at API layer: `active → acknowledged`, `active → escalated`, `acknowledged → resolved`, `acknowledged → escalated`, `escalated → resolved`. `active → dismissed` only permitted for `informational` and `low` severity. Invalid transitions rejected (422 Unprocessable Entity). |
| **Verification** | State machine transition tests. Invalid transitions return 422. |

### TR-404 — Alert Expiry Non-Resolution Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-404 |
| **Technical Obligation** | Expired alerts must NOT transition to `resolved`. Expiry moves alert to `expired` status (terminal, distinct from `resolved`). `resolved` requires explicit resolution action with recorded source. No background job may set `status = resolved` without a resolution source. |
| **Verification** | Expired alert tests confirm not shown as resolved. Resolution requires explicit source. |

### TR-405 — Quota Threshold Alert Technical Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-405 |
| **Technical Obligation** | Quota threshold proactive alerts (FR-606) generated by background monitor polling AIMCC quota state at configurable interval (default 15 minutes). Threshold breach creates alert in `alerts` with `source: quota_threshold_monitor`. Severity mapping: Warning → medium, Critical → high, Exceeded → critical. Deduplication: no duplicate active alert for same threshold level if one already exists. |
| **Verification** | Monitor polling tests. Deduplication tests. |

---

## 7. TR-500: Audit Technical Contracts

> FRS Traceability: FR-1301 to FR-1304, BR-AUDIT-001, BR-AUDIT-002

### TR-501 — Audit Event Schema

| Field | Value |
|---|---|
| **Requirement ID** | TR-501 |
| **Technical Obligation** | All audit events stored in `audit_events` table. Mandatory fields: `audit_event_id` (UUID PK), `event_type` (text, not null), `actor` (UUID or 'system', not null), `actor_role` (text, not null), `occurred_at` (timestamptz, not null, default now()), `subject_type` (text, not null), `subject_id` (text, not null), `detail` (jsonb, not null), `session_id` (UUID, nullable), `ip_address` (text, nullable). |
| **Constraint** | Append-only. No UPDATE or DELETE permitted. RLS: service role INSERT only. |
| **Verification** | Schema migration verified. UPDATE/DELETE rejected in DB policy tests. |

### TR-502 — Audit Atomicity

| Field | Value |
|---|---|
| **Requirement ID** | TR-502 |
| **Technical Obligation** | Audit event INSERT is part of same database transaction as data mutation. Transaction rollback on audit INSERT failure — no partial commits. |
| **Verification** | Rollback simulation confirms no data-without-audit partial state. |

### TR-503 — Audit Retention

| Field | Value |
|---|---|
| **Requirement ID** | TR-503 |
| **Technical Obligation** | Audit events retained minimum 24 months. No automated purge within retention window without CS2 authorization. |
| **Verification** | Retention policy documented. No automated deletion within window. |

---

## 8. TR-600: State & Persistence Technical Contracts

> FRS Traceability: FR-1701 to FR-1703, §23.4 State/Persistence Expectations Summary

### TR-601 — RLS Enforcement

| Field | Value |
|---|---|
| **Requirement ID** | TR-601 |
| **Technical Obligation** | All AMC data tables must have PostgreSQL RLS enabled with default-deny policies. Service role key never used in frontend. Frontend uses user JWT only. |
| **Verification** | RLS policy migration tests. Unauthorized JWT access returns no data. |

### TR-602 — Tenant Isolation

| Field | Value |
|---|---|
| **Requirement ID** | TR-602 |
| **Technical Obligation** | All multi-tenant tables include non-nullable `organisation_id` (UUID FK). RLS policies enforce `organisation_id = auth.jwt() → 'organisation_id'`. Cross-tenant leakage prevented at RLS level. |
| **Verification** | Cross-tenant access tests confirm no data returned for another organisation's records. |

### TR-603 — External State Ownership

| Field | Value |
|---|---|
| **Requirement ID** | TR-603 |
| **Technical Obligation** | AMC must not cache or claim canonical ownership of data owned by external systems (AIMCC, Knowledge/Memory System). Cached representations must have explicit staleness metadata and expiry. Stale data must NEVER be served as current without explicit indicator. |
| **Verification** | Data ownership audit. Every external-system cache table has staleness metadata. |

---

## 9. TR-700: Authentication & Authorization Technical Contracts

> FRS Traceability: FR-1401 to FR-1403, BR-AUTH-001 to BR-AUTH-004

### TR-701 — JWT-Based Authentication

| Field | Value |
|---|---|
| **Requirement ID** | TR-701 |
| **Technical Obligation** | Supabase Auth for all authentication. JWT includes: `sub`, `email`, `role`, `organisation_id`. JWT expiry ≤ 1 hour. Refresh tokens maintain sessions. No session cookies. |
| **Verification** | Auth flow tests confirm JWT structure. Expired token → 401. |

### TR-702 — Role-Based Authority

| Field | Value |
|---|---|
| **Requirement ID** | TR-702 |
| **Technical Obligation** | Role-authority model: `cs2` (Johan Ras — full authority including reserved matters), `maturion_delegate` (delegated authority only). Authority check at Edge Function level before database access. |
| **Verification** | `maturion_delegate` attempting reserved-matter approval → 403. |

### TR-703 — Session Isolation

| Field | Value |
|---|---|
| **Requirement ID** | TR-703 |
| **Technical Obligation** | Sessions isolated by user and organisation. Every Edge Function extracts `organisation_id` from JWT and applies it as filter on all database queries. No query omits `organisation_id` filtering on multi-tenant tables. |
| **Verification** | Cross-organisation session isolation tests. |

### TR-704 — Auth-Failure Behavior

| Field | Value |
|---|---|
| **Requirement ID** | TR-704 |
| **Technical Obligation** | Auth failure → 401 with no data disclosure. Authorization failure → 403 with no record IDs or field values in response. |
| **Verification** | Auth failure response body tests confirm no data disclosure. |

---

## 10. TR-800: Operational Quota Management Technical Contracts

> FRS Traceability: FR-603, FR-606, FR-607, BR-QUOTA-001, BR-QUOTA-002
> Stage 1 Traceability: §4 AMC Technical/Operating Domain Declaration (Dynamic Upload Quota Management)
> Stage 2 Traceability: §4.6.1 Dynamic Upload Quota Management Console Journey, §7.6.1 Quota Management Console Wiring

> **Quota Management is an operationally distinct AMC domain** with its own data schema, API routes, and AIMCC integration.

### TR-801 — Quota State Schema

| Field | Value |
|---|---|
| **Requirement ID** | TR-801 |
| **Technical Obligation** | `quota_state` table (transient AIMCC cache): `quota_state_id` (UUID PK), `organisation_id` (UUID FK, not null), `current_limit` (bigint bytes, not null), `current_usage` (bigint bytes, not null), `usage_percent` (numeric(5,2) computed), `warning_threshold_percent` (numeric(5,2), not null, default 75.0), `critical_threshold_percent` (numeric(5,2), not null, default 90.0), `last_fetched_at` (timestamptz, not null), `is_stale` (boolean, not null, default false), `stale_since` (timestamptz, nullable). |
| **Constraint** | `is_stale` set true when AIMCC unavailable or `last_fetched_at` older than `amc_config.quota_stale_threshold_minutes`. Stale quota NEVER served without `is_stale: true`. |
| **Verification** | Schema migration. Staleness indicator tests. |

### TR-802 — Quota Change Request Schema

| Field | Value |
|---|---|
| **Requirement ID** | TR-802 |
| **Technical Obligation** | `quota_change_requests` table: `request_id` (UUID PK), `organisation_id` (UUID FK, not null), `requested_by` (UUID FK, not null), `requested_at` (timestamptz, not null), `new_limit` (bigint, not null), `justification` (text, not null — non-empty enforced), `urgency` (enum: normal/high, not null), `status` (enum: pending/approved/rejected/deferred, not null), `decided_by` (UUID FK, nullable), `decided_at` (timestamptz, nullable), `decision_basis` (text, nullable — required on approval), `rejection_reason` (text, nullable — required on rejection), `aimcc_notification_status` (enum: not_sent/pending/sent/failed, not null, default not_sent), `aimcc_notified_at` (timestamptz, nullable). |
| **Verification** | Schema migration. Validation tests: empty justification rejected; decision_basis required on approval; rejection_reason required on rejection. |

### TR-803 — Quota Change AIMCC Notification

| Field | Value |
|---|---|
| **Requirement ID** | TR-803 |
| **Technical Obligation** | On quota change approval: AMC sends `POST /api/aimcc/quota/apply` with `{request_id, organisation_id, new_limit, approved_by, approved_at, decision_basis}`. Records HTTP response status as `aimcc_notification_status`. AIMCC notification failure does NOT rollback approval decision. Failed notifications enter retry queue. Console surfaces pending notification status. |
| **Verification** | AIMCC notification tests. Failure simulation confirms `aimcc_notification_status = failed` and decision still recorded. Retry queue test. |

### TR-804 — Quota Polling Technical Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-804 |
| **Technical Obligation** | Background quota polling function fetches AIMCC quota state at configurable interval (default 15 minutes). Success: update `quota_state` with `is_stale = false`. Failure: set `is_stale = true`, `stale_since = now()`. Polling jitter ≤ 5 minutes. AIMCC failures handled gracefully. |
| **Verification** | Polling schedule tests. AIMCC unavailability confirms stale state set. |

---

## 11. TR-900: Cross-System Integration Technical Contracts

> FRS Traceability: FR-1501 to FR-1504, §23.3 Cross-System Interaction Requirements Summary

### TR-901 — AIMC Integration Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-901 |
| **Technical Obligation** | All AMC → AIMC calls: (1) use governed URL from `amc_config.aimc_api_url` — no hardcoded URLs, (2) include governed auth token (not user JWT), (3) include `organisation_id`, (4) record dispatch in `aimc_action_log` before call, (5) record response outcome in `aimc_action_log`. No direct AI model provider calls from AMC — CI lint check enforced. |
| **Verification** | AIMC integration tests. CI lint check for direct AI provider URLs. |

### TR-902 — AIMCC Integration Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-902 |
| **Technical Obligation** | AMC → AIMCC permitted endpoints only: `GET /api/aimcc/uploads`, `GET /api/aimcc/uploads/{id}`, `GET /api/aimcc/quota/summary`, `POST /api/aimcc/quota/apply`, `GET /api/aimcc/health`. AMC must not call AIMCC internal ingestion endpoints. Uses governed URL from `amc_config.aimcc_api_url`. |
| **Verification** | AIMCC integration tests for each permitted endpoint. |

### TR-903 — Foreman Integration Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-903 |
| **Technical Obligation** | Intervention dispatch: `POST /api/execute/intervention` on Foreman API (URL from `amc_config.foreman_api_url`). Foreman callback received at `POST /api/amc/execution-callback/{intervention_id}`. Callback validates Foreman auth token. Build status: read-only GET only. |
| **Verification** | Foreman dispatch and callback integration tests. |

### TR-904 — ARC Execution Integration Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-904 |
| **Technical Obligation** | ARC execution notification: `POST /api/arc/execute/{arc_event_id}` on ARC execution endpoint (URL from `amc_config.arc_execution_api_url`). Payload signed with governed service token. ARC execution is a distinct integration — not routed through Foreman or AIMC. Missing config → explicit error (not silent failure). |
| **Verification** | ARC execution integration tests. Missing config test. |

---

## 12. TR-1000: Degraded-Mode Technical Requirements

> FRS Traceability: FR-1601 to FR-1603, BR-DEGRADE-001, BR-DEGRADE-002

### TR-1001 — Dependency Health Check Architecture

| Field | Value |
|---|---|
| **Requirement ID** | TR-1001 |
| **Technical Obligation** | Health check polling for each external dependency: AIMC, AIMCC, Knowledge/Memory System, ARC execution endpoint. Polls at configurable interval (default 60 seconds). Results written to `system_health_events`. Health state is per-dependency — one degraded dependency does not automatically mark others degraded. Frontend subscribes via Supabase Realtime. |
| **Verification** | Health check tests. Per-dependency degradation isolation confirmed. |

### TR-1002 — AIMC Degraded Mode

| Field | Value |
|---|---|
| **Requirement ID** | TR-1002 |
| **Technical Obligation** | AIMC degraded: (1) AIMC dispatch routes return 503 `{error: "AIMC_UNAVAILABLE"}`, (2) AIMC degraded banner on Conversation/AI Action Monitor/proactive summary surfaces, (3) no fallback to direct model provider calls. AIMC degradation must not cascade to Alert Centre, Approval Queue, Intervention Manager, ARC Console, Quota Console. |
| **Verification** | AIMC degraded mode tests. Non-AIMC surfaces operational during AIMC degradation. |

### TR-1003 — AIMCC Degraded Mode

| Field | Value |
|---|---|
| **Requirement ID** | TR-1003 |
| **Technical Obligation** | AIMCC degraded: (1) quota state served from cache with `is_stale = true`, (2) upload status served from last-fetch cache with stale indicator, (3) new quota change requests blocked at API level (503), (4) AIMCC degraded banner on AIMCC Supervision and Quota Console. Stale data must NEVER render without explicit `is_stale` flag. |
| **Verification** | AIMCC degraded mode tests. Stale flag propagation tests. Quota change request blocking at API level confirmed. |

### TR-1004 — Knowledge System Degraded Mode

| Field | Value |
|---|---|
| **Requirement ID** | TR-1004 |
| **Technical Obligation** | Knowledge/Memory System degraded: (1) retrieval requests return 503, (2) Knowledge Reference surface renders degraded indicator on all items, (3) cached knowledge rendered with explicit "may be outdated" label — not as current. Degradation must not affect Alert Centre, Approval Queue, Intervention, ARC, Quota. |
| **Verification** | Knowledge degraded mode tests. Non-knowledge surface availability confirmed. |

---

## 13. TR-1100: Mobile Technical Requirements

> FRS Traceability: FR-1201 to FR-1204

### TR-1101 — Responsive Design Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-1101 |
| **Technical Obligation** | All AMC surfaces responsive from 375px (mobile) to 1920px (desktop). Critical executive actions (acknowledge alert, approve/reject, escalate) performable on mobile without zoom or horizontal scroll. Responsive layout via CSS media queries — shared React codebase, no separate mobile app. |
| **Verification** | Responsive layout tests at 375px, 768px, 1024px, 1440px. |

### TR-1102 — Cross-Device Session Continuity

| Field | Value |
|---|---|
| **Requirement ID** | TR-1102 |
| **Technical Obligation** | Conversation, alert, approval, intervention, and ARC event state synchronized across devices via Supabase Realtime. Action taken on mobile reflected on desktop within 5 seconds without page refresh. Supabase Realtime subscriptions required on: `alerts`, `approvals`, `interventions`, `conversation_messages`, `arc_events`. |
| **Verification** | Cross-device synchronization tests. Propagation latency < 5 seconds. |

---

## 14. Technical Non-Negotiables Summary

| Non-Negotiable | Technical Enforcement | Source |
|---|---|---|
| No direct AI model provider calls from AMC | CI lint check + no provider URLs in config | FR-503, Stage 1 §2, BR-SYS-001 |
| No direct AIMCC internal ingestion from AMC | TR-902 permitted endpoints only | FR-605, BR-SYS-001 |
| ARC-gated actions must not auto-execute past approval gate | TR-304 — execution only after approval recorded | FR-1807, BR-ARC-001 |
| Audit events atomic with data mutations | TR-502 — transactional | FR-1301, BR-AUDIT-001 |
| Audit records are append-only | TR-501 — RLS, no UPDATE/DELETE | BR-AUDIT-002 |
| Stale quota data never served without indicator | TR-801 — is_stale flag mandatory | FR-603, BR-QUOTA-001 |
| Quota change basis required on approval | TR-802 — non-null constraint | FR-607, BR-QUOTA-002 |
| RLS enabled on all tables | TR-601 — default-deny policies | FR-1701, FR-1702 |
| Tenant isolation via organisation_id | TR-602 — RLS + JWT claim | Stage 1 privacy guardrails |
| JWT-based auth; service_role key never in frontend | TR-701 — frontend uses user JWT only | FR-1401 |
| Alert auto-escalation within timeout + 5 min jitter | TR-402 — scheduler contract | FR-208, BR-ALERT-003 |
| ARC is a named, separate technical domain | TR-301 to TR-304 — own table/routes/surface | FR-1801 to FR-1807, Stage 1 §4 |
| Dynamic Upload Quota Management is an operational control | TR-801 to TR-804 — own schema/routes/AIMCC integration | FR-603, FR-606, FR-607, Stage 1 §4 |

---

*End of Technical Requirements Specification — Stage 4 v1.0. Produced by foreman-v2-agent under POLC_ORCHESTRATION. CS2 approval required before Stage 5 (Architecture) may begin.*

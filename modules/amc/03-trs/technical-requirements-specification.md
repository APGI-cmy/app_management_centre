# Technical Requirements Specification — Stage 4

**Stage**: 4 — Technical Requirements Specification (TRS)
**Module**: App Management Centre (AMC)
**Version**: 1.0
**Status**: 🟡 Produced Approval-Ready — 2026-04-23
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: app_management_centre#1127
**Upstream Sources**:
- Stage 1 App Description: `modules/amc/00-app-description/app-description.md` v1.0 (CS2-approved 2026-04-22, ref #1117)
- Stage 2 UX Workflow & Wiring Spec: `modules/amc/01-ux-workflow-wiring-spec/` v1.0 (CS2-approved, ref #1121)
- Stage 3 FRS: `modules/amc/02-frs/functional-requirements-specification.md` v1.0 (CS2-approved for Stage 4 progression, ref #1123)
**Canonical Location**: `modules/amc/03-trs/technical-requirements-specification.md`

---

> **DERIVATION DECLARATION**
> This document derives directly from the approved Stage 3 FRS (`modules/amc/02-frs/functional-requirements-specification.md` v1.0), the approved Stage 2 UX Workflow & Wiring Spec, and the approved Stage 1 App Description. It translates approved functional requirements into explicit technical requirements, interface constraints, data structures, state rules, integration contracts, and implementation-constraining decisions. It does not invent product truth. No technical requirement may be introduced here without traceable derivation from Stage 1, 2, or 3 approved truth. The TRS does not replace Architecture (Stage 5) — it defines the technical boundaries that Architecture must realize.

---

## Table of Contents

1. [Purpose & Scope](#1-purpose--scope)
2. [Cross-System Technical Boundary Map](#2-cross-system-technical-boundary-map)
3. [Technology Stack Constraints](#3-technology-stack-constraints)
4. [TR-100: Executive Estate Oversight — Technical Requirements](#4-tr-100-executive-estate-oversight--technical-requirements)
5. [TR-200: Alert Management — Technical Requirements](#5-tr-200-alert-management--technical-requirements)
6. [TR-300: Approval Workflow — Technical Requirements](#6-tr-300-approval-workflow--technical-requirements)
7. [TR-400: Intervention — Technical Requirements](#7-tr-400-intervention--technical-requirements)
8. [TR-500: AI-Routed Actions (AIMC) — Technical Requirements](#8-tr-500-ai-routed-actions-aimc--technical-requirements)
9. [TR-600: AIMCC / Knowledge Upload Centre Supervision — Technical Requirements](#9-tr-600-aimcc--knowledge-upload-centre-supervision--technical-requirements)
10. [TR-700: Memory-Aware / Knowledge-Aware View — Technical Requirements](#10-tr-700-memory-aware--knowledge-aware-view--technical-requirements)
11. [TR-800: Executive Conversation — Technical Requirements](#11-tr-800-executive-conversation--technical-requirements)
12. [TR-900: Specialist Agent Workspace Oversight — Technical Requirements](#12-tr-900-specialist-agent-workspace-oversight--technical-requirements)
13. [TR-1000: Maintenance & Assurance Reporting — Technical Requirements](#13-tr-1000-maintenance--assurance-reporting--technical-requirements)
14. [TR-1100: Estate Configuration & Wellbeing — Technical Requirements](#14-tr-1100-estate-configuration--wellbeing--technical-requirements)
15. [TR-1200: Mobile Continuity — Technical Requirements](#15-tr-1200-mobile-continuity--technical-requirements)
16. [TR-1300: Audit & Provenance — Technical Requirements](#16-tr-1300-audit--provenance--technical-requirements)
17. [TR-1400: Authentication & Authorization — Technical Requirements](#17-tr-1400-authentication--authorization--technical-requirements)
18. [TR-1500: Cross-System Integration — Technical Requirements](#18-tr-1500-cross-system-integration--technical-requirements)
19. [TR-1600: Degraded-Mode — Technical Requirements](#19-tr-1600-degraded-mode--technical-requirements)
20. [TR-1700: State & Persistence — Technical Requirements](#20-tr-1700-state--persistence--technical-requirements)
21. [API / Interface Contract Summary](#21-api--interface-contract-summary)
22. [Data Schema Requirements Summary](#22-data-schema-requirements-summary)
23. [Integration Contract Definitions](#23-integration-contract-definitions)
24. [Deferred-to-Stage-5 Declarations](#24-deferred-to-stage-5-declarations)
25. [Sign-Off / Approval Record](#25-sign-off--approval-record)

---

## 1. Purpose & Scope

### 1.1 Purpose

This Technical Requirements Specification translates the approved Stage 3 Functional Requirements Specification into explicit technical requirements, interface definitions, data structures, state rules, and integration contracts for the App Management Centre (AMC).

The TRS defines **how the system must be technically structured and constrained** — without yet becoming a full architecture document. It establishes the technical boundaries that must be honored in Stage 5 Architecture and all downstream stages.

Every technical requirement stated here is bounded so that downstream Architecture (Stage 5) and QA-to-Red (Stage 6) agents can derive their work without guessing technical intent.

### 1.2 Scope

**In scope for Stage 4 TRS:**
- API and interface-level requirements (endpoint contracts, request/response shape requirements, transport security)
- Event and action contract definitions (action types, required fields, callback patterns)
- Data and state ownership rules at the schema-requirement level
- Schema-facing technical requirements (table names, required columns, index constraints, append-only enforcement)
- Integration requirements for AMC ↔ AIMC ↔ AIMCC ↔ KUC ↔ knowledge/memory system ↔ Foreman/agents
- Authentication and authorization enforcement requirements (Supabase Auth, JWT, RLS, token patterns)
- Degraded-mode technical behavior (what the system must do at the API/data/UI layer when dependencies are unavailable)
- Audit/provenance technical requirements (schema fields, append-only enforcement, cross-system linkage)
- State consistency and cross-device continuity requirements
- Mobile and real-time delivery requirements at the technical level

**Explicitly out of scope for Stage 4 TRS:**
- Full database schema definitions with column types and index DDL (Stage 5 Architecture / schema-builder)
- API code implementation (Stage 12 Build)
- Deployment infrastructure definitions (Stage 5 Architecture)
- Test specifications (Stage 6 QA-to-Red)
- UI component tree design (Stage 5 Architecture)
- CI/CD pipeline definitions (Stage 5 Architecture)

> FRS Traceability: §1 Purpose & Scope

---

## 2. Cross-System Technical Boundary Map

These boundaries are non-negotiable. They are reproduced here from Stage 1 and Stage 3 with technical elaboration. No TRS requirement may contradict or soften these boundaries.

> FRS Traceability: §2 Cross-System Boundary Rules; Stage 1 §1 Executive Layer Boundary Definitions

| System Layer | Technical Role | AMC Technical Interaction Pattern |
|---|---|---|
| **AMC** | React front-end + API layer. Owns executive state (alerts, approvals, interventions, audit, conversation, health events). Does not execute AI models. Does not own persistent knowledge truth | Writes to AMC-owned tables. Reads from external systems via governed API calls |
| **AIMC** | AI execution gateway service. Sole authorized AI model router | AMC calls AIMC REST/WebSocket API only. No direct model provider SDK calls from AMC application code |
| **AIMCC** | Knowledge ingestion and memory operations service | AMC calls AIMCC read API for status and provenance. AMC calls KUC API for upload submission — never AIMCC ingestion endpoints directly |
| **Knowledge Upload Centre (KUC)** | Governed knowledge upload entry point. REST API surface | AMC POSTs upload submissions exclusively to KUC API. AMC does not call AIMCC ingestion endpoints directly |
| **Knowledge / Memory System** | Persistent estate knowledge substrate | AMC calls governed knowledge query API with provenance requirement. AMC does not write to or cache knowledge records beyond transient session display |
| **Foreman** | Orchestration agent. Reporting source, intervention dispatch target | AMC reads Foreman reporting feed (read-only). AMC dispatches intervention orders to Foreman dispatch API |
| **Specialist Agents** | Domain-specific sandboxed workers | AMC receives status callbacks from specialist agents. AMC may dispatch termination orders through governed pathway |

**Non-bypass technical enforcement rules:**

| Rule | Technical Constraint |
|---|---|
| **TR-BOUNDARY-001** | AMC application code MUST NOT import or instantiate any AI model SDK (e.g., OpenAI SDK, Anthropic SDK). All AI calls must use the AIMC API client. Architecture must enforce this at the dependency level |
| **TR-BOUNDARY-002** | AMC application code MUST NOT call AIMCC internal ingestion endpoints. Upload submissions must POST to the KUC API base URL exclusively |
| **TR-BOUNDARY-003** | AMC MUST NOT maintain a local write-primary copy of knowledge/memory records. Transient display cache is permitted only with stale-detection TTL |
| **TR-BOUNDARY-004** | All external API calls from AMC MUST include a governed service-identity auth token in the Authorization header |

---

## 3. Technology Stack Constraints

The following technology constraints are established from approved Stage 1 and Stage 2 sources and confirmed at Stage 4. These constraints must be honored throughout Architecture (Stage 5) and Build (Stage 12).

| Layer | Constraint | Source Authority |
|---|---|---|
| **Authentication** | Supabase Auth. JWT-based session tokens. MFA capability required | FRS FR-1401; Stage 1 §25 |
| **Database** | Supabase (PostgreSQL). Row-Level Security (RLS) must be enabled for all tables containing executive or actor-specific data | FRS FR-1402; Stage 1 §25 |
| **Frontend framework** | React (inferred from estate stack; must be confirmed at Architecture stage) | Stage 1 §25; Deferred confirmation: §24 |
| **API pattern** | REST API with JSON payloads. HTTPS only. No unencrypted API calls | FRS FR-1504 |
| **Real-time / push** | WebSocket or Supabase Realtime subscription for live state updates (alert acknowledgments, intervention status, conversation messages). Polling fallback permitted for health data only | FRS FR-1204, FR-404, FR-803 |
| **Push notifications** | Native mobile push (FCM/APNs) or Progressive Web App push API for Critical alert interrupts | FRS FR-1202 |
| **Audit log persistence** | Append-only write pattern. No UPDATE on audit_events rows. Corrections are additive records | FRS FR-1301 |
| **Token storage** | JWT stored in secure, httpOnly cookie (preferred) or Supabase Auth session store. Not in localStorage for production | FRS FR-1401, FR-1402 |

---

## 4. TR-100: Executive Estate Oversight — Technical Requirements

> FRS Traceability: FR-101 to FR-104

### TR-101 — Dashboard API Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-101 |
| **FRS Source** | FR-101 |
| **Technical Requirement** | AMC backend must expose a `GET /api/dashboard/summary` endpoint. The response payload must include: (1) `health_domains[]` — array of five health domain objects, each with: `domain_id`, `label` (System Health / Execution Health / Governance Health / Security / Compliance), `status` (ok / warning / critical / unavailable), `updated_at`; (2) `alert_panel` — `critical_count`, `high_count`, `pending_acknowledgment_count`; (3) `approval_summary` — `pending_count`; (4) `intervention_summary` — `active_count`; (5) `proactive_panel` — `available` (boolean), `summary` (nullable string), `response_type`, `linked_action_ref` (nullable) |
| **Transport / Auth** | HTTPS. JWT auth required. No unauthenticated access |
| **Error Response** | On partial data fetch failure: return available fields with `status: "unavailable"` for missing domains; do not return HTTP 200 with incomplete data unmarked as partial. Return `partial: true` flag when any domain data is unavailable |
| **Deferred to Stage 5** | Health data aggregation logic (how each domain computes its status) |

### TR-102 — Health Domain Drill-Down API

| Field | Value |
|---|---|
| **Requirement ID** | TR-102 |
| **FRS Source** | FR-102 |
| **Technical Requirement** | AMC backend must expose `GET /api/dashboard/health/{domain_id}` returning domain-specific records for the selected health domain. If the domain data is unavailable: response must return `{ status: "unavailable", reason: "<explicit reason>" }` — not an empty array |
| **Transport / Auth** | HTTPS. JWT auth required |
| **Deferred to Stage 5** | Per-domain health record schema details |

### TR-103 — Proactive Summary AIMC Request Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-103 |
| **FRS Source** | FR-103 |
| **Technical Requirement** | AMC must dispatch a governed request to AIMC with action type `proactive_summary` on dashboard load and on background polling cycle (polling interval: configurable, default 60 seconds). Request payload to AIMC must include: `action_type: "proactive_summary"`, `session_id`, `requesting_actor: "system"`, `context: { surface: "executive_dashboard" }`. AIMC response must be surfaced with response type label "Observation". If AIMC returns an error or is unreachable: AMC must render the explicit "Maturion communication unavailable — AIMC unreachable" string — not an empty panel |
| **Audit Event** | `AIMC_REQUEST` with fields: actor, action_type, source, timestamp |
| **Deferred to Stage 5** | AIMC routing logic internal to AIMC |

### TR-104 — Navigation State Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-104 |
| **FRS Source** | FR-104 |
| **Technical Requirement** | AMC frontend router must define explicit named routes for each primary surface: `/dashboard`, `/alerts`, `/approvals`, `/interventions`, `/ai-actions`, `/aimcc-supervision`, `/knowledge`, `/conversation`, `/agent-oversight`, `/maintenance-reports`, `/estate-config`. Navigation must not depend on AIMC or AIMCC availability — routing failures must not silently leave the user on a blank route |
| **Deferred to Stage 5** | Route guard implementation details |

---

## 5. TR-200: Alert Management — Technical Requirements

> FRS Traceability: FR-201 to FR-209

### TR-201 — Alerts Table Schema Requirements

| Field | Value |
|---|---|
| **Requirement ID** | TR-201 |
| **FRS Source** | FR-201 to FR-209 |
| **Technical Requirement** | AMC database must define an `alerts` table with at minimum the following columns: `id` (UUID, primary key), `alert_class` (enum: critical / high / medium / low / informational), `source_system` (text), `summary` (text, NOT NULL), `created_at` (timestamptz, NOT NULL), `acknowledged_at` (timestamptz, nullable), `acknowledged_by` (text / actor ref, nullable), `escalated_at` (timestamptz, nullable), `escalation_target` (text, nullable), `escalation_type` (enum: manual / timeout, nullable), `dismissed_at` (timestamptz, nullable), `dismissed_by` (text, nullable), `dismiss_reason` (text, nullable), `linked_approval_id` (UUID, nullable FK → approvals), `linked_intervention_id` (UUID, nullable FK → interventions), `status` (enum: active / acknowledged / escalated / dismissed / resolved). RLS policy: only authenticated executive actor may read/write. Informational only: index on `alert_class` + `status` for priority ordering |
| **API Endpoint** | `GET /api/alerts` — ordered by: critical → high → medium → low → informational, then by `created_at` DESC. Must return `status: "error"` and explicit message if fetch fails — must not return empty array silently |
| **Real-Time** | Alert status changes (acknowledgment, escalation, dismissal) must be propagated via Supabase Realtime or WebSocket broadcast to connected AMC sessions |

### TR-202 — Alert Acknowledgment Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-202 |
| **FRS Source** | FR-203 |
| **Technical Requirement** | `POST /api/alerts/{alert_id}/acknowledge`. Request body: `{ actor_id, actor_type, basis }`. Endpoint must: (1) verify actor is authorized (Johan Ras or authorized Maturion delegate); (2) set `acknowledged_at` and `acknowledged_by` on the alert row; (3) write `ALERT_ACKNOWLEDGED` audit event; (4) return success with `{ acknowledged_at, audit_ref }`. If write fails: return HTTP 4xx/5xx — acknowledgment must not be shown as complete. If actor is unauthorized: return HTTP 403 with explicit rejection |

### TR-203 — Alert Escalation Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-203 |
| **FRS Source** | FR-204, FR-208 |
| **Technical Requirement** | `POST /api/alerts/{alert_id}/escalate`. Request body: `{ actor_id, actor_type, escalation_target, escalation_type }`. For manual escalation: write `ALERT_ESCALATED` audit event. For auto-escalation: background job fires at configurable timeout (default: 30 minutes for unacknowledged Critical alerts); writes `ALERT_ESCALATED_TIMEOUT` audit event with `escalation_type: "timeout"`. Background job must generate a system-level error alert if it itself fails |

### TR-204 — Alert Dismissal Enforcement Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-204 |
| **FRS Source** | FR-205 |
| **Technical Requirement** | `POST /api/alerts/{alert_id}/dismiss`. Server-side enforcement: if `alert_class` is critical, high, or medium — return HTTP 422 with body `{ error: "dismissal_not_permitted", reason: "Critical/High/Medium alerts may not be dismissed — must be acknowledged then resolved" }`. No client-side-only enforcement: server must reject independently of client-side UI hiding. Dismiss action requires non-empty `dismiss_reason` field |

### TR-205 — Alert-to-Approval Link Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-205 |
| **FRS Source** | FR-206 |
| **Technical Requirement** | `POST /api/alerts/{alert_id}/link-approval`. Creates approval record in `approvals` table with `source_alert_id` populated. Writes audit event `APPROVAL_CREATED_FROM_ALERT`. Returns `{ approval_id, approval_queue_url }`. If approval creation fails: HTTP 500 with explicit error — alert state must not be altered |

### TR-206 — Auto-Escalation Scheduler Technical Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-206 |
| **FRS Source** | FR-208 |
| **Technical Requirement** | A background scheduled job (Supabase Edge Function, cron, or equivalent) must run at minimum every 5 minutes. Query: SELECT alerts WHERE `alert_class = 'critical' AND acknowledged_at IS NULL AND created_at < (now() - escalation_timeout_interval)`. For each matched alert: execute escalation (write escalation fields, write `ALERT_ESCALATED_TIMEOUT` audit event). Scheduler failure must generate a new Critical alert in the `alerts` table with `source_system: "amc_scheduler"` |

---

## 6. TR-300: Approval Workflow — Technical Requirements

> FRS Traceability: FR-301 to FR-307

### TR-301 — Approvals Table Schema Requirements

| Field | Value |
|---|---|
| **Requirement ID** | TR-301 |
| **FRS Source** | FR-301 to FR-307 |
| **Technical Requirement** | AMC database must define an `approvals` table with at minimum: `id` (UUID, primary key), `approval_type` (text), `source_type` (enum: ai_action / governance_action / intervention / reserved_matter / aimcc_governance / manual), `source_alert_id` (UUID, nullable FK → alerts), `source_intervention_id` (UUID, nullable FK → interventions), `source_aimc_action_id` (UUID, nullable FK → aimc_action_log), `aimcc_context_id` (text, nullable), `authority_boundary_type` (enum: reserved_matter / delegated / operational), `status` (enum: pending / approved / rejected / deferred / cancelled), `deciding_actor` (text, nullable), `decided_at` (timestamptz, nullable), `approval_basis` (text, nullable — required on approve), `rejection_reason` (text, nullable — required on reject), `deferred_by` (text, nullable), `deferred_at` (timestamptz, nullable), `deferral_note` (text, nullable — required on defer), `follow_up_at` (timestamptz, nullable), `deadline` (timestamptz, nullable), `created_at` (timestamptz, NOT NULL), `downstream_action_ref` (text, nullable — reference to unblocked action) |

### TR-302 — Approval Decision API Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-302 |
| **FRS Source** | FR-303, FR-304 |
| **Technical Requirement** | `POST /api/approvals/{approval_id}/decide`. Request body: `{ decision: "approved" | "rejected" | "deferred", actor_id, actor_type, basis?, reason?, deferral_note?, follow_up_at? }`. Server-side enforcement rules: (1) `approval_basis` must be non-empty for `approved` decisions — return HTTP 422 if empty; (2) `rejection_reason` must be non-empty for `rejected` decisions — return HTTP 422 if empty; (3) `deferral_note` must be non-empty for `deferred` decisions; (4) `reserved_matter` authority boundary requires actor to be Johan Ras — return HTTP 403 if actor type is non-Johan on reserved matters; (5) decision must be idempotent against race condition: if already decided, return HTTP 409 with current decision state |

### TR-303 — Post-Approval Action Dispatch

| Field | Value |
|---|---|
| **Requirement ID** | TR-303 |
| **FRS Source** | FR-303 |
| **Technical Requirement** | On successful `approved` decision: AMC backend must dispatch the unblocked downstream action to the appropriate external service (AIMC, Foreman dispatch API, AIMCC governance endpoint) within the same transaction or in an atomic post-commit step. If downstream dispatch fails after the approval record is committed: the approval record must remain persisted with `status: approved`; a `downstream_dispatch_failed` flag must be set; an explicit error response returned to the user. The approval decision must not be rolled back due to downstream service unavailability |

### TR-304 — Approval Blocking Rule Enforcement

| Field | Value |
|---|---|
| **Requirement ID** | TR-304 |
| **FRS Source** | FR-307 |
| **Technical Requirement** | Any API endpoint that dispatches a governance-sensitive action must check for the existence of a pending or approved approval record before proceeding. Check implementation: query `approvals` table WHERE `downstream_action_ref = <action_id>` AND `status = 'pending'`. If pending approval exists: return HTTP 423 (Locked) with `{ blocked_by_approval: true, approval_id }`. This check must execute server-side — not client-side only |

---

## 7. TR-400: Intervention — Technical Requirements

> FRS Traceability: FR-401 to FR-407

### TR-401 — Interventions Table Schema Requirements

| Field | Value |
|---|---|
| **Requirement ID** | TR-401 |
| **FRS Source** | FR-401 to FR-407 |
| **Technical Requirement** | AMC database must define an `interventions` table with at minimum: `id` (UUID, primary key), `intervention_type` (text — from predefined catalogue or custom), `scope_target` (text — target system/agent/module), `scope_description` (text), `intended_outcome` (text), `authority_level` (enum: reserved_matter / delegated / operational), `initiator_actor` (text), `initiator_type` (enum: human / ai_executive / system), `status` (enum: pending_approval / queued / in_progress / completed / failed / cancelled / dispatch_failed), `approval_required` (boolean), `linked_approval_id` (UUID, nullable FK → approvals), `dispatched_at` (timestamptz, nullable), `executing_agent` (text, nullable), `dispatch_failed_at` (timestamptz, nullable), `completed_at` (timestamptz, nullable), `outcome` (text, nullable), `failed_at` (timestamptz, nullable), `failure_reason` (text, nullable), `cancelled_by` (text, nullable), `cancel_reason` (text, nullable — required on cancel), `cancelled_at` (timestamptz, nullable), `created_at` (timestamptz, NOT NULL), `source_alert_id` (UUID, nullable FK → alerts), `source_report_id` (text, nullable) |

### TR-402 — Intervention Dispatch API Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-402 |
| **FRS Source** | FR-403 |
| **Technical Requirement** | On dispatch: `POST /api/foreman/dispatch-intervention` (external call) OR `POST /api/specialist-agents/{agent_id}/dispatch` (external call). AMC must: (1) include governed auth token in Authorization header; (2) receive a synchronous acknowledgment (HTTP 202 Accepted) confirming the intervention entered a governed execution path; (3) update `interventions.status` to `in_progress` and set `dispatched_at` and `executing_agent`; (4) write `INTERVENTION_DISPATCHED` audit event. If dispatch returns non-2xx: set `status: dispatch_failed`, write audit event |

### TR-403 — Intervention Status Callback Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-403 |
| **FRS Source** | FR-404, FR-405, FR-406 |
| **Technical Requirement** | AMC must expose a callback endpoint: `POST /api/interventions/{intervention_id}/status-update`. Payload: `{ status: "in_progress" | "completed" | "failed", executing_agent, step_description?, outcome?, failure_reason?, timestamp }`. On receipt: (1) update `interventions` table row; (2) broadcast status update via Supabase Realtime to connected sessions viewing that intervention; (3) write relevant audit event (`INTERVENTION_COMPLETED` or `INTERVENTION_FAILED`). Callback endpoint must validate that the calling agent is the registered `executing_agent` for this intervention |

### TR-404 — Cancel Intervention Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-404 |
| **FRS Source** | FR-407 |
| **Technical Requirement** | `POST /api/interventions/{intervention_id}/cancel`. Request body: `{ actor_id, actor_type, cancel_reason }`. Server-side: `cancel_reason` must be non-empty — return HTTP 422 if empty. On success: (1) update `status: cancelled`, set `cancelled_by`, `cancel_reason`, `cancelled_at`; (2) dispatch abort signal to `executing_agent` if intervention is in_progress; (3) write `INTERVENTION_CANCELLED` audit event. If abort signal to executing agent fails: cancellation record must still be persisted; abort failure recorded as a separate `INTERVENTION_ABORT_SIGNAL_FAILED` event |

---

## 8. TR-500: AI-Routed Actions (AIMC) — Technical Requirements

> FRS Traceability: FR-501 to FR-504

### TR-501 — AIMC Action Log Schema Requirements

| Field | Value |
|---|---|
| **Requirement ID** | TR-501 |
| **FRS Source** | FR-501 to FR-504 |
| **Technical Requirement** | AMC database must define an `aimc_action_log` table with at minimum: `id` (UUID, primary key), `action_type` (text — e.g., `proactive_summary`, `conversation_message`, `governance_action`, `specialist_task`), `originating_actor` (text), `originating_actor_type` (enum: human / ai_executive / system / specialist_agent), `aimc_route_target` (text), `approval_required` (boolean), `linked_approval_id` (UUID, nullable FK → approvals), `dispatch_status` (enum: pending / dispatched / completed / failed / blocked_by_approval), `dispatched_at` (timestamptz, nullable), `aimc_ref` (text, nullable — AIMC-side reference), `result_summary` (text, nullable), `outcome` (enum: success / failure / error / pending, nullable), `completed_at` (timestamptz, nullable), `error_detail` (text, nullable), `created_at` (timestamptz, NOT NULL) |

### TR-502 — AIMC API Call Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-502 |
| **FRS Source** | FR-501, FR-503 |
| **Technical Requirement** | All AI action dispatches from AMC must call the AIMC base API URL (configurable environment variable `AIMC_API_BASE_URL`). AMC must NOT contain any import or invocation of direct model provider SDKs (OpenAI, Anthropic, Google Gemini, etc.). The Architecture stage must enforce this as a linting/dependency rule. AMC AIMC request format: `POST {AIMC_API_BASE_URL}/actions`. Headers: `Authorization: Bearer {service_token}`, `Content-Type: application/json`. Payload: `{ action_type, originating_actor, originating_actor_type, context, approval_status, amc_action_id }` |

### TR-503 — AIMC Callback Endpoint Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-503 |
| **FRS Source** | FR-502 |
| **Technical Requirement** | AMC must expose `POST /api/aimc/callback`. Payload: `{ amc_action_id, aimc_ref, outcome, result_summary, completed_at, error_detail? }`. On receipt: (1) update `aimc_action_log` row; (2) write `AIMC_ACTION_COMPLETED` audit event; (3) broadcast result to relevant surfaces via Supabase Realtime. AIMC callback endpoint must validate the calling service identity via shared service token before accepting |

### TR-504 — AIMC Non-Bypass Enforcement Technical Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-504 |
| **FRS Source** | FR-503 |
| **Technical Requirement** | Architecture must enforce: (1) `package.json` (or equivalent) must not list any model-provider SDK as a dependency; (2) any attempt to add such a dependency must be flagged by dependency scanning (enforceable via CI dependency gate); (3) if AMC detects a bypass attempt at runtime (e.g., an unexpected direct model call), it must write a `BOUNDARY_BYPASS_ATTEMPTED` event to `audit_events` with `severity: critical` and surface a Critical alert |

---

## 9. TR-600: AIMCC / Knowledge Upload Centre Supervision — Technical Requirements

> FRS Traceability: FR-601 to FR-605

### TR-601 — AIMCC Status Read API Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-601 |
| **FRS Source** | FR-601, FR-602, FR-603 |
| **Technical Requirement** | AMC must call `GET {AIMCC_API_BASE_URL}/uploads/status` to fetch active and recent upload items. The AIMCC API response must provide per-upload: `id`, `document_name`, `submitter`, `submitted_at`, `kuc_receipt_status`, `ingestion_state`, `outcome`, `aimcc_tracking_ref`. AMC must surface this as read-only; AMC must not write to AIMCC upload records. If AIMCC is unreachable: AMC surfaces previously-fetched data with `stale: true` indicator and `stale_since: <timestamp>` — not silently presenting stale data as current |

### TR-602 — Quota Data Read Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-602 |
| **FRS Source** | FR-603 |
| **Technical Requirement** | AMC must call `GET {AIMCC_API_BASE_URL}/quota/current` to fetch upload quota state. Expected response fields: `current_quota`, `used`, `usage_percentage`, `threshold_warning_level` (enum: ok / warning / critical), `approved_change_pending` (boolean). AMC must store last-known quota values locally with a TTL cache; on AIMCC degraded mode: display last-known values with explicit stale indicator |

### TR-603 — AIMCC Governance Action Creation Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-603 |
| **FRS Source** | FR-604 |
| **Technical Requirement** | When a governance action is required (quota change request, content flag): `POST /api/approvals` with `source_type: "aimcc_governance"` and `aimcc_context_id` populated. On approval decision: `POST {AIMCC_API_BASE_URL}/governance/decision` with `{ aimcc_context_id, decision, decided_by, decided_at, basis }`. Headers: governed service token. If AIMCC is unavailable: governance action approval decision must be queued; AIMCC must be notified on recovery — not auto-processed |

### TR-604 — KUC Non-Bypass Technical Enforcement

| Field | Value |
|---|---|
| **Requirement ID** | TR-604 |
| **FRS Source** | FR-605 |
| **Technical Requirement** | Any knowledge upload submission from AMC context must POST to `{KUC_API_BASE_URL}/submit` exclusively. Architecture must prevent any direct call to AIMCC ingestion endpoints from AMC code. If a bypass is detected at runtime: write `BOUNDARY_BYPASS_ATTEMPTED` event to `audit_events` |

---

## 10. TR-700: Memory-Aware / Knowledge-Aware View — Technical Requirements

> FRS Traceability: FR-701 to FR-703

### TR-701 — Knowledge Retrieval API Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-701 |
| **FRS Source** | FR-701 |
| **Technical Requirement** | AMC must call `POST {KNOWLEDGE_API_BASE_URL}/retrieve` with payload: `{ query, requesting_actor, requesting_actor_type, session_id, require_provenance: true }`. Response must include per-result: `id`, `content_summary`, `source_document`, `ingestion_date`, `aimcc_tracking_ref`, `confidence_indicator`, `retrieval_timestamp`. AMC must enforce `require_provenance: true` — anonymous knowledge references without provenance are prohibited from rendering. AMC must write `KNOWLEDGE_RETRIEVED` audit event |

### TR-702 — Knowledge Retrieval Log Schema Requirements

| Field | Value |
|---|---|
| **Requirement ID** | TR-702 |
| **FRS Source** | FR-701, FR-702 |
| **Technical Requirement** | AMC database must define a `knowledge_retrieval_log` table with: `id` (UUID, primary key), `actor` (text), `actor_type` (text), `query_summary` (text), `result_count` (integer), `source_refs` (jsonb — array of source refs), `retrieval_timestamp` (timestamptz), `knowledge_system_ref` (text, nullable). No write access to the knowledge/memory system by AMC — read only |

### TR-703 — Knowledge Non-Ownership Enforcement

| Field | Value |
|---|---|
| **Requirement ID** | TR-703 |
| **FRS Source** | FR-703 |
| **Technical Requirement** | AMC MUST NOT define any database table that stores persistent knowledge/memory content as AMC-canonical truth. The `knowledge_retrieval_log` stores retrieval metadata only, not knowledge content. Any in-memory or Redis-style cache of retrieved knowledge must have a maximum TTL of 5 minutes and must include stale-at timestamp. Cache invalidation on knowledge system degradation: immediately mark all cached items as stale. Architecture must enforce: no table with column names implying knowledge ownership (e.g., no `knowledge_content`, `memory_record`, `fact_store` tables owned by AMC) |

---

## 11. TR-800: Executive Conversation — Technical Requirements

> FRS Traceability: FR-801 to FR-807

### TR-801 — Conversation Messages Table Schema Requirements

| Field | Value |
|---|---|
| **Requirement ID** | TR-801 |
| **FRS Source** | FR-801 to FR-807 |
| **Technical Requirement** | AMC database must define a `conversation_messages` table with: `id` (UUID, primary key), `session_id` (text — ties to auth session or conversation thread), `message_text` (text, NOT NULL), `sender_actor` (text), `sender_actor_type` (enum: human / ai_executive / system), `response_type` (enum: Observation / Recommendation / Request / Decision / Alert — required for AI messages, nullable for human messages), `aimc_ref` (text, nullable), `linked_approval_id` (UUID, nullable FK → approvals), `linked_alert_id` (UUID, nullable FK → alerts), `linked_intervention_id` (UUID, nullable FK → interventions), `acknowledged_at` (timestamptz, nullable), `acknowledged_by` (text, nullable), `is_proactive` (boolean, default false), `priority` (enum: normal / high / critical, nullable), `created_at` (timestamptz, NOT NULL). Index: `session_id` + `created_at` for conversation load |

### TR-802 — Conversation API Contracts

| Field | Value |
|---|---|
| **Requirement ID** | TR-802 |
| **FRS Source** | FR-801, FR-802 |
| **Technical Requirement** | `GET /api/conversation/messages?limit=N&before=<timestamp>` — paginated conversation history load. `POST /api/conversation/messages` — send user message. Payload: `{ message_text, session_id, actor_id, actor_type }`. On success: (1) persist to `conversation_messages`; (2) dispatch to AIMC via `TR-502` AIMC API call with action_type `conversation_message`; (3) return `{ message_id, dispatched_to_aimc: boolean, aimc_dispatch_error? }`. If AIMC dispatch fails: message is persisted; response includes `{ dispatched_to_aimc: false, aimc_dispatch_error: "<reason>" }` |

### TR-803 — AIMC Conversation Callback Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-803 |
| **FRS Source** | FR-803, FR-806 |
| **Technical Requirement** | AIMC delivers Maturion conversation responses to `POST /api/aimc/conversation-callback`. Payload must include: `{ amc_message_id, response_text, response_type, aimc_ref, linked_action_refs?: [] }`. `response_type` must be one of: Observation / Recommendation / Request / Decision / Alert. If `response_type` is absent or unrecognized: AMC must persist the message with `response_type: "unknown"` and render it with explicit "type unavailable" indicator — not suppress or default to "Decision" |

### TR-804 — Proactive Message Push Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-804 |
| **FRS Source** | FR-804 |
| **Technical Requirement** | AIMC may push proactive Maturion messages to AMC via `POST /api/aimc/proactive-message`. Payload: `{ message_text, response_type, priority, linked_action_refs?: [], alert_class? }`. AMC must: (1) persist to `conversation_messages` with `is_proactive: true`; (2) if `alert_class` is present: also create an alert record in `alerts` table; (3) broadcast to connected sessions via Supabase Realtime; (4) write `PROACTIVE_MESSAGE_RECEIVED` audit event |

### TR-805 — Cross-Device Conversation Continuity

| Field | Value |
|---|---|
| **Requirement ID** | TR-805 |
| **FRS Source** | FR-805 |
| **Technical Requirement** | Conversation state must be stored server-side in `conversation_messages` table (not client-local state only). Any connected session (mobile or desktop) must subscribe to the same `conversation_messages` Supabase Realtime channel filtered by `session_id`. Realtime subscription must deliver message acknowledgment events across devices within 2 seconds of the write |

---

## 12. TR-900: Specialist Agent Workspace Oversight — Technical Requirements

> FRS Traceability: FR-901 to FR-904

### TR-901 — Workspace Status API Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-901 |
| **FRS Source** | FR-901, FR-902 |
| **Technical Requirement** | AMC must call `GET {SPECIALIST_AGENT_API_BASE_URL}/workspaces` for workspace status (or equivalent Foreman reporting feed). Per-workspace response: `id`, `name`, `agent_type`, `scope_boundary`, `current_status` (enum: idle / active / error / terminated), `active_tasks_count`, `last_reporting_event`, `sandbox_isolation_indicator` (boolean — must always be present). AMC must display sandbox_isolation_indicator on all workspace list and detail views. AMC must not request or display internal specialist agent state — only outcomes |

### TR-902 — Workspace Termination Approval Gate

| Field | Value |
|---|---|
| **Requirement ID** | TR-902 |
| **FRS Source** | FR-904 |
| **Technical Requirement** | `POST /api/workspaces/{workspace_id}/terminate` must first check `authority_level` of the workspace. If reserved-matter or authority-sensitive: create an approval record (`source_type: "workspace_termination"`) and return `{ blocked_by_approval: true, approval_id }` — do not dispatch termination until approval is recorded. On approval: `POST {SPECIALIST_AGENT_API_BASE_URL}/workspaces/{workspace_id}/terminate` with governed auth token |

---

## 13. TR-1000: Maintenance & Assurance Reporting — Technical Requirements

> FRS Traceability: FR-1001 to FR-1004

### TR-1001 — Reports Surface API Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-1001 |
| **FRS Source** | FR-1001, FR-1002 |
| **Technical Requirement** | `GET /api/reports` — returns all maintenance and assurance report items. Per-item required fields: `id`, `report_type` (enum: maintenance / iaa_assurance), `agent_id`, `findings_summary`, `severity` (enum: all_clear / advisory / warning / critical), `recommended_action`, `evidence_ref`, `run_at` (timestamptz). IAA reports (report_type: iaa_assurance) must be returnable as a filtered subset separately from maintenance reports — API must support `?type=iaa_assurance` and `?type=maintenance` query parameters |

### TR-1002 — Critical Finding Alert Auto-Generation

| Field | Value |
|---|---|
| **Requirement ID** | TR-1002 |
| **FRS Source** | FR-1003 |
| **Technical Requirement** | On receipt of any report with `severity: critical`: AMC backend must automatically create an alert record in `alerts` with `alert_class: critical`, `source_system: <originating_agent_id>`, `summary: <findings_summary>`, `linked_report_id: <report.id>`. If alert creation fails: write `REPORT_ALERT_CREATION_FAILED` system error event to audit log — critical finding must remain visible in reports surface |

---

## 14. TR-1100: Estate Configuration & Wellbeing — Technical Requirements

> FRS Traceability: FR-1101 to FR-1103

### TR-1101 — Foreman Reporting Feed Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-1101 |
| **FRS Source** | FR-1101, FR-1103 |
| **Technical Requirement** | AMC reads Foreman reporting data from `GET {FOREMAN_API_BASE_URL}/reporting/build-status` (or equivalent Foreman event feed). AMC renders this data read-only — AMC must not call any Foreman command endpoint (no start build, no build control). Response expected: `active_jobs[]`, each with: `job_id`, `stage`, `status`, `started_at`, `assigned_agent`. If Foreman feed is unavailable: display `{ status: "unavailable", last_known_at: <timestamp> }` per job — not empty or silently stale |

### TR-1102 — Configuration Change Approval Enforcement

| Field | Value |
|---|---|
| **Requirement ID** | TR-1102 |
| **FRS Source** | FR-1102 |
| **Technical Requirement** | Configuration values are read-only in the database from AMC's perspective — no `UPDATE` on estate configuration rows is permitted without a completed approval record. API: `POST /api/estate-config/request-change` creates an approval record with `authority_boundary_type: reserved_matter`. On approval: dispatch configuration change to appropriate governed service. Configuration must remain unchanged if approval is outstanding |

---

## 15. TR-1200: Mobile Continuity — Technical Requirements

> FRS Traceability: FR-1201 to FR-1204

### TR-1201 — Mobile Responsive Layout Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-1201 |
| **FRS Source** | FR-1201 |
| **Technical Requirement** | AMC frontend must implement responsive breakpoints that produce a distinct mobile layout at ≤768px viewport width. Mobile layout must: (1) surface critical and high alerts immediately on load without scroll; (2) render Approve/Reject controls without horizontal scroll; (3) not hide functional surfaces behind scrollable containers that obscure active alerts. Mobile layout is not a visual mirror of desktop — it must expose executive actions |

### TR-1202 — Critical Alert Push Notification Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-1202 |
| **FRS Source** | FR-1202 |
| **Technical Requirement** | On `alert_class: critical` alert creation: AMC backend must dispatch a push notification via configured push provider (FCM for Android, APNs for iOS, or PWA Push API for web). Push notification payload: `{ title: "Critical Alert", body: <summary>, deep_link: "/alerts/{alert_id}" }`. If push notification dispatch fails: the failure must be recorded but must not block alert creation. On next AMC app open: in-app alert banner must display outstanding unacknowledged critical alerts — this fallback is mandatory |

### TR-1203 — Cross-Device State Synchronization Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-1203 |
| **FRS Source** | FR-1204 |
| **Technical Requirement** | All state writes that affect shared executive context (alert acknowledgment, approval decision, intervention status change, conversation messages) must propagate via Supabase Realtime to all connected sessions authenticated as the same user. Realtime subscription channel: `amc_executive_state_{user_id}`. Contradictory state between sessions must produce a client-side stale detection: if local state diverges from a received Realtime event, the Realtime event is authoritative and the UI must update |

---

## 16. TR-1300: Audit & Provenance — Technical Requirements

> FRS Traceability: FR-1301 to FR-1304

### TR-1301 — Audit Events Table Schema Requirements

| Field | Value |
|---|---|
| **Requirement ID** | TR-1301 |
| **FRS Source** | FR-1301 |
| **Technical Requirement** | AMC database must define an `audit_events` table with at minimum: `id` (UUID, primary key), `event_type` (text, NOT NULL — see TR-1302 required event types), `actor` (text, NOT NULL), `actor_type` (enum: human / ai_executive / orchestration / assurance / specialist / system / service), `source_system` (text, NOT NULL), `object_type` (text — entity type affected), `object_id` (text — entity ID affected), `action` (text, NOT NULL), `state_before` (jsonb, nullable), `state_after` (jsonb, nullable), `state_transition` (text, nullable), `outcome` (enum: success / failure / partial / pending, NOT NULL), `approval_basis` (text, nullable), `timestamp` (timestamptz, NOT NULL), `cross_system_ref` (text, nullable — TR-1304), `session_id` (text, nullable), `metadata` (jsonb, nullable). **Hard constraint**: NO UPDATE or DELETE is permitted on this table. RLS policy: audit_events are append-only. Corrections must insert a new row with `event_type: correction_record` referencing the original `id` |

### TR-1302 — Required Audit Event Types

| Field | Value |
|---|---|
| **Requirement ID** | TR-1302 |
| **FRS Source** | FR-1302 |
| **Technical Requirement** | The `audit_events` table must receive events for the following event_type values (minimum). Architecture must confirm all are wired before Stage 6 QA-to-Red: `ALERT_ACKNOWLEDGED`, `ALERT_ESCALATED`, `ALERT_ESCALATED_TIMEOUT`, `ALERT_DISMISSED`, `APPROVAL_CREATED_FROM_ALERT`, `INTERVENTION_CREATED_FROM_ALERT`, `APPROVAL_DECIDED`, `APPROVAL_DEFERRED`, `CLARIFICATION_REQUESTED`, `INTERVENTION_INITIATED`, `INTERVENTION_DISPATCHED`, `INTERVENTION_COMPLETED`, `INTERVENTION_CANCELLED`, `INTERVENTION_FAILED`, `INTERVENTION_ABORT_SIGNAL_FAILED`, `AIMC_REQUEST`, `AIMC_ACTION_INITIATED`, `AIMC_ACTION_COMPLETED`, `AIMC_DEGRADED`, `AIMC_RECOVERED`, `AIMCC_DEGRADED`, `AIMCC_GOVERNANCE_ACTION_CREATED`, `KNOWLEDGE_RETRIEVED`, `KNOWLEDGE_SYSTEM_DEGRADED`, `AUTH_LOGIN`, `AUTH_LOGIN_FAILED`, `AUTH_SESSION_EXPIRED`, `UNAUTHORIZED_ACCESS_ATTEMPT`, `PROACTIVE_MESSAGE_RECEIVED`, `CONVERSATION_MESSAGE_SENT`, `CONVERSATION_RESPONSE_RECEIVED`, `MESSAGE_ACKNOWLEDGED`, `BOUNDARY_BYPASS_ATTEMPTED`, `REPORT_ALERT_CREATION_FAILED`, `CORRECTION_RECORD` |

### TR-1303 — Audit Accessibility API Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-1303 |
| **FRS Source** | FR-1303 |
| **Technical Requirement** | `GET /api/audit-events` must support query parameters: `?actor=<actor>`, `?event_type=<type>`, `?source_system=<system>`, `?from=<ISO8601>`, `?to=<ISO8601>`, `?object_id=<id>`. Response must be paginated (default page size: 50, max: 200). RLS: Johan Ras and IAA-type actors may query audit_events within their authorized scope. Service-system-only events must require elevated service role — not accessible via user JWT |

### TR-1304 — Cross-System Audit Linkage

| Field | Value |
|---|---|
| **Requirement ID** | TR-1304 |
| **FRS Source** | FR-1304 |
| **Technical Requirement** | For any AMC event that triggers downstream execution in AIMC, AIMCC, Foreman, or specialist agents: the AMC-side audit event must populate `cross_system_ref` with the external service reference ID (e.g., AIMC action ID, Foreman job ID, AIMCC tracking ref). If cross-system reference is not available at audit write time: write event with `cross_system_ref: null` and `event_type` suffix `_CROSS_REF_PENDING`. When the cross-system ref becomes available (via callback): write a `CORRECTION_RECORD` event referencing the original and providing `cross_system_ref` |

---

## 17. TR-1400: Authentication & Authorization — Technical Requirements

> FRS Traceability: FR-1401 to FR-1403

### TR-1401 — Supabase Auth Configuration Requirements

| Field | Value |
|---|---|
| **Requirement ID** | TR-1401 |
| **FRS Source** | FR-1401 |
| **Technical Requirement** | Authentication must use Supabase Auth. Required configuration: (1) email/password provider enabled; (2) MFA (TOTP) support enabled — not mandatory per-session, but must be configurable per-user; (3) JWT expiry: configurable, default ≤4 hours for executive sessions; (4) JWT stored in httpOnly cookie (not localStorage) for web sessions; (5) failed login must trigger `AUTH_LOGIN_FAILED` audit event; (6) session expiry must trigger `AUTH_SESSION_EXPIRED` audit event; (7) unauthorized access attempt must trigger `UNAUTHORIZED_ACCESS_ATTEMPT` audit event. Auth service unavailability must not produce a fallback that allows unauthenticated access — explicit "service unavailable" must be shown |

### TR-1402 — Row-Level Security Policy Requirements

| Field | Value |
|---|---|
| **Requirement ID** | TR-1402 |
| **FRS Source** | FR-1402 |
| **Technical Requirement** | All AMC tables containing executive-visible or actor-specific data must have Supabase RLS policies enabled. Required RLS policies (minimum): (1) `alerts`: readable and writable only by authenticated executive actor; (2) `approvals`: readable only by authorized actor; writable only by authorized deciding actor; (3) `interventions`: readable/writable by authorized actor; (4) `audit_events`: insert permitted for service role; SELECT for executive actors (filtered by scope); no DELETE, no UPDATE; (5) `conversation_messages`: readable/writable by session owner. Service-to-service calls (AIMC callbacks, Foreman callbacks) must use Supabase service_role token — not user JWT |

### TR-1403 — Identity Separation Technical Enforcement

| Field | Value |
|---|---|
| **Requirement ID** | TR-1403 |
| **FRS Source** | FR-1403 |
| **Technical Requirement** | The following actor identity types must be distinguishable in all database records and audit events via `actor_type` column: `human` (Johan Ras human login), `ai_executive` (Maturion via AIMC), `orchestration` (Foreman), `assurance` (IAA agents), `specialist` (specialist agents), `system` (AMC background jobs, scheduler), `service` (external service callbacks). No single-actor-type `user` field that collapses all types. Actor identity is resolved at the API layer based on JWT claims or service token metadata — not passed freely by callers |

### TR-1404 — Authority-Domain Enforcement Technical Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-1404 |
| **FRS Source** | FR-1402 |
| **Technical Requirement** | AMC backend must implement authority-domain checks as middleware or service-layer guards that execute server-side for every consequential action endpoint. Required checks: (1) `reserved_matter` authority boundary → actor must resolve to `human` type with Johan Ras identity claim; (2) `delegated` authority boundary → actor must resolve to `ai_executive` type within approved delegated scope configuration; (3) `operational` boundary → authenticated executive actor permitted. These checks must be enforced independently of client-side UI visibility — server must reject regardless of what the UI presented to the actor |

---

## 18. TR-1500: Cross-System Integration — Technical Requirements

> FRS Traceability: FR-1501 to FR-1504

### TR-1501 — AIMC Health Check Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-1501 |
| **FRS Source** | FR-1501 |
| **Technical Requirement** | AMC must poll `GET {AIMC_API_BASE_URL}/health` at configurable interval (default: 30 seconds). Expected response: HTTP 200 with `{ status: "healthy" | "degraded" | "unavailable" }`. On non-200 or unavailable status: enter AIMC degraded mode immediately (write `AIMC_DEGRADED` audit event, update `system_health_events`, broadcast via Supabase Realtime). On recovery detection (next successful health check): write `AIMC_RECOVERED` event; exit degraded mode |

### TR-1502 — AIMCC Health Check Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-1502 |
| **FRS Source** | FR-1502 |
| **Technical Requirement** | AMC must poll `GET {AIMCC_API_BASE_URL}/health` at configurable interval (default: 30 seconds). On non-200 or unavailable: enter AIMCC degraded mode (write `AIMCC_DEGRADED` audit event). Recovery detection: as per AIMC pattern |

### TR-1503 — Knowledge System Health Check Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-1503 |
| **FRS Source** | FR-1503 |
| **Technical Requirement** | AMC must poll `GET {KNOWLEDGE_API_BASE_URL}/health` at configurable interval (default: 30 seconds). On non-200 or unavailable: enter knowledge system degraded mode (write `KNOWLEDGE_SYSTEM_DEGRADED` audit event). All cached knowledge items must be immediately marked stale |

### TR-1504 — Service Token Management for External Calls

| Field | Value |
|---|---|
| **Requirement ID** | TR-1504 |
| **FRS Source** | FR-1504 |
| **Technical Requirement** | AMC must maintain a service-identity token for each external dependency (AIMC, AIMCC, KUC, knowledge/memory system, Foreman, specialist agents). Token configuration: environment variables (`AIMC_SERVICE_TOKEN`, `AIMCC_SERVICE_TOKEN`, `KUC_SERVICE_TOKEN`, `KNOWLEDGE_SERVICE_TOKEN`, `FOREMAN_SERVICE_TOKEN`). Tokens must not be hardcoded in application source. Every outbound API call must include `Authorization: Bearer {service_token}` in headers. If token is absent or invalid: call must be blocked; error written to audit log |

### TR-1505 — External API Base URL Configuration

| Field | Value |
|---|---|
| **Requirement ID** | TR-1505 |
| **FRS Source** | FR-1501 to FR-1504 |
| **Technical Requirement** | All external service base URLs must be environment-variable-configured: `AIMC_API_BASE_URL`, `AIMCC_API_BASE_URL`, `KUC_API_BASE_URL`, `KNOWLEDGE_API_BASE_URL`, `FOREMAN_API_BASE_URL`. Hardcoded service URLs are prohibited. Architecture must confirm that URL injection is validated at startup — missing required URL configuration must prevent application startup with explicit startup error |

---

## 19. TR-1600: Degraded-Mode — Technical Requirements

> FRS Traceability: FR-1601 to FR-1603

### TR-1601 — System Health Events Table Schema Requirements

| Field | Value |
|---|---|
| **Requirement ID** | TR-1601 |
| **FRS Source** | FR-1601 to FR-1603 |
| **Technical Requirement** | AMC database must define a `system_health_events` table with: `id` (UUID, primary key), `dependency` (enum: aimc / aimcc / knowledge_system / foreman / specialist_agents / amc_scheduler), `event_type` (enum: degraded / recovered / health_check_failed), `detected_at` (timestamptz, NOT NULL), `recovered_at` (timestamptz, nullable), `impact_summary` (text), `audit_event_ref` (UUID, FK → audit_events). RLS: executive-readable, system-writable |

### TR-1602 — AIMC Degraded Mode Technical Behavior

| Field | Value |
|---|---|
| **Requirement ID** | TR-1602 |
| **FRS Source** | FR-1601 |
| **Technical Requirement** | On AIMC degraded mode entry: (1) `system_health_events` row inserted; (2) `AIMC_DEGRADED` audit event written; (3) Supabase Realtime broadcast to all connected sessions: `{ event: "system_degraded", dependency: "aimc", detected_at }`; (4) all pending `aimc_action_log` dispatch attempts must return `{ blocked: true, reason: "aimc_degraded" }` — no queue overflow into fallback paths; (5) `POST /api/aimc/*` endpoints must return HTTP 503 with body `{ error: "aimc_unavailable" }` while degraded; (6) Maturion Proactive Panel must render the required exact string: "Maturion communication unavailable — AIMC unreachable" |

### TR-1603 — AIMCC Degraded Mode Technical Behavior

| Field | Value |
|---|---|
| **Requirement ID** | TR-1603 |
| **FRS Source** | FR-1602 |
| **Technical Requirement** | On AIMCC degraded mode entry: (1) `system_health_events` row inserted; (2) `AIMCC_DEGRADED` audit event written; (3) Realtime broadcast to sessions; (4) all AIMCC quota/upload read calls return last cached data with `stale: true, stale_since: <detected_at>`; (5) AIMCC governance actions that require AIMCC availability remain in `pending` state — no auto-approval or auto-rejection; (6) Upload submission attempts via KUC must be queued locally with `{ queued_for_retry: true, reason: "aimcc_degraded" }` — not silently dropped |

### TR-1604 — Knowledge System Degraded Mode Technical Behavior

| Field | Value |
|---|---|
| **Requirement ID** | TR-1604 |
| **FRS Source** | FR-1603 |
| **Technical Requirement** | On knowledge system degraded mode entry: (1) `system_health_events` row inserted; (2) `KNOWLEDGE_SYSTEM_DEGRADED` audit event written; (3) all cached knowledge items' stale flags set immediately; (4) knowledge retrieval endpoints return HTTP 503 with `{ error: "knowledge_system_unavailable" }` — not empty arrays; (5) any surface showing knowledge references must display the stale/unavailable indicator |

---

## 20. TR-1700: State & Persistence — Technical Requirements

> FRS Traceability: FR-1701 to FR-1703

### TR-1701 — Canonical State Ownership Table

The following table defines the authoritative technical state ownership for AMC. Architecture and schema-builder must enforce this.

| State Domain | Canonical Owner | AMC Write Access | AMC Read Access | Notes |
|---|---|---|---|---|
| `alerts` table | AMC | Full (INSERT, UPDATE) | Full | RLS enforced |
| `approvals` table | AMC | Full (INSERT, UPDATE) | Full | RLS enforced |
| `interventions` table | AMC | Full (INSERT, UPDATE) | Full | RLS enforced |
| `audit_events` table | AMC | Append-only (INSERT only) | Filtered SELECT | No UPDATE, no DELETE. Corrections via insert only |
| `conversation_messages` table | AMC | Full (INSERT, UPDATE for ack) | Full | Session-scoped |
| `aimc_action_log` table | AMC | Full (INSERT, UPDATE on callback) | Full | |
| `knowledge_retrieval_log` table | AMC | Full (INSERT) | Full | No knowledge content stored |
| `system_health_events` table | AMC | Full (INSERT, UPDATE on recovery) | Full | |
| `knowledge_upload_records` (AIMCC) | AIMCC | None (read via AIMCC API) | AIMCC read API only | AMC does not write to this |
| `knowledge/memory content` (Knowledge/Memory System) | Knowledge/Memory System | None | Governed read API only | AMC does not store canonical knowledge |

### TR-1702 — State Consistency Technical Enforcement

| Field | Value |
|---|---|
| **Requirement ID** | TR-1702 |
| **FRS Source** | FR-1702 |
| **Technical Requirement** | All state mutations (alert acknowledgment, approval decision, intervention status change) must propagate via Supabase Realtime to all connected sessions. Realtime channel: `amc_executive_state_{user_id}`. Frontend must subscribe on mount and unsubscribe on unmount. On receiving a Realtime update: the local state in all affected components must be updated immediately — no stale-while-revalidate pattern that could surface contradictory states without explicit staleness indicator |

### TR-1703 — Session Restore Contract

| Field | Value |
|---|---|
| **Requirement ID** | TR-1703 |
| **FRS Source** | FR-1703 |
| **Technical Requirement** | On session restore (user returns to AMC): AMC frontend must fetch current state from server APIs (not local cache only): (1) `GET /api/dashboard/summary` for current health state; (2) `GET /api/alerts?status=active` for current alert state; (3) `GET /api/approvals?status=pending` for approval queue; (4) `GET /api/interventions?status=active` for intervention state; (5) `GET /api/conversation/messages?limit=20` for conversation history. If any fetch fails: explicit error indicator — not silently using last-known local state as current |

---

## 21. API / Interface Contract Summary

This section summarises all API endpoints defined in this TRS. Architecture (Stage 5) must implement every endpoint in this list. Deviations require CS2 approval.

### 21.1 AMC Internal API Endpoints

| Endpoint | Method | TR Reference | Purpose |
|---|---|---|---|
| `/api/dashboard/summary` | GET | TR-101 | Executive dashboard data |
| `/api/dashboard/health/{domain_id}` | GET | TR-102 | Health domain drill-down |
| `/api/alerts` | GET | TR-201 | Alert list (priority-ordered) |
| `/api/alerts/{id}/acknowledge` | POST | TR-202 | Acknowledge alert |
| `/api/alerts/{id}/escalate` | POST | TR-203 | Escalate alert |
| `/api/alerts/{id}/dismiss` | POST | TR-204 | Dismiss alert (Low/Info only) |
| `/api/alerts/{id}/link-approval` | POST | TR-205 | Link alert to approval |
| `/api/approvals` | GET | TR-301 | Approval queue |
| `/api/approvals` | POST | TR-303, TR-603 | Create approval |
| `/api/approvals/{id}/decide` | POST | TR-302 | Approve/reject/defer |
| `/api/interventions` | GET | TR-401 | Intervention list |
| `/api/interventions` | POST | TR-401 | Create intervention |
| `/api/interventions/{id}/cancel` | POST | TR-404 | Cancel intervention |
| `/api/interventions/{id}/status-update` | POST | TR-403 | Status callback (from executing agent) |
| `/api/workspaces/{id}/terminate` | POST | TR-902 | Terminate workspace (approval-gated) |
| `/api/estate-config/request-change` | POST | TR-1102 | Request config change (approval-gated) |
| `/api/conversation/messages` | GET | TR-802 | Conversation history |
| `/api/conversation/messages` | POST | TR-802 | Send user message |
| `/api/reports` | GET | TR-1001 | Maintenance/assurance reports |
| `/api/audit-events` | GET | TR-1303 | Audit log access |

### 21.2 AMC Inbound Callback Endpoints

| Endpoint | Method | TR Reference | Caller |
|---|---|---|---|
| `/api/aimc/callback` | POST | TR-503 | AIMC |
| `/api/aimc/conversation-callback` | POST | TR-803 | AIMC |
| `/api/aimc/proactive-message` | POST | TR-804 | AIMC |
| `/api/interventions/{id}/status-update` | POST | TR-403 | Foreman / Specialist Agent |

### 21.3 AMC Outbound API Calls

| Target | Endpoint Pattern | TR Reference | Purpose |
|---|---|---|---|
| AIMC | `POST {AIMC_API_BASE_URL}/actions` | TR-502 | All AI action dispatches |
| AIMC | `GET {AIMC_API_BASE_URL}/health` | TR-1501 | Health polling |
| AIMCC | `GET {AIMCC_API_BASE_URL}/uploads/status` | TR-601 | Upload status read |
| AIMCC | `GET {AIMCC_API_BASE_URL}/quota/current` | TR-602 | Quota read |
| AIMCC | `POST {AIMCC_API_BASE_URL}/governance/decision` | TR-603 | Governance decision notification |
| AIMCC | `GET {AIMCC_API_BASE_URL}/health` | TR-1502 | Health polling |
| KUC | `POST {KUC_API_BASE_URL}/submit` | TR-604 | Upload submission |
| Knowledge System | `POST {KNOWLEDGE_API_BASE_URL}/retrieve` | TR-701 | Knowledge retrieval |
| Knowledge System | `GET {KNOWLEDGE_API_BASE_URL}/health` | TR-1503 | Health polling |
| Foreman | `GET {FOREMAN_API_BASE_URL}/reporting/build-status` | TR-1101 | Build status read |
| Foreman | `POST {FOREMAN_API_BASE_URL}/dispatch-intervention` | TR-402 | Intervention dispatch |
| Specialist Agent | `POST {SPECIALIST_AGENT_API_BASE_URL}/workspaces/{id}/terminate` | TR-902 | Workspace termination |

---

## 22. Data Schema Requirements Summary

This section summarises all tables AMC must own. Column types and index DDL are deferred to Stage 5 Architecture (schema-builder).

| Table | AMC Write Rule | Key Constraints | TR Reference |
|---|---|---|---|
| `alerts` | INSERT + UPDATE | RLS; enum: alert_class, status | TR-201 |
| `approvals` | INSERT + UPDATE | RLS; enum: authority_boundary_type, status; approval_basis required on approved | TR-301 |
| `interventions` | INSERT + UPDATE | RLS; cancel_reason required on cancelled | TR-401 |
| `audit_events` | INSERT only (append-only) | No UPDATE, no DELETE; RLS | TR-1301 |
| `conversation_messages` | INSERT + UPDATE (ack only) | response_type required for AI messages | TR-801 |
| `aimc_action_log` | INSERT + UPDATE (on callback) | FK → approvals | TR-501 |
| `knowledge_retrieval_log` | INSERT only | No knowledge content columns | TR-702 |
| `system_health_events` | INSERT + UPDATE (on recovery) | FK → audit_events | TR-1601 |

---

## 23. Integration Contract Definitions

### 23.1 AMC ↔ AIMC Integration Contract

| Dimension | Requirement |
|---|---|
| **Call direction** | AMC → AIMC: action dispatch, proactive summary request. AIMC → AMC: action result callbacks, conversation callbacks, proactive message pushes |
| **Transport** | HTTPS REST. AIMC callback endpoints exposed by AMC |
| **Auth** | AMC outbound: `AIMC_SERVICE_TOKEN`. AIMC inbound callbacks: AMC validates `AIMC_CALLBACK_TOKEN` |
| **Non-bypass** | AMC must never call any model provider SDK directly. AIMC is the exclusive AI gateway |
| **Degraded mode** | AIMC health failure → TR-1602 degraded mode; no fallback AI call path |
| **Audit** | Every AMC→AIMC dispatch generates `AIMC_ACTION_INITIATED`. Every AIMC callback generates `AIMC_ACTION_COMPLETED` |

### 23.2 AMC ↔ AIMCC / KUC Integration Contract

| Dimension | Requirement |
|---|---|
| **Call direction** | AMC → AIMCC: status reads, quota reads, governance decision notifications. AMC → KUC: upload submissions only |
| **Upload enforcement** | All upload submissions POST to `KUC_API_BASE_URL/submit`. Never to AIMCC internal ingestion endpoints |
| **Auth** | `AIMCC_SERVICE_TOKEN` for AIMCC calls; `KUC_SERVICE_TOKEN` for KUC calls |
| **Degraded mode** | AIMCC health failure → TR-1603 degraded mode; governance actions frozen |

### 23.3 AMC ↔ Knowledge/Memory System Integration Contract

| Dimension | Requirement |
|---|---|
| **Call direction** | AMC → Knowledge System: retrieval queries only (read-only) |
| **Non-ownership** | AMC does not write to knowledge/memory system. No local caching of knowledge content beyond 5-minute TTL |
| **Provenance enforcement** | Every retrieval must request provenance metadata. Anonymous knowledge display is prohibited |
| **Degraded mode** | Knowledge system health failure → TR-1604 degraded mode; stale indicators applied immediately |

### 23.4 AMC ↔ Foreman Integration Contract

| Dimension | Requirement |
|---|---|
| **Call direction** | AMC → Foreman: intervention dispatch, build status reads. Foreman → AMC: intervention status callbacks |
| **Read-only reporting** | AMC reads Foreman reporting feed only. AMC does not issue build commands |
| **Callback security** | Foreman callback to `POST /api/interventions/{id}/status-update` must include Foreman service token in Authorization header |

### 23.5 AMC ↔ Specialist Agents Integration Contract

| Dimension | Requirement |
|---|---|
| **Call direction** | AMC → Specialist Agent: workspace termination orders. Specialist Agent → AMC: status callbacks |
| **Surface rule** | AMC surfaces outcomes only — not internal specialist agent state |
| **Sandbox isolation** | `sandbox_isolation_indicator` must be present on all workspace data surfaces |

---

## 24. Deferred-to-Stage-5 Declarations

The following items are explicitly deferred from Stage 4 TRS to Stage 5 Architecture. Deferral does not indicate descoping — these are Stage 5 responsibilities.

| Deferred Item | Reason for Deferral | Stage 5 Owner |
|---|---|---|
| Database column types and index DDL | Schema design details require Architecture-level decisions | schema-builder |
| Frontend React component tree | UI architecture specifics are Architecture-stage decisions | ui-builder |
| API server framework selection (e.g., Next.js API routes, dedicated REST server) | Deployment architecture decision | Architecture stage |
| Realtime channel subscription implementation details | Implementation-level WebSocket/Supabase Realtime wiring | api-builder |
| CI/CD pipeline and deployment infrastructure | Infrastructure architecture | Architecture stage |
| Push notification service provider selection (FCM vs APNs vs PWA) | Platform-specific integration decision | Architecture / integration-builder |
| AIMC health check failure retry logic specifics | Implementation detail | api-builder |
| Per-domain health status computation algorithm | Business logic within health domain services | Architecture stage |
| Authority delegated-domain configuration storage format | Configuration system architecture | Architecture stage |
| Foreman reporting event feed format details | Foreman-side API contract detail | Foreman / integration-builder |
| Background scheduler implementation (cron, Supabase Edge Function, etc.) | Infrastructure architecture | Architecture stage |

---

## 25. Sign-Off / Approval Record

| Field | Value |
|---|---|
| **Document** | AMC Technical Requirements Specification — Stage 4 |
| **Version** | 1.0 |
| **Prepared by** | foreman-v2-agent (POLC_ORCHESTRATION) |
| **Prepared Date** | 2026-04-23 |
| **CS2 Authorization for Stage 4** | app_management_centre#1127 |
| **Stage 3 Approval Reference** | app_management_centre#1123 (CS2-approved for Stage 4 progression) |
| **Reviewed by** | *Pending CS2 review* |
| **Approved by** | *Pending CS2 approval* |
| **Approval Date** | *Pending* |
| **Approval Reference** | *To be assigned by CS2 on approval* |
| **Stage** | Stage 4 of 12 — TRS |
| **Next Stage** | Stage 5 — Architecture (blocked until CS2 approves Stage 4) |

### Approval Basis Required

CS2 approval of this document confirms:
1. The TRS is technically explicit, comprehensive, and non-contradictory
2. All FRS requirement families are technically realized or explicitly deferred to Stage 5
3. Cross-system boundaries from Stages 1–3 are preserved and technically enforced
4. The TRS is sufficient for Stage 5 Architecture derivation
5. Stage 5 Architecture is authorized to commence following this approval

### CS2 Approval Instruction

To formally approve this TRS:
- Record approval in a Stage 4 approval artifact at `modules/amc/03-trs/trs-approval.md`
- Reference this document: `modules/amc/03-trs/technical-requirements-specification.md` v1.0
- Update `modules/amc/BUILD_PROGRESS_TRACKER.md` Stage 4 status to `✅ COMPLETE — CS2 APPROVED`
- Authorize commencement of Stage 5 Architecture

---

*End of Technical Requirements Specification — Stage 4. Produced by foreman-v2-agent under POLC_ORCHESTRATION. CS2 approval required before Architecture (Stage 5) derivation begins.*

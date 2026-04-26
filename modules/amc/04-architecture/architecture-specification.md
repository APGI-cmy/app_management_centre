# Architecture Specification — Stage 5

**Stage**: 5 — Architecture
**Module**: App Management Centre (AMC)
**Version**: 1.0
**Status**: 🟡 Produced — Approval Pending (CS2)
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: app_management_centre#1131 (Stage 5 kickoff; Stage 4 TRS treated as approved for Stage 5 progression)
**Governing Issue**: app_management_centre#1131
**Wave**: amc-stage5-architecture-20260426
**Date**: 2026-04-26
**Upstream Sources**:
- Stage 1 App Description: `modules/amc/00-app-description/app-description.md` v1.1 (CS2-approved, ref #1117)
- Stage 2 UX Workflow & Wiring Spec: `modules/amc/01-ux-workflow-wiring-spec/` v1.1 (CS2-approved, ref #1121)
- Stage 3 FRS: `modules/amc/02-frs/functional-requirements-specification.md` v1.1 (CS2-approved, ref #1123)
- Stage 4 TRS: `modules/amc/03-trs/technical-requirements-specification.md` v1.1 (treated as approved for Stage 5 progression, ref #1131)
**Canonical Location**: `modules/amc/04-architecture/architecture-specification.md`

---

> **DERIVATION DECLARATION**
> This Architecture Specification derives from the approved Stage 4 Technical Requirements Specification (`modules/amc/03-trs/technical-requirements-specification.md` v1.1) and all upstream approved truth (Stages 1–3). It translates the approved technical requirements into a coherent, explicit, non-contradictory system architecture for the App Management Centre. It does not invent product behavior. No architectural decision may contradict or silently soften any TRS requirement. This document defines the architectural boundaries that Stage 6 QA-to-Red, Stage 7 PBFAG, and Stage 12 Build must honor. Architecture decisions made here are binding on all downstream stages unless explicitly amended with CS2 approval.

---

## Table of Contents

1. [Purpose & Scope](#1-purpose--scope)
2. [Cross-System Boundary Confirmation](#2-cross-system-boundary-confirmation)
3. [Core Architecture Structure](#3-core-architecture-structure)
   - 3.1 [Major Architectural Components](#31-major-architectural-components)
   - 3.2 [Frontend Architecture](#32-frontend-architecture)
   - 3.3 [Backend / API Architecture](#33-backend--api-architecture)
   - 3.4 [Database Architecture](#34-database-architecture)
   - 3.5 [Real-Time Architecture](#35-real-time-architecture)
   - 3.6 [Background Scheduler Architecture](#36-background-scheduler-architecture)
   - 3.7 [Push Notification Architecture](#37-push-notification-architecture)
   - 3.8 [Deployment Architecture](#38-deployment-architecture)
4. [AMC Domain Architecture](#4-amc-domain-architecture)
   - 4.1 [Action Resolution Centre (ARC) — First-Class Technical Domain](#41-action-resolution-centre-arc--first-class-technical-domain)
   - 4.2 [Dynamic Upload Quota Management — Operational Console](#42-dynamic-upload-quota-management--operational-console)
   - 4.3 [Alert / Escalation Contract Architecture](#43-alert--escalation-contract-architecture)
   - 4.4 [Audit & Provenance Contract Architecture](#44-audit--provenance-contract-architecture)
   - 4.5 [Authentication & Authorization Contract Architecture](#45-authentication--authorization-contract-architecture)
   - 4.6 [State Ownership Architecture](#46-state-ownership-architecture)
5. [Cross-System Interaction Architecture](#5-cross-system-interaction-architecture)
   - 5.1 [AMC ↔ AIMC](#51-amc--aimc)
   - 5.2 [AMC ↔ AIMCC](#52-amc--aimcc)
   - 5.3 [AMC ↔ Knowledge Upload Centre (KUC)](#53-amc--knowledge-upload-centre-kuc)
   - 5.4 [AMC ↔ Knowledge / Memory System](#54-amc--knowledge--memory-system)
   - 5.5 [AMC ↔ Foreman / Governed Agents](#55-amc--foreman--governed-agents)
   - 5.6 [Non-Bypass Enforcement Architecture](#56-non-bypass-enforcement-architecture)
6. [State, Audit, and Resilience Architecture](#6-state-audit-and-resilience-architecture)
   - 6.1 [State Consistency Architecture](#61-state-consistency-architecture)
   - 6.2 [Cross-Device / Cross-Session Continuity](#62-cross-device--cross-session-continuity)
   - 6.3 [Audit / Provenance Recording Architecture](#63-audit--provenance-recording-architecture)
   - 6.4 [Degraded-Mode Behavior Architecture](#64-degraded-mode-behavior-architecture)
   - 6.5 [Recovery and Stale-Data Signaling Architecture](#65-recovery-and-stale-data-signaling-architecture)
7. [Trust Boundaries and Authority Boundaries](#7-trust-boundaries-and-authority-boundaries)
8. [Deployment-Shaping Architectural Decisions](#8-deployment-shaping-architectural-decisions)
9. [Deferred to Stage 6](#9-deferred-to-stage-6)
10. [Sign-Off / Approval Record](#10-sign-off--approval-record)

---

## 1. Purpose & Scope

### 1.1 Purpose

This Architecture Specification converts the approved Stage 4 Technical Requirements Specification (TRS v1.1) into a clear, explicit, non-contradictory system architecture for the App Management Centre (AMC). It defines component boundaries, service responsibilities, data and state ownership, trust boundaries, integration paths, event flows, and deployment-shaping architectural decisions.

The architecture makes explicit how AMC is structured as an executive supervisory application and preserves the approved cross-system boundary model without reassigning ownership across boundaries.

### 1.2 Scope

**In scope for Stage 5 Architecture:**
- All major architectural components, layers, and subsystems
- Frontend, backend, database, real-time, and scheduler component boundaries
- API endpoint architecture and service responsibilities
- State ownership, tenant isolation, and data persistence architecture
- Trust boundaries, authority enforcement architecture, and inter-service identity model
- ARC technical domain architecture
- Dynamic Upload Quota Management console architecture
- Cross-system integration architecture (AMC ↔ AIMC, AIMCC, KUC, knowledge/memory, Foreman, Specialist Agents)
- Alert delivery, escalation, and resilience architecture
- Audit and provenance architecture
- Authentication and authorization architecture
- Degraded-mode and recovery architecture
- Deployment-shaping architectural decisions that constrain Stage 12 Build
- Background scheduler architecture
- Push notification delivery architecture
- CI/CD architecture (pipeline structure; not CI script implementation)

**Out of scope for Stage 5 Architecture:**
- Column-level DDL with types and indices (deferred to schema-builder per TRS §25)
- React component tree and UI component design (deferred to ui-builder per TRS §25)
- CI script implementation (Stage 12 Build)
- API code implementation (Stage 12 Build)
- Test specifications (Stage 6 QA-to-Red)
- Builder-level implementation task specifications (Stages 8–11)

> TRS Traceability: TRS §1.2 Scope

---

## 2. Cross-System Boundary Confirmation

These boundaries are inherited from Stage 1 and technically elaborated in Stage 4 TRS §2. They are reproduced here as architecture-binding invariants. No architecture decision in this document may contradict or soften them.

| System | Architectural Role | AMC Architectural Interaction |
|---|---|---|
| **AMC** | React front-end + Next.js API layer. Executive supervisory operating surface. Owns executive state (alerts, approvals, interventions, audit, conversation, health events, ARC, quota management). Does not execute AI models. Does not own persistent knowledge truth. | Authoritative writer to AMC-owned tables. Reads external systems only via governed API calls. |
| **AIMC** | AI execution gateway. Sole authorized AI model router. Governs all AI model invocation. | AMC calls AIMC REST/WebSocket API only. AMC application code never imports or instantiates any model provider SDK. |
| **AIMCC** | Knowledge ingestion and memory operations service. Governs ingestion pipelines and knowledge memory operations. | AMC calls AIMCC read API for status and quota reads, governance decision notifications. AMC never calls AIMCC internal ingestion endpoints. |
| **Knowledge Upload Centre (KUC)** | Governed knowledge upload entry surface. REST API for upload submission only. | AMC POSTs upload submissions to KUC API only. Never to AIMCC ingestion endpoints. |
| **Knowledge / Memory System** | Persistent estate knowledge substrate. Canonical truth store. | AMC calls governed knowledge retrieval API (read-only, provenance required). AMC does not write to or persist knowledge records beyond transient TTL cache. |
| **Foreman** | Orchestration agent. Reporting source; intervention dispatch target for Foreman-governed interventions. | AMC reads Foreman reporting feed (read-only). AMC dispatches intervention orders to Foreman dispatch API. AMC does not issue build commands. |
| **Specialist Agents** | Domain-specific sandboxed workers. | AMC receives status callbacks from specialist agents. AMC may dispatch termination orders through governed pathway. AMC surfaces outcomes only — not internal specialist agent state. |

**Architecture-binding boundary invariants (TRS TR-BOUNDARY-001 to TR-BOUNDARY-004):**

1. **AI model SDK prohibition**: AMC `package.json` must not list any model-provider SDK (OpenAI, Anthropic, Google Gemini, etc.) as a dependency. Architecture enforces this at the dependency scanning layer. Runtime bypass detection via `BOUNDARY_BYPASS_ATTEMPTED` audit event.
2. **AIMCC ingestion bypass prohibition**: AMC never calls AIMCC internal ingestion endpoints. All upload submissions POST to `KUC_API_BASE_URL/submit` only.
3. **Knowledge write prohibition**: AMC does not define any table that stores persistent knowledge/memory content as AMC-canonical truth. Transient cache TTL maximum 5 minutes with stale-detection markers.
4. **Service identity auth**: All outbound API calls from AMC must include `Authorization: Bearer {service_token}` header. Missing or invalid token blocks the call and writes audit event.

---

## 3. Core Architecture Structure

### 3.1 Major Architectural Components

AMC is structured as a full-stack web application with the following major components:

```
┌─────────────────────────────────────────────────────────────────┐
│                    AMC APPLICATION STACK                        │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              FRONTEND LAYER (React SPA)                  │   │
│  │  Surface components / Routes / State management          │   │
│  │  Supabase Realtime subscriptions / Auth session client   │   │
│  └────────────────────┬───────────────────────────────────┘   │
│                        │ HTTPS (internal)                       │
│  ┌─────────────────────▼───────────────────────────────────┐   │
│  │           API LAYER (Next.js API Routes)                  │   │
│  │  Auth middleware / Authority-domain enforcement           │   │
│  │  Business logic / Integration client services             │   │
│  │  External service calls / Callback endpoints              │   │
│  └────────────────────┬───────────────────────────────────┘   │
│                        │                                        │
│  ┌─────────────────────▼───────────────────────────────────┐   │
│  │         SUPABASE SERVICES LAYER                           │   │
│  │  PostgreSQL (RLS enforced) / Supabase Auth               │   │
│  │  Supabase Realtime / Supabase Edge Functions              │   │
│  └───────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                           │
          External Service Boundary (HTTPS, governed service tokens)
                           │
    ┌──────────┬──────────┬──────────┬──────────┬───────────┐
    │  AIMC    │  AIMCC   │   KUC    │Knowledge │  Foreman  │
    │ Gateway  │ Service  │  API     │  System  │  Agent    │
    └──────────┴──────────┴──────────┴──────────┴───────────┘
```

**Component responsibilities:**

| Component | Responsibility | Scope Boundary |
|---|---|---|
| **React SPA** | User interface, surface routing, local state management, Realtime subscription management, auth session client | Client-side only; no AI model calls; no direct database access |
| **Next.js API Routes** | All server-side business logic, authority enforcement, database reads/writes, external service integration, callback handling | Server-side only; all consequential actions; authority middleware mandatory |
| **Supabase PostgreSQL** | Persistent state for all AMC-owned tables; RLS enforcement | AMC-owned tables only; no cross-tenant access |
| **Supabase Auth** | User authentication, JWT session management, MFA | Auth authority only; JWT validated on every API route |
| **Supabase Realtime** | Live state broadcast to connected sessions | AMC executive state channel; conversation channel; health event channel |
| **Supabase Edge Functions** | Background scheduler jobs (alert auto-escalation, health polling, ARC stale-item detection, quota threshold monitoring) | Scheduled background execution; no user-facing interaction |
| **Integration Clients** | Service-specific HTTP clients for AIMC, AIMCC, KUC, knowledge system, Foreman, specialist agents | Outbound calls only; governed service token per client |

### 3.2 Frontend Architecture

**Framework**: React (SPA) with server-side rendering support via Next.js.

**Routing architecture**: Next.js App Router with named routes matching TRS TR-104 route list:

| Route | Surface | TRS Source |
|---|---|---|
| `/dashboard` | Executive Dashboard | TR-104, TR-101 |
| `/alerts` | Alert Management Centre | TR-104, TR-201 |
| `/approvals` | Approval Queue | TR-104, TR-301 |
| `/interventions` | Intervention Console | TR-104, TR-401 |
| `/ai-actions` | AI-Routed Actions (AIMC) | TR-104, TR-501 |
| `/aimcc-supervision` | AIMCC / KUC Supervision | TR-104, TR-601 |
| `/knowledge` | Knowledge-Aware View | TR-104, TR-701 |
| `/conversation` | Executive Conversation | TR-104, TR-801 |
| `/agent-oversight` | Specialist Agent Workspace Oversight | TR-104, TR-901 |
| `/maintenance-reports` | Maintenance & Assurance Reports | TR-104, TR-1001 |
| `/estate-config` | Estate Configuration & Wellbeing | TR-104, TR-1101 |
| `/arc` | Action Resolution Centre | TR-104, TR-1801 |

**Route guard architecture**: Every authenticated route enforces Supabase Auth session validity at the Next.js middleware layer. Navigation must not depend on AIMC or AIMCC availability — route failures must not silently leave the user on a blank route (TRS TR-104). Route guards are server-side middleware, not client-side redirect logic.

**Responsive layout architecture**: Responsive breakpoints must produce a distinct mobile layout at ≤768px viewport width per TRS TR-1201. Mobile layout surfaces critical and high alerts immediately on load without scroll. Approve/Reject controls render without horizontal scroll on mobile.

**State management**: React context + Supabase Realtime subscriptions for live state. Local component state for transient UI state only. Server state (alert lists, approval queues, etc.) must be fetched from server APIs — not maintained as local-only state. On session restore, all critical state domains are re-fetched from server APIs per TRS TR-1703.

**Realtime subscription architecture**: Frontend subscribes to Supabase Realtime channels on mount and unsubscribes on unmount:
- `amc_executive_state_{user_id}` — alert, approval, intervention, health domain state changes
- `amc_conversation_{session_id}` — conversation message events
- `amc_arc_{user_id}` — ARC item classification and state change events
- `amc_health_events` — system health event broadcasts

On receiving a Realtime update, affected component state must be updated immediately — no stale-while-revalidate that surfaces contradictory states without explicit staleness indicator (TRS TR-1702).

**AI model SDK prohibition**: `package.json` must not include any model-provider SDK. This is enforced at the dependency scanning gate (CI) and verified at startup.

### 3.3 Backend / API Architecture

**API framework**: Next.js API Routes (App Router `app/api/` path handlers). All AMC server-side logic is implemented as Next.js API route handlers. This decision is made at Architecture stage (was deferred from TRS §25).

**Rationale for Next.js API Routes**: Next.js provides native integration with Supabase Auth, React SSR for the frontend, and a unified deployment unit. API route handlers execute server-side with full Node.js runtime access. This eliminates the need for a separate REST server process while remaining capable of handling all AMC API surface requirements.

**Middleware architecture**: Every API route handler that performs a consequential action must execute the following middleware layers in order:

```
Request → [Auth Middleware] → [Actor Resolution] → [Authority-Domain Check] → [Route Handler] → Response
```

1. **Auth Middleware**: Validates Supabase JWT from request headers or cookies. Returns HTTP 401 on missing or invalid JWT. Sets `authenticated_actor` context.
2. **Actor Resolution**: Resolves `actor_type` from JWT claims or service token metadata. Maps to one of: `human`, `ai_executive`, `orchestration`, `assurance`, `specialist`, `system`, `service`. Actor identity is never passed freely by callers (TRS TR-1403).
3. **Authority-Domain Check**: Enforces authority boundary per TRS TR-1404. `reserved_matter` → actor must be `human` with Johan Ras identity claim. `delegated` → actor must be `ai_executive` within approved delegated scope configuration. `operational` → authenticated executive actor permitted. These checks run server-side and cannot be bypassed by client-side UI.
4. **Route Handler**: Business logic, database operations, external service calls.

**API namespace structure**:
- `/api/dashboard/*` — Executive estate oversight
- `/api/alerts/*` — Alert management
- `/api/approvals/*` — Approval workflow
- `/api/interventions/*` — Intervention management
- `/api/aimcc/*` — AIMCC supervision including quota management
- `/api/conversation/*` — Executive conversation
- `/api/reports/*` — Maintenance & assurance reports
- `/api/audit-events/*` — Audit log access
- `/api/arc/*` — Action Resolution Centre
- `/api/workspaces/*` — Specialist agent workspace oversight
- `/api/estate-config/*` — Estate configuration
- `/api/aimc/*` — AIMC callback receiving endpoints
- `/api/health/*` — Internal health status (for system self-monitoring)

**Full API endpoint inventory**: The complete API endpoint list defined in TRS §22 is architecturally binding. Every endpoint listed in TRS §22.1 (internal), §22.2 (inbound callbacks), and §22.3 (outbound calls) must be implemented. Architecture adds no new endpoints and removes none.

**Configuration validation at startup**: On application startup, AMC API layer must validate that all required environment variables are present. Missing required environment variable configuration (service tokens, base URLs) must prevent startup with explicit startup error logged. Required environment variables: `AIMC_API_BASE_URL`, `AIMCC_API_BASE_URL`, `KUC_API_BASE_URL`, `KNOWLEDGE_API_BASE_URL`, `FOREMAN_API_BASE_URL`, `SPECIALIST_AGENT_API_BASE_URL`, `AIMC_SERVICE_TOKEN`, `AIMCC_SERVICE_TOKEN`, `KUC_SERVICE_TOKEN`, `KNOWLEDGE_SERVICE_TOKEN`, `FOREMAN_SERVICE_TOKEN`, `SPECIALIST_AGENT_SERVICE_TOKEN` (TRS TR-1504, TR-1505).

**Post-approval dispatch architecture**: On successful approval decision, downstream action dispatch to external services (AIMC, Foreman, AIMCC) must execute as an atomic post-commit step. If downstream dispatch fails after the approval record is committed: the approval record remains persisted with `status: approved`; `downstream_dispatch_failed` flag is set; explicit error returned. The approval decision is never rolled back due to downstream service unavailability (TRS TR-303).

### 3.4 Database Architecture

**Database**: Supabase (PostgreSQL). Row-Level Security (RLS) enabled on all tables containing tenant or actor-specific data. Tenant isolation key: `organisation_id` required on all AMC-owned tables per TRS §23.

**AMC-owned tables** (canonical set — schema-builder must implement column DDL):

| Table | RLS Policy | Write Rule | TRS Source |
|---|---|---|---|
| `alerts` | `organisation_id` tenant-scoped | INSERT + UPDATE | TR-201 |
| `approvals` | `organisation_id` tenant-scoped | INSERT + UPDATE | TR-301 |
| `interventions` | `organisation_id` tenant-scoped | INSERT + UPDATE | TR-401 |
| `audit_events` | `organisation_id` tenant-scoped | INSERT only (append-only, no UPDATE, no DELETE) | TR-1301 |
| `conversation_messages` | `organisation_id` tenant-scoped | INSERT + UPDATE (ack only) | TR-801 |
| `aimc_action_log` | `organisation_id` tenant-scoped | INSERT + UPDATE (on callback) | TR-501 |
| `knowledge_retrieval_log` | `organisation_id` tenant-scoped | INSERT only | TR-702 |
| `system_health_events` | `organisation_id` tenant-scoped, system-writable | INSERT + UPDATE (on recovery) | TR-1601 |
| `arc_classifications` | `organisation_id` tenant-scoped, service-writable | INSERT + UPDATE | TR-1806 |

**Tenant isolation architecture**: `organisation_id` must be present on every AMC-owned table. All RLS policies key off `organisation_id`. No AMC API route may return or write data without resolving `organisation_id` from the authenticated JWT or service token context. Cross-tenant reads and writes are architecturally prohibited at the RLS enforcement layer (TRS §23, §24).

**Append-only enforcement for audit_events**: `audit_events` table is INSERT-only. No UPDATE, no DELETE operations are permitted on this table from any service or maintenance path. Corrections are written as additive INSERT records (TRS TR-1301, TR-1305).

**Foreign key relationships**: Architecture binding FK relationships:
- `approvals.source_alert_id` → `alerts.id`
- `approvals.source_intervention_id` → `interventions.id`
- `approvals.source_aimc_action_id` → `aimc_action_log.id`
- `interventions.source_alert_id` → `alerts.id`
- `interventions.linked_approval_id` → `approvals.id`
- `aimc_action_log.linked_approval_id` → `approvals.id`
- `system_health_events.audit_event_ref` → `audit_events.id`
- `arc_classifications` — logical FK to source object (not enforced at DB level due to polymorphic source_type; enforced at application layer)

**Column type and index DDL**: Deferred to schema-builder per TRS §25. Schema-builder must implement all column type specifications and index constraints consistent with TRS §4–§21 requirements.

### 3.5 Real-Time Architecture

**Technology**: Supabase Realtime with PostgreSQL logical replication for live state propagation.

**Channel architecture**:

| Channel | Pattern | Subscribers | Events |
|---|---|---|---|
| `amc_executive_state_{user_id}` | User-scoped | All connected AMC sessions for this user | Alert status changes, approval decisions, intervention status changes, system health events |
| `amc_conversation_{session_id}` | Session-scoped | All devices for this conversation session | New conversation messages, message acknowledgments, proactive message delivery |
| `amc_arc_{user_id}` | User-scoped | ARC surface subscribers | ARC item classifications, state changes, resolutions |
| `amc_health_broadcast` | System-level | All authenticated sessions | System dependency degraded/recovered events |

**Real-time delivery SLAs** (architecture must support):
- Alert status changes → connected sessions: ≤2 seconds of INSERT commit (TRS TR-207)
- ARC surface update after referenced alert acknowledgment: ≤2 seconds (TRS TR-1806)
- Cross-device conversation continuity: ≤2 seconds (TRS TR-805)
- State mutations (alert ack, approval decision, intervention status): broadcast to all connected sessions immediately (TRS TR-1702)

**Polling fallback**: Health data polling as fallback for health domain status only (TRS §3 Technology Stack). Real-time is primary delivery mechanism; polling is fallback only.

### 3.6 Background Scheduler Architecture

**Technology**: Supabase Edge Functions with scheduled invocation (cron triggers). This decision is made at Architecture stage (was deferred from TRS §25).

**Rationale**: Supabase Edge Functions provide native integration with the Supabase database and Realtime layer, eliminating the need for an external scheduler service. Cron-trigger Edge Functions are the architectural choice for all background scheduled jobs.

**Scheduler functions and their cadences**:

| Function | Cadence | Responsibility | TRS Source |
|---|---|---|---|
| `amc-alert-escalation-scheduler` | Every 5 minutes | Auto-escalate Critical unacknowledged alerts per two-level escalation chain (default: Level 1 at 30 min, Level 2 at 60 min) | TR-206, TR-209 |
| `amc-health-poll-scheduler` | Every 30 seconds | Poll AIMC, AIMCC, Knowledge System health endpoints; detect degraded/recovered transitions; write system_health_events; broadcast via Realtime | TR-1501, TR-1502, TR-1503 |
| `amc-arc-staleness-scheduler` | Every 15 minutes | Detect ARC items in `open` or `in_resolution` state past SLA (default: 240 min); generate Medium alerts referencing the ARC item | TR-1804 |
| `amc-quota-threshold-monitor` | After every upload completion callback | Check quota threshold state machine transitions; write audit events; generate alerts on threshold entry | TR-607 |
| `amc-quota-override-reminder` | Every 60 minutes | Check approved temporary quota overrides for pre-expiry (default: 24h lead time); generate reminder alert | TR-606 |
| `amc-approval-arc-timeout-checker` | Every 10 minutes | Detect reserved-matter approval items past ARC timeout (default: 120 min) for ARC classification | TR-1802 |
| `amc-alert-timing-sla-monitor` | Continuous (event-driven) | Detect SLA breach between trigger event and INSERT, INSERT and Realtime broadcast, INSERT and push dispatch; write `ALERT_DELIVERY_DELAYED` audit event on breach | TR-207 |

**Scheduler failure behavior**: If any scheduler function itself fails at execution time: a Critical alert must be generated in `alerts` with `source_system: "amc_scheduler"` and the specific function name. If the alert INSERT itself fails (database write error): the Edge Function runtime error log captures the failure, and a separate health event is emitted. No scheduler failure may be silent (TRS TR-206).

**Threshold and timeout configuration**: All threshold values and timeout intervals are configurable via environment variables. No hardcoded values. Required environment variables: `ALERT_ESCALATION_LEVEL_1_MINUTES`, `ALERT_ESCALATION_LEVEL_2_MINUTES`, `ARC_RESERVED_MATTER_TIMEOUT_MINUTES`, `ARC_BOUNDARY_BYPASS_TIMEOUT_MINUTES`, `ARC_STALE_ITEM_SLA_MINUTES`, `QUOTA_WARNING_THRESHOLD_PERCENT`, `QUOTA_CRITICAL_THRESHOLD_PERCENT`, `HEALTH_POLL_INTERVAL_SECONDS` (TRS TR-607, TR-1802, TR-1804).

**Authority delegated-domain configuration storage**: Authority delegated-domain configuration values (which `ai_executive` actors have which delegated scope) are stored as structured JSON in a Supabase-hosted configuration table `authority_domain_config` (not environment variables, as this is a runtime-manageable configuration). AMC API middleware reads this table on each authority check for `delegated` boundary types. This table is append-only from an audit perspective — changes are new records, not in-place updates. This decision is made at Architecture stage (was deferred from TRS §25).

### 3.7 Push Notification Architecture

**Technology decision** (deferred from TRS §25): AMC implements push notifications via the following tiered approach:
- **Web/Desktop**: Web Push API (PWA-compatible) via a service worker. Enables push to any modern browser.
- **Android**: Firebase Cloud Messaging (FCM) for native Android push.
- **iOS**: Apple Push Notification Service (APNs) for native iOS push.

**Unified dispatch architecture**: AMC API layer dispatches push notifications through a unified notification service client that abstracts the channel selection. The client resolves the push channel based on the device registration record (device type + push token) associated with the authenticated user. Multiple devices per user are supported.

**Deep link on push payload**: Every push notification includes a `deep_link` field pointing to the relevant AMC surface (e.g., `/alerts/{alert_id}`) per TRS TR-1202.

**Push failure handling**: Push notification dispatch failures must not block alert creation. Failure is recorded but does not roll back the alert. On next AMC app open: in-app alert banner displays outstanding unacknowledged critical alerts (mandatory fallback, TRS TR-1202).

**Device registration**: A `push_device_registrations` table in Supabase stores device push tokens per user. This is an ancillary operational table not listed in the core AMC table set — it is managed by the push notification subsystem.

### 3.8 Deployment Architecture

**Deployment platform**: Vercel (Next.js-native deployment). This is the recommended deployment platform. The application must also be deployable to any Node.js hosting environment supporting Next.js 14+ — deployment platform lock-in is avoided.

**CI/CD pipeline architecture** (high-level — CI script implementation deferred to Stage 12):
- **Branch protection**: All merges to `main` require PR review + CI pass
- **CI gate stages**: Lint → Type check → Dependency scan (AI SDK prohibition) → Unit tests → Integration tests → E2E smoke tests → Deployment
- **Dependency scanning gate**: Automated check that `package.json` does not list any AI model provider SDK. This gate enforces TR-BOUNDARY-001 at CI time.
- **Environment variable validation**: Startup check fails build if required env vars are absent in the target deployment environment

**Environment tiers**: Development, Staging, Production. Supabase projects per environment tier. Environment-variable-based configuration for all service endpoints and tokens (TRS TR-1505).

---

## 4. AMC Domain Architecture

### 4.1 Action Resolution Centre (ARC) — First-Class Technical Domain

ARC is explicitly recognized as a first-class architectural and technical domain within AMC. It is not absorbed into generic umbrella sections and is not merely a UI-layer filter over alerts or approvals tables.

**ARC architectural identity**:
- Distinct database table: `arc_classifications` (not a view or derived table)
- Dedicated API namespace: `/api/arc/`
- Dedicated frontend route: `/arc` (accessible from executive navigation sidebar)
- Distinct audit event family: `ARC_ITEM_CLASSIFIED`, `ARC_ITEM_STATE_CHANGED`, `ARC_ITEM_RESOLVED`, `ARC_ITEM_EXTERNALLY_ESCALATED`
- Dedicated Realtime channel: `amc_arc_{user_id}`

**ARC architectural position within AMC**:

```
┌─────────────────────────────────────────────────────────────────┐
│                     AMC OPERATIONAL DOMAINS                     │
│                                                                 │
│  ┌──────────┐  ┌───────────┐  ┌──────────────┐  ┌──────────┐  │
│  │  ALERTS  │  │ APPROVALS │  │INTERVENTIONS │  │ AIMC     │  │
│  │  Domain  │  │  Domain   │  │  Domain      │  │ Actions  │  │
│  └────┬─────┘  └─────┬─────┘  └──────┬───────┘  └────┬─────┘  │
│       │               │               │                │        │
│       └───────────────┴───────────────┘                │        │
│                       │ ARC classification triggers     │        │
│                       ▼                                 │        │
│  ┌────────────────────────────────────────────────────┐│        │
│  │       ARC — ACTION RESOLUTION CENTRE               ││        │
│  │  arc_classifications table / /api/arc/ namespace   ││        │
│  │  Resolution workspace for governance-blocked items ││        │
│  │  Authority-enforced: Johan Ras / Maturion per item ││        │
│  └────────────────────────────────────────────────────┘│        │
│                                                         │        │
└─────────────────────────────────────────────────────────────────┘
```

**ARC triggering architecture** (server-side classification, not client-side):

ARC classification is written to `arc_classifications` by server-side logic triggered by the following conditions (TRS TR-1802):

1. Critical alert escalated to Level 2 and unresolved (via `amc-alert-escalation-scheduler`)
2. Reserved-matter approval item in `pending` state past ARC timeout (via `amc-approval-arc-timeout-checker`)
3. Intervention with `status: "dispatch_failed"` requiring human re-authorization
4. AIMCC governance approval frozen past ARC timeout
5. Boundary-bypass event (`BOUNDARY_BYPASS_ATTEMPTED` audit event) without resolution record within ARC timeout

**ARC state machine architecture**:

```
    open
     │
     │ POST /api/arc/{id}/begin-resolution
     ▼
in_resolution
     │
     │ POST /api/arc/{id}/resolve
     ▼
resolved (terminal)

     OR

open/in_resolution
     │
     │ POST /api/arc/{id}/escalate-externally
     ▼
externally_escalated (terminal)
```

Each transition writes `ARC_ITEM_STATE_CHANGED` audit event. Stale items (open or in_resolution past SLA) trigger Medium alert via `amc-arc-staleness-scheduler`.

**ARC authority enforcement architecture** (server-side, not client-side):
- ARC items from reserved-matter approvals: Johan Ras (`human` actor) only
- ARC items from boundary-bypass events: Johan Ras acknowledgment and resolution only; cannot be auto-resolved
- ARC items from operational-scope interventions: Maturion within approved delegated authority (authority-domain check via `authority_domain_config`)
- ARC resolution requires `ARC_ITEM_RESOLVED` audit event with mandatory fields per TRS TR-1803

**ARC Realtime architecture**: ARC surface subscribes to `amc_arc_{user_id}` Realtime channel. When a referenced source object changes (e.g., alert acknowledged), ARC surface must reflect this within 2 seconds via Realtime update.

### 4.2 Dynamic Upload Quota Management — Operational Console

Dynamic Upload Quota Management is architecturally defined as a hands-on operational management console capability within AMC — not merely supervisory visibility. This is an explicit first-class architectural decision derived from Stage 1 §4 and TRS TR-605 to TR-609.

**Architectural characterization**: The quota management console is an active control surface through which authorized actors (Johan Ras, and within delegated authority, Maturion) can initiate quota adjustments, temporary overrides, and review quota history — all gated through the approval workflow.

**Quota management architectural structure**:

```
┌─────────────────────────────────────────────────────────────────┐
│         AIMCC SUPERVISION SURFACE (/aimcc-supervision)          │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │        UPLOAD STATUS PANEL (read-only from AIMCC)        │   │
│  │  AIMCC read API → upload status per document             │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │    QUOTA MANAGEMENT CONSOLE (operational control)        │   │
│  │                                                          │   │
│  │  Current quota display (AIMCC read API)                  │   │
│  │  Threshold state indicator (ok / warning / critical)     │   │
│  │  ── Control surfaces ────────────────────────────────    │   │
│  │  [Request Quota Increase] → POST /api/aimcc/quota/...   │   │
│  │  [Request Quota Decrease] → POST /api/aimcc/quota/...   │   │
│  │  [Request Temporary Override] → POST /api/aimcc/quota/  │   │
│  │  ── Approval gate ───────────────────────────────────    │   │
│  │  All quota changes require approval (reserved_matter)    │   │
│  │  Approval record created → approval workflow             │   │
│  │  On approval: AIMCC governance decision notification     │   │
│  │  ── Observability ───────────────────────────────────    │   │
│  │  Quota change history reconstructable from audit_events  │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

**Quota management architectural rules**:
- `POST /api/aimcc/quota/request-adjustment` is the sole quota-change initiation path from AMC
- All quota adjustment requests create `reservedmatter` approval records
- No quota change takes effect without a completed approval record
- AIMCC is notified of approved quota changes via `POST {AIMCC_API_BASE_URL}/governance/decision`
- Temporary overrides require `override_expiry_at`; AIMCC enforces expiry; AMC records events
- Quota threshold state machine: `ok` → `warning` → `critical` transitions generate alerts and audit events
- Quota threshold configuration: environment-variable-configurable (`QUOTA_WARNING_THRESHOLD_PERCENT`, `QUOTA_CRITICAL_THRESHOLD_PERCENT`)
- Full quota change history reconstructable from `audit_events` (no separate quota history table)

### 4.3 Alert / Escalation Contract Architecture

Alert management is a core operational domain. The architecture addresses the complete alert lifecycle including delivery timing, durability, escalation chain, and retry behavior.

**Alert delivery pipeline architecture**:

```
Trigger Event (scheduler / AIMC callback / health check / intervention failure)
    │
    │ ≤5 seconds
    ▼
INSERT into alerts table (AMC PostgreSQL)
    │
    │ ≤2 seconds (Supabase Realtime)
    ▼
Broadcast to amc_executive_state_{user_id} channel
    │
    │ ≤5 seconds (concurrently with Realtime)
    ▼
Push notification dispatch (FCM / APNs / Web Push)
```

**Alert timing SLA self-monitoring architecture**: AMC implements event-driven SLA monitoring via the `amc-alert-timing-sla-monitor` component. If a SLA breach is detected (trigger → INSERT > 5s, INSERT → Realtime > 2s, INSERT → push dispatch begin > 5s): write `ALERT_DELIVERY_DELAYED` audit event with `severity: warning`. This component is implemented as an observable in the alert creation pipeline.

**Two-level escalation chain architecture** (TRS TR-209):
- **Level 0**: Alert created, awaiting acknowledgment
- **Level 1**: Unacknowledged past `escalation_timeout_level_1_minutes` (default: 30 min for Critical) → auto-escalation to Maturion; `ALERT_ESCALATED_LEVEL_1` audit event
- **Level 2**: Still unacknowledged past `escalation_timeout_level_2_minutes` (default: 60 min) → escalation to Johan Ras direct; push notification mandatory; `ALERT_ESCALATED_LEVEL_2` audit event

Level skipping is prohibited. Manual escalation by Johan Ras may jump to any level. Level 2 is terminal for auto-escalation.

**Alert write retry architecture**: Failed alert INSERTs trigger retry with exponential back-off: retry 1 at 1s, retry 2 at 3s, retry 3 at 10s. If all 3 retries fail: write to durable fallback audit sink; surface error to UI if human-initiated; generate `SYSTEM_ERROR` alert when database recovers (TRS TR-208).

**Class-based dismissal enforcement**: Critical, High, and Medium alerts cannot be dismissed (HTTP 422 on server-side enforcement). Dismissal requires non-empty `dismiss_reason`. Server must reject regardless of client-side UI state.

### 4.4 Audit & Provenance Contract Architecture

**Audit architecture principles**:
- `audit_events` table is append-only (INSERT only; no UPDATE; no DELETE)
- Every consequential action produces at least one audit event before returning success to the caller
- If the audit event INSERT fails, the consequential action must be rolled back (atomicity contract, TRS TR-1305)
- Audit events carry full actor identity (`actor`, `actor_type` from the authority model)
- Cross-system references (`cross_system_ref`) are populated for all actions dispatched to external services

**Audit event categories and required fields**:

| Event Category | Required Fields | TRS Source |
|---|---|---|
| Alert lifecycle events | `alert_id`, `alert_class`, `actor`, `actor_type`, `timestamp` | TR-202, TR-203, TR-204 |
| Approval lifecycle events | `approval_id`, `decision`, `actor`, `actor_type`, `authority_boundary_type`, `basis`, `timestamp` | TR-302 |
| Intervention lifecycle events | `intervention_id`, `status`, `actor`, `actor_type`, `timestamp` | TR-402, TR-403, TR-404 |
| AIMC interaction events | `action_type`, `actor`, `actor_type`, `source`, `aimc_ref`, `timestamp` | TR-502, TR-503 |
| ARC lifecycle events | `arc_item_id`, `source_type`, `source_id`, `arc_status`, `actor`, `actor_type`, `timestamp` | TR-1805 |
| Quota management events | `actor`, `current_quota`, `requested_quota`, `threshold_state`, `aimcc_context_id`, `timestamp` | TR-609 |
| Knowledge retrieval events | `actor`, `actor_type`, `query_summary`, `result_count`, `source_refs`, `retrieval_timestamp` | TR-701 |
| System health events | `dependency`, `event_type`, `detected_at`, `impact_summary`, `audit_event_ref` | TR-1601 |
| Boundary bypass events | `bypass_type`, `detected_at`, `severity: critical` | TR-504, TR-604 |

**Audit delivery atomicity**: The audit event INSERT and the consequential action that triggers it must succeed together or fail together. If the application cannot write both the action record and the audit event, neither must be committed (TRS TR-1305). This is enforced at the database transaction layer.

**Provenance requirement for knowledge references**: All knowledge retrieval calls must include `require_provenance: true`. Anonymous knowledge references without provenance metadata are prohibited from rendering in AMC surfaces (TRS TR-701).

### 4.5 Authentication & Authorization Contract Architecture

**Authentication architecture**:
- **Technology**: Supabase Auth (JWT-based session tokens, MFA capability required per TRS TR-1401)
- **Token storage**: JWT stored in httpOnly cookie (preferred) or Supabase Auth session store. Not in localStorage in production.
- **Session validation**: Every API route validates JWT via Supabase Auth server client at middleware layer

**Authorization architecture — authority domain model**:

```
Actor types (resolved from JWT or service token — never passed by caller):
  - human          → Johan Ras human login
  - ai_executive   → Maturion AI executive via AIMC
  - orchestration  → Foreman agent
  - assurance      → IAA agents
  - specialist     → Specialist agents
  - system         → AMC background jobs, scheduler
  - service        → External service callbacks

Authority boundaries (per action):
  - reserved_matter → actor must be human (Johan Ras identity claim)
  - delegated       → actor must be ai_executive within approved scope (authority_domain_config)
  - operational     → authenticated executive actor permitted
```

**Authority boundary enforcement architecture**:
- Enforcement runs at the API middleware layer for every consequential action endpoint
- `authority_domain_config` Supabase table stores delegated-scope configurations (runtime-configurable without code changes)
- Server rejects unauthorized actors regardless of what client-side UI presented

**Inter-service trust boundary architecture** (TRS TR-1405):
- AMC is the sole authorized writer to AMC-owned tables
- Every inbound callback endpoint (`/api/aimc/callback`, `/api/aimc/conversation-callback`, `/api/aimc/proactive-message`, `/api/interventions/{id}/status-update`) validates `Authorization: Bearer` header against registered service token before processing payload
- Invalid token → HTTP 401
- Mismatched service identity → HTTP 403 + `UNAUTHORIZED_ACCESS_ATTEMPT` audit event
- Service tokens are environment-variable-configurable and rotatable without code changes
- Trust escalation prohibition: AIMC service token cannot access Foreman endpoints or AMC admin operations
- `actor_type` in callback payloads must match the token's registered service identity or the callback is rejected

### 4.6 State Ownership Architecture

State ownership is defined in TRS TR-1701 and is architecture-binding. It is reproduced here with architectural context:

| State Domain | Canonical Owner | AMC Write Access | Architecture Enforcement |
|---|---|---|---|
| `alerts` | AMC | INSERT + UPDATE | RLS; organisation_id key |
| `approvals` | AMC | INSERT + UPDATE | RLS; organisation_id key |
| `interventions` | AMC | INSERT + UPDATE | RLS; organisation_id key |
| `audit_events` | AMC | INSERT only | RLS; database-level INSERT-only RLS policy enforced |
| `conversation_messages` | AMC | INSERT + UPDATE (ack) | RLS; organisation_id key |
| `aimc_action_log` | AMC | INSERT + UPDATE (on callback) | RLS; organisation_id key |
| `knowledge_retrieval_log` | AMC | INSERT only | RLS; organisation_id key; no knowledge content columns |
| `system_health_events` | AMC | INSERT + UPDATE (on recovery) | RLS; organisation_id key |
| `arc_classifications` | AMC | INSERT + UPDATE | RLS; service-writable; organisation_id key |
| `knowledge_upload_records` (AIMCC) | AIMCC | None | AMC reads via AIMCC API only; no DB access |
| `knowledge/memory content` (Knowledge System) | Knowledge System | None | AMC reads via governed query API; no DB access |

**Architecture enforcement for non-AMC state**: AMC must have no database credentials that permit direct access to AIMCC, KUC, or Knowledge System database tables. AMC reads external state exclusively via governed REST API calls.

---

## 5. Cross-System Interaction Architecture

### 5.1 AMC ↔ AIMC

**Interaction pattern**: AMC is the initiator of all AI action dispatches. AIMC is the responder and sole AI gateway. AIMC initiates proactive pushes back to AMC.

**Direction of responsibility**:
- AMC → AIMC: Action dispatch (`POST {AIMC_API_BASE_URL}/actions`), health polling, proactive summary requests
- AIMC → AMC: Action result callbacks (`POST /api/aimc/callback`), conversation callbacks (`POST /api/aimc/conversation-callback`), proactive message pushes (`POST /api/aimc/proactive-message`)

**Routing principles**:
- All AMC-initiated AI action dispatches use a single AIMC client service class that wraps `POST {AIMC_API_BASE_URL}/actions`
- Action type disambiguates routing within AIMC (e.g., `proactive_summary`, `conversation_message`, `governance_action`, `specialist_task`)
- AMC never dispatches to individual AI model provider APIs

**Non-bypass constraint enforcement**:
- `package.json` AI SDK exclusion check (CI dependency gate)
- Runtime: `BOUNDARY_BYPASS_ATTEMPTED` audit event + Critical alert on detected bypass

**Degraded mode**: AIMC health failure → enter AIMC degraded mode immediately. All pending AIMC dispatch attempts return `{ blocked: true, reason: "aimc_degraded" }`. `POST /api/aimc/*` returns HTTP 503. Maturion Proactive Panel renders "Maturion communication unavailable — AIMC unreachable" (exact required string, TRS TR-1602).

**Audit trail**: Every AMC→AIMC dispatch generates `AIMC_ACTION_INITIATED`. Every AIMC callback generates `AIMC_ACTION_COMPLETED` or `AIMC_ACTION_FAILED`.

### 5.2 AMC ↔ AIMCC

**Interaction pattern**: AMC supervises AIMCC operations but does not control ingestion pipelines. AMC reads status and quota data from AIMCC. AMC notifies AIMCC of governance decisions.

**Direction of responsibility**:
- AMC → AIMCC: Upload status reads (`GET {AIMCC_API_BASE_URL}/uploads/status`), quota reads (`GET {AIMCC_API_BASE_URL}/quota/current`), governance decision notifications (`POST {AIMCC_API_BASE_URL}/governance/decision`)
- AIMCC → AMC: No direct callbacks; AIMCC does not call AMC endpoints (status reads are AMC-initiated polling)

**Routing principles**:
- Upload status is read-only: AMC presents it as supervisory visibility
- Quota adjustments require approval workflow completion before AIMCC governance decision notification
- If AIMCC is unavailable during governance decision delivery: queue the notification for delivery on recovery; do not auto-process

**Non-bypass constraint enforcement**:
- AMC never calls any AIMCC ingestion endpoint
- Runtime bypass detection: `BOUNDARY_BYPASS_ATTEMPTED` audit event

**Degraded mode**: AIMCC health failure → enter AIMCC degraded mode. Status and quota data served from last-known cache with `stale: true, stale_since` marker. AIMCC governance actions frozen in `pending` state. KUC upload submissions queued with `queued_for_retry: true` (TRS TR-1603).

### 5.3 AMC ↔ Knowledge Upload Centre (KUC)

**Interaction pattern**: AMC is the submission surface for knowledge upload requests. KUC is the governed entry point.

**Direction of responsibility**:
- AMC → KUC: Upload submission (`POST {KUC_API_BASE_URL}/submit`) only
- KUC → AMC: No direct callbacks; KUC is a submission-only boundary from AMC perspective

**Routing principles**:
- All knowledge upload submissions from AMC context must POST exclusively to KUC API
- No direct path to AIMCC ingestion from AMC code
- AMC does not read upload processing status from KUC — it reads from AIMCC status API

**Non-bypass constraint enforcement**:
- Architecture enforces no AIMCC ingestion endpoint calls from AMC code (linting gate)

### 5.4 AMC ↔ Knowledge / Memory System

**Interaction pattern**: AMC is a read-only consumer of knowledge. It retrieves context and displays it with mandatory provenance.

**Direction of responsibility**:
- AMC → Knowledge System: Knowledge retrieval queries (`POST {KNOWLEDGE_API_BASE_URL}/retrieve`), health polling
- Knowledge System → AMC: No callbacks (read-only relationship)

**Routing principles**:
- All knowledge queries must include `require_provenance: true`
- AMC never writes to knowledge/memory system
- Local cache maximum TTL: 5 minutes with stale-at timestamp

**Non-bypass constraint enforcement**:
- No AMC table stores canonical knowledge content (schema enforced)
- Cache invalidated immediately on knowledge system degradation

**Degraded mode**: Knowledge system health failure → all cached items marked stale; retrieval endpoints return HTTP 503; all knowledge reference surfaces show unavailable indicator (TRS TR-1604).

### 5.5 AMC ↔ Foreman / Governed Agents

**Interaction pattern**: AMC reads Foreman reporting data and dispatches intervention orders via Foreman. AMC receives intervention status callbacks.

**Direction of responsibility**:
- AMC → Foreman: Intervention dispatch (`POST {FOREMAN_API_BASE_URL}/api/foreman/dispatch-intervention`), build status reads (`GET {FOREMAN_API_BASE_URL}/reporting/build-status`)
- Foreman → AMC: Intervention status callbacks (`POST /api/interventions/{id}/status-update`)
- AMC → Specialist Agent: Workspace termination orders (`POST {SPECIALIST_AGENT_API_BASE_URL}/workspaces/{id}/terminate`)
- Specialist Agent → AMC: Status callbacks (`POST /api/interventions/{id}/status-update`)

**Routing principles**:
- AMC reads Foreman reporting feed as read-only; AMC does not issue build commands (TRS TR-1101)
- Intervention dispatch is unidirectional (AMC → Foreman/agent); acknowledgment (HTTP 202) required
- Callback validation: Foreman/agent callback must include service token in Authorization header

**Non-bypass constraint enforcement**:
- AMC does not call Foreman command endpoints (no start build, no build control)
- Workspace termination requires approval gate for reserved-matter/authority-sensitive workspaces

### 5.6 Non-Bypass Enforcement Architecture

Non-bypass constraints are enforced at four layers:

| Enforcement Layer | Mechanism | Constraints Enforced |
|---|---|---|
| **Dependency scan (CI gate)** | CI step checks `package.json` for forbidden AI SDK packages | TR-BOUNDARY-001: No AI model SDK |
| **Startup validation** | Application startup check for required env vars and URL configuration | TR-1505: No hardcoded URLs; missing config prevents startup |
| **API middleware** | Server-side authority checks; service token validation on all callback endpoints | TR-1404: Authority domains; TR-1405: Inter-service trust |
| **Runtime detection** | Event-driven monitoring; boundary bypass events write Critical audit event + alert | TR-504: AIMC bypass; TR-604: AIMCC ingestion bypass |

---

## 6. State, Audit, and Resilience Architecture

### 6.1 State Consistency Architecture

**Canonical state ownership**: All AMC executive state is owned by AMC-owned Supabase tables. No external service may directly modify AMC-owned state. External state mutations must arrive via AMC callback endpoints with validated service identity.

**State mutation propagation**: Every state mutation (alert acknowledgment, approval decision, intervention status change) must propagate via Supabase Realtime broadcast to all connected AMC sessions. Channel: `amc_executive_state_{user_id}`. Local component state must update immediately on Realtime event — no stale-while-revalidate pattern that surfaces contradictory states.

**Transactional integrity**: Consequential database operations (action + audit event pair) are executed within a single database transaction. If either fails, both are rolled back (TRS TR-1305).

**Idempotency**: All decision endpoints (approval, ARC resolution, alert acknowledgment) enforce idempotency. If already decided: return HTTP 409 with current state. No double-processing of identical requests.

### 6.2 Cross-Device / Cross-Session Continuity

**Architecture**: Cross-device continuity is provided by the combination of:
1. Server-side state persistence in Supabase tables (not client-local only)
2. Supabase Realtime channel subscriptions per authenticated user — all devices for a user subscribe to the same channels
3. Session restore re-fetch protocol: on AMC load, all critical state domains are fetched from server APIs

**Session restore architecture** (TRS TR-1703): On session restore, AMC frontend must fetch fresh data from:
- `GET /api/dashboard/summary` — current health state
- `GET /api/alerts?status=active` — current alert state
- `GET /api/approvals?status=pending` — approval queue
- `GET /api/interventions?status=active` — intervention state
- `GET /api/conversation/messages?limit=20` — conversation history

If any fetch fails: explicit error indicator rendered — no silent fallback to last-known local state as current.

**Conversation continuity**: Conversation messages stored server-side in `conversation_messages` table. All devices for a user subscribe to `amc_conversation_{session_id}` channel. Message acknowledgment events delivered across devices within 2 seconds.

### 6.3 Audit / Provenance Recording Architecture

**Audit atomicity**: Every consequential action (state mutation + audit event) executes in a single database transaction. Partial writes (action committed but audit event missing) are prohibited (TRS TR-1305).

**Append-only guarantee**: `audit_events` table enforces INSERT-only via RLS policy at the database layer. No application code may issue UPDATE or DELETE against `audit_events`. This is enforced at the Supabase RLS policy level, not only at the API layer.

**Cross-system audit linkage**: When AMC dispatches an action to an external service, the resulting audit event includes `cross_system_ref` pointing to the external service reference. This enables full provenance chain reconstruction across systems.

**Knowledge provenance**: All knowledge references displayed in AMC must include provenance metadata from the knowledge retrieval response. Anonymous knowledge display is architecturally prohibited — rendering knowledge content without provenance triggers an audit event for the provenance gap.

### 6.4 Degraded-Mode Behavior Architecture

**Dependency health monitoring**: The `amc-health-poll-scheduler` function polls AIMC, AIMCC, and Knowledge System health endpoints every 30 seconds. Degraded mode is entered immediately on non-200 response or unavailability — there is no grace period.

**Degraded mode state propagation**: On degraded mode entry for any dependency, the following executes atomically:
1. `system_health_events` row inserted with `event_type: "degraded"`
2. Dependency-specific audit event written (`AIMC_DEGRADED`, `AIMCC_DEGRADED`, `KNOWLEDGE_SYSTEM_DEGRADED`)
3. Supabase Realtime broadcast to all connected sessions: `{ event: "system_degraded", dependency: "<name>", detected_at }`
4. Dependency-specific behavior rules applied (per TRS TR-1602, TR-1603, TR-1604)

**Degraded mode behavioral rules by dependency**:

| Dependency | Degraded Behavior |
|---|---|
| **AIMC unavailable** | All AIMC dispatch attempts return `{ blocked: true, reason: "aimc_degraded" }`. `POST /api/aimc/*` returns HTTP 503. Maturion Proactive Panel renders exact required string. No fallback AI call path. |
| **AIMCC unavailable** | Quota and upload reads return last-cached data with `stale: true, stale_since`. AIMCC governance actions remain `pending`. KUC upload submissions queued with `queued_for_retry: true`. |
| **Knowledge System unavailable** | All cached knowledge items immediately marked stale. Knowledge retrieval returns HTTP 503. All knowledge reference surfaces show unavailable indicator. |
| **Foreman unavailable** | Foreman reporting feed displays `{ status: "unavailable", last_known_at }` per job. Intervention dispatch returns HTTP 503 with explicit error. |

**No silent failures**: Every degraded mode entry, every failed external call, and every SLA breach must produce an observable audit event or alert. Silent suppression is architecturally prohibited.

### 6.5 Recovery and Stale-Data Signaling Architecture

**Recovery detection**: Health polling detects recovery when the next health check returns HTTP 200 with `{ status: "healthy" }` after a degraded period.

**Recovery procedure**:
1. Update `system_health_events` row: set `recovered_at`, `event_type: "recovered"`
2. Write dependency-specific recovery audit event (`AIMC_RECOVERED`, etc.)
3. Broadcast `{ event: "system_recovered", dependency: "<name>", recovered_at }` via Realtime
4. Resume normal operation for the recovered dependency

**Stale data signaling**: Any data item served from cache after a dependency's degraded mode entry must carry:
- `stale: true` flag in API response
- `stale_since: <detected_at>` timestamp
- UI surface must display explicit staleness indicator — not present stale data as current

---

## 7. Trust Boundaries and Authority Boundaries

### 7.1 Trust Boundary Map

```
┌───────────────────────────────────────────────────────────────┐
│                    TRUST ZONE: AMC OWNED                       │
│                                                                │
│  Next.js API Layer + Supabase PostgreSQL + Supabase Auth       │
│  All AMC-owned tables; all API routes; auth session tokens     │
│                                                                │
│  Trust anchor: JWT from Supabase Auth (human actors)           │
│  Trust anchor: Service token per external system               │
│  RLS enforcement: all tables                                   │
└───────────────────┬───────────────────────────────────────────┘
                    │ HTTPS + Service Token
        ┌───────────┼────────────────────┐
        │           │                    │
   ┌────▼───┐  ┌────▼───┐  ┌────────────▼────┐
   │  AIMC  │  │ AIMCC  │  │ Knowledge/Foreman│
   │  Trust │  │  Trust │  │  Trust Boundary  │
   │ Zone   │  │  Zone  │  │                  │
   └────────┘  └────────┘  └─────────────────┘
```

**Trust rules**:
- AMC trusts AIMC for AI execution; AIMC does not receive direct database access
- AIMC callbacks to AMC are validated via shared `AIMC_SERVICE_TOKEN`
- AIMCC callbacks are NOT expected (AMC polls AIMCC, not the reverse)
- Foreman callbacks validated via `FOREMAN_SERVICE_TOKEN`
- Specialist agent callbacks validated via `SPECIALIST_AGENT_SERVICE_TOKEN`
- No external service token grants elevated trust or cross-service access
- All inbound callbacks must match `actor_type` to registered service identity

### 7.2 Authority Boundary Map

| Boundary | Authorized Actors | Scope | Enforcement |
|---|---|---|---|
| `reserved_matter` | Johan Ras (`human` actor type only) | Ultimate executive decisions; quota changes; reserved approvals; boundary-bypass acknowledgments | Server-side; HTTP 403 on violation |
| `delegated` | Maturion (`ai_executive`) within approved scope | Operational AI executive decisions within configured delegated scope | Server-side via `authority_domain_config` table; HTTP 403 on scope violation |
| `operational` | Any authenticated executive actor | Standard executive operations | JWT auth mandatory; RLS enforced |

**Authority boundary enforcement invariant**: Server rejects unauthorized actors regardless of client-side UI presentation. No client-side-only authority enforcement.

---

## 8. Deployment-Shaping Architectural Decisions

The following architectural decisions have been made at Stage 5 that shape the deployment and build approach for Stage 12. These are binding decisions.

> **TRS §25 Deferral Resolution Summary**: TRS §25 listed 16 items deferred from Stage 4 to Stage 5 Architecture. This section resolves 9 of those 16 items (API framework, background scheduler, push notification provider, deployment platform, authority domain config storage, per-domain health computation, approval queue ordering, alert history endpoint, deferral reminder scheduling, and Foreman reporting feed format). The remaining 7 TRS §25 items (column DDL, React component tree, Realtime subscription implementation, ARC table DDL, ARC Realtime wiring, alert timing SLA monitor implementation, and ARC stale-item scheduling implementation) are correctly deferred onward to schema-builder, ui-builder, and api-builder as implementation-stage responsibilities. See `trs-to-architecture-traceability.md` §4 for full resolution status.

| Decision | Value | Rationale | TRS Deferral Resolved |
|---|---|---|---|
| **API Framework** | Next.js App Router API Routes | Unified deployment with React frontend; native Supabase integration; no separate REST server process required | TRS §25 (API server framework) |
| **Background Scheduler** | Supabase Edge Functions (cron-trigger) | Native Supabase integration; no external scheduler service required | TRS §25 (Background scheduler) |
| **Push Notification Provider** | Web Push API (PWA) + FCM (Android) + APNs (iOS); unified dispatch client | Covers all platform targets; unified client abstracts channel selection | TRS §25 (Push notification provider) |
| **Deployment Platform** | Vercel (recommended); any Node.js host supporting Next.js 14+ | Next.js-native; avoids lock-in; production-proven for this stack | TRS §25 (Deployment infrastructure) |
| **Authority Domain Config Storage** | Supabase table `authority_domain_config` (runtime-configurable) | Runtime-manageable without code changes; auditable changes | TRS §25 (Authority delegated-domain config) |
| **Health Status Computation** | Per-domain computation rules defined in architecture; aggregated by `amc-health-poll-scheduler` | Dashboard domain health aggregated from `system_health_events` + dependency health API responses | TRS §25 (Per-domain health computation) |
| **Per-Domain Health Status Computation** | Each health domain aggregates from its contributing `system_health_events` records: System Health = scheduler + database; Execution Health = AIMC + interventions; Governance Health = approvals + ARC; Security = auth events + boundary bypass events; Compliance = audit completeness + quota compliance | Explicit computation rules for each of the five dashboard health domains (TR-101) | TRS §25 (Per-domain health computation) |
| **Approval Queue Priority Ordering** | `approvals` ordered by: `reserved_matter` → deadline ASC → `delegated` → `operational`; within same authority boundary: deadline ASC, then `created_at` ASC | Priority-first ordering ensuring reserved matters surface above delegated and operational | TRS §25 (Priority/deadline ordering) |
| **Alert History Endpoint** | `GET /api/alerts` with `?status=all` or `?status=dismissed|resolved` query parameters | Extends the base endpoint with status filter for history view | TRS §25 (Alert history view API) |
| **Deferral Reminder Scheduling** | `amc-approval-arc-timeout-checker` Edge Function checks `deferred` approvals for `follow_up_at` reminder | Alerts generated T-24h before `follow_up_at` | TRS §25 (Deferral reminder scheduling) |
| **Foreman Reporting Feed Format** | `GET {FOREMAN_API_BASE_URL}/reporting/build-status` response format: `{ active_jobs: [{ job_id, stage, status, started_at, assigned_agent }] }` | AMC expects this contract; Foreman must implement it | TRS §25 (Foreman reporting format) |

---

## 9. Deferred to Stage 6

The following items are explicitly deferred from Stage 5 Architecture to Stage 6 QA-to-Red and beyond. Deferral does not indicate descoping — these are Stage 6 and builder responsibilities.

| Deferred Item | Stage 6 / Builder Responsibility | Architecture Constraint Applied |
|---|---|---|
| Database column types and index DDL | schema-builder (Stage 6 QA-to-Red → Stage 12 Build) | Column names and constraints defined in TRS §4–§21; DDL implements these exactly |
| React component tree and UI component design | ui-builder (Stage 6 QA-to-Red → Stage 12 Build) | Route list, responsive breakpoints, and surface-level requirements defined (TRS TR-104, TR-1201) |
| CI script implementation | Stage 12 Build | CI gate structure defined in §3.8; scripts are Stage 12 |
| API code implementation | api-builder (Stage 12 Build) | All API contracts defined in TRS §22; no code here |
| Realtime channel subscription implementation | api-builder (Stage 12 Build) | Channel names and event patterns defined in §3.5 |
| Test specifications | Stage 6 QA-to-Red | Stage 5 defines architecture; Stage 6 derives Red test suite |
| Push notification device registration implementation | integration-builder (Stage 12 Build) | Architecture pattern defined in §3.7 |
| `arc_classifications` table DDL | schema-builder | Minimum column set defined in TRS TR-1806; DDL is Stage 12 |
| AIMC health check failure retry logic | api-builder | Retry not required before switching to degraded mode (immediate on non-200) |
| `push_device_registrations` table DDL | schema-builder | Architecture notes ancillary table; DDL is Stage 12 |

---

## 10. Sign-Off / Approval Record

| Field | Value |
|---|---|
| **Document** | AMC Architecture Specification — Stage 5 |
| **Version** | 1.0 |
| **Prepared by** | foreman-v2-agent (POLC_ORCHESTRATION) |
| **Prepared Date** | 2026-04-26 |
| **CS2 Authorization for Stage 5** | app_management_centre#1131 |
| **Stage 4 TRS Reference** | `modules/amc/03-trs/technical-requirements-specification.md` v1.1 (treated as approved per #1131) |
| **Wave** | amc-stage5-architecture-20260426 |
| **Reviewed by** | *Pending CS2 review* |
| **Approved by** | *Pending CS2 approval* |
| **Approval Date** | *Pending* |
| **Approval Reference** | *To be assigned by CS2 on approval* |
| **Stage** | Stage 5 of 12 — Architecture |
| **Next Stage** | Stage 6 — QA-to-Red (blocked until CS2 approves Stage 5) |

### Version History

| Version | Date | Change Summary |
|---|---|---|
| 1.0 | 2026-04-26 | Initial production — complete Stage 5 Architecture covering all 5 mandatory inclusion areas: core architecture structure, AMC domain architecture (ARC + Dynamic Upload Quota + contract surfaces), cross-system interaction architecture, state/audit/resilience architecture, traceability to TRS |

### Approval Basis Required

CS2 approval of this document confirms:
1. The Architecture Specification is clear, comprehensive, architecturally explicit, and non-contradictory
2. AMC ↔ AIMC ↔ AIMCC ↔ KUC ↔ knowledge/memory cross-system boundaries are preserved and architecturally enforced
3. ARC is explicitly recognized as a first-class architectural domain with dedicated table, API namespace, route, audit family, and Realtime channel
4. Dynamic Upload Quota Management is architecturally defined as an operational management console capability, not merely supervisory visibility
5. Alert/escalation/audit/state/auth contract-level control surfaces are explicitly reflected in the architecture
6. All 18 TRS domain families are architecturally realized in this specification (verified by traceability artifact)
7. No TRS requirement family is silently dropped
8. Stage 6 QA-to-Red is authorized to derive its Red test suite from this Architecture Specification

### CS2 Approval Instruction

To formally approve this Architecture Specification:
- Record approval in a Stage 5 approval artifact at `modules/amc/04-architecture/architecture-approval.md`
- Reference this document: `modules/amc/04-architecture/architecture-specification.md` v1.0
- Update `modules/amc/BUILD_PROGRESS_TRACKER.md` Stage 5 status to `✅ COMPLETE — CS2 APPROVED`
- Authorize commencement of Stage 6 QA-to-Red

---

*End of Architecture Specification — Stage 5 v1.0. Produced by foreman-v2-agent under POLC_ORCHESTRATION. CS2 approval required before Stage 6 QA-to-Red derivation begins.*

# UX Workflow & Wiring Spec — Stage 2

**Stage**: 2 — UX Workflow & Wiring Spec
**Module**: App Management Centre (AMC)
**Version**: 1.1
**Status**: ✅ Approved — CS2-approved (issue #1121, 2026-04-22). Harmonization pass 2026-04-23.
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: app_management_centre#1121 (original); harmonization issue (harmonization pass)
**Upstream Source**: `modules/amc/00-app-description/app-description.md` v1.1 (approved 2026-04-22; harmonization pass 2026-04-23)
**Canonical Location**: `modules/amc/01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md`

---

> **DERIVATION DECLARATION**
> This document derives directly from the approved Stage 1 App Description (`modules/amc/00-app-description/app-description.md` v1.1, CS2-approved 2026-04-22, harmonization pass 2026-04-23). It does not invent product truth. Every major section is traceable to a corresponding Stage 1 section. **Harmonization pass (2026-04-23)**: Explicit ARC Governance Console journey (§4.4.1) and Dynamic Upload Quota Management Console journey (§4.6.1) added to reflect Stage 1 v1.1 AMC Technical/Operating Domain Declaration and §2 In Scope additions.

---

## Table of Contents

1. [Purpose & Scope](#1-purpose--scope)
2. [Cross-System Boundary Definitions](#2-cross-system-boundary-definitions)
3. [Actor Model](#3-actor-model)
4. [Primary User Journeys](#4-primary-user-journeys)
   - 4.1 Executive Estate Oversight
   - 4.2 Alert Review & Handling
   - 4.3 Approval Workflow
   - 4.4 Intervention Launch & Monitoring
     - 4.4.1 ARC Governance Console Journey
   - 4.5 AI-Routed Actions (AIMC)
   - 4.6 Knowledge Upload / Ingestion Supervision (AIMCC / KUC)
     - 4.6.1 Dynamic Upload Quota Management Console Journey
   - 4.7 Memory-Aware / Knowledge-Aware Operating View
   - 4.8 Executive Conversation with Maturion
5. [Secondary User Journeys](#5-secondary-user-journeys)
   - 5.1 Specialist Agent Workspace Oversight
   - 5.2 Maintenance & Assurance Reporting
   - 5.3 Estate Configuration & Wellbeing
   - 5.4 Mobile Continuity
6. [Screen / Surface Model](#6-screen--surface-model)
7. [Wiring Model](#7-wiring-model)
8. [Cross-System Integration Wiring](#8-cross-system-integration-wiring)
9. [Degraded-Mode Operating Patterns](#9-degraded-mode-operating-patterns)
10. [Stage 1 Traceability Index](#10-stage-1-traceability-index)

---

## 1. Purpose & Scope

### 1.1 Purpose

This Stage 2 UX Workflow & Wiring Spec defines:

- the user and system journeys through which AMC's executive, supervisory, and governance functions are experienced
- the screen / surface model for each major operating surface
- the explicit wiring between UI events, backend routes, data tables, external services, and audit outputs
- the cross-system integration boundaries between AMC, AIMC, AIMCC, Knowledge Upload Centre, and the knowledge / memory system

This document is the governing UX truth from which FRS (Stage 3) functional requirements will be derived. FRS authors must derive from this document without inventing new UX or wiring patterns.

### 1.2 Scope

**In scope for Stage 2:**
- All primary executive user journeys (Johan Ras / Maturion operating surfaces)
- Alert review and handling flows
- Approval and reserved-matter workflows
- Intervention launch and monitoring flows
- AIMC-mediated AI action surfaces
- AIMCC / Knowledge Upload Centre supervision surfaces
- Knowledge-aware operating views (with provenance)
- Two-way conversation surface with Maturion
- Specialist agent oversight surfaces
- Maintenance and assurance reporting surfaces
- Mobile and cross-device operating patterns
- Degraded-mode operating patterns for each external dependency
- Cross-system wiring between AMC, AIMC, AIMCC, KUC, and knowledge / memory system

**Explicitly out of scope for Stage 2:**
- Implementation code (Stage 12)
- Technical architectural decisions (Stage 5)
- Detailed API contract definitions (TRS Stage 4 / Architecture Stage 5)
- Test specifications (Stage 6 QA-to-Red)
- Database schema definitions (Stage 5 / Stage 4 TRS)

> Stage 1 Traceability: §2 Scope Definition

---

## 2. Cross-System Boundary Definitions

These boundaries are non-negotiable and must be preserved in all surfaces and wiring defined in this document.

> Stage 1 Traceability: §1 Executive Layer Boundary Definitions, §2 AMC/AIMC/AIMCC Boundary

| Layer | Operating Role in UX | What AMC Shows / Does | What AMC Does NOT Do |
|---|---|---|---|
| **AMC** | Executive supervisory surface and operating environment | Presents executive visibility, alerts, approvals, conversations, interventions, and oversight surfaces | Executes AI models, ingests knowledge, stores persistent memory truth |
| **AIMC** | Sole governed AI execution gateway | Routes AI requests, surfaces AI outcomes and status | Is accessed directly by AMC UI without AIMC API routing |
| **AIMCC** | Knowledge ingestion and memory operations layer | Surfaces ingestion status, upload outcomes, knowledge-management state | Owns persistent knowledge/memory truth; is bypassed by AMC |
| **Knowledge Upload Centre (KUC)** | Governed ingestion entry point | AMC surfaces upload status sourced from KUC/AIMCC | Accepts direct uploads from AMC without KUC routing |
| **Knowledge / memory system** | Persistent knowledge and memory substrate | AMC surfaces retrieved knowledge references with provenance | Is silently duplicated or privately cached inside AMC |

**Non-bypass rule**: Every AI action from AMC must route through AIMC. Every knowledge ingestion/upload from AMC must route through KUC/AIMCC. AMC must not implement direct pathways around these governed layers.

---

## 3. Actor Model

> Stage 1 Traceability: §1 Target Users/Audience, §13 Agent Authority Chain

| Actor | Role in AMC UX | Entry Pattern | Authority Level |
|---|---|---|---|
| **Johan Ras** | Constitutional human authority; primary executive user | Authenticated login; all surfaces accessible | Full authority — reserved matters, all approvals |
| **Maturion** | Resident AI executive; proactive estate intelligence | AI-driven interaction via AIMC; surfaces decisions and alerts | Delegated operational authority; escalates reserved matters to Johan |
| **Foreman** | Supervised orchestration authority | Backend reporting into AMC; no direct AMC login | Operational scope only; visible via execution reporting surfaces |
| **IAA agents** | Independent assurance layer | Report findings into AMC via governed pathways | Advisory / assurance outputs visible in reporting surfaces |
| **Specialist agents** | Domain-specific workers | Sandboxed; visible via specialist oversight surface | Task-scoped; AMC surfaces their status, not their internal state |
| **Maintenance agents** | Upkeep, health checks, diagnostics | Reporting via governed pathways | Status visible in maintenance reporting surface |

---

## 4. Primary User Journeys

### 4.1 Journey: Executive Estate Oversight

> Stage 1 Traceability: §1 Core Value Proposition, §23 Dashboard and Drill-Down Pattern, §3 Operating Success Measures

**Purpose**: Give Johan Ras and Maturion a persistent, real-time view of the overall health and state of the Maturion estate — system health, governance health, execution health, security posture, and compliance posture — without requiring manual interrogation.

**Primary Actor**: Johan Ras (primary), Maturion (co-presenting estate intelligence)  
**Entry Point**: AMC Home / Executive Dashboard (default landing surface after auth)

**Journey Steps**:

1. User authenticates (Supabase Auth → JWT validated)
2. Executive Dashboard loads — Maturion surfaces current estate health summary
3. Health tiles displayed: System Health | Execution Health | Governance Health | Security | Compliance
4. Critical / High alerts visible immediately in Alert Panel (top priority section)
5. User can see at-a-glance: active approvals awaiting, active interventions, AI action status
6. Maturion proactive panel surfaces current AI-detected estate summary (if new insight since last session)
7. User can drill into any health tile → surfaces sub-surface for that domain (e.g. Execution Health → Execution Monitor)
8. User can navigate to Alert Centre, Approval Queue, Intervention Manager from dashboard nav

**Wiring summary**: See §7.1 Executive Dashboard wiring.

**UX Requirements derived from Stage 1**:
- Dashboard must not be a passive report gallery (§23 Prohibited UX Patterns)
- Proactive awareness panel must surface important matters before user asks (§23 Proactive Awareness Requirement)
- Mobile must support full estate overview with action paths (§23 Mobile and Cross-Context Responsiveness)

---

### 4.2 Journey: Alert Review and Handling

> Stage 1 Traceability: §23 Notification Classes, §23 Alert Class and Priority Framework, §3 Executive Alerting

**Purpose**: Surface, categorize, and drive to resolution all alerts generated across the estate — from informational to critical — with explicit acknowledgment, escalation, and audit recording.

**Primary Actor**: Johan Ras (final acknowledger for Critical/High), Maturion (first-pass synthesizer)  
**Entry Point**: Alert Centre (nav: Dashboard Alert Panel → full Alert Centre, or direct nav)

**Journey Steps**:

1. User navigates to Alert Centre
2. Alerts displayed in priority order: Critical | High | Medium | Low/Informational
3. Each alert shows: alert class, source system, summary, timestamp, acknowledgment status, escalation status
4. User selects an alert → Alert Detail view opens
5. Alert Detail shows: full description, originating system/actor, timeline, linked approval or intervention (if any), context references
6. User can take actions on alert:
   - **Acknowledge**: marks alert as acknowledged with actor + timestamp (recorded in audit trail)
   - **Escalate**: routes alert to escalation flow (creates escalation record, notifies escalation target)
   - **Dismiss** (Low/Informational only): marks alert dismissed with reason
   - **Link to Approval**: opens approval creation flow with alert context pre-populated
   - **Link to Intervention**: opens intervention creation with alert context pre-populated
7. Unacknowledged Critical alerts: escalation timer visible; if timer expires → escalation event fires automatically
8. Alert history accessible: all past alerts with final status visible to authorized actors

**Wiring summary**: See §7.2 Alert Review and Handling wiring.

**UX Requirements derived from Stage 1**:
- Critical alerts must interrupt operator even on mobile (§23 Alert Class and Priority Framework)
- Acknowledgment is explicit actor action, not implicit on view (§23 Acknowledgment)
- Alert expiry must not silently resolve underlying condition (§23 Retry / Expiry)
- Reserved-matter approvals must not be buried inside generic notifications (§23 Approval-Centred UX)

---

### 4.3 Journey: Approval Workflow

> Stage 1 Traceability: §23 Approval-Centred UX, §13 Constitutional Authority, §3 Approval / Intervention Flows

**Purpose**: Route governance-sensitive and reserved-matter decisions to the correct authority, present full context for the decision, capture the explicit decision with audit record, and unblock or reject the awaiting action.

**Primary Actor**: Johan Ras (reserved matters, final approver), Maturion (delegated approvals within explicitly approved domains)  
**Entry Point**: Approval Queue (nav from dashboard, from alert, or from notification)

**Journey Steps**:

1. Approval item surfaces in Approval Queue (originated from: AI action requiring approval, governance action awaiting decision, intervention requiring executive sign-off, reserved-matter change)
2. Approval Queue shows: pending items, priority, originating source, authority boundary type, deadline/timeout if applicable
3. User selects approval item → Approval Detail view opens
4. Approval Detail shows:
   - What is being proposed (explicit, not vague)
   - Why it is being proposed (context and rationale)
   - Which authority boundary applies (reserved matter / delegated / operational)
   - Consequence of approval (what will happen)
   - Consequence of rejection or delay (what will not happen / risk)
   - Supporting evidence or context (linked artifacts, AI reasoning summary if AIMC-sourced)
5. User takes decision:
   - **Approve**: approval recorded with: actor, timestamp, approval basis, outcome → approval event fires → blocked action unblocked
   - **Reject**: rejection recorded with: actor, timestamp, rejection reason → blocked action cancelled or escalated
   - **Defer with note**: defers decision, records note, sets follow-up reminder
   - **Request Clarification**: opens conversation thread with Maturion or originating agent for clarification before deciding
6. Audit record created: every approval/rejection is a traceable audit event (actor, timestamp, basis, outcome)
7. Post-approval: user sees confirmation of action unblocked + audit reference
8. Post-rejection: user sees confirmation of action cancelled + audit reference

**Wiring summary**: See §7.3 Approval Workflow wiring.

**UX Requirements derived from Stage 1**:
- Reserved-matter approvals must never be disguised as routine task prompts (§23)
- Every governance-sensitive action requiring approval must be blocked until approval is explicitly granted (§3)
- Approval decisions are recorded with actor, timestamp, basis, and outcome (§3)

---

### 4.4 Journey: Intervention Launch and Monitoring

> Stage 1 Traceability: §23 Escalation and Intervention Pattern, §3 Operating Success Measures, §2 In Scope

**Purpose**: Allow Johan Ras or Maturion (within delegated scope) to initiate a governed intervention against an estate condition, track it through to completion or cancellation, and capture full audit trail of the intervention lifecycle.

**Primary Actor**: Johan Ras (all interventions), Maturion (delegated-scope interventions)  
**Entry Point**: Intervention Manager (nav from Alert Centre, from Approval Queue, from Executive Dashboard, or direct nav)

**Journey Steps**:

1. User navigates to Intervention Manager or opens intervention from an alert/approval
2. Active interventions list shows: in-progress interventions with status, owner, timeline
3. User initiates new intervention:
   - Selects intervention type (predefined intervention catalogue or custom)
   - Defines scope: target system/agent/module, description of issue, intended outcome
   - Specifies authority level: requires approval? Reserved matter? Delegated?
   - Submits → if approval required: intervention enters Approval Queue before execution
4. Approved intervention: enters execution state
   - AMC routes intervention order through governed pathway (Foreman / specialist agent / target system)
   - AMC surfaces execution status in real-time: queued → in progress → completed / failed
5. Intervention Detail shows throughout lifecycle: timeline, current step, executing agent, error state if any
6. User can: Cancel intervention (with reason, recorded), Add note, Escalate if stalled
7. On completion: completion record created with: outcome, duration, executing agent, audit reference
8. On failure: failure record created; user prompted to decide: retry / escalate / close with note

**Wiring summary**: See §7.4 Intervention Launch and Monitoring wiring.

**UX Requirements derived from Stage 1**:
- AMC must confirm that intervention entered governed execution path (§23 Escalation and Intervention Pattern)
- Intervention actions are traceable from initiation through to completion or cancellation (§3)
- Intervention visibility must persist until completion or explicit closure

---

### 4.4.1 ARC Governance Console Journey

> Stage 1 Traceability: §4 Original AMC Intent Reconciliation (ARC Trigger Governance), §4 AMC Technical/Operating Domain Declaration (ARC Governance Console), §2 In Scope (ARC governance console)
> **Harmonization Pass 2026-04-23**: Added to make ARC explicitly recognizable as a first-class named AMC technical operating domain.

**Purpose**: Provide a dedicated, explicitly named ARC Governance Console surface through which Johan Ras can initiate, review, approve, and audit ARC (Automated Response Control) triggered governance actions. ARC actions are distinct from generic interventions — they are automated-response-triggered governance events that require human executive decision and audit trail.

**Primary Actor**: Johan Ras (all ARC approvals and decisions); Maturion (ARC detection and surface triggering)
**Entry Point**: ARC Governance Console (dedicated nav item; also reachable from Alert Centre when an ARC-triggered alert surfaces)

**Journey Steps**:

1. User opens ARC Governance Console surface
2. Console shows: active ARC-triggered governance events, their detected condition, proposed automated response, current state (pending review / approved / rejected / escalated), and timestamps
3. Each ARC event entry shows:
   - Triggering condition (what ARC detected)
   - Proposed automated response
   - Current state
   - Priority level
   - Time since detection
4. User selects an ARC event → ARC Event Detail opens
5. ARC Event Detail shows:
   - Full trigger description and detection metadata
   - Proposed automated response (e.g., suppress, escalate, approve, reject, route)
   - Impact scope (which systems, agents, or data are affected)
   - Prior ARC actions in same context (audit chain)
   - Approval requirement and authority level
6. User decides:
   - **Approve ARC action**: ARC response is authorized; execution routed through governed pathway; audit event created
   - **Reject ARC action**: ARC response blocked; rejection reason required; audit event created
   - **Escalate**: ARC event escalated to Johan if not already at highest authority; escalation record created
   - **Defer**: ARC event deferred with note; follow-up scheduled
7. Decision recorded with: decision, decided_by, decided_at, basis/reason (required), audit reference
8. ARC event state updated; downstream ARC execution notified of outcome
9. All ARC events regardless of outcome are retained in the ARC audit history — never silently discarded

**Non-bypass invariant**: ARC actions requiring human approval must not auto-execute past the approval gate. ARC-triggered governance actions are not a bypass of AMC's approval model.

**Wiring summary**: See §7.4 ARC Governance Console wiring (appended to §7.4 table).

**UX Requirements derived from Stage 1**:
- ARC is an explicitly named, first-class AMC domain — not absorbed into generic intervention flows (§4 AMC Technical/Operating Domain Declaration)
- All ARC governance actions require explicit decision — no silent auto-execution past human gate (§3 Authority Constraints)
- ARC audit history is permanent and append-only (§26 Audit Log Design)
- ARC surface is accessible as a dedicated console, not buried in generic intervention list (§4 AMC Domain Declaration)

> Stage 1 Traceability: §18 AI Integration Requirements, §18 Multi-Layer AI Integration Model, §2 AMC/AIMC Boundary

**Purpose**: Allow AI-initiated or AI-supported actions to flow through AMC into AIMC for execution, with full governance, routing visibility, and audit capture. AMC surfaces AIMC action status but does not execute AI models directly.

**Primary Actor**: Maturion (AI-initiated), Johan Ras (oversight, approval where required)  
**Entry Point**: AI Action Monitor (nav from Executive Dashboard, or embedded in Conversation surface)

**Journey Steps**:

1. AI action originates from: Maturion conversation, Maturion proactive detection, specialist agent request, or user-initiated AI task
2. AMC creates AI action request record: action type, originating actor, AIMC route target, approval requirement flag
3. If approval required: action enters Approval Queue (see Journey 4.3)
4. If no approval required (or post-approval): action is dispatched to AIMC via governed API call
   - AMC records: dispatch timestamp, action ID, AIMC route, dispatch status
5. AIMC processes action → returns result to AMC
6. AMC surfaces result in AI Action Monitor: outcome, result summary, audit reference, timestamp
7. If AIMC unavailable: AMC enters AIMC degraded mode (see §9.1); user sees explicit degraded-mode notification
8. All AIMC interactions are recorded in audit trail: source, route, outcome, timestamp (no anonymous AI actions)

**Non-bypass invariant**: AMC must not execute AI model calls directly. The AIMC pathway is the only permissible route.

**Wiring summary**: See §7.5 AI-Routed Actions wiring.

**UX Requirements derived from Stage 1**:
- Zero AI model executions from AMC context that do not route through AIMC (§3)
- AIMC unavailability must be surfaced to operator with explicit degraded-mode behavior (§18)
- All AIMC-routed actions are recorded in audit trail (§3)
- AI must distinguish clearly between observation, recommendation, request, and decision (§23 AI-Mediated UX Discipline)

---

### 4.6 Journey: Knowledge Upload / Ingestion Supervision (AIMCC / KUC)

> Stage 1 Traceability: §2 AIMCC/KUC Boundary, §18 Multi-Layer AI Integration Model, §3 AIMCC/KUC Oversight

**Purpose**: Allow Johan Ras and Maturion to supervise the state of knowledge uploads and ingestion pipelines managed by AIMCC / Knowledge Upload Centre. AMC surfaces status, outcomes, and governance states; it does not bypass KUC/AIMCC.

**Primary Actor**: Johan Ras (governance approvals on ingestion), Maturion (ongoing oversight surfacing)  
**Entry Point**: AIMCC / Knowledge Supervision surface (nav from Executive Dashboard or dedicated nav item)

**Journey Steps**:

1. User opens AIMCC / Knowledge Supervision surface
2. Surface shows: active uploads, ingestion pipeline status, recent outcomes, pending governance actions
3. Upload items show: document name, submitter, submission time, KUC receipt status, AIMCC ingestion state, outcome
4. User can filter: by status (pending / in progress / complete / failed / rejected), by submitter, by time range
5. User selects an upload item → Upload Detail view opens
6. Upload Detail shows: upload metadata, KUC routing record, AIMCC ingestion progress/outcome, knowledge-system storage confirmation, audit reference
7. If governance action required (e.g., quota review, flagged content requiring approval):
   - Governance action surfaces in Approval Queue with upload context
   - User decides → decision recorded with audit trail
8. Dynamic upload quota state surfaced: current quota, usage, threshold warnings, approved quota changes
9. AIMCC unavailability: explicit degraded-mode notification; upload features enter degraded mode (see §9.2)

**Non-bypass invariant**: AMC must not initiate knowledge ingestion directly. All knowledge upload and ingestion actions route through KUC/AIMCC.

**Wiring summary**: See §7.6 AIMCC / KUC Supervision wiring.

**UX Requirements derived from Stage 1**:
- AMC surfaces upload status and ingestion outcomes sourced from AIMCC (§3)
- No unmanaged knowledge ingestion pathway exists within AMC (§3)
- AIMCC unavailability is handled gracefully with explicit degraded-mode behavior (§3)

---

### 4.6.1 Dynamic Upload Quota Management Console Journey

> Stage 1 Traceability: §4 Original AMC Intent Reconciliation (Dynamic Upload Quota Management), §4 AMC Technical/Operating Domain Declaration (Dynamic Upload Quota Management), §2 In Scope (Dynamic Upload Quota Management console)
> **Harmonization Pass 2026-04-23**: Added to make the quota management console explicitly recognizable as a first-class operational control surface, not merely a supervisory view within the AIMCC overview.

**Purpose**: Provide a dedicated, explicitly named Dynamic Upload Quota Management Console through which Johan Ras can view live quota state, initiate quota adjustment requests, approve or reject quota change proposals, receive proactive threshold warnings, and maintain a complete audit trail of all quota governance actions. This is a hands-on operational control surface — not a read-only display.

**Primary Actor**: Johan Ras (all quota decisions and approvals); Maturion (proactive quota alert surfacing)
**Entry Point**: Quota Management Console (accessible as a named panel within AIMCC/Knowledge Supervision surface AND as a dedicated nav item from the Executive Dashboard quota indicator)

**Journey Steps**:

1. User opens Quota Management Console (or navigates to the quota panel within AIMCC Supervision)
2. Console shows:
   - Current quota limit (total allocated quota in MB/GB)
   - Current usage (absolute and percentage)
   - Usage trend (last 7 days visual)
   - Threshold warning levels: Warning (configurable %, e.g. 75%), Critical (configurable %, e.g. 90%), Exceeded
   - Status of any pending quota change requests
   - Recent quota governance action history
3. Proactive threshold alerts: if usage crosses a configured threshold, a proactive alert surfaces automatically in the Alert Centre and in the Quota Management Console header
4. User can initiate a quota change request:
   - Specifies: new quota limit, justification, urgency
   - Request enters Approval Queue (FR-604/FR-607 — approval required for quota changes)
   - If user IS the authority (Johan Ras): can approve own request on the spot with audit trail
5. User reviews pending quota change requests in the console:
   - Approve: quota change authorized; AIMCC notified; audit event created
   - Reject: quota change blocked; rejection reason required; audit event created
   - Defer with note: follow-up scheduled
6. All quota governance actions (approve, reject, defer) create a complete audit record:
   - actor, action_type, old_quota, new_quota (if approved), basis/reason, timestamp, aimcc_notification_status
7. If AIMCC is unavailable: quota panel shows stale indicator with last-known values; new quota change submissions are blocked pending AIMCC recovery; stale data is NEVER served as current without explicit indicator

**Non-bypass invariant**: All quota change executions route through AIMCC. AMC records the decision and notifies AIMCC — it does not directly modify quota values in AIMCC storage.

**Wiring summary**: See §7.6 Quota Management Console wiring (appended to §7.6 table).

**UX Requirements derived from Stage 1**:
- Quota management is an operational console, not a read-only supervisory view (§4 AMC Technical/Operating Domain Declaration)
- All quota governance actions require explicit decision with audit trail (§26 Audit Log Design)
- Proactive threshold warnings must surface before explicit user inquiry (§3 Operating Success Measures)
- Quota data sourced from AIMCC — AMC does not own or locally manage quota values (§2 AMC/AIMC/AIMCC Boundary)

> Stage 1 Traceability: §2 Knowledge/Memory System, §3 Memory-Aware Operational Clarity, §24 Shared State Architecture

**Purpose**: Allow Johan Ras and Maturion to surface and interact with knowledge/memory references managed by the estate's knowledge/memory system — with provenance attribution, not as anonymous authoritative facts. AMC never becomes the canonical owner.

**Primary Actor**: Johan Ras, Maturion  
**Entry Point**: Knowledge Reference surface (accessible from Conversation, from specific context surfacing, or dedicated nav item)

**Journey Steps**:

1. User or Maturion initiates knowledge retrieval (e.g., "What does the estate know about X?")
2. AMC routes retrieval request via governed API to the knowledge/memory system
3. Knowledge/memory system returns references with provenance metadata (source document, ingestion date, confidence indicators, AIMCC tracking reference)
4. AMC surfaces retrieved knowledge with full provenance: source, ingestion path, retrieval timestamp
5. User can: view reference detail, follow provenance chain, request Maturion to synthesize or explain
6. AMC makes explicit: this is retrieved knowledge (not AMC-originated), with named provenance
7. Memory retrieval degradation: if knowledge/memory system is degraded → explicit degraded indicator shown on all knowledge surface items; user is not shown stale data as if it were current (see §9.3)
8. AMC does not silently cache or duplicate knowledge/memory truth beyond transient presentation state

**Non-bypass invariant**: AMC must not become the canonical long-term store of knowledge truth. All persistent knowledge/memory remains owned by the knowledge/memory system.

**Wiring summary**: See §7.7 Knowledge-Aware Operating View wiring.

---

### 4.8 Journey: Executive Conversation with Maturion

> Stage 1 Traceability: §23 Two-Way Conversational Interaction, §18 Executive AI Role, §23 AI-Mediated UX Discipline

**Purpose**: Provide a persistent two-way conversational surface through which Johan Ras and Maturion maintain ongoing executive dialogue — covering inquiry, proactive notification, clarification, approval requests, escalation, and action confirmation.

**Primary Actor**: Johan Ras (initiating user), Maturion (AI executive participant via AIMC routing)  
**Entry Point**: Conversation surface (persistent panel on Executive Dashboard; full-screen expansion available)

**Journey Steps**:

1. User opens Conversation surface (or it is pre-opened on dashboard)
2. Conversation history loads: recent exchanges, unread AI-initiated messages marked
3. User types or uses voice (where supported) to initiate an exchange with Maturion
4. Maturion responds via AIMC — response surfaces in conversation panel with:
   - response text
   - response type indicator: Observation | Recommendation | Request | Decision | Alert (§23 AI-Mediated UX Discipline)
   - source/reasoning summary where applicable
   - linked actions (e.g., link to approval item, intervention, alert)
5. Maturion-initiated proactive messages arrive in conversation even when user has not sent a message:
   - type: alert, recommendation, approval request, escalation request, status update
   - displayed with proactive indicator and priority level
6. User can: Reply, Acknowledge, Take linked action, Escalate, or Mark for follow-up
7. Conversation supports: executive inquiry, clarification dialogue, approval discussion, intervention planning
8. Every materially significant exchange generates an audit event (actor, timestamp, topic, linked action)
9. Conversation state is persistent across devices (session continuity — same conversation visible on mobile and desktop)

**Wiring summary**: See §7.8 Executive Conversation wiring.

**UX Requirements derived from Stage 1**:
- AI must distinguish clearly between observation, recommendation, request, and decision (§23)
- AI must not imply approval where approval has not been given (§23)
- Conversation state persistent across devices (§23 Mobile and Cross-Context Responsiveness)

---

## 5. Secondary User Journeys

### 5.1 Journey: Specialist Agent Workspace Oversight

> Stage 1 Traceability: §13 Specialist-Agent Layer, §18 Specialist-Agent Integration

**Purpose**: Give Johan Ras and Maturion visibility into specialist agent workspaces operating under AMC supervision, without absorbing the specialist workspaces into AMC's own state.

**Primary Actor**: Johan Ras, Maturion  
**Entry Point**: Specialist Agent Oversight surface (nav from Executive Dashboard)

**Journey Steps**:

1. User opens Specialist Agent Oversight surface
2. List of active and recent specialist agent workspaces displayed: name, type, scope, current status
3. User selects a workspace → Workspace Detail view opens
4. Workspace Detail shows: purpose, scope boundary, current status, active tasks, last reporting event, any escalations
5. User can: View output summary, Escalate issue to Maturion, Initiate intervention (routes to Intervention flow), Terminate workspace (if authority permits and intervention-approved)
6. Specialist agent outputs are surfaced — AMC shows outcomes, not internal specialist state
7. Sandbox isolation indicator always visible (workspace is bounded, cannot propagate outside approved boundaries)
8. Escalation from specialist workspace follows Escalation/Intervention wiring (§7.4)

---

### 5.2 Journey: Maintenance & Assurance Reporting

> Stage 1 Traceability: §2 In Scope (maintenance/assurance), §13 Maintenance and Operational Support Layer, §13 Independent Assurance Layer

**Purpose**: Surface health check results, scan outcomes, maintenance actions, and assurance findings through AMC's executive view, enabling proactive detection of estate health degradation.

**Primary Actor**: Johan Ras, Maturion  
**Entry Point**: Maintenance & Assurance Reports surface (nav from Executive Dashboard health tiles or direct nav)

**Journey Steps**:

1. User opens Maintenance & Assurance Reports surface
2. Reports shown: scheduled health checks, last run status, findings summary, assurance scan results
3. Items colour-coded by severity: all clear / advisory / warning / critical finding
4. User selects report → Report Detail view opens
5. Report Detail shows: findings, severity, recommended action, originating agent (maintenance or IAA), evidence reference
6. Critical findings automatically generate alerts in Alert Centre (Journey 4.2 triggered)
7. User can: Acknowledge finding, Create intervention from finding (routes to Intervention flow), Mark for follow-up, Export report reference
8. Assurance outputs (IAA verdicts, rejection packages where visible) shown separately from maintenance outputs — IAA independence preserved

---

### 5.3 Journey: Estate Configuration & Wellbeing

> Stage 1 Traceability: §2 In Scope (build/job initiation, operational wellbeing), §5 Build Lifecycle Stages

**Purpose**: Allow Johan Ras and Maturion to review estate configuration state, track active build and job execution, and manage estate-level wellbeing inputs within governed boundaries.

**Primary Actor**: Johan Ras (approvals), Maturion (operational oversight)  
**Entry Point**: Estate Configuration & Wellbeing surface (nav from Executive Dashboard)

**Journey Steps**:

1. User opens Estate Configuration & Wellbeing surface
2. Active build jobs and governance lifecycle stages visible with current status
3. Estate configuration summary: deployment state, active environment, key configuration parameters (read-only unless approved change)
4. User can: Request configuration change (triggers approval flow), Review active build status, View deployment wave status, Trigger approved maintenance action
5. Configuration changes require explicit approval (Approval Workflow Journey 4.3 — reserved matter handling)
6. Build/job visibility surfaces Foreman reporting in read-only mode (Johan oversees, does not directly control Foreman's orchestration)

---

### 5.4 Journey: Mobile Continuity

> Stage 1 Traceability: §23 Mobile and Cross-Context Responsiveness, §23 Desktop/Mobile Continuity

**Purpose**: Ensure Johan Ras can remain in meaningful executive contact with the estate from a mobile device, including live client and field contexts.

**Primary Actor**: Johan Ras  
**Entry Point**: Same AMC application on mobile browser / PWA (responsive layout, mobile-first critical paths)

**Journey Steps**:

1. User opens AMC on mobile (mobile-responsive layout activates)
2. Mobile landing view: condensed estate health summary + Alert Panel (most critical items surfaced immediately)
3. Critical alert: interrupts with push notification or in-app alert even on mobile
4. User can: Review alert detail, Acknowledge alert, Approve/Reject from mobile approval view
5. Mobile approval view: concise but complete — what / why / consequence — rapid approval/rejection path
6. Mobile conversation: Maturion conversation accessible with compressed layout; full exchange history available
7. Mobile interventions: can initiate and monitor interventions from mobile (approve to launch)
8. Session continuity: state synchronized between mobile and desktop — action taken on mobile is visible immediately on desktop and vice versa

**UX Requirements derived from Stage 1**:
- Mobile must not merely mirror desktop visuals — must support real executive action (§23)
- Alert state consistent across desktop and mobile (§23 Desktop/Mobile Continuity)
- Context preserved when switching devices or locations (§23)

---

## 6. Screen / Surface Model

| Screen / Surface | Purpose | Primary Actor | Entry Point | Key UI Components | Outputs Shown | Actions Available | Navigation / Transition Rules |
|---|---|---|---|---|---|---|---|
| **Login** | Authenticate user to AMC | Johan Ras | Direct URL / app launch | Login form (email/password), Supabase Auth redirect, MFA prompt if enabled | Auth error states | Submit credentials, MFA entry | On success: → Executive Dashboard. On failure: error message + retry. |
| **Executive Dashboard** | Central estate overview — proactive executive awareness | Johan Ras, Maturion | Default post-auth landing | Health tiles (5 domains), Alert Panel, Approval count badge, Maturion proactive panel, Nav sidebar | Estate health summary, active alerts count, active approvals count, active interventions count | Drill into any health tile, open Alert Centre, open Approval Queue, open Conversation, open Intervention Manager | All other surfaces accessible from sidebar nav. Maturion proactive messages auto-surface. |
| **Alert Centre** | Review, acknowledge, escalate, and action all estate alerts | Johan Ras | From dashboard Alert Panel, sidebar nav, notification tap | Alert list (priority-ordered), alert filters, alert detail panel | All active and historical alerts, priority labels, acknowledgment status, escalation status | Acknowledge, Escalate, Dismiss (low/info only), Link to Approval, Link to Intervention | Transitions to Alert Detail on select. Approval link → Approval Queue. Intervention link → Intervention Manager. |
| **Alert Detail** | Full context on a single alert | Johan Ras | From Alert Centre list | Alert metadata header, timeline, linked items, action buttons | Full description, source, timeline, linked approval/intervention, audit reference | Acknowledge, Escalate, Dismiss, Link to Approval, Link to Intervention | Returns to Alert Centre on dismiss/back. |
| **Approval Queue** | Review and decide on all pending governance-sensitive approvals | Johan Ras | Dashboard badge, Alert link, sidebar nav | Approval list, priority indicators, deadline indicators, approval detail panel | All pending approvals, approval type, originating source, authority boundary, deadline | Approve, Reject, Defer with note, Request Clarification | On Approve/Reject: confirmation + audit reference surfaced. Clarification → Conversation surface. |
| **Approval Detail** | Full context and decision surface for a single approval | Johan Ras | From Approval Queue list | Proposal summary, rationale, authority boundary label, consequence panel, evidence panel, decision buttons | What/Why/Authority/Approve-consequence/Reject-consequence/Evidence | Approve, Reject, Defer, Request Clarification | Returns to Approval Queue. Links to source alert or intervention if applicable. |
| **Intervention Manager** | Launch, monitor, and manage governed interventions | Johan Ras, Maturion | From Alert Centre, Approval Queue, dashboard, sidebar nav | Active interventions list, intervention detail panel, new intervention form | Active and historical interventions, status, owner, timeline, outcome | Initiate new intervention, Cancel, Add note, Escalate, View execution trace | New intervention → approval if required → Approval Queue. Post-approval → execution state. |
| **Intervention Detail** | Full lifecycle view of a single intervention | Johan Ras | From Intervention Manager list | Timeline component, current step indicator, executing agent, error state, action buttons | Status at each lifecycle stage, executing agent, audit reference | Cancel, Add note, Escalate, View completion/failure record | Returns to Intervention Manager. Escalation → Escalation flow. |
| **AI Action Monitor** | Visibility into AIMC-routed AI actions | Johan Ras, Maturion | From Executive Dashboard, Conversation surface, sidebar nav | Action list, AIMC route indicator, status per action, audit reference | Active AI actions, outcome, AIMC route, audit reference, degraded mode indicator if AIMC unavailable | View detail, Escalate if stalled | Approval-required actions → Approval Queue. AIMC degraded mode → explicit status message shown. |
| **AIMCC / Knowledge Supervision** | Supervise knowledge upload and ingestion pipelines | Johan Ras, Maturion | From Executive Dashboard, sidebar nav | Upload list, ingestion pipeline status, quota panel, governance action panel | Upload items with KUC/AIMCC status, quota state, governance action items | Filter, view upload detail, take governance action (→ Approval Queue), review quota | Governance actions → Approval Queue. Upload detail panel inline. AIMCC degraded mode → explicit status shown. |
| **ARC Governance Console** | Dedicated surface for ARC (Automated Response Control) governance events — review, approve, reject, escalate, and audit ARC-triggered governance actions | Johan Ras | From Alert Centre (ARC-triggered alerts), sidebar nav (dedicated ARC nav item) | ARC event list, ARC event detail panel, decision buttons, audit history panel | Active ARC-triggered events, proposed automated responses, current state, priority, prior ARC actions | Approve, Reject, Escalate, Defer, View ARC audit history | Approved ARC actions → downstream ARC execution (governed). Rejected → blocked with audit record. Escalation → Alert Centre / Intervention Manager. |
| **Quota Management Console** | Operational console for hands-on management of upload quota — view live quota state, initiate quota change requests, approve/reject changes, monitor threshold warnings | Johan Ras | From AIMCC/Knowledge Supervision surface (quota panel), sidebar nav (dedicated quota nav item), Executive Dashboard quota indicator | Quota state panel (usage, threshold, trend), pending change requests list, approve/reject controls, quota audit history | Current quota limit, usage %, threshold warning levels, pending quota change requests, quota governance action history | Initiate quota change request, Approve quota change, Reject quota change, Defer, View quota audit history | Quota change requests → Approval Queue (or inline approval for Johan). AIMCC notification on approval. Full audit record on every quota decision. AIMCC degraded → stale indicator, no new quota changes. |
| **Knowledge Reference** | Surface knowledge/memory references with provenance | Johan Ras, Maturion | From Conversation, contextual surface, sidebar nav | Reference list, provenance metadata per item, retrieval status, degraded indicator | Knowledge references with source, ingestion path, retrieval timestamp | View detail, follow provenance, ask Maturion to synthesize | Memory degraded → explicit stale/unavailable indicator on all items. |
| **Conversation** | Two-way executive dialogue with Maturion | Johan Ras | Persistent panel on dashboard; full-screen mode from nav | Message thread, response type indicators, linked action buttons, proactive message indicator | Full conversation history, unread messages, message type labels, linked items | Reply, Acknowledge, Take linked action, Escalate, Mark for follow-up | Linked actions → Approval Queue or Intervention Manager. Full-screen conversation from nav. |
| **Specialist Agent Oversight** | Visibility into specialist agent workspaces | Johan Ras, Maturion | From Executive Dashboard, sidebar nav | Workspace list, sandbox isolation indicator, workspace detail panel | Active workspaces, status, scope, last reporting event, escalations | View output, Escalate, Initiate intervention, Terminate (approval-gated) | Termination → Approval Queue if approval required. Escalation → Alert Centre / Intervention Manager. |
| **Maintenance & Assurance Reports** | Executive view of health checks and assurance findings | Johan Ras | From dashboard health tiles, sidebar nav | Report list, severity indicators, report detail panel | Reports by agent/type, findings, severity, recommended actions | Acknowledge finding, Create intervention, Mark for follow-up, Export reference | Critical findings → linked alert in Alert Centre. Intervention → Intervention Manager. |
| **Estate Configuration & Wellbeing** | Estate config state, build job tracking, wellbeing | Johan Ras | From Executive Dashboard, sidebar nav | Config summary panel, active jobs list, deployment state panel, change request form | Estate configuration state, active build/job statuses, deployment wave status | Request config change (approval-gated), Review build status, Trigger approved maintenance | Config change → Approval Queue. Build status from Foreman read-only reporting. |
| **Mobile Alert View** | Mobile-optimized critical alert surface | Johan Ras | Mobile app landing / push notification tap | Condensed alert summary, critical alert cards, quick-action buttons | Critical and High alerts, estate health summary | Acknowledge, Approve/Reject (mobile approval shortcut), View detail | On detail view: full alert detail. Actions trigger same wiring as desktop. |

---

## 7. Wiring Model

> Stage 1 Traceability: §14 Schema-to-Hook Validation, §15 Table Pathway Audit, §24 Shared State Architecture, §26 Audit Log Design

For each interaction below, the wiring defines: UI trigger → action/route → data path → external service call (if any) → state/table → audit output → user-visible result.

### 7.1 Executive Dashboard — Wiring

| UI Event / Trigger | Invoked Action / Route | Data Read/Write Path | External Service | Target Table / State | Approval / Authority | Audit | User-Visible Result |
|---|---|---|---|---|---|---|---|
| Dashboard load (post-auth) | GET /api/estate/summary | Read: health_scores, active_alerts_count, active_approvals_count, active_interventions_count | None | `estate_health_scores`, `alerts`, `approvals`, `interventions` | None required | None (read-only) | Estate health tiles + alert count + approval count loaded |
| Health tile click (e.g., Execution Health) | GET /api/health/{domain} | Read: domain-specific health records | None | `health_events`, `execution_records` | None required | None (read-only) | Sub-surface for that health domain opens |
| Maturion proactive panel load | POST /api/aimc/request (type: proactive_summary) | Write: aimc_action_log (dispatch); Read: AIMC response | **AIMC** | `aimc_action_log` | None required | AuditEvent: AIMC_REQUEST (actor: Maturion, action: proactive_summary, source: AMC) | Maturion estate summary surfaced with response type: Observation |
| Alert panel item click | GET /api/alerts/{id} | Read: alert detail | None | `alerts` | None required | None | Alert Detail opens |

### 7.2 Alert Review and Handling — Wiring

| UI Event / Trigger | Invoked Action / Route | Data Read/Write Path | External Service | Target Table / State | Approval / Authority | Audit | User-Visible Result |
|---|---|---|---|---|---|---|---|
| Alert Centre load | GET /api/alerts (paginated, priority-ordered) | Read: alerts with priority, status, acknowledgment | None | `alerts` | None | None | Alerts listed priority-first |
| Alert item select | GET /api/alerts/{id}/detail | Read: full alert record, linked approvals/interventions | None | `alerts`, `approvals`, `interventions` | None | None | Alert Detail panel opens |
| Acknowledge alert | POST /api/alerts/{id}/acknowledge | Write: `alerts` (acknowledged_at, acknowledged_by) | None | `alerts` | Actor must be Johan or authorized Maturion delegate | AuditEvent: ALERT_ACKNOWLEDGED (actor, alert_id, timestamp) | Alert marked acknowledged; acknowledgment badge shown |
| Escalate alert | POST /api/alerts/{id}/escalate | Write: `escalations` (new record); Read: escalation routing config | None | `escalations`, `alerts` | Actor must be authorized | AuditEvent: ALERT_ESCALATED (actor, alert_id, target, timestamp) | Escalation record created; escalation target notified |
| Dismiss alert (info/low only) | POST /api/alerts/{id}/dismiss | Write: `alerts` (dismissed_at, dismissed_by, dismiss_reason) | None | `alerts` | Low/Informational class only; Johan required | AuditEvent: ALERT_DISMISSED (actor, alert_id, reason, timestamp) | Alert removed from active queue; visible in history |
| Critical alert timeout (auto-escalate) | Background event: `escalation_scheduler` fires after timeout | Write: `escalations` (auto-escalation record) | None | `escalations`, `alerts` | System-generated; logged as system actor | AuditEvent: ALERT_ESCALATED_TIMEOUT (alert_id, timeout_at, timestamp) | Escalation event logged; escalation target notified |
| Link alert to approval | POST /api/approvals (create from alert context) | Write: `approvals` (new record with alert_id reference) | None | `approvals` | Actor authorization checked | AuditEvent: APPROVAL_CREATED_FROM_ALERT (actor, approval_id, alert_id, timestamp) | New approval item created; user navigated to Approval Queue |
| Link alert to intervention | POST /api/interventions (create from alert context) | Write: `interventions` (new record with alert_id reference) | None | `interventions` | Actor authorization checked | AuditEvent: INTERVENTION_CREATED_FROM_ALERT (actor, intervention_id, alert_id, timestamp) | New intervention created; user navigated to Intervention Manager |

### 7.3 Approval Workflow — Wiring

| UI Event / Trigger | Invoked Action / Route | Data Read/Write Path | External Service | Target Table / State | Approval / Authority | Audit | User-Visible Result |
|---|---|---|---|---|---|---|---|
| Approval Queue load | GET /api/approvals?status=pending | Read: pending approvals with priority, source, deadline | None | `approvals` | None (read) | None | Pending approvals listed |
| Approval item select | GET /api/approvals/{id}/detail | Read: full approval record, linked context | None | `approvals` | None (read) | None | Approval Detail panel opens |
| Approve action | POST /api/approvals/{id}/decide (body: {decision: "approved", basis: "..."}) | Write: `approvals` (decision, decided_by, decided_at, basis); trigger post-approval action unlock | Downstream service (depends on approval type: AIMC / Foreman / AIMCC) | `approvals` | Johan (reserved matters) or Maturion (delegated domains) | AuditEvent: APPROVAL_DECIDED (actor, approval_id, decision: approved, basis, timestamp) | Approval recorded; blocked action unblocked; confirmation shown with audit reference |
| Reject action | POST /api/approvals/{id}/decide (body: {decision: "rejected", reason: "..."}) | Write: `approvals` (decision, decided_by, decided_at, reason); trigger post-rejection action cancellation | Downstream service notified of rejection | `approvals` | Johan (reserved matters) or Maturion (delegated domains) | AuditEvent: APPROVAL_DECIDED (actor, approval_id, decision: rejected, reason, timestamp) | Rejection recorded; action cancelled; confirmation shown with audit reference |
| Defer with note | POST /api/approvals/{id}/defer | Write: `approvals` (deferred_at, deferred_by, note, follow_up_at) | None | `approvals` | Authorized actor | AuditEvent: APPROVAL_DEFERRED (actor, approval_id, note, follow_up_at, timestamp) | Approval deferred; follow-up reminder scheduled |
| Request Clarification | POST /api/conversation/message (body: {context: approval_id}) | Write: `conversation_messages` (new message, linked to approval_id) | **AIMC** (Maturion conversation) | `conversation_messages`, `approvals` | Authorized actor | AuditEvent: CLARIFICATION_REQUESTED (actor, approval_id, timestamp) | Conversation opens with approval context; Maturion responds via AIMC |

### 7.4 Intervention Launch and Monitoring — Wiring

| UI Event / Trigger | Invoked Action / Route | Data Read/Write Path | External Service | Target Table / State | Approval / Authority | Audit | User-Visible Result |
|---|---|---|---|---|---|---|---|
| Open Intervention Manager | GET /api/interventions | Read: all interventions with status, timeline | None | `interventions` | None (read) | None | Active and historical interventions listed |
| Initiate new intervention | POST /api/interventions (create) | Write: `interventions` (new record: type, scope, initiator, authority_level, status: pending_approval or queued) | None (approval routing internal) | `interventions`, `approvals` (if approval required) | Johan or Maturion (delegated); approval gated if reserved matter | AuditEvent: INTERVENTION_INITIATED (actor, intervention_id, type, scope, timestamp) | Intervention created; if approval required → Approval Queue entry created |
| Approve intervention (from Approval Queue) | As per Approval Workflow wiring | As per Approval wiring | As per approval type | `approvals`, `interventions` | Johan (reserved) / Maturion (delegated) | As per Approval Workflow audit | Intervention moves to queued → dispatched to execution |
| Dispatch intervention to execution | Internal: POST /api/execute/intervention (routes to Foreman/specialist agent) | Write: `interventions` (status: in_progress, dispatched_at, executing_agent) | Foreman API / Specialist Agent API | `interventions`, `execution_records` | Prior approval recorded | AuditEvent: INTERVENTION_DISPATCHED (actor: system/Foreman, intervention_id, executing_agent, timestamp) | Execution status updates in real-time in Intervention Detail |
| Cancel intervention | POST /api/interventions/{id}/cancel | Write: `interventions` (status: cancelled, cancelled_by, cancel_reason, cancelled_at) | Execution abort signal to executing agent | `interventions` | Johan or authorized Maturion delegate | AuditEvent: INTERVENTION_CANCELLED (actor, intervention_id, reason, timestamp) | Intervention marked cancelled; executing agent notified |
| Intervention completes | System event: executing agent returns completion | Write: `interventions` (status: completed, completed_at, outcome) | Foreman / Specialist agent → AMC callback | `interventions`, `execution_records` | System | AuditEvent: INTERVENTION_COMPLETED (agent, intervention_id, outcome, timestamp) | Completion record shown; outcome surfaced to user |
| Intervention fails | System event: executing agent returns failure | Write: `interventions` (status: failed, failed_at, failure_reason) | Foreman / Specialist agent → AMC callback | `interventions`, `execution_records` | System | AuditEvent: INTERVENTION_FAILED (agent, intervention_id, reason, timestamp) | Failure shown; user prompted: retry / escalate / close with note |

#### 7.4.1 ARC Governance Console — Wiring

> Harmonization Pass 2026-04-23: ARC Governance Console wiring added as a named slice of §7.4.

| UI Event / Trigger | Invoked Action / Route | Data Read/Write Path | External Service | Target Table / State | Approval / Authority | Audit | User-Visible Result |
|---|---|---|---|---|---|---|---|
| Open ARC Governance Console | GET /api/arc/events (list with status) | Read: `arc_events` (triggering_condition, proposed_response, current_state, priority, detected_at) | None | `arc_events` | None (read) | None | ARC events listed with triggering condition, proposed response, and current state |
| Select ARC event | GET /api/arc/events/{id}/detail | Read: full ARC event record, audit chain, impact scope | None | `arc_events`, `arc_audit_log` | None (read) | None | ARC Event Detail opens with full trigger description, proposed response, impact scope, prior actions |
| Approve ARC action | POST /api/arc/events/{id}/decide (body: {decision: "approved", basis: "..."}) | Write: `arc_events` (decision: approved, decided_by, decided_at, basis); trigger downstream ARC execution | ARC execution endpoint (governed) | `arc_events`, `arc_audit_log`, `approvals` | Johan Ras (constitutional authority on ARC governance actions) | AuditEvent: ARC_ACTION_APPROVED (actor, arc_event_id, basis, timestamp) | ARC event approved; downstream execution triggered; approval audit record created |
| Reject ARC action | POST /api/arc/events/{id}/decide (body: {decision: "rejected", reason: "..."}) | Write: `arc_events` (decision: rejected, decided_by, decided_at, reason) | None | `arc_events`, `arc_audit_log` | Johan Ras | AuditEvent: ARC_ACTION_REJECTED (actor, arc_event_id, reason, timestamp) | ARC event rejected; execution blocked; rejection audit record created |
| Escalate ARC event | POST /api/arc/events/{id}/escalate | Write: `arc_events` (escalated_at, escalated_by, escalation_target); create `escalations` record | None | `arc_events`, `escalations`, `arc_audit_log` | Authorized actor | AuditEvent: ARC_EVENT_ESCALATED (actor, arc_event_id, target, timestamp) | Escalation record created; escalation target notified |
| Defer ARC event | POST /api/arc/events/{id}/defer | Write: `arc_events` (deferred_at, deferred_by, note, follow_up_at) | None | `arc_events`, `arc_audit_log` | Authorized actor | AuditEvent: ARC_EVENT_DEFERRED (actor, arc_event_id, note, follow_up_at, timestamp) | ARC event deferred; follow-up reminder scheduled |

### 7.5 AI-Routed Actions (AIMC) — Wiring

| UI Event / Trigger | Invoked Action / Route | Data Read/Write Path | External Service | Target Table / State | Approval / Authority | Audit | User-Visible Result |
|---|---|---|---|---|---|---|---|
| User / Maturion initiates AI action | POST /api/aimc/request | Write: `aimc_action_log` (action_type, initiator, route_target, status: dispatching); approval check | **AIMC** | `aimc_action_log`, `approvals` (if approval required) | Depends on action type; approval if governance-sensitive | AuditEvent: AIMC_ACTION_INITIATED (actor, action_type, route, timestamp) | AI Action Monitor entry created; if approval required → Approval Queue |
| AIMC returns result | System event: AIMC callback | Write: `aimc_action_log` (outcome, result_summary, completed_at); Read: result payload | **AIMC** callback | `aimc_action_log` | None (system event) | AuditEvent: AIMC_ACTION_COMPLETED (action_id, outcome, timestamp) | Result surfaced in AI Action Monitor with outcome summary and audit reference |
| AIMC unavailable detected | System health check / failed AIMC call | Write: `system_health_events` (AIMC_DEGRADED event) | None | `system_health_events` | None (system event) | AuditEvent: AIMC_DEGRADED (detected_at, impact_summary) | Explicit AIMC degraded-mode banner shown; AI-dependent features enter degraded state |
| AIMC recovers | System health check / successful AIMC call | Write: `system_health_events` (AIMC_RECOVERED event) | AIMC | `system_health_events` | None (system event) | AuditEvent: AIMC_RECOVERED (recovered_at) | Degraded-mode banner cleared; AI features resume normal state |

### 7.6 AIMCC / KUC Supervision — Wiring

| UI Event / Trigger | Invoked Action / Route | Data Read/Write Path | External Service | Target Table / State | Approval / Authority | Audit | User-Visible Result |
|---|---|---|---|---|---|---|---|
| Open AIMCC/Knowledge Supervision | GET /api/aimcc/uploads (status overview) | Read: `knowledge_upload_records` (status, submitter, KUC receipt, ingestion state) | **AIMCC** (status fetch) | `knowledge_upload_records` | None (read) | None | Upload list shown with KUC/AIMCC status per item |
| View upload detail | GET /api/aimcc/uploads/{id} | Read: full upload record including KUC routing, AIMCC ingestion progress/outcome, knowledge-system confirmation | **AIMCC** | `knowledge_upload_records` | None (read) | None | Upload Detail panel opens with full provenance chain |
| Governance action required (quota/flag) | POST /api/approvals (create from AIMCC governance context) | Write: `approvals` (new record, aimcc_context_id) | None | `approvals`, `knowledge_upload_records` | Johan (quota approval, content governance) | AuditEvent: AIMCC_GOVERNANCE_ACTION_CREATED (actor, context_id, action_type, timestamp) | Approval item created in Approval Queue with AIMCC context |
| AIMCC unavailable detected | System health check / failed AIMCC call | Write: `system_health_events` (AIMCC_DEGRADED) | None | `system_health_events` | None (system) | AuditEvent: AIMCC_DEGRADED (detected_at) | Explicit AIMCC degraded banner; knowledge upload/reference features enter degraded state |

#### 7.6.1 Dynamic Upload Quota Management Console — Wiring

> Harmonization Pass 2026-04-23: Quota Management Console wiring added as an explicitly named operational control slice of §7.6.

| UI Event / Trigger | Invoked Action / Route | Data Read/Write Path | External Service | Target Table / State | Approval / Authority | Audit | User-Visible Result |
|---|---|---|---|---|---|---|---|
| Open Quota Management Console | GET /api/aimcc/quota/summary | Read: `quota_state` (current_limit, current_usage, usage_percent, warning_threshold, critical_threshold, pending_change_requests) | **AIMCC** | `quota_state` | None (read) | None | Quota Console loaded: current usage, threshold levels, trend, pending change requests |
| Quota threshold warning triggered | System event: usage crosses configured threshold | Write: `alerts` (new QUOTA_THRESHOLD alert, severity based on level: Warning/Critical/Exceeded); Write: `quota_state` (threshold_triggered_at) | None | `alerts`, `quota_state` | None (system) | AuditEvent: QUOTA_THRESHOLD_TRIGGERED (level, current_usage_percent, threshold_value, timestamp) | Alert surfaced in Alert Centre and in Quota Console header with current usage level |
| Initiate quota change request | POST /api/aimcc/quota/change-request (body: {new_limit, justification, urgency}) | Write: `quota_change_requests` (new request: requested_by, new_limit, justification, urgency, status: pending); create `approvals` record | None | `quota_change_requests`, `approvals` | Johan Ras (if self-approving: approve inline with basis); otherwise standard approval gate | AuditEvent: QUOTA_CHANGE_REQUESTED (actor, requested_limit, justification, timestamp) | Quota change request created; appears in Approval Queue and in Quota Console pending section |
| Approve quota change | POST /api/approvals/{id}/decide (body: {decision: "approved", basis: "..."}) | Write: `approvals` (decision, decided_by, decided_at, basis); Write: `quota_change_requests` (approved_at, new_limit); notify AIMCC via POST /api/aimcc/quota/apply | **AIMCC** (quota update notification) | `approvals`, `quota_change_requests`, `quota_state` | Johan Ras | AuditEvent: QUOTA_CHANGE_APPROVED (actor, old_limit, new_limit, basis, aimcc_notification_status, timestamp) | Quota change approved; AIMCC notified; quota state updated in console; full audit record created |
| Reject quota change | POST /api/approvals/{id}/decide (body: {decision: "rejected", reason: "..."}) | Write: `approvals` (decision, decided_by, decided_at, reason); Write: `quota_change_requests` (rejected_at, reason) | None | `approvals`, `quota_change_requests` | Johan Ras | AuditEvent: QUOTA_CHANGE_REJECTED (actor, requested_limit, reason, timestamp) | Quota change rejected; reason recorded; request moves to rejected history |
| AIMCC quota state unavailable | System event: AIMCC degraded / failed quota fetch | Write: `quota_state` (stale_since, last_known values retained) | None | `quota_state`, `system_health_events` | None (system) | AuditEvent: QUOTA_STATE_STALE (detected_at, last_known_usage) | Quota Console shows explicit stale indicator; last-known values displayed clearly as stale; new quota change requests blocked until AIMCC recovery |

### 7.7 Knowledge-Aware Operating View — Wiring

| UI Event / Trigger | Invoked Action / Route | Data Read/Write Path | External Service | Target Table / State | Approval / Authority | Audit | User-Visible Result |
|---|---|---|---|---|---|---|---|
| Knowledge retrieval request | POST /api/knowledge/retrieve (query) | Write: `knowledge_retrieval_log` (query, requestor, timestamp); Read: knowledge/memory system response with provenance | **Knowledge/Memory System** (via governed API) | `knowledge_retrieval_log` | None (read) | AuditEvent: KNOWLEDGE_RETRIEVED (actor, query_summary, source_ref, timestamp) | Knowledge references surfaced with provenance: source, ingestion date, retrieval time |
| Knowledge system degraded | System health check / failed retrieval | Write: `system_health_events` (KNOWLEDGE_SYSTEM_DEGRADED) | None | `system_health_events` | None (system) | AuditEvent: KNOWLEDGE_SYSTEM_DEGRADED (detected_at) | Explicit stale/unavailable indicator on all knowledge surface items |
| View provenance detail | GET /api/knowledge/provenance/{ref_id} | Read: `knowledge_retrieval_log`, AIMCC ingestion metadata | **AIMCC** (provenance lookup) | `knowledge_retrieval_log` | None (read) | None | Provenance chain displayed: source → KUC submission → AIMCC ingestion → storage |

### 7.8 Executive Conversation — Wiring

| UI Event / Trigger | Invoked Action / Route | Data Read/Write Path | External Service | Target Table / State | Approval / Authority | Audit | User-Visible Result |
|---|---|---|---|---|---|---|---|
| Conversation surface load | GET /api/conversation/messages (recent history) | Read: `conversation_messages` (recent exchanges, unread markers) | None | `conversation_messages` | None (read) | None | Conversation history loaded with unread messages marked |
| User sends message | POST /api/conversation/message | Write: `conversation_messages` (user message, timestamp, session_id); dispatch to AIMC for Maturion response | **AIMC** | `conversation_messages` | None required | AuditEvent: CONVERSATION_MESSAGE_SENT (actor, message_summary, timestamp) | Message shown in thread; Maturion response requested via AIMC |
| AIMC returns Maturion response | System event: AIMC callback | Write: `conversation_messages` (Maturion response, response_type, timestamp, aimc_ref) | **AIMC** | `conversation_messages` | None (system event) | AuditEvent: CONVERSATION_RESPONSE_RECEIVED (actor: Maturion, response_type, aimc_ref, timestamp) | Maturion response rendered with type indicator (Observation/Recommendation/Request/Decision/Alert) |
| Maturion proactive message arrives | System event: AIMC push / Maturion proactive trigger | Write: `conversation_messages` (proactive message, type, priority, timestamp) | **AIMC** | `conversation_messages`, `alerts` (if alert-class) | None (Maturion delegated scope) | AuditEvent: PROACTIVE_MESSAGE_RECEIVED (actor: Maturion, type, priority, timestamp) | Proactive message shown with priority indicator; linked actions surfaced |
| Take linked action from conversation | Depends on action type: → Approve, → Intervene, → Escalate | As per linked action wiring above | Depends on action | As per linked action | As per linked action authority | As per linked action audit | Navigates to Approval Queue, Intervention Manager, or Alert Centre as appropriate |
| Acknowledge message | POST /api/conversation/messages/{id}/acknowledge | Write: `conversation_messages` (acknowledged_at, acknowledged_by) | None | `conversation_messages` | Authorized actor | AuditEvent: MESSAGE_ACKNOWLEDGED (actor, message_id, timestamp) | Message marked acknowledged |

---

## 8. Cross-System Integration Wiring

> Stage 1 Traceability: §2 Executive Layer Boundary Definitions, §18 Multi-Layer AI Integration Model, §3 Success Criteria (integration-specific)

### 8.1 AMC ↔ AIMC

| Interaction | AMC Side | AIMC Side | Boundary Rule |
|---|---|---|---|
| AI action request dispatch | POST to AIMC API with action type, context, auth token | AIMC receives, validates, routes to model/agent | AMC must not call model providers directly |
| AIMC response callback | AMC receives result payload, writes to `aimc_action_log`, surfaces to user | AIMC sends result with action_id reference | AMC must not interpret result as authoritative truth without provenance |
| AIMC availability check | GET /api/aimc/health (periodic and on demand) | AIMC health endpoint responds | AMC must surface degraded state to operator; must not fall back to direct model calls |
| Auth | AMC passes governed auth token with each AIMC call | AIMC validates token before execution | No anonymous AIMC calls |

### 8.2 AMC ↔ AIMCC / Knowledge Upload Centre

| Interaction | AMC Side | AIMCC Side | Boundary Rule |
|---|---|---|---|
| Upload status fetch | GET /api/aimcc/uploads (read-only) | AIMCC returns upload status and metadata | AMC surfaces status only; does not ingest |
| Upload governance action | POST /api/approvals (creates approval referencing AIMCC context) | AIMCC waits for approval outcome to proceed with governed action | AMC must not bypass AIMCC governance |
| AIMCC availability check | GET /api/aimcc/health | AIMCC health endpoint responds | AMC must surface degraded state; upload/ingestion features enter degraded mode |
| Knowledge upload submission (if initiated from AMC context) | POST to KUC API (routes through KUC not direct to AIMCC) | KUC accepts submission, routes to AIMCC | AMC must not bypass KUC for knowledge uploads |

### 8.3 AMC ↔ Knowledge / Memory System

| Interaction | AMC Side | Knowledge/Memory System Side | Boundary Rule |
|---|---|---|---|
| Knowledge retrieval | POST /api/knowledge/retrieve | Knowledge/memory system returns references with provenance | AMC must surface provenance; must not present as anonymous authoritative fact |
| Knowledge system availability | GET /api/knowledge/health | Knowledge/memory system health endpoint responds | AMC must surface degraded indicator on all knowledge surfaces when unavailable |
| Provenance lookup | GET /api/knowledge/provenance/{ref_id} | Returns provenance chain (source → KUC → AIMCC → storage) | AMC must preserve and display the full provenance chain |

### 8.4 AMC ↔ Foreman / Builder / Specialist Agents

| Interaction | AMC Side | Foreman / Agent Side | Boundary Rule |
|---|---|---|---|
| Intervention dispatch | POST /api/execute/intervention (routes to Foreman API) | Foreman receives intervention order; orchestrates execution | Foreman must not self-authorize reserved matters |
| Execution status reporting | Foreman/agent pushes status updates to AMC callback endpoint | AMC receives updates, writes to `interventions` and `execution_records` | Status is read-only to AMC; execution is Foreman's responsibility |
| Build / job status | Foreman pushes reporting events to AMC | AMC surfaces in Estate Configuration surface (read-only) | Johan oversees; does not directly control Foreman orchestration |
| Specialist agent outcome reporting | Specialist agent pushes outcome summary to AMC endpoint | AMC surfaces in Specialist Agent Oversight surface | AMC shows outcomes, not internal specialist state |

---

## 9. Degraded-Mode Operating Patterns

> Stage 1 Traceability: §18 Degraded mode requirements, §3 Integration success criteria

### 9.1 AIMC Unavailable

**Trigger**: AMC health check detects AIMC unreachable or AIMC returns non-OK status.

**UX behavior**:
- Explicit AIMC degraded-mode banner displayed on all surfaces where AI features are shown
- Conversation surface: Maturion responses unavailable; user sees "Maturion communication unavailable — AIMC unreachable" message
- AI Action Monitor: no new AI actions may be dispatched; pending items frozen with degraded indicator
- Approval Queue: AI-sourced approval items show degraded source indicator; decision by Johan still possible
- No fallback to direct model calls — system must wait for AIMC recovery
- AIMC degraded event recorded in `system_health_events` and audit trail

**Recovery**:
- Health check detects AIMC recovery → degraded banner cleared → AI features resume
- AIMC_RECOVERED audit event generated

### 9.2 AIMCC Unavailable

**Trigger**: AMC health check detects AIMCC unreachable.

**UX behavior**:
- Explicit AIMCC degraded-mode banner on AIMCC/Knowledge Supervision surface
- Upload status items shown with stale-data indicator; no real-time updates available
- Knowledge upload governance actions frozen (cannot process approvals dependent on AIMCC state)
- Knowledge Reference surface: items sourced via AIMCC retrieval show stale/unavailable indicator
- AIMCC_DEGRADED event recorded in audit trail

**Recovery**:
- Health check detects AIMCC recovery → degraded banner cleared → features resume

### 9.3 Knowledge / Memory System Degraded

**Trigger**: AMC health check detects knowledge/memory system unreachable or degraded retrieval.

**UX behavior**:
- Explicit stale/unavailable indicator on all knowledge reference items across all surfaces
- Retrieval requests that fail are surfaced with explicit failure message (not silent suppression)
- AMC does not serve stale cached knowledge as if it were current (no silent staleness)
- Knowledge retrieval degradation event recorded in audit trail

**Recovery**:
- Health check detects system recovery → indicators cleared → retrieval resumes

---

## 10. Stage 1 Traceability Index

All materially significant wiring and journey decisions in this Stage 2 document trace to an approved Stage 1 section. No product truth has been invented in Stage 2.

| Stage 2 Section | Traces to Stage 1 Section(s) |
|---|---|
| §2 Cross-System Boundary Definitions | §1 Executive Layer Boundary Definitions, §2 AMC/AIMC/AIMCC Boundary, §18 Multi-Layer AI Integration Model |
| §3 Actor Model | §1 Target Users/Audience, §13 Agent Authority Chain, §13 Authority Matrix |
| §4.1 Executive Estate Oversight | §1 Core Value Proposition, §23 Dashboard and Drill-Down Pattern, §3 Operating Success Measures |
| §4.2 Alert Review & Handling | §23 Notification Classes, §23 Alert Class and Priority Framework, §3 Executive Alerting |
| §4.3 Approval Workflow | §23 Approval-Centred UX, §13 Constitutional Authority, §3 Approval/Intervention Flows |
| §4.4 Intervention Launch & Monitoring | §23 Escalation and Intervention Pattern, §3 Operating Success Measures |
| §4.5 AI-Routed Actions (AIMC) | §18 AI Integration Requirements, §18 Multi-Layer AI Integration Model, §3 AIMC Success Criteria |
| §4.6 AIMCC / KUC Supervision | §2 AIMCC/KUC Boundary, §18 Multi-Layer AI Integration Model, §3 AIMCC/KUC Oversight |
| §4.7 Memory-Aware View | §2 Knowledge/Memory Boundary, §3 Memory-Aware Operational Clarity, §24 Shared State Architecture |
| §4.8 Executive Conversation | §23 Two-Way Conversational Interaction, §18 Executive AI Role, §23 AI-Mediated UX Discipline |
| §5.1 Specialist Agent Oversight | §13 Specialist-Agent Layer, §18 Specialist-Agent Integration |
| §5.2 Maintenance & Assurance | §2 In Scope, §13 Maintenance Layer, §13 Independent Assurance Layer |
| §5.3 Estate Configuration & Wellbeing | §2 In Scope, §5 Build Lifecycle Stages |
| §5.4 Mobile Continuity | §23 Mobile and Cross-Context Responsiveness, §23 Desktop/Mobile Continuity |
| §6 Screen/Surface Model | §23 Dashboard and Drill-Down, §23 Approval-Centred UX, §23 Escalation and Intervention Pattern |
| §7 Wiring Model | §14 Schema-to-Hook Validation, §15 Table Pathway Audit, §26 Audit Log Design, §25 API Authentication |
| §8 Cross-System Integration Wiring | §2 Boundary Definitions, §18 Multi-Layer AI Integration Model |
| §9 Degraded-Mode Patterns | §18 Degraded Mode Requirements, §3 Integration Success Criteria |

---

*End of UX Workflow & Wiring Spec — Stage 2. Produced by foreman-v2-agent under POLC_ORCHESTRATION. CS2 approval required before FRS (Stage 3) derivation begins.*

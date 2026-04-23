# Functional Requirements Specification — Stage 3

**Stage**: 3 — Functional Requirements Specification (FRS)
**Module**: App Management Centre (AMC)
**Version**: 1.0
**Status**: 🟡 Produced Approval-Ready — 2026-04-23
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: app_management_centre#1123
**Upstream Sources**:
- Stage 1 App Description: `modules/amc/00-app-description/app-description.md` v1.0 (CS2-approved 2026-04-22)
- Stage 2 UX Workflow & Wiring Spec: `modules/amc/01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md` v1.0 (CS2-approved via issue #1121)
**Canonical Location**: `modules/amc/02-frs/functional-requirements-specification.md`

---

> **DERIVATION DECLARATION**
> This document derives directly from the approved Stage 1 App Description (`modules/amc/00-app-description/app-description.md` v1.0) and the approved Stage 2 UX Workflow & Wiring Spec (`modules/amc/01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md` v1.0). It does not invent product truth. Every requirement family is traceable to one or more Stage 1 and Stage 2 sections. No requirement may be introduced here without a traceable upstream source.

---

## Table of Contents

1. [Purpose & Scope](#1-purpose--scope)
2. [Cross-System Boundary Rules](#2-cross-system-boundary-rules)
3. [Actor Model & Authority Constraints](#3-actor-model--authority-constraints)
4. [FR-100: Executive Estate Oversight](#4-fr-100-executive-estate-oversight)
5. [FR-200: Alert Management](#5-fr-200-alert-management)
6. [FR-300: Approval Workflow](#6-fr-300-approval-workflow)
7. [FR-400: Intervention Launch & Monitoring](#7-fr-400-intervention-launch--monitoring)
8. [FR-500: AI-Routed Actions (AIMC)](#8-fr-500-ai-routed-actions-aimc)
9. [FR-600: AIMCC / Knowledge Upload Centre Supervision](#9-fr-600-aimcc--knowledge-upload-centre-supervision)
10. [FR-700: Memory-Aware / Knowledge-Aware Operating View](#10-fr-700-memory-aware--knowledge-aware-operating-view)
11. [FR-800: Executive Conversation with Maturion](#11-fr-800-executive-conversation-with-maturion)
12. [FR-900: Specialist Agent Workspace Oversight](#12-fr-900-specialist-agent-workspace-oversight)
13. [FR-1000: Maintenance & Assurance Reporting](#13-fr-1000-maintenance--assurance-reporting)
14. [FR-1100: Estate Configuration & Wellbeing](#14-fr-1100-estate-configuration--wellbeing)
15. [FR-1200: Mobile Continuity](#15-fr-1200-mobile-continuity)
16. [FR-1300: Audit & Provenance](#16-fr-1300-audit--provenance)
17. [FR-1400: Authentication & Authorization](#17-fr-1400-authentication--authorization)
18. [FR-1500: Cross-System Integration & Boundary Enforcement](#18-fr-1500-cross-system-integration--boundary-enforcement)
19. [FR-1600: Degraded-Mode Behavior](#19-fr-1600-degraded-mode-behavior)
20. [FR-1700: State & Persistence](#20-fr-1700-state--persistence)
21. [Business Rules & Decision Rules Summary](#21-business-rules--decision-rules-summary)
22. [Requirement Groupings for Downstream Derivation](#22-requirement-groupings-for-downstream-derivation)

---

## 1. Purpose & Scope

### 1.1 Purpose

This Functional Requirements Specification translates the approved Stage 1 App Description and approved Stage 2 UX Workflow & Wiring Spec into explicit, verifiable, architecture-ready functional requirements for the App Management Centre (AMC).

The FRS defines **what AMC must do**, **under what conditions**, **for which actors**, **with what constraints**, and **with what required outcomes**. It does not define implementation detail. That is the responsibility of TRS (Stage 4) and Architecture (Stage 5).

Every requirement in this document is stated in a form that allows downstream TRS, Architecture, and QA agents to verify without guessing intent.

### 1.2 Scope

**In scope for Stage 3 FRS:**
- All functional capabilities derived from Stage 1 and Stage 2 approved truth
- Actor-specific behavior for each major functional family
- Business and decision rules governing approved vs delegated vs reserved-matter actions
- Alerting, escalation, approval, and intervention rules
- Audit and provenance requirements
- Cross-system interaction requirements (AMC ↔ AIMC, AIMCC, KUC, knowledge/memory system)
- State and persistence expectations at the functional level
- Degraded-mode behavior for each governed external dependency

**Explicitly out of scope for Stage 3 FRS:**
- Technical architecture decisions (Stage 5)
- API contract definitions (Stage 4 TRS / Stage 5 Architecture)
- Database schema definitions (Stage 4 TRS / Stage 5)
- Implementation code (Stage 12)
- Test specifications (Stage 6 QA-to-Red)

> Stage 1 Traceability: §5 Stage 3 definition, §6 Role of the FRS

---

## 2. Cross-System Boundary Rules

These boundaries are non-negotiable and must be preserved in all requirements stated in this document and all downstream derivations.

> Stage 1 Traceability: §1 Executive Layer Boundary Definitions, §2 AMC/AIMC/AIMCC Boundary, §18 Multi-Layer AI Integration Model
> Stage 2 Traceability: §2 Cross-System Boundary Definitions

| Layer | Definition | AMC Interaction Rule |
|---|---|---|
| **AMC** | Executive supervisory application and operating surface | Presents executive visibility, alerts, approvals, conversations, interventions, and oversight surfaces. Does not execute AI models, ingest knowledge, or store persistent memory truth |
| **AIMC** | Sole governed AI execution gateway | All AI model interactions from AMC context must route through AIMC. AMC must not call model providers directly under any circumstance |
| **AIMCC** | Knowledge ingestion and memory operations layer | AMC surfaces ingestion status and knowledge-management state sourced from AIMCC. AMC must not bypass AIMCC for knowledge operations |
| **Knowledge Upload Centre (KUC)** | Governed ingestion entry point | All knowledge upload actions from AMC context must route through KUC. AMC must not initiate ingestion directly |
| **Knowledge / memory system** | Persistent knowledge and memory substrate | AMC may query and surface knowledge references with provenance. AMC must not become the canonical owner or privately cache persistent knowledge truth |

**Non-bypass rule (BR-SYS-001)**: Any AI action from AMC that does not route through AIMC is a governance violation. Any knowledge ingestion or upload from AMC that does not route through KUC/AIMCC is a governance violation.

---

## 3. Actor Model & Authority Constraints

> Stage 1 Traceability: §1 Target Users, §13 Agent Authority Chain, §13 Authority Matrix
> Stage 2 Traceability: §3 Actor Model

| Actor | Role | Authority Level | AMC Entry Pattern |
|---|---|---|---|
| **Johan Ras** | Constitutional human authority; primary executive user | Full authority — all reserved matters, all approvals | Authenticated login; all surfaces accessible |
| **Maturion** | Resident AI executive; proactive estate intelligence | Delegated operational authority within explicitly approved domains; escalates reserved matters to Johan | AI-driven via AIMC; surfaces decisions and alerts |
| **Foreman** | Supervised orchestration authority | Operational scope only; visible via execution reporting surfaces | Backend reporting into AMC; no direct AMC login |
| **IAA agents** | Independent assurance layer | Advisory / assurance outputs only | Report findings via governed pathways; visible in reporting surfaces |
| **Specialist agents** | Domain-specific workers | Task-scoped; bounded sandbox | Sandboxed; AMC surfaces their status, not internal state |
| **Maintenance agents** | Upkeep, health checks, diagnostics | Status reporting only | Reporting via governed pathways |

**Authority Constraint Rules:**
- **BR-AUTH-001**: Reserved matters (governance changes, agent-file changes, major architectural direction, constitutional boundary changes, authority transfers) require explicit Johan Ras approval. No AMC workflow may silently convert a reserved matter into a routine operational matter.
- **BR-AUTH-002**: Maturion may approve or trigger actions only within explicitly approved delegated domains. All other matters escalate to Johan.
- **BR-AUTH-003**: AMC must not approve its own governance actions. All approval decisions route to Johan or Maturion within their respective authority domains.
- **BR-AUTH-004**: AI-generated suggestions and recommendations must not be treated as approved decisions. AMC must distinguish observation, recommendation, request, and decision in all interfaces.

---

## 4. FR-100: Executive Estate Oversight

> Stage 1 Traceability: §1 Core Value Proposition, §3 Operating Success Measures, §23 Dashboard and Drill-Down Pattern, §23 Proactive Awareness Requirement
> Stage 2 Traceability: §4.1 Executive Estate Oversight Journey, §6 Screen/Surface Model (Executive Dashboard), §7.1 Executive Dashboard Wiring

### FR-101 — Executive Dashboard Load

| Field | Value |
|---|---|
| **Requirement ID** | FR-101 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | User authenticates successfully via Supabase Auth; session JWT validated |
| **Required System Behavior** | AMC loads the Executive Dashboard as the default post-authentication landing surface. The dashboard presents: (1) five health domain tiles — System Health, Execution Health, Governance Health, Security, Compliance; (2) a prioritized Alert Panel showing Critical and High alerts; (3) a count badge for active pending approvals; (4) a count indicator for active interventions; (5) a Maturion Proactive Panel showing current AI-detected estate intelligence if new insight exists since last session |
| **User-Visible Result** | Executive Dashboard is fully loaded with current estate health summary, active alert count, active approval count, active intervention count, and Maturion proactive message if present |
| **Required State / Audit Effect** | Read-only; no audit event required for passive load |
| **Approval / Authority Constraint** | None required for load |
| **Failure / Degraded Expectation** | If AIMC is unavailable: Maturion Proactive Panel shows explicit "Maturion communication unavailable — AIMC unreachable" message. All non-AI health tiles still load. If health data fetch fails: tiles show explicit error state, not stale data as if current |

### FR-102 — Health Domain Drill-Down

| Field | Value |
|---|---|
| **Requirement ID** | FR-102 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | User clicks a health domain tile on the Executive Dashboard |
| **Required System Behavior** | AMC navigates to or opens the domain-specific sub-surface for the selected health domain (e.g., Execution Health → Execution Monitor; Governance Health → governance posture surface) |
| **User-Visible Result** | Domain-specific health detail is visible with relevant records, events, or findings |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None |
| **Failure / Degraded Expectation** | If domain data is unavailable: sub-surface shows explicit unavailable state, not empty/silent |

### FR-103 — Proactive Estate Awareness

| Field | Value |
|---|---|
| **Requirement ID** | FR-103 |
| **Actor** | Maturion (AI-initiated via AIMC), Johan Ras (recipient) |
| **Trigger / Precondition** | AMC dashboard load or background polling cycle; AIMC available |
| **Required System Behavior** | AMC dispatches a proactive summary request to AIMC (action type: `proactive_summary`). AIMC returns Maturion's current estate intelligence. AMC surfaces the result in the Maturion Proactive Panel labeled as response type "Observation". The panel must not be a passive static text block — it must link to any relevant action surface (alert, approval, intervention) where applicable |
| **User-Visible Result** | Maturion proactive summary visible on dashboard; linked actions accessible |
| **Required State / Audit Effect** | AuditEvent: `AIMC_REQUEST` (actor: Maturion, action: proactive_summary, source: AMC, timestamp) |
| **Approval / Authority Constraint** | No approval required; Maturion operates within delegated executive scope for awareness |
| **Failure / Degraded Expectation** | AIMC unavailable: explicit degraded indicator shown; panel displays last-known status with stale indicator, or explicit "unavailable" message. No silent failure |

### FR-104 — Dashboard Navigation

| Field | Value |
|---|---|
| **Requirement ID** | FR-104 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User is authenticated on Executive Dashboard |
| **Required System Behavior** | Navigation sidebar provides direct access to: Alert Centre, Approval Queue, Intervention Manager, AI Action Monitor, AIMCC/Knowledge Supervision, Knowledge Reference, Conversation, Specialist Agent Oversight, Maintenance & Assurance Reports, Estate Configuration & Wellbeing |
| **User-Visible Result** | All primary surfaces are one navigation action away from the Executive Dashboard |
| **Required State / Audit Effect** | None |
| **Approval / Authority Constraint** | All surfaces are accessible to Johan Ras. Maturion-context surfaces are accessible to Maturion within approved scope |
| **Failure / Degraded Expectation** | Navigation must not be broken by partial degraded-mode states; surfaces load with appropriate degraded indicators where relevant |

---

## 5. FR-200: Alert Management

> Stage 1 Traceability: §23 Notification Classes, §23 Alert Class and Priority Framework, §3 Executive Alerting Success Criteria
> Stage 2 Traceability: §4.2 Alert Review and Handling Journey, §7.2 Alert Review and Handling Wiring

### FR-201 — Alert Centre Load

| Field | Value |
|---|---|
| **Requirement ID** | FR-201 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User navigates to Alert Centre |
| **Required System Behavior** | AMC loads all active alerts ordered by priority: Critical first, then High, then Medium, then Low/Informational. Each listed alert displays: alert class, source system, summary, timestamp, acknowledgment status, and escalation status |
| **User-Visible Result** | Prioritized alert list is displayed with class and status visible per item |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If alert data fetch fails: explicit error shown, not an empty list presented as "no alerts" |

### FR-202 — Alert Detail View

| Field | Value |
|---|---|
| **Requirement ID** | FR-202 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User selects an alert from the Alert Centre list |
| **Required System Behavior** | AMC displays the Alert Detail view showing: full alert description, originating system/actor, timeline of events, linked approval or intervention (if any), context references, available actions |
| **User-Visible Result** | Alert Detail view is open with complete alert context and available actions |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If linked approval/intervention is unavailable: detail still loads with explicit note that linked item is unavailable |

### FR-203 — Alert Acknowledgment

| Field | Value |
|---|---|
| **Requirement ID** | FR-203 |
| **Actor** | Johan Ras (all alerts); Maturion (within authorized delegated scope for Medium/Low) |
| **Trigger / Precondition** | User explicitly selects "Acknowledge" on an alert from Alert Detail or Alert Centre |
| **Required System Behavior** | AMC records the acknowledgment: sets `acknowledged_at` and `acknowledged_by` on the alert record. Acknowledgment is an explicit actor action — it is not triggered implicitly by viewing the alert. The alert displays an acknowledgment badge. If the alert has linked required follow-up actions (approval or intervention), those are surfaced post-acknowledgment |
| **User-Visible Result** | Alert shows acknowledged status with actor name and timestamp; post-acknowledgment actions surfaced if applicable |
| **Required State / Audit Effect** | AuditEvent: `ALERT_ACKNOWLEDGED` (actor, alert_id, timestamp); alert record updated: acknowledged_at, acknowledged_by |
| **Approval / Authority Constraint** | Actor must be Johan or authorized Maturion delegate. Unauthorized acknowledgment attempts must be rejected |
| **Failure / Degraded Expectation** | If write fails: acknowledgment must not be shown as completed; user receives explicit error; retry available |

### FR-204 — Alert Escalation

| Field | Value |
|---|---|
| **Requirement ID** | FR-204 |
| **Actor** | Johan Ras, Maturion (within authorized scope) |
| **Trigger / Precondition** | User selects "Escalate" on an alert, or auto-escalation timer fires for an unacknowledged Critical alert |
| **Required System Behavior** | AMC creates an escalation record referencing the alert. The escalation record stores: originating alert ID, escalation actor (human or system), escalation target, timestamp. Escalation notification is delivered to the escalation target. The alert displays an escalation status indicator |
| **User-Visible Result** | Alert shows escalation status; escalation target is notified |
| **Required State / Audit Effect** | AuditEvent: `ALERT_ESCALATED` (actor, alert_id, escalation_target, timestamp) — for manual escalation. AuditEvent: `ALERT_ESCALATED_TIMEOUT` (alert_id, timeout_at, timestamp) — for auto-escalation |
| **Approval / Authority Constraint** | Actor must be authorized. Auto-escalation fires as system actor after defined timeout for unacknowledged Critical alerts |
| **Failure / Degraded Expectation** | If escalation write fails: user receives explicit error; escalation must not be silently dropped |

### FR-205 — Alert Dismissal (Low/Informational Only)

| Field | Value |
|---|---|
| **Requirement ID** | FR-205 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User selects "Dismiss" on a Low or Informational class alert |
| **Required System Behavior** | AMC records the dismissal with: dismissed_by, dismissed_at, dismiss_reason (required field). Alert is removed from active queue and moved to alert history |
| **User-Visible Result** | Alert removed from active queue; visible in history with dismissed status |
| **Required State / Audit Effect** | AuditEvent: `ALERT_DISMISSED` (actor, alert_id, reason, timestamp); alert record updated |
| **Approval / Authority Constraint** | Dismiss action is restricted to Low/Informational alert class only. Critical, High, and Medium alerts may not be dismissed — they must be acknowledged and then resolved. Actor must be Johan |
| **Failure / Degraded Expectation** | Attempt to dismiss a Critical/High/Medium alert must be rejected with an explicit error. No silent downgrading of alert class to allow dismissal |

### FR-206 — Link Alert to Approval

| Field | Value |
|---|---|
| **Requirement ID** | FR-206 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User selects "Link to Approval" from an alert |
| **Required System Behavior** | AMC creates a new approval record with the alert context pre-populated (alert_id reference). User is navigated to the Approval Queue where the new approval item is visible |
| **User-Visible Result** | Approval item created with alert context; user is in Approval Queue |
| **Required State / Audit Effect** | AuditEvent: `APPROVAL_CREATED_FROM_ALERT` (actor, approval_id, alert_id, timestamp) |
| **Approval / Authority Constraint** | Actor must be authorized to create approvals |
| **Failure / Degraded Expectation** | If approval creation fails: explicit error; no orphaned alert without feedback |

### FR-207 — Link Alert to Intervention

| Field | Value |
|---|---|
| **Requirement ID** | FR-207 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User selects "Link to Intervention" from an alert |
| **Required System Behavior** | AMC creates a new intervention record with the alert context pre-populated (alert_id reference). User is navigated to the Intervention Manager where the new intervention item is visible |
| **User-Visible Result** | Intervention record created with alert context; user is in Intervention Manager |
| **Required State / Audit Effect** | AuditEvent: `INTERVENTION_CREATED_FROM_ALERT` (actor, intervention_id, alert_id, timestamp) |
| **Approval / Authority Constraint** | Actor must be authorized |
| **Failure / Degraded Expectation** | If intervention creation fails: explicit error; alert state not altered |

### FR-208 — Critical Alert Auto-Escalation

| Field | Value |
|---|---|
| **Requirement ID** | FR-208 |
| **Actor** | System (background scheduler) |
| **Trigger / Precondition** | A Critical alert has not been acknowledged within the defined escalation timeout period |
| **Required System Behavior** | AMC background escalation scheduler fires. An auto-escalation record is created referencing the unacknowledged Critical alert. The escalation event is recorded with a system actor, escalation timestamp, and pre-defined escalation target. Alert expiry does not silently resolve the underlying condition |
| **User-Visible Result** | Escalation is recorded and escalation target is notified; alert remains visible with auto-escalated status indicator |
| **Required State / Audit Effect** | AuditEvent: `ALERT_ESCALATED_TIMEOUT` (alert_id, timeout_at, timestamp, system_actor) |
| **Approval / Authority Constraint** | System actor; no human approval required for auto-escalation trigger |
| **Failure / Degraded Expectation** | Escalation scheduler failure must generate a system-level error alert. The failure to auto-escalate must not silently pass |

### FR-209 — Alert History

| Field | Value |
|---|---|
| **Requirement ID** | FR-209 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User accesses alert history view |
| **Required System Behavior** | AMC displays all past alerts with their final resolved status (acknowledged, escalated, dismissed), actor, timestamp |
| **User-Visible Result** | Complete alert history accessible with final status per item |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If history load fails: explicit error; no silent empty list |

---

## 6. FR-300: Approval Workflow

> Stage 1 Traceability: §23 Approval-Centred UX, §13 Constitutional Authority, §3 Approval/Intervention Success Criteria, §23 Prohibited UX Patterns
> Stage 2 Traceability: §4.3 Approval Workflow Journey, §7.3 Approval Workflow Wiring

### FR-301 — Approval Queue Load

| Field | Value |
|---|---|
| **Requirement ID** | FR-301 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User navigates to the Approval Queue |
| **Required System Behavior** | AMC loads all pending approval items ordered by priority and deadline. Each item displays: approval type, originating source (AI action / governance action / intervention / reserved-matter), authority boundary type, deadline/timeout if applicable |
| **User-Visible Result** | Pending approvals listed with type, source, authority boundary, and deadline visible |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If load fails: explicit error; no silent empty queue |

### FR-302 — Approval Detail View

| Field | Value |
|---|---|
| **Requirement ID** | FR-302 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User selects an approval item from the queue |
| **Required System Behavior** | AMC opens the Approval Detail surface displaying: (1) what is being proposed (explicit, not vague); (2) why it is being proposed (context and rationale); (3) which authority boundary applies (reserved matter / delegated / operational); (4) consequence of approval; (5) consequence of rejection or delay; (6) supporting evidence or context including AI reasoning summary if AIMC-sourced |
| **User-Visible Result** | Approval Detail is fully visible with what/why/authority/consequences/evidence |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If evidence or linked context is unavailable: detail still loads with explicit note that supporting evidence is unavailable; user is not blocked from deciding |

### FR-303 — Approval Grant

| Field | Value |
|---|---|
| **Requirement ID** | FR-303 |
| **Actor** | Johan Ras (reserved matters and all governance-sensitive actions); Maturion (delegated operational matters only) |
| **Trigger / Precondition** | User selects "Approve" with a stated approval basis on an Approval Detail view |
| **Required System Behavior** | AMC records the approval with: deciding actor, timestamp, approval basis (required field), outcome. AMC triggers the post-approval action unlock — the blocked downstream action is unblocked and dispatched to the appropriate service (AIMC, Foreman, AIMCC, etc.). User sees confirmation of action unblocked with audit reference |
| **User-Visible Result** | Approval recorded and confirmed; downstream action unblocked; audit reference shown |
| **Required State / Audit Effect** | AuditEvent: `APPROVAL_DECIDED` (actor, approval_id, decision: approved, basis, timestamp); approval record updated: decided_by, decided_at, basis, outcome |
| **Approval / Authority Constraint** | Reserved-matter approvals require Johan Ras. Delegated-domain approvals may be decided by Maturion within explicitly approved scope. Approval basis must be provided — empty basis is rejected |
| **Failure / Degraded Expectation** | If downstream action dispatch fails after approval: the approval record is retained; the unblocking failure is surfaced to the user; user can retry dispatch. The approval decision must not be lost due to downstream service failure |

### FR-304 — Approval Rejection

| Field | Value |
|---|---|
| **Requirement ID** | FR-304 |
| **Actor** | Johan Ras; Maturion (within delegated scope) |
| **Trigger / Precondition** | User selects "Reject" with a rejection reason on an Approval Detail view |
| **Required System Behavior** | AMC records the rejection with: deciding actor, timestamp, rejection reason (required field), outcome. The blocked action is cancelled. Downstream service is notified of rejection. User sees confirmation of action cancelled with audit reference |
| **User-Visible Result** | Rejection recorded and confirmed; action cancelled; audit reference shown |
| **Required State / Audit Effect** | AuditEvent: `APPROVAL_DECIDED` (actor, approval_id, decision: rejected, reason, timestamp) |
| **Approval / Authority Constraint** | As per FR-303. Rejection reason must be provided |
| **Failure / Degraded Expectation** | If downstream service cannot be notified of rejection: rejection record is retained; notification failure is surfaced to the user |

### FR-305 — Approval Deferral with Note

| Field | Value |
|---|---|
| **Requirement ID** | FR-305 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User selects "Defer with note" on an approval item |
| **Required System Behavior** | AMC records the deferral with: deferred_by, deferred_at, note (required), follow_up_at (scheduled follow-up reminder). The approval item remains in the queue with a deferred indicator. The follow-up reminder is scheduled |
| **User-Visible Result** | Approval item shows deferred status with follow-up time; user receives confirmation |
| **Required State / Audit Effect** | AuditEvent: `APPROVAL_DEFERRED` (actor, approval_id, note, follow_up_at, timestamp) |
| **Approval / Authority Constraint** | Actor must be authorized; deferral note required |
| **Failure / Degraded Expectation** | If reminder scheduling fails: deferral record is retained; explicit warning shown that follow-up reminder scheduling failed |

### FR-306 — Request Clarification from Maturion

| Field | Value |
|---|---|
| **Requirement ID** | FR-306 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User selects "Request Clarification" on an approval item |
| **Required System Behavior** | AMC opens the Conversation surface with the approval context pre-populated. AMC creates a conversation message linked to the approval_id. The message is dispatched to AIMC for Maturion response. Maturion responds in the conversation thread with clarification |
| **User-Visible Result** | Conversation surface opens with approval context; Maturion provides clarification via AIMC |
| **Required State / Audit Effect** | AuditEvent: `CLARIFICATION_REQUESTED` (actor, approval_id, timestamp) |
| **Approval / Authority Constraint** | Actor must be authorized |
| **Failure / Degraded Expectation** | If AIMC is unavailable: clarification request is logged; explicit AIMC unavailable message shown; user is not blocked from deciding independently |

### FR-307 — Approval Blocking Rule

| Field | Value |
|---|---|
| **Requirement ID** | FR-307 |
| **Actor** | System (enforcement rule) |
| **Trigger / Precondition** | Any governance-sensitive action is initiated that has an approval requirement |
| **Required System Behavior** | AMC must block execution of the action until explicit approval is granted (FR-303). The action must not proceed on the basis of a recommendation, suggestion, or implicit assumption of approval. Reserved-matter actions must not be disguised as routine task prompts |
| **User-Visible Result** | Action blocked; approval item surfaced in Approval Queue |
| **Required State / Audit Effect** | Approval record created in pending state |
| **Approval / Authority Constraint** | No bypass of approval gate is permitted for approval-required actions |
| **Failure / Degraded Expectation** | If the approval system itself is degraded: actions requiring approval must remain blocked. No degraded-mode fallback may silently allow approval-gated actions to proceed |

---

## 7. FR-400: Intervention Launch & Monitoring

> Stage 1 Traceability: §23 Escalation and Intervention Pattern, §3 Operating Success Measures, §2 In Scope
> Stage 2 Traceability: §4.4 Intervention Launch and Monitoring Journey, §7.4 Intervention Wiring

### FR-401 — Intervention Manager Load

| Field | Value |
|---|---|
| **Requirement ID** | FR-401 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | User navigates to Intervention Manager |
| **Required System Behavior** | AMC loads all active and historical interventions with: status, owner/initiator, timeline, type |
| **User-Visible Result** | Active interventions listed with current status, owner, and timeline visible |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If load fails: explicit error |

### FR-402 — Initiate New Intervention

| Field | Value |
|---|---|
| **Requirement ID** | FR-402 |
| **Actor** | Johan Ras (all interventions); Maturion (delegated-scope interventions only) |
| **Trigger / Precondition** | User selects "Initiate new intervention" in the Intervention Manager |
| **Required System Behavior** | AMC presents intervention creation form. User specifies: intervention type (from predefined catalogue or custom), scope (target system/agent/module, description, intended outcome), authority level (requires approval? Reserved matter? Delegated?). On submission: if approval required, intervention enters Approval Queue before execution. If no approval required, intervention enters queued state |
| **User-Visible Result** | Intervention record created; if approval required → Approval Queue entry created; otherwise → queued status shown |
| **Required State / Audit Effect** | AuditEvent: `INTERVENTION_INITIATED` (actor, intervention_id, type, scope, timestamp); intervention record created with: type, scope, initiator, authority_level, status |
| **Approval / Authority Constraint** | Interventions on reserved-matter systems require Johan Ras approval. Maturion may initiate delegated-scope interventions. Approval gate is mandatory for reserved-matter interventions — no bypass |
| **Failure / Degraded Expectation** | If intervention creation fails: explicit error; no silent failure |

### FR-403 — Intervention Dispatch to Execution

| Field | Value |
|---|---|
| **Requirement ID** | FR-403 |
| **Actor** | System (post-approval or post-initiation) |
| **Trigger / Precondition** | Intervention is in queued state (approval granted if required, or no approval required) |
| **Required System Behavior** | AMC dispatches the intervention order through the governed execution pathway (Foreman API or specialist agent API). AMC records: dispatched_at, executing_agent. AMC surfaces execution status in real-time: queued → in progress → completed/failed. AMC must confirm to the user that the intervention entered a governed execution path |
| **User-Visible Result** | Real-time execution status visible in Intervention Detail; confirmation that governed path was entered |
| **Required State / Audit Effect** | AuditEvent: `INTERVENTION_DISPATCHED` (actor: system/Foreman, intervention_id, executing_agent, timestamp) |
| **Approval / Authority Constraint** | Prior approval must be recorded before dispatch for approval-required interventions |
| **Failure / Degraded Expectation** | If dispatch fails: intervention status set to dispatch_failed; user is notified explicitly with error detail |

### FR-404 — Intervention Monitoring

| Field | Value |
|---|---|
| **Requirement ID** | FR-404 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | Intervention is in in-progress state |
| **Required System Behavior** | AMC surfaces execution status updates as they arrive from the executing agent (Foreman/specialist agent callback). Intervention Detail shows: timeline, current step, executing agent, error state if any. Visibility persists until completion or explicit closure |
| **User-Visible Result** | Live status updates visible in Intervention Detail |
| **Required State / Audit Effect** | Status updates written to intervention record as received |
| **Approval / Authority Constraint** | None for monitoring |
| **Failure / Degraded Expectation** | If status updates cease (executing agent unreachable): AMC shows last-known status with explicit stale indicator; user is surfaced the option to escalate |

### FR-405 — Intervention Completion

| Field | Value |
|---|---|
| **Requirement ID** | FR-405 |
| **Actor** | System (executing agent callback) |
| **Trigger / Precondition** | Executing agent returns a completion result to AMC |
| **Required System Behavior** | AMC records completion: status: completed, completed_at, outcome, executing_agent. Completion record shown to user with outcome and audit reference |
| **User-Visible Result** | Intervention shows "Completed" with outcome and audit reference |
| **Required State / Audit Effect** | AuditEvent: `INTERVENTION_COMPLETED` (agent, intervention_id, outcome, timestamp) |
| **Approval / Authority Constraint** | System event |
| **Failure / Degraded Expectation** | N/A (this is the success path) |

### FR-406 — Intervention Failure Handling

| Field | Value |
|---|---|
| **Requirement ID** | FR-406 |
| **Actor** | System (executing agent callback); Johan Ras (decision on failure) |
| **Trigger / Precondition** | Executing agent returns a failure result to AMC |
| **Required System Behavior** | AMC records failure: status: failed, failed_at, failure_reason. User is prompted with options: retry, escalate, or close with note |
| **User-Visible Result** | Intervention shows "Failed" with reason; user action options presented |
| **Required State / Audit Effect** | AuditEvent: `INTERVENTION_FAILED` (agent, intervention_id, reason, timestamp) |
| **Approval / Authority Constraint** | Retry may re-enter approval flow if authority requires it |
| **Failure / Degraded Expectation** | Failure record must be preserved even if user closes the session |

### FR-407 — Cancel Intervention

| Field | Value |
|---|---|
| **Requirement ID** | FR-407 |
| **Actor** | Johan Ras; Maturion (within delegated scope) |
| **Trigger / Precondition** | User selects "Cancel" on an active intervention |
| **Required System Behavior** | AMC records cancellation: cancelled_by, cancel_reason (required), cancelled_at. Executing agent receives abort signal. Intervention status set to: cancelled |
| **User-Visible Result** | Intervention shows "Cancelled" with reason |
| **Required State / Audit Effect** | AuditEvent: `INTERVENTION_CANCELLED` (actor, intervention_id, reason, timestamp) |
| **Approval / Authority Constraint** | Actor must be Johan or authorized Maturion delegate. Cancellation reason required |
| **Failure / Degraded Expectation** | If abort signal to executing agent fails: cancellation is still recorded; executing agent abort failure is surfaced to user |

---

## 8. FR-500: AI-Routed Actions (AIMC)

> Stage 1 Traceability: §18 AI Integration Requirements, §18 Multi-Layer AI Integration Model, §3 AIMC Success Criteria, §13 Authority Matrix
> Stage 2 Traceability: §4.5 AI-Routed Actions Journey, §7.5 AI-Routed Actions Wiring, §8.1 AMC ↔ AIMC

### FR-501 — AI Action Initiation

| Field | Value |
|---|---|
| **Requirement ID** | FR-501 |
| **Actor** | Maturion (AI-initiated); Johan Ras (oversight); specialist agent (requests) |
| **Trigger / Precondition** | AI action originates from: Maturion conversation, Maturion proactive detection, specialist agent request, or user-initiated AI task |
| **Required System Behavior** | AMC creates an AI action request record: action type, originating actor, AIMC route target, approval requirement flag. If approval required: action enters Approval Queue. If no approval required (or post-approval): action is dispatched to AIMC via governed API call. AMC records: dispatch timestamp, action ID, AIMC route, dispatch status |
| **User-Visible Result** | AI Action Monitor entry created; if approval required → Approval Queue entry shown; otherwise → dispatching status shown |
| **Required State / Audit Effect** | AuditEvent: `AIMC_ACTION_INITIATED` (actor, action_type, route, timestamp) |
| **Approval / Authority Constraint** | Governance-sensitive AI actions require approval (FR-307). Non-governance-sensitive actions within Maturion's delegated scope proceed without approval |
| **Failure / Degraded Expectation** | If AIMC is unavailable: action dispatch fails immediately; AIMC degraded mode entered (FR-1601); user sees explicit degraded state. No fallback to direct model calls is permitted |

### FR-502 — AI Action Result Surfacing

| Field | Value |
|---|---|
| **Requirement ID** | FR-502 |
| **Actor** | AIMC (callback), Johan Ras / Maturion (recipients) |
| **Trigger / Precondition** | AIMC completes processing and returns result to AMC callback endpoint |
| **Required System Behavior** | AMC receives AIMC result payload. Records: outcome, result_summary, completed_at, aimc_ref. Surfaces result in AI Action Monitor: outcome summary, audit reference, timestamp |
| **User-Visible Result** | Result visible in AI Action Monitor with outcome and audit reference |
| **Required State / Audit Effect** | AuditEvent: `AIMC_ACTION_COMPLETED` (action_id, outcome, timestamp) |
| **Approval / Authority Constraint** | None for result receipt |
| **Failure / Degraded Expectation** | If AIMC returns an error: error surfaced explicitly to user; error recorded in `aimc_action_log`; no silent suppression of AIMC error responses |

### FR-503 — AIMC Non-Bypass Rule Enforcement

| Field | Value |
|---|---|
| **Requirement ID** | FR-503 |
| **Actor** | System (enforcement rule) |
| **Trigger / Precondition** | Any AI model interaction request originates from AMC context |
| **Required System Behavior** | AMC must route all AI model requests through the AIMC API. Direct calls to underlying model providers from AMC application logic are prohibited at the architecture level. This is a hard enforcement rule — not a soft recommendation |
| **User-Visible Result** | N/A (enforcement constraint) |
| **Required State / Audit Effect** | Any attempt to bypass AIMC must generate a system error event recorded in audit trail |
| **Approval / Authority Constraint** | No bypass is permitted. Not overridable by any user action |
| **Failure / Degraded Expectation** | AIMC unavailability does not authorize fallback to direct model calls. AIMC unavailability triggers degraded mode (FR-1601) |

### FR-504 — AI Action Monitor

| Field | Value |
|---|---|
| **Requirement ID** | FR-504 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | User navigates to AI Action Monitor |
| **Required System Behavior** | AMC displays all active and recent AI actions: action type, AIMC route, status, outcome (for completed), audit reference, degraded mode indicator (if AIMC unavailable) |
| **User-Visible Result** | AI action list visible with status and AIMC route per item |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If AIMC is unavailable: AI Action Monitor shows explicit degraded banner; new AI actions cannot be dispatched |

---

## 9. FR-600: AIMCC / Knowledge Upload Centre Supervision

> Stage 1 Traceability: §2 AIMCC/KUC Boundary, §18 Multi-Layer AI Integration Model, §3 AIMCC/KUC Oversight Success Criteria
> Stage 2 Traceability: §4.6 Knowledge Upload/Ingestion Supervision Journey, §7.6 AIMCC/KUC Supervision Wiring, §8.2 AMC ↔ AIMCC/KUC

### FR-601 — AIMCC/Knowledge Supervision Surface Load

| Field | Value |
|---|---|
| **Requirement ID** | FR-601 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | User navigates to AIMCC/Knowledge Supervision surface |
| **Required System Behavior** | AMC fetches upload status from AIMCC API. Displays: active uploads, ingestion pipeline status, recent outcomes, pending governance actions. Each item shows: document name, submitter, submission time, KUC receipt status, AIMCC ingestion state, outcome |
| **User-Visible Result** | Upload list with KUC/AIMCC status per item; pipeline status visible |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If AIMCC is unavailable: explicit AIMCC degraded banner; upload items shown with stale-data indicator; no real-time updates available (FR-1602) |

### FR-602 — Upload Detail View

| Field | Value |
|---|---|
| **Requirement ID** | FR-602 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | User selects an upload item |
| **Required System Behavior** | AMC displays Upload Detail: upload metadata, KUC routing record, AIMCC ingestion progress/outcome, knowledge-system storage confirmation, audit reference. The full provenance chain (KUC submission → AIMCC ingestion → knowledge-system storage) must be visible |
| **User-Visible Result** | Upload Detail panel open with full provenance chain |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If provenance lookup fails: explicit failure indicator; partial available provenance still shown |

### FR-603 — Knowledge Upload Quota Supervision

| Field | Value |
|---|---|
| **Requirement ID** | FR-603 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | AIMCC/Knowledge Supervision surface loaded |
| **Required System Behavior** | AMC surfaces dynamic upload quota state sourced from AIMCC: current quota, usage percentage, threshold warnings, approved quota change status |
| **User-Visible Result** | Quota panel visible with current usage and threshold warnings |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | Quota changes require approval through FR-604 |
| **Failure / Degraded Expectation** | If AIMCC unavailable: quota panel shows stale indicator and last-known values |

### FR-604 — AIMCC Governance Action (Approval Routing)

| Field | Value |
|---|---|
| **Requirement ID** | FR-604 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | A governance action is required (e.g., quota review approval, flagged content requiring decision) |
| **Required System Behavior** | AMC creates a new approval record referencing the AIMCC governance context (aimcc_context_id). The approval item surfaces in the Approval Queue. User decides through standard approval workflow (FR-303/FR-304). The decision is recorded with audit trail. AIMCC is notified of the outcome |
| **User-Visible Result** | Approval item created in queue; decision recorded and AIMCC notified |
| **Required State / Audit Effect** | AuditEvent: `AIMCC_GOVERNANCE_ACTION_CREATED` (actor, context_id, action_type, timestamp) |
| **Approval / Authority Constraint** | Quota approval and content governance actions require Johan Ras |
| **Failure / Degraded Expectation** | If AIMCC governance actions cannot be processed while AIMCC is degraded: actions remain frozen in pending state; no silent approval or rejection |

### FR-605 — AIMCC Non-Bypass Rule Enforcement

| Field | Value |
|---|---|
| **Requirement ID** | FR-605 |
| **Actor** | System (enforcement rule) |
| **Trigger / Precondition** | Any knowledge upload or ingestion action is initiated from AMC context |
| **Required System Behavior** | All knowledge upload and ingestion actions must route through KUC/AIMCC. AMC must not initiate knowledge ingestion directly. Any knowledge upload submission from AMC must POST to the KUC API endpoint — not directly to AIMCC internal ingestion endpoints |
| **User-Visible Result** | N/A (enforcement constraint) |
| **Required State / Audit Effect** | Any bypass attempt must generate a system error event |
| **Approval / Authority Constraint** | No bypass permitted |
| **Failure / Degraded Expectation** | AIMCC unavailability does not authorize direct ingestion bypass |

---

## 10. FR-700: Memory-Aware / Knowledge-Aware Operating View

> Stage 1 Traceability: §2 Knowledge/Memory System Boundary, §3 Memory-Aware Operational Clarity, §24 Shared State Architecture
> Stage 2 Traceability: §4.7 Memory-Aware/Knowledge-Aware Operating View Journey, §7.7 Knowledge-Aware Operating View Wiring, §8.3 AMC ↔ Knowledge/Memory System

### FR-701 — Knowledge Retrieval Request

| Field | Value |
|---|---|
| **Requirement ID** | FR-701 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | User or Maturion initiates a knowledge retrieval (e.g., "What does the estate know about X?") |
| **Required System Behavior** | AMC routes the retrieval request via governed API to the knowledge/memory system. The knowledge/memory system returns references with provenance metadata (source document, ingestion date, AIMCC tracking reference, confidence indicators). AMC surfaces retrieved knowledge with full provenance: source, ingestion path, retrieval timestamp. Provenance is mandatory — anonymous presentation of retrieved knowledge is prohibited |
| **User-Visible Result** | Knowledge references listed with provenance: source, ingestion path, retrieval timestamp |
| **Required State / Audit Effect** | AuditEvent: `KNOWLEDGE_RETRIEVED` (actor, query_summary, source_ref, timestamp) |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If knowledge/memory system is degraded: retrieval request surfaces with explicit failure message; no stale data served as if current (FR-1603) |

### FR-702 — Provenance Chain Display

| Field | Value |
|---|---|
| **Requirement ID** | FR-702 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | User selects a knowledge reference to view provenance chain |
| **Required System Behavior** | AMC fetches and displays the full provenance chain: source document → KUC submission → AIMCC ingestion → knowledge-system storage. AMC makes explicit that this is retrieved knowledge (not AMC-originated), with named provenance |
| **User-Visible Result** | Provenance chain displayed from source through to storage confirmation |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None |
| **Failure / Degraded Expectation** | If provenance lookup fails: explicit failure shown; partial chain displayed if available |

### FR-703 — Knowledge Non-Ownership Rule

| Field | Value |
|---|---|
| **Requirement ID** | FR-703 |
| **Actor** | System (enforcement rule) |
| **Trigger / Precondition** | Any knowledge reference is surfaced in AMC |
| **Required System Behavior** | AMC must not silently cache or duplicate knowledge/memory truth beyond transient presentation state. AMC must not become the canonical long-term store of estate knowledge. All persistent knowledge/memory truth remains owned by the knowledge/memory system |
| **User-Visible Result** | All knowledge references are visibly attributed to their source; none are presented as AMC-originated authoritative facts |
| **Required State / Audit Effect** | Enforcement constraint; no audit event for read |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | Knowledge system degradation must never cause AMC to serve stale cached data as current knowledge |

---

## 11. FR-800: Executive Conversation with Maturion

> Stage 1 Traceability: §23 Two-Way Conversational Interaction, §18 Executive AI Role, §23 AI-Mediated UX Discipline
> Stage 2 Traceability: §4.8 Executive Conversation Journey, §7.8 Executive Conversation Wiring

### FR-801 — Conversation Surface Load

| Field | Value |
|---|---|
| **Requirement ID** | FR-801 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User opens the Conversation surface (persistent panel on Executive Dashboard, or full-screen from nav) |
| **Required System Behavior** | AMC loads recent conversation history from `conversation_messages` store. Unread messages are marked as unread. The conversation is accessible both as a persistent panel on the dashboard and as a full-screen surface |
| **User-Visible Result** | Conversation history loaded; unread messages marked |
| **Required State / Audit Effect** | Read-only for load; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If AIMC is unavailable: conversation history loads but new Maturion responses are unavailable; explicit degraded message shown |

### FR-802 — User Message Send

| Field | Value |
|---|---|
| **Requirement ID** | FR-802 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User types and submits a message in the Conversation surface |
| **Required System Behavior** | AMC records the user message in `conversation_messages` (message text, timestamp, session_id). AMC dispatches the message to AIMC for Maturion processing. Message is displayed in the conversation thread immediately |
| **User-Visible Result** | User message visible in thread; Maturion response pending indicator shown |
| **Required State / Audit Effect** | AuditEvent: `CONVERSATION_MESSAGE_SENT` (actor, message_summary, timestamp) |
| **Approval / Authority Constraint** | None |
| **Failure / Degraded Expectation** | If AIMC dispatch fails: message is stored; explicit error shown; user is informed that Maturion response is unavailable |

### FR-803 — Maturion Response Display

| Field | Value |
|---|---|
| **Requirement ID** | FR-803 |
| **Actor** | AIMC (callback), Maturion (response source) |
| **Trigger / Precondition** | AIMC returns Maturion response to AMC |
| **Required System Behavior** | AMC receives and stores the Maturion response in `conversation_messages`. Response is rendered in the conversation thread with: response text, response type indicator (Observation \| Recommendation \| Request \| Decision \| Alert), source/reasoning summary where applicable, linked actions (link to approval item, intervention, or alert where applicable) |
| **User-Visible Result** | Maturion response visible with type indicator and linked actions |
| **Required State / Audit Effect** | AuditEvent: `CONVERSATION_RESPONSE_RECEIVED` (actor: Maturion, response_type, aimc_ref, timestamp) |
| **Approval / Authority Constraint** | None |
| **Failure / Degraded Expectation** | None — this is success path |

### FR-804 — Maturion Proactive Message

| Field | Value |
|---|---|
| **Requirement ID** | FR-804 |
| **Actor** | Maturion (AI-initiated via AIMC) |
| **Trigger / Precondition** | AIMC pushes a Maturion-initiated proactive message to AMC |
| **Required System Behavior** | AMC records the proactive message in `conversation_messages` with: type, priority, timestamp. If the message is alert-class: a corresponding alert record is also created. The message is displayed in the Conversation surface with a proactive indicator and priority level. Linked actions are surfaced |
| **User-Visible Result** | Proactive message visible with priority indicator; linked actions accessible |
| **Required State / Audit Effect** | AuditEvent: `PROACTIVE_MESSAGE_RECEIVED` (actor: Maturion, type, priority, timestamp) |
| **Approval / Authority Constraint** | Maturion proactive messages are within delegated executive scope |
| **Failure / Degraded Expectation** | If AMC fails to record proactive message: failure is logged as system error; Maturion-side may retry |

### FR-805 — Conversation Session Persistence

| Field | Value |
|---|---|
| **Requirement ID** | FR-805 |
| **Actor** | System (persistence rule) |
| **Trigger / Precondition** | User switches from desktop to mobile (or vice versa), or navigates away and returns |
| **Required System Behavior** | Conversation state is persistent across devices and navigation. The same conversation history is visible on mobile and desktop. An action taken on mobile (e.g., acknowledging a message) is visible immediately on desktop and vice versa |
| **User-Visible Result** | Same conversation context visible across devices; no context loss on navigation |
| **Required State / Audit Effect** | Persistence is a state requirement; no specific audit event |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | If synchronization between devices fails: explicit synchronization warning shown; user is not misled into thinking they have complete current state |

### FR-806 — AI Response Type Discipline

| Field | Value |
|---|---|
| **Requirement ID** | FR-806 |
| **Actor** | System (enforcement rule for Maturion response rendering) |
| **Trigger / Precondition** | Any Maturion response is rendered in AMC |
| **Required System Behavior** | Every Maturion response must be labeled with a response type indicator: Observation, Recommendation, Request, Decision, or Alert. AMC must not render a Recommendation as if it were an approved Decision. AMC must not render an AI Request as if it were an obligation. Type labels are mandatory — unlabeled Maturion responses are prohibited from rendering |
| **User-Visible Result** | Response type visible on every Maturion message |
| **Required State / Audit Effect** | Enforcement rule; audit captured in `CONVERSATION_RESPONSE_RECEIVED` |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | If response type metadata is missing from AIMC response: AMC must render the response with an explicit "type unavailable" indicator rather than suppressing the type or defaulting to "Decision" |

### FR-807 — Message Acknowledgment

| Field | Value |
|---|---|
| **Requirement ID** | FR-807 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User explicitly acknowledges a Maturion message in the conversation |
| **Required System Behavior** | AMC records acknowledgment: acknowledged_at, acknowledged_by |
| **User-Visible Result** | Message marked acknowledged |
| **Required State / Audit Effect** | AuditEvent: `MESSAGE_ACKNOWLEDGED` (actor, message_id, timestamp) |
| **Approval / Authority Constraint** | Actor must be authorized |
| **Failure / Degraded Expectation** | If write fails: acknowledgment not shown as complete; explicit error |

---

## 12. FR-900: Specialist Agent Workspace Oversight

> Stage 1 Traceability: §13 Specialist-Agent Layer, §18 Specialist-Agent Integration
> Stage 2 Traceability: §5.1 Specialist Agent Workspace Oversight Journey

### FR-901 — Specialist Agent Oversight Surface Load

| Field | Value |
|---|---|
| **Requirement ID** | FR-901 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | User navigates to Specialist Agent Oversight surface |
| **Required System Behavior** | AMC displays list of active and recent specialist agent workspaces: name, type, scope, current status. Sandbox isolation indicator is always visible |
| **User-Visible Result** | Workspace list with status and sandbox isolation indicator visible per item |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If workspace status feed is unavailable: explicit unavailability shown; list shows last-known state with stale indicator |

### FR-902 — Workspace Detail View

| Field | Value |
|---|---|
| **Requirement ID** | FR-902 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | User selects a workspace |
| **Required System Behavior** | AMC displays Workspace Detail: purpose, scope boundary, current status, active tasks, last reporting event, any escalations. AMC shows outcomes — not internal specialist state. The sandbox scope boundary must be explicitly labeled |
| **User-Visible Result** | Workspace Detail shows outcomes and scope boundary; no internal specialist state exposed |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If detail load fails: explicit error |

### FR-903 — Escalate Workspace Issue

| Field | Value |
|---|---|
| **Requirement ID** | FR-903 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | User selects "Escalate issue" from a workspace |
| **Required System Behavior** | AMC routes escalation to Maturion (via Conversation surface) or creates an alert. Follows Escalation/Intervention wiring (§7.4 Stage 2) |
| **User-Visible Result** | Escalation created; routes to Alert Centre or Conversation |
| **Required State / Audit Effect** | As per FR-204 escalation audit |
| **Approval / Authority Constraint** | As per escalation authority rules |
| **Failure / Degraded Expectation** | If escalation fails: explicit error |

### FR-904 — Terminate Workspace (Approval-Gated)

| Field | Value |
|---|---|
| **Requirement ID** | FR-904 |
| **Actor** | Johan Ras (authority decision) |
| **Trigger / Precondition** | User selects "Terminate workspace" from a workspace detail |
| **Required System Behavior** | If approval is required (reserved matter or authority-sensitive): termination request enters Approval Queue before execution. On approval: AMC dispatches termination order through governed pathway. Termination is traceable |
| **User-Visible Result** | If approval required → Approval Queue entry shown; on approval → termination confirmed |
| **Required State / Audit Effect** | As per FR-303/FR-403 approval and intervention audit |
| **Approval / Authority Constraint** | Workspace termination is approval-gated where authority requires it. Not self-authorized by specialist agent or Maturion alone |
| **Failure / Degraded Expectation** | If termination fails after approval: failure surfaced; cancellation record retained |

---

## 13. FR-1000: Maintenance & Assurance Reporting

> Stage 1 Traceability: §2 In Scope (maintenance/assurance), §13 Maintenance and Operational Support Layer, §13 Independent Assurance Layer
> Stage 2 Traceability: §5.2 Maintenance & Assurance Reporting Journey

### FR-1001 — Maintenance & Assurance Reports Surface Load

| Field | Value |
|---|---|
| **Requirement ID** | FR-1001 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | User navigates to Maintenance & Assurance Reports surface |
| **Required System Behavior** | AMC displays: scheduled health checks with last-run status, maintenance findings summaries, assurance scan results. Items colour-coded by severity: all clear / advisory / warning / critical finding. Assurance outputs (IAA verdicts) are displayed separately from maintenance outputs — IAA independence is preserved |
| **User-Visible Result** | Reports listed by agent/type, severity-coded; IAA and maintenance outputs visually separated |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If reporting feed is unavailable: explicit unavailability shown |

### FR-1002 — Report Detail View

| Field | Value |
|---|---|
| **Requirement ID** | FR-1002 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User selects a report |
| **Required System Behavior** | AMC displays Report Detail: findings, severity, recommended action, originating agent (maintenance or IAA), evidence reference |
| **User-Visible Result** | Report Detail visible with severity, findings, and recommended action |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | None for read |
| **Failure / Degraded Expectation** | If evidence reference is unavailable: explicit note shown |

### FR-1003 — Critical Finding Alert Generation

| Field | Value |
|---|---|
| **Requirement ID** | FR-1003 |
| **Actor** | System (automatic) |
| **Trigger / Precondition** | A maintenance or assurance report contains a critical-severity finding |
| **Required System Behavior** | AMC automatically generates a Critical alert in the Alert Centre (FR-201). The alert references the originating report |
| **User-Visible Result** | Critical alert appears in Alert Centre with report reference |
| **Required State / Audit Effect** | Alert record created; audit event as per alert creation |
| **Approval / Authority Constraint** | System-generated; no approval required for alert creation |
| **Failure / Degraded Expectation** | If alert creation fails: system-level error recorded; finding remains visible in report surface |

### FR-1004 — Create Intervention from Maintenance Finding

| Field | Value |
|---|---|
| **Requirement ID** | FR-1004 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User selects "Create intervention" from a report finding |
| **Required System Behavior** | AMC creates an intervention record pre-populated with the report finding context. Follows standard intervention initiation (FR-402) |
| **User-Visible Result** | Intervention created; user navigated to Intervention Manager |
| **Required State / Audit Effect** | As per FR-402 audit |
| **Approval / Authority Constraint** | As per FR-402 authority constraints |
| **Failure / Degraded Expectation** | As per FR-402 failure handling |

---

## 14. FR-1100: Estate Configuration & Wellbeing

> Stage 1 Traceability: §2 In Scope (build/job initiation, operational wellbeing), §5 Build Lifecycle Stages
> Stage 2 Traceability: §5.3 Estate Configuration & Wellbeing Journey

### FR-1101 — Estate Configuration Surface Load

| Field | Value |
|---|---|
| **Requirement ID** | FR-1101 |
| **Actor** | Johan Ras, Maturion |
| **Trigger / Precondition** | User navigates to Estate Configuration & Wellbeing surface |
| **Required System Behavior** | AMC displays: active build jobs and governance lifecycle stages with status, estate configuration summary (deployment state, active environment, key parameters — read-only), deployment wave status |
| **User-Visible Result** | Configuration summary, active build/job statuses, deployment wave status visible |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | Configuration is read-only unless a configuration change is explicitly approved |
| **Failure / Degraded Expectation** | If Foreman reporting is unavailable: build status shows explicit stale indicator |

### FR-1102 — Request Configuration Change (Approval-Gated)

| Field | Value |
|---|---|
| **Requirement ID** | FR-1102 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User requests a configuration change |
| **Required System Behavior** | AMC creates an approval request for the configuration change. The approval enters the Approval Queue for Johan Ras (reserved matter handling per FR-307). Until approval is granted, the configuration remains unchanged. On approval: approved change is dispatched through the governed execution pathway |
| **User-Visible Result** | Approval request created; configuration unchanged until decision recorded |
| **Required State / Audit Effect** | As per FR-303/FR-304 approval audit |
| **Approval / Authority Constraint** | Configuration changes are reserved-matter-adjacent and require Johan Ras approval |
| **Failure / Degraded Expectation** | Configuration must remain in prior state if approval fails or dispatch fails |

### FR-1103 — Build/Job Status Visibility

| Field | Value |
|---|---|
| **Requirement ID** | FR-1103 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User views active build/job statuses on Estate Configuration surface |
| **Required System Behavior** | AMC surfaces Foreman reporting events as read-only build status. Johan oversees but does not directly control Foreman's orchestration. Build status is display-only — AMC does not issue build commands |
| **User-Visible Result** | Active build/job statuses visible in read-only mode |
| **Required State / Audit Effect** | Read-only; no audit event |
| **Approval / Authority Constraint** | Read-only; no approval for view |
| **Failure / Degraded Expectation** | If Foreman feed is unavailable: explicit stale indicator shown |

---

## 15. FR-1200: Mobile Continuity

> Stage 1 Traceability: §23 Mobile and Cross-Context Responsiveness, §23 Desktop/Mobile Continuity
> Stage 2 Traceability: §5.4 Mobile Continuity Journey

### FR-1201 — Mobile Responsive Layout

| Field | Value |
|---|---|
| **Requirement ID** | FR-1201 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User accesses AMC on a mobile device |
| **Required System Behavior** | AMC activates mobile-responsive layout. Mobile landing view shows: condensed estate health summary and Alert Panel with most critical items surfaced immediately. Mobile does not merely mirror desktop visuals — it must support real executive action |
| **User-Visible Result** | Mobile-optimized layout active with critical items prominent |
| **Required State / Audit Effect** | Layout adaptation; no audit event |
| **Approval / Authority Constraint** | None |
| **Failure / Degraded Expectation** | If layout adaptation fails: user receives explicit mobile layout error; app remains functional in degraded mobile layout |

### FR-1202 — Mobile Critical Alert Interrupt

| Field | Value |
|---|---|
| **Requirement ID** | FR-1202 |
| **Actor** | System (push notification), Johan Ras (recipient) |
| **Trigger / Precondition** | A Critical alert is generated while user is on mobile |
| **Required System Behavior** | Critical alert interrupts the operator on mobile via push notification or in-app alert even if AMC is in background. Tap on notification opens alert detail directly |
| **User-Visible Result** | Critical alert visible immediately even on mobile; tap → Alert Detail |
| **Required State / Audit Effect** | As per alert audit |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | If push notification fails: in-app alert banner shown on next AMC open; no silent loss of Critical alert notification |

### FR-1203 — Mobile Approval & Acknowledgment

| Field | Value |
|---|---|
| **Requirement ID** | FR-1203 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User is on mobile and has an alert or approval requiring action |
| **Required System Behavior** | AMC provides mobile-optimized approval view: concise but complete (what/why/consequence). Rapid approve/reject path is available. Acknowledgment is executable from mobile. Actions on mobile trigger the same wiring as desktop |
| **User-Visible Result** | Approve/Reject and Acknowledge actions accessible on mobile |
| **Required State / Audit Effect** | As per approval and acknowledgment audit |
| **Approval / Authority Constraint** | As per FR-303/FR-304/FR-203 |
| **Failure / Degraded Expectation** | Mobile approval must not drop actions due to network interruption; retry available |

### FR-1204 — Cross-Device Session Continuity

| Field | Value |
|---|---|
| **Requirement ID** | FR-1204 |
| **Actor** | System (state synchronization) |
| **Trigger / Precondition** | User switches between mobile and desktop devices |
| **Required System Behavior** | State is synchronized between mobile and desktop: alert state, approval decisions, conversation history, intervention status are consistent across both. An action taken on mobile is immediately visible on desktop and vice versa |
| **User-Visible Result** | No action or state is lost between mobile and desktop context switches |
| **Required State / Audit Effect** | Synchronization is a state requirement; no specific audit event |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | If synchronization fails: explicit warning shown on whichever device detects the discrepancy; user is not presented with contradictory states without warning |

---

## 16. FR-1300: Audit & Provenance

> Stage 1 Traceability: §26 Audit Log Design, §3 State/Audit/Provenance Success Criteria
> Stage 2 Traceability: §7 Wiring Model (audit columns throughout)

### FR-1301 — Mandatory Audit Event Fields

| Field | Value |
|---|---|
| **Requirement ID** | FR-1301 |
| **Actor** | System (enforcement rule) |
| **Trigger / Precondition** | Any consequential action or system event occurs |
| **Required System Behavior** | Every audit event in AMC must include at minimum: `actor` (human or agent who initiated), `source_system` (AMC, AIMC, AIMCC, etc.), `approval_basis` (where applicable), `timestamp` (ISO 8601 UTC), `object` (entity affected), `action` (action type), `state_transition` (before/after state where applicable), `outcome` (success/failure/partial/pending) |
| **User-Visible Result** | N/A (system enforcement) |
| **Required State / Audit Effect** | Audit record created with all mandatory fields |
| **Approval / Authority Constraint** | Audit records must not be mutable. Corrections must be made as additive corrective records, not silent overwrites |
| **Failure / Degraded Expectation** | If mandatory audit fields cannot be populated: the action must be blocked or the event must be flagged as incomplete in the audit trail. Silent omission of mandatory audit fields is prohibited |

### FR-1302 — Required Audit Event Coverage

| Field | Value |
|---|---|
| **Requirement ID** | FR-1302 |
| **Actor** | System |
| **Trigger / Precondition** | Any covered event type occurs |
| **Required System Behavior** | AMC must generate audit events for all of the following event types: (1) alert generation, acknowledgment, escalation, expiry; (2) approval granted, approval rejected, approval deferred; (3) intervention initiated, dispatched, completed, cancelled, failed; (4) AIMC-routed AI action (request, response, error); (5) knowledge upload submitted via KUC; (6) ingestion outcome received from AIMCC; (7) knowledge reference retrieved in decision-support context; (8) authentication events (login, session expiry, unauthorized access attempt); (9) degraded-mode entry and exit for each external dependency; (10) any executive action that changes persisted state |
| **User-Visible Result** | N/A (backend requirement) |
| **Required State / Audit Effect** | Complete audit trail per event type as listed |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | Missing audit events for covered types are governance defects |

### FR-1303 — Audit Accessibility

| Field | Value |
|---|---|
| **Requirement ID** | FR-1303 |
| **Actor** | Johan Ras, IAA agents, authorized reviewers |
| **Trigger / Precondition** | Reviewer accesses audit trail |
| **Required System Behavior** | AMC audit model must support review by: actor, app/sandbox, authority domain, event class, time range. It must be possible to reconstruct timelines, inspect approval chains, inspect AI-mediated action histories. Audit data must be practically usable, not just technically stored |
| **User-Visible Result** | Audit review surfaces provide filtered views by actor, event class, time range |
| **Required State / Audit Effect** | Read-only for audit review |
| **Approval / Authority Constraint** | Audit visibility is governed: executive-only records are restricted to Johan/Maturion; assurance agents may see their relevant audit scope |
| **Failure / Degraded Expectation** | If audit review fails: explicit error; audit data must not be silently inaccessible |

### FR-1304 — Cross-System Event Integrity

| Field | Value |
|---|---|
| **Requirement ID** | FR-1304 |
| **Actor** | System |
| **Trigger / Precondition** | An action spans multiple systems (e.g., AMC initiates → AIMC executes) |
| **Required System Behavior** | The audit record for the AMC-originating event must contain sufficient provenance to link it to the downstream execution event in AIMC/AIMCC. The audit trail must not lose the chain of custody at system boundaries |
| **User-Visible Result** | N/A (audit backend requirement) |
| **Required State / Audit Effect** | Cross-system linkage fields present in audit records |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | If cross-system provenance cannot be established: the event is flagged in the audit trail as cross-system linkage incomplete |

---

## 17. FR-1400: Authentication & Authorization

> Stage 1 Traceability: §17 Auth Wiring Checklist, §25 API Authentication, §13 Authority Matrix
> Stage 2 Traceability: §7 Wiring Model (Approval/Authority columns throughout)

### FR-1401 — User Authentication

| Field | Value |
|---|---|
| **Requirement ID** | FR-1401 |
| **Actor** | Johan Ras |
| **Trigger / Precondition** | User accesses AMC URL |
| **Required System Behavior** | AMC presents login surface. User authenticates via Supabase Auth (email/password + MFA if enabled). On success: JWT issued; user redirected to Executive Dashboard. On failure: explicit error message shown; retry available |
| **User-Visible Result** | Login form displayed; on success → Executive Dashboard; on failure → error with retry |
| **Required State / Audit Effect** | AuditEvent: auth login event (actor, timestamp, outcome) |
| **Approval / Authority Constraint** | Authentication is mandatory; no unauthenticated access to any AMC surface |
| **Failure / Degraded Expectation** | Auth service unavailability: explicit service-unavailable message; no bypass path exists |

### FR-1402 — Authority-Aware Action Enforcement

| Field | Value |
|---|---|
| **Requirement ID** | FR-1402 |
| **Actor** | System (enforcement rule) |
| **Trigger / Precondition** | Any consequential action is initiated |
| **Required System Behavior** | AMC evaluates the authority domain and actor identity before permitting any consequential action. Reserved-matter actions require Johan Ras. Delegated actions require the authorized delegated actor (Maturion within approved scope). Unauthorized action attempts are rejected with explicit feedback. Authority evaluation is not based on login status alone — it includes role-based and domain-based authority checks |
| **User-Visible Result** | Unauthorized actions produce explicit rejection messages, not silent failures |
| **Required State / Audit Effect** | AuditEvent: unauthorized access attempt (actor, action, timestamp) |
| **Approval / Authority Constraint** | Enforcement constraint |
| **Failure / Degraded Expectation** | Auth or authority service degradation must not default to open access. If authority cannot be verified: action must be blocked |

### FR-1403 — Identity Separation

| Field | Value |
|---|---|
| **Requirement ID** | FR-1403 |
| **Actor** | System (enforcement rule) |
| **Trigger / Precondition** | Multiple actor types interact with AMC |
| **Required System Behavior** | AMC must distinguish between human identities (Johan Ras), AI executive identity (Maturion), orchestration identity (Foreman), assurance identity (IAA agents), specialist agent identities, and service/system identities. These must not be collapsed into a single undifferentiated access principal |
| **User-Visible Result** | N/A (backend enforcement) |
| **Required State / Audit Effect** | Actor type is recorded in all audit events |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | If identity resolution fails: action is blocked |

---

## 18. FR-1500: Cross-System Integration & Boundary Enforcement

> Stage 1 Traceability: §2 Boundary Definitions, §18 Multi-Layer AI Integration Model, §29 Cross-System Topology Declaration
> Stage 2 Traceability: §8 Cross-System Integration Wiring

### FR-1501 — AIMC Health Check

| Field | Value |
|---|---|
| **Requirement ID** | FR-1501 |
| **Actor** | System (periodic health monitor) |
| **Trigger / Precondition** | Periodic health check cycle or failed AIMC call |
| **Required System Behavior** | AMC performs periodic and on-demand health checks against the AIMC health endpoint. If AIMC health check fails: AIMC degraded mode is entered (FR-1601). If AIMC recovers: recovery detected on next successful health check; degraded mode exited |
| **User-Visible Result** | AIMC degraded banner when unavailable; cleared on recovery |
| **Required State / Audit Effect** | AuditEvent: `AIMC_DEGRADED` (detected_at, impact_summary); AuditEvent: `AIMC_RECOVERED` (recovered_at) |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | Failure to perform health check is itself a system health event |

### FR-1502 — AIMCC Health Check

| Field | Value |
|---|---|
| **Requirement ID** | FR-1502 |
| **Actor** | System |
| **Trigger / Precondition** | Periodic health check cycle or failed AIMCC call |
| **Required System Behavior** | AMC performs periodic and on-demand health checks against the AIMCC health endpoint. If AIMCC health check fails: AIMCC degraded mode is entered (FR-1602). If AIMCC recovers: degraded mode exited |
| **User-Visible Result** | AIMCC degraded banner when unavailable; cleared on recovery |
| **Required State / Audit Effect** | AuditEvent: `AIMCC_DEGRADED` (detected_at); AuditEvent on recovery |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | As per FR-1602 |

### FR-1503 — Knowledge/Memory System Health Check

| Field | Value |
|---|---|
| **Requirement ID** | FR-1503 |
| **Actor** | System |
| **Trigger / Precondition** | Periodic health check or failed retrieval |
| **Required System Behavior** | AMC performs health checks against the knowledge/memory system health endpoint. If degraded: FR-1603 degraded mode entered |
| **User-Visible Result** | Knowledge system degraded indicator on all knowledge surfaces when unavailable |
| **Required State / Audit Effect** | AuditEvent: `KNOWLEDGE_SYSTEM_DEGRADED` (detected_at) |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | As per FR-1603 |

### FR-1504 — Governed Auth Token for External Calls

| Field | Value |
|---|---|
| **Requirement ID** | FR-1504 |
| **Actor** | System |
| **Trigger / Precondition** | Any API call to AIMC, AIMCC, KUC, or knowledge/memory system |
| **Required System Behavior** | AMC must pass a governed auth token with every external API call. Anonymous calls to governed external services are prohibited. Token validation is performed by the receiving service |
| **User-Visible Result** | N/A |
| **Required State / Audit Effect** | Auth token presence is verifiable in audit trail |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | If auth token cannot be issued: external call must be blocked; not attempted without token |

---

## 19. FR-1600: Degraded-Mode Behavior

> Stage 1 Traceability: §18 Degraded Mode Requirements, §3 Integration Success Criteria
> Stage 2 Traceability: §9 Degraded-Mode Operating Patterns

### FR-1601 — AIMC Unavailable Degraded Mode

| Field | Value |
|---|---|
| **Requirement ID** | FR-1601 |
| **Actor** | System |
| **Trigger / Precondition** | AIMC health check fails or AIMC call returns non-OK status |
| **Required System Behavior** | (1) Explicit AIMC degraded-mode banner displayed on all surfaces where AI features are shown. (2) Conversation surface: Maturion responses unavailable; explicit "Maturion communication unavailable — AIMC unreachable" message displayed. (3) AI Action Monitor: no new AI actions may be dispatched; pending items frozen with degraded indicator. (4) Approval Queue: AI-sourced approval items show degraded source indicator; manual decision by Johan still possible. (5) No fallback to direct model calls is permitted. (6) AIMC_DEGRADED event recorded in `system_health_events` and audit trail |
| **User-Visible Result** | AIMC degraded banner visible; Maturion unavailable message shown; AI dispatch blocked |
| **Required State / Audit Effect** | AuditEvent: `AIMC_DEGRADED` (detected_at, impact_summary); system_health_events record created |
| **Approval / Authority Constraint** | Johan's ability to make approval decisions independently of Maturion must be preserved during AIMC degraded mode |
| **Failure / Degraded Expectation** | Degraded mode must activate immediately on detection; no delay that creates a window of silent failure |

### FR-1602 — AIMCC Unavailable Degraded Mode

| Field | Value |
|---|---|
| **Requirement ID** | FR-1602 |
| **Actor** | System |
| **Trigger / Precondition** | AIMCC health check fails |
| **Required System Behavior** | (1) Explicit AIMCC degraded-mode banner on AIMCC/Knowledge Supervision surface. (2) Upload status items shown with stale-data indicator; no real-time updates available. (3) Knowledge upload governance actions frozen — approvals dependent on AIMCC state cannot be processed. (4) Knowledge Reference surface: items sourced via AIMCC show stale/unavailable indicator. (5) AIMCC_DEGRADED event recorded in audit trail. (6) Recovery: on health check detecting AIMCC available again → degraded banner cleared → features resume |
| **User-Visible Result** | AIMCC degraded banner visible; upload items show stale indicator |
| **Required State / Audit Effect** | AuditEvent: `AIMCC_DEGRADED` (detected_at) |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | AIMCC governance actions that cannot be processed must remain in pending state — not auto-approved or auto-rejected |

### FR-1603 — Knowledge/Memory System Degraded Mode

| Field | Value |
|---|---|
| **Requirement ID** | FR-1603 |
| **Actor** | System |
| **Trigger / Precondition** | Knowledge/memory system health check fails or retrieval degrades |
| **Required System Behavior** | (1) Explicit stale/unavailable indicator on all knowledge reference items across all surfaces. (2) Retrieval requests that fail are surfaced with explicit failure message — not silently suppressed. (3) AMC does not serve stale cached knowledge as if it were current. (4) Knowledge retrieval degradation event recorded in audit trail. (5) Recovery: on health check detecting system recovery → indicators cleared → retrieval resumes |
| **User-Visible Result** | Stale/unavailable indicator visible on all knowledge items; explicit failure messages on retrieval requests |
| **Required State / Audit Effect** | AuditEvent: `KNOWLEDGE_SYSTEM_DEGRADED` (detected_at) |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | Degraded mode must never cause AMC to silently serve stale knowledge as current |

---

## 20. FR-1700: State & Persistence

> Stage 1 Traceability: §24 Shared State Architecture, §28 State Persistence Specification
> Stage 2 Traceability: §7 Wiring Model (Target Table / State columns throughout)

### FR-1701 — State Domain Ownership

| Field | Value |
|---|---|
| **Requirement ID** | FR-1701 |
| **Actor** | System (architecture constraint) |
| **Trigger / Precondition** | Any state change occurs |
| **Required System Behavior** | AMC-owned state: alert records, approval records, intervention records, audit events, conversation_messages, aimc_action_log, knowledge_retrieval_log, system_health_events. AIMCC-owned state: knowledge_upload_records (ingestion workflow-state and curation metadata). Knowledge/memory system: persistent knowledge/memory truth (sole canonical owner). State ownership must be explicit — AMC must not silently duplicate or claim ownership of state owned by other systems |
| **User-Visible Result** | N/A (architecture enforcement) |
| **Required State / Audit Effect** | State ownership determines where writes are authoritative |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | State write conflicts between systems must be surfaced as errors, not silently resolved by duplication |

### FR-1702 — State Consistency Across Surfaces

| Field | Value |
|---|---|
| **Requirement ID** | FR-1702 |
| **Actor** | System |
| **Trigger / Precondition** | Multiple AMC surfaces are open simultaneously or user navigates between surfaces |
| **Required System Behavior** | AMC must maintain consistent shared state across all open surfaces. An alert acknowledged on the Alert Centre must show as acknowledged on the Executive Dashboard. An approval decision recorded on the Approval Queue must show as resolved on any linked surface. There must be no contradictory state presentations between surfaces |
| **User-Visible Result** | Consistent state visible across all surfaces; no contradictory statuses |
| **Required State / Audit Effect** | N/A |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | If state synchronization fails: surfaces show explicit stale indicator, not false-current data |

### FR-1703 — Session Continuity

| Field | Value |
|---|---|
| **Requirement ID** | FR-1703 |
| **Actor** | System |
| **Trigger / Precondition** | User returns to AMC after navigation away or session interruption |
| **Required System Behavior** | AMC restores executive context: current alert state, approval queue status, active intervention state, conversation history. The executive dashboard reflects current state, not last-visited state |
| **User-Visible Result** | Estate current state visible on return; no stale-state trap |
| **Required State / Audit Effect** | N/A |
| **Approval / Authority Constraint** | N/A |
| **Failure / Degraded Expectation** | If session restore fails: explicit error with retry available; no silent stale-state presentation |

---

## 21. Business Rules & Decision Rules Summary

The following table consolidates the key business rules referenced throughout this FRS for downstream reference:

| Rule ID | Rule Statement | Enforcement Level | Relevant FR |
|---|---|---|---|
| **BR-SYS-001** | Any AI action from AMC that does not route through AIMC is a governance violation. Any knowledge ingestion from AMC that does not route through KUC/AIMCC is a governance violation | Hard enforcement — no exceptions | FR-503, FR-605 |
| **BR-AUTH-001** | Reserved matters require explicit Johan Ras approval. No AMC workflow may silently convert a reserved matter into a routine operational action | Hard enforcement | FR-307, FR-303 |
| **BR-AUTH-002** | Maturion may approve or trigger actions only within explicitly approved delegated domains | Hard enforcement | FR-303, FR-402 |
| **BR-AUTH-003** | AMC must not approve its own governance actions | Hard enforcement | FR-307 |
| **BR-AUTH-004** | AI-generated suggestions must be distinguishable from approved decisions in all interfaces | Hard enforcement | FR-806, FR-803 |
| **BR-ALERT-001** | Acknowledgment of an alert is an explicit actor action, not implicit on view | Hard enforcement | FR-203 |
| **BR-ALERT-002** | Dismissal is restricted to Low/Informational alert class only | Hard enforcement | FR-205 |
| **BR-ALERT-003** | Unacknowledged Critical alerts auto-escalate after defined timeout | Hard enforcement | FR-208 |
| **BR-ALERT-004** | Alert expiry does not silently resolve the underlying condition | Hard enforcement | FR-208 |
| **BR-APPROVAL-001** | Governance-sensitive actions must be blocked until explicit approval is granted | Hard enforcement | FR-307 |
| **BR-APPROVAL-002** | Approval basis is a required field on all approval decisions | Hard enforcement | FR-303 |
| **BR-APPROVAL-003** | Rejection reason is a required field on all rejection decisions | Hard enforcement | FR-304 |
| **BR-AUDIT-001** | Every consequential action must produce an audit event with all mandatory fields | Hard enforcement | FR-1301 |
| **BR-AUDIT-002** | Audit records must be append-oriented; corrections must be additive records, not silent overwrites | Hard enforcement | FR-1301 |
| **BR-STATE-001** | AMC must not silently duplicate or cache persistent knowledge truth beyond transient presentation state | Hard enforcement | FR-703 |
| **BR-STATE-002** | Degraded mode must never cause AMC to serve stale data as current data without an explicit indicator | Hard enforcement | FR-1601, FR-1602, FR-1603 |
| **BR-DEGRADE-001** | AIMC unavailability does not authorize fallback to direct model calls | Hard enforcement | FR-1601, FR-503 |
| **BR-DEGRADE-002** | AIMCC unavailability does not authorize direct knowledge ingestion bypass | Hard enforcement | FR-1602, FR-605 |

---

## 22. Requirement Groupings for Downstream Derivation

The following groupings are provided to assist TRS (Stage 4), Architecture (Stage 5), and QA-to-Red (Stage 6) derivation:

### 22.1 Functional Requirement Families

| Family | Requirements | Primary Downstream Owner |
|---|---|---|
| Executive Estate Oversight | FR-101 to FR-104 | UI, API, Data |
| Alert Management | FR-201 to FR-209 | UI, API, Data, Notification |
| Approval Workflow | FR-301 to FR-307 | UI, API, Data, Auth |
| Intervention | FR-401 to FR-407 | UI, API, Data, Auth |
| AI-Routed Actions (AIMC) | FR-501 to FR-504 | API, AIMC Integration, Data |
| AIMCC/KUC Supervision | FR-601 to FR-605 | UI, API, AIMCC Integration, Data |
| Memory-Aware View | FR-701 to FR-703 | UI, API, Knowledge System Integration, Data |
| Executive Conversation | FR-801 to FR-807 | UI, API, AIMC Integration, Data |
| Specialist Agent Oversight | FR-901 to FR-904 | UI, API, Data |
| Maintenance & Assurance | FR-1001 to FR-1004 | UI, API, Data |
| Estate Config & Wellbeing | FR-1101 to FR-1103 | UI, API, Foreman Integration, Data |
| Mobile Continuity | FR-1201 to FR-1204 | UI, Notification, State |
| Audit & Provenance | FR-1301 to FR-1304 | Data, API, Audit System |
| Authentication & Authorization | FR-1401 to FR-1403 | Auth, API, Data |
| Cross-System Integration | FR-1501 to FR-1504 | API, Integration Layer |
| Degraded-Mode Behavior | FR-1601 to FR-1603 | All layers |
| State & Persistence | FR-1701 to FR-1703 | Data, State Management |

### 22.2 Business Rules Groupings

| Group | Rules |
|---|---|
| System boundary / non-bypass rules | BR-SYS-001, BR-DEGRADE-001, BR-DEGRADE-002 |
| Authority and approval rules | BR-AUTH-001, BR-AUTH-002, BR-AUTH-003, BR-AUTH-004, BR-APPROVAL-001, BR-APPROVAL-002, BR-APPROVAL-003 |
| Alerting rules | BR-ALERT-001, BR-ALERT-002, BR-ALERT-003, BR-ALERT-004 |
| Audit / provenance rules | BR-AUDIT-001, BR-AUDIT-002 |
| State / ownership rules | BR-STATE-001, BR-STATE-002 |

### 22.3 Cross-System Interaction Requirements Summary

| Interaction | AMC Action | Required Pathway | Enforcement |
|---|---|---|---|
| AI model execution | Initiates request | AIMC API only | FR-503, BR-SYS-001 |
| AI result surfacing | Receives AIMC callback | AIMC callback endpoint | FR-502 |
| Knowledge upload | Routes via KUC | KUC API → AIMCC | FR-605, BR-SYS-001 |
| Ingestion status | Reads from AIMCC | AIMCC read API | FR-601 |
| Knowledge retrieval | Queries knowledge/memory system | Governed knowledge API | FR-701 |
| Provenance lookup | Queries AIMCC provenance | AIMCC provenance API | FR-702 |
| Intervention dispatch | Routes to Foreman/specialist agents | Foreman API / Specialist Agent API | FR-403 |
| Build status | Reads Foreman reporting | Foreman reporting event feed (read-only) | FR-1103 |

### 22.4 State / Persistence Expectations Summary

| State Domain | Canonical Owner | AMC Write Access | Notes |
|---|---|---|---|
| Alert records | AMC | Full | Created, updated by AMC |
| Approval records | AMC | Full | Created, updated by AMC |
| Intervention records | AMC | Full | Created, updated by AMC |
| Audit events | AMC | Append-only | FR-1301 |
| Conversation messages | AMC | Full | Includes Maturion responses |
| AIMC action log | AMC | Full | Records dispatches and outcomes |
| Knowledge retrieval log | AMC | Full | Records retrieval requests |
| System health events | AMC | Full | Degraded/recovered events |
| Knowledge upload records | AIMCC (canonical) | Read-only (status surface) | AMC surfaces, does not own |
| Persistent knowledge/memory | Knowledge/memory system (canonical) | None | AMC surfaces with provenance only |

### 22.5 Degraded-Mode Coverage Summary

| Dependency | Degraded Mode ID | Key Behavioral Rule |
|---|---|---|
| AIMC unavailable | FR-1601 | Explicit banner; no AI dispatch; no direct model fallback; Johan can still approve manually |
| AIMCC unavailable | FR-1602 | Explicit banner; stale data indicator; governance actions frozen pending |
| Knowledge/memory degraded | FR-1603 | Explicit stale indicator; no silent staleness; no cached data served as current |

---

*End of Functional Requirements Specification — Stage 3. Produced by foreman-v2-agent under POLC_ORCHESTRATION. CS2 approval required before TRS (Stage 4) derivation begins.*

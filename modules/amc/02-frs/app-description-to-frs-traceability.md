# Stage 1 + Stage 2 to FRS Traceability — Stage 3

**Stage**: 3 — Traceability Artifact
**Module**: App Management Centre (AMC)
**Version**: 1.0
**Status**: 🟡 Produced Approval-Ready — 2026-04-23
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: app_management_centre#1123
**Upstream Sources**:
- Stage 1 App Description: `modules/amc/00-app-description/app-description.md` v1.0
- Stage 2 UX Workflow & Wiring Spec: `modules/amc/01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md` v1.0
**FRS Target**: `modules/amc/02-frs/functional-requirements-specification.md` v1.0

---

> **PURPOSE STATEMENT**
> This document demonstrates that every major approved Stage 1 and Stage 2 commitment is realized in Stage 3 FRS requirements, and that no major approved upstream requirement family was silently dropped. It also shows that the FRS does not introduce requirements without traceable upstream sources.

---

## Table of Contents

1. [Stage 1 → FRS Traceability Matrix](#1-stage-1--frs-traceability-matrix)
2. [Stage 2 → FRS Traceability Matrix](#2-stage-2--frs-traceability-matrix)
3. [FRS Coverage Completeness Check](#3-frs-coverage-completeness-check)
4. [Cross-System Boundary Traceability](#4-cross-system-boundary-traceability)
5. [Dropped / Deferred Commitment Disclosure](#5-dropped--deferred-commitment-disclosure)

---

## 1. Stage 1 → FRS Traceability Matrix

This matrix maps the authoritative Stage 1 App Description sections to the FRS requirement families that realize them.

| Stage 1 Section | Stage 1 Commitment | FRS Requirement(s) | Realized? |
|---|---|---|---|
| **§1 Application Identity / Purpose** | AMC is the executive control centre of the Maturion estate: oversight, monitoring, interventions, approvals, escalation | FR-101 to FR-104 (Estate Oversight), FR-301 to FR-307 (Approvals), FR-401 to FR-407 (Interventions) | ✅ Yes |
| **§1 Target Users** | Johan Ras, Maturion, Foreman, IAA agents, specialist agents, maintenance agents as actors | §3 Actor Model & Authority Constraints (all FRs, actor columns) | ✅ Yes |
| **§1 Core Value Proposition** | Proactive awareness; no manual interrogation required; rapid governed intervention | FR-103 (Proactive Awareness), FR-804 (Maturion Proactive Messages), FR-1202 (Mobile Critical Alert Interrupt) | ✅ Yes |
| **§1 Executive Layer Boundary Definitions** | AMC, AIMC, AIMCC, KUC, knowledge/memory system layers non-negotiable | §2 Cross-System Boundary Rules; FR-503 (AIMC non-bypass), FR-605 (AIMCC non-bypass), FR-703 (knowledge non-ownership) | ✅ Yes |
| **§2 In Scope — Executive oversight** | Estate oversight, alerts, approvals, interventions, audit | FR-100 family, FR-200 family, FR-300 family, FR-400 family, FR-1300 family | ✅ Yes |
| **§2 In Scope — Mobile / desktop access** | Mobile-first and always-available executive access | FR-1200 family (Mobile Continuity) | ✅ Yes |
| **§2 In Scope — AIMC-routed AI actions** | All AI interactions through AIMC | FR-500 family, FR-1501 (AIMC health check) | ✅ Yes |
| **§2 In Scope — AIMCC / KUC oversight** | Upload status surfacing; quota supervision | FR-600 family | ✅ Yes |
| **§2 In Scope — Audit / provenance** | Audit-aware management of app evolution | FR-1300 family | ✅ Yes |
| **§2 AMC/AIMC/AIMCC Boundary — AMC owns** | Executive visibility, approval/intervention surfaces, audit event generation, AMC operational state | FR-100 to FR-1200 families (executive surfaces), FR-1300 (audit), FR-1701 (state ownership) | ✅ Yes |
| **§2 AMC/AIMC/AIMCC Boundary — AMC does NOT** | Does not execute AI models directly; does not ingest knowledge; does not become canonical owner of knowledge/memory | FR-503 (AIMC non-bypass), FR-605 (AIMCC non-bypass), FR-703 (knowledge non-ownership), BR-SYS-001 | ✅ Yes |
| **§3 Executive Alerting Success Criteria** | Alerts generated proactively; critical alerts reach authority within SLA; acknowledgment and escalation recorded | FR-201 to FR-209 (Alert Management) | ✅ Yes |
| **§3 Approval/Intervention Success Criteria** | Every approval-required action blocked until explicit approval; approval decisions recorded with actor/timestamp/basis/outcome; interventions traceable | FR-301 to FR-307 (Approvals), FR-401 to FR-407 (Interventions) | ✅ Yes |
| **§3 AIMC Success Criteria** | Zero AI executions without AIMC routing; AIMC unavailability handled gracefully; all AIMC actions in audit trail | FR-503 (non-bypass), FR-1601 (AIMC degraded mode), FR-502 (result auditing) | ✅ Yes |
| **§3 AIMCC/KUC Success Criteria** | AMC surfaces upload status from AIMCC; no unmanaged ingestion pathway; AIMCC unavailability handled | FR-601 to FR-604, FR-1602 (AIMCC degraded mode) | ✅ Yes |
| **§3 Memory-Aware Success Criteria** | Knowledge/memory references surfaced with provenance; no silent caching of knowledge truth; retrieval degradation surfaced | FR-701 to FR-703, FR-1603 (knowledge degraded mode) | ✅ Yes |
| **§3 State/Audit/Provenance Success Criteria** | Every consequential action has traceable audit event; state ownership explicit; no orphaned audit events | FR-1301 to FR-1304 (Audit), FR-1701 (state ownership) | ✅ Yes |
| **§4 Strategic Context — why AMC exists** | Estate-level control plane; proactive awareness; support rapid governed intervention | FR-101 to FR-104, FR-103 (proactive), FR-1202 (mobile interrupt) | ✅ Yes |
| **§4 Strategic Evolution Path** | Progressive delegation from Johan → Maturion; explicit approval boundaries; audit traceability at each delegation step | §3 Authority Constraints (BR-AUTH-001 to BR-AUTH-004), FR-303/FR-304 delegation rules | ✅ Yes |
| **§4 Original AMC Capabilities — ARC Trigger Governance** | Absorbed into intervention launch and escalation routing | FR-401 to FR-407 (Interventions), FR-204 (Escalation) | ✅ Yes |
| **§4 Original AMC Capabilities — Dynamic Upload Quota Management** | Surfaced from AIMCC; quota supervision; approval pathway for changes | FR-603 (quota supervision), FR-604 (governance actions) | ✅ Yes |
| **§4 Original AMC Capabilities — Alert Dashboard** | Preserved and elevated as proactive executive alerting surface | FR-201 to FR-209, FR-101 (dashboard alert panel) | ✅ Yes |
| **§4 Original AMC Capabilities — Audit Trail** | Comprehensive audit trail covering all consequential pathways | FR-1300 family, FR-1301 (mandatory fields), FR-1302 (event coverage) | ✅ Yes |
| **§4 Original AMC Capabilities — Progressive Automation Control** | Progressive delegation with explicit approval boundaries, rollback capability, audit traceability | §3 Authority Constraints, FR-303/FR-304, BR-AUTH-002 | ✅ Yes |
| **§13 Constitutional Authority — Johan Ras** | Reserved matters require Johan Ras; no workflow silently converts reserved matter to routine operation | BR-AUTH-001, FR-307 (blocking rule), FR-303 (approval grant authority) | ✅ Yes |
| **§13 Maturion executive role** | Resident AI executive; proactive awareness; progressive delegation within approved domains | FR-103, FR-804, FR-803, §3 Actor Model | ✅ Yes |
| **§13 Foreman role** | Supervised orchestration; visible via execution reporting; no direct AMC login | FR-1103 (build/job status read-only), FR-403 (intervention dispatch via Foreman) | ✅ Yes |
| **§13 IAA independence** | IAA reports visible in reporting surfaces; assurance outputs separated from maintenance outputs | FR-1001 (separated display), FR-1002 (report detail) | ✅ Yes |
| **§13 Specialist-Agent layer** | Status surfaces, sandbox isolation indicator, outcomes not internal state | FR-901 to FR-904 (Specialist Agent Oversight) | ✅ Yes |
| **§13 Delegation Rule** | Progressive delegation permitted only with: defined domain, approval boundaries, audit traceability, revocation possibility | §3 Authority Constraints, BR-AUTH-002, FR-303 (approval basis required) | ✅ Yes |
| **§13 Authority Matrix** | Actor read/propose/approve/trigger/ingest/store/retrieve/act boundaries | §3 Actor Model & Authority Constraints; FR-1402 (authority-aware enforcement) | ✅ Yes |
| **§18 Core AI Integration** | All AI through AIMC; no direct provider coupling | FR-503 (AIMC non-bypass), FR-501 (AI action initiation), BR-SYS-001 | ✅ Yes |
| **§18 Executive AI Role — Maturion** | Conversational continuity; proactive surfacing; estate awareness | FR-801 to FR-807 (Executive Conversation), FR-103 | ✅ Yes |
| **§18 Proactive Communication Requirement** | Notify before being asked where justified; surface emerging issues early | FR-103 (proactive awareness), FR-804 (proactive messages) | ✅ Yes |
| **§18 Approval/Action Boundaries** | Governance-sensitive AI actions surface for correct authority; AI does not silently proceed | FR-307, FR-501 (approval requirement flag), FR-806 (response type discipline) | ✅ Yes |
| **§18 AI Traceability and Audit** | All AI-mediated actions traceable; which AI role, context, approval status, consequence | FR-1302 (AIMC actions in required audit coverage), FR-502 (result auditing) | ✅ Yes |
| **§18 Degraded Mode Requirements** | AIMC/AIMCC/knowledge system degraded modes defined | FR-1601 (AIMC), FR-1602 (AIMCC), FR-1603 (knowledge system) | ✅ Yes |
| **§23 Executive UX Principle** | Executive UX not developer-console UX; clarity of state and meaning | FR-101 (dashboard design requirements), FR-1202 (mobile alert interrupt), § requirements throughout |  ✅ Yes |
| **§23 Proactive Awareness Requirement** | AMC must surface matters before user asks | FR-103, FR-804, FR-1202 | ✅ Yes |
| **§23 Two-Way Conversational Interaction** | Persistent conversation with Maturion; executive inquiry, clarification, approval, escalation | FR-801 to FR-807 | ✅ Yes |
| **§23 Notification Classes** | Informational / warning / approval / operational intervention / emergency differentiation | FR-201 (priority ordering: Critical/High/Medium/Low/Informational) | ✅ Yes |
| **§23 Approval-Centred UX** | Explicit what/why/authority/consequence in approval views | FR-302 (Approval Detail View) | ✅ Yes |
| **§23 Mobile and Cross-Context Responsiveness** | Real executive action on mobile, not just visual mirroring | FR-1201 to FR-1204 | ✅ Yes |
| **§23 Dashboard and Drill-Down Pattern** | Overview + drill-down; not passive report gallery | FR-101 (dashboard), FR-102 (drill-down), FR-104 (navigation) | ✅ Yes |
| **§23 Escalation and Intervention Pattern** | Explicit escalation path; confirmation that action entered governed execution path | FR-204 (escalation), FR-403 (dispatch confirmation), FR-407 (cancel) | ✅ Yes |
| **§23 AI-Mediated UX Discipline** | Observation / recommendation / request / decision labels; no approval implied without explicit grant | FR-806 (response type discipline), FR-803 (response display) | ✅ Yes |
| **§23 Alert Class and Priority Framework** | Critical/High/Medium/Low class; auto-escalation; explicit acknowledgment; desktop/mobile consistency | FR-203 (acknowledgment), FR-205 (dismissal restriction), FR-208 (auto-escalation), FR-1202 (mobile interrupt), FR-1204 (cross-device consistency) | ✅ Yes |
| **§24 Shared State Architecture** | Coherent state across views, workflows, devices; state domains | FR-1701 (state domain ownership), FR-1702 (consistency), FR-1703 (session continuity), FR-805 (conversation persistence) | ✅ Yes |
| **§24 State Domains** | Executive context, conversation, alert/notification, escalation, approval, intervention, wellbeing, job/execution, agent status, cross-device | FR-1701 state domain ownership table covers all domains | ✅ Yes |
| **§26 Audit Log Design** | Structured audit trail; authority attribution; approval audit; AI-mediated action audit; cross-system integrity | FR-1301 to FR-1304 | ✅ Yes |
| **§26 Required Audit Event Coverage** | Full list of mandatory event types | FR-1302 (mirrors §26 required coverage list) | ✅ Yes |
| **§26 Audit Fields** | actor, source_system, approval_basis, timestamp, object, action, state_transition, outcome | FR-1301 (mandatory fields mirrors §26 field table) | ✅ Yes |

---

## 2. Stage 2 → FRS Traceability Matrix

This matrix maps the Stage 2 UX Workflow & Wiring Spec sections to the FRS requirement families that realize them.

| Stage 2 Section | Stage 2 Element | FRS Requirement(s) | Realized? |
|---|---|---|---|
| **§2 Cross-System Boundary Definitions** | AMC/AIMC/AIMCC/KUC/knowledge system ownership table | §2 Cross-System Boundary Rules; FR-503, FR-605, FR-703 | ✅ Yes |
| **§3 Actor Model** | Johan Ras, Maturion, Foreman, IAA, specialist, maintenance actor table | §3 Actor Model & Authority Constraints | ✅ Yes |
| **§4.1 Executive Estate Oversight** | Dashboard load, health tiles, alert panel, proactive panel, drill-down, navigation | FR-101 to FR-104 | ✅ Yes |
| **§4.2 Alert Review and Handling** | Alert Centre, priority ordering, detail, acknowledge, escalate, dismiss, link to approval/intervention, auto-escalation timer, history | FR-201 to FR-209 | ✅ Yes |
| **§4.3 Approval Workflow** | Approval Queue, detail (what/why/authority/consequence/evidence), approve, reject, defer, request clarification, blocking rule | FR-301 to FR-307 | ✅ Yes |
| **§4.4 Intervention Launch and Monitoring** | Initiate, catalogue/custom, authority level, approval gate, dispatch, real-time monitoring, cancel, completion, failure options | FR-401 to FR-407 | ✅ Yes |
| **§4.5 AI-Routed Actions (AIMC)** | AI action request, approval check, AIMC dispatch, result surfacing, AI Action Monitor, AIMC unavailability, non-bypass invariant, audit | FR-501 to FR-504, FR-1601 | ✅ Yes |
| **§4.6 AIMCC/KUC Supervision** | Upload list, detail, quota panel, governance action routing, AIMCC availability, non-bypass invariant | FR-601 to FR-605, FR-1602 | ✅ Yes |
| **§4.7 Memory-Aware / Knowledge-Aware View** | Retrieval request, provenance display, knowledge non-ownership rule, degraded indicator | FR-701 to FR-703, FR-1603 | ✅ Yes |
| **§4.8 Executive Conversation** | Conversation surface load, user message send, Maturion response with type indicator, proactive messages, session persistence, response type labels, acknowledgment | FR-801 to FR-807 | ✅ Yes |
| **§5.1 Specialist Agent Workspace Oversight** | Workspace list, sandbox isolation indicator, workspace detail, outcomes not internal state, escalate, terminate (approval-gated) | FR-901 to FR-904 | ✅ Yes |
| **§5.2 Maintenance & Assurance Reporting** | Reports list, severity coding, detail, critical finding → alert, create intervention, IAA independence preservation | FR-1001 to FR-1004 | ✅ Yes |
| **§5.3 Estate Configuration & Wellbeing** | Config state read-only, change request → approval, build/job status via Foreman (read-only), active stages | FR-1101 to FR-1103 | ✅ Yes |
| **§5.4 Mobile Continuity** | Responsive layout, mobile landing, critical alert interrupt, mobile approval path, session continuity across devices | FR-1201 to FR-1204 | ✅ Yes |
| **§6 Screen/Surface Model** | All surfaces identified and mapped | FR families cover all listed surfaces — Login (FR-1401), Executive Dashboard (FR-101), Alert Centre (FR-201), Approval Queue (FR-301), Intervention Manager (FR-401), AI Action Monitor (FR-504), AIMCC Supervision (FR-601), Knowledge Reference (FR-701), Conversation (FR-801), Specialist Agent Oversight (FR-901), Maintenance & Assurance (FR-1001), Estate Config (FR-1101), Mobile Alert View (FR-1202) | ✅ Yes |
| **§7.1 Executive Dashboard Wiring** | POST /api/aimc/request (proactive_summary), audit event AIMC_REQUEST | FR-103 (proactive awareness with AIMC routing and audit) | ✅ Yes |
| **§7.2 Alert Wiring** | ALERT_ACKNOWLEDGED, ALERT_ESCALATED, ALERT_DISMISSED, ALERT_ESCALATED_TIMEOUT, APPROVAL_CREATED_FROM_ALERT, INTERVENTION_CREATED_FROM_ALERT | FR-203, FR-204, FR-205, FR-208, FR-206, FR-207 | ✅ Yes |
| **§7.3 Approval Wiring** | APPROVAL_DECIDED (approved/rejected), APPROVAL_DEFERRED, CLARIFICATION_REQUESTED | FR-303, FR-304, FR-305, FR-306 | ✅ Yes |
| **§7.4 Intervention Wiring** | INTERVENTION_INITIATED, INTERVENTION_DISPATCHED, INTERVENTION_CANCELLED, INTERVENTION_COMPLETED, INTERVENTION_FAILED | FR-402, FR-403, FR-407, FR-405, FR-406 | ✅ Yes |
| **§7.5 AI-Routed Actions Wiring** | AIMC_ACTION_INITIATED, AIMC_ACTION_COMPLETED, AIMC_DEGRADED, AIMC_RECOVERED | FR-501, FR-502, FR-1601 | ✅ Yes |
| **§7.6 AIMCC/KUC Wiring** | AIMCC_GOVERNANCE_ACTION_CREATED, AIMCC_DEGRADED | FR-604, FR-1602 | ✅ Yes |
| **§7.7 Knowledge-Aware Wiring** | KNOWLEDGE_RETRIEVED, KNOWLEDGE_SYSTEM_DEGRADED | FR-701, FR-1603 | ✅ Yes |
| **§7.8 Executive Conversation Wiring** | CONVERSATION_MESSAGE_SENT, CONVERSATION_RESPONSE_RECEIVED, PROACTIVE_MESSAGE_RECEIVED, MESSAGE_ACKNOWLEDGED | FR-802, FR-803, FR-804, FR-807 | ✅ Yes |
| **§8.1 AMC ↔ AIMC** | Auth token per call; health check; no direct provider calls; no anonymous AIMC calls | FR-1501, FR-1504, FR-503 | ✅ Yes |
| **§8.2 AMC ↔ AIMCC/KUC** | Upload status read-only; governance action via approval; health check; KUC routing for uploads | FR-601, FR-604, FR-1502, FR-605 | ✅ Yes |
| **§8.3 AMC ↔ Knowledge/Memory System** | Knowledge retrieval with provenance; health check; provenance lookup | FR-701, FR-702, FR-1503 | ✅ Yes |
| **§8.4 AMC ↔ Foreman/Agents** | Intervention dispatch via Foreman API; execution status reporting callback; build/job status read-only; specialist agent outcome reporting | FR-403, FR-404, FR-1103, FR-902 | ✅ Yes |
| **§9.1 AIMC Unavailable** | Degraded banner; Maturion unavailable message; AI dispatch blocked; no direct model fallback; AIMC_DEGRADED audit | FR-1601 | ✅ Yes |
| **§9.2 AIMCC Unavailable** | AIMCC degraded banner; stale-data indicator; governance actions frozen; AIMCC_DEGRADED audit | FR-1602 | ✅ Yes |
| **§9.3 Knowledge/Memory System Degraded** | Stale/unavailable indicator on all knowledge items; explicit failure message on failed retrieval; no silent staleness | FR-1603 | ✅ Yes |

---

## 3. FRS Coverage Completeness Check

The following table confirms that all major AMC functional capability areas mandated by Stage 1 and Stage 2 are covered in the FRS, and that no significant commitment was silently dropped.

| Capability Area | Stage 1 Commitment | Stage 2 Journey/Surface | FRS Coverage | Status |
|---|---|---|---|---|
| Executive dashboard and estate overview | §1, §3, §23 | §4.1, §6 (Executive Dashboard) | FR-101 to FR-104 | ✅ Covered |
| Proactive alerting and awareness | §23 Alert Class Framework, §3 Executive Alerting | §4.1, §4.2 | FR-103, FR-201 to FR-208, FR-804 | ✅ Covered |
| Alert acknowledgment | §23 Acknowledgment | §4.2 | FR-203 | ✅ Covered |
| Alert escalation (manual and auto) | §23 Escalation | §4.2 | FR-204, FR-208 | ✅ Covered |
| Alert dismissal (Low/Informational only) | §23 Alert classes | §4.2 | FR-205 | ✅ Covered |
| Alert → approval / intervention linking | §23 | §4.2 | FR-206, FR-207 | ✅ Covered |
| Approval workflow (approve/reject/defer/clarify) | §13, §23 Approval-Centred UX, §3 | §4.3 | FR-301 to FR-307 | ✅ Covered |
| Approval blocking rule | §3, §23 | §4.3 | FR-307 | ✅ Covered |
| Intervention launch | §2, §23 Escalation/Intervention | §4.4 | FR-402 | ✅ Covered |
| Intervention monitoring and lifecycle | §3 Operating Success | §4.4 | FR-403 to FR-406 | ✅ Covered |
| Intervention cancellation | §2 | §4.4 | FR-407 | ✅ Covered |
| AIMC-routed AI actions | §18, §3 AIMC Success Criteria | §4.5 | FR-501 to FR-504 | ✅ Covered |
| AIMC non-bypass enforcement | §18 Prohibition, §2 Boundary | §4.5 Non-bypass invariant | FR-503, BR-SYS-001 | ✅ Covered |
| AIMCC/KUC supervision | §2 AIMCC/KUC Boundary, §3 | §4.6 | FR-601 to FR-604 | ✅ Covered |
| Upload quota supervision | §4 Dynamic Upload Quota | §4.6 | FR-603 | ✅ Covered |
| AIMCC non-bypass enforcement | §2 Prohibition | §4.6 Non-bypass invariant | FR-605, BR-SYS-001 | ✅ Covered |
| Knowledge/memory reference with provenance | §2 Knowledge/Memory, §3 Memory-Aware | §4.7 | FR-701 to FR-703 | ✅ Covered |
| Knowledge non-ownership rule | §2 AMC prohibitions | §4.7 Non-bypass invariant | FR-703, BR-STATE-001 | ✅ Covered |
| Executive conversation with Maturion | §23 Two-Way Conversational, §18 Executive AI | §4.8 | FR-801 to FR-807 | ✅ Covered |
| AI response type labeling | §23 AI-Mediated UX Discipline | §4.8 | FR-806 | ✅ Covered |
| Conversation persistence across devices | §23 Mobile Continuity | §4.8 | FR-805, FR-1204 | ✅ Covered |
| Specialist agent workspace oversight | §13 Specialist-Agent Layer, §18 | §5.1 | FR-901 to FR-904 | ✅ Covered |
| Sandbox isolation visibility | §18 Sandboxed AI Environments | §5.1 | FR-901, FR-902 | ✅ Covered |
| Maintenance & assurance reporting | §2 In Scope, §13 Maintenance/IAA layers | §5.2 | FR-1001 to FR-1004 | ✅ Covered |
| IAA independence preservation | §13 IAA | §5.2 | FR-1001 | ✅ Covered |
| Estate configuration & wellbeing | §2 In Scope, §5 Lifecycle | §5.3 | FR-1101 to FR-1103 | ✅ Covered |
| Build/job status visibility (read-only) | §5 Lifecycle Stages | §5.3 | FR-1103 | ✅ Covered |
| Mobile continuity | §23 Mobile and Cross-Context | §5.4 | FR-1201 to FR-1204 | ✅ Covered |
| Cross-device session continuity | §23 Desktop/Mobile Continuity | §5.4 | FR-1204, FR-805 | ✅ Covered |
| Audit trail (all event types) | §26 Audit Log Design | §7 throughout | FR-1301 to FR-1304 | ✅ Covered |
| Authentication & identity | §17, §25, §13 | §7.1 (auth wiring) | FR-1401 to FR-1403 | ✅ Covered |
| AIMC degraded mode | §18 Degraded Mode | §9.1 | FR-1601 | ✅ Covered |
| AIMCC degraded mode | §18 Degraded Mode | §9.2 | FR-1602 | ✅ Covered |
| Knowledge/memory degraded mode | §18 Degraded Mode | §9.3 | FR-1603 | ✅ Covered |
| Health check monitoring | §18, §3 Integration Success | §8.1, §8.2, §8.3 | FR-1501 to FR-1503 | ✅ Covered |
| Governed auth tokens for external calls | §25 API Authentication | §8.1 Non-bypass rule | FR-1504 | ✅ Covered |
| State domain ownership | §24 Shared State Architecture | §7 (Target Table columns) | FR-1701 | ✅ Covered |
| State consistency across surfaces | §24 Shared State | §7 throughout | FR-1702 | ✅ Covered |
| Progressive delegation model | §4 Strategic Evolution, §13 Delegation Rule | §3 Actor Model | §3 Authority Constraints, BR-AUTH-002 | ✅ Covered |
| ARC trigger governance | §4 Original AMC Capabilities | §4.4 (intervention flows) | FR-401 to FR-407 | ✅ Covered |

---

## 4. Cross-System Boundary Traceability

This section confirms that every cross-system boundary established in Stage 1 and Stage 2 is explicitly enforced in the FRS.

| Boundary | Stage 1 Source | Stage 2 Source | FRS Enforcement |
|---|---|---|---|
| AMC must not execute AI models directly | §1 Executive Layer Boundaries, §18 Prohibition | §2 Cross-System Boundaries, §4.5 Non-bypass invariant | FR-503, BR-SYS-001, BR-DEGRADE-001 |
| AMC must not ingest knowledge directly | §1 Executive Layer Boundaries, §2 AMC prohibitions | §2, §4.6 Non-bypass invariant | FR-605, BR-SYS-001, BR-DEGRADE-002 |
| AMC must not become canonical owner of knowledge/memory | §1, §2 Knowledge/memory system definition | §2, §4.7 Non-bypass invariant | FR-703, BR-STATE-001 |
| AMC must surface AIMC results with provenance | §18 AI Traceability | §4.5, §7.5 | FR-502, FR-806 |
| AMC must surface knowledge references with provenance | §3 Memory-Aware Operational Clarity | §4.7 | FR-701, FR-702 |
| AIMC unavailability must not lead to direct model fallback | §18 Degraded Mode Requirements | §9.1 | FR-1601, BR-DEGRADE-001 |
| AIMCC unavailability must not lead to direct ingestion bypass | §18 Degraded Mode Requirements | §9.2 | FR-1602, BR-DEGRADE-002 |
| AIMCC governs ingestion metadata; knowledge/memory system is canonical owner of persistent truth | §1 Executive Layer Boundaries (AIMCC definition), §13 Authority Matrix | §2 | FR-1701 (state domain ownership), BR-STATE-001 |
| Foreman is not a top-level executive authority; reads through AMC as reporting surface | §13 Foreman role, §13 Authority Matrix | §3 Actor Model | FR-1103 (build/job read-only), FR-403 (Foreman is executing agent for interventions, not authority) |

---

## 5. Dropped / Deferred Commitment Disclosure

This section explicitly records any Stage 1 or Stage 2 commitment that was **not** fully realized in the FRS, with documented justification. The goal is zero silent drops.

| Commitment | Source | FRS Status | Justification |
|---|---|---|---|
| **ARC Trigger Governance** (specific ARC mechanics) | §4 Original AMC Capabilities | FRS treats this as intervention launch (FR-401 to FR-407). ARC-specific trigger mechanics are architecture/TRS concerns, not FRS-level functional requirements | Deferred to TRS/Architecture — correctly scoped: FRS defines what (governed intervention pathway), not how (ARC integration specifics) |
| **Specific SLA values** (e.g., "critical alerts reach authority within defined SLA") | §3 Executive Alerting | FRS states SLA-enforcement requirement (FR-208 auto-escalation timeout) but does not define specific numeric SLA values | Numeric SLA values are TRS/Architecture concerns — FRS establishes the functional requirement that SLA enforcement exists; TRS defines the values |
| **Specific notification retry counts / expiry durations** | §23 Alert Class — Retry/Expiry | FRS states retry/expiry behavior is required (FR-208) but does not define specific counts or durations | TRS/Architecture will define numeric thresholds; FRS establishes the behavioral requirement |
| **Specific quota thresholds** | §4 Dynamic Upload Quota Management | FR-603 establishes quota supervision requirement; specific threshold values are AIMCC configuration concerns | TRS/Architecture will define; FRS establishes the functional obligation to surface and govern quota state |
| **Specific escalation timeout values** | §23 Alert Class — Escalation | FR-208 establishes auto-escalation requirement; timeout value is TRS/Architecture concern | As above — FRS establishes existence of requirement |
| **Specific MFA enforcement rules** | §17, §25 Auth | FR-1401 states MFA is supported if enabled; specific MFA enforcement policy is TRS/Architecture concern | TRS will define auth technical obligations |
| **Complete Edge Function Registry** | §19 Edge Function Registry | Not FRS scope — edge functions are architecture/implementation concern | Correctly scoped for Stage 5 Architecture |
| **Specific schema / table definitions** | §14–§16 Schema-to-Hook, Table Pathway, RLS | Not FRS scope — data schema is TRS/Architecture concern | Correctly scoped |

**Confirmation**: No Stage 1 or Stage 2 major functional capability commitment has been silently dropped from this FRS. All deferrals above are to appropriate downstream stages (TRS, Architecture) and are not omissions of functional obligations.

---

*End of Stage 1 + Stage 2 to FRS Traceability — Stage 3. Produced by foreman-v2-agent under POLC_ORCHESTRATION. CS2 approval required before TRS (Stage 4) derivation begins.*

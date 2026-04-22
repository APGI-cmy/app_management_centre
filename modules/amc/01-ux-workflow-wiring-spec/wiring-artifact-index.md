# Wiring Artifact Index — Stage 2

**Stage**: 2 — UX Workflow & Wiring Spec  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: ✅ Approval-Ready — Produced 2026-04-22  
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)  
**CS2 Authorization**: app_management_centre#1123  
**Upstream Source**: `modules/amc/00-app-description/app-description.md` v1.0 (approved 2026-04-22)  
**Canonical Location**: `modules/amc/01-ux-workflow-wiring-spec/wiring-artifact-index.md`

---

## Purpose

This index catalogs all wiring artifacts defined in Stage 2, mapping:
- UI surfaces to journeys
- Wiring table sections to their corresponding UI events and backend paths
- Cross-system integration surfaces to their governed layer boundaries
- Key tables / state objects referenced across all wiring

This index supports FRS (Stage 3) and Architecture (Stage 5) derivation by providing a structured catalog of all wiring relationships defined in Stage 2.

---

## Index 1 — Journeys and Their Wiring Sections

| Journey | Section in spec | Wiring Table Section |
|---|---|---|
| Executive Estate Oversight | §4.1 | §7.1 |
| Alert Review and Handling | §4.2 | §7.2 |
| Approval Workflow | §4.3 | §7.3 |
| Intervention Launch and Monitoring | §4.4 | §7.4 |
| AI-Routed Actions (AIMC) | §4.5 | §7.5 |
| AIMCC / KUC Supervision | §4.6 | §7.6 |
| Memory-Aware / Knowledge-Aware View | §4.7 | §7.7 |
| Executive Conversation with Maturion | §4.8 | §7.8 |
| Specialist Agent Workspace Oversight | §5.1 | Wired via §7.4 (Intervention) + §7.2 (Alert/Escalation) |
| Maintenance & Assurance Reporting | §5.2 | Wired via §7.2 (Alert creation from reports) |
| Estate Configuration & Wellbeing | §5.3 | Wired via §7.3 (Approval for config changes) |
| Mobile Continuity | §5.4 | Cross-cutting; applies to §7.1–§7.8 |

---

## Index 2 — Screen / Surface Catalog

| Surface | Section | Primary Journey(s) | Entry Point |
|---|---|---|---|
| Login | §6 | N/A (auth only) | Direct URL / app launch |
| Executive Dashboard | §6 | 4.1, 4.8 | Post-auth default |
| Alert Centre | §6 | 4.2 | Dashboard panel, sidebar nav |
| Alert Detail | §6 | 4.2 | From Alert Centre |
| Approval Queue | §6 | 4.3 | Dashboard badge, sidebar nav |
| Approval Detail | §6 | 4.3 | From Approval Queue |
| Intervention Manager | §6 | 4.4 | Dashboard, Alert Centre, sidebar nav |
| Intervention Detail | §6 | 4.4 | From Intervention Manager |
| AI Action Monitor | §6 | 4.5 | Dashboard, Conversation, sidebar nav |
| AIMCC / Knowledge Supervision | §6 | 4.6 | Dashboard, sidebar nav |
| Knowledge Reference | §6 | 4.7 | Conversation, contextual |
| Conversation | §6 | 4.8 | Dashboard persistent panel, sidebar nav |
| Specialist Agent Oversight | §6 | 5.1 | Dashboard, sidebar nav |
| Maintenance & Assurance Reports | §6 | 5.2 | Dashboard health tiles, sidebar nav |
| Estate Configuration & Wellbeing | §6 | 5.3 | Dashboard, sidebar nav |
| Mobile Alert View | §6 | 5.4 | Mobile app landing / push notification |

---

## Index 3 — Data Tables / State Objects Referenced

The following table lists all named data tables and state objects referenced in the Stage 2 wiring model. These are candidate schema objects for Stage 4 (TRS) and Stage 5 (Architecture). Exact schema is not defined at Stage 2 — these are wiring-layer names only.

| Object Name | Referenced In | Wiring Function | Owning Layer |
|---|---|---|---|
| `alerts` | §7.1, §7.2, §7.8 | Store all estate alerts with priority, class, status, audit fields | AMC |
| `escalations` | §7.2 | Track alert and intervention escalation events | AMC |
| `approvals` | §7.2, §7.3, §7.4, §7.6 | Track all pending and decided governance-sensitive approval items | AMC |
| `interventions` | §7.3, §7.4 | Track all interventions from initiation through completion | AMC |
| `execution_records` | §7.4 | Execution trace for interventions (steps, agent, status) | AMC |
| `aimc_action_log` | §7.5 | Record all AI action dispatches and AIMC responses | AMC |
| `knowledge_upload_records` | §7.6 | Track knowledge upload items with KUC/AIMCC status | AMC (sourced from AIMCC) |
| `knowledge_retrieval_log` | §7.7 | Log all knowledge retrieval requests with provenance | AMC |
| `conversation_messages` | §7.8 | Persistent two-way conversation thread between Johan and Maturion | AMC |
| `system_health_events` | §7.5, §7.6, §7.7 | Track AIMC/AIMCC/knowledge system health and degraded events | AMC |
| `estate_health_scores` | §7.1 | Aggregated health domain scores for executive dashboard | AMC |
| `health_events` | §7.1 | Health domain event records for drill-down | AMC |

> **Note**: `knowledge_upload_records` content is sourced from AIMCC. AMC holds a read-only projection of AIMCC-governed upload state. AIMCC remains the owning layer for upload workflow truth. AMC does not become the canonical owner.

---

## Index 4 — External Service Integration Points

| External Service | Referenced In | Integration Type | Governed Pathway |
|---|---|---|---|
| **AIMC** | §7.1, §7.5, §7.8, §8.1 | AI action dispatch, Maturion conversation, AIMC health | AMC → AIMC API (governed endpoint); no direct model provider calls |
| **AIMCC** | §7.6, §7.7, §8.2 | Upload status fetch, governance action routing, knowledge retrieval | AMC → AIMCC API (governed endpoint); AMC read-only for upload status |
| **Knowledge Upload Centre (KUC)** | §7.6, §8.2 | Knowledge upload submission routing | AMC → KUC API; KUC routes to AIMCC |
| **Knowledge / Memory System** | §7.7, §8.3 | Knowledge retrieval with provenance | AMC → Knowledge/Memory governed API |
| **Foreman** | §7.4, §8.4 | Intervention dispatch, execution status reporting | AMC → Foreman API; Foreman → AMC callback |
| **Specialist Agents** | §5.1, §8.4 | Outcome reporting, status surfacing | Specialist → AMC endpoint (governed callback only) |
| **Supabase Auth** | §6 (Login) | JWT-based authentication | Supabase Auth SDK / Supabase Auth API |

---

## Index 5 — Audit Event Types Referenced

All materially significant wiring events in Stage 2 generate audit events. The following is a catalog of all named audit events referenced in the Stage 2 wiring model. Exact audit log schema is defined at Stage 4 (TRS) / Stage 5 (Architecture), tracing to §26 Audit Log Design in the Stage 1 App Description.

| Audit Event Type | Source Section | Trigger |
|---|---|---|
| `AIMC_REQUEST` | §7.1, §7.5 | Maturion proactive summary or AI action dispatched to AIMC |
| `ALERT_ACKNOWLEDGED` | §7.2 | User explicitly acknowledges an alert |
| `ALERT_ESCALATED` | §7.2 | User escalates alert to escalation flow |
| `ALERT_DISMISSED` | §7.2 | User dismisses low/informational alert |
| `ALERT_ESCALATED_TIMEOUT` | §7.2 | Critical alert auto-escalates after timeout |
| `APPROVAL_CREATED_FROM_ALERT` | §7.2 | Approval item created from alert context |
| `INTERVENTION_CREATED_FROM_ALERT` | §7.2 | Intervention created from alert context |
| `APPROVAL_DECIDED` | §7.3 | User approves or rejects an approval item |
| `APPROVAL_DEFERRED` | §7.3 | User defers an approval with note |
| `CLARIFICATION_REQUESTED` | §7.3 | User requests clarification from Maturion on an approval |
| `INTERVENTION_INITIATED` | §7.4 | User initiates a new intervention |
| `INTERVENTION_DISPATCHED` | §7.4 | Intervention dispatched to execution by Foreman/agent |
| `INTERVENTION_CANCELLED` | §7.4 | User cancels an active intervention |
| `INTERVENTION_COMPLETED` | §7.4 | Executing agent signals completion |
| `INTERVENTION_FAILED` | §7.4 | Executing agent signals failure |
| `AIMC_ACTION_INITIATED` | §7.5 | AI action request dispatched to AIMC |
| `AIMC_ACTION_COMPLETED` | §7.5 | AIMC returns result for an action |
| `AIMC_DEGRADED` | §7.5 | AIMC unavailability detected |
| `AIMC_RECOVERED` | §7.5 | AIMC recovery detected |
| `AIMCC_GOVERNANCE_ACTION_CREATED` | §7.6 | AIMCC governance action creates approval item |
| `AIMCC_DEGRADED` | §7.6 | AIMCC unavailability detected |
| `KNOWLEDGE_RETRIEVED` | §7.7 | Knowledge retrieval request completed |
| `KNOWLEDGE_DEGRADED` | §7.7 | Knowledge/memory system degraded detected |
| `CONVERSATION_MESSAGE_SENT` | §7.8 | User sends a conversation message |
| `CONVERSATION_RESPONSE_RECEIVED` | §7.8 | Maturion response received from AIMC |
| `PROACTIVE_MESSAGE_RECEIVED` | §7.8 | Maturion-initiated proactive message arrives |
| `MESSAGE_ACKNOWLEDGED` | §7.8 | User acknowledges a conversation message |

---

## Index 6 — Cross-System Boundary Rules (Non-Bypass Invariants)

These invariants are non-negotiable and must be preserved in FRS, TRS, Architecture, and Build. Any artifact that contradicts these is a Stage 2 traceability defect.

| Invariant | Source | Rule |
|---|---|---|
| No direct AI model calls | §2, §4.5, §8.1 | All AI execution from AMC must route through AIMC. AMC must not call model providers directly under any circumstances. |
| No direct knowledge ingestion | §2, §4.6, §8.2 | All knowledge upload and ingestion from AMC context must route through KUC and AIMCC. AMC must not bypass these layers. |
| No canonical knowledge ownership | §2, §4.7, §8.3 | AMC must not become the canonical long-term store of knowledge/memory truth. All persistent knowledge is owned by the knowledge/memory system. |
| No anonymous AI actions | §4.5, §7.5 | Every AI action dispatched to AIMC must be associated with an actor and recorded in the audit trail. |
| No silent degraded mode | §9.1, §9.2, §9.3 | When AIMC, AIMCC, or the knowledge/memory system is unavailable, AMC must surface explicit degraded-mode indicators. Silent suppression is prohibited. |
| No reserved-matter self-approval | §4.3, §7.3 | AMC must not approve its own governance actions. Approvals route to Johan (reserved matters) or Maturion (delegated domains). |
| No silent audit suppression | §7 (all wiring tables) | Every consequential action must generate a named audit event with actor, timestamp, and outcome. |

---

## Index 7 — Degraded-Mode Coverage

| Dependency | Degraded Mode Section | UX Impact | Recovery |
|---|---|---|---|
| AIMC unavailable | §9.1 | AI features enter defined degraded mode; explicit banner shown; no fallback to direct model calls | AIMC_RECOVERED event → normal mode |
| AIMCC unavailable | §9.2 | Upload/ingestion features enter degraded mode; stale indicators shown | AIMCC recovery detected → normal mode |
| Knowledge/Memory system degraded | §9.3 | All knowledge surfaces show stale/unavailable indicator; no silent serving of stale data | System recovery detected → normal mode |

---

## Index 8 — Stage 1 Source References (Summary)

| Stage 1 Section | Subject | Referenced in Stage 2 |
|---|---|---|
| §1 Executive Layer Boundary Definitions | Cross-system ownership boundaries | §2, §8 |
| §1 Core Value Proposition | AMC's executive purpose | §4.1 |
| §2 AMC/AIMC/AIMCC Boundary | Layer-level prohibitions | §2, §4.5, §4.6 |
| §3 Operating Success Measures | Executive alerting, approval, AI, AIMCC | §4.1–§4.6, §7 |
| §5 Stage 2 — UX Workflow & Wiring Spec | Lifecycle mandate for Stage 2 | All sections |
| §13 Agent Authority Chain | Authority matrix for all actors | §3, §4.3, §4.4 |
| §13 Authority Matrix | Actor-level action authority | §3 |
| §18 AI Integration Requirements | AIMC routing requirements | §4.5, §7.5, §8.1 |
| §18 Multi-Layer AI Integration Model | AI layer definitions | §2, §4.5, §8.1 |
| §18 Degraded Mode Requirements | Degraded behavior | §9.1 |
| §23 Notification Classes | Alert classification | §4.2 |
| §23 Alert Class and Priority Framework | Alert priorities and escalation | §4.2, §7.2 |
| §23 Two-Way Conversational Interaction | Conversation model | §4.8, §7.8 |
| §23 Approval-Centred UX | Approval surface requirements | §4.3, §7.3 |
| §23 Mobile and Cross-Context Responsiveness | Mobile operating requirements | §5.4 |
| §23 Dashboard and Drill-Down Pattern | Dashboard model | §4.1, §6 |
| §23 Escalation and Intervention Pattern | Intervention flow | §4.4, §7.4 |
| §23 AI-Mediated UX Discipline | AI UX rules | §4.8, §7.8 |
| §24 Shared State Architecture | State ownership model | §4.7 |
| §26 Audit Log Design | Audit event requirements | §7 (all wiring tables), Index 5 |

---

*End of Wiring Artifact Index — Stage 2. Produced by foreman-v2-agent under POLC_ORCHESTRATION. CS2 approval required before FRS (Stage 3) derivation begins.*

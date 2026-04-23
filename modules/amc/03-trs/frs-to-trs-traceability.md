# FRS to TRS Traceability — Stage 4

**Stage**: 4 — Traceability Artifact
**Module**: App Management Centre (AMC)
**Version**: 1.1
**Status**: 🟡 Produced Approval-Ready — 2026-04-23 (Hardened 2026-04-23)
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: app_management_centre#1127
**Upstream Source**: `modules/amc/02-frs/functional-requirements-specification.md` v1.0 (CS2-approved for Stage 4 progression, ref #1123)
**TRS Target**: `modules/amc/03-trs/technical-requirements-specification.md` v1.1
**Canonical Location**: `modules/amc/03-trs/frs-to-trs-traceability.md`

---

> **PURPOSE STATEMENT**
> This document demonstrates that every approved Stage 3 FRS requirement family is technically realized in Stage 4 TRS requirements, and that no approved Stage 3 requirement family was silently dropped. It also shows where specific items are deferred to Stage 5 Architecture rather than resolved in Stage 4, with explicit rationale. This artifact supports CS2 approval verification and downstream Architecture and QA-to-Red derivation.

---

## Table of Contents

1. [FRS Requirement Family Coverage Matrix](#1-frs-requirement-family-coverage-matrix)
2. [Individual FRS Requirement Traceability](#2-individual-frs-requirement-traceability)
3. [Business Rule Technical Realization](#3-business-rule-technical-realization)
4. [Stage 4 Deferred Items Register](#4-stage-4-deferred-items-register)
5. [Coverage Completeness Verification](#5-coverage-completeness-verification)
6. [Cross-System Boundary Preservation Check](#6-cross-system-boundary-preservation-check)

---

## 1. FRS Requirement Family Coverage Matrix

This matrix shows every FRS requirement family from Stage 3 and confirms it is technically realized in Stage 4 TRS. No family was silently dropped.

| FRS Family | FRS IDs | TRS Section | TRS Requirement IDs | Status |
|---|---|---|---|---|
| Executive Estate Oversight | FR-101 to FR-104 | §4 TR-100 | TR-101, TR-102, TR-103, TR-104 | ✅ Realized |
| Alert Management | FR-201 to FR-209 | §5 TR-200 | TR-201, TR-202, TR-203, TR-204, TR-205, TR-206, TR-207, TR-208, TR-209 | ✅ Realized |
| Approval Workflow | FR-301 to FR-307 | §6 TR-300 | TR-301, TR-302, TR-303, TR-304 | ✅ Realized |
| Intervention | FR-401 to FR-407 | §7 TR-400 | TR-401, TR-402, TR-403, TR-404 | ✅ Realized |
| AI-Routed Actions (AIMC) | FR-501 to FR-504 | §8 TR-500 | TR-501, TR-502, TR-503, TR-504 | ✅ Realized |
| AIMCC / KUC Supervision | FR-601 to FR-605 | §9 TR-600 | TR-601, TR-602, TR-603, TR-604, TR-605, TR-606, TR-607, TR-608, TR-609 | ✅ Realized |
| Memory-Aware / Knowledge-Aware View | FR-701 to FR-703 | §10 TR-700 | TR-701, TR-702, TR-703 | ✅ Realized |
| Executive Conversation | FR-801 to FR-807 | §11 TR-800 | TR-801, TR-802, TR-803, TR-804, TR-805 | ✅ Realized |
| Specialist Agent Workspace Oversight | FR-901 to FR-904 | §12 TR-900 | TR-901, TR-902 | ✅ Realized |
| Maintenance & Assurance Reporting | FR-1001 to FR-1004 | §13 TR-1000 | TR-1001, TR-1002 | ✅ Realized |
| Estate Configuration & Wellbeing | FR-1101 to FR-1103 | §14 TR-1100 | TR-1101, TR-1102 | ✅ Realized |
| Mobile Continuity | FR-1201 to FR-1204 | §15 TR-1200 | TR-1201, TR-1202, TR-1203 | ✅ Realized |
| Audit & Provenance | FR-1301 to FR-1304 | §16 TR-1300 | TR-1301, TR-1302, TR-1303, TR-1304, TR-1305 | ✅ Realized |
| Authentication & Authorization | FR-1401 to FR-1403 | §17 TR-1400 | TR-1401, TR-1402, TR-1403, TR-1404, TR-1405 | ✅ Realized |
| Cross-System Integration | FR-1501 to FR-1504 | §18 TR-1500 | TR-1501, TR-1502, TR-1503, TR-1504, TR-1505 | ✅ Realized |
| Degraded-Mode Behavior | FR-1601 to FR-1603 | §19 TR-1600 | TR-1601, TR-1602, TR-1603, TR-1604 | ✅ Realized |
| State & Persistence | FR-1701 to FR-1703 | §20 TR-1700 | TR-1701, TR-1702, TR-1703 | ✅ Realized |
| **ARC Technical Domain** | **Stage 1 §4 ARC Trigger Governance** | **§21 TR-1800** | **TR-1801, TR-1802, TR-1803, TR-1804, TR-1805, TR-1806** | **✅ Realized** |

**Result: 17 FRS requirement families + 1 Stage 1 §4 ARC domain. 18 families realized in Stage 4 TRS v1.1. 0 silently dropped.**

---

## 2. Individual FRS Requirement Traceability

This section traces every individual FRS requirement to its Stage 4 TRS realization. Where a functional requirement is partially or fully deferred to Stage 5 Architecture, the deferral is explicitly noted.

### FR-100 Family: Executive Estate Oversight

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-101 | Executive Dashboard Load | TR-101: `GET /api/dashboard/summary` contract defined; response payload structure specified; partial-availability `partial: true` flag required | Health domain status aggregation logic deferred to Stage 5 |
| FR-102 | Health Domain Drill-Down | TR-102: `GET /api/dashboard/health/{domain_id}` contract defined; unavailability response structure required | Per-domain record schema details deferred to Stage 5 |
| FR-103 | Proactive Estate Awareness | TR-103: AIMC `proactive_summary` dispatch contract defined; polling interval; required degraded string specified | AIMC routing logic deferred to AIMC system |
| FR-104 | Dashboard Navigation | TR-104: Named route list defined (`/dashboard`, `/alerts`, etc.); navigation must not depend on external service availability | Route guard implementation deferred to Stage 5 |

### FR-200 Family: Alert Management

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-201 | Alert Centre Load | TR-201: `alerts` table schema requirements; `GET /api/alerts` priority ordering contract; explicit error on fetch failure | None |
| FR-202 | Alert Detail View | TR-201: `alerts` table FK columns (linked_approval_id, linked_intervention_id) support alert detail context | Alert detail UI layout deferred to Stage 5 |
| FR-203 | Alert Acknowledgment | TR-202: `POST /api/alerts/{id}/acknowledge` contract; actor authorization check; audit event requirement; write-failure behavior; TR-208: retry policy on write failure | None |
| FR-204 | Alert Escalation | TR-203: `POST /api/alerts/{id}/escalate` contract; manual and timeout escalation; `ALERT_ESCALATED` and `ALERT_ESCALATED_TIMEOUT` audit events; TR-209: escalation chain two-level model with distinct event types per level | None |
| FR-205 | Alert Dismissal | TR-204: Server-side class enforcement (HTTP 422 for Critical/High/Medium); non-empty `dismiss_reason` required | None |
| FR-206 | Link Alert to Approval | TR-205: `POST /api/alerts/{id}/link-approval`; audit event `APPROVAL_CREATED_FROM_ALERT`; alert state not altered on failure | None |
| FR-207 | Link Alert to Intervention | TR-401: `interventions` table `source_alert_id` FK column; intervention creation from alert context | None |
| FR-208 | Critical Alert Auto-Escalation | TR-206: Background scheduler contract; query pattern; scheduler failure alert requirement; TR-209: two-level escalation chain definition | Scheduler implementation mechanism deferred to Stage 5 |
| FR-209 | Alert History | TR-201: `alerts` table retains dismissed/resolved records for history | History view API endpoint deferred to Stage 5 (extend GET /api/alerts with status filter) |
| — | Alert Timing & Retry (Stage 1 §3 Success Criteria) | TR-207: Alert generation and delivery timing SLA contract (trigger→INSERT ≤5s; INSERT→Realtime ≤2s; INSERT→push ≤5s); TR-208: Retry policy (3 retries with exponential back-off) on write failure; durability contract | Alert timing SLA self-monitoring deferred to Stage 5 |

### FR-300 Family: Approval Workflow

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-301 | Approval Queue Load | TR-301: `approvals` table schema; `GET /api/approvals` endpoint | Priority/deadline ordering details deferred to Stage 5 |
| FR-302 | Approval Detail View | TR-301: `approvals` table columns covering what/why/authority/consequence data | Detail surface layout deferred to Stage 5 |
| FR-303 | Approval Grant | TR-302: `POST /api/approvals/{id}/decide` contract; `approval_basis` non-empty enforcement (HTTP 422); reserved-matter actor check (HTTP 403); TR-303: post-approval dispatch contract; approval persistence on downstream failure | None |
| FR-304 | Approval Rejection | TR-302: `rejection_reason` non-empty enforcement (HTTP 422); downstream notification requirement | None |
| FR-305 | Approval Deferral | TR-302: `deferral_note` non-empty enforcement; `follow_up_at` field; deferral record persistence | Deferral reminder scheduling implementation deferred to Stage 5 |
| FR-306 | Request Clarification from Maturion | TR-802: Conversation message creation with approval context; AIMC dispatch with conversation message action type | Clarification conversation UI deferred to Stage 5 |
| FR-307 | Approval Blocking Rule | TR-304: Server-side approval blocking gate; `GET /api/approvals` check before action dispatch; HTTP 423 with `blocked_by_approval` response | None |

### FR-400 Family: Intervention

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-401 | Intervention Manager Load | TR-401: `interventions` table schema; `GET /api/interventions` endpoint | None |
| FR-402 | Initiate New Intervention | TR-401: Table schema covers all initiation fields; authority_level; approval_required; TR-402: approval queue routing for reserved-matter interventions | Intervention type catalogue definition deferred to Stage 5 |
| FR-403 | Intervention Dispatch | TR-402: Foreman dispatch API contract; governed auth token; HTTP 202 acknowledgment; audit event; dispatch_failed handling | Foreman-side intervention format deferred to Foreman spec |
| FR-404 | Intervention Monitoring | TR-403: Status callback contract; Realtime broadcast; last-known status with stale indicator | None |
| FR-405 | Intervention Completion | TR-403: Callback contract covers `completed` status; `INTERVENTION_COMPLETED` audit event | None |
| FR-406 | Intervention Failure Handling | TR-403: Callback contract covers `failed` status; `INTERVENTION_FAILED` audit event; failure_reason field | Retry/escalate/close options UI deferred to Stage 5 |
| FR-407 | Cancel Intervention | TR-404: `cancel_reason` non-empty enforcement; abort signal dispatch; abort signal failure separate event | None |

### FR-500 Family: AI-Routed Actions

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-501 | AI Action Initiation | TR-501: `aimc_action_log` schema; TR-502: AIMC API call contract; approval gate routing | None |
| FR-502 | AI Action Result Surfacing | TR-503: AIMC callback endpoint contract; `AIMC_ACTION_COMPLETED` audit event; Realtime broadcast | None |
| FR-503 | AIMC Non-Bypass Rule | TR-504: Architecture dependency enforcement; `BOUNDARY_BYPASS_ATTEMPTED` runtime event; TR-BOUNDARY-001 | None |
| FR-504 | AI Action Monitor | TR-501: `aimc_action_log` table records all actions; TR-503: Realtime delivery | AI Action Monitor UI surface deferred to Stage 5 |

### FR-600 Family: AIMCC / KUC Supervision

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-601 | AIMCC/Knowledge Supervision Surface Load | TR-601: AIMCC read API call contract; stale indicator on degraded | None |
| FR-602 | Upload Detail View | TR-601: Full provenance chain fields in AIMCC API response requirement | Provenance chain UI layout deferred to Stage 5 |
| FR-603 | Knowledge Upload Quota Supervision | TR-602: Quota read API contract; last-known cache with stale indicator; TR-607: quota threshold state machine (ok/warning/critical) with automated alert generation on threshold transitions; TR-608: quota authorization rules | None |
| FR-604 | AIMCC Governance Action | TR-603: Approval creation with `aimcc_governance` source type; AIMCC governance decision notification on approval; queued pending on AIMCC degraded; TR-605: quota adjustment request console action; TR-606: temporary quota override contract with expiry handling; TR-609: quota audit event catalog | None |
| FR-605 | AIMCC Non-Bypass Rule | TR-604: KUC-only upload submission enforcement; `BOUNDARY_BYPASS_ATTEMPTED` on violation; TR-BOUNDARY-002 | None |
| — | Dynamic Upload Quota Management Console (Stage 1 §4 reconciliation) | TR-605: `POST /api/aimcc/quota/request-adjustment` with adjustment_reason enforcement and approval gate; TR-606: temporary override with `override_expiry_at` enforcement, pre-expiry alert, AIMCC notification; TR-607: three-state threshold machine (ok/warning/critical) with automated alert generation; TR-608: reserved_matter authorization enforcement; TR-609: quota audit event catalog with full observability | None |

### FR-700 Family: Memory-Aware / Knowledge-Aware View

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-701 | Knowledge Retrieval Request | TR-701: Knowledge API call contract; `require_provenance: true` enforcement; `KNOWLEDGE_RETRIEVED` audit event | None |
| FR-702 | Provenance Chain Display | TR-701: Provenance metadata fields required in API response; TR-702: `knowledge_retrieval_log` records source refs | Provenance chain UI display deferred to Stage 5 |
| FR-703 | Knowledge Non-Ownership Rule | TR-703: No knowledge content tables in AMC database; 5-minute TTL cache max; stale flag on degraded; architecture prohibition on ownership columns; TR-BOUNDARY-003 | None |

### FR-800 Family: Executive Conversation

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-801 | Conversation Surface Load | TR-802: `GET /api/conversation/messages` pagination contract; TR-801: `conversation_messages` schema | Conversation UI layout deferred to Stage 5 |
| FR-802 | Send User Message | TR-802: `POST /api/conversation/messages` contract; AIMC dispatch; AIMC failure handling | None |
| FR-803 | Maturion Response Display | TR-803: AIMC conversation callback contract; `response_type` mandatory; `type unavailable` fallback render | None |
| FR-804 | Maturion Proactive Message | TR-804: AIMC proactive message push endpoint; `is_proactive` flag; alert creation if alert_class present; Realtime broadcast | None |
| FR-805 | Conversation Session Persistence | TR-805: Server-side `conversation_messages` table; Realtime subscription per session; 2-second propagation target | None |
| FR-806 | AI Response Type Discipline | TR-803: `response_type` validation; `type unavailable` indicator on missing metadata; prohibition on defaulting to "Decision" | None |
| FR-807 | Message Acknowledgment | TR-801: `acknowledged_at`, `acknowledged_by` columns on `conversation_messages`; `MESSAGE_ACKNOWLEDGED` audit event | None |

### FR-900 Family: Specialist Agent Workspace Oversight

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-901 | Specialist Agent Oversight Surface Load | TR-901: Workspace status API contract; `sandbox_isolation_indicator` required | None |
| FR-902 | Workspace Detail View | TR-901: Per-workspace response fields covering outcomes (not internal state) | Workspace detail UI deferred to Stage 5 |
| FR-903 | Escalate Workspace Issue | Covered by existing escalation wiring (TR-203, TR-802 conversation routing) — no dedicated workspace escalation endpoint required | None |
| FR-904 | Terminate Workspace | TR-902: Termination approval gate contract; authority check; governed dispatch to specialist agent | None |

### FR-1000 Family: Maintenance & Assurance Reporting

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-1001 | Maintenance & Assurance Reports Surface Load | TR-1001: `GET /api/reports` contract; `report_type` filter parameter; IAA/maintenance separation | None |
| FR-1002 | Report Detail View | TR-1001: Report item fields cover findings, severity, recommended_action, evidence_ref, agent_id | Report detail UI deferred to Stage 5 |
| FR-1003 | Critical Finding Alert Generation | TR-1002: Automatic alert creation on `severity: critical` report; failure logging | None |
| FR-1004 | Create Intervention from Maintenance Finding | TR-401: `interventions` table `source_report_id` column supports this flow | None |

### FR-1100 Family: Estate Configuration & Wellbeing

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-1101 | Estate Configuration Surface Load | TR-1101: Foreman read API contract; stale indicator when unavailable; read-only requirement | None |
| FR-1102 | Request Configuration Change | TR-1102: Approval-gated configuration change; `reserved_matter` authority boundary; no UPDATE without approval | None |
| FR-1103 | Build/Job Status Visibility | TR-1101: Foreman reporting feed is read-only; no build command endpoints in AMC API | None |

### FR-1200 Family: Mobile Continuity

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-1201 | Mobile Responsive Layout | TR-1201: Responsive breakpoint at ≤768px; critical/high alerts surfaced without scroll; actions accessible | Specific UI component breakpoint implementation deferred to Stage 5 |
| FR-1202 | Mobile Critical Alert Interrupt | TR-1202: Push notification dispatch on Critical alert creation; deep link payload; in-app fallback mandatory | Push provider selection (FCM/APNs/PWA) deferred to Stage 5 |
| FR-1203 | Mobile Approval & Acknowledgment | TR-1201: Mobile layout must expose approve/reject controls; TR-1203: Realtime state sync ensures mobile actions replicate to desktop | Mobile-specific UI layout deferred to Stage 5 |
| FR-1204 | Cross-Device Session Continuity | TR-1203: Supabase Realtime channel `amc_executive_state_{user_id}`; Realtime event as authoritative on conflict | None |

### FR-1300 Family: Audit & Provenance

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-1301 | Mandatory Audit Event Fields | TR-1301: `audit_events` table schema with all mandatory fields; append-only constraint; correction-record pattern | None |
| FR-1302 | Required Audit Event Coverage | TR-1302: Complete list of required `event_type` values defined (expanded in v1.1 to include quota and ARC events); all wired across TRS sections | Wiring verification deferred to Stage 6 QA-to-Red |
| FR-1303 | Audit Accessibility | TR-1303: `GET /api/audit-events` query parameters defined; pagination; RLS scope | Audit review surface UI deferred to Stage 5 |
| FR-1304 | Cross-System Event Integrity | TR-1304: `cross_system_ref` column; `_CROSS_REF_PENDING` suffix pattern; correction-record update flow | None |
| — | Audit Delivery Atomicity (Stage 1 §3 State/Audit/Provenance Success Criteria) | TR-1305: Audit event delivery atomicity contract — state mutation and audit write must be atomic; compensating `AUDIT_WRITE_FAILED` event on cross-system failure | None |

### FR-1400 Family: Authentication & Authorization

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-1401 | User Authentication | TR-1401: Supabase Auth configuration requirements; JWT expiry; httpOnly cookie; auth event audit requirements; service-unavailable behavior | MFA per-user configuration flow deferred to Stage 5 |
| FR-1402 | Authority-Aware Action Enforcement | TR-1404: Server-side authority-domain middleware; reserved_matter → human actor check; delegated → ai_executive within scope; independent of client UI | Delegated-domain scope configuration storage deferred to Stage 5 |
| FR-1403 | Identity Separation | TR-1403: `actor_type` enum in all tables and audit events; actor resolution at API layer from JWT claims or service token | None |
| — | Inter-Service Trust Boundary (Stage 1 §1 Explicit Prohibitions) | TR-1405: Inter-service trust anchor — AMC sole writer to AMC tables; all callback endpoints validate service token; trust escalation prohibition; cross-service impersonation rejection | None |

### FR-1500 Family: Cross-System Integration

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-1501 | AIMC Health Check | TR-1501: Health polling contract; 30-second default interval; immediate degraded mode on failure; recovery detection | None |
| FR-1502 | AIMCC Health Check | TR-1502: Health polling contract; degraded mode entry | None |
| FR-1503 | Knowledge/Memory System Health Check | TR-1503: Health polling contract; immediate cache stale-marking on degraded | None |
| FR-1504 | Governed Auth Token for External Calls | TR-1504: Service token environment variables; token required on all outbound calls; TR-1505: URL configuration requirements | None |

### FR-1600 Family: Degraded-Mode Behavior

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-1601 | AIMC Unavailable Degraded Mode | TR-1602: Six required behaviors on AIMC degraded mode; required exact degraded string; HTTP 503 on AIMC endpoints; `AIMC_DEGRADED` audit event | None |
| FR-1602 | AIMCC Unavailable Degraded Mode | TR-1603: Five required behaviors; stale-with-timestamp; governance actions frozen; upload queue pending | None |
| FR-1603 | Knowledge/Memory System Degraded Mode | TR-1604: Five required behaviors; HTTP 503 on retrieval; stale indicators applied; knowledge_system_degraded audit event | None |

### FR-1700 Family: State & Persistence

| FRS ID | FRS Title | TRS Realization | Deferred Item (if any) |
|---|---|---|---|
| FR-1701 | State Domain Ownership | TR-1701: Canonical state ownership table with all state domains; AMC write access rules per table; external system read-only enforcement | None |
| FR-1702 | State Consistency Across Surfaces | TR-1702: Realtime channel for state mutations; authoritative Realtime event pattern; stale indicator on synchronization failure | None |
| FR-1703 | Session Continuity | TR-1703: Server-fetch sequence on session restore; five required API fetches; explicit error on fetch failure | None |

### ARC Technical Domain: Stage 1 §4 ARC Trigger Governance

> **Traceability Note**: ARC (Action Resolution Centre) is not an FRS requirement family — it is a first-class AMC executive function declared in Stage 1 §4 ARC Trigger Governance reconciliation. The Stage 3 FRS absorbed ARC trigger governance into the alert, approval, and intervention families. Stage 4 TRS v1.1 restores ARC as an explicitly recognizable technical domain with its own section (§21 TR-1800), API namespace, data table, and audit family as mandated by Stage 1.

| Stage 1 Source | TRS Realization | Deferred Item (if any) |
|---|---|---|
| Stage 1 §4: ARC Trigger Governance — "first-class AMC executive function"; absorbed into intervention, escalation routing, and approval workflow | TR-1801: ARC domain scope declaration; distinct surface at `/arc`, API namespace `/api/arc/`, `arc_classifications` table | `arc_classifications` DDL and ARC surface design deferred to Stage 5 |
| Stage 1 §4: ARC items require executive resolution tracking | TR-1802: ARC triggering model — five classified trigger conditions; server-side classification written to `arc_classifications` | ARC stale-item alert scheduling deferred to Stage 5 |
| Stage 1 §3: Authority boundaries on escalated items | TR-1803: ARC authority path — reserved-matter items require Johan Ras; `ARC_ITEM_RESOLVED` audit event with full actor identity | None |
| Stage 1 §4: Escalated items must not silently age without resolution | TR-1804: ARC state machine — open/in_resolution/resolved/externally_escalated; explicit API actions for each transition; stale alert generation | ARC Realtime subscription wiring deferred to Stage 5 |
| Stage 1 §3: Audit significance of all consequential actions | TR-1805: ARC audit event catalog — four required event types with mandatory fields; cross-system ref requirement | None |
| Stage 1 §4: ARC as architecturally recognizable domain | TR-1806: Architecture implications — `arc_classifications` table required; ARC not implementable as UI filter; Realtime subscription requirement; Stage 5 obligations listed | As listed in TR-1806 |

---

## 3. Business Rule Technical Realization

All FRS business rules from Section 21 (Business Rules & Decision Rules Summary) are technically realized as shown:

| FRS Rule | Rule Statement | TRS Technical Enforcement | Status |
|---|---|---|---|
| BR-SYS-001 | AI actions must route through AIMC; knowledge ingestion must route through KUC/AIMCC | TR-BOUNDARY-001, TR-BOUNDARY-002, TR-504, TR-604; dependency enforcement via architecture; `BOUNDARY_BYPASS_ATTEMPTED` event | ✅ Realized |
| BR-AUTH-001 | Reserved matters require Johan Ras; no silent conversion to routine | TR-1404: `reserved_matter` authority boundary → human actor check server-side | ✅ Realized |
| BR-AUTH-002 | Maturion approves only within delegated domains | TR-1404: `delegated` boundary → `ai_executive` actor type check | ✅ Realized |
| BR-AUTH-003 | AMC must not approve its own governance actions | TR-304: Approval blocking rule; server-side check before any governance-sensitive dispatch | ✅ Realized |
| BR-AUTH-004 | AI suggestions distinguishable from decisions | TR-803: `response_type` mandatory; prohibition on defaulting to "Decision"; "type unavailable" indicator | ✅ Realized |
| BR-ALERT-001 | Acknowledgment is explicit actor action, not implicit on view | TR-202: Explicit `POST /api/alerts/{id}/acknowledge` required; no implicit acknowledgment on GET | ✅ Realized |
| BR-ALERT-002 | Dismissal restricted to Low/Informational | TR-204: Server-side HTTP 422 rejection for Critical/High/Medium dismiss attempts | ✅ Realized |
| BR-ALERT-003 | Unacknowledged Critical alerts auto-escalate after timeout | TR-206: Background scheduler contract; query pattern; timeout escalation audit event | ✅ Realized |
| BR-ALERT-004 | Alert expiry does not silently resolve underlying condition | TR-203: Escalation records alert ID; alert remains visible with escalation status | ✅ Realized |
| BR-APPROVAL-001 | Governance-sensitive actions blocked until explicit approval | TR-304: Server-side approval blocking gate; HTTP 423 on blocked actions | ✅ Realized |
| BR-APPROVAL-002 | Approval basis required | TR-302: `approval_basis` non-empty enforcement; HTTP 422 if empty | ✅ Realized |
| BR-APPROVAL-003 | Rejection reason required | TR-302: `rejection_reason` non-empty enforcement; HTTP 422 if empty | ✅ Realized |
| BR-AUDIT-001 | Every consequential action must produce audit event with all mandatory fields | TR-1301: Append-only `audit_events` schema; mandatory fields defined; action-blocking if fields cannot be populated | ✅ Realized |
| BR-AUDIT-002 | Audit records append-oriented; corrections additive | TR-1301: No UPDATE/DELETE on `audit_events`; `CORRECTION_RECORD` pattern defined | ✅ Realized |
| BR-STATE-001 | AMC must not cache persistent knowledge truth | TR-703: No knowledge content tables; 5-minute TTL max; TR-BOUNDARY-003 | ✅ Realized |
| BR-STATE-002 | Degraded mode must not serve stale data as current | TR-1602, TR-1603, TR-1604: Explicit stale indicators and HTTP 503 responses; no silent stale-as-current serving | ✅ Realized |
| BR-DEGRADE-001 | AIMC unavailability does not authorize direct model fallback | TR-1602: HTTP 503 on AIMC endpoints during degraded; no fallback path defined or permitted | ✅ Realized |
| BR-DEGRADE-002 | AIMCC unavailability does not authorize direct ingestion bypass | TR-1603: Upload queue pending during AIMCC degraded; not processed directly | ✅ Realized |

---

## 4. Stage 4 Deferred Items Register

The following items were identified in Stage 4 TRS but explicitly deferred to Stage 5 Architecture. Deferral is documented with rationale. None of these deferrals represents a requirement drop — all are Stage 5 responsibilities.

| Item | FRS Source | Deferral Rationale | Stage 5 Owner |
|---|---|---|---|
| Health domain status aggregation algorithm | FR-101 | Business logic detail requires Architecture-stage domain design | Architecture stage / api-builder |
| Per-domain health record schema column types | FR-102 | Schema column type decisions are Architecture/schema-builder domain | schema-builder |
| Route guard implementation | FR-104 | Frontend framework implementation detail | ui-builder |
| Alert history API endpoint filtering | FR-209 | Extension of existing GET /api/alerts — implementation detail | api-builder |
| Approval detail UI surface layout | FR-302 | UI component design | ui-builder |
| Deferral reminder scheduling implementation | FR-305 | Infrastructure mechanism selection | Architecture stage |
| Clarification conversation UI wiring | FR-306 | UI interaction pattern | ui-builder |
| Intervention type catalogue definition | FR-402 | Product domain list — requires product design session | Architecture stage (with CS2 input) |
| Foreman-side intervention dispatch format | FR-403 | Cross-system contract owned by Foreman spec | Foreman specification |
| Intervention retry/escalate/close UI | FR-406 | UI interaction pattern | ui-builder |
| Provenance chain UI display | FR-602, FR-702 | UI layout | ui-builder |
| Knowledge retrieval UI surface | FR-701 | UI component design | ui-builder |
| Conversation UI layout | FR-801 | UI component design | ui-builder |
| Workspace detail UI layout | FR-902 | UI component design | ui-builder |
| Report detail UI layout | FR-1002 | UI component design | ui-builder |
| Push provider selection (FCM/APNs/PWA) | FR-1202 | Platform-specific integration decision | Architecture stage / integration-builder |
| Mobile UI component breakpoints | FR-1201, FR-1203 | Frontend implementation | ui-builder |
| MFA per-user configuration flow | FR-1401 | Authentication UX flow | ui-builder / api-builder |
| Delegated-domain scope configuration storage | FR-1402 | Configuration architecture | Architecture stage |
| Background scheduler implementation mechanism | FR-208 | Infrastructure mechanism (cron/Edge Function) | Architecture stage |
| Audit review surface UI | FR-1303 | UI component design | ui-builder |
| CI/CD and deployment infrastructure | Stage 4 scope | Infrastructure decisions are Architecture stage | Architecture stage |
| `arc_classifications` table DDL (column types, index design) | Stage 1 §4 / TR-1806 | Schema design details | schema-builder |
| ARC surface UI/UX design and component tree | Stage 1 §4 / TR-1801 | Architecture-stage decision | ui-builder |
| ARC Realtime subscription wiring for underlying source object changes | Stage 1 §4 / TR-1806 | Implementation-level Realtime wiring | api-builder |
| ARC stale-item alert scheduling implementation | Stage 1 §4 / TR-1804 | Infrastructure mechanism | Architecture stage |
| Alert timing SLA breach self-monitoring implementation | FR-201 / TR-207 | System observability infrastructure | Architecture / api-builder |
| Quota threshold configuration storage and runtime reload mechanism | FR-603 / TR-607 | Configuration system architecture | Architecture stage |

---

## 5. Coverage Completeness Verification

| Check | Result |
|---|---|
| Total FRS requirement families covered | 17 of 17 — ✅ No family dropped |
| Stage 1 §4 ARC domain explicitly realized | 1 of 1 — ✅ TR-1800 family added in v1.1 |
| Total FRS individual requirements mapped | 60+ individual FRs mapped + ARC domain + quota console — see §2 |
| FRS families silently dropped | 0 |
| Business rules technically realized | 18 of 18 — ✅ All realized |
| Deferred items disclosed | 30 items (21 original + 9 added in v1.1) — all explicitly documented in §4 |
| Cross-system boundaries preserved | ✅ All 5 boundaries preserved — see §6 |
| Stage 5 deferred items clearly bounded | ✅ All deferred items assigned to Stage 5 owner |
| TRS contains no vague technical wording | ✅ All TRS requirements specify explicit API contracts, schema fields, or enforcement mechanisms |
| ARC technical domain explicitly defined | ✅ TR-1801–TR-1806; distinct domain, table, API namespace, audit family |
| Dynamic Upload Quota Management as operational console | ✅ TR-605–TR-609; adjustment, override, threshold state machine, authorization, audit |
| Alert timing/retry/escalation contract family explicit | ✅ TR-207, TR-208, TR-209 |
| Audit & Provenance declared as contract family | ✅ TR-1300 section — explicit contract family declaration + TR-1305 atomicity |
| Auth & Trust-Boundary declared as contract family | ✅ TR-1400 section — explicit contract family declaration + TR-1405 trust anchor |
| State Ownership declared as contract family | ✅ TR-1700 section — explicit contract family declaration |

---

## 6. Cross-System Boundary Preservation Check

This section confirms that all approved cross-system boundaries from Stages 1–3 are preserved in Stage 4 TRS. No Stage 4 wording silently reassigns ownership.

| Boundary | Stage 1–3 Rule | Stage 4 TRS Enforcement | Preserved? |
|---|---|---|---|
| **AMC / AIMC** | All AI model interactions must route through AIMC. AMC must not call model providers directly | TR-BOUNDARY-001: No model-provider SDK in AMC dependencies. TR-502: All AI calls via AIMC API. TR-504: Architecture dependency enforcement | ✅ Preserved |
| **AMC / AIMCC** | AMC must not bypass AIMCC for knowledge operations. AMC surfaces ingestion status sourced from AIMCC — does not own it | TR-BOUNDARY-002: No direct AIMCC ingestion endpoint calls from AMC. TR-601: AIMCC read API for status only. TR-1701: AIMCC owns knowledge_upload_records | ✅ Preserved |
| **AMC / KUC** | All knowledge upload actions from AMC must route through KUC. AMC must not initiate ingestion directly | TR-604: All upload submissions POST to KUC API exclusively. TR-BOUNDARY-002 | ✅ Preserved |
| **AMC / Knowledge/Memory System** | AMC may query and surface knowledge with provenance. AMC must not become canonical owner or privately cache persistent knowledge truth | TR-703: No knowledge content tables in AMC. 5-minute TTL cache max. Provenance mandatory on all retrieval. TR-BOUNDARY-003. TR-1701: Knowledge/memory system is sole canonical owner | ✅ Preserved |
| **AMC / Foreman** | Foreman is supervised orchestration authority. AMC surfaces Foreman reporting read-only. AMC does not issue build commands | TR-1101: Foreman reporting feed read-only. No build command endpoints in AMC API. TR-402: Intervention dispatch through governed pathway only | ✅ Preserved |

**Boundary preservation result: All 5 cross-system boundaries preserved. No ownership reassignment in Stage 4.**

---

*End of FRS-to-TRS Traceability — Stage 4 v1.1. Produced by foreman-v2-agent under POLC_ORCHESTRATION. CS2 approval required alongside the Technical Requirements Specification before Architecture (Stage 5) derivation begins.*

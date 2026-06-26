# AMC Stage 5 Functional Delivery Architecture Map

**Stage**: 5 — Architecture mapping artifact  
**Module**: App Management Centre (AMC)  
**Version**: 1.1  
**Status**: Produced for CS2 review  
**Wave**: amc-stage5-functional-delivery-retrofit-20260626  
**Issue**: app_management_centre#1187  
**Authority basis**: PR #1186, FR-1900, TR-1900, Stage 2 CTA/API/Data/Audit matrix, Stage 4 TRS canonical route/event contracts  
**Non-scope**: This map does not start Stage 5a, Stage 6, Stage 8, builder checklist, IAA pre-brief, builder appointment, or implementation work.

---

## 1. Purpose

This map binds AMC material user actions to architecture responsibilities so that Stage 5 can demonstrate functional-delivery coverage without leaking into implementation.

It is not a code plan. It is an architecture traceability control.

---

## 2. Route-to-Capability Map

| Surface | Frontend route / surface owner | Capability | Canonical architecture source | Stage 5 disposition |
|---|---|---|---|---|
| Executive Dashboard | `/dashboard` | Estate summary, health domain drill-down, proactive summary display | TR-101 to TR-104; Architecture §3.2/§3.3 | CLEAN — route and API family exist; response/degraded states must be preserved in QA |
| Alert Centre | `/alerts` | Acknowledge, escalate, dismiss, link to approval/intervention | TR-201 to TR-209; Architecture §4.3 | CLEAN — architecture covers table, endpoints, timing, retry, dismissal enforcement |
| Approval Queue | `/approvals` | Approve, reject, defer, block/unblock downstream action | TR-301 to TR-304; Architecture §3.3/§4.5 | CLEAN with retrofit note — deferral must use canonical decision endpoint |
| Intervention Console | `/interventions` | Create, dispatch, cancel, status update timeline | TR-401 to TR-404; Architecture §5.5 | CLEAN — callback path must remain `status-update` per TRS |
| AI Action Monitor | `/ai-actions` | Initiate AIMC action, track callback/result | TR-501 to TR-504; Architecture §5.1/§5.6 | CLEAN — AIMC only; no direct model provider path |
| AIMCC/KUC Supervision | `/aimcc-supervision` | View upload/quota status, submit upload via KUC, request quota action | TR-601 to TR-609; Architecture §4.2/§5.2/§5.3 | CLEAN — outbound service contracts only; no direct AIMCC ingestion |
| Knowledge-Aware View | `/knowledge` | Retrieve knowledge with provenance and stale-state display | TR-701 to TR-703; Architecture §5.4/§6.3 | CLEAN — outbound knowledge retrieval contract only; read-only projection and provenance required |
| Conversation | `/conversation` | Send governed message, receive AIMC/proactive response | TR-801 to TR-805; Architecture §5.1/§6.2 | CLEAN — AIMC routed where AI action is required; persistence in conversation state |
| Specialist Agent Workspace Oversight | `/agent-oversight` | View specialist workspace status and request governed termination | TR-901 to TR-902; Architecture §5.5 | CLEAN — status is read-only projection; termination is approval-gated |
| Maintenance & Assurance Reports | `/maintenance-reports` | View maintenance/IAA reports and surface critical findings as alerts | TR-1001 to TR-1002; Architecture §3.3/§4.3 | CLEAN — report surface and critical-alert creation path covered |
| Estate Configuration & Wellbeing | `/estate-config` | View Foreman build status and request governed configuration changes | TR-1101 to TR-1102; Architecture §5.5 | CLEAN — Foreman feed is read-only; config changes are approval-gated |
| ARC Governance Console | `/arc` | Review, begin resolution, resolve, externally escalate ARC item | TR-1801 to TR-1806; Architecture §4.1 | CLEAN — canonical `arc_classifications` / `ARC_ITEM_*` model preserved |
| Mobile Critical Alerts | responsive/mobile alert surface | Open critical alert, acknowledge/escalate from mobile context | TR-1201 to TR-1203 plus TR-200 family | CLEAN — mobile parity must be tested downstream |

---

## 3. Action-to-State / Audit Architecture Map

| Action family | Canonical API / service contract | State owner / data object | Audit event family | Authority / degraded architecture | Stage 5 disposition |
|---|---|---|---|---|---|
| Dashboard summary | `GET /api/dashboard/summary` | `estate_health_scores`, `health_events` | dashboard view / AIMC request events where applicable | Partial availability and stale-state display | CLEAN |
| Health drill-down | `GET /api/dashboard/health/{domain_id}` | `health_events`, domain read model | health-domain view event where audit applies | Unauthorized access denied; unavailable data shown | CLEAN |
| Alert acknowledge/escalate/dismiss | Alert API family from TR-202 to TR-204 | `alerts`, `escalations`, `audit_events` | `ALERT_ACKNOWLEDGED`, `ALERT_ESCALATED`, `ALERT_DISMISSED` | Server-side class enforcement and escalation failure visibility | CLEAN |
| Alert-to-approval | `POST /api/alerts/{alert_id}/link-approval` | `alerts`, `approvals`, `audit_events` | `APPROVAL_CREATED_FROM_ALERT` | Source alert context preserved | CLEAN |
| Alert-to-intervention | Canonical intervention creation contract with `source_alert_id` | `alerts`, `interventions`, `audit_events` | `INTERVENTION_CREATED_FROM_ALERT` | Authority gate before intervention path | CLEAN |
| Approval decision | `POST /api/approvals/{approval_id}/decide` | `approvals`, blocked action record, `audit_events` | `APPROVAL_DECIDED`; deferral event where TRS requires | Reserved matter and blocking gate before side effects | CLEAN |
| Intervention dispatch | External dispatch per TR-402 | `interventions`, `execution_records`, `audit_events` | `INTERVENTION_DISPATCHED` / failure event | External dispatch failure remains visible after local persistence | CLEAN |
| Intervention status update | `POST /api/interventions/{intervention_id}/status-update` | `interventions`, `execution_records`, `audit_events` | `INTERVENTION_COMPLETED` / `INTERVENTION_FAILED` | Authenticated callback and stale timeline detection | CLEAN |
| AIMC action initiation | `POST {AIMC_API_BASE_URL}/actions` plus local action log | `aimc_action_log`, `audit_events` | `AIMC_ACTION_INITIATED`, `AIMC_REQUEST` | AIMC unavailable state; no model-provider bypass | CLEAN |
| AIMC result callback | `POST /api/aimc/callback` | `aimc_action_log`, `audit_events` | `AIMC_ACTION_COMPLETED` / failed result event | Authenticated callback; failure surfaces to user | CLEAN |
| KUC upload submission | `POST {KUC_API_BASE_URL}/submit` | `knowledge_upload_records` projection, `audit_events` | `KUC_UPLOAD_SUBMITTED` | KUC unavailable shown; no direct AIMCC ingestion | CLEAN — event name is canonical for this map; any rename is DRIFT requiring CS2 disposition |
| AIMCC status/quota read | `GET {AIMCC_API_BASE_URL}/uploads/status`; `GET {AIMCC_API_BASE_URL}/quota/current` | `knowledge_upload_records`, quota projection | AIMCC status/quota view events where audit applies | Stale projection and source timestamp required | CLEAN |
| Quota adjustment / override | `POST /api/aimcc/quota/request-adjustment` | `approvals`, quota projection, `audit_events` | `QUOTA_ADJUSTMENT_REQUESTED`, `AIMCC_GOVERNANCE_ACTION_CREATED`, `QUOTA_OVERRIDE_ACTIVATED`, `QUOTA_OVERRIDE_EXPIRED` | Approval gate; temporary override via `adjustment_type` | CLEAN |
| Knowledge retrieval | `POST {KNOWLEDGE_API_BASE_URL}/retrieve` | transient display cache, `knowledge_retrieval_log`, `audit_events` | `KNOWLEDGE_RETRIEVED` | Provenance required; stale/TTL marker required; no AMC-owned knowledge truth | CLEAN |
| Conversation message | Stage 4 conversation contract; AIMC dispatch where AI routing needed | `conversation_messages`, `audit_events` | `CONVERSATION_MESSAGE_SENT`, AIMC event where dispatched | Failed/pending AIMC state visible | CLEAN |
| Specialist workspace status | `GET {SPECIALIST_AGENT_API_BASE_URL}/workspaces` or equivalent Foreman reporting feed | external workspace status projection, `audit_events` where access is audited | workspace status view event where audit applies | Read-only projection; sandbox isolation indicator visible; no internal specialist state exposed | CLEAN |
| Specialist workspace termination | `POST /api/workspaces/{workspace_id}/terminate`; after approval `POST {SPECIALIST_AGENT_API_BASE_URL}/workspaces/{workspace_id}/terminate` | `approvals`, specialist workspace projection, `audit_events` | `APPROVAL_DECIDED`, `UNAUTHORIZED_ACCESS_ATTEMPT` where rejected, termination dispatch event where Stage 6 names it | Reserved/authority-sensitive termination blocked until approval | CLEAN — Stage 6 must bind exact termination dispatch event name or record DRIFT |
| Reports surface read | `GET /api/reports` with `?type=iaa_assurance` and `?type=maintenance` filters | reports projection, `audit_events` where access is audited | reports view event where audit applies | Report fetch failure shown; report items remain visible by severity | CLEAN |
| Critical report alert creation | Backend critical report ingestion path per TR-1002 | `alerts`, report projection, `audit_events` | `REPORT_ALERT_CREATION_FAILED` on alert creation failure | Critical report remains visible even if alert creation fails | CLEAN |
| Foreman build status read | `GET {FOREMAN_API_BASE_URL}/reporting/build-status` | Foreman status projection, `system_health_events`, `audit_events` where access is audited | Foreman health/status events where applicable | Read-only feed; AMC must not call build command endpoints | CLEAN |
| Estate configuration change request | `POST /api/estate-config/request-change` | `approvals`, estate config projection, `audit_events` | `APPROVAL_DECIDED`, `UNAUTHORIZED_ACCESS_ATTEMPT` where rejected, config dispatch event where Stage 6 names it | Config remains unchanged until completed approval record exists | CLEAN — Stage 6 must bind exact config dispatch event name or record DRIFT |
| ARC review/resolution/escalation | `/api/arc/{id}` family; `begin-resolution`, `resolve`, `escalate-externally` | `arc_classifications`, `approvals`, `interventions` where applicable, `audit_events` | `ARC_ITEM_CLASSIFIED`, `ARC_ITEM_STATE_CHANGED`, `ARC_ITEM_RESOLVED`, `ARC_ITEM_EXTERNALLY_ESCALATED` | Reserved/constitutional boundaries enforced | CLEAN |
| Mobile critical alert action | Alert API family through responsive/mobile surface | `alerts`, `audit_events` | mobile alert open/action events where Stage 6 names them | Mobile action parity and cross-device consistency | CLEAN |

---

## 4. External Dependency and Degraded-Mode Map

| Dependency | Architecture role | Degraded / failure state | User-visible obligation | Audit/provenance obligation |
|---|---|---|---|---|
| AIMC | AI action and proactive/conversation gateway | `dependency_unavailable` or action failed/pending | Show Maturion/AIMC unavailable or pending state; no direct model fallback | AIMC request/failure/callback event |
| AIMCC | Upload/quota status and governance notification owner | `stale_projection` or `dependency_unavailable` | Show stale timestamp/source and unavailable reason | AIMCC status/quota event where applicable |
| KUC | Governed upload submission path | submission rejected/unavailable | Show receipt or rejection/unavailable state | `KUC_UPLOAD_SUBMITTED` on submission attempt; failure outcome captured on the same audit event or follow-up failure event named by Stage 6 |
| Knowledge / Memory | Read-only knowledge/provenance source | stale/provenance unavailable | Do not present stale output as current truth | `KNOWLEDGE_RETRIEVED` with provenance/stale marker |
| Foreman | Build-status reporting and intervention dispatch target | dispatch failed / callback stale / feed unavailable | Show failed dispatch or stale/unavailable execution timeline | dispatch/callback/failure audit events; health/status events where applicable |
| Specialist agents | Workspace status and execution-status source for delegated work | callback unavailable/stale; workspace feed unavailable | Show workspace stale/failure state and sandbox isolation indicator | authenticated callback/status events where applicable |
| Push service | Mobile critical alert delivery | delivery failed/delayed | Mobile view must still fetch current server state | push delivery/open/action events where applicable |

---

## 5. Stage 6 QA Derivation Hints

Stage 6 must derive RED tests from the following Stage 5 architecture obligations:

| Failure class | Stage 5 architectural signal | Stage 6 test expectation |
|---|---|---|
| Dead CTA | CTA/action lacks API/service target | Test fails if action exists with no target |
| Backend-only route | API exists but no visible state binding | Test fails if response cannot be surfaced to user |
| Missing state effect | Consequential action lacks state owner/table/projection | Test fails if action cannot persist or declare read-only status |
| Missing audit | Consequential action lacks audit event | Test fails if audit/provenance is absent |
| Authority bypass | Side effect precedes authority/approval gate | Test fails if reserved or approval-gated action proceeds |
| Silent degradation | Dependency failure returns success/no-op | Test fails if degraded/unavailable state is hidden |
| Placeholder leakage | Placeholder action counted as complete | Test fails unless CS2-approved placeholder record exists |
| Route/event drift | Matrix and TRS names conflict without disposition | Test fails until canonical route/event is identified |
| Omitted material route | Stage 5 route exists but is absent from route/action map | Test fails until route appears in Stage 5 and Stage 6 traceability |
| Journey incompleteness | Journey cannot complete frontend + backend + state + audit + visible result | Test fails at journey level |

---

## 6. Open Dispositions for CS2

| Item | Finding | Recommended CS2 disposition |
|---|---|---|
| Stage 2 `wiring-artifact-index.md` status/version drift | Header posture may lag v1.1 approved/harmonized Stage 2 posture | Correct or explicitly supersede before Stage 7/PBFAG final use |
| Stage 5 original architecture v1.0 approval status | Original architecture remains produced approval-pending | Approve only with this Stage 5 retrofit imported |
| Stage 5a dependency | Deployment execution remains separate and mandatory | Do not treat this addendum as Stage 5a completion |
| Stage 6 QA derivation | Stage 6 must import dead-CTA/functional-delivery tests and material routes in this map | Require Stage 6 retrofit/disposition after Stage 5 |
| Stage 8 | Still blocked | Do not start until Stage 5/5a/6/7 are dispositioned |

---

## 7. Verdict

Stage 5 Architecture is functionally aligned after this map is accepted or dispositioned with the Stage 5 addendum and change-propagation audit.

This map is not an implementation plan and does not authorize build work.

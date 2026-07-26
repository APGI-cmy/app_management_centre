# AMC Stage 2 Addendum — CTA/API/Data/Audit Contract Matrix

**Stage**: 2 — UX Workflow & Wiring Spec addendum  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: 🟡 Retrofit Reference Input — merged PR #1186; downstream obligations adopted by the approved Stage 5–8 authority chain.
**Wave**: amc-stage1-4-functional-delivery-retrofit-20260625  
**Issue**: app_management_centre#1185  
**Authority basis**: ISMS/MMM Phase 3 functional-delivery retrofit, PRE_BUILD_STAGE_MODEL_CANON, MMM dead-CTA / visual-shell failure lesson  
**Non-scope**: This addendum does not start Stage 8, does not appoint builders, and does not authorize implementation work.

---

## 1. Purpose

This addendum makes Stage 2 build-safe by converting AMC's journey and wiring model into an explicit CTA/API/Data/Audit contract matrix.

The matrix prevents the following failure classes:

- screens delivered without backend targets;
- backend routes delivered without user-visible confirmation;
- CTAs that silently no-op;
- state changes without persistence;
- approvals or interventions without audit trail;
- degraded external services being hidden from the user;
- placeholder UI being mistaken for complete functionality.

---

## 2. Matrix Rule

Every material AMC user action or system-triggered action must be traceable using this pattern:

`Surface -> CTA/action -> API/route/callback -> owning data/state object -> external dependency -> audit event -> authority/degraded behavior -> visible confirmation -> QA evidence placeholder`

A journey is not fully wired unless every consequential action in that journey appears in this matrix or an equivalent downstream matrix.

### 2.1 Canonical Endpoint and Audit-Event Authority

This retrofit matrix does **not** create new canonical endpoint names, table names, audit-event names, or external service contracts. It is a functional-delivery coverage matrix that must be reconciled against the approved Stage 2 wiring tables and the Stage 4 TRS API/interface and audit-event summaries.

Where this matrix, the Stage 2 wiring spec, and the Stage 4 TRS differ, the downstream rule is:

1. the approved Stage 4 TRS API/interface contract is authoritative for endpoint naming, payload shape, callback naming, HTTP/error behavior, data ownership, and audit-event naming;
2. the approved Stage 2 UX workflow/wiring spec is authoritative for user journey and surface intent;
3. this addendum is authoritative only for requiring complete CTA/API/Data/Audit/Degraded/Confirmation/QA coverage;
4. any remaining route, event, or state-name mismatch must be recorded as DRIFT and reconciled or explicitly CS2-dispositioned before Stage 5/6/7 propagation.

Builders must not infer a new endpoint from this matrix where the TRS already defines a canonical contract.

---

## 3. CTA/API/Data/Audit Contract Matrix

| Surface | CTA / action | API / route / callback | Data / state object | External dependency | Required audit event | Authority / degraded behavior | Visible confirmation | QA evidence placeholder |
|---|---|---|---|---|---|---|---|---|
| Executive Dashboard | Load dashboard summary | `GET /api/dashboard/summary` per TR-101, unless CS2 reconciles a Stage 2 naming drift | `estate_health_scores`, `health_events`, `alerts`, `approvals`, `interventions` | AIMC for proactive summary where applicable | `DASHBOARD_SUMMARY_VIEWED`, `AIMC_REQUEST` when proactive summary requested | If AIMC unavailable, show explicit Maturion unavailable state; dashboard core must still load partial health state | Health tiles render with status, timestamp, partial/stale flags | Stage 6 test: dashboard loads partial state and does not hide degraded AIMC |
| Executive Dashboard | Drill into health domain | `GET /api/dashboard/health/{domain_id}` per TR-102, unless CS2 reconciles a Stage 2 naming drift | `health_events`, domain-specific read model | Domain source feeds | `HEALTH_DOMAIN_VIEWED` | Unauthorized domain access denied; unavailable data returns explicit unavailable reason | Drill-down screen shows records or unavailable state, never empty unmarked list | Stage 6 test: domain drill-down unavailable response visible |
| Alert Centre | Acknowledge alert | `POST /api/alerts/{id}/acknowledge` | `alerts`, `audit_events` | None | `ALERT_ACKNOWLEDGED` | Actor must be authorized; write failure must not mark alert acknowledged | Alert status changes to acknowledged; audit reference shown | Stage 6 test: acknowledge persists and audit event exists |
| Alert Centre | Escalate alert | `POST /api/alerts/{id}/escalate` | `alerts`, `escalations`, `audit_events` | Escalation notification service if configured | `ALERT_ESCALATED` | Escalation target and reason required; escalation failure remains visible | Escalation status and target shown | Stage 6 test: escalation creates escalation record and audit event |
| Alert Centre | Dismiss alert | `POST /api/alerts/{id}/dismiss` | `alerts`, `audit_events` | None | `ALERT_DISMISSED` | Critical/High/Medium dismissal blocked server-side unless canon permits; reason required | Dismissal confirmation or blocked message shown | Stage 6 test: restricted alert class cannot be dismissed |
| Alert Centre | Link alert to approval | `POST /api/alerts/{alert_id}/link-approval` | `alerts`, `approvals`, `audit_events` | None | `APPROVAL_CREATED_FROM_ALERT` | Failure must not alter alert state; approval context must preserve source alert | Approval item created and linked reference displayed | Stage 6 test: alert-to-approval creates linked approval |
| Alert Centre | Link alert to intervention | Canonical Stage 4/5 intervention creation contract; must preserve `source_alert_id` | `alerts`, `interventions`, `audit_events` | Foreman later at dispatch only | `INTERVENTION_CREATED_FROM_ALERT` | Intervention creation respects authority level and approval requirement | Intervention draft/detail opens with alert context | Stage 6 test: alert-to-intervention preserves source context |
| Approval Queue | Approve item | `POST /api/approvals/{approval_id}/decide` with `decision: "approved"` | `approvals`, `audit_events`, affected blocked action record | Downstream service only after approval persists | `APPROVAL_DECIDED` | Reserved matters require Johan/CS2; approval basis required; downstream dispatch failure must not erase approval record | Approved state plus downstream unblock result shown | Stage 6 test: reserved matter cannot self-approve; audit persists before dispatch |
| Approval Queue | Reject item | `POST /api/approvals/{approval_id}/decide` with `decision: "rejected"` | `approvals`, `audit_events`, affected blocked action record | Originating service notification if applicable | `APPROVAL_DECIDED` | Rejection reason required; blocked action remains blocked/cancelled per contract | Rejected state and reason shown | Stage 6 test: rejection requires reason and cancels/unblocks correctly |
| Approval Queue | Defer with note | `POST /api/approvals/{approval_id}/decide` with `decision: "deferred"` | `approvals`, `audit_events` | Reminder scheduler if configured | `APPROVAL_DECIDED`, `APPROVAL_DEFERRED` where TR-1302 audit family requires explicit deferral event | Deferral note and follow-up time required | Deferred state and follow-up time shown | Stage 6 test: deferral uses canonical decision endpoint, requires note, and remains pending |
| Approval Queue | Request clarification | Stage 4 conversation/AIMC contract; no new approval endpoint | `conversation_messages`, `approvals`, `audit_events` | AIMC via canonical AIMC API call contract when AI is used | `CLARIFICATION_REQUESTED`; `AIMC_REQUEST` only when AIMC dispatch actually occurs | AIMC degraded state must be visible; approval remains pending | Conversation thread opens with linked approval context | Stage 6 test: clarification does not imply approval |
| Intervention Manager | Create intervention | Stage 4/5 intervention creation contract; must persist to `interventions` before dispatch | `interventions`, `audit_events` | None | `INTERVENTION_INITIATED` | Reserved/intervention-sensitive types must create approval gate first | Intervention created as draft/pending approval/ready to dispatch | Stage 6 test: intervention authority gate is enforced |
| Intervention Manager | Dispatch intervention | External dispatch per TR-402: `POST {FOREMAN_API_BASE_URL}/api/foreman/dispatch-intervention` or specialist-agent dispatch contract | `interventions`, `execution_records`, `audit_events` | Foreman dispatch API / specialist-agent API | `INTERVENTION_DISPATCHED` | Dispatch blocked until required approval exists; Foreman unavailable shows failed dispatch, not complete | Dispatch accepted with Foreman/specialist correlation ID or failure reason | Stage 6 test: dispatch cannot proceed without approval and records external ack |
| Intervention Manager | Cancel intervention | `POST /api/interventions/{intervention_id}/cancel` | `interventions`, `execution_records`, `audit_events` | Foreman/specialist abort pathway if already dispatched | `INTERVENTION_CANCELLED`; `INTERVENTION_ABORT_SIGNAL_FAILED` if abort signal fails | Cancel reason required; abort failure is separately visible | Cancelled or abort-pending state shown | Stage 6 test: cancellation persists and handles abort failure |
| Intervention Detail | Receive execution status | `POST /api/interventions/{intervention_id}/status-update` per TR-403 | `interventions`, `execution_records`, `audit_events` | Foreman / specialist agents | `INTERVENTION_COMPLETED` or `INTERVENTION_FAILED` | Callback authenticated; stale status flagged if no update inside threshold | Timeline updates in real time or shows stale indicator | Stage 6 test: callback auth and status timeline work |
| AI Action Monitor | Initiate AI-routed action | `POST {AIMC_API_BASE_URL}/actions` per TR-502; AMC persists local `aimc_action_log` | `aimc_action_log`, `audit_events`, related approval if needed | AIMC only | `AIMC_ACTION_INITIATED`, `AIMC_REQUEST` | No direct model SDK/provider call permitted; approval-required actions blocked before AIMC dispatch | Action shown as pending/blocked/dispatched | Stage 6 test: no direct provider call; blocked approval works |
| AI Action Monitor | Receive AI action result | `POST /api/aimc/callback` per TR-503 | `aimc_action_log`, `audit_events` | AIMC | `AIMC_ACTION_COMPLETED` | Callback authenticated; failed AIMC result surfaces failure, not success | Action status and result/error visible | Stage 6 test: AIMC callback updates action log |
| AIMCC/KUC Supervision | View upload status | TRS-defined outbound AIMCC read/status API; AMC must not invent an AIMCC ingestion route | `knowledge_upload_records` read-only projection | AIMCC | `AIMCC_STATUS_VIEWED` or TRS/Stage 5 named read-audit event if superseded | AIMCC unavailable shows stale/degraded indicator; AMC remains non-owner | Upload list shows status/provenance/stale flag | Stage 6 test: upload status degrades explicitly |
| AIMCC/KUC Supervision | Submit upload through governed path | TRS-defined outbound KUC submission API; no direct AIMCC ingestion endpoint | `knowledge_upload_records` projection, `audit_events` | KUC -> AIMCC | `KUC_UPLOAD_SUBMITTED` or TRS/Stage 5 named upload-submission event if superseded | AMC must not call AIMCC ingestion directly; failure shows KUC rejection/unavailable state | Submission receipt or failure reason shown | Stage 6 test: upload path uses KUC only |
| Dynamic Upload Quota Console | Request quota adjustment | `POST /api/aimcc/quota/request-adjustment` | `approvals`, `audit_events`, quota projection | AIMCC after approval | `QUOTA_ADJUSTMENT_REQUESTED`, `AIMCC_GOVERNANCE_ACTION_CREATED` | Reserved matter approval required; reason, requested value, and `adjustment_type` required | Approval item created; quota not changed before approval | Stage 6 test: quota adjustment is approval-gated and emits canonical request event |
| Dynamic Upload Quota Console | Request temporary quota override | `POST /api/aimcc/quota/request-adjustment` with `adjustment_type: "temporary_override"` | `approvals`, `audit_events`, quota projection | AIMCC after approval | `QUOTA_ADJUSTMENT_REQUESTED`; later lifecycle events: `QUOTA_OVERRIDE_ACTIVATED`, `QUOTA_OVERRIDE_EXPIRED` | Expiry required; approval required; pre-expiry alert required; no separate temporary override initiation route | Override request pending/active/expired state visible | Stage 6 test: temporary override uses canonical request-adjustment route and lifecycle events |
| Knowledge-Aware View | Retrieve knowledge with provenance | `POST /api/knowledge/query` | transient display cache, `knowledge_retrieval_log`, `audit_events` | Knowledge/memory governed API | `KNOWLEDGE_RETRIEVED` | `require_provenance: true`; no local write-primary knowledge cache | Answer/reference shown with source/provenance/stale state | Stage 6 test: provenance required and stale state visible |
| Conversation | Send message to Maturion | Stage 4 conversation message contract plus AIMC dispatch via `POST {AIMC_API_BASE_URL}/actions` where AI routing is required | `conversation_messages`, `audit_events` | AIMC | `CONVERSATION_MESSAGE_SENT`, `AIMC_REQUEST` when AIMC dispatch occurs | AIMC unavailable keeps user message with failed/pending state; no direct model fallback | Message appears with pending/sent/failed status | Stage 6 test: message persists and degraded AIMC shown |
| Conversation | Receive proactive Maturion message | AIMC result via `POST /api/aimc/callback`, rendered into conversation/proactive surface | `conversation_messages`, `alerts` if urgent, `audit_events` | AIMC | `PROACTIVE_MESSAGE_RECEIVED`, `CONVERSATION_RESPONSE_RECEIVED` where response is rendered as conversation | Response type label required; reserved decision cannot be implied | Proactive message shown with type label and action path | Stage 6 test: proactive message cannot imply approval |
| ARC Governance Console | Review ARC item | `GET /api/arc/{id}` or list/detail route defined by Stage 5 architecture over canonical ARC item model | `arc_classifications`, `approvals`, `audit_events` | ARC source / Foreman where applicable | `ARC_ITEM_CLASSIFIED` or `ARC_ITEM_STATE_CHANGED` where the view causes state/audit change; pure reads may use read-access audit only if Stage 5 defines it | Reserved/constitutional ARC items route to CS2 approval boundary | ARC item detail shows authority boundary, classification state, and permitted next actions | Stage 6 test: ARC item authority boundary visible |
| ARC Governance Console | Begin ARC resolution | `POST /api/arc/{id}/begin-resolution` | `arc_classifications`, `audit_events` | Foreman if resolution requires governed execution | `ARC_ITEM_STATE_CHANGED` | Actor must have resolution authority; item must be in resolvable state | Resolution state and correlation reference shown | Stage 6 test: ARC resolution start persists canonical state |
| ARC Governance Console | Resolve ARC item | `POST /api/arc/{id}/resolve` | `arc_classifications`, `audit_events` | Foreman if completion evidence is external | `ARC_ITEM_RESOLVED` | Required evidence/rationale captured; reserved matter approval enforced where applicable | Resolved state and evidence reference shown | Stage 6 test: ARC resolution emits canonical event and evidence reference |
| ARC Governance Console | Escalate ARC item externally | `POST /api/arc/{id}/escalate-externally` | `arc_classifications`, `audit_events`, `interventions` where applicable | External escalation target / Foreman where applicable | `ARC_ITEM_EXTERNALLY_ESCALATED` | Escalation reason and target required; downstream dispatch failure visible | Escalated state and target/correlation shown | Stage 6 test: ARC external escalation uses canonical route and audit event |
| Mobile Critical Alert | Open critical push alert | `GET /api/alerts/{id}` plus push notification deep link | `alerts`, `audit_events` | Push service | `MOBILE_ALERT_OPENED` | Mobile action parity required; no view-only critical alert dead end | Mobile alert detail opens with acknowledge/escalate actions | Stage 6 test: mobile critical alert has functional action path |

---

## 4. Stage 2 Closure Rule

Stage 2 may be considered functionally aligned only when every primary and secondary journey has a completed row set in this matrix or a downstream equivalent. Any CTA/action not mapped to an API/data/audit/degraded behavior must be treated as a DRIFT or AMBIGUITY item in the change-propagation audit.

---

## 5. Downstream Carry-Forward

Stage 3 must convert the matrix into functional requirements. Stage 4 must convert it into technical requirements. Stage 5 must convert it into route/component/schema architecture. Stage 6 must create RED tests from it. Stage 7 must fail PBFAG if material CTA/API/Data/Audit mappings are missing. Stage 5/6/7 must use the canonical Stage 4 TRS route/event contracts when deriving architecture and tests from this matrix.

# AMC Stage 1 Addendum — Functional Delivery Definition

**Stage**: 1 — App Description addendum  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: Produced for CS2 review  
**Wave**: amc-stage1-4-functional-delivery-retrofit-20260625  
**Issue**: app_management_centre#1185  
**Authority basis**: ISMS/MMM Phase 3 functional-delivery retrofit, PRE_BUILD_STAGE_MODEL_CANON, MMM deployment-execution lessons  
**Non-scope**: This addendum does not start Stage 8, does not appoint builders, and does not authorize implementation work.

---

## 1. Purpose

This addendum amends the Stage 1 AMC App Description with a fully functional delivery definition.

The purpose is to prevent AMC from being treated as complete because screens exist, documents exist, tests are listed, or CI passes. AMC is an executive control plane. A visual shell, dead CTA, unpersisted state change, silent integration failure, missing audit event, or unverified approval pathway is a governance failure.

---

## 2. Fully Functional Delivery Definition

AMC delivery is complete only when every user-visible capability is functionally wired end to end.

A capability is not complete unless all of the following are true:

1. **User action exists** — the relevant screen, CTA, form, notification, panel, or system-triggered action is visible and usable by the authorized actor.
2. **Backend/API target exists** — the action has a defined route, endpoint, callback, service method, or integration target.
3. **Authority is enforced** — the action checks actor authority, reserved-matter status, delegation boundary, and approval prerequisites before execution.
4. **State effect is explicit** — the action either mutates a defined AMC-owned state object/table or is explicitly read-only.
5. **Audit event is emitted** — every consequential action writes a named audit/provenance event with actor, timestamp, action, object, authority basis, result, and correlation reference where applicable.
6. **External dependency behavior is defined** — AIMC, AIMCC, KUC, knowledge/memory, Foreman, and specialist-agent dependency failures surface explicit degraded or failure states; they must not silently no-op.
7. **User-visible confirmation exists** — success, failure, blocked, pending, stale, and degraded states are visible to the user.
8. **Test and evidence path exists** — the capability is traceable to QA-to-Red and later wave evidence proving it works as a user journey, not merely as isolated code.
9. **No undeclared placeholder remains** — a placeholder surface, stub, disabled button, mock response, or partial feature may not be counted complete unless explicitly declared and CS2-approved.

---

## 3. AMC-Specific High-Risk Functional Delivery Surfaces

The following AMC surfaces are high-risk because a partial implementation can create false governance confidence:

| Surface | Failure if incomplete | Required functional delivery proof |
|---|---|---|
| Executive Dashboard | False estate-health picture | Health data source, stale/degraded indicators, drill-down route, audit/provenance for generated alerts |
| Alert Centre | Critical matters unseen or unhandled | Acknowledge/escalate/dismiss/link flows persist state and emit audit events |
| Approval Queue | Reserved matter bypass or dead approval | Blocking gate, authority check, decision persistence, downstream unblock/reject behavior |
| Intervention Manager | Intervention appears dispatched but is not | Foreman dispatch acknowledgement, execution status callback, cancellation, failure handling |
| AI Action Monitor | AI action bypasses AIMC or result disappears | AIMC-only routing, action log, callback/retry/degraded handling |
| AIMCC/KUC Supervision | Upload/quota governance appears active but is not | Read-only AIMCC projection, KUC-only submission, quota thresholds, approval gate |
| Knowledge-Aware View | Stale/private knowledge shown as truth | Provenance display, non-ownership rule, stale indicator, no local write-primary cache |
| Conversation with Maturion | Conversation looks live but has no governed backend | AIMC routed message, response type labels, persistence, acknowledgement, degraded behavior |
| ARC Governance Console | Governance trigger appears handled but is not | Trigger state, authority gate, escalation path, audit trail |
| Mobile Critical Alerts | Mobile shows information but cannot act | Push/interrupt, acknowledge/escalate actions, cross-device state consistency |

---

## 4. Downstream Propagation Rule

This definition must be propagated into:

- Stage 2 as a CTA/API/Data/Audit contract matrix;
- Stage 3 as fully functional delivery requirements;
- Stage 4 as technical fully functional delivery requirements;
- Stage 5 architecture as route-to-capability and action-to-state mapping;
- Stage 6 QA-to-Red as tests for dead CTA, backend missing, audit missing, degraded-mode missing, and placeholder leakage;
- Stage 7 PBFAG as a functional-delivery hard gate;
- Stage 8 implementation planning as wave completion criteria.

No later stage may mark AMC implementation-ready unless this propagation is checked and recorded.

---

## 5. Gate Statement

Until this addendum is accepted or dispositioned by CS2, AMC Stages 1-4 should be treated as requiring retrofit for functional-delivery alignment. This does not invalidate the existing Stage 1 approval; it adds a mandatory build-readiness interpretation layer based on later ISMS/MMM learning.

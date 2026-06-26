# AMC Stage 3 Addendum — Fully Functional Delivery Requirements

**Stage**: 3 — Functional Requirements Specification addendum  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: Produced for CS2 review  
**Wave**: amc-stage1-4-functional-delivery-retrofit-20260625  
**Issue**: app_management_centre#1185  
**Authority basis**: ISMS/MMM Phase 3 functional-delivery retrofit, PRE_BUILD_STAGE_MODEL_CANON, MMM dead-CTA / visual-shell failure lesson  
**Non-scope**: This addendum does not start Stage 8, does not appoint builders, and does not authorize implementation work.

---

## 1. Purpose

This addendum adds a cross-cutting functional-delivery requirement family to AMC Stage 3.

The existing FRS defines what AMC must do. This addendum defines the minimum conditions under which a functional capability may be counted as delivered.

---

## 2. New Requirement Family: FR-1900 — Fully Functional Delivery

### FR-1901 — End-to-End User Action Completion

Every material user-visible action in AMC must be delivered end to end. A material action includes any CTA, form submission, dashboard drill-down, alert action, approval action, intervention action, AI action, quota action, knowledge retrieval, conversation message, mobile alert action, ARC trigger action, or system-triggered action that changes state or influences governance.

**Acceptance criteria**:

- The action has a visible entry point.
- The action has a defined backend/API target or governed callback pathway.
- The action has a defined success state and failure state.
- The action cannot silently no-op.
- The action is traceable to Stage 2 CTA/API/Data/Audit matrix coverage.

### FR-1902 — Backend Wiring Required for Visible Actions

No user-visible AMC action may be counted complete unless it is wired to its required backend/API target, state object, external dependency, and audit event.

**Acceptance criteria**:

- UI-only delivery is not sufficient.
- Backend-only delivery is not sufficient.
- Any declared placeholder must be explicitly identified, justified, and approved by CS2 before it can exist in a delivered wave.

### FR-1903 — Functional State Persistence

Every consequential AMC action must either persist state to the correct AMC-owned state object/table or be explicitly defined as read-only.

**Acceptance criteria**:

- Approval decisions persist to the approval record before downstream dispatch.
- Alert actions persist to alert/escalation records.
- Intervention actions persist to intervention/execution records.
- AI actions persist to the AIMC action log.
- Conversation messages persist to the conversation thread.
- Knowledge status and upload status remain projections where ownership belongs to AIMCC/KUC/knowledge-memory systems.

### FR-1904 — Mandatory Audit and Provenance Coverage

Every consequential AMC action must emit a named audit/provenance event.

**Acceptance criteria**:

- Audit event includes actor, timestamp, source system, action, target object, authority basis where applicable, result, and correlation reference where applicable.
- Approval-sensitive actions include approval basis or rejection/deferral rationale.
- AI-routed actions include AIMC correlation.
- External dependency interactions include dependency status and failure classification where applicable.
- Missing audit event is a functional-delivery failure.

### FR-1905 — Explicit Blocked, Degraded, and Failure States

AMC must surface blocked, degraded, stale, unavailable, and failed states explicitly to the user.

**Acceptance criteria**:

- AIMC unavailable state is visible and does not fall back to direct model calls.
- AIMCC/KUC unavailable state is visible and does not create unmanaged ingestion paths.
- Knowledge/memory unavailable or stale state is visible and does not silently serve stale truth.
- Foreman dispatch unavailable state is visible and does not mark intervention dispatched or complete.
- Approval-required actions show blocked state until the correct approval exists.

### FR-1906 — Authority-Safe Functional Delivery

Fully functional delivery includes authority correctness. A feature that works technically but bypasses reserved-matter, delegation, approval, or non-bypass boundaries is not complete.

**Acceptance criteria**:

- Reserved matters cannot be approved by unauthorized actors.
- Maturion cannot silently convert a reserved matter into a delegated action.
- AMC cannot approve its own governance-sensitive actions.
- All AI actions route through AIMC.
- All knowledge/upload actions route through KUC/AIMCC as applicable.
- AMC cannot become canonical owner of knowledge or memory truth.

### FR-1907 — User-Visible Confirmation and Recovery

Every material action must produce user-visible confirmation of the resulting state.

**Acceptance criteria**:

- Success confirmation identifies what happened.
- Failure confirmation identifies why the action failed where safe to disclose.
- Blocked confirmation identifies what approval/dependency is missing.
- Degraded confirmation identifies which dependency is unavailable or stale.
- Recovery path is visible where the user can retry, request clarification, escalate, or defer.

### FR-1908 — Journey-Level Completion Evidence

AMC completion must be proven at journey level, not only requirement or component level.

**Acceptance criteria**:

- Each primary and secondary user journey must be testable as a complete flow.
- Stage 6 QA-to-Red must include journey-level tests for functional-delivery failure modes.
- Stage 8 implementation waves must define which journeys advance and what evidence proves completion.
- A wave cannot close if it delivers screens without backend wiring or backend routes without user-visible confirmation.

### FR-1909 — Placeholder Declaration Rule

AMC may contain placeholders only when they are explicit, bounded, and CS2-approved.

**Acceptance criteria**:

- Placeholder is named and recorded in wave evidence.
- Placeholder states what is missing and why.
- Placeholder cannot cover an approval, alert, intervention, AI action, audit, ARC, quota, or critical mobile flow unless CS2 explicitly approves the risk.
- Undeclared placeholder is a functional-delivery defect.

---

## 3. Traceability Requirement

FR-1900 must trace downstream as follows:

| Source | Downstream obligation |
|---|---|
| Stage 1 functional delivery definition | FR-1901 to FR-1909 |
| Stage 2 CTA/API/Data/Audit matrix | FR-1901, FR-1902, FR-1903, FR-1904, FR-1907 |
| Stage 3 FRS | Stage 4 TR-1900 family |
| Stage 4 TRS | Stage 5 route/component/schema architecture and Stage 6 RED tests |
| Stage 6 QA-to-Red | Dead CTA, missing backend, missing audit, degraded-mode, placeholder leakage tests |
| Stage 7 PBFAG | Functional-delivery gate must fail on unresolved FR-1900 coverage gaps |

---

## 4. Gate Statement

FR-1900 is a cross-cutting family. It does not replace FR-100 through FR-1800. It constrains how every AMC functional requirement must be delivered and evidenced.

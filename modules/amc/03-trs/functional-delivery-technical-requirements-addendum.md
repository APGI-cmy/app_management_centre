# AMC Stage 4 Addendum — Fully Functional Delivery Technical Requirements

**Stage**: 4 — Technical Requirements Specification addendum  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: Produced for CS2 review  
**Wave**: amc-stage1-4-functional-delivery-retrofit-20260625  
**Issue**: app_management_centre#1185  
**Authority basis**: ISMS/MMM Phase 3 functional-delivery retrofit, PRE_BUILD_STAGE_MODEL_CANON, MMM deployment-execution lessons  
**Non-scope**: This addendum does not start Stage 8, does not appoint builders, and does not authorize implementation work.

---

## 1. Purpose

This addendum converts Stage 3 FR-1900 fully functional delivery obligations into technical implementation constraints for Stage 5 Architecture, Stage 6 QA-to-Red, Stage 7 PBFAG, and later build waves.

The goal is to prevent AMC from passing as build-ready while still containing dead CTAs, frontend-only screens, backend-only routes, missing audit events, silent degraded modes, unresolved authority bypass risk, or untested user journeys.

---

## 2. New TR Family: TR-1900 — Fully Functional Delivery Technical Requirements

### TR-1901 — CTA-to-Route Contract

Every material CTA/action must have a named route, API endpoint, callback, service method, or explicitly read-only declaration.

**Technical constraints**:

- CTA/action identifiers must be stable enough to map into QA tests.
- No material CTA may exist without a corresponding technical target.
- Disabled or placeholder CTAs must be recorded as placeholders and cannot be counted complete.
- Stage 5 must map each material CTA to a frontend component, route, and backend/API target.
- Endpoint names, callback paths, external service URLs, data ownership, and audit-event names must follow the approved Stage 4 TRS. This addendum cannot introduce a competing endpoint namespace.

### TR-1902 — Typed Success, Failure, Blocked, and Degraded Responses

Every material API/action endpoint must return typed responses for success, validation failure, authorization failure, blocked-by-approval, dependency degraded/unavailable, and unexpected failure.

**Encoding rule**: These response classes are semantic classes for deterministic architecture and QA coverage. They must be represented through the existing Stage 4 TRS HTTP status/error-response patterns and per-endpoint JSON bodies. Where a single envelope discriminator is needed, Stage 5 Architecture may define one consistent field such as `status` or `error_code`, but it must not conflict with the TRS-defined HTTP status codes or per-endpoint payload contracts. Stage 6 tests must assert the concrete encoding selected by Stage 5.

**Minimum response classes**:

| Response class | Required use |
|---|---|
| `success` | Action completed and state persisted or read-only data returned |
| `validation_error` | Required input missing or invalid |
| `unauthorized` | Actor/session lacks access |
| `forbidden_reserved_matter` | Actor lacks authority for reserved/delegated boundary |
| `blocked_by_approval` | Action cannot execute until approval exists |
| `dependency_unavailable` | AIMC/AIMCC/KUC/knowledge-memory/Foreman/dependency unavailable |
| `stale_projection` | Read-only projection is stale but displayed with warning |
| `dispatch_failed` | Downstream dispatch failed after local persistence |
| `unexpected_error` | Unexpected server failure with safe message |

### TR-1903 — Atomic Audit Persistence for Consequential Actions

Consequential actions must persist their business state and audit/provenance state atomically where the same persistence boundary controls both.

**Technical constraints**:

- Approval decision and `APPROVAL_DECIDED` audit event must not diverge.
- Alert acknowledgment/escalation/dismissal and corresponding audit event must not diverge.
- Intervention create/dispatch/cancel/status callback and corresponding audit events must not diverge.
- AI action initiation/result and AIMC correlation event must not diverge.
- If atomic persistence is impossible across external systems, AMC must persist local state first and record external dispatch/callback outcome separately.

### TR-1904 — Authority Enforcement Before Side Effects

Authority checks must execute before any irreversible side effect or downstream dispatch.

**Technical constraints**:

- Reserved-matter checks precede approval decision, ARC decision, intervention dispatch, quota override, and destructive/configuration actions.
- Approval-blocking checks precede AIMC action dispatch, Foreman dispatch, quota update, and ARC-triggered execution.
- Unauthorized attempts generate a security/audit event where safe and appropriate.
- The frontend may pre-warn, but server-side enforcement is mandatory.

### TR-1905 — External Dependency Non-Bypass Enforcement

AMC must enforce external dependency boundaries in code and runtime behavior.

**Technical constraints**:

- AMC code must not import model-provider SDKs or call model providers directly.
- AMC upload submissions must route through KUC; AMC must not call AIMCC internal ingestion endpoints directly.
- AMC must not maintain a write-primary knowledge/memory store.
- Foreman and specialist-agent callbacks must be authenticated and correlation-bound.
- Dependency failure must surface `dependency_unavailable` or `stale_projection`, not silent success.

### TR-1906 — State Persistence and Projection Boundaries

Each AMC action must declare whether it mutates AMC-owned state, reads external projection state, or dispatches to an external owner.

**Technical constraints**:

| State category | Technical rule |
|---|---|
| AMC-owned state | Persist in AMC table/state object with RLS/authorization and audit coverage |
| External projection | Store/read only as projection with source, timestamp, stale flag, and owner reference |
| External dispatch | Persist local dispatch intent/outcome and external correlation reference |
| Transient display | Allowed only with TTL/stale warning and no canonical ownership claim |

### TR-1907 — User-Visible State Binding

Frontend components must bind material actions to visible state transitions.

**Technical constraints**:

- Every action must have loading, success, failure, blocked, and degraded UI states where applicable.
- A successful API response must update the visible UI or invalidate/refetch the relevant state cache.
- A failed API response must not leave the user believing the action succeeded.
- Realtime updates must have polling/refetch fallback where the TRS permits fallback.
- Mobile critical alert actions must maintain cross-device state consistency.

### TR-1908 — No Frontend-Only or Backend-Only Completion

A feature may not be counted complete if only one side of the user journey is implemented.

**Technical constraints**:

- A screen without working action targets is incomplete.
- An API route without user-visible confirmation is incomplete.
- A database table without surfaced state/evidence path is incomplete for user-facing flows.
- A workflow without audit/provenance is incomplete.
- Any exception requires CS2-approved placeholder declaration.

### TR-1909 — QA Evidence Binding

Every TR-1900 requirement must be converted into Stage 6 RED tests and later wave evidence.

**Technical constraints**:

- QA must include dead CTA tests.
- QA must include missing backend target tests.
- QA must include missing audit event tests.
- QA must include authority bypass tests.
- QA must include dependency degraded-mode tests.
- QA must include placeholder leakage tests.
- QA must include journey-level completion tests for all primary surfaces.

### TR-1910 — Deployment-Execution Carry-Forward

Stage 5/5a must freeze deployment and runtime execution behavior with enough precision that builders do not invent operational behavior.

**Technical constraints**:

- Stage 5/5a must identify deployment surface ownership, workflow ownership, environment/protected gate behavior, migration mechanism, live validation sequence, and CI/preview/production boundaries.
- No build wave may rely on operational speculation where the deployment execution contract is blank, TBD, stale, or ambiguous.
- Runtime health/smoke validation must be defined before build waves can close.

---

## 3. Stage 5/6/7 Carry-Forward Requirements

| Downstream stage | Required import from TR-1900 |
|---|---|
| Stage 5 Architecture | Route-to-capability map, CTA-to-component map, API-to-schema map, audit-event map, external dependency map, state ownership/projection map |
| Stage 5a Deployment Execution Strategy | Deployment-execution contract with workflow ownership, live validation, protected gates, environment assumptions, CI/preview/live boundaries |
| Stage 6 QA-to-Red | RED tests for every TR-1900 failure class |
| Stage 7 PBFAG | Hard fail if any material action lacks CTA/API/Data/Audit/QA coverage |
| Stage 8 Implementation Plan | Wave completion standard requiring frontend + backend + state + audit + degraded behavior + evidence |

---

## 4. Gate Statement

TR-1900 is cross-cutting and applies to every AMC technical domain. Any contradiction between TR-1900 and a weaker downstream interpretation must be treated as a governance DRIFT item until resolved by Foreman and CS2.

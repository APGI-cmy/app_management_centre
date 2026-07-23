# AMC Stage 5 Addendum — Functional Delivery Architecture

**Stage**: 5 — Architecture addendum  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: ✅ CS2 Approved with Conditions — decision issue #1197 / merged PR #1198.
**Wave**: amc-stage5-functional-delivery-retrofit-20260626  
**Issue**: app_management_centre#1187  
**Authority basis**: PR #1186, Stage 1 functional-delivery definition, Stage 2 CTA/API/Data/Audit matrix, Stage 3 FR-1900, Stage 4 TR-1900, Stage 1-4 change-propagation audit  
**Non-scope**: This addendum does not start Stage 5a, Stage 6, Stage 8, builder checklist, IAA pre-brief, builder appointment, or implementation work.

---

## 1. Purpose

This addendum imports the merged Stage 1-4 functional-delivery retrofit into Stage 5 Architecture.

The existing Stage 5 Architecture Specification remains the primary architecture artifact. This addendum does not replace it. It adds a mandatory architectural interpretation layer so that Stage 5 cannot be treated as disposition-ready unless it carries forward the fully functional delivery controls created by PR #1186.

---

## 2. Architecture Interpretation Rule

Every material AMC user action must be architecturally traceable as follows:

`Surface -> Frontend route/component responsibility -> API route or external service contract -> state owner/table/projection -> audit event -> authority/degraded behavior -> visible state transition -> Stage 6 QA derivation`

A surface, screen, component, or journey is not architecturally complete if the architecture only defines the frontend or only defines the backend.

Stage 5 must therefore bind:

1. user action;
2. route/component responsibility;
3. API or callback contract;
4. state ownership or read-only projection boundary;
5. audit/provenance event;
6. authority gate;
7. degraded/failure state;
8. user-visible confirmation state;
9. downstream QA derivation.

---

## 3. Canonical Endpoint and Audit-Event Authority

Stage 5 must preserve the canonical endpoint and audit-event authority rule introduced in the Stage 2 retrofit matrix:

1. the approved Stage 4 TRS API/interface contract is authoritative for endpoint naming, payload shape, callback naming, HTTP/error behavior, data ownership, and audit-event naming;
2. the approved Stage 2 UX workflow/wiring spec is authoritative for user journey and surface intent;
3. the Stage 2 CTA/API/Data/Audit matrix is authoritative for requiring complete coverage, but it may not introduce a competing endpoint namespace;
4. any remaining route, event, or state-name mismatch must be recorded as DRIFT and reconciled or explicitly CS2-dispositioned before Stage 6/7/8 use the architecture.

Builders must not infer new endpoints from the matrix where the TRS already defines a canonical contract.

---

## 4. Required Stage 5 Architecture Maps

The existing architecture already includes component boundaries, routes, API namespaces, state tables, audit architecture, degraded-mode behavior, and cross-system interactions. To satisfy TR-1900, Stage 5 must additionally expose the following architecture maps:

| Map | Required by | Stage 5 realization |
|---|---|---|
| Route-to-capability map | TR-1901, FR-1901, FR-1908 | `functional-delivery-architecture-map.md` §2 |
| CTA/action-to-state map | TR-1901, TR-1903, TR-1906 | `functional-delivery-architecture-map.md` §3 |
| API-to-state/audit map | TR-1903, TR-1904, TR-1905 | `functional-delivery-architecture-map.md` §3 |
| External dependency/degraded-mode map | TR-1905, TR-1907 | `functional-delivery-architecture-map.md` §4 |
| No-placeholder/no-dead-CTA controls | TR-1908, FR-1909 | This addendum §6 |
| Stage 6 QA derivation hints | TR-1909 | `functional-delivery-architecture-map.md` §5 |

---

## 5. Response-Class Architecture

TR-1902 defines semantic response classes. Stage 5 adopts the following architecture rule:

- HTTP status codes and per-endpoint JSON bodies remain governed by the existing Stage 4 TRS.
- The semantic response classes in TR-1902 must be represented through those TRS response patterns.
- Where a uniform discriminator is required for client-state binding, Stage 5 permits a single consistent response field named `status` or `error_code`, but only if it does not conflict with the endpoint-specific TRS payload.
- Stage 6 must test the concrete encoding selected by Stage 5/implementation.

Minimum semantic classes to preserve are:

- `success`;
- `validation_error`;
- `unauthorized`;
- `forbidden_reserved_matter`;
- `blocked_by_approval`;
- `dependency_unavailable`;
- `stale_projection`;
- `dispatch_failed`;
- `unexpected_error`.

---

## 6. No-Placeholder / No-Dead-CTA Architecture Control

Stage 5 must not permit unrecorded placeholder functionality.

A frontend route, surface, widget, CTA, action menu item, notification action, mobile action, or system-triggered action is architecturally incomplete unless it has:

1. a defined architectural owner;
2. a user-visible state binding;
3. an API/external service target or explicit read-only declaration;
4. a state effect or projection boundary;
5. an audit/provenance event where consequential;
6. authority/degraded behavior;
7. a downstream QA derivation.

If a placeholder is unavoidable, it must be explicitly recorded with:

- placeholder name;
- affected surface/action;
- missing architectural element;
- risk class;
- proposed downstream disposition;
- CS2 decision requirement.

No placeholder may silently cover alerts, approvals, interventions, AI-routed actions, AIMCC/KUC quota actions, ARC actions, critical mobile alerts, audit/provenance, or non-bypass boundaries.

---

## 7. Downstream Propagation

This Stage 5 addendum must be imported into:

- Stage 5a only for deployment-execution constraints, not implementation work;
- Stage 6 for RED tests covering dead CTA, missing route, missing state, missing audit, authority bypass, degraded-mode, placeholder leakage, and journey-level completion;
- Stage 7 for PBFAG hard-gate evaluation;
- Stage 8 only after CS2 has dispositioned Stage 5, Stage 5a, Stage 6, and Stage 7.

---

## 8. Stage 5 Disposition Statement

Stage 5 Architecture may be treated as functionally aligned only if this addendum, the functional-delivery architecture map, and the Stage 5 change-propagation audit are reviewed and accepted or explicitly dispositioned by CS2.

This addendum does not approve Stage 5 by itself. It produces the retrofit package for CS2 review.

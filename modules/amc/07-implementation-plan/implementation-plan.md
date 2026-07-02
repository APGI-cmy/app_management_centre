# Implementation Plan - Stage 8

**Stage**: 8 - Implementation Plan  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: Produced for CS2 review  
**Issue**: app_management_centre#1199  
**Wave**: amc-stage8-implementation-plan-20260702

---

## 1. Purpose

This Stage 8 artifact converts the approved AMC pre-build pack into a governed plan for later delivery.

It is a planning artifact only. It does not create downstream stage work.

---

## 2. Binding Inputs

Stage 8 imports:

1. `cs2-decision-record-stages-5-5a-6-7.md`.
2. Stage 5 route, action, state, audit, and degraded-mode map.
3. Stage 5a deployment validation matrix.
4. Stage 6 QA-FD and QA-DEPLOY rows.
5. Stage 7 PBFAG blocker rows.
6. First E2E `/alerts` acknowledgement path.
7. Placeholder and stub rejection rule.
8. Production approval gates and secret separation.
9. Supabase migration command freeze.
10. Rollback planning.
11. Runtime health and smoke validation.
12. Dependency readiness and visible degraded-mode behavior.
13. Complete delivery evidence package.
14. Tracker and artifact-index updates.

---

## 3. Planned Delivery Waves

| Wave | Scope | Required controls |
|---|---|---|
| W1 | Runtime foundation and environment setup | CI, preview, secret, and environment boundaries |
| W2 | Auth, tenant, authority, and audit baseline | Authority checks, state ownership, audit events |
| W3 | Core AMC routes and material surfaces | Route/action/state/audit/degraded-mode mapping |
| W4 | `/alerts` first E2E path | UI, API, authority, state, audit, realtime, visible result |
| W5 | ARC, approvals, interventions, and workflow surfaces | ARC model, authority, state, audit, evidence |
| W6 | AIMC, AIMCC, KUC, knowledge, Foreman, specialist, and push integrations | Service-token boundaries, dependency readiness, degraded mode |
| W7 | Deployment execution and release controls | Migration command, rollback, health, smoke, evidence |
| W8 | QA-to-Green consolidation | QA-FD, QA-DEPLOY, PBFAG rows, no placeholder proof |

---

## 4. Evidence Expectations

Later delivery waves must produce evidence for:

- user-visible behavior;
- API behavior;
- state changes;
- audit/provenance events;
- authority checks;
- degraded-mode behavior;
- deployment or preview URL where applicable;
- test logs;
- health and smoke checks;
- rollback or recovery where applicable.

---

## 5. Stage 8 Exit Criteria

Stage 8 can be recommended for CS2 acceptance when:

1. every CS2 condition is mapped to a delivery wave;
2. the `/alerts` first E2E path is planned;
3. deployment, QA, dependency, and evidence duties are planned;
4. Stage 9 inputs are clear;
5. later stages remain gated until separately authorized.

---

## 6. Boundary

This artifact does not create builder checklist, IAA pre-brief, builder appointment, source code, build evidence, or build work.

# AMC Stage 6 Addendum — Functional Delivery QA-to-Red

**Stage**: 6 — QA-to-Red addendum  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: Produced for CS2 review  
**Wave**: amc-stage6-qa-to-red-retrofit-20260629  
**Issue**: app_management_centre#1191  
**Authority basis**: PR #1186, PR #1188, PR #1190, FR-1900, TR-1900, TR-1910, Stage 2 CTA/API/Data/Audit matrix, Stage 5 architecture map, Stage 5a deployment execution validation matrix  
**Non-scope**: This addendum does not start Stage 7, Stage 8, builder checklist, IAA pre-brief, builder appointment, or implementation work.

---

## 1. Purpose

This addendum imports the merged Stage 1-5a functional-delivery controls into Stage 6 QA-to-Red.

The existing Stage 6 artifacts remain the primary QA-to-Red pack:

- `qa-to-red-specification.md`;
- `architecture-and-des-to-qa-traceability.md`;
- `red-test-catalog.md`.

This addendum does not replace those artifacts. It adds mandatory RED coverage so Stage 6 can test the fully functional delivery failure classes introduced after the original Stage 6 pack was produced.

---

## 2. Functional Delivery QA Rule

A QA-to-Red pack is incomplete if it only tests that architectural domains exist.

Stage 6 must also test whether every material user action is fully wired across:

1. visible user surface;
2. CTA/action trigger;
3. API route or external service contract;
4. state owner/table/projection;
5. audit/provenance event;
6. authority gate;
7. degraded-mode behavior;
8. user-visible confirmation or failure state;
9. deployment-execution evidence path.

Any screen, CTA, route, API, callback, or workflow that cannot be tested through this chain must remain RED.

---

## 3. Mandatory Retrofit Failure Classes

Stage 6 must import the following failure classes as RED tests or validation checks:

| Failure class | Source | Stage 6 treatment |
|---|---|---|
| Dead CTA | Stage 5 architecture map | RED test required |
| Missing backend/API/service target | Stage 5 architecture map | RED test required |
| Missing state/projection | Stage 5 architecture map | RED test required |
| Missing audit/provenance | FR-1900 / TR-1900 / Stage 5 map | RED test required |
| Authority bypass | Stage 5 architecture and ARC authority rules | RED test required |
| Degraded mode hidden from user | Stage 5 architecture map | RED test required |
| Placeholder leakage | Stage 5 architecture addendum | RED test required |
| Route/event drift | Stage 2 matrix + Stage 4 TRS + Stage 5 map | RED test required |
| Omitted material route | Stage 5 architecture map | RED test required |
| Journey-level incompleteness | FR-1900 / TR-1900 | RED test required |
| Missing environment variable | `.env.example` + Stage 5a matrix | RED check required |
| Production secret leakage | Stage 5a matrix | RED check required |
| Ungated production deployment | Stage 5a matrix | RED check required |
| Migration command drift | Stage 5a matrix | RED check required |
| Missing runtime health/smoke evidence | Stage 5a matrix | RED check required |
| Missing first E2E audit proof | Stage 5a matrix | RED test required |

---

## 4. First E2E Path Binding

The first required end-to-end evidence candidate remains the `/alerts` acknowledgement path defined by the Stage 5 architecture and Stage 5a validation matrix:

`/alerts` UI -> alert acknowledge API -> authority check -> `alerts` update -> `audit_events` insert -> realtime update -> visible acknowledged state -> audit verification.

Stage 6 must test this path as a full journey. It is not enough to test only a route, only a database update, or only an audit event.

---

## 5. QA-to-Red Catalog Expansion Rule

The original red-test catalog remains valid. This addendum requires an expansion layer rather than renumbering the existing catalog.

New tests introduced by the retrofit must use the `QA-FD-*` and `QA-DEPLOY-*` families:

- `QA-FD-*` for functional-delivery wiring and journey completion;
- `QA-DEPLOY-*` for deployment-execution validation and evidence controls.

Existing test IDs must not be repurposed. If an existing test partially covers a new failure class, the new matrix must record whether the original test is sufficient or whether a new `QA-FD-*` / `QA-DEPLOY-*` test is required.

---

## 6. Stage 7 Carry-Forward

Stage 7 PBFAG must treat the following as blockers before Stage 8:

- missing Stage 6 coverage for any Stage 5 material route/action;
- missing Stage 6 coverage for any Stage 5a deployment execution validation domain;
- any QA-to-Red test that can pass against a stub or placeholder;
- any QA-to-Red family that lacks exact fail and pass conditions;
- unresolved tracker/index mismatch for Stage 6 artifacts;
- missing proof that Stage 6 imported the Stage 5 and Stage 5a retrofit obligations.

---

## 7. Stage 6 Disposition Statement

Stage 6 may be treated as functionally aligned only if this addendum, the RED test expansion matrix, and the Stage 6 change-propagation audit are reviewed and accepted or explicitly dispositioned by CS2.

This addendum does not approve Stage 6 by itself, does not start Stage 7, and does not authorize implementation.

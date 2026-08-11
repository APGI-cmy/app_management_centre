# Issue #1233 — A2-T Intentional-RED Lifecycle Classification

## Authority

- Governing issue: #1233
- Parent QA issue: #1226
- Parent blocker: Issue #1233 baseline regression debt
- B0 freeze authority: Issue #1235 / PR #1236
- Frozen population records: `qa/evidence/issue-1235/B0_REGRESSION_POPULATION_FREEZE.md`
- Frozen B0 base: `eaf9ced583e61b2392a3772a1bea09944ee71439`
- Classification date: 2026-08-07
- Classifier role: Foreman (governance disposition only)

---

## Purpose

This record produces the full Foreman lifecycle classification for the P3 intentional-RED test
population (25 nodes in two files) that were identified in the Issue #1233 failure inventory and
frozen in the B0 population record.

No builder is appointed by this record. No test or runtime code is modified.

---

## Frozen P3 Population (25 nodes)

### File 1: `tests/wave2_0_qa_infrastructure/test_advanced_flow_scenarios.py`

**Subwave:** 2.5  
**Markers:** `@pytest.mark.wave2`, `@pytest.mark.subwave_2_5`  
**QA range:** QA-211 to QA-225 (15 nodes)  
**Declared ownership:** `qa-builder`

| Node ID | QA Ref | Description | Current failure mechanism |
|---|---|---|---|
| `test_qa_211_state_persistence_across_flow` | QA-211 | State persistence across flow | `NotImplementedError: QA-211: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_212_evidence_generation_across_flow` | QA-212 | Evidence generation across flow | `NotImplementedError: QA-212: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_213_authorization_checks_across_flow` | QA-213 | Authorization checks across flow | `NotImplementedError: QA-213: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_214_timeout_handling_in_flow` | QA-214 | Timeout handling in flow | `NotImplementedError: QA-214: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_215_flow_cancellation` | QA-215 | Flow cancellation | `NotImplementedError: QA-215: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_216_escalation_end_to_end` | QA-216 | Escalation end to end | `NotImplementedError: QA-216: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_217_escalation_trigger_detection` | QA-217 | Escalation trigger detection | `NotImplementedError: QA-217: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_218_escalation_creation` | QA-218 | Escalation creation | `NotImplementedError: QA-218: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_219_escalation_routing` | QA-219 | Escalation routing | `NotImplementedError: QA-219: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_220_escalation_presentation` | QA-220 | Escalation presentation | `NotImplementedError: QA-220: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_221_escalation_decision` | QA-221 | Escalation decision | `NotImplementedError: QA-221: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_222_escalation_resolution` | QA-222 | Escalation resolution | `NotImplementedError: QA-222: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_223_escalation_timeout` | QA-223 | Escalation timeout | `NotImplementedError: QA-223: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_224_multiple_concurrent_escalations` | QA-224 | Multiple concurrent escalations | `NotImplementedError: QA-224: To be implemented by qa-builder in Subwave 2.5` |
| `test_qa_225_escalation_error_handling` | QA-225 | Escalation error handling | `NotImplementedError: QA-225: To be implemented by qa-builder in Subwave 2.5` |

### File 2: `tests/wave2_0_qa_infrastructure/test_parking_station_advanced.py`

**Subwave:** 2.2  
**Markers:** `@pytest.mark.wave2`, `@pytest.mark.subwave_2_2`  
**QA range:** QA-416 to QA-425 (10 nodes)  
**Declared ownership:** `ui-builder`

| Node ID | QA Ref | Description | Current failure mechanism |
|---|---|---|---|
| `test_qa_416_assign_priority` | QA-416 | Assign priority to parked idea | `NotImplementedError: QA-416: To be implemented by ui-builder` |
| `test_qa_417_sort_by_priority` | QA-417 | Sort parking station by priority | `NotImplementedError: QA-417: To be implemented by ui-builder` |
| `test_qa_418_priority_change_workflow` | QA-418 | Priority change workflow | `NotImplementedError: QA-418: To be implemented by ui-builder` |
| `test_qa_419_priority_escalation` | QA-419 | Priority-based escalation | `NotImplementedError: QA-419: To be implemented by ui-builder` |
| `test_qa_420_priority_display` | QA-420 | Priority display in UI | `NotImplementedError: QA-420: To be implemented by ui-builder` |
| `test_qa_421_bulk_select` | QA-421 | Bulk select parked ideas | `NotImplementedError: QA-421: To be implemented by ui-builder` |
| `test_qa_422_bulk_priority_update` | QA-422 | Bulk priority update | `NotImplementedError: QA-422: To be implemented by ui-builder` |
| `test_qa_423_bulk_archive` | QA-423 | Bulk archive ideas | `NotImplementedError: QA-423: To be implemented by ui-builder` |
| `test_qa_424_bulk_export` | QA-424 | Bulk export ideas | `NotImplementedError: QA-424: To be implemented by ui-builder` |
| `test_qa_425_bulk_error_handling` | QA-425 | Bulk operation error handling | `NotImplementedError: QA-425: To be implemented by ui-builder` |

---

## Lifecycle Classification Decision

### Classification rationale

These 25 tests are examined against three options:
- **(a) Retain as canonical QA-to-Red** — correct existing intentional-RED posture, appropriate for the Wave 2 Subwave 2.5 / 2.2 features that are not yet built
- **(b) Implement** — build the missing feature so tests pass
- **(c) Archive** — remove the tests with a documented rationale and CS2 governance record

### Classification verdict per group

#### QA-211 to QA-225 (Subwave 2.5 — Advanced Flow Scenarios)

**Verdict: RETAIN as canonical QA-to-Red (Option A)**

These tests represent the QA-to-Red obligations for Subwave 2.5 Advanced Flow features.
They are correctly structured: `NotImplementedError` failure, explicit ownership declaration
(`qa-builder`), correct markers, correct module location. The feature has not been built yet.
These tests must remain failing for the correct intended reason until `qa-builder` is appointed
for Subwave 2.5 Build-to-Green. No lifecycle change is authorised now.

**B1 posture:** P3 canonical expected-RED — must show `25 failed`, `0 passed`, `0 errors`,
`0 skips`, `0 xfails` in all B1 runs. Deviation is a stop condition.

#### QA-416 to QA-425 (Subwave 2.2 — Parking Station Advanced)

**Verdict: RETAIN as canonical QA-to-Red (Option A)**

These tests represent the QA-to-Red obligations for Subwave 2.2 Parking Station Advanced
features. They are correctly structured: `NotImplementedError` failure, explicit ownership
declaration (`ui-builder`), correct markers, correct module location. The feature has not been
built yet. These tests must remain failing for the correct intended reason until `ui-builder`
is appointed for Subwave 2.2 Build-to-Green. No lifecycle change is authorised now.

**B1 posture:** same as QA-211–225: P3 canonical expected-RED.

### Combined classification summary

| Group | Count | Disposition | B1 Posture | Build-to-Green authority |
|---|---|---|---|---|
| QA-211–225 (Subwave 2.5) | 15 | RETAIN canonical QA-to-Red | 15 failed, 0 pass/err/skip/xfail | qa-builder / Subwave 2.5 appointment |
| QA-416–425 (Subwave 2.2) | 10 | RETAIN canonical QA-to-Red | 10 failed, 0 pass/err/skip/xfail | ui-builder / Subwave 2.2 appointment |
| **Total P3** | **25** | **All retained** | **25 failed, 0 other** | **Separate future appointments** |

---

## Prohibitions confirmed

The following remain prohibited for all agents including Foreman:

- skip, xfail, ignore, or deselect any P3 node
- delete, rename, or move any P3 test file or class
- change any P3 test's markers, docstring, or `NotImplementedError` message
- reclassify a P3 failure as an error or pass
- modify `pytest.ini`, `conftest.py`, or discovery configuration to change P3 membership
- appoint a builder for Subwave 2.2 or 2.5 Build-to-Green without a separate CS2-gated
  appointment process and IAA pre-brief

---

## Governance impact on B1

With A2-T lifecycle classification complete:

- P3 posture is **confirmed canonical QA-to-Red**: 25 expected-RED, all `NotImplementedError`
- B1 runs must show exactly `25 failed` in the P3 command set
- B1 runs must show exactly `13 passed` in the P1 command set  
- B1 runs must show all P2 nodes passed
- B1 runs must show P4 (Stage 6) exactly `19 failed`

No new stop condition is introduced by this classification; the P3 population was already the
frozen expected-RED population in the B0 record.

---

## Classification status

```text
A2-T LIFECYCLE CLASSIFICATION: COMPLETE
P3 disposition: ALL 25 NODES RETAINED AS CANONICAL QA-TO-RED
B1 unblocking condition from A2-T: SATISFIED
B1 blocking conditions remaining:
  - B1 execution evidence must be produced on the accepted merged-main head
  - B1 must confirm P1 GREEN (13 passed), P2 GREEN (all nodes), P3 expected-RED (25 failed),
    P4 GREEN/expected-RED per Stage 6 lane disposition
A2-T builder: NOT APPOINTED (not required — no code change)
Sub-lane B governance: CLOSED
```

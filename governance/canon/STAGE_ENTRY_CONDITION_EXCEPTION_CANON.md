
**Status**: CANONICAL | **Version**: 1.0.0 | **Authority**: CS2
**Date**: 2026-04-27
**Canon ID**: SECC-001
**Issue**: app_management_centre#1139 — Hardening — PR handover must enforce governing-issue role separation, retire stale handover injectors, and block partial handover state

> **Amendment Authority**: Only CS2 (Johan Ras / repo owner) may amend this canon.
> Any PR modifying this file without CS2 sign-off is auto-FAIL at the merge gate.

---

# Stage Entry-Condition Exception Canon

## Purpose

This canon defines the **mandatory schema and governance rules** for recording when CS2
intentionally authorizes a stage to be produced before its normal entry condition is satisfied.

The goal is to prevent the recurring failure mode where:
- A stage is executed under a CS2-granted exception
- But the resulting artifacts do not explicitly record the exception posture
- Leading to a mixed "blocked but executed" repo state with no traceability
- And downstream review failing because the exception is implied, not stated

When an exception exists, it MUST be visible in the PR body, main artifact header, wave record,
and artifact index — not just in session notes or memory.

---

## 1. Normal Entry Conditions

### 1.1 The 12-Stage Pre-Build Model Entry Conditions

The following normal entry conditions apply to each stage in the 12-stage pre-build model.
A stage may not be initiated until its entry condition is met — unless an exception is
explicitly authorized by CS2 and recorded per §2.

| Stage | Name | Normal Entry Condition |
|-------|------|----------------------|
| 1 | App Description | CS2 authorization to begin the build |
| 2 | UX Workflow & Wiring Spec | Stage 1 (App Description) approved |
| 3 | Functional Requirements Specification | Stage 2 approved (mandatory for user-facing builds) |
| 4 | Technical Requirements Specification | Stage 3 (FRS) approved |
| 5 | Architecture Design | Stage 4 (TRS) approved |
| 6 | QA-to-Red (Red test suite) | Stage 5 (Architecture) approved |
| 7 | Pre-Build Functionality Assessment Gate (PBFAG) | Stages 1–6 complete; FM signed off on red suite |
| 8 | Implementation Plan | PBFAG (Stage 7) PASS |
| 9 | Builder Checklist | Stage 8 (Implementation Plan) approved |
| 10 | IAA Pre-Brief | Stage 9 (Builder Checklist) FM-signed |
| 11 | Builder Appointment | Stages 1–10 complete |
| 12 | Build | Builder Appointment confirmed (Stage 11) |

### 1.2 Parallel Production Entry Condition

Parallel waves (concurrent production of multiple stages) require an additional entry condition:
- **CS2 explicit authorization** for concurrent execution
- **Clear wave isolation boundaries** with no shared mutable state
- **Merge ordering pre-declared** before any parallel wave begins

---

## 2. Exception Authorization Schema

### 2.1 Required Schema Fields

When CS2 authorizes an exception to a normal entry condition, the following fields MUST
be recorded in the PR body, wave record section 1, and main artifact header:

```yaml
entry_condition_exception:
  normal_entry_condition: "[Exact description of the normally required prerequisite]"
  exception_authorized_by: "CS2 — #NNN [Issue reference or comment URL at which CS2 authorized]"
  exception_scope: "[Exactly which stage entry condition was bypassed, e.g., Stage 3 approval not yet obtained]"
  exception_reason: "[Why the exception was granted — business or governance justification]"
  parallel_production_authorized: "YES / NO"
  exception_changes_next_stage_gate: "YES — [how the next stage gate is affected] / NO"
  exception_recorded_in_artifact_chain: "YES"
```

### 2.2 Minimal Acceptable Exception Record

A minimal exception record MUST contain at least:
- `normal_entry_condition` — the specific prerequisite that was bypassed
- `exception_authorized_by` — a traceable CS2 reference (issue number or comment URL)
- `exception_scope` — exactly what was bypassed
- `exception_reason` — why

Without these four fields, the exception is **not adequately recorded** and the PR fails
the entry-condition check (SECC-VIOLATION-001).

### 2.3 Where the Exception Must Appear

An exception record MUST appear in ALL of the following locations:

| Location | Required Exception Content |
|----------|---------------------------|
| PR body `entry_condition_status` field | `EXCEPTION — [brief scope]` |
| Wave record section 1 | Full exception schema per §2.1 |
| Main artifact header | `entry_condition_status: EXCEPTION` + brief reference |
| Artifact index row | Exception noted in artifact status column |

If any of these locations is missing the exception record, the wave fails the
entry-condition parity check (SECC-VIOLATION-002).

---

## 3. Parallel Production Rules

### 3.1 Parallel Production Authorization

Parallel production of stages (producing multiple stages concurrently, not sequentially)
requires an **explicit, separate authorization** from the stage entry-condition exception.

Even if CS2 has authorized a stage under an entry-condition exception, parallel production
of *additional* stages requires a separate `parallel_production_authorized: YES` entry.

### 3.2 Parallel Production Records

When `parallel_production_authorized: YES`, the following MUST also be recorded:

```yaml
parallel_production:
  concurrent_stages: "[List stages being produced in parallel]"
  isolation_boundary: "[How shared mutable state is prevented between concurrent waves]"
  merge_order_declared: "YES — [Wave A merges before Wave B]"
  wave_isolation_verified_by: "Foreman / ECAP"
```

### 3.3 Parallel Production Failure Mode

If parallel production is underway but `parallel_production_authorized: NO` or the
record is absent:
- The PR MUST be flagged as SECC-VIOLATION-003
- The PR MUST NOT be merged until the parallel production authorization is documented
- The Foreman MUST escalate to CS2 to obtain retroactive authorization or halt the
  parallel wave

---

## 4. Pre-PR Checks for Entry-Condition Status

### 4.1 Producing Agent Responsibility

Before opening a PR as review-ready, the producing agent MUST:

1. Determine whether the stage was produced under normal entry conditions or an exception
2. If NORMAL: record `entry_condition_status: NORMAL` in the PR body and wave record
3. If EXCEPTION: populate the full exception schema (§2.1) in all required locations (§2.3)
4. Verify the exception posture is consistent across PR body, wave record, artifact header,
   and artifact index

### 4.2 Exception Consistency Check

The exception posture MUST be consistent across all four artifact surfaces listed in §2.3.
A PR where:
- The wave record says `EXCEPTION` but the PR body says `NORMAL`, OR
- The PR body says `EXCEPTION` but the artifact header does not reflect it

is a SECC-VIOLATION-002 failure.

### 4.3 Integration with Pre-PR Blocking Gate (PHCP-001)

`entry_condition_status` is a required field in the pre-PR blocking gate evidence
(see `PR_HANDOVER_CANONICAL_PACKAGE.md` §4.1). A PR cannot pass the pre-PR blocking
gate if `entry_condition_status` is absent or inconsistent across the artifact chain.

---

## 5. Violation Classes

| Code | Description | Severity | Blocker? |
|------|-------------|---------|---------|
| `SECC-VIOLATION-001` | Exception not adequately recorded (missing one or more of the four required minimal fields) | HIGH | YES — wave blocker |
| `SECC-VIOLATION-002` | Exception posture inconsistent across artifact surfaces (PR body, wave record, artifact header, artifact index) | HIGH | YES — wave blocker |
| `SECC-VIOLATION-003` | Parallel production underway without documented authorization | HIGH | YES — wave blocker |
| `SECC-VIOLATION-004` | `exception_changes_next_stage_gate: YES` declared but downstream gate not updated | MEDIUM | YES — next wave blocker |
| `SECC-MISSING-FIELD` | `entry_condition_status` field absent from PR body or wave record | HIGH | YES — pre-PR blocking gate FAIL |

---

## 6. ECAP and IAA Duties

### 6.1 ECAP Duty

When ECAP prepares the ceremony bundle, it MUST:
1. Check whether `entry_condition_status` is populated in the wave record section 1
2. If `EXCEPTION`: verify the full exception schema fields are present
3. Verify exception posture consistency across all four surfaces (§2.3)
4. Record exception verification result in the ECAP reconciliation summary (C2 field)
5. Flag any inconsistency to the Foreman before sign-off

### 6.2 IAA Duty

IAA MUST verify:
1. `entry_condition_status` is present and populated (not blank or placeholder)
2. If `EXCEPTION`: all four required schema fields are present and non-blank
3. Exception posture is consistent across PR body, wave record, artifact header, artifact index
4. If `parallel_production_authorized: YES`: parallel production record §3.2 is present

If any check fails: IAA issues REJECTION-PACKAGE citing the applicable SECC violation code.

---

## 7. Normal-Condition Acknowledgment

When entry conditions are fully met and no exception applies, the wave record MUST still
explicitly record:

```yaml
entry_condition_status: "NORMAL"
entry_condition_verified: "YES"
entry_condition_notes: "N/A"
```

**The `NORMAL` declaration is not implicit** — it must be stated. An absent
`entry_condition_status` field is treated the same as a missing exception record
and fails the pre-PR blocking gate.

---

## Appendix A: Quick-Reference Exception Check

Before opening a PR, verify:

```
✅ entry_condition_status populated in wave record section 1 (NORMAL or EXCEPTION)
✅ If EXCEPTION: all four required fields present (normal_entry_condition, exception_authorized_by, exception_scope, exception_reason)
✅ Exception posture consistent: PR body = wave record = artifact header = artifact index
✅ If parallel_production_authorized: YES → parallel_production record present
✅ entry_condition_status field present in pre-PR blocking gate evidence (PHCP-001 §4.1)
```

---

**Canon ID**: SECC-001
**Filed by**: foreman-v2-agent (POLC-Orchestration governance specification) | **Date**: 2026-04-27
**Authority**: CS2 — Issue #1139
**See also**: `PR_HANDOVER_CANONICAL_PACKAGE.md` (PHCP-001), `PRE_BUILD_STAGE_MODEL_CANON.md`


**Status**: CANONICAL | **Version**: 1.0.0 | **Authority**: CS2
**Date**: 2026-04-26
**Canon ID**: EWCS-001
**Issue**: app_management_centre#1143 — Hardening — Foreman/ceremony must enforce end-of-wave closeout sweep, tracker/header parity, and kickoff-state retirement

> **Amendment Authority**: Only CS2 (Johan Ras / repo owner) may amend this canon.
> Any PR modifying this file without CS2 sign-off is auto-FAIL at the merge gate.

---

# End-of-Wave Closeout Sweep Canon

## Purpose

This canon defines the **mandatory end-of-wave closeout sweep** — an explicit, named,
sequential governance step that must be completed and evidenced before any wave may be
marked as:

- `qp_verdict: PASS`
- approval-ready
- handover-ready
- merge-ready

The canon exists because AMC waves have repeatedly failed final review not on substantive
content quality, but on **wave-close execution discipline**: stale tracker headers, incomplete
wave checklists left in kickoff state, ceremony artifacts not reflecting final wave state, and
no single explicit pass over all control surfaces before handover.

This canon directly addresses the recurring pattern where:
1. The governing issue is correct
2. The main stage artifacts are correct
3. The tracker body is partly updated
4. But one or more control surfaces remain stale or kickoff-state

The result is a corrective cycle even when the substantive content is already good. This canon
closes that gap by making the closeout sweep a named, mandatory, sequenced governance step.

---

## 1. The Mandatory End-of-Wave Closeout Sweep

### 1.1 Definition

The **end-of-wave closeout sweep** is an **explicit, sequential, single-pass review** over
all control surfaces and ceremony artifacts performed immediately before the wave is declared
QP PASS / handover-ready.

The sweep is:
- **Explicit** — it is a named step, not an implied side-effect of other QP checks
- **Sequential** — each surface is checked one at a time in the order defined in §1.3
- **Blocking** — the wave MUST NOT be declared QP PASS until the sweep produces a PASS verdict
- **Evidenced** — the sweep result MUST be recorded in the wave record (see §5)

### 1.2 When to Execute

The closeout sweep is executed by the Foreman (or ECAP acting as ceremony admin) at:
- **Before QP verdict is recorded** in the wave record
- **Before the wave checklist is marked complete** (all items ticked)
- **Before the PR is opened or presented as merge-ready**

The sweep is executed once per wave at wave close. If any sweep item FAILS, the failing
surface must be corrected and the sweep re-run from the beginning.

### 1.3 Closeout Sweep Checklist (Minimum Required Surfaces)

The following surfaces MUST be checked, in this order, as part of every closeout sweep.
Each surface produces a PASS or FAIL result. A single FAIL blocks the sweep.

| # | Surface | What to Verify |
|---|---------|----------------|
| CS-01 | **PR body** | Contains correct governing issue reference; status fields reflect final wave state; no kickoff-state text remains |
| CS-02 | **Primary stage artifact header** | `governing_stage_issue`, `current_stage`, and authority fields updated; no stale issue reference |
| CS-03 | **Traceability artifact header** | If present: header fields match primary artifact header; no stale issue reference |
| CS-04 | **BUILD_PROGRESS_TRACKER header** | Top-of-file control fields (`Issue:`, `Last Updated`, `Updated By`) reflect the current governing wave and issue — see §2 for tracker header/body parity requirement |
| CS-05 | **BUILD_PROGRESS_TRACKER stage rows** | Stage summary row for the active stage matches the stage detail section; no mismatch between summary status and detail status |
| CS-06 | **Wave checklist** | All tasks ticked `[x]`; `qp_verdict` fields all show PASS (not PENDING); kickoff-state items retired per §3 |
| CS-07 | **Wave record** | Sections 1–4 fully populated; governing issue consistent with §1a; §3a parity evidence complete; §3b ceremony evidence complete |
| CS-08 | **Session memory** | `triggering_issue`, `outcome`, `coverage_summary`, `learning`, `wave_record_path` all populated; outcome reflects final result |
| CS-09 | **Sign-off / approval surface** | If applicable: approval record updated; `approval_reference` field in wave record populated if approval was obtained this wave |
| CS-10 | **AMC artifact index** | `AMC_PRE_BUILD_ARTIFACT_INDEX.md` or equivalent: stage row for the active stage updated to match tracker; governing issue aligned |

> **Note**: Surfaces CS-02, CS-03, CS-04, CS-05, CS-09, CS-10 are conditional — mark N/A
> (with reason) if the artifact does not exist or is explicitly out of scope for the current wave.
> CS-01, CS-06, CS-07, CS-08 are MANDATORY for every wave — they may not be N/A.

### 1.4 Sweep Verdict

- **PASS**: All required surfaces (non-N/A) verified with no failures
- **FAIL**: One or more required surfaces failed. The failing surface(s) must be corrected
  and the sweep re-run from CS-01 before the wave may proceed

---

## 2. Tracker Header/Body Parity — Distinct Binary Gate

### 2.1 Why This Is a Separate Gate

The GOVERNING_ISSUE_PARITY_PROTOCOL (GIPC-001) already enforces that the tracker references
the correct governing issue. This section adds a **separate and distinct** requirement: the
tracker's **header-level control fields** (top-of-file) must be consistent with the
tracker's **body/stage-detail content**.

This gate exists because a tracker can have its body correctly updated (stage rows, detail
sections) while the header still references an old wave, old issue, or old stage posture.
Such a tracker PASSES GIPC-001's governing-issue check but still represents a control-surface
defect that will trigger rejection at final review.

### 2.2 Tracker Header Fields

The following are the **tracker header fields** for the purposes of this gate:

| Field | Location | Description |
|-------|----------|-------------|
| `Issue:` | Top block | The GitHub issue number that authorized the most recent update |
| `Last Updated:` | Top block | The date of the most recent update |
| `Updated By:` | Top block | The wave/agent that most recently updated the tracker |
| Classification and status posture | Classification block | Any classification or status marker in the header block |

### 2.3 Tracker Body Fields

The following are the **tracker body fields** for the purposes of this gate:

| Field | Location | Description |
|-------|----------|-------------|
| Stage summary rows | `## Stage Summary` table | Status, notes, and governing issue references for each stage |
| Stage detail sections | `### Stage N — Name` | Status, key artifacts, completion dates, approval references |
| Blocker and next-action annotations | Any stage row or detail | Current blocker description, next-action requirement |

### 2.4 Parity Requirements

The tracker header and body MUST satisfy all of the following before the sweep may PASS:

1. **Issue reference parity**: The `Issue:` field in the header must reference the same
   governing wave issue that produced the most recent substantive body update.

2. **Stage posture parity**: The `Updated By:` field in the header must reference the same
   wave that updated the body stage rows. A header saying "wave X" while the body reflects
   "wave Y" is a PARITY FAIL.

3. **Active stage parity**: The most recent active stage in the stage summary table must
   match the stage posture implied by the header fields. Example: if the summary table shows
   Stage 4 as APPROVAL PENDING, the header must not still say "Stage 3 approved" without
   a corresponding Stage 4 status indicator.

4. **Blocker/next-action parity**: If the body records a blocker or next-action for a stage,
   the header must not describe a different posture (e.g., header says "ready to proceed"
   but body stage row says "BLOCKED — requires CS2 approval").

### 2.5 Tracker Header/Body Parity Gate Verdict

- **PASS**: Header fields and body content describe the same stage posture, same governing
  wave, same blocker/next-action posture.
- **FAIL**: Any parity requirement in §2.4 is not met.

A tracker whose body is current but whose header still points at an old stage, old wave, or
old governing issue MUST FAIL this gate.

### 2.6 Relationship to GIPC-001

This gate is **additive** to GIPC-001 §4. GIPC-001 checks that the tracker references the
correct governing issue. This gate additionally checks that the tracker header and body
are internally consistent. Both gates must PASS.

---

## 3. Kickoff-State Retirement Rule for Wave Checklists

### 3.1 Definition of Kickoff State

A wave checklist is in **kickoff state** if any of the following conditions are true:

- Any task shows `[ ]` (unchecked) at wave close
- Any task shows `qp_verdict: PENDING` at wave close
- The checklist has no final-state summary or wave-close annotation
- The checklist shows no evidence that all tasks were QP-evaluated
- The checklist was created from a template and template placeholders remain

### 3.2 Retirement Requirement

Before the closeout sweep may PASS (CS-06), every wave checklist created at or during wave
kickoff MUST be **converted to close state**. Close state means:

1. All completed tasks are ticked: `[x]`
2. All `qp_verdict` fields show `PASS` or `DESCOPED` (with documented reason)
3. No `qp_verdict: PENDING` remains
4. A wave-close summary annotation is appended (see §3.3)
5. Any task removed or deferred mid-wave is marked `[~]` with a documented reason
   (silent task removal is prohibited)

### 3.3 Wave-Close Summary Annotation

When converting a checklist from kickoff state to close state, append the following block
at the end of the checklist file:

```markdown
---

## Wave Close Summary

**Closed**: [YYYY-MM-DD]
**Closed by**: [agent-id]
**QP Verdict**: PASS
**All tasks ticked**: YES
**Pending tasks at close**: NONE
**Descoped tasks**: [list with reason, or NONE]
**Deferred tasks**: [list with target wave, or NONE]
**Closeout sweep performed**: YES — see wave record §3c
```

### 3.4 Kickoff-State Checklist = Wave Blocker

A wave checklist that remains in kickoff state at handover is treated as a **blocking defect**,
equivalent in severity to a missing PREHANDOVER proof. This is true even if:

- The wave record says QP PASS
- The PREHANDOVER proof is present
- IAA has not yet been invoked

A kickoff-state checklist detected by ECAP or IAA after the Foreman has declared handover-
ready is an ECAP-001 protocol failure (CCI-03 violation — stale PENDING wording in a
final-state artifact).

---

## 4. Explicit Control-Surface Closeout Checklist

### 4.1 Purpose

The control-surface closeout checklist is a **reusable, sequenced checklist** for final-state
verification of control surfaces. It is executed as the last step of the closeout sweep,
after the individual surface checks (§1.3).

This checklist replaces ad-hoc reviewer habits with a structured, machine-checkable pass.

### 4.2 Control-Surface Closeout Checklist

```
## Control-Surface Closeout Checklist

### Tracker Parity (EWCS-001 §2)
- [ ] CS-T1: Tracker header `Issue:` field updated to current governing wave issue
- [ ] CS-T2: Tracker header `Last Updated:` field reflects today's date
- [ ] CS-T3: Tracker header `Updated By:` field references the current wave
- [ ] CS-T4: Tracker body stage summary row for active stage matches detail section
- [ ] CS-T5: Tracker header posture matches body blocker/next-action posture
- [ ] Tracker Header/Body Parity Gate: PASS | FAIL

### Wave Checklist (EWCS-001 §3)
- [ ] CS-C1: All tasks ticked [x]
- [ ] CS-C2: All qp_verdict fields show PASS or DESCOPED (none show PENDING)
- [ ] CS-C3: Wave-close summary annotation appended (see §3.3 template)
- [ ] CS-C4: No template placeholders remain in the checklist
- [ ] Kickoff-State Retirement: COMPLETE | INCOMPLETE

### Session Memory (EWCS-001 §1.3 CS-08)
- [ ] CS-M1: triggering_issue matches governing stage issue
- [ ] CS-M2: outcome field populated (COMPLETE / PARTIAL / ESCALATED)
- [ ] CS-M3: coverage_summary populated (not blank, not placeholder)
- [ ] CS-M4: learning field populated (mandatory — never blank)
- [ ] CS-M5: wave_record_path populated and correct

### Artifact Index (EWCS-001 §1.3 CS-10)
- [ ] CS-A1: AMC_PRE_BUILD_ARTIFACT_INDEX.md stage row updated (or N/A — reason: ___)
- [ ] CS-A2: Governing issue in index matches tracker governing issue (or N/A)

### PR Body (EWCS-001 §1.3 CS-01)
- [ ] CS-P1: CS2 authorization reference = governing stage issue
- [ ] CS-P2: IAA result field populated (ASSURANCE-TOKEN reference, or N/A pre-IAA)
- [ ] CS-P3: Wave record path included
- [ ] CS-P4: Wave checklist status = all ticked / documented justification for any exceptions
- [ ] CS-P5: QP verdict = PASS
- [ ] CS-P6: Parity check verdict = PASS

### Sign-off / Approval
- [ ] CS-S1: approval_reference in wave record blank (if no approval yet) or populated (if approval received this wave)
- [ ] CS-S2: If approval received: sign-off artifact updated and path recorded in wave record

### Overall Closeout Verdict
- [ ] All required control surfaces verified
- [ ] Tracker Header/Body Parity Gate: PASS
- [ ] Kickoff-State Retirement: COMPLETE
- [ ] **CLOSEOUT SWEEP VERDICT**: PASS | FAIL
```

---

## 5. Ceremony Evidence of Closeout Sweep

### 5.1 Mandatory Ceremony Evidence Fields

The wave record MUST explicitly record that the closeout sweep was performed. All five labeled
fields below MUST be populated in the wave record **before QP PASS is declared**.

| Field | Location | Required Value |
|-------|----------|----------------|
| `closeout_sweep_performed` | Wave record §3c | YES / FAIL — [reason] |
| `tracker_header_parity_verified` | Wave record §3c | PASS / FAIL / N/A — [reason] |
| `tracker_body_parity_verified` | Wave record §3c | PASS / FAIL / N/A — [reason] |
| `wave_checklist_retired_from_kickoff_state` | Wave record §3c | YES / NO — [reason if NO] |
| `control_surfaces_finalized` | Wave record §3c | YES / PARTIAL — [list incomplete surfaces] |

### 5.2 Evidence Completeness Requirement

A wave with any of the following conditions MUST NOT be declared QP PASS or handover-ready:

- `closeout_sweep_performed` is blank or shows FAIL
- `tracker_header_parity_verified` is blank, PENDING, or FAIL
- `tracker_body_parity_verified` is blank, PENDING, or FAIL
- `wave_checklist_retired_from_kickoff_state` is NO or blank
- `control_surfaces_finalized` is PARTIAL

### 5.3 ECAP Duty for Closeout Sweep Evidence

When ECAP prepares the ceremony bundle, it MUST additionally:

1. Verify the wave record §3c contains all five labeled fields (§5.1) as non-blank entries
2. Verify `closeout_sweep_performed = YES`
3. Verify `tracker_header_parity_verified = PASS` (or N/A with documented reason)
4. Verify `wave_checklist_retired_from_kickoff_state = YES`
5. Verify `control_surfaces_finalized = YES`

If any field is blank, FAIL, or PARTIAL: record as C1 failure in the ECAP reconciliation
summary and return the bundle to the producing agent for correction.

### 5.4 IAA Assurance Check for Closeout Sweep Evidence

IAA MUST, as part of its standard audit, verify:

1. The wave record §3c contains all five labeled fields from §5.1
2. `closeout_sweep_performed = YES` — not blank, not FAIL
3. `wave_checklist_retired_from_kickoff_state = YES` — not NO, not blank
4. No surface in §1.3 Mandatory surfaces (CS-01, CS-06, CS-07, CS-08) shows FAIL or N/A

If any check FAILS: IAA MUST issue REJECTION-PACKAGE citing EWCS-CLOSEOUT-INCOMPLETE.

---

## 6. Fail Conditions for Partial Control-Surface Completion

### 6.1 Definition

A wave MUST fail the closeout sweep (and therefore MUST NOT be declared QP PASS, approval-
ready, handover-ready, or merge-ready) if substantive artifacts are complete but control
surfaces are only **partially** updated.

### 6.2 Specific Fail Conditions

The following are **explicit fail conditions** — each individually blocks the wave:

| Fail ID | Condition | Fail Type |
|---------|-----------|-----------|
| EWCS-FAIL-01 | Tracker body updated but tracker header (`Issue:`, `Updated By:`) still references an old wave or old issue | Tracker Header/Body Parity FAIL |
| EWCS-FAIL-02 | Tracker header updated but tracker body stage rows still reflect old stage posture or old governing issue | Tracker Header/Body Parity FAIL |
| EWCS-FAIL-03 | Wave record shows QP PASS but wave checklist still shows `qp_verdict: PENDING` for any task | Kickoff-State Retirement FAIL |
| EWCS-FAIL-04 | Wave record shows QP PASS but wave checklist still has unchecked `[ ]` tasks at wave close | Kickoff-State Retirement FAIL |
| EWCS-FAIL-05 | PR body says complete but stage control document (artifact header) still references an old governing issue | GIPC-001 Parity FAIL (also a closeout sweep FAIL) |
| EWCS-FAIL-06 | Sign-off surface updated but tracker not aligned to the same stage/governing issue | Cross-Surface Parity FAIL |
| EWCS-FAIL-07 | Session memory `outcome` is COMPLETE but wave checklist tasks show PENDING | Cross-Artifact Consistency FAIL |
| EWCS-FAIL-08 | Closeout sweep §3c evidence fields not populated in wave record | Ceremony Evidence FAIL |
| EWCS-FAIL-09 | Artifact index not updated when a stage artifact was produced or modified this wave | Control-Surface Update Obligation FAIL |
| EWCS-FAIL-10 | Any mandatory sweep surface (CS-01, CS-06, CS-07, CS-08) returned N/A without documented justification | Surface Coverage FAIL |

### 6.3 Partial Completion is Not Progress

The "almost done, one more correction" pattern MUST be stopped by this canon. Specifically:

> A wave that has completed all substantive artifacts but has even **one** stale or
> kickoff-state control surface MUST fail the closeout sweep. There is no "partial PASS"
> or "pass with known exceptions" for control-surface defects.

This rule exists because:
- Every stale control surface triggers a correction cycle on an otherwise-complete wave
- Stale surfaces are a first-pass failure, not a post-merge cleanup item
- The discipline of first-pass control-surface finalization is exactly as important as
  first-pass substantive content quality

---

## 7. Relationship to Existing Governance

### 7.1 Relationship to GIPC-001 (Governing-Issue Parity Protocol)

| Concern | Governed By |
|---------|------------|
| Governing issue consistent across all artifact surfaces | GIPC-001 §2 |
| Tracker references correct governing issue | GIPC-001 §4 |
| Artifact index references correct governing issue | GIPC-001 §4 |
| **Tracker header/body internal parity** | **EWCS-001 §2 (new)** |
| **Kickoff-state retirement for wave checklists** | **EWCS-001 §3 (new)** |
| **Explicit closeout sweep as a named step** | **EWCS-001 §1 (new)** |
| Ceremony evidence fields for governing-issue parity | GIPC-001 §6 |
| **Ceremony evidence fields for closeout sweep** | **EWCS-001 §5 (new)** |

Both GIPC-001 and EWCS-001 MUST PASS before QP PASS is declared. They are complementary,
not overlapping.

### 7.2 Relationship to ECAP-001 (Execution Ceremony Administration Protocol)

ECAP-001 §3.6 CCI-03 prohibits stale PENDING wording in final-state artifacts. EWCS-001 §3
(kickoff-state retirement) makes this rule concrete and specific for wave checklists.

ECAP-001 §3.5 (final-state normalization) requires coherent final-state story. EWCS-001 §4
(control-surface closeout checklist) makes this requirement sequential and traceable.

### 7.3 Relationship to Wave Reconciliation Checklist (WRC-001)

The Wave Reconciliation Checklist (`wave-reconciliation-checklist.md`) addresses post-wave
incident capture, NBR registry sync, liveness status, and evidence completeness. EWCS-001
is **additive** — it adds the closeout sweep as a separate mandatory step focused on
control-surface finalization.

The WRC Section E (added per EWCS-001) integrates both the closeout sweep and the
tracker/header parity check into the unified wave-close workflow.

---

## Appendix A: Closeout Sweep Quick Reference

```
Before every QP PASS, run the closeout sweep:

CS-01 ✅ PR body — governing issue correct; no kickoff-state text
CS-02 ✅ Primary artifact header — governing issue + stage correct
CS-03 ✅ Traceability artifact header — matches primary (if exists)
CS-04 ✅ Tracker header — Issue:, Last Updated:, Updated By: reflect current wave
CS-05 ✅ Tracker body — stage summary matches stage detail; no header/body mismatch
CS-06 ✅ Wave checklist — all ticked; no PENDING; wave-close summary appended
CS-07 ✅ Wave record — §1a, §3a, §3b, §3c all populated
CS-08 ✅ Session memory — all fields populated; outcome reflects final result
CS-09 ✅ Sign-off surface — aligned (if applicable)
CS-10 ✅ Artifact index — stage row updated (if applicable)

Wave record §3c evidence:
✅ closeout_sweep_performed: YES
✅ tracker_header_parity_verified: PASS | N/A
✅ tracker_body_parity_verified: PASS | N/A
✅ wave_checklist_retired_from_kickoff_state: YES
✅ control_surfaces_finalized: YES
```

---

## Appendix B: Violation Classes

| Violation Class | Description |
|-----------------|-------------|
| EWCS-CLOSEOUT-INCOMPLETE | Closeout sweep not performed or §3c evidence fields missing/blank |
| EWCS-TRACKER-PARITY-FAIL | Tracker header and body describe different stage/wave/issue posture |
| EWCS-CHECKLIST-KICKOFF-STATE | Wave checklist left in kickoff state (unchecked tasks or PENDING verdicts) at handover |
| EWCS-SURFACE-PARTIAL | One or more control surfaces incomplete while others show final state |
| EWCS-CEREMONY-EVIDENCE-MISSING | Wave record §3c not populated with all five labeled closeout evidence fields |

---

**Canon ID**: EWCS-001
**Filed by**: foreman-v2-agent (POLC-Orchestration governance specification) | **Date**: 2026-04-26
**Authority**: CS2 — Issue #1143

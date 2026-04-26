
**Status**: CANONICAL | **Version**: 1.0.0 | **Authority**: CS2
**Date**: 2026-04-23
**Canon ID**: GIPC-001
**Issue**: app_management_centre#1129 — Hardening — Foreman/ceremony must enforce governing-issue parity and issue-role separation across the full artifact chain

> **Amendment Authority**: Only CS2 (Johan Ras / repo owner) may amend this canon.
> Any PR modifying this file without CS2 sign-off is auto-FAIL at the merge gate.

---

# Governing-Issue Parity Protocol

## Purpose

This protocol defines the **mandatory checks and labeled field requirements** that enforce
governing-issue identity integrity across the full artifact chain of a stage wave. It addresses
the recurring failure mode where a stage kickoff issue is correct, but produced artifacts drift
and start citing a later hardening, harmonization, or continuous-improvement issue as the
governing authority.

> **Key invariant**: The stage kickoff issue that authorized the wave is the governing issue
> for every artifact in that wave's artifact chain. This identity MUST remain stable from
> wave kickoff through PR merge. A wave MUST NOT pass if any artifact in the chain cites a
> different issue as the governing authority without an explicit, documented supersession rule.

---

## 1. Issue-Role Separation

### 1.1 Issue Role Taxonomy

Every GitHub issue that interacts with a stage wave MUST be classified into exactly one of
the following roles:

| Role | Description | May populate governing_stage_issue? |
|------|-------------|-------------------------------------|
| **Stage Kickoff Issue** | The issue that authorized and defined the scope of this stage wave. Opened (or explicitly delegated) by CS2. | ✅ YES — this is the only valid value for `governing_stage_issue` |
| **Approval Reference** | An issue or comment that records the approval decision for a stage artifact. | ❌ NO — populate `approval_reference` only |
| **Hardening Issue** | An issue whose primary objective is strengthening, tightening, or adding enforcement to an already-delivered artifact or protocol. Usually titled with "Hardening —" prefix. | ❌ NO — populate `related_hardening_issue` only |
| **Harmonization Issue** | An issue whose primary objective is aligning inconsistency across multiple artifacts or modules. Usually titled with "Harmonization —" or "Alignment —" prefix. | ❌ NO — populate `related_harmonization_issue` only |
| **Continuous-Improvement Issue** | An issue that improves tooling, governance, or workflow without changing the stage artifact's approved content. | ❌ NO — do not populate any governing authority field |
| **Sub-Issue / Child Issue** | An issue created to track a specific task within a parent stage wave. | ❌ NO — the parent Stage Kickoff Issue remains the governing issue |

### 1.2 Classification Rules

1. A hardening issue (even one directly related to the current stage wave's artifacts) is
   **never** the governing issue for the original wave's artifact chain.

2. A harmonization issue that was opened *after* the stage kickoff issue is never the
   governing issue, even if it touches the same artifacts.

3. An approval reference is *not* the governing issue — it records the approval event but
   does not replace the kickoff issue as the chain's authority.

4. If a later issue *explicitly supersedes* the original stage kickoff issue (CS2 records
   a supersession decision in writing), the new issue becomes the governing issue only after
   the supersession is documented. A supersession MUST be explicitly stated — it cannot be
   inferred from the fact that the newer issue is related.

### 1.3 Overshadow Prohibition

**Definition**: "Overshadow" occurs when a later issue (hardening, harmonization, or CI)
is used in place of the original Stage Kickoff Issue in artifact authority fields, PR body,
or ceremony artifacts — without an explicit supersession decision.

Overshadow is prohibited. The following artifact fields MUST contain the Stage Kickoff Issue
number, not a later related issue:

- `governing_stage_issue` in wave records, stage artifact headers, PREHANDOVER proofs
- `triggering_wave_issue` in wave records
- The CS2 authorization field in wave checklists
- The governing issue in PR body "CS2 authorization reference"

---

## 2. Mandatory Governing-Issue Parity Check

### 2.1 Parity Check Definition

Before a wave may be marked approval-ready / QP PASS, the system (Foreman + ECAP + IAA)
MUST verify that the **same Stage Kickoff Issue** appears consistently as the governing
authority across every artifact in the wave's artifact chain.

### 2.2 Minimum Artifact Chain Coverage

The parity check MUST verify the following surfaces at minimum:

| Surface | Field to Check | Expected Value |
|---------|----------------|----------------|
| **PR body** | CS2 authorization reference | Stage Kickoff Issue number |
| **Wave record section 1** | `triggering_issue` | Stage Kickoff Issue number |
| **Wave checklist** | Authority line | Stage Kickoff Issue number |
| **Main stage artifact header** | `governing_stage_issue` or authority field | Stage Kickoff Issue number |
| **Traceability artifact header** | `governing_stage_issue` or authority field | Stage Kickoff Issue number (if traceability artifact exists) |
| **Build progress tracker** | Governing issue citation (if present) | Stage Kickoff Issue number |
| **Artifact index / pre-build artifact index** | Governing issue citation (if present) | Stage Kickoff Issue number |
| **Sign-off / approval record** | Triggering issue reference | Stage Kickoff Issue number |
| **PREHANDOVER proof** | `governing_stage_issue` field | Stage Kickoff Issue number |
| **Session memory** | `triggering_issue` field | Stage Kickoff Issue number |

### 2.3 Parity Check Binary Gate

Parity check is a **binary gate**:

- **PASS**: All surfaces in §2.2 cite the same Stage Kickoff Issue number as the governing
  authority. Wave may proceed to IAA.
- **FAIL**: Any surface in §2.2 cites a different issue number (hardening, harmonization,
  approval, or other) as the governing authority. Wave MUST be halted; all non-conforming
  surfaces must be corrected before re-running the parity check.

A parity check FAIL is a wave blocker. It is not a post-merge cleanup item.

### 2.4 Parity Check Evidence

The producing agent MUST record parity check results in the PREHANDOVER proof:

```
governing_issue_parity_check:
  governing_stage_issue: "#NNN"
  surfaces_verified:
    - pr_body: PASS
    - wave_record_triggering_issue: PASS
    - wave_checklist_authority: PASS
    - main_artifact_header: PASS
    - traceability_artifact_header: PASS | N/A
    - build_progress_tracker: PASS | N/A
    - artifact_index: PASS | N/A
    - sign_off_record: PASS | N/A
    - prehandover_proof: PASS
    - session_memory: PASS
  parity_verdict: PASS | FAIL
  overshadow_detected: NO | YES — [issue number that was incorrectly used]
```

---

## 3. Mandatory Labeled Authority Fields

### 3.1 Required Fields for Stage Artifacts

Free-form authority lines are no longer sufficient for stage wave artifacts. Every new
or significantly updated stage artifact header MUST use the following explicitly labeled fields:

| Field | Required | Description |
|-------|----------|-------------|
| `governing_stage_issue` | **MANDATORY** | The Stage Kickoff Issue number (e.g., `#1129`). Never blank. Must be the issue that authorized this specific wave. A kickoff issue with a "Hardening —" or "Harmonization —" title is valid when it is the issue that opened this wave. What is prohibited is substituting a *later follow-on* hardening/harmonization issue (opened after the wave started) in place of the original kickoff issue — that constitutes overshadow (§5). |
| `triggering_wave_issue` | **MANDATORY** | Same as `governing_stage_issue` unless an explicit supersession rule applies. |
| `current_stage` | **MANDATORY** | The 12-stage pre-build stage this artifact belongs to (e.g., `Stage 1 — App Description`). |
| `next_stage_blocked_by` | Conditional | What must be true before the next stage begins. Blank if no explicit blocker. |
| `approval_reference` | Conditional | Issue number or URL where approval was recorded. Blank until actual approval exists. Never pre-populated with the Stage Kickoff Issue. |
| `related_hardening_issue` | Optional | Issue number of any directly related hardening issue. Cited for traceability only — NOT as a governing authority. |
| `related_harmonization_issue` | Optional | Issue number of any directly related harmonization issue. Cited for traceability only. |

### 3.2 Field Population Rules

1. `governing_stage_issue` MUST be populated at wave kickoff and MUST NOT change during
   the wave unless an explicit supersession decision is recorded.

2. `approval_reference` MUST be blank until the approval event actually occurs. A field
   pre-populated with a Stage Kickoff Issue number is a violation — the kickoff issue is
   the authorization, not the approval record.

3. `related_hardening_issue` and `related_harmonization_issue` are citation fields only.
   Their presence does not grant those issues any governing authority over the artifact chain.

4. These fields apply to: stage artifact headers, PREHANDOVER proofs, wave records, and
   any artifact that carries a "governing authority" declaration.

### 3.3 Wave Record Template Authority Fields (Minimum Required)

Wave records MUST include the following authority section in addition to the existing
wave identity table:

```markdown
## Governing Authority

| Field | Value |
|-------|-------|
| governing_stage_issue | [#NNN — title] |
| triggering_wave_issue | [#NNN — same as governing_stage_issue unless superseded] |
| current_stage | [Stage N — Name] |
| next_stage_blocked_by | [blocker description or N/A] |
| approval_reference | [blank — fill when approval exists] |
| related_hardening_issue | [#NNN or N/A] |
| related_harmonization_issue | [#NNN or N/A] |
```

---

## 4. Tracker and Control-Surface Parity as a Binary Gate

### 4.1 Control Surfaces Defined

The following repository control surfaces are **first-class wave deliverables**, not optional
post-processing items:

| Surface | File Pattern |
|---------|-------------|
| **Build Progress Tracker** | `build-progress-tracker-*.md`, `*-tracker.md` |
| **Artifact Index** | `pre-build-artifact-index-*.md`, `artifact-index-*.md` |
| **Sign-off / Approval Record** | `approval-record-*.md`, `sign-off-*.md` |

### 4.2 Control-Surface Parity Requirements

A wave MUST NOT be declared COMPLETE unless:

1. The build progress tracker matches the actual stage posture at wave close.
2. The artifact index matches tracker posture (same stage, same governing issue).
3. The sign-off / approval posture matches both tracker and artifact index.
4. The governing issue reference is consistent across all three surfaces.

### 4.3 Control-Surface Parity Gate

This gate is evaluated as part of §2.2 parity check. Specifically:

- If the build progress tracker references a different issue from the Stage Kickoff Issue:
  **PARITY FAIL**
- If the artifact index references a different issue: **PARITY FAIL**
- If tracker and artifact index are inconsistent with each other: **PARITY FAIL**
- If control surfaces were not updated as part of the wave: **PARITY FAIL** (unless
  explicitly scoped out by CS2 with documented justification)

### 4.4 Control-Surface Update Obligation

Every wave that produces or modifies a stage artifact MUST update the corresponding
control surfaces as part of the wave deliverable. The PREHANDOVER proof MUST include:

```
control_surfaces_updated:
  build_progress_tracker: UPDATED | NOT_APPLICABLE — [reason]
  artifact_index: UPDATED | NOT_APPLICABLE — [reason]
  sign_off_record: UPDATED | NOT_APPLICABLE — [reason if no sign-off yet]
```

---

## 5. Recent-Authority Overshadow Detection

### 5.1 Overshadow Pattern Definition

The following pattern constitutes a **Recent-Authority Overshadow**:

> A wave is kicked off under Stage Kickoff Issue #A. During or after execution, a related
> issue #B is opened (titled with "Hardening —", "Harmonization —", "Alignment —", or
> "Continuous Improvement —"). Artifacts produced during the wave begin citing #B as the
> governing issue instead of #A, without any supersession decision.

### 5.2 Overshadow Detection Rule

Before recording `governing_stage_issue` in any artifact, verify:

1. Is the issue number being used the original Stage Kickoff Issue that authorized this wave?
2. If a different (newer) issue is being used, is it titled or classified as hardening,
   harmonization, alignment, or continuous improvement?
3. Does the original Stage Kickoff Issue explicitly state it is superseded by the newer issue?

If (2) is TRUE and (3) is FALSE: **OVERSHADOW DETECTED — halt and correct.**

### 5.3 Overshadow Detection Checklist (mandatory pre-QP)

Before QP evaluation, the Foreman MUST run the following overshadow detection check:

```
Overshadow Detection Check:
1. Identify the Stage Kickoff Issue number: #___
2. Is this issue numbered lower than any related issue referenced in artifacts? YES/NO
3. If YES: for each higher-numbered referenced issue:
   a. Title check — does it contain "Hardening", "Harmonization", "Alignment", or
      "Continuous Improvement"? YES/NO
   b. If YES: did the Stage Kickoff Issue explicitly say it is superseded? YES/NO
   c. If YES to (a) and NO to (b): OVERSHADOW DETECTED — reject, correct, re-verify.
4. Overshadow status: CLEAN | DETECTED — [issue number]
```

### 5.4 Wave Failure on Overshadow

If overshadow is detected at any review layer (Foreman QP, ECAP, or IAA), the wave MUST:

1. Halt immediately.
2. Identify all artifacts that cite the incorrect issue.
3. Correct every affected artifact to cite the Stage Kickoff Issue.
4. Re-run the full §2.2 parity check.
5. Re-run the §5.3 overshadow detection check to confirm clean.
6. Only then may the wave proceed to the next review layer.

---

## 6. Ceremony and Wave Artifact Enforcement

### 6.1 Mandatory Ceremony Evidence Fields

The ceremony layer (wave record + wave checklist + ECAP artifacts) MUST explicitly record
the following for every wave:

| Field | Where | Description |
|-------|-------|-------------|
| `governing_stage_issue` | Wave record §1 | Stage Kickoff Issue number |
| `related_hardening_issue` | Wave record §1 (new field) | Any directly related hardening issue, or N/A |
| `related_harmonization_issue` | Wave record §1 (new field) | Any directly related harmonization issue, or N/A |
| `approval_exists` | Wave record §1 (new field) | YES / NO / PENDING — whether formal approval has been recorded |
| `parity_check_performed` | Wave record §3 | PASS / FAIL / N/A |
| `overshadow_check_performed` | Wave record §3 | CLEAN / DETECTED / N/A |
| `control_surfaces_verified` | Wave record §3 | YES / N/A — whether tracker/index/sign-off surfaces were checked |

### 6.2 Ceremony Completeness Invariant

A wave ceremony package is incomplete if any of the following are absent or unverified:

- `governing_stage_issue` is blank or points to a *later follow-on* hardening/harmonization issue instead of the issue that authorized this wave
- `parity_check_performed` is blank or PENDING
- `overshadow_check_performed` is blank or not recorded
- `control_surfaces_verified` is blank when control surfaces exist for this stage

An incomplete ceremony package is a handover blocker equivalent to a missing PREHANDOVER proof.

### 6.3 ECAP Ceremony Duty (ECAP-001 Extension)

When ECAP (execution-ceremony-admin-agent) prepares the ceremony bundle, it MUST additionally:

1. Verify `governing_stage_issue` in the wave record matches `triggering_issue`.
2. Verify the same issue number appears in the PR body authority field.
3. Run the §5.3 overshadow detection check and record the result.
4. Confirm §2.2 parity check evidence is present in the PREHANDOVER proof.
5. Flag any discrepancy to the Foreman before the ceremony bundle is signed off.

If ECAP finds a governing-issue discrepancy: record as C1 failure in the ECAP reconciliation
summary and return the bundle to the producing agent for correction.

### 6.4 IAA Assurance Check for Governing-Issue Parity (ACR Extension)

IAA MUST, as part of its standard audit, verify:

1. The `governing_stage_issue` field is present and non-blank in: wave record, PREHANDOVER proof.
2. The issue number in `governing_stage_issue` matches the issue that authorized the wave.
3. The issue in `governing_stage_issue` is the one that authorized this specific wave — it is not a *later related* issue (hardening, harmonization, or CI) that was opened after this wave was kicked off.
4. The §2.4 parity check evidence block is present in the PREHANDOVER proof.
5. No *later* hardening/harmonization/CI issue (opened after wave kickoff) is used as the governing authority anywhere in the chain.

If any of these checks FAIL: IAA MUST issue REJECTION-PACKAGE citing GIP-PARITY-FAIL.

---

## Appendix A: Quick-Reference Parity Check Card

```
Before every QP PASS, verify:
✅ governing_stage_issue in wave record = #[kickoff issue]
✅ governing_stage_issue in PREHANDOVER proof = #[kickoff issue]
✅ PR body CS2 auth reference = #[kickoff issue]
✅ Wave checklist authority = #[kickoff issue]
✅ Main artifact header = #[kickoff issue]
✅ No newer hardening/harmonization issue used in place of #[kickoff issue]
✅ Control surfaces updated to match #[kickoff issue]
```

---

## Appendix B: Violation Classes

| Violation Class | Description |
|-----------------|-------------|
| GIP-PARITY-FAIL | Governing issue differs across one or more surfaces in the §2.2 artifact chain |
| GIP-OVERSHADOW-001 | A hardening/harmonization/CI issue used as governing authority without explicit supersession |
| GIP-FIELD-MISSING | A mandatory labeled authority field (§3.1) is absent from a stage artifact |
| GIP-CONTROL-SURFACE-SKIP | Tracker/index/sign-off surface not updated as part of the wave deliverable |
| GIP-CEREMONY-INCOMPLETE | Wave ceremony package is missing parity or overshadow check evidence (§6.2) |

---

## Appendix C: Relationship to EWCS-001 (End-of-Wave Closeout Sweep Canon)

This protocol (GIPC-001) and `END_OF_WAVE_CLOSEOUT_SWEEP_CANON.md` (EWCS-001) are
**complementary and both required**. They govern different but related failure modes:

| Concern | Governed By |
|---------|------------|
| Governing issue consistent across all artifact surfaces | **GIPC-001 §2** |
| Tracker references correct governing issue | **GIPC-001 §4** |
| Tracker header/body **internal** parity | **EWCS-001 §2** |
| Wave checklist kickoff-state retirement | **EWCS-001 §3** |
| Explicit closeout sweep as a named mandatory step | **EWCS-001 §1** |
| Ceremony evidence fields for closeout sweep | **EWCS-001 §5** |
| Partial control-surface completion fail conditions | **EWCS-001 §6** |

GIPC-001 governs **cross-artifact governing-issue consistency**.
EWCS-001 governs **intra-artifact consistency and closeout-state finalization**.

Both MUST PASS before QP PASS is declared. They are not alternatives.

---

**Canon ID**: GIPC-001
**Filed by**: foreman-v2-agent (POLC-Orchestration governance specification) | **Date**: 2026-04-23
**Authority**: CS2 — Issue #1129
**See also**: `governance/canon/END_OF_WAVE_CLOSEOUT_SWEEP_CANON.md` (EWCS-001) — Issue #1143

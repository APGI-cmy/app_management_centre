
**Status**: CANONICAL | **Version**: 1.0.0 | **Authority**: CS2
**Date**: 2026-04-27
**Canon ID**: WRCC-001
**Issue**: app_management_centre#1143 — Hardening — pre-PR gate must enforce wave-result coherence, checklist close-state, and truthful §3c handover evidence

> **Amendment Authority**: Only CS2 (Johan Ras / repo owner) may amend this canon.
> Any PR modifying this file without CS2 sign-off is auto-FAIL at the merge gate.

---

# Wave Result Coherence Canon

## Purpose

This canon defines the **wave-result-state coherence invariants** that MUST hold at
producer-side before any wave may be opened as PR-review-ready.

It exists to stop the specific failure class where one or more producer-side control
surfaces are allowed to contradict each other at handover:

- wave-record Section 5 simultaneously claiming PASS/token-issued AND retaining active
  rejection/fix-required language,
- wave checklist remaining in kickoff/PENDING state while the wave record claims all tasks
  complete and QP PASS,
- §3c handover evidence claiming self-consistency or PASS while the actual artifact set
  still contradicts that claim.

**These are producer-side gating failures.** They MUST be caught before PR handover — not
discovered by downstream review.

**Governing basis**: EWCS-001 §6 already defines partial control-surface completion as a
failure class. PHCP-001 §4 defines the pre-PR blocking gate. This canon operationalizes
both into explicit, machine-checkable coherence gates for the three critical surfaces.

---

## 1. Final-Assurance State Coherence Gate

### 1.1 Purpose

The wave-record Section 5 (Assurance) MUST resolve to exactly **one** valid final state
before the PR may be opened as review-ready. A Section 5 that simultaneously exhibits PASS
and REJECTION posture is a **coherence violation** and a blocking defect.

### 1.2 Allowed Final States (Exactly One Must Be Active)

| State | Indicator | Description |
|-------|-----------|-------------|
| `ASSURANCE_TOKEN_ISSUED` | `PHASE_B_BLOCKING_TOKEN: IAA-session-NNN-YYYYMMDD-PASS` present | IAA issued PASS; no rejection language active |
| `REJECTION_PACKAGE_ACTIVE` | Rejection/fix-required language present; no valid token | IAA issued rejection or fix required; re-invocation pending |

A Section 5 that contains indicators from **both** states simultaneously is an
incoherent final-assurance state and is prohibited.

### 1.3 Coherence Rule — PASS State

If Section 5 claims `ASSURANCE_TOKEN_ISSUED` (i.e., a valid `PHASE_B_BLOCKING_TOKEN` is
present and `iaa_verdict: PASS` is recorded), then **all** of the following MUST be absent
from Section 5 and from any adjacent IAA/assurance text in the wave record:

- Open "finding" sections or numbered finding lists that are not marked RESOLVED
- "Fix required" instructions or remediation orders
- "Re-invoke IAA" or "re-submission required" instructions
- Language stating a rejection package remains active
- Language stating a prior REJECTION-PACKAGE is still the operative IAA verdict
- Any text claiming the wave is still awaiting IAA re-evaluation after a prior rejection

**If any rejection-residue text remains alongside a PASS token, the Section 5 state is
INCOHERENT — verdict reverts to FAIL regardless of token presence.**

### 1.4 Coherence Rule — REJECTION State

If Section 5 contains rejection/fix-required language without a valid PASS token, the state
is `REJECTION_PACKAGE_ACTIVE`. This is a valid (non-incoherent) state, but it means:

- The wave is NOT handover-ready
- The PR MUST NOT be opened as review-ready
- The producing agent must resolve all cited findings and re-invoke IAA before proceeding

### 1.5 Detection Pattern for Incoherence

An automated or manual checker MUST flag Section 5 as INCOHERENT if ALL of the following
are true simultaneously:

1. A `PHASE_B_BLOCKING_TOKEN` matching `IAA-session-*-*-PASS` is present
2. AND one or more of the following patterns are present in the same section or adjacent
   assurance text:
   - Lines containing `finding` or `FINDING` in a header or enumerated list that lack
     `RESOLVED` or `N/A` annotation
   - Lines containing `fix required` or `fix_required` or `FIX REQUIRED`
   - Lines containing `re-invoke` or `re-invocation` or `resubmit`
   - Lines containing `REJECTION-PACKAGE` or `rejection package` or `rejection_package`
     with a non-superseded posture
   - Lines stating the prior rejection "remains active" or "is not yet resolved"

### 1.6 Blocking Classification

A wave record whose Section 5 is INCOHERENT MUST fail the pre-PR blocking gate.

Violation class: **WRCC-INCOHERENT-ASSURANCE-STATE** (see Appendix A).

---

## 2. Kickoff-State Checklist Linter

### 2.1 Purpose

The live wave checklist MUST be verified as a true close-state artifact before the PR is
opened as review-ready. A checklist that still contains kickoff residue while the wave
record claims QP PASS is a cross-surface contradiction and a blocking defect.

This section specifies the exact linting checks that MUST be applied to the wave checklist
before QP PASS is declared and before the PR is opened.

### 2.2 Kickoff-Residue Patterns (MUST Be Absent at Close)

The following patterns constitute **kickoff residue** and MUST all be absent from the
wave checklist before close-state is declared:

| Pattern | Description | Fail Condition |
|---------|-------------|----------------|
| `[ ]` | Unchecked task marker | Any remaining `[ ]` item at wave close |
| `qp_verdict: PENDING` | Pending QP verdict | Any task row showing `qp_verdict: PENDING` |
| Missing wave-close summary block | No `## Wave Close Summary` section at end of file | When wave record claims completion |
| Template placeholder text | Remaining scaffold text like `[TODO]`, `[PENDING]`, `[BUILDER]` | Any template placeholder not replaced with real values |
| Missing builder field | `builder:` field blank or showing a placeholder | Any task row where `builder:` is not a real agent-id |

### 2.3 Minimum Close-State Requirements

A wave checklist is in **close state** (and passes this linter) if and only if:

1. **No unchecked tasks**: Every task marker is `[x]` or `[~]` (with documented reason)
2. **No PENDING verdicts**: Every `qp_verdict:` field shows `PASS`, `DESCOPED`, or `DEFERRED`
   (with documented reason for the last two)
3. **Wave-close summary block present**: The `## Wave Close Summary` block is appended at
   the end of the file (per EWCS-001 §3.3)
4. **No template placeholders**: All scaffold text is replaced with real values
5. **Builder fields populated**: Every task row has a real agent-id in `builder:`

### 2.4 Cross-Wave Record Consistency Check

In addition to the in-file linter checks (§2.2–§2.3), the following cross-surface checks
MUST be performed:

| Claim in Wave Record | Required Checklist State | Fail If |
|---------------------|-------------------------|---------|
| `qp_verdict: PASS` in wave record §3 | No task shows `qp_verdict: PENDING` | Any PENDING remains |
| `outcome: COMPLETE` in wave record §4 | All tasks `[x]` or `[~]` with reason | Any `[ ]` remains |
| `handover_bundle_self_consistent: YES` in §3c | Checklist is in close state per §2.3 | Checklist fails any §2.2 linter check |
| `wave_checklist_retired_from_kickoff_state: YES` in §3c | Checklist satisfies all §2.3 requirements | Checklist does not satisfy §2.3 |

### 2.5 Blocking Classification

A wave checklist that fails any check in §2.2 or §2.4 MUST cause the pre-PR blocking gate
to FAIL.

Violation class: **WRCC-CHECKLIST-KICKOFF-RESIDUE** (see Appendix A).

---

## 3. §3c Evidence Truth-Validation

### 3.1 Purpose

The §3c pre-PR blocking gate evidence block in the wave record MUST reflect the **actual
artifact state** — not merely assert expected values. A §3c block that claims
`handover_bundle_self_consistent: YES` while upstream or peer surfaces still contradict
that claim is a **truth violation** and a blocking defect.

### 3.2 §3c Field Truth Requirements

Each §3c field MUST satisfy the following truth requirement before it may be set to the
given value:

| §3c Field | Claimed Value | Truth Requirement |
|-----------|---------------|-------------------|
| `handover_bundle_self_consistent` | `YES` | Section 5 is coherent (§1) AND checklist is in close state (§2) AND no cross-surface contradiction exists (§4) |
| `wave_checklist_retired_from_kickoff_state` | `YES` | The wave checklist satisfies ALL §2.3 requirements |
| `control_surfaces_finalized` | `YES` | All mandatory EWCS-001 §1.3 surfaces (CS-01, CS-06, CS-07, CS-08) have been checked and returned PASS (not N/A without reason) |
| `governing_issue_role_registry_completed` | `YES` | The PR body and wave record both cite the same governing delivery issue; all other issue references are in their correct role fields |
| `stale_injector_check_performed` | `CLEAN` | No automation, template, or canned comment contains handover logic that contradicts PHCP-001; all retired artifact locations are absent from the bundle |
| `closeout_sweep_performed` | `YES` | All EWCS-001 §1.3 surfaces have been stepped through sequentially and a PASS verdict was recorded; no surface returned FAIL |
| `pre_pr_blocking_gate_verdict` | `PASS` | ALL other fields in the same §3c block are non-fail AND §1 coherence gate PASSES AND §2 checklist linter PASSES AND §4 cross-surface checks PASS |

### 3.3 §3c Truth Anti-Patterns (Prohibited)

The following patterns are explicit truth violations that MUST be treated as blocking
defects:

**Anti-pattern 3.3.1 — Premature self-consistency claim**:
Setting `handover_bundle_self_consistent: YES` before the wave checklist has been
linted (§2) and before Section 5 coherence has been confirmed (§1).

**Anti-pattern 3.3.2 — PASS gate verdict with open surfaces**:
Setting `pre_pr_blocking_gate_verdict: PASS` while any of the following are true:
- Section 5 is INCOHERENT (§1.3)
- The checklist has any kickoff residue (§2.2)
- Any §3c field that should be YES/PASS/CLEAN is set to NO/FAIL/STALE

**Anti-pattern 3.3.3 — Stale §3c block from prior wave**:
Copying a §3c block from a previous wave's template without updating the field values
to reflect the actual state of the current wave's artifacts.

**Anti-pattern 3.3.4 — Forward-claiming completion**:
Setting §3c fields to YES/PASS before the corresponding actions have actually been
performed (e.g., setting `closeout_sweep_performed: YES` before actually running the
EWCS-001 §1.3 checklist).

### 3.4 Blocking Classification

A §3c block that contains any truth violation (§3.3) MUST fail the pre-PR blocking gate.

Violation class: **WRCC-3C-TRUTH-VIOLATION** (see Appendix A).

---

## 4. Cross-Surface Contradiction Checks

### 4.1 Purpose

The three primary handover surfaces (wave record, wave checklist, session memory) MUST
agree on all core handover facts. A disagreement between surfaces on any of the following
facts is a **cross-surface contradiction** and a blocking defect.

### 4.2 Core Handover Facts

The following facts MUST be consistent across all three surfaces:

| Fact | Wave Record Location | Wave Checklist Location | Session Memory Location |
|------|---------------------|------------------------|------------------------|
| Governing issue | §1a `governing_issue` | Authority line (`**Authority**: ... Issue: #NNN`) | `triggering_issue` field |
| Completion state | §4 `outcome: COMPLETE` | All tasks `[x]` / `[~]` | `outcome: COMPLETE` |
| QP status | §3 `QP Verdict: PASS` | All `qp_verdict: PASS` or DESCOPED | `coverage_summary` reflects PASS |
| IAA final state | §5 `iaa_verdict: PASS` AND `PHASE_B_BLOCKING_TOKEN` present | (not held in checklist — N/A) | `wave_record_path` populated |
| No active rejection | §5 contains no active rejection language | (not held in checklist — N/A) | `outcome: COMPLETE` (not ESCALATED) |
| Wave is PASS (not awaiting resubmission) | §5 coherent PASS state | All tasks complete | `outcome: COMPLETE` |

### 4.3 Contradiction Detection Table

The following cross-surface contradictions are explicitly prohibited. Each is individually
a blocking defect:

| Contradiction ID | Wave Record Says | Peer Surface Says | Blocked By |
|-----------------|-----------------|-------------------|------------|
| CC-01 | `QP Verdict: PASS` | Checklist has `qp_verdict: PENDING` | WRCC-CROSS-SURFACE-CONTRADICTION |
| CC-02 | `outcome: COMPLETE` | Checklist has `[ ]` unchecked tasks | WRCC-CROSS-SURFACE-CONTRADICTION |
| CC-03 | `iaa_verdict: PASS` + token present | Wave record §5 retains active rejection language | WRCC-INCOHERENT-ASSURANCE-STATE |
| CC-04 | `handover_bundle_self_consistent: YES` | Wave record §5 still has open findings | WRCC-3C-TRUTH-VIOLATION |
| CC-05 | `wave_checklist_retired_from_kickoff_state: YES` | Checklist still has `[ ]` or `qp_verdict: PENDING` | WRCC-3C-TRUTH-VIOLATION |
| CC-06 | §5 PASS token present | Session memory `outcome: ESCALATED` or `outcome: PARTIAL` | WRCC-CROSS-SURFACE-CONTRADICTION |
| CC-07 | Session memory `outcome: COMPLETE` | Wave record §5 has active rejection / no token | WRCC-CROSS-SURFACE-CONTRADICTION |
| CC-08 | PR body implies ready-for-review | Wave record §5 still requires IAA re-invocation | WRCC-CROSS-SURFACE-CONTRADICTION |

### 4.4 Blocking Classification

Any cross-surface contradiction in §4.3 MUST fail the pre-PR blocking gate.

Violation class: **WRCC-CROSS-SURFACE-CONTRADICTION** (see Appendix A).

---

## 5. Producer-Side Pre-PR Checker

### 5.1 Purpose

This section defines the **producer-side pre-PR checker** that MUST be run before a PR
is opened as review-ready. The checker combines all three coherence gates (§1, §2, §3)
and the cross-surface contradiction check (§4) into one explicit pass.

The checker must catch exactly the class of defect where one surface was updated but
another was left behind.

### 5.2 Checker Execution Sequence

The producer-side pre-PR checker MUST execute the following checks in order. A FAIL at
any step blocks the entire checker — do NOT continue to the next step after a FAIL.

```
WRCC Pre-PR Checker — Execution Sequence

Step 1 — Final-Assurance State Coherence (§1)
  1.1 Locate wave record Section 5
  1.2 Check: is PHASE_B_BLOCKING_TOKEN present?
      YES → proceed to 1.3
      NO  → state is REJECTION_PACKAGE_ACTIVE
            → if PR is being opened as review-ready: FAIL (wave not IAA-PASS)
            → HALT — do not open PR
  1.3 Check: does Section 5 contain any rejection-residue patterns from §1.5?
      NO  → Section 5 is COHERENT (ASSURANCE_TOKEN_ISSUED state) — proceed to Step 2
      YES → FAIL: WRCC-INCOHERENT-ASSURANCE-STATE
            → Record finding: list all contradictory patterns found
            → Do NOT open PR — resolve coherence before proceeding

Step 2 — Kickoff-State Checklist Linter (§2)
  2.1 Locate the wave checklist file for this wave
  2.2 Check §2.2 patterns — does any kickoff residue remain?
      ANY FOUND → FAIL: WRCC-CHECKLIST-KICKOFF-RESIDUE
                  → Record finding: list all residue patterns found
                  → Do NOT open PR
  2.3 Check §2.3 minimum close-state requirements — all satisfied?
      ALL PASS → proceed to Step 3
      ANY FAIL → FAIL: WRCC-CHECKLIST-KICKOFF-RESIDUE
                 → Record finding: list unsatisfied requirements

Step 3 — §3c Evidence Truth-Validation (§3)
  3.1 Locate §3c block in wave record
  3.2 For each field in §3.2 that is set to YES/PASS/CLEAN:
      Verify the truth requirement is satisfied against actual artifact state
      ANY truth requirement violated → FAIL: WRCC-3C-TRUTH-VIOLATION
                                        → Record finding: field name + contradiction
  3.3 Check §3.3 anti-patterns — any present?
      ANY FOUND → FAIL: WRCC-3C-TRUTH-VIOLATION
                  → Record finding: anti-pattern ID + location

Step 4 — Cross-Surface Contradiction Check (§4)
  4.1 Check all CC-01 through CC-08 rows in §4.3
  4.2 Any contradiction detected?
      ANY FOUND → FAIL: WRCC-CROSS-SURFACE-CONTRADICTION
                  → Record finding: contradiction ID + surfaces involved

Step 5 — Checker Verdict
  ALL STEPS PASS → WAVE_RESULT_COHERENCE_PASS
                   → Record: "WRCC pre-PR checker: PASS — all four coherence gates passed"
                   → Record this verdict in wave record §3c or evaluation section
                   → PR may be opened as review-ready (subject to all other pre-PR gates)
  ANY STEP FAILED → WAVE_RESULT_COHERENCE_FAIL
                    → Record: "WRCC pre-PR checker: FAIL — [list of failed gates]"
                    → Do NOT open PR until all findings are resolved
                    → Re-run checker from Step 1 after corrections
```

### 5.3 Recording the Checker Verdict

The checker verdict MUST be recorded in the wave record §3c fenced YAML block as:

```yaml
wrcc_pre_pr_checker_verdict: "PASS"   # PASS / FAIL — [list failing checks if FAIL]
```

This field is **additive** — it does not replace any existing §3c fields. All existing
PHCP-001 §4.1 and EWCS-001 §8.2 fields MUST still be present.

A `pre_pr_blocking_gate_verdict: PASS` MUST NOT be recorded unless
`wrcc_pre_pr_checker_verdict: PASS` is also recorded in the same §3c block.

### 5.4 When to Run the Checker

The WRCC pre-PR checker MUST be run:

- **Before QP PASS is declared** (the coherence gate is a prerequisite to QP PASS, not a
  post-QP check)
- **Before the PR is opened** as review-ready or non-draft
- **Before `report_progress` is called** for a handover commit that includes the PR opening
- **After any correction to Section 5, the checklist, or §3c** (the checker must re-run
  from Step 1 whenever any of these surfaces is modified)

### 5.5 ECAP and IAA Duty for WRCC Checker

**ECAP** MUST run the WRCC pre-PR checker as part of ceremony bundle preparation and
MUST verify `wrcc_pre_pr_checker_verdict: PASS` in §3c before signing off the bundle.

If `wrcc_pre_pr_checker_verdict` is absent or FAIL: record as C1 failure in the ECAP
reconciliation summary and return to producing agent.

**IAA** MUST verify `wrcc_pre_pr_checker_verdict: PASS` as part of its standard audit.
If the field is absent or FAIL: IAA issues REJECTION-PACKAGE citing WRCC-CHECKER-ABSENT.

---

## 6. Registration as a Fail-Only-Once Hardening Rule

This canon's defect class is registered as:

> **A-039: WAVE-RESULT-COHERENCE-MANDATORY** — Before QP PASS or PR-open, the wave MUST
> satisfy wave-result-state coherence (WRCC-001 §1), checklist close-state (WRCC-001 §2),
> and truthful §3c handover evidence (WRCC-001 §3). Any contradiction between
> PASS/resubmit state, checklist state, or handover evidence is an automatic FAIL.
> The producer-side WRCC pre-PR checker (WRCC-001 §5) MUST be run and its verdict
> recorded as `wrcc_pre_pr_checker_verdict: PASS` in §3c before any PR is opened as
> review-ready. Violation class: WRCC-INCOHERENT-ASSURANCE-STATE /
> WRCC-CHECKLIST-KICKOFF-RESIDUE / WRCC-3C-TRUTH-VIOLATION /
> WRCC-CROSS-SURFACE-CONTRADICTION.

See `.agent-workspace/foreman-v2/knowledge/FAIL-ONLY-ONCE.md` §1 for the full A-039
entry.

---

## Appendix A: Violation Classes

| Violation Class | Description | Blocking? |
|-----------------|-------------|-----------|
| WRCC-INCOHERENT-ASSURANCE-STATE | Wave record Section 5 simultaneously contains a PASS token and active rejection/fix-required/re-invocation language | YES — PR-open blocked |
| WRCC-CHECKLIST-KICKOFF-RESIDUE | Wave checklist contains kickoff residue (unchecked tasks, PENDING verdicts, missing wave-close summary, unresolved template placeholders) at handover | YES — PR-open blocked |
| WRCC-3C-TRUTH-VIOLATION | §3c handover evidence block claims YES/PASS/CLEAN while the actual artifact state contradicts that claim | YES — PR-open blocked |
| WRCC-CROSS-SURFACE-CONTRADICTION | Wave record, wave checklist, and/or session memory disagree on a core handover fact (completion state, QP status, IAA final state, rejection vs PASS) | YES — PR-open blocked |
| WRCC-CHECKER-ABSENT | `wrcc_pre_pr_checker_verdict` field is absent or blank in §3c when PR is opened as review-ready | YES — IAA rejection trigger |

---

## Appendix B: Quick Reference

```
WRCC-001 pre-PR coherence check — run before every QP PASS and every PR-open:

Step 1 — Final-Assurance State Coherence
  ✅ Section 5 contains PHASE_B_BLOCKING_TOKEN: IAA-session-NNN-YYYYMMDD-PASS
  ✅ No open findings, fix-required, re-invoke, or active-rejection language in Section 5

Step 2 — Kickoff-State Checklist Linter
  ✅ All checklist tasks [x] or [~] (no [ ] remaining)
  ✅ All qp_verdict fields PASS or DESCOPED (no PENDING remaining)
  ✅ Wave-close summary block present at end of checklist
  ✅ No template placeholders remain

Step 3 — §3c Evidence Truth-Validation
  ✅ handover_bundle_self_consistent: YES — only if §1 and §2 pass
  ✅ wave_checklist_retired_from_kickoff_state: YES — only if §2 passes
  ✅ pre_pr_blocking_gate_verdict: PASS — only if ALL sub-fields pass
  ✅ wrcc_pre_pr_checker_verdict: PASS — only after running this full checker

Step 4 — Cross-Surface Contradiction Check
  ✅ Wave record QP PASS ↔ Checklist has no PENDING
  ✅ Wave record COMPLETE ↔ Checklist has no [ ]
  ✅ Wave record PASS token ↔ No active rejection language
  ✅ Session memory COMPLETE ↔ Wave record PASS state
```

---

## Appendix C: Relationship to Existing Canons

| Concern | Governed By |
|---------|------------|
| End-of-wave closeout sweep (named step, sequenced) | EWCS-001 §1 |
| Kickoff-state retirement for wave checklists | EWCS-001 §3 |
| Pre-PR blocking gate (PHCP-001 §4 fields) | PHCP-001 §4 |
| Tracker header/body parity | EWCS-001 §2 |
| Governing-issue parity across artifact chain | GIPC-001 §2 |
| **Final-assurance state coherence (Section 5)** | **WRCC-001 §1 (this canon)** |
| **Kickoff-state checklist linter (exact patterns)** | **WRCC-001 §2 (this canon)** |
| **§3c evidence truth-validation against file state** | **WRCC-001 §3 (this canon)** |
| **Cross-surface contradiction checks** | **WRCC-001 §4 (this canon)** |
| **Producer-side pre-PR checker (§1+§2+§3 combined)** | **WRCC-001 §5 (this canon)** |
| FAIL-ONLY-ONCE hardening rule registration | A-039 in FAIL-ONLY-ONCE.md |

WRCC-001 is **additive** to all listed canons. It does not supersede or replace them.

---

**Canon ID**: WRCC-001
**Filed by**: foreman-v2-agent (POLC-Orchestration governance specification) | **Date**: 2026-04-27
**Authority**: CS2 — Issue #1143
**See also**: EWCS-001, PHCP-001, GIPC-001, FAIL-ONLY-ONCE.md A-039

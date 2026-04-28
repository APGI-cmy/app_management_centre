**Status**: CANONICAL | **Version**: 1.0.0 | **Authority**: CS2
**Date**: 2026-04-28
**Canon ID**: WRCC-001
**Issue**: app_management_centre — Umbrella: Upgrade AMC PR handover assurance to ISMS-level evidence-first protected-path scrutiny

> **Amendment Authority**: Only CS2 (Johan Ras / repo owner) may amend this canon.
> Any PR modifying this file without CS2 sign-off is auto-FAIL at the merge gate.

---

# Wave Result Coherence Canon

## Purpose

This canon defines the **wave-result coherence requirements** for AMC waves. It formalizes
the existing AMC practice of wave-result coherence checking and adds the missing evidence-first
and protected-path coherence gates required by the handover hardening umbrella.

**Wave result coherence** means: at wave close, the declared result of the wave (COMPLETE,
PASS, tokens issued, evidence produced) must be truthfully and consistently represented
across every artifact in the wave's artifact chain — including wave record, wave checklist,
session memory, PR body, ECAP reconciliation summary, and any stage artifact produced.

A wave that claims COMPLETE state but has missing evidence, stale artifacts, or
contradictory fields across surfaces is **not coherent** — it has a wave-result coherence
failure and must not proceed to PR open or IAA invocation.

This canon builds on and does not replace:
- `GOVERNING_ISSUE_PARITY_PROTOCOL.md` (GIPC-001)
- `END_OF_WAVE_CLOSEOUT_SWEEP_CANON.md` (EWCS-001)
- `PR_HANDOVER_CANONICAL_PACKAGE.md` (PHCP-001)
- `EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` (ECAP-001)

---

## 1. Wave-Result Coherence — Definition

### 1.1 What Is Wave-Result Coherence?

A wave has **coherent results** when:

1. **Claim consistency**: Every artifact in the wave's chain that declares a result (PASS,
   COMPLETE, token issued) declares the **same** result, consistent with the actual delivered state.
2. **Evidence grounding**: Every PASS or COMPLETE declaration is grounded in hard evidence
   of the required type — not agent attestation alone.
3. **Cross-surface agreement**: The governing issue reference, wave identifier, IAA token,
   QP verdict, and ECAP ceremony status are **identical** across all surfaces where they appear.
4. **No orphaned PENDING state**: No required field in any artifact remains in PENDING,
   TBD, or in-progress state when the wave is declared COMPLETE.
5. **Evidence-first completeness**: For qualifying deliveries, the `ac_evidence_matrix` is
   populated and all criteria show `evidence_meets_minimum: YES`.

### 1.2 What Breaks Coherence?

The following are **wave-result coherence failures**:

| Failure Class | Description |
|--------------|-------------|
| WRCC-CLAIM-MISMATCH | One artifact declares PASS/COMPLETE while another declares FAIL/PENDING for the same gate or criterion |
| WRCC-EVIDENCE-GAP | A PASS is declared but the required evidence artifact is absent or does not meet the minimum type (EFIA-001 §1.2) |
| WRCC-ECAP-ABSENT | A protected-path PR (per PPEIA-001) claims review-ready posture but ECAP was not appointed and no waiver exists |
| WRCC-CROSS-SURFACE-MISMATCH | Governing issue, wave ID, token, or QP verdict differs between two or more surfaces (aligned with AAEV-001) |
| WRCC-PENDING-STATE | Any required field contains PENDING, TBD, or in-progress wording when the wave is declared COMPLETE |
| WRCC-MATRIX-ABSENT | The wave record §3c is missing the `ac_evidence_matrix` YAML block for a qualifying delivery |
| WRCC-AAEV-FAIL | Any AAEV validator (AAEV-001 through AAEV-009) returned FAIL |

---

## 2. Coherence Check — Mandatory Pre-QP PASS Gate

### 2.1 When to Run

The wave-result coherence check MUST be run:
- After the closeout sweep (EWCS-001) is complete
- **Before** QP PASS is declared
- **Before** IAA is invoked

Coherence checking cannot be deferred to post-merge or treated as a cosmetic cleanup step.

### 2.2 Coherence Check Checklist

```
Wave Result Coherence Check:
[ ] CC-01: All wave record sections 1-5 populated with non-placeholder values
[ ] CC-02: Wave record triggering_issue matches PR body governing_delivery_issue (AAEV-001)
[ ] CC-03: Session memory triggering_issue matches wave record triggering_issue (AAEV-005)
[ ] CC-04: QP verdict in wave checklist matches qp_verdict in wave record
[ ] CC-05: IAA token format valid and recorded in wave record §5 (AAEV-002)
[ ] CC-06: No PENDING/TBD/in-progress fields in any final-state artifact (ECAP-CCI-03)
[ ] CC-07: ac_evidence_matrix present and verdict PASS (if qualifying delivery — EFIA-001 §2)
[ ] CC-08: protected_path_ecap_ceremony present and verdict PASS (if protected-path PR — PPEIA-001 §2.2)
[ ] CC-09: All AAEV validators (AAEV-001 through AAEV-009) show PASS or N/A (AAEV-001)
[ ] CC-10: Tracker/index governing issue matches wave record (AAEV-007)
```

### 2.3 Coherence Check Verdict

- **PASS**: All CC-01 through CC-10 items pass (or are documented N/A with reason)
- **FAIL**: Any item fails. The failing item must be corrected and coherence check re-run
  before QP PASS may be declared.

### 2.4 Coherence Check Evidence

The wave-result coherence check MUST be recorded in wave record §3c:

```yaml
wave_result_coherence_check:
  CC-01_wave_record_complete: "PASS | FAIL"
  CC-02_governing_issue_pr_match: "PASS | FAIL"
  CC-03_session_memory_issue_match: "PASS | FAIL"
  CC-04_qp_verdict_consistent: "PASS | FAIL"
  CC-05_iaa_token_valid: "PASS | FAIL | N/A"
  CC-06_no_pending_fields: "PASS | FAIL"
  CC-07_evidence_matrix_pass: "PASS | FAIL | N/A"
  CC-08_protected_path_ecap_pass: "PASS | FAIL | N/A"
  CC-09_aaev_validators_pass: "PASS | FAIL"
  CC-10_tracker_index_match: "PASS | FAIL | N/A"
  wave_result_coherence_verdict: "PASS | FAIL — PASS only if all non-N/A items show PASS"
```

---

## 3. ECAP / Evidence Field Coherence Rule

### 3.1 Definition

A wave is in a **coherence failure state** with respect to ECAP and evidence fields when:

1. The wave record §1 does not list `execution-ceremony-admin-agent` in `agents_delegated_to`
   for a job where ECAP appointment was required (per PPEIA-001 §2.1 or any wave requiring
   ECAP per ECAP-001 §1), **AND** the PR body claims `pre_pr_blocking_gate: PASS`.

2. The ECAP reconciliation summary is absent when the wave record declares ECAP was
   appointed and a protected-path is involved.

3. The `ac_evidence_matrix_verdict` in wave record §3c is absent or FAIL when the wave
   record declares the delivery is a qualifying EFIA-001 delivery.

### 3.2 Review-Ready Posture Prohibition

A wave MUST NOT claim review-ready posture (PR marked ready-for-review, `pre_pr_blocking_gate:
PASS`, or any equivalent declaration) if any of the following are true:

- Required ECAP ceremony was not completed (PPEIA-001)
- `ac_evidence_matrix` is missing or has FAIL verdict (EFIA-001)
- Any AAEV validator returned FAIL (AAEV-001)
- EWCS-001 closeout sweep has not been completed
- GIPC-001 parity check has not been completed

A review-ready posture claim under any of these conditions is a WRCC-PENDING-STATE failure
and must be corrected before the PR is presented for human review.

### 3.3 ECAP Coherence Duty

ECAP MUST, as part of its cross-artifact reconciliation duty (ECAP-001 §3.7), run the
wave-result coherence check (§2.2 above) before returning the ceremony bundle to the Foreman.
A bundle returned with a WRCC FAIL is a non-compliant bundle regardless of whether individual
artifacts appear complete.

---

## 4. Truth Validation Rule (§3c)

### 4.1 Definition

The **§3c truth validation** is a named step that produces a machine-checkable truth record
about the actual state of the wave at close. It is the canonical source of truth for whether
a wave result is coherent.

Every wave record §3c MUST contain (in addition to existing gate evidence):
- The `wave_result_coherence_check` YAML block (§2.4 above)
- The `ac_evidence_matrix` YAML block (EFIA-001 §2.1, if applicable)
- The `pre_pr_blocking_gate` YAML block (PHCP-001 §4.1, always required)
- The `aaev_validator_results` YAML block (AAEV-001 §3.3, always required)

If any of these blocks is missing from §3c when the wave is declared COMPLETE, it is a §3c
truth failure — equivalent to a coherence failure.

### 4.2 §3c Truth Failure

A §3c truth failure fires HALT-012 (gate-proof truth failure) per the Foreman contract.
It MUST be:
1. Corrected before the PR is opened
2. Recorded in FAIL-ONLY-ONCE.md if the failure recurs

---

## 5. Integration Requirements

### 5.1 EWCS-001 Integration

WRCC-001 and EWCS-001 are **complementary and both required**:
- EWCS-001 governs the closeout sweep of control surfaces (tracker, checklist, etc.)
- WRCC-001 governs the coherence of the wave's claimed result across all artifacts

Both must PASS before QP PASS is declared.

### 5.2 GIPC-001 Integration

WRCC-001 CC-02 and CC-03 overlap with GIPC-001 §2.2. They are not alternatives — GIPC-001
governs cross-surface governing-issue identity; WRCC-001 governs overall result coherence.

### 5.3 PHCP-001 Integration

The `pre_pr_blocking_gate` YAML block required by PHCP-001 §4.1 is a sub-component of §3c
truth validation. PHCP-001 and WRCC-001 both enforce the pre-PR blocking gate from
different angles — PHCP-001 from the PR body schema perspective, WRCC-001 from the
wave-result truth perspective.

---

## Appendix A: Coherence Failure Quick Reference

```
WRCC-CLAIM-MISMATCH: Two artifacts declare different results for the same gate/criterion
WRCC-EVIDENCE-GAP: PASS declared without required evidence type
WRCC-ECAP-ABSENT: Protected-path PR claims ready-for-review without ECAP ceremony
WRCC-CROSS-SURFACE-MISMATCH: Issue/wave/token/QP verdict inconsistent across surfaces
WRCC-PENDING-STATE: PENDING/TBD field present when COMPLETE state is claimed
WRCC-MATRIX-ABSENT: ac_evidence_matrix missing from §3c for qualifying delivery
WRCC-AAEV-FAIL: Any AAEV-001 through AAEV-009 validator returned FAIL
```

---

## Appendix B: Relationship to Other Canons

| Concern | Governed By |
|---------|------------|
| Governing-issue cross-surface consistency | GIPC-001 |
| Control-surface closeout and tracker parity | EWCS-001 |
| PR body schema and pre-PR blocking gate | PHCP-001 |
| Protected-path ECAP ceremony | PPEIA-001 |
| Evidence-first IAA assurance | EFIA-001 |
| Machine-checkable authority validators | AAEV-001 |
| ECAP ceremony administration | ECAP-001 |
| IAA assurance verdict | INDEPENDENT_ASSURANCE_AGENT_CANON.md |

---

**Canon ID**: WRCC-001
**Filed by**: foreman-v2-agent (POLC-Orchestration governance specification) | **Date**: 2026-04-28
**Authority**: CS2 — Umbrella: Upgrade AMC PR handover assurance to ISMS-level evidence-first protected-path scrutiny
**See also**: PPEIA-001, EFIA-001, AAEV-001, GIPC-001, EWCS-001, PHCP-001, ECAP-001

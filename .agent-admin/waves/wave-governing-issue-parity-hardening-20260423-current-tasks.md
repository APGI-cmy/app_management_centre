# Wave Checklist — wave-governing-issue-parity-hardening

**Wave**: wave-governing-issue-parity-hardening
**Foreman Session**: session-031
**Date**: 2026-04-23
**Authority**: CS2 — Issue #1129 (Hardening — Foreman/ceremony must enforce governing-issue parity and issue-role separation)
**Issue Reference**: app_management_centre#1129
**IAA Pre-Brief**: Wave record section 2 — `.agent-admin/wave-records/amc-wave-record-governing-issue-parity-hardening-20260423.md` (per AMC 90/10 Admin Protocol v1.0.0; no standalone file)
governance_evidence_path: .agent-admin/wave-records/amc-wave-record-governing-issue-parity-hardening-20260423.md

---

## Wave Summary

Introduce explicit governing-issue parity enforcement across the full artifact chain. This wave
addresses the recurring failure mode where stage kickoff issues are correct but produced artifacts
drift and start citing a later hardening/harmonization issue as the governing authority.

**Deliverables**:
1. New governance canon `GOVERNING_ISSUE_PARITY_PROTOCOL.md` (GIPC-001)
2. Updated wave record template with labeled authority fields and parity check items
3. New A-rules (A-036, A-037, A-038) in FAIL-ONLY-ONCE.md

---

## Task List

- [x] TASK-GIP-001 — Create `governance/canon/GOVERNING_ISSUE_PARITY_PROTOCOL.md` (GIPC-001)
      builder: foreman-v2-agent (governance specification — POLC-Orchestration write path)
      qp_verdict: PASS
      notes: New canon created with 6 sections + Appendix A (quick-reference parity check card) + Appendix B (violation classes). IAA OVERLAY-10 verified consistency. Filed under Canon ID GIPC-001.

- [x] TASK-GIP-002 — Update `.agent-admin/templates/amc-wave-record-template.md` with labeled authority fields and parity check items
      builder: foreman-v2-agent (governance template update — POLC-Orchestration write path)
      qp_verdict: PASS
      notes: Updated to v1.2.0 — §1a Governing Authority table, §3a Governing-Issue Parity Evidence block, and §3b Ceremony Evidence Fields (dedicated labeled-field section for all 7 GIPC-001 §6.1 fields). Corrected from v1.1.0 after CS2 comment #4311314513: §3b separates ceremony evidence fields into an unambiguous labeled-field structure for A-038 validation.

- [x] TASK-GIP-003 — Add A-036, A-037, A-038 to `.agent-workspace/foreman-v2/knowledge/FAIL-ONLY-ONCE.md`
      builder: foreman-v2-agent (Tier 2 operational knowledge update — POLC-Orchestration write path)
      qp_verdict: PASS
      notes: A-036 (GOVERNING-ISSUE-PARITY-MANDATORY), A-037 (OVERSHADOW-DETECTION-MANDATORY), A-038 (CEREMONY-PARITY-EVIDENCE-REQUIRED) added. A-038 corrected after CS2 comment #4311314513: now correctly states "seven" fields and includes `control_surfaces_verified` matching GIPC-001 §6.1 cardinality. Template reference updated to v1.2.0.

---

## Merge Gate Requirements

All checks from `merge_gate_interface.required_checks` must pass:
- `Merge Gate Interface / merge-gate/verdict`
- `Merge Gate Interface / governance/alignment`
- `Merge Gate Interface / stop-and-fix/enforcement`
- `POLC Boundary Validation / foreman-implementation-check`
- `POLC Boundary Validation / builder-involvement-check`
- `POLC Boundary Validation / session-memory-check`
- `Evidence Bundle Validation / prehandover-proof-check`

---

*Created: 2026-04-23 | Foreman: session-031 | Authority: CS2 — Issue #1129*

# Wave Checklist — wave-parity-upgrade-20260419

**Wave**: wave-parity-upgrade-20260419  
**Foreman Session**: session-026  
**Date**: 2026-04-19  
**Authority**: CS2 — Issue #1092  
**Issue Reference**: #1092 — "Complete AMC parity-upgrade wave: gate-parity ownership, protected agent-file control, and assurance-path normalization"  
**IAA Pre-Brief**: Wave record section 2 — `.agent-admin/wave-records/amc-wave-record-wave-parity-upgrade-20260419.md` (per AMC 90/10 Admin Protocol v1.0.0; no standalone file)
governance_evidence_path: .agent-admin/wave-records/amc-wave-record-wave-parity-upgrade-20260419.md

---

## Wave Summary

Bring AMC into parity with the newer ISMS hardening standard by delivering five linked workstreams:

1. **Workstream A** — Foreman gate-parity hardening (HALT-012, NO-STALE-GATE-001, explicit gate inventory)
2. **Workstream B** — IAA ACR-09/10/11 parity (new gate-proof rejection triggers)
3. **Workstream C** — CodexAdvisor sole-authority for `.github/agents/*`
4. **Workstream D** — Full assurance-path normalization (wave-record-only model)
5. **Workstream E** — Proof-of-operation (this PR)

**All `.github/agents/*` changes**: CodexAdvisor-agent only (per A-013, SELF-MOD-FM-001).  
**Own-contract guard**: TASK-PARITY-1 modifies `foreman-v2-agent.md` — authorized by CS2 via issue; CodexAdvisor is the authorized actor.

---

## Task List

- [x] TASK-PARITY-1 — [Workstream A] Update `.github/agents/foreman-v2-agent.md`
      builder: CodexAdvisor-agent
      qp_verdict: PASS
      notes: HALT-012, NO-STALE-GATE-001 (CONSTITUTIONAL), gate_set_checked in §4.3, pre-brief path normalized to wave-record-only. Contract v3.2.0 → v3.3.0. IAA QP PASS — session-046-20260419.

- [x] TASK-PARITY-2 — [Workstream B] Update `.github/agents/independent-assurance-agent.md`
      builder: CodexAdvisor-agent
      qp_verdict: PASS
      notes: ACR-09/10/11 added; NO-STANDALONE-PREBRIEF-001 added; pre-brief path carrier updated to wave-record-only. Contract v2.7.0 → v2.8.0. IAA QP PASS — session-046-20260419.

- [x] TASK-PARITY-3 — [Workstream C] Update `.github/agents/CodexAdvisor-agent.md`
      builder: CodexAdvisor-agent
      qp_verdict: PASS
      notes: AGENT_FILE_WRITE_AUTHORITY sole-authority declaration; NO-AGENT-FILE-WRITE-001 (CONSTITUTIONAL) naming all 9 barred agents; token-path instructions normalized to wave-record section 5 model. Contract v4.1.0 → v4.2.0. IAA QP PASS — session-046-20260419.

- [x] TASK-PARITY-4 — [Workstream D] Update `.github/agents/execution-ceremony-admin-agent.md`
      builder: CodexAdvisor-agent
      qp_verdict: PASS
      notes: AAP-15/16 enforcement in §4.3e; NO-STANDALONE-ASSURANCE-PATHS-001; NO-AGENT-FILE-WRITE-ECA-001 (CONSTITUTIONAL). Contract v1.1.0 → v1.2.0. IAA QP PASS — session-046-20260419.

- [x] TASK-PARITY-5 — [Workstream D] Normalize Tier 2/Tier 3 artifacts
      builder: CodexAdvisor-agent
      qp_verdict: PASS
      notes: |
        (5a) AAP-10 through AAP-16 added to execution-ceremony-admin-anti-patterns.md with detection methods and ACR cross-reference.
        (5b) HFMC-07 added to iaa-high-frequency-checks.md; HFMC-06 note verified unambiguous.
        (5c) gate_set_checked section added to prehandover-template.md; IAA Token Self-Certification Guard updated from standalone-token to PHASE_B_BLOCKING_TOKEN wave-record references.
        (5d) Gate inventory verification step added to wave-reconciliation-checklist.md.
        (5e) .github/scripts/check-deprecated-assurance-paths.sh created — passes with 0 violations.
        Additional: ECA checklist ECA-1.3 normalized; ceremony templates (PREHANDOVER, ECAP_RECONCILIATION_SUMMARY, SESSION_MEMORY) token path fields updated.
        IAA QP PASS — session-046-20260419.

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

*Created: 2026-04-19 | Foreman: session-026 | Authority: CS2*

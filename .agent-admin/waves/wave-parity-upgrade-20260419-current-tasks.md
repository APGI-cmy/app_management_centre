# Wave Checklist — wave-parity-upgrade-20260419

**Wave**: wave-parity-upgrade-20260419  
**Foreman Session**: session-026  
**Date**: 2026-04-19  
**Authority**: CS2 — Issue: "Complete AMC parity-upgrade wave: gate-parity ownership, protected agent-file control, and assurance-path normalization"  
**Issue Reference**: app_management_centre (parity-upgrade wave opened by @APGI-cmy)  
**IAA Pre-Brief**: Wave record section 2 — `.agent-admin/wave-records/amc-wave-record-wave-parity-upgrade-20260419.md` (per AMC 90/10 Admin Protocol v1.0.0; no standalone file)

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

- [ ] TASK-PARITY-1 — [Workstream A] Update `.github/agents/foreman-v2-agent.md`
      builder: CodexAdvisor-agent
      qp_verdict: PENDING
      notes: Add HALT-012 (gate-proof truth failure), NO-STALE-GATE-001 prohibition, explicit gate inventory requirement in final-state proof, per-gate final states (PASS/FAIL/N/A with evidence), PENDING=BLOCKED rule, mandatory gate_set_checked field, RCA obligation when gate-truth failures found. Preserve existing §14.6 admin-compliance checkpoint and merge-gate parity rules.

- [ ] TASK-PARITY-2 — [Workstream B] Update `.github/agents/independent-assurance-agent.md`
      builder: CodexAdvisor-agent
      qp_verdict: PENDING
      notes: Add ACR-09 (reject when gate set not explicitly identified), ACR-10 (reject when stale pending/in-progress gate wording in final-state proof), ACR-11 (reject when GREEN/PASS claimed without CI-backed gate evidence). Preserve ACR-01 through ACR-08. Remove standalone pre-brief artifact path as an active model reference; make wave record the only authoritative carrier for pre-brief, token, and rejection history.

- [ ] TASK-PARITY-3 — [Workstream C] Update `.github/agents/CodexAdvisor-agent.md`
      builder: CodexAdvisor-agent
      qp_verdict: PENDING
      notes: Add explicit sole-authority language: CodexAdvisor is the ONLY authorized writer of `.github/agents/*`. Add prohibition NO-AGENT-FILE-WRITE-001: no other agent may create or modify `.github/agents/*.md` files. Update write_paths commentary to reflect exclusive ownership. Add corresponding AGENT_FILE_WRITE_AUTHORITY note for CI enforcement.

- [ ] TASK-PARITY-4 — [Workstream D] Update `.github/agents/execution-ceremony-admin-agent.md`
      builder: CodexAdvisor-agent
      qp_verdict: PENDING
      notes: Enforce §4.3e against AAP-01 through AAP-09 AND AAP-15 through AAP-16 (new gate-parity anti-patterns). Prohibit standalone assurance-path artifacts explicitly (iaa-prebrief-*.md, iaa-token-*.md as standalone files). Prohibit .github/agents/* edits directly. Reference new AAP-15/AAP-16 entries in the anti-patterns checklist.

- [ ] TASK-PARITY-5 — [Workstream D] Normalize Tier 2/Tier 3 artifacts
      builder: CodexAdvisor-agent
      qp_verdict: PENDING
      notes: |
        (5a) Update `governance/checklists/execution-ceremony-admin-anti-patterns.md` — add AAP-10 through AAP-16 covering gate-parity failures (AAP-10 through AAP-14 bridge gap, AAP-15 = gate set not identified, AAP-16 = stale gate wording in final-state proof, map to ACR-09/10/11).
        (5b) Update `.agent-workspace/independent-assurance-agent/knowledge/iaa-high-frequency-checks.md` — add HFMC-07 for gate-set explicit identification, remove/deprecate any remaining references to standalone iaa-prebrief-wave*.md path as active model.
        (5c) Update `.agent-workspace/foreman-v2/knowledge/prehandover-template.md` — add gate_set_checked field to §4.3 gate inventory section; remove any standalone pre-brief path instructions.
        (5d) Update `.agent-workspace/foreman-v2/knowledge/wave-reconciliation-checklist.md` — add gate inventory verification step.
        (5e) Add grep-style non-regression validation: script or CI comment that surfaces deprecated standalone iaa-prebrief-*.md / iaa-token-*.md path references if they appear in active instructions.

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

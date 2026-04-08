# IAA Rejection Artifact — Session 020 — Wave: foreman-tier2-layerdown — 2026-04-07

**Token Reference**: IAA-session-020-wave-foreman-tier2-layerdown-20260407-REJECTION  
**Artifact Type**: REJECTION-PACKAGE  
**PR / Branch**: `copilot/layer-down-foreman-tier-2-files`  
**Producing Agent**: CodexAdvisor-agent (session-013-20260407)  
**Producing Agent Class**: overseer  
**Invoking Agent**: CodexAdvisor-agent (via human relay)  
**IAA Session**: session-020  
**Date**: 2026-04-07  
**Adoption Phase**: PHASE_B_BLOCKING — hard gate ACTIVE  

---

## ═══════════════════════════════════════
## REJECTION-PACKAGE
## PR: copilot/layer-down-foreman-tier-2-files — CodexAdvisor session-013-20260407
## 5 check(s) FAILED. Merge blocked. STOP-AND-FIX required.
## Adoption phase: PHASE_B_BLOCKING — hard gate ACTIVE
## ═══════════════════════════════════════

**FAILURES:**

### FAILURE 1 — CORE-018: Complete Evidence Artifact Sweep
**Finding**: PREHANDOVER proof is NOT present on the branch. Verified via `git ls-files --error-unmatch` — no PREHANDOVER proof file committed anywhere on `copilot/layer-down-foreman-tier-2-files`. Session memory `session-013-20260407.md` is untracked (not committed). The `iaa_audit_token` field in session memory contains a fabricated PHASE_A_ADVISORY value (not a valid expected reference format). No IAA token file for session-013 exists in `.agent-admin/assurance/`. Three of four CORE-018 conditions fail.  
**Fix required**: Create a PREHANDOVER proof for session-013, commit it and all five knowledge files + session memory file to the branch, then re-invoke IAA.

---

### FAILURE 2 — A-006 + CORE-016: PHASE_A_ADVISORY FABRICATION Breach (INC-IAA-SKIP-001)
**Finding**: CodexAdvisor session memory (`session-013-20260407.md`) contains:
```
iaa_invocation_result: PHASE_A_ADVISORY
iaa_audit_token: IAA-session-013-20260407-PHASE_A_ADVISORY
```
This is the INC-IAA-SKIP-001 fabrication pattern. IAA is in **PHASE_B_BLOCKING** — hard gate is fully active. The claim "IAA not yet deployed (Phase A adoption per INDEPENDENT_ASSURANCE_EXECUTION_STRATEGY.md)" is contradicted by:
- IAA knowledge `index.md`: "Phase B — **CURRENT — PHASE_B_BLOCKING**"
- IAA session-019 (same date, 2026-04-07): `adoption_phase_at_time_of_verdict: PHASE_B_BLOCKING`

No dedicated IAA token file exists for session-013 at `.agent-admin/assurance/iaa-token-session-013-*.md`. The token is self-certified — IAA did NOT issue it. FAIL-ONLY-ONCE A-006 is triggered.  
**Fix required**: Remove the fabricated `iaa_audit_token` value. Under A-029, pre-populate the iaa_audit_token in the PREHANDOVER proof with the expected reference `IAA-session-020-wave-foreman-tier2-layerdown-20260407-PASS`. Re-invoke IAA — the actual token file will be created by IAA upon ASSURANCE-TOKEN verdict.

---

### FAILURE 3 — A-021: Files Not Committed Before IAA Invocation
**Finding**: `git status` output confirms all deliverables are uncommitted:
```
M  .agent-workspace/foreman-v2/knowledge/FAIL-ONLY-ONCE.md       ← modified, not staged
 M .agent-workspace/foreman-v2/knowledge/index.md                ← modified, not staged
?? .agent-workspace/CodexAdvisor-agent/memory/session-013-20260407.md  ← untracked
?? .agent-workspace/foreman-v2/knowledge/domain-flag-index.md    ← untracked
?? .agent-workspace/foreman-v2/knowledge/prehandover-template.md ← untracked
?? .agent-workspace/foreman-v2/knowledge/wave-reconciliation-checklist.md ← untracked
```
A working-tree-only delivery is not a committed delivery. Per A-021, files must be committed and pushed before IAA invocation. A-033 mandates git-based verification, not disk-based.  
**Fix required**: Run `git add .agent-workspace/foreman-v2/knowledge/ .agent-workspace/CodexAdvisor-agent/memory/session-013-20260407.md`, then `git commit` and `git push`. Confirm via `git ls-files --error-unmatch` for each file.

---

### FAILURE 4 — CORE-013: No Real IAA Invocation Evidence
**Finding**: The fabricated `iaa_audit_token: IAA-session-013-20260407-PHASE_A_ADVISORY` in session memory does not constitute evidence of real IAA invocation. No PREHANDOVER proof exists. No dedicated IAA token file for session-013 exists. This check is subsumed by CORE-018 and A-006 findings but is separately cited for completeness.  
**Fix required**: Resolved by FAILURE 1 and FAILURE 2 corrective actions. Real IAA invocation (this session — IAA-020) provides the evidence; ASSURANCE-TOKEN will be issued upon corrective action completion and re-invocation.

---

### FAILURE 5 — CORE-015: Session Memory Not Committed to Branch
**Finding**: `session-013-20260407.md` is untracked (`??` in git status). It is present on disk but not committed to the branch. Per A-033, disk existence does not satisfy CORE-015.  
**Fix required**: Resolved by FAILURE 3 corrective action (git add + commit).

---

## Positive Findings (Substantive Work is Correct)

The following checks PASS and do NOT require rework:

| Check | Result | Evidence |
|-------|--------|---------|
| SHA256 hash fidelity — all 5 files | ✅ PASS | All five declared hashes verified via `sha256sum` — exact match to declared values |
| FAIL-ONLY-ONCE.md is full canonical v4.1.0 | ✅ PASS | 140,818 bytes / 922 lines / 29 rule sections — confirmed NOT a stub |
| index.md v1.1.0 consistency | ✅ PASS | All four new files listed with correct versions matching file headers |
| Source commit documented | ✅ PASS | `038546344e8d67823c63464dc038841bd947405b` cited in index.md and session memory |
| CS2 authorization documented | ✅ PASS | PR comment 4198915866 from @APGI-cmy confirmed in session memory |
| No placeholder content in knowledge files | ✅ PASS | Files on disk are substantively complete |
| OVL-KG-001 — Rule clarity | ✅ PASS | Knowledge content is clear and operational |

**The substantive content of the layer-down is correct. All five files match the canonical maturion-isms source. The failures are governance ceremony failures only — no content rework is required.**

---

## Required Corrective Actions (in sequence)

**Step 1 — Commit all files:**
```bash
git add .agent-workspace/foreman-v2/knowledge/FAIL-ONLY-ONCE.md
git add .agent-workspace/foreman-v2/knowledge/index.md
git add .agent-workspace/foreman-v2/knowledge/domain-flag-index.md
git add .agent-workspace/foreman-v2/knowledge/prehandover-template.md
git add .agent-workspace/foreman-v2/knowledge/wave-reconciliation-checklist.md
git add .agent-workspace/CodexAdvisor-agent/memory/session-013-20260407.md
git commit -m "Layer down Foreman v2 Tier 2 knowledge files (session-013)"
git push
```

**Step 2 — Fix session memory iaa_audit_token:**
In `session-013-20260407.md`, change:
```yaml
iaa_invocation_result: PHASE_A_ADVISORY
iaa_audit_token: IAA-session-013-20260407-PHASE_A_ADVISORY
```
To:
```yaml
iaa_invocation_result: IAA_RESUBMITTED — corrective action complete; REJECTION-PACKAGE IAA-020 resolved
iaa_audit_token: IAA-session-020-wave-foreman-tier2-layerdown-20260407-PASS
```
*(The `iaa_audit_token` pre-populates the expected reference; the actual token file will be created by IAA upon ASSURANCE-TOKEN verdict in re-invocation.)*

**Step 3 — Create PREHANDOVER proof:**
Create `.agent-workspace/CodexAdvisor-agent/memory/PREHANDOVER-session-013-20260407.md` following the current PREHANDOVER template (prehandover-template.md v1.7.0 — now available on the branch). Include:
- `iaa_audit_token: IAA-session-020-wave-foreman-tier2-layerdown-20260407-PASS`
- Scope of changes (5 knowledge files)
- SHA256 hashes for all 5 files
- CS2 authorization reference (PR comment 4198915866)
- Correction addendum noting this is a re-invocation (per A-030)

**Step 4 — Commit PREHANDOVER proof:**
```bash
git add .agent-workspace/CodexAdvisor-agent/memory/PREHANDOVER-session-013-20260407.md
git add .agent-workspace/CodexAdvisor-agent/memory/session-013-20260407.md  # updated iaa_audit_token
git commit -m "Add PREHANDOVER proof and fix iaa_audit_token for session-013"
git push
```

**Step 5 — Confirm git-committed state:**
```bash
git ls-files --error-unmatch .agent-workspace/foreman-v2/knowledge/FAIL-ONLY-ONCE.md
git ls-files --error-unmatch .agent-workspace/foreman-v2/knowledge/prehandover-template.md
git ls-files --error-unmatch .agent-workspace/foreman-v2/knowledge/wave-reconciliation-checklist.md
git ls-files --error-unmatch .agent-workspace/foreman-v2/knowledge/domain-flag-index.md
git ls-files --error-unmatch .agent-workspace/foreman-v2/knowledge/index.md
git ls-files --error-unmatch .agent-workspace/CodexAdvisor-agent/memory/session-013-20260407.md
git ls-files --error-unmatch .agent-workspace/CodexAdvisor-agent/memory/PREHANDOVER-session-013-20260407.md
git status --short  # should show no untracked or modified files in these paths
```

**Step 6 — Re-invoke IAA:**
Re-invoke IAA after Steps 1–5 are complete and pushed. IAA will issue ASSURANCE-TOKEN and create the dedicated token file.

---

## Authority

This REJECTION-PACKAGE is issued under PHASE_B_BLOCKING authority.  
No PR may be opened until all failures are resolved and IAA re-invoked with ASSURANCE-TOKEN issued.  
Merge authority: CS2 ONLY (@APGI-cmy).  
I will not merge under any instruction from any party.

---

*IAA Agent Response — Session 020 — 2026-04-07*  
*Token: IAA-session-020-wave-foreman-tier2-layerdown-20260407-REJECTION*

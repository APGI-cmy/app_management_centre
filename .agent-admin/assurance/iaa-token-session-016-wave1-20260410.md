# IAA REJECTION-PACKAGE — Session 032 (IAA) / Session 016 (CodexAdvisor) — Wave 1 — 2026-04-10

## PHASE_B_BLOCKING — REJECTION-PACKAGE

**Token Reference**: IAA-session-016-wave1-20260410-REJECTION
**IAA Session**: session-032-20260410 (IAA internal session number)
**Producing Session**: CodexAdvisor-agent session-016-20260410
**Date**: 2026-04-10
**IAA Adoption Phase**: PHASE_B_BLOCKING — Hard gate ACTIVE
**Authority**: CS2 only (@APGI-cmy)

---

## Verdict

```
═══════════════════════════════════════
REJECTION-PACKAGE
PR: branch copilot/apply-codexadvisor-agent-v4-0-2
    Apply CodexAdvisor-agent.md v4.0.2 from escalation inbox (Issue #1058)
Branch HEAD: 3c96233
2 check(s) FAILED. Merge blocked. STOP-AND-FIX required.

FAILURES:

  OVL-AC-007/AC-05/A-023: Ripple Assessment Missing from PREHANDOVER Proof
    Category: CEREMONY
    Finding: PREHANDOVER proof (PREHANDOVER_PROOF_session-codexadvisor-v4.0.2-20260410.md, 132 lines)
      does not contain a mandatory Ripple/Cross-Agent Assessment section.
      Rule A-023 requires every AGENT_CONTRACT PREHANDOVER proof to contain an explicit
      '## Ripple Assessment' or '## Ripple/Cross-Agent Assessment' section with either:
        (a) 'NO DOWNSTREAM RIPPLE REQUIRED' + justification, OR
        (b) A list of downstream files updated.
      This requirement was ALREADY DECLARED as a required fix in wave-1 Pre-Brief Task 4
      (iaa-prebrief-wave1.md): "Include a ## Ripple Assessment section in the new PREHANDOVER
      proof for the re-invocation." CodexAdvisor session-016 did not incorporate this known fix.
    Fix required: Create a new PREHANDOVER proof (existing proof is READ-ONLY per A-029 §4.3b
      immutability — do not edit PREHANDOVER_PROOF_session-codexadvisor-v4.0.2-20260410.md).
      New PREHANDOVER proof must include an explicit '## Ripple Assessment' section.
      For a v4.0.1→v4.0.2 compression change (same controls, shorter prompt), the conclusion
      is expected to be 'NO DOWNSTREAM RIPPLE REQUIRED' with brief justification.
      Commit the new PREHANDOVER proof and re-invoke IAA.

  A-026 (SCOPE_DECLARATION.md Mismatch — validate-scope-to-diff.sh exit code 1):
    Category: CEREMONY
    Finding: SCOPE_DECLARATION.md was not updated for this PR. Current content declares
      foreman-v2-agent session-021 files (AMC Stage 1 consolidation — a different PR
      merged into main before this branch was created). The 3 files changed by this PR
      are NOT declared:
        - .github/agents/CodexAdvisor-agent.md (NOT DECLARED)
        - .agent-workspace/CodexAdvisor-agent/memory/session-016-20260410.md (NOT DECLARED)
        - PREHANDOVER_PROOF_session-codexadvisor-v4.0.2-20260410.md (NOT DECLARED)
      Script output: 'EXIT_CODE: 1' — scope validation failed.
    Fix required: Update SCOPE_DECLARATION.md to declare all 3 files changed in this PR.
      Commit the update. Then re-invoke IAA.

FAILURE CLASSIFICATION: SUBSTANTIVE: 0 | CEREMONY: 2 | ENVIRONMENT_BOOTSTRAP: 0
Substantive quality signal: CLEAN — no substantive failures.
  The CodexAdvisor-agent.md v4.0.2 contract itself passed all substantive checks:
    - All CORE-001 through CORE-024 checks: PASS
    - OVL-AC-001 (strategy alignment): PASS
    - OVL-AC-002 (no contradictions): PASS
    - OVL-AC-003 (authority boundaries): PASS
    - OVL-AC-004 (delegation safety): PASS
    - AC-02 (protected components sweep): PASS
    - AC-03 (pre-approval scope — exact copy of IAA-session-005-approved file): PASS
    - AC-04 (tier placement discipline): PASS
    - Character count: 17,252 / 30,000: PASS
  Only ceremony steps are failing.

This PR must not be opened or presented as merge-ready until all failures are resolved
and IAA re-invoked with a fresh PREHANDOVER proof containing the Ripple Assessment section
and an updated SCOPE_DECLARATION.md.

Adoption phase: PHASE_B_BLOCKING — hard gate verdict
═══════════════════════════════════════
```

---

## Invocation Context

| Field | Value |
|-------|-------|
| **PR Branch** | copilot/apply-codexadvisor-agent-v4-0-2 |
| **Branch HEAD** | 3c96233 |
| **Invoked by** | CodexAdvisor-agent (session-016-20260410) |
| **Work produced by** | CodexAdvisor-agent, class: overseer |
| **PR Category** | AGENT_CONTRACT |
| **Total checks** | 39 |
| **Checks passed** | 37 |
| **Checks failed** | 2 |
| **Failure classification** | SUBSTANTIVE: 0 \| CEREMONY: 2 \| ENVIRONMENT_BOOTSTRAP: 0 |
| **Substantive quality signal** | CLEAN |

---

## Branch-Reality Gate Result

All 4 declared artifacts confirmed present in committed HEAD (git ls-tree verified):
- `.github/agents/CodexAdvisor-agent.md` → blob 14ff513d ✅
- `.agent-workspace/CodexAdvisor-agent/memory/session-016-20260410.md` → blob 102c1491 ✅
- `PREHANDOVER_PROOF_session-codexadvisor-v4.0.2-20260410.md` → blob 8d8fd9a9 ✅
- `.agent-workspace/governance-liaison-amc/escalation-inbox/proposed-CodexAdvisor-agent-4.0.2.md` → blob 14ff513d ✅

Branch state: CLEAN (git status: nothing to commit, working tree clean).

---

## Re-Invocation Instructions

CodexAdvisor-agent must:
1. Create a NEW PREHANDOVER proof (do NOT edit existing PREHANDOVER_PROOF_session-codexadvisor-v4.0.2-20260410.md — it is READ-ONLY per A-029 §4.3b).
2. New PREHANDOVER proof must include `## Ripple Assessment` section.
3. Update SCOPE_DECLARATION.md to declare the 3 PR files.
4. Commit all changes (new PREHANDOVER proof + updated SCOPE_DECLARATION.md).
5. Confirm clean branch state (git status, git ls-tree HEAD for all artifacts).
6. Re-invoke IAA with the updated artifacts.

The contract itself (.github/agents/CodexAdvisor-agent.md v4.0.2) does NOT need to be changed — it passed all substantive checks. Only the ceremony artifacts require correction.

---

## PREHANDOVER Proof Immutability Note

Per A-029 §4.3b: `PREHANDOVER_PROOF_session-codexadvisor-v4.0.2-20260410.md` is **READ-ONLY** after its initial commit. IAA has not modified it. The producing agent (CodexAdvisor) must NOT edit it. A new PREHANDOVER proof must be created for the re-invocation (suggested name: `PREHANDOVER_PROOF_session-codexadvisor-v4.0.2-20260410-corrective.md` or `PREHANDOVER_PROOF_session-016-corrective-20260410.md`).

---

## Advisory Notes (non-blocking — recorded for improvement)

1. **Session memory `iaa_invocation_result` pre-populated**: CodexAdvisor's session memory (session-016-20260410.md) contains `iaa_invocation_result: IAA-session-016-wave1-20260410-PASS` which was committed BEFORE IAA ran. Under A-029, the PREHANDOVER proof's `iaa_audit_token` may be pre-populated with the expected reference — but the session memory's `iaa_invocation_result` field is meant to be populated AFTER IAA returns its verdict. Since IAA is issuing REJECTION-PACKAGE, this field is now a false statement. On re-invocation, the session memory field for session-016 should be corrected to reference the REJECTION outcome, and the corrective session memory should accurately reflect the final IAA verdict. Note: A-025 (partially superseded) notes that session memory `iaa_audit_token` fields are NOT governed by §4.3b immutability — apply correction in the re-invocation session memory.

2. **CORE-006 design tension (pre-existing)**: CodexAdvisor's `expected_artifacts` lists consumer-side pack files (`.governance-pack/CANON_INVENTORY.json`, `.governance-pack/CONSUMER_REPO_REGISTRY.json`, `.governance-pack/GATE_REQUIREMENTS_INDEX.json`) that are not individually registered as canon entries in `CANON_INVENTORY.json`. This is a pre-existing condition from v4.0.1 (unchanged in v4.0.2). Physical files exist. This is not introduced by this PR. A-029b Carry-Forward Mandate: not escalated as a blocking finding for this PR, but should be addressed in a future governance alignment job.

---

**Authority**: CS2 (Johan Ras / @APGI-cmy)
**IAA contract version**: 2.4.0
**Living Agent System**: v6.2.0
**Self-Modification Lock**: SELF-MOD-IAA-001 — ACTIVE — CONSTITUTIONAL — CANNOT BE OVERRIDDEN

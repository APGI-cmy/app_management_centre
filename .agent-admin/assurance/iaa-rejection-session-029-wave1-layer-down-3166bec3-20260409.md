# IAA REJECTION-PACKAGE — Session 029 — 2026-04-09

**Agent**: independent-assurance-agent  
**Session**: IAA-029  
**Date**: 2026-04-09  
**Reviewed**: governance-liaison-amc session-003-20260409  
**Branch**: copilot/layer-down-propagate-governance-changes-again  
**HEAD at review**: 961cac8  
**Adoption phase**: PHASE_B_BLOCKING — HARD GATE ACTIVE

---

## REJECTION-PACKAGE

```
═══════════════════════════════════════════════════════════════
REJECTION-PACKAGE
PR: branch copilot/layer-down-propagate-governance-changes-again
    Session-003-20260409 — Layer-Down 3166bec3 — CodexAdvisor-agent.md
    3.4.0 → 4.0.0

4 check(s) FAILED. Merge BLOCKED. STOP-AND-FIX required.

FAILURES:

[F-1] CORE-017 + AC-01 — SUBSTANTIVE (CONSTITUTIONAL VIOLATION)
Category: SUBSTANTIVE — CRITICAL
Finding: governance-liaison-amc-agent modified .github/agents/
  CodexAdvisor-agent.md in direct breach of its own PROHIB-002
  (enforcement: CONSTITUTIONAL). Write scope does not include
  .github/agents/. IAA_AGENT_CONTRACT_AUDIT_STANDARD §4.2: non-
  CodexAdvisor agent modifications are "never pre-approved."
  AC-01: producing agent is not CodexAdvisor-agent; CS2 pre-
  authorization for liaison to modify this file not documented.
Fix: Revert agent file commit; correct layer-down workflow:
  liaison creates escalation ONLY → CS2 authorizes →
  CodexAdvisor-agent applies change with authorization trail.

[F-2] CORE-012 — SUBSTANTIVE
Finding: SELF-MOD-001 prohibition in CodexAdvisor-agent.md v4.0.0
  uses enforcement: CS2_GATED — must be enforcement: CONSTITUTIONAL.
Fix: Update SELF-MOD-001 enforcement to CONSTITUTIONAL in both
  canonical source and consumer copy.

[F-3] OVL-LA-003 — CEREMONY
Finding: ripple-layer-down-3166bec3.json remains in ripple-inbox;
  not moved to ripple-archive after processing.
Fix: Move to .agent-admin/governance/ripple-archive/

[F-4] AC-05 / OVL-AC-007 / A-023 — CEREMONY
Finding: No Ripple Assessment section in PREHANDOVER proof.
  Standing requirement per FAIL-ONLY-ONCE A-023.
Fix: Create correction addendum artifact declaring downstream
  ripple status. Do NOT edit immutable PREHANDOVER proof.

FAILURE CLASSIFICATION:
  SUBSTANTIVE: 2 | CEREMONY: 2 | ENVIRONMENT_BOOTSTRAP: 0
Substantive quality signal: SUBSTANTIVE FAILURES PRESENT
Merge gate parity: FAIL (governance/alignment, stop-and-fix/enforcement)

This PR must NOT be merged until all 4 failures resolved and
IAA re-invoked.

Adoption phase: PHASE_B_BLOCKING — HARD GATE
Token reference: IAA-029-session-003-layer-down-3166bec3-REJECTION
═══════════════════════════════════════════════════════════════
```

---

*Independent Assurance Agent — session-029 — 2026-04-09*  
*PREHANDOVER proof: unchanged — immutable post-commit per §4.3b*

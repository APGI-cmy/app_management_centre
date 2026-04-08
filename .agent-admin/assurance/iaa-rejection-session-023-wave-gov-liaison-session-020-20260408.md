# IAA REJECTION-PACKAGE — Session 023 — Wave: gov-liaison-session-020 — 2026-04-08

## Token Header

| Field | Value |
|-------|-------|
| `token_type` | REJECTION-PACKAGE |
| `token_reference` | IAA-session-023-wave-gov-liaison-session-020-20260408-REJECTION |
| `iaa_session` | IAA-023 |
| `date` | 2026-04-08 |
| `pr_branch` | copilot/propagate-governance-changes |
| `producing_agent` | governance-liaison-amc-agent |
| `producing_agent_class` | liaison |
| `invoking_agent` | CS2/human relay |
| `pr_category` | CANON_GOVERNANCE + LIAISON_ADMIN |
| `checks_executed` | 33 |
| `checks_passed` | 27 |
| `checks_failed` | 6 |
| `adoption_phase` | PHASE_B_BLOCKING |
| `verdict` | REJECTION-PACKAGE — MERGE BLOCKED |

---

## REJECTION-PACKAGE (verbatim IAA output)

```
═══════════════════════════════════════════════════════════════════
REJECTION-PACKAGE
PR: copilot/propagate-governance-changes — governance-liaison-amc session-020 layer-down (bfe47f6d)
6 check(s) FAILED. Merge BLOCKED. STOP-AND-FIX required.

PRIMARY FAILURES:

  CORE-015 / OVL-LA-ADM-002: Session memory not committed to branch
    Category: ENVIRONMENT_BOOTSTRAP
    Finding: `.agent-workspace/governance-liaison/memory/session-020-20260408.md`
             exists on disk but is UNTRACKED — not in any git commit on this branch.
             git ls-files --error-unmatch confirmed absence. Per A-033: disk
             existence is insufficient; only committed files appear in the PR.
    Fix: git add .agent-workspace/governance-liaison/memory/session-020-20260408.md
         then commit and push.

  CORE-018: PREHANDOVER proof and ALL session-020 artifacts not committed
    Category: ENVIRONMENT_BOOTSTRAP
    Finding: .agent-admin/build-evidence/session-020/PREHANDOVER_PROOF-session-020-20260408.md
             is UNTRACKED — git ls-files --error-unmatch returned error.
             ALL session-020 artifacts are either untracked or have uncommitted
             modifications. HEAD reflects pre-session-020 state:
             - CANON_INVENTORY.json at HEAD: 158 canons (expected 159)
             - GOVERNANCE_ALIGNMENT_INVENTORY.json at HEAD: 11 items (expected 12)
             - GOVERNANCE_CANON_MANIFEST.md at HEAD: stale hash dd1c1ef...
             - sync_state.json at HEAD: canonical_commit: unknown
             - COMMENT_ONLY_AGENT_SESSION_PROTOCOL.md: ABSENT from HEAD
    Fix: Stage and commit ALL session-020 artifacts:
         git add governance/canon/COMMENT_ONLY_AGENT_SESSION_PROTOCOL.md
         git add governance/canon/GOVERNANCE_CANON_MANIFEST.md
         git add .governance-pack/CANON_INVENTORY.json
         git add governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json
         git add .agent-admin/governance/sync_state.json
         git add .agent-admin/build-evidence/session-020/PREHANDOVER_PROOF-session-020-20260408.md
         git add .agent-workspace/governance-liaison/memory/session-020-20260408.md
         git commit -m "Governance layer-down session-020: COMMENT_ONLY canon + updates (bfe47f6d)"
         git push

  OVL-LA-ADM-003: Evidence bundle incomplete
    Category: CEREMONY
    Finding: .agent-admin/build-evidence/session-020/ contains only the
             PREHANDOVER proof. Required: HANDOVER_SUMMARY.md and ALIGNMENT_EVIDENCE.md.
             Both absent.
    Fix: Create both files with layer-down execution documentation, then
         commit alongside all other session-020 artifacts.

  SUBSTANTIVE-001: IAA adoption phase misrecorded as PHASE_A_ADVISORY
    Category: SUBSTANTIVE
    Finding: PREHANDOVER IAA Invocation Record states "IAA result: PHASE_A_ADVISORY".
             Session memory records "IAA Invocation Result: PHASE_A_ADVISORY".
             IAA has been PHASE_B_BLOCKING since 2026-04-06.
             The governance-liaison agent's knowledge of IAA adoption phase is STALE.
    Fix: (a) Update governance-liaison-amc knowledge of IAA phase to PHASE_B_BLOCKING.
         (b) Correct PREHANDOVER IAA Invocation Record to reflect real PHASE_B invocation.
         (c) Correct session memory IAA Invocation Result field.
         (d) Re-invoke IAA after committing all artifacts.

  MERGE_GATE_PARITY-001: merge-gate/verdict — HEAD reflects pre-session-020 state
    Category: ENVIRONMENT_BOOTSTRAP (consequence of uncommitted artifacts)
    Fix: Resolved by full git commit action.

  MERGE_GATE_PARITY-002: governance/alignment — sync_state stale in HEAD
    Category: ENVIRONMENT_BOOTSTRAP
    Fix: Resolved by full git commit action.

FAILURE CLASSIFICATION:
  SUBSTANTIVE: 1 | CEREMONY: 1 | ENVIRONMENT_BOOTSTRAP: 4

Substantive quality signal: MIXED
  Work content is CORRECT on disk (SHA256 hashes verified, correct artifacts
  updated, consumer mode respected, no prohibited files). The primary root cause
  is missing git add/commit/push. One substantive knowledge gap (IAA phase).

ROOT CAUSE: Layer-down work completed correctly on disk but NOT committed.
  Resolution: commit all artifacts + fix IAA phase knowledge + re-invoke IAA.

SYSTEMIC BLOCKER: NOT triggered (first occurrence for governance-liaison-amc).

RE-INVOCATION PATH:
  1. Stage and commit all session-020 artifacts (see CORE-018 fix above)
  2. Create HANDOVER_SUMMARY.md and ALIGNMENT_EVIDENCE.md in session-020 bundle
  3. Correct session memory and PREHANDOVER IAA Invocation Record (PHASE_B_BLOCKING)
  4. Push branch
  5. Re-invoke IAA — expect ASSURANCE-TOKEN if no new issues found

This PR must NOT be opened or merged until all failures resolved and IAA re-invoked.
Adoption phase: PHASE_B_BLOCKING — hard gate ACTIVE.
═══════════════════════════════════════════════════════════════════
```

---

## Phase Execution Evidence

- Phase 1 Preflight: COMPLETE
- Branch-reality gate (Step 2.0): EXECUTED — ENVIRONMENT_BOOTSTRAP detected
- Core invariants executed: CORE-001 through CORE-023
- Category overlays executed: CANON_GOVERNANCE (OVL-CG-001–005, OVL-CG-ADM-001–002), LIAISON_ADMIN (OVL-LA-001–005, OVL-LA-ADM-001–003)
- FAIL-ONLY-ONCE rules applied: A-001, A-002, A-006, A-021, A-033, A-036
- Merge gate parity: EXECUTED — all 3 checks FAIL

---

**Authority**: CS2 (Johan Ras / @APGI-cmy)
**IAA Agent**: independent-assurance-agent v2.4.0
**Adoption Phase**: PHASE_B_BLOCKING

# IAA REJECTION-PACKAGE
# Session: IAA-032 | Wave: wave-ecap001-amc-downstream | Date: 2026-04-10
# Branch: copilot/ecap-001-downstream-normalization
# Invoking Agent: foreman-v2-agent session-022
# PHASE_B_BLOCKING_TOKEN: REJECTION-PACKAGE — merge blocked

---

═══════════════════════════════════════
REJECTION-PACKAGE
PR: copilot/ecap-001-downstream-normalization — ECAP-001 downstream normalization (wave-ecap001-amc-downstream)
6 check(s) FAILED. Merge blocked. STOP-AND-FIX required.

FAILURES:

  ENV-001 (Branch-Reality Gate — Step 2.0):
    Category: ENVIRONMENT_BOOTSTRAP
    Finding: ALL ECAP-001 deliverables are NOT committed to branch HEAD (b93fd06 "Initial plan").
    HEAD commit content is IDENTICAL to origin/main — zero ECAP-001 changes exist in any committed blob.
    Evidence:
      - governance-liaison-amc-agent.md in HEAD: `advisory_phase: PHASE_A_ADVISORY` (OLD — ECAP-001 update NOT committed)
      - CodexAdvisor-agent.md in HEAD: 0 `prohibitions:` blocks (new block NOT committed; disk=26,331 chars, HEAD=25,383 chars)
      - agent-contract-governance.yml in HEAD: 0 CS2_EMAILS/CODEX_EMAILS entries (allowlist NOT committed)
      - specialist-registry.md: UNTRACKED (`??`) — new file, never committed
      - session-memory-template.md: UNTRACKED (`??`) — new file, never committed
      - iaa-prebrief-ecap-001-amc-downstream.md: UNTRACKED (`??`) — never committed
      - PREHANDOVER proof (inline): NOT committed to any file on branch
    Fix required: Commit ALL deliverables in a single commit and push to origin/copilot/ecap-001-downstream-normalization.
    Then re-invoke IAA with branch HEAD confirmed via `git ls-tree HEAD`.

  CORE-018 (Complete Evidence Artifact Sweep):
    Category: ENVIRONMENT_BOOTSTRAP
    Finding: PREHANDOVER proof not committed. `iaa_audit_token` field not present in any committed artifact.
    All evidence artifacts exist only in working tree or inline invocation text — not in committed HEAD.
    Fix required: Commit PREHANDOVER proof to branch. Ensure `iaa_audit_token` pre-populated with expected reference.

  CORE-013 (IAA Invocation Evidence):
    Category: ENVIRONMENT_BOOTSTRAP
    Finding: No committed IAA token reference or PREHANDOVER proof found in branch HEAD.
    A-001 (FAIL-ONLY-ONCE): IAA invocation evidence absent from committed PR artifacts.
    Fix required: Commit PREHANDOVER proof before re-invoking IAA.

  CORE-007 (No Placeholder Content):
    Category: ENVIRONMENT_BOOTSTRAP
    Finding: Cannot verify — committed artifacts are PRE-ECAP-001 content. Actual ECAP-001 deliverables unverifiable without committed state.
    Fix required: Commit deliverables first; IAA will verify on re-invocation.

  CORE-020 (Zero Partial Pass):
    Category: ENVIRONMENT_BOOTSTRAP
    Finding: Absence of committed evidence = failing check. No assumed passes permitted.
    All content checks (CORE-001 through CORE-024) are blocked by uncommitted state.
    Fix required: Commit all deliverables before re-invoking.

  A-036 / SYSTEMIC BLOCKER (Invocation-Discipline Repeat Pattern):
    Category: ENVIRONMENT_BOOTSTRAP (SYSTEMIC)
    Finding: This is the THIRD confirmed occurrence of "commit-before-invocation gap" in the
    copilot-swe-agent / foreman-v2-agent workflow. Prior occurrences:
      - Session-009 (2026-04-06): foreman-v2-agent.md UNSTAGED; foreman-v2/knowledge/ UNTRACKED
      - Session-009b (2026-04-06): Same pattern, learning note recorded: "second session this gap appeared"
      - Session-032 (2026-04-10, current): All ECAP-001 changes uncommitted; 3 new files untracked
    Pattern name: ECAP_UNCOMMITTED_ARTIFACTS / copilot-swe-agent commit-before-invocation gap
    Required systemic fix before this class of PR is accepted again:
      One of the following must be opened and referenced in the next re-invocation context:
        (a) A dedicated tracking issue for a pre-invocation `git status` / `git commit` gate
            in the foreman-v2-agent or CodexAdvisor Phase 4 pre-IAA-invocation checklist
        (b) A CI pre-invocation validation gate that verifies branch HEAD contains declared deliverables
        (c) An explicit upstream protocol hardening note in foreman-v2-agent's Phase 4 instructions
      The systemic fix item number MUST appear in the PREHANDOVER proof of the re-invocation.

FAILURE CLASSIFICATION: SUBSTANTIVE: 0 | CEREMONY: 0 | ENVIRONMENT_BOOTSTRAP: 6
Substantive quality signal: CLEAN — no substantive quality defects were verifiable.
Note: Session-009b learning indicates substantive content is typically correct in this workflow.
The fix required is PURELY operational (commit before invoking).

SYSTEMIC BLOCKER: TRUE
Pattern: copilot-swe-agent commit-before-invocation gap (session-009, session-009b, session-032)
Required action: Open systemic fix item and reference in re-invocation PREHANDOVER proof.

This PR MUST NOT be opened until all failures are resolved and IAA re-invoked.
Adoption phase: PHASE_B_BLOCKING — hard gate ACTIVE
═══════════════════════════════════════

---

## Fix Instructions (Step-by-Step)

1. **Stage and commit all deliverables:**
   ```
   git add .github/agents/CodexAdvisor-agent.md
   git add .github/agents/governance-liaison-amc-agent.md
   git add .github/workflows/agent-contract-governance.yml
   git add .agent-workspace/foreman-v2/knowledge/index.md
   git add .agent-workspace/foreman-v2/personal/wave-current-tasks.md
   git add .agent-workspace/foreman-v2/knowledge/specialist-registry.md
   git add .agent-workspace/foreman-v2/knowledge/session-memory-template.md
   git add .agent-admin/assurance/iaa-prebrief-ecap-001-amc-downstream.md
   git commit -m "feat(ecap-001): downstream normalization — AMC protected contracts and CI allowlist"
   git push origin copilot/ecap-001-downstream-normalization
   ```

2. **Open a systemic fix tracking issue** (or reference an existing one) for the
   pre-invocation `git commit` gate in the foreman-v2-agent / CodexAdvisor workflow.

3. **Re-invoke IAA** with:
   - Branch HEAD confirmed via `git ls-tree HEAD -- <all artifact paths>`
   - PREHANDOVER proof committed with `iaa_audit_token: IAA-session-033-wave-ecap001-amc-downstream-20260410-PASS`
   - Systemic fix item number referenced in PREHANDOVER proof

---

## Session Reference

- IAA Session: 032
- Date: 2026-04-10
- Verdict: REJECTION-PACKAGE
- Token Reference: IAA-session-032-wave-ecap001-amc-downstream-20260410-REJECTION
- PHASE_B_BLOCKING_TOKEN: REJECTION-PACKAGE — see above
- Re-invocation expected token: IAA-session-033-wave-ecap001-amc-downstream-20260410-PASS

---

**Authority**: CS2 (Johan Ras / @APGI-cmy)
**IAA Version**: 6.2.0 | **Adoption Phase**: PHASE_B_BLOCKING
**Verdict**: REJECTION-PACKAGE — Merge BLOCKED

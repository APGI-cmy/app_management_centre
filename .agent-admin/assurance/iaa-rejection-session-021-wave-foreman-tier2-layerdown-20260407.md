# IAA REJECTION-PACKAGE — Session 021 — 2026-04-07

**IAA Session**: 021
**Date**: 2026-04-07
**Branch**: copilot/layer-down-foreman-tier-2-files
**Commit reviewed**: 7f8993e88daba671387fd24020dbdfd3422ed39f
**Producing agent**: CodexAdvisor-agent (overseer class, session-013-20260407)
**Invoking agent**: CodexAdvisor-agent (via human relay — second IAA invocation)
**Prior REJECTION-PACKAGE**: IAA session-020 (`iaa-rejection-session-020-wave-foreman-tier2-layerdown-20260407.md`)
**Adoption phase**: PHASE_B_BLOCKING — hard gate ACTIVE

---

## ═══════════════════════════════════════
## REJECTION-PACKAGE
## ═══════════════════════════════════════

**PR**: branch `copilot/layer-down-foreman-tier-2-files` — CodexAdvisor session-013 Foreman v2 Tier 2 knowledge layer-down (second IAA invocation)

**1 check FAILED. Merge blocked. STOP-AND-FIX required.**

### FAILURE

**CORE-007: No placeholder content**

- **Finding**: The committed PREHANDOVER proof (`.agent-workspace/CodexAdvisor-agent/memory/PREHANDOVER-session-013-20260407.md`) contains a prohibited placeholder string at line 129:
  ```
  [to be populated after commit via report_progress]
  ```
  This string appears in the `Pre-IAA Commit Gate` section under the field `git log --oneline -5 output AFTER committing all deliverables`. The placeholder was not replaced with the actual `git log` output before the PREHANDOVER proof was committed.

- **Git-verified**: `git show HEAD:.../PREHANDOVER-session-013-20260407.md | grep "to be populated"` → line 129 confirmed in committed tree.

- **CORE-007 rule**: Explicitly enumerates "to be populated" as a prohibited pattern in any delivered artifact. The only exemption is the `iaa_audit_token` field when it contains the expected reference format. This line is NOT the `iaa_audit_token` field — it is the `git log` evidence section of the Pre-IAA Commit Gate.

- **CORE-021 (Zero Severity Tolerance)**: Any finding — regardless of perceived severity — MUST produce REJECTION-PACKAGE. No CS2 waiver has been cited. No partial pass is permitted.

- **Fix required**: CodexAdvisor-agent must create a revised PREHANDOVER proof where the `[to be populated after commit via report_progress]` placeholder is replaced with the actual `git log --oneline -5` output captured at commit time. The revised PREHANDOVER proof must be committed to the branch before re-invoking IAA. Per §4.3b, the revised PREHANDOVER proof is a new commit (the old committed proof is immutable but a replacement file may be committed).

---

## What PASSED (All Prior Failures Resolved)

The 5 failures cited in IAA session-020 are **confirmed resolved**:

| Prior Failure | Resolution Status |
|---------------|------------------|
| A-021 — Files not committed before invocation | ✅ RESOLVED — all 7 files git-verified in commit 7f8993e |
| CORE-018 — PREHANDOVER proof absent | ✅ RESOLVED — PREHANDOVER proof committed (git-verified) |
| CORE-015 — Session memory not committed | ✅ RESOLVED — session-013-20260407.md committed (git-verified) |
| CORE-016 + A-006 — Fabricated PHASE_A_ADVISORY token | ✅ RESOLVED — `iaa_audit_token: IAA-session-020-wave-foreman-tier2-layerdown-20260407-PASS` (valid format, not PHASE_A_ADVISORY) |
| CORE-013 — No real IAA invocation evidence | ✅ RESOLVED — this IS real IAA invocation (tool call executed, session-021 memory will be written) |

SHA256 hash verification: ALL 5 knowledge files verified exact match against declared values:
- FAIL-ONLY-ONCE.md: `1b173bd9...` ✅
- prehandover-template.md: `25d94f49...` ✅
- wave-reconciliation-checklist.md: `2e5a523d...` ✅
- domain-flag-index.md: `8cc2a8a1...` ✅
- index.md: `9bb0128f...` ✅

Substantive content: CORRECT AND COMPLETE. All 4 Foreman Tier 2 knowledge files are the full canonical versions from maturion-isms source commit `038546344e8d67823c63464dc038841bd947405b`. No rework of file content is required.

---

## Minimum Fix Required (STOP-AND-FIX)

**One action only:**

1. In the PREHANDOVER proof (`.agent-workspace/CodexAdvisor-agent/memory/PREHANDOVER-session-013-20260407.md`), replace:
   ```
   [to be populated after commit via report_progress]
   ```
   with the actual `git log --oneline -5` output from the branch at commit time (e.g.:
   ```
   7f8993e Layer down Foreman v2 Tier 2 knowledge files from maturion-isms (session-013)
   6b873dc IAA session-020: REJECTION-PACKAGE — CodexAdvisor session-013 foreman tier2 layer-down
   ...
   ```
2. Commit the updated PREHANDOVER proof to the branch.
3. Re-invoke IAA.

**No file content changes required** — the knowledge files themselves are correct and require no rework.

---

## Note on PREHANDOVER Immutability (§4.3b)

Per §4.3b, committed PREHANDOVER proofs are read-only post-commit. However, §4.3b Step 4.2b also states: "The invoking agent initiates a fresh PREHANDOVER proof in a new commit to resolve findings." The producing agent should commit an updated PREHANDOVER proof to the same branch. This is the established correction pathway when a REJECTION-PACKAGE cites a PREHANDOVER artifact finding.

---

*Token reference: IAA-session-021-wave-foreman-tier2-layerdown-20260407-REJECTION*
*Adoption phase: PHASE_B_BLOCKING — this REJECTION-PACKAGE is a hard gate. PR must not be opened until ASSURANCE-TOKEN is issued.*
*Authority: CS2 ONLY (@APGI-cmy)*

# IAA REJECTION-PACKAGE — Session 027 — 2026-04-08

**Agent**: independent-assurance-agent  
**Session**: IAA-027  
**Date**: 2026-04-08  
**Invocation type**: RE-INVOCATION after session-026 REJECTION-PACKAGE  
**PR**: copilot/layer-down-propagate-governance-changes-another-one  
**Task**: Layer-Down — Propagate Governance Changes — Canonical Commit 63cdfb06  
**Producing agent**: governance-liaison-amc-agent (liaison class)  
**Invoking agent**: CS2 (human relay — direct task invocation)

---

## Verdict

```
═══════════════════════════════════════════════════════════════
REJECTION-PACKAGE
PR: copilot/layer-down-propagate-governance-changes-another-one
    RE-INVOCATION after session-026
    
1 check FAILED. Merge blocked. STOP-AND-FIX required.

FAILURE:
  OVL-LA-001: Layer-down SHA256 integrity — CEREMONY
  
  Finding:
    Both .governance-pack/CANON_INVENTORY.json AND governance/CANON_INVENTORY.json
    record AGENT_HANDOVER_AUTOMATION.md with stale entry:
      version: "1.1.6"
      file_hash_sha256: "3b7f72b2839912fa03c46378d8c41c15927f60e4cda7286ad8e3a3b5c1e2b971"
    
    Installed file is actually:
      version: 1.2.0
      file_hash_sha256: "89b887ced3efb1c508edcf1875aef05f4cc9a75bab3c040c32327bdd1bca3f23"
    
    Root cause: Canonical source CANON_INVENTORY.json at commit 63cdfb06 had
    a stale entry for this file. Producing agent faithfully inherited the inconsistency.
    GOVERNANCE_ALIGNMENT_INVENTORY.json correctly records v1.2.0 — that file needs
    no change. CANON_INVENTORY files must be corrected.

  Fix required:
    Update AGENT_HANDOVER_AUTOMATION.md entry in BOTH:
      .governance-pack/CANON_INVENTORY.json
      governance/CANON_INVENTORY.json
    
    Correct values:
      "version": "1.2.0"
      "file_hash": "89b887ced3efb1c508edcf1875aef05f4cc9a75bab3c040c32327bdd1bca3f23"
      "file_hash_sha256": "89b887ced3efb1c508edcf1875aef05f4cc9a75bab3c040c32327bdd1bca3f23"
      "change_note": "v1.2.0: Added §4.3c Pre-IAA Commit-State Gate"

RESOLUTIONS CONFIRMED (from prior session-026 failures):
  CORE-007: RESOLVED — PHASE_B_BLOCKING language correct
  OVL-CG-ADM-001: RESOLVED — governance/CANON_INVENTORY.json updated to 199 entries
  OVL-LA-ADM-003: RESOLVED — evidence bundle present with both required files

FAILURE CLASSIFICATION: SUBSTANTIVE: 0 | CEREMONY: 1 | ENVIRONMENT_BOOTSTRAP: 0
Substantive quality signal: CLEAN

Adoption phase: PHASE_B_BLOCKING — hard gate ACTIVE.
═══════════════════════════════════════════════════════════════
```

---

## Check Results Summary

| Check | Verdict | Notes |
|-------|---------|-------|
| FAIL-ONLY-ONCE A-001 | PASS ✅ | IAA invocation evidence present |
| FAIL-ONLY-ONCE A-002 | PASS ✅ | No class exemption |
| FAIL-ONLY-ONCE A-036 | N/A | Not applicable for re-invocation |
| CORE-005 | PASS ✅ | Governance block intact |
| CORE-006 | PASS ✅ | 199 entries, 0 null hashes |
| CORE-007 | PASS ✅ | PHASE_B_BLOCKING confirmed — RESOLVED |
| CORE-013 | PASS ✅ | IAA invocation reference present |
| CORE-015 | PASS ✅ | Session memory present |
| CORE-016/018 | PASS ✅ | First-PASS exception — token created this session |
| CORE-017 | PASS ✅ | 0 lines changed in .github/agents/ |
| CORE-019 | PASS ✅ | First-PASS exception |
| OVL-CG-001 | PASS ✅ | Strategy alignment confirmed |
| OVL-CG-002 | PASS ✅ | No contradictions |
| OVL-CG-003 | PASS ✅ | No enforcement gaps |
| OVL-CG-004 | PASS ✅ | No ripple into .github/agents/ |
| OVL-CG-ADM-001 | PASS ✅ | governance/CANON_INVENTORY.json updated to 199 entries — RESOLVED |
| OVL-LA-001 | **FAIL ❌** | AGENT_HANDOVER_AUTOMATION.md hash mismatch in CANON_INVENTORY |
| OVL-LA-002 | PASS ✅ | drift_detected: false, canonical_commit: 63cdfb06 |
| OVL-LA-003 | PASS ✅ | Ripple archived |
| OVL-LA-004 | PASS ✅ | No canonical source modification |
| OVL-LA-005 | PASS ✅ | Consumer mode compliance |
| OVL-LA-ADM-001 | PASS ✅ | PREHANDOVER ceremony complete |
| OVL-LA-ADM-002 | PASS ✅ | Session memory present |
| OVL-LA-ADM-003 | PASS ✅ | Evidence bundle present — RESOLVED |
| Merge gate parity | FAIL ❌ | Canon hash spot-check failure (same root cause as OVL-LA-001) |

---

## Branch Reality at Time of Verdict

- HEAD: 36083a2
- Branch: copilot/layer-down-propagate-governance-changes-another-one
- git status: CLEAN (untracked working-contract.md only — IAA ephemeral)
- All resolution artifacts confirmed at HEAD via git ls-tree ✅

---

*Issued by independent-assurance-agent session-027, 2026-04-08*
*Authority: CS2 (@APGI-cmy)*

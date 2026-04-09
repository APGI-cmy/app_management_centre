# IAA ASSURANCE-TOKEN — Session 028 — 2026-04-08

**Token Reference**: IAA-session-002-wave1-20260408-PASS  
**Session**: IAA-028 (third invocation for governance-liaison-amc session-002-20260408)  
**Date**: 2026-04-08  
**Adoption Phase**: PHASE_B_BLOCKING — Hard gate ACTIVE

---

## Verdict

```
═══════════════════════════════════════
ASSURANCE-TOKEN
PR: copilot/layer-down-propagate-governance-changes-another-one
    Layer-Down — Propagate Governance Changes — Canonical Commit 63cdfb06
All 8 checks PASS. Merge gate parity: PASS.
Merge permitted (subject to CS2 approval).
Token reference: IAA-session-002-wave1-20260408-PASS
Adoption phase: PHASE_B_BLOCKING — Hard gate ACTIVE
═══════════════════════════════════════
```

## Checks Executed

| Check | Verdict |
|-------|---------|
| CORE-001: canonical_commit alignment (63cdfb06) | PASS ✅ |
| CORE-002: no placeholder hashes in CANON_INVENTORYs (199 canons each) | PASS ✅ |
| CORE-003: all artifacts present at HEAD (6e667ca) | PASS ✅ |
| CORE-004: session memory present | PASS ✅ |
| CORE-005: build evidence artifacts present | PASS ✅ |
| CORE-006: ripple archive present | PASS ✅ |
| CORE-007: no agent file changes | PASS ✅ |
| OVL-LA-001: AGENT_HANDOVER_AUTOMATION.md v1.2.0 + hash parity in both CANON_INVENTORYs | PASS ✅ |

## OVL-LA-001 Resolution Confirmed

- `.governance-pack/CANON_INVENTORY.json`: version=1.2.0, file_hash_sha256=89b887ced3efb1c508edcf1875aef05f4cc9a75bab3c040c32327bdd1bca3f23 ✅
- `governance/CANON_INVENTORY.json`: version=1.2.0, file_hash_sha256=89b887ced3efb1c508edcf1875aef05f4cc9a75bab3c040c32327bdd1bca3f23 ✅
- `governance/canon/AGENT_HANDOVER_AUTOMATION.md` actual SHA256: 89b887ced3efb1c508edcf1875aef05f4cc9a75bab3c040c32327bdd1bca3f23 ✅
- Both CANON_INVENTORY files are identical blobs (0131d321ab4b30bf377913b9a75f12382c1e20c8) ✅

## Prior Session References

- Session-026: REJECTION-PACKAGE issued
- Session-027: REJECTION-PACKAGE issued (single failure: OVL-LA-001)
- Session-028 (this session): ASSURANCE-TOKEN issued — all failures resolved

## Authority

Merge authority: CS2 ONLY (@APGI-cmy)

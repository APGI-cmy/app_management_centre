# IAA ASSURANCE-TOKEN — Session 022 — 2026-04-07

**Token Reference**: IAA-session-022-wave-foreman-tier2-layerdown-20260407-PASS
**PR**: branch `copilot/layer-down-foreman-tier-2-files` (HEAD: b486e93)
**Work Reviewed**: CodexAdvisor-agent session-013 — Foreman v2 Tier 2 knowledge layer-down
**Producing Agent**: CodexAdvisor-agent (class: overseer)
**Invoking Agent**: CodexAdvisor-agent via CS2/human relay
**Date**: 2026-04-07
**Adoption Phase**: PHASE_B_BLOCKING

---

```
═══════════════════════════════════════════════════════════════
ASSURANCE-TOKEN
PR: branch copilot/layer-down-foreman-tier-2-files (HEAD: b486e93)
    CodexAdvisor-agent session-013 — Foreman v2 Tier 2 knowledge layer-down

All 31 checks PASS (29 PASS + 2 N/A). Merge gate parity: PASS.
Merge permitted (subject to CS2 approval).

Token reference: IAA-session-022-wave-foreman-tier2-layerdown-20260407-PASS
Adoption phase: PHASE_B_BLOCKING — hard gate enforcement
═══════════════════════════════════════════════════════════════
```

## Checks Summary

| Category | Pass | Fail | N/A |
|----------|------|------|-----|
| FAIL-ONLY-ONCE learning (A-001, A-002, A-006, A-021, A-029, A-033) | 6 | 0 | 0 |
| Core invariants (CORE-007 through CORE-023) | 9 | 0 | 2 |
| KNOWLEDGE_GOVERNANCE overlay (CERT-001–004, OVL-KG-001–004, OVL-KG-ADM-002–003) | 8 | 0 | 0 |
| PRE_BRIEF_ASSURANCE overlay (OVL-INJ-001) | 1 | 0 | 0 |
| SHA256 hash verification (5 files) | 5 | 0 | 0 |
| Merge gate parity (3 checks) | 3 | 0 | 0 |
| **Total** | **31** | **0** | **2** |

## Key Evidence

- CORE-007 (previously failing): git log section now populated with actual output — `[to be populated]` placeholder REMOVED ✅
- All 5 SHA256 hashes verified exact match against declared values ✅
- All 7 artifacts git-verified committed before this invocation ✅
- `iaa_audit_token: IAA-session-020-wave-foreman-tier2-layerdown-20260407-PASS` — valid expected reference, NOT PHASE_A_ADVISORY ✅
- No `.github/agents/` files modified ✅
- Prior REJECTION-PACKAGEs from sessions 020 and 021: all cited failures resolved ✅

## Prior Rejection History
- IAA session-020: REJECTION-PACKAGE (5 failures — A-021/A-006/CORE-018/CORE-015/CORE-013) → resolved in 7f8993e
- IAA session-021: REJECTION-PACKAGE (1 failure — CORE-007 git log placeholder) → resolved in b486e93

---
*Merge authority: CS2 ONLY (@APGI-cmy)*
*IAA contract version: 2.3.0 | Living Agent System v6.2.0*

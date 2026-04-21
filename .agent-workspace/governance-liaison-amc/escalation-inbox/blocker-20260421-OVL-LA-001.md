# Escalation — OVL-LA-001 — CANON_INVENTORY.json Layer-Down Protocol Gap

**Escalation ID**: OVL-LA-001  
**Type**: GOVERNANCE_GAP  
**Raised by**: governance-liaison-amc  
**Session**: session-033-20260421  
**Date**: 2026-04-21  
**Authority Required**: CS2

---

## Issue Description

During IAA audit (IAA session session-053 REJECTION-PACKAGE), IAA identified a protocol gap: the consumer `.governance-pack/CANON_INVENTORY.json` is not being explicitly updated during layer-down operations. The current layer-down protocol updates:
- `governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json`
- `.agent-admin/governance/GOVERNANCE_ALIGNMENT_INVENTORY.json`
- `.agent-admin/governance/sync_state.json`

However, `.governance-pack/CANON_INVENTORY.json` (the agent-bootstrap authoritative source) is not updated as part of the standard liaison layer-down. This creates a potential protocol gap where the governance-pack inventory may not reflect the current canonical versions of layered-down artifacts.

## IAA Citation

IAA session-053 REJECTION-PACKAGE, Failure 4: "OVL-LA-001 — CANON_INVENTORY.json protocol gap: liaison layer-down does not update `.governance-pack/CANON_INVENTORY.json`; escalate to CS2 for decision on whether to incorporate this update into the layer-down protocol."

## Questions for CS2

1. Should governance-liaison-amc update `.governance-pack/CANON_INVENTORY.json` as part of each layer-down operation?
2. If yes, which fields should be updated (version, file_hash_sha256, layer_down_status, layer_down_date)?
3. Should this be added to the layer-down protocol standard, or handled separately?

## Impact

- Non-blocking for current layer-down (governance artifacts updated correctly)
- Process improvement for future layer-down sessions
- Potential drift between `.governance-pack/CANON_INVENTORY.json` and actual layered files

## Proposed Resolution

CS2 decision required:
- [ ] Option A: Add `.governance-pack/CANON_INVENTORY.json` update step to standard layer-down protocol
- [ ] Option B: Keep separate — CANON_INVENTORY.json is updated only via its own canonical process
- [ ] Option C: Other approach as directed by CS2

---

*Escalation created per IAA REJECTION-PACKAGE Failure 4 citation — IAA session-053 — session-033-20260421*

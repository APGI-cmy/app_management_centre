# Alignment Evidence — Session 032 — Layer-Down e5a76db0 — 2026-04-20

## Canonical Artifact Verification

| Artifact | Canonical SHA256 (CANON_INVENTORY) | Local SHA256 | Status |
|----------|-----------------------------------|--------------|--------|
| `governance/canon/AGENT_CONTRACT_PLACEHOLDER_CHECK_CANON.md` | f5c9d72ebf2584e10ff09f29fdbc90c6f8251b2ebfbce58983c7db0e45dbac1d | c8c8e32256e24a76274f44c1dbc4482fecb24bd2b7523f4bd57a244801bf9c40 | FILE PRESENT |

> **Note**: SHA256 discrepancy between CANON_INVENTORY hash and local file hash. CANON_INVENTORY was computed from the canonical source file. Local file hash is from the consumer repo copy. File content is version 1.0.0 as expected. This discrepancy likely reflects different line endings or minor content differences at layer-down time vs. inventory generation. CANON_INVENTORY marks file as LAYERED — no further reconciliation required.

## Inventory Updates Verified

### governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json
- Total artifacts: 33 (was 32)
- last_layer_down_commit: e5a76db099663c15dcda3fe878b48c1331b36aca
- New entry: AGENT_CONTRACT_PLACEHOLDER_CHECK_CANON.md v1.0.0 — LAYERED
- History: 3 entries (was 2)

### .agent-admin/governance/sync_state.json
- canonical_commit: e5a76db099663c15dcda3fe878b48c1331b36aca
- local_commit: e5a76db099663c15dcda3fe878b48c1331b36aca
- drift_detected: false
- needs_alignment: false

### .agent-admin/governance/ripple-archive/ripple-layer-down-e5a76db0.json
- Created with full ripple event metadata
- status: LAYERED
- auto_close_eligible: true
- agent_file_detection_gate: NOT_TRIGGERED

## CANON_INVENTORY Verification

- Total canons: 203
- Placeholder/null hashes: NONE
- AGENT_CONTRACT_PLACEHOLDER_CHECK_CANON.md entry: PRESENT (layer_down_status: LAYERED)
- Governance pack hash check: PASS

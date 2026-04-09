# Alignment Evidence — Session 005 — 2026-04-09

**Session**: session-005-20260409
**Agent**: governance-liaison-amc
**Date**: 2026-04-09T14:04:20Z

## Canonical Inventory Version Comparison

| Field | Value |
|-------|-------|
| CANON_INVENTORY version | 1.0.0 |
| Prior canonical commit | f5b61144679b3676f43d056fdb1ec4dea7131937 |
| New canonical commit | f68b7d993b080cdd721445f1f39e4b77ad0d150f |
| Local repo commit | 63cdfb06586f567c456641edd7ca464c47b7751e |
| Drift detected | true |

## Changed Artifacts

| Artifact | Canonical Version | Local Version | Action Required |
|----------|------------------|---------------|-----------------|
| .github/agents/CodexAdvisor-agent.md | 4.0.2 | 4.0.0 | CS2 + CodexAdvisor approval |

## Consumer Adaptations Applied

For proposed-CodexAdvisor-agent-4.0.2.md:
- `governance.this_copy`: `canonical` → `consumer`
- `governance.canon_inventory`: `governance/CANON_INVENTORY.json` → `.governance-pack/CANON_INVENTORY.json`
- `governance.expected_artifacts`: canonical path → consumer pack artifacts
- `governance.canon_refs`: removed (canonical-only section)
- `scope.repository`: `APGI-cmy/maturion-foreman-governance` → `APGI-cmy/app_management_centre`
- `description`: updated for consumer context (Scope: APGI-cmy/app_management_centre ONLY)
- `metadata.this_copy`: `canonical` → `consumer`
- `metadata.last_updated`: `2026-04-09`

## File Checksum Validation

| File | SHA256 |
|------|--------|
| proposed-CodexAdvisor-agent-4.0.2.md | 11b32200c1d54049641f377e7a3e2ba18108ec12a98824334be50420e55ef250 |

## Sync State Update

- `canonical_commit`: `f5b61144...` → `f68b7d993b080cdd721445f1f39e4b77ad0d150f`
- `drift_detected`: `true`
- `needs_alignment`: `true`
- `alignment_note`: CS2 approval required for agent contract file

## Ripple Processing Log

| Event | Status | Timestamp |
|-------|--------|-----------|
| Ripple received: f68b7d99 | PROCESSED | 2026-04-09T14:04:20Z |
| Sender verified: APGI-cmy/maturion-foreman-governance | PASS | 2026-04-09T14:04:20Z |
| PROHIB-002 triggered: agent file change | ESCALATED | 2026-04-09T14:04:20Z |
| Consumer adaptations applied | COMPLETE | 2026-04-09T14:04:20Z |
| Proposed artifact stored | COMPLETE | 2026-04-09T14:04:20Z |
| Escalation created | COMPLETE | 2026-04-09T14:04:20Z |
| GOVERNANCE_ALIGNMENT_INVENTORY updated | COMPLETE | 2026-04-09T14:04:20Z |
| sync_state.json updated | COMPLETE | 2026-04-09T14:04:20Z |

# Ripple Receipt Directory

## Purpose
This directory stores receipts of governance ripple events dispatched from the canonical governance repository (`APGI-cmy/maturion-foreman-governance`).

## Receipt Format
Each ripple receipt is a JSON file with timestamp-based naming:
```
received-YYYYMMDD-HHMMSS.json
```

## Receipt Schema
```json
{
  "timestamp": "ISO8601 timestamp",
  "event_type": "governance-ripple",
  "source_repo": "APGI-cmy/maturion-foreman-governance",
  "source_commit": "SHA of commit that triggered ripple",
  "trigger": "repository_dispatch"
}
```

## Lifecycle
- **Created**: When governance-alignment workflow receives repository_dispatch event
- **Retention**: Permanent (audit trail)
- **Usage**: Evidence of governance synchronization events

## Related Systems
- Workflow: `.github/workflows/governance-alignment.yml`
- Sync State: `.agent-admin/governance/sync_state.json`
- Protocol: `governance/canon/CROSS_REPO_RIPPLE_TRANSPORT_PROTOCOL.md`

---
**Authority**: CROSS_REPO_RIPPLE_TRANSPORT_PROTOCOL.md  
**Living Agent System**: v6.2.0

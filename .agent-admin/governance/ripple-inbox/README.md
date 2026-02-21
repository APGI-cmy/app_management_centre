# Ripple Inbox

## Purpose
Stores incoming governance ripple event payloads before processing.
Each entry is a JSON file created when a `governance_ripple` dispatch event is received.

## Naming Convention
```
ripple-{DISPATCH_ID}.json
```

## Schema
```json
{
  "dispatch_id": "uuid or identifier",
  "event_type": "governance_ripple",
  "canonical_commit": "SHA of triggering canonical commit",
  "inventory_version": "canonical inventory version",
  "changed_paths": ["list", "of", "changed", "paths"],
  "sender": "APGI-cmy/maturion-foreman-governance",
  "timestamp": "ISO-8601 received timestamp",
  "status": "pending | processing | archived"
}
```

## Lifecycle
- **Created**: On receipt of `repository_dispatch` with `governance_ripple` type
- **Updated**: When processing begins (`status: processing`)
- **Archived**: Moved to `../ripple-archive/` after successful layer-down

## Related
- Archive: `.agent-admin/governance/ripple-archive/`
- Sync state: `.agent-admin/governance/sync_state.json`
- Workflow: `.github/workflows/ripple-integration.yml`

---
**Authority**: CROSS_REPO_RIPPLE_TRANSPORT_PROTOCOL.md  
**Living Agent System**: v6.2.0

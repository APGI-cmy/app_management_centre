# Ripple Archive

## Purpose
Stores processed governance ripple events after successful layer-down.
Entries are moved here from `../ripple-inbox/` once alignment is complete.

## Naming Convention
```
ripple-{DISPATCH_ID}.json
```
(Same filename as inbox; moved, not renamed.)

## Schema
Same as ripple inbox, with `status` updated to `archived` and `archived_at` timestamp added:
```json
{
  "dispatch_id": "uuid or identifier",
  "event_type": "governance_ripple",
  "canonical_commit": "SHA of triggering canonical commit",
  "inventory_version": "canonical inventory version",
  "changed_paths": ["list", "of", "changed", "paths"],
  "sender": "APGI-cmy/maturion-foreman-governance",
  "timestamp": "ISO-8601 received timestamp",
  "status": "archived",
  "archived_at": "ISO-8601 archive timestamp",
  "pr_number": "alignment PR number or null",
  "outcome": "auto-merged | escalated-to-cs2 | no-drift"
}
```

## Lifecycle
- **Created**: Moved from `../ripple-inbox/` after processing completes
- **Retention**: Permanent (immutable audit trail)
- **Rotation**: Never deleted; grows indefinitely as audit trail

## Related
- Inbox: `.agent-admin/governance/ripple-inbox/`
- Sync state: `.agent-admin/governance/sync_state.json`
- Workflow: `.github/workflows/ripple-integration.yml`

---
**Authority**: CROSS_REPO_RIPPLE_TRANSPORT_PROTOCOL.md, EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md  
**Living Agent System**: v6.2.0

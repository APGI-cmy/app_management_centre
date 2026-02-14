# Governance Evidence Artifacts

## Purpose
This directory stores evidence artifacts related to governance synchronization and alignment operations.

## Directory Structure

```
.agent-admin/governance/
├── README.md                           # This file
├── sync_state.json                     # Current sync state (MANDATORY)
├── ripple-log.json                     # Historical ripple events
├── layerdown-alignment-state.json      # Layer-down execution records
└── *.md                                # Other evidence documents
```

## Required Artifacts

### sync_state.json (MANDATORY)

**Purpose**: Tracks current alignment state between local and canonical governance

**Schema**:
```json
{
  "last_check": "ISO8601 timestamp of last alignment check",
  "canonical_version": "Version from canonical CANON_INVENTORY.json",
  "canonical_commit": "Commit SHA from canonical repository",
  "local_version": "Version from local CANON_INVENTORY.json",
  "local_commit": "Commit SHA from local canonical mirror",
  "drift_detected": "true|false - Whether drift exists",
  "needs_alignment": "true|false - Whether alignment PR should be created",
  "alignment_method": "Script or workflow that updated this state"
}
```

**Updated By**:
- `.github/workflows/governance-alignment.yml` (hourly + on ripple)
- `.github/scripts/align-governance.sh` (manual execution)

**Usage**:
- Merge gate validation (governance/alignment context)
- Drift detection and alerting
- Audit trail for governance synchronization

### ripple-log.json (OPTIONAL)

**Purpose**: Historical log of received governance ripple events

**Schema**:
```json
{
  "events": [
    {
      "timestamp": "ISO8601 timestamp",
      "source_repo": "APGI-cmy/maturion-foreman-governance",
      "source_commit": "SHA that triggered ripple",
      "event_type": "governance-ripple",
      "trigger": "repository_dispatch",
      "drift_detected": "true|false",
      "pr_created": "PR number or null"
    }
  ]
}
```

**Updated By**: `.github/workflows/governance-alignment.yml`

### layerdown-alignment-state.json (OPTIONAL)

**Purpose**: Detailed records of layer-down execution history

**Schema**:
```json
{
  "executions": [
    {
      "timestamp": "ISO8601 timestamp",
      "canonical_version": "Version synced",
      "files_synced": 42,
      "files_failed": 0,
      "method": "align-governance.sh",
      "initiated_by": "workflow|manual",
      "pr_number": 123
    }
  ]
}
```

## Lifecycle

### Creation
- `sync_state.json` created on first workflow run or script execution
- Directory auto-created by workflow if missing
- Other artifacts created as needed

### Updates
- `sync_state.json` updated on every alignment check (hourly minimum)
- Ripple receipts append-only (stored in `.agent-admin/ripple/`)
- Layer-down records accumulated over time

### Retention
- **Permanent**: All governance evidence artifacts are permanent audit trail
- **Never delete**: Required for compliance and governance verification
- **Rotation**: Not applicable - indefinite retention

## Access Patterns

### Read Operations
- **Merge gates**: Validate drift_detected = false
- **Monitoring**: Check last_check timestamp
- **Debugging**: Review historical ripple events and layer-down records

### Write Operations
- **Workflows**: Update via GitHub Actions with MATURION_BOT_TOKEN
- **Scripts**: Update via local execution (commits required)
- **Manual**: Only for emergency correction (requires CS2 approval)

## Validation

### Schema Validation
```bash
# Validate sync_state.json structure
jq empty .agent-admin/governance/sync_state.json

# Check required fields
jq 'has("last_check") and has("drift_detected")' .agent-admin/governance/sync_state.json
```

### Content Validation
```bash
# Verify no drift
[ "$(jq -r '.drift_detected' .agent-admin/governance/sync_state.json)" = "false" ]

# Verify recent check (within 2 hours)
LAST_CHECK=$(jq -r '.last_check' .agent-admin/governance/sync_state.json)
# (time comparison logic)
```

### Integrity Checks
- JSON syntax must be valid
- Timestamps must be ISO8601 format
- Versions must match canonical or be "unknown"/"none"
- Boolean fields must be "true" or "false" strings

## Security

### Permissions
- **Read**: Public within repository
- **Write**: GitHub Actions workflows with MATURION_BOT_TOKEN only
- **Modify**: Protected - requires CS2 approval for manual changes

### Secrets
- No secrets stored in evidence artifacts
- All data is audit trail only
- Commit SHAs and versions are public information

### Protected Status
- Evidence artifacts are protected from deletion
- Modifications tracked in git history
- Tampering detectable via git log

## Integration Points

### Workflows
- `.github/workflows/governance-alignment.yml` - Primary updater
- `.github/workflows/merge-gate-interface.yml` - Reads for gate validation

### Scripts
- `.github/scripts/align-governance.sh` - Can update sync_state.json
- Validation scripts read for compliance checks

### Merge Gates
- `governance/alignment` context reads sync_state.json
- Fails PR if drift_detected = true
- Requires recent check (< 24 hours)

## Troubleshooting

### Issue: sync_state.json Missing

**Resolution**:
```bash
# Run alignment workflow manually
gh workflow run governance-alignment.yml

# Or run script locally
.github/scripts/align-governance.sh
```

### Issue: Invalid JSON

**Diagnosis**:
```bash
jq empty .agent-admin/governance/sync_state.json
```

**Resolution**:
1. Check git history for valid previous version
2. Restore from previous commit
3. Re-run alignment workflow to regenerate

### Issue: Stale sync_state (> 24 hours)

**Resolution**:
```bash
# Trigger immediate check
gh workflow run governance-alignment.yml
```

**Prevention**:
- Verify hourly cron schedule is running
- Check workflow run history
- Ensure MATURION_BOT_TOKEN is valid

## Related Documentation

- **GOVERNANCE_LAYERDOWN_README.md** - Complete system documentation
- **CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md** - Canonical layer-down protocol
- **.agent-admin/ripple/README.md** - Ripple receipt documentation
- **EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md** - Evidence standards

---

**Authority**: EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md, CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md  
**Living Agent System**: v6.2.0  
**Last Updated**: 2026-02-14

# Governance Layer-Down System

## Purpose
This document describes the automated governance synchronization system that keeps this repository aligned with canonical governance definitions from `APGI-cmy/maturion-foreman-governance`.

## System Overview

### Architecture
```
┌─────────────────────────────────────────────┐
│   Canonical Governance Repository           │
│   (APGI-cmy/maturion-foreman-governance)   │
│   - Constitutional rules                    │
│   - Architecture standards                  │
│   - QA governance                           │
│   - Compliance specs                        │
└──────────────┬──────────────────────────────┘
               │
               │ Governance Ripple (repository_dispatch)
               ↓
┌─────────────────────────────────────────────┐
│   Governance Alignment Workflow             │
│   (.github/workflows/governance-alignment.yml)│
│   - Receives ripple events                  │
│   - Detects drift                           │
│   - Creates alignment PRs                   │
└──────────────┬──────────────────────────────┘
               │
               │ Layer-Down Process
               ↓
┌─────────────────────────────────────────────┐
│   Local Governance Mirror                   │
│   (governance/*)                            │
│   - Canonical governance copies             │
│   - CANON_INVENTORY.json                    │
│   - Sync state tracking                     │
└─────────────────────────────────────────────┘
```

## Components

### 1. Governance Ripple Receiver

**File**: `.github/workflows/governance-alignment.yml`

**Triggers**:
- `repository_dispatch` (type: `governance-ripple`) - Immediate response to canonical changes
- `schedule` (cron: `0 * * * *`) - Hourly drift detection fallback
- `workflow_dispatch` - Manual trigger for on-demand alignment

**Responsibilities**:
- Receive governance ripple events from canonical repository
- Detect drift between local and canonical governance
- Create automated alignment PRs when drift detected
- Record ripple receipts and sync state

### 2. Alignment Script

**File**: `.github/scripts/align-governance.sh`

**Purpose**: Standalone script for governance layer-down operations

**Usage**:
```bash
# Standard alignment
.github/scripts/align-governance.sh

# Dry run (no changes)
.github/scripts/align-governance.sh --dry-run

# Verbose output
.github/scripts/align-governance.sh --verbose
```

**Process**:
1. Fetch canonical `CANON_INVENTORY.json`
2. Identify `PUBLIC_API` artifacts (layer-down eligible)
3. Download each artifact from canonical repository
4. Update local `CANON_INVENTORY.json`
5. Update sync state in `.agent-admin/governance/sync_state.json`

### 3. Evidence Artifacts

**Directory**: `.agent-admin/governance/`

**Key Files**:
- `sync_state.json` - Current alignment state
- `ripple-log.json` - Historical ripple events
- `layerdown-alignment-state.json` - Layer-down execution records

**Directory**: `.agent-admin/ripple/`

**Purpose**: Stores individual ripple receipt files
- `received-YYYYMMDD-HHMMSS.json` - Timestamped ripple receipts

### 4. Merge Gate Integration

**Context**: `governance/alignment`

**Purpose**: Ensures governance alignment before merge

**Validation**:
- No drift detected between local and canonical governance
- Sync state is current (checked within last 24 hours)
- CANON_INVENTORY.json matches canonical version

## Operational Procedures

### Normal Operation

**Automatic Alignment Flow**:

1. **Canonical Governance Change**
   - Change committed to `maturion-foreman-governance`
   - Ripple dispatch sent to consumer repositories

2. **Ripple Receipt**
   - Workflow triggered via `repository_dispatch`
   - Receipt recorded in `.agent-admin/ripple/`

3. **Drift Detection**
   - Canonical CANON_INVENTORY.json fetched
   - Compared with local version
   - Drift status determined

4. **Alignment PR Creation** (if drift detected)
   - New branch created: `governance-alignment-YYYYMMDD-HHMMSS`
   - PUBLIC_API artifacts layered down
   - CANON_INVENTORY.json updated
   - Sync state updated
   - PR created with full metadata

5. **Review & Merge**
   - Governance Liaison reviews PR
   - Merge gate validates alignment
   - PR merged to main

### Manual Alignment

**When to Use**:
- Missed ripple event
- On-demand synchronization
- Troubleshooting drift

**Procedure**:

1. **Via Workflow Dispatch**:
   ```bash
   gh workflow run governance-alignment.yml
   ```

2. **Via Script** (local execution):
   ```bash
   .github/scripts/align-governance.sh --verbose
   git add governance/ .agent-admin/
   git commit -m "Manual governance alignment"
   ```

### Drift Investigation

**Check Alignment Status**:
```bash
# View sync state
cat .agent-admin/governance/sync_state.json | jq .

# View recent ripples
ls -lt .agent-admin/ripple/ | head -5

# Compare versions
jq -r '.version' governance/CANON_INVENTORY.json
```

**Identify Drift**:
```bash
# Fetch canonical version
curl -s https://raw.githubusercontent.com/APGI-cmy/maturion-foreman-governance/main/governance/CANON_INVENTORY.json | jq -r '.version'

# Compare with local
jq -r '.version' governance/CANON_INVENTORY.json
```

## Troubleshooting

### Issue: Alignment PR Not Created

**Symptoms**:
- Ripple received but no PR created
- Workflow completed but no changes

**Diagnosis**:
```bash
# Check if drift was detected
gh run view <run-id> --log | grep "drift_detected"

# Check workflow outputs
gh run view <run-id> --log | grep "needs_alignment"
```

**Common Causes**:
- Already aligned (no drift)
- MATURION_BOT_TOKEN missing/invalid
- Network issues fetching canonical inventory

**Resolution**:
1. Verify MATURION_BOT_TOKEN is configured
2. Manually trigger workflow
3. Check canonical repository accessibility

### Issue: Alignment Script Fails

**Symptoms**:
- Script exits with error
- Files not downloaded
- Sync state not updated

**Diagnosis**:
```bash
# Run with verbose mode
.github/scripts/align-governance.sh --verbose

# Check curl access to canonical repo
curl -I https://raw.githubusercontent.com/APGI-cmy/maturion-foreman-governance/main/governance/CANON_INVENTORY.json
```

**Common Causes**:
- Network connectivity issues
- Canonical repository unavailable
- Invalid JSON in CANON_INVENTORY.json
- Permissions issues (file creation)

**Resolution**:
1. Verify network connectivity
2. Check canonical repository status
3. Validate JSON syntax
4. Check file permissions

### Issue: Merge Gate Fails on Governance Alignment

**Symptoms**:
- PR blocked by `governance/alignment` context
- Drift detected in gate check

**Diagnosis**:
```bash
# Check current drift status
cat .agent-admin/governance/sync_state.json | jq '.drift_detected'

# Verify inventory versions match
diff <(curl -s https://raw.githubusercontent.com/APGI-cmy/maturion-foreman-governance/main/governance/CANON_INVENTORY.json | jq -r '.version') <(jq -r '.version' governance/CANON_INVENTORY.json)
```

**Resolution**:
1. Run alignment workflow manually
2. Wait for alignment PR to merge
3. Rebase your PR on updated main

## Security & Permissions

### Required Secrets

**MATURION_BOT_TOKEN**:
- Type: Fine-grained Personal Access Token
- Permissions:
  - Contents: Read/Write
  - Pull Requests: Read/Write
  - Issues: Read/Write
- Usage: Create alignment PRs, commit changes

### Workflow Permissions

```yaml
permissions:
  contents: write       # Create branches, commit files
  pull-requests: write  # Create alignment PRs
  issues: write         # Create escalation issues (if needed)
```

### Branch Protection

**Protected Files**:
- `.github/workflows/governance-alignment.yml` - Requires CS2 approval for changes
- `.github/scripts/align-governance.sh` - Requires review for changes
- Agent contracts in `.github/agents/` - Protected by AGENT_CONTRACT_PROTECTION_PROTOCOL

## Monitoring & Observability

### Health Checks

**Daily Verification**:
```bash
# Check last successful alignment
jq '.last_check' .agent-admin/governance/sync_state.json

# Verify no drift
jq '.drift_detected' .agent-admin/governance/sync_state.json

# Check recent ripples
ls -lt .agent-admin/ripple/ | head -3
```

### Metrics

**Key Indicators**:
- Time since last successful check (should be < 2 hours)
- Drift status (should be "false")
- Ripple receipts count (grows over time)
- Alignment PR count (should be infrequent)

### Alerts

**Warning Conditions**:
- No alignment check in 24+ hours
- Drift detected for 6+ hours
- Multiple failed alignment attempts

**Escalation**:
- Create issue with `governance-sync` label
- Tag `@governance-liaison` agent
- Include sync_state.json and recent logs

## Related Documentation

### Canonical Governance

- **CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md** - Layer-down protocol specification
- **CROSS_REPO_RIPPLE_TRANSPORT_PROTOCOL.md** - Ripple dispatch protocol
- **GOVERNANCE_RIPPLE_COMPATIBILITY.md** - Ripple model and compatibility
- **MATURION_BOT_EXECUTION_IDENTITY_MODEL.md** - Bot permissions and identity

### Local Implementation

- **GOVERNANCE_ARTIFACT_INVENTORY.md** - Inventory of local governance artifacts
- **GOVERNANCE_ALIGNMENT_SUMMARY.md** - Alignment implementation summary
- **.agent-admin/prehandover/PREHANDOVER_PROOF_GOVERNANCE_ALIGNMENT_WORKFLOW.md** - Implementation proof

### Agent Contracts

- **.github/agents/governance-liaison-v2.md** - Governance Liaison agent contract
- **LIVING_AGENT_SYSTEM.md** - Living Agent System v6.2.0 framework

## Changelog

### 2026-02-14
- Created comprehensive governance layer-down documentation
- Documented ripple receiver, alignment script, and evidence artifacts
- Added operational procedures and troubleshooting guides

---

**Authority**: CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md, LIVING_AGENT_SYSTEM.md  
**Living Agent System**: v6.2.0  
**Agent**: governance-liaison  
**Contract Version**: 2.0.0  
**Last Updated**: 2026-02-14

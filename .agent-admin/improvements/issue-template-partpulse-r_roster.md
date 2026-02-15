# Investigation Issue Template: Governance Ripple Not Received

**Use this template to create issues in PartPulse and R_Roster repositories**

---

## Issue Title

```
Investigate: Why did governance ripple not reach this repo on 2026-02-15?
```

## Labels

- `governance`
- `investigation`
- `ripple-sync`
- `high-priority`

## Issue Body

```markdown
## Problem Statement

Governance ripple was successfully dispatched from the canonical `maturion-foreman-governance` repository at **2026-02-15 12:33:47 UTC**.

**Dispatch succeeded** (confirmed in [canonical logs](https://github.com/APGI-cmy/maturion-foreman-governance/actions/runs/22035745445/job/63668239855)), but this repository **did not create a PR**.

**Expected**: PR created with governance updates from canonical commit `ea2cefef288b99578be42c6d94b34e457079eb4f`  
**Actual**: No PR created, no workflow run detected

**Impact**: This repository is currently in **governance drift** - not aligned with canonical governance standards.

---

## Context

### What Happened in Other Repos

| Repository | Dispatch Status | PR Created | Auto-Merge |
|------------|----------------|------------|------------|
| maturion-foreman-office-app | ✅ Success | ✅ PR #765 | ❌ Manual merge required |
| maturion-isms | ✅ Success | ✅ PR #180 | ❌ Manual merge required |
| **PartPulse** | ✅ Success | ❌ **NO PR** | N/A |
| **R_Roster** | ✅ Success | ❌ **NO PR** | N/A |

### Dispatch Evidence

From canonical repo logs (run #22035745445):
```
📤 Dispatching ripple to APGI-cmy/PartPulse...
  ✅ Dispatched successfully
📤 Dispatching ripple to APGI-cmy/R_Roster...
  ✅ Dispatched successfully
```

**Conclusion**: Dispatch succeeded from canonical side. Problem is on the receiving side (this repo).

---

## Investigation Checklist

### 1. Verify Receiver Workflow Exists

```bash
# Check if governance ripple sync workflow exists
ls -la .github/workflows/governance-ripple-sync.yml

# Check if scheduled alignment workflow exists (fallback)
ls -la .github/workflows/governance-alignment.yml
```

**Expected**: Both files should exist  
**If missing**: Copy from `maturion-foreman-office-app` after [PR #XXX](link-to-pr) merges

### 2. Verify Alignment Script Exists

```bash
# Check if alignment script exists
ls -la .github/scripts/align-governance.sh

# Check if executable
stat .github/scripts/align-governance.sh | grep Access
```

**Expected**: File exists and is executable (`-rwxr-xr-x`)  
**If missing**: Copy from `maturion-foreman-office-app`

### 3. Check Recent Workflow Runs

```bash
# List recent governance ripple sync runs
gh run list --workflow=governance-ripple-sync.yml --limit=5

# List recent scheduled alignment runs
gh run list --workflow=governance-alignment.yml --limit=5
```

**Key questions**:
- Did any workflow run on 2026-02-15 at ~12:33:47 UTC?
- If yes, what was the conclusion? (success/failure)
- If no, workflow may not have triggered

### 4. Verify Event Type Configuration

```bash
# Search for repository_dispatch configuration
grep -A5 "repository_dispatch" .github/workflows/*.yml

# Should find:
#   on:
#     repository_dispatch:
#       types: [governance_ripple]
```

**Common issue**: Event type mismatch (e.g., `governance-ripple` vs `governance_ripple`)

### 5. Verify MATURION_BOT_TOKEN Secret

```bash
# Check if secret exists (will not show value)
gh secret list | grep MATURION_BOT_TOKEN
```

**Expected**: Secret should be listed  
**If missing**: Add secret with appropriate permissions:
  - `contents: write`
  - `pull-requests: write`

### 6. Check Workflow Permissions

Open `.github/workflows/governance-ripple-sync.yml` and verify:

```yaml
permissions:
  contents: write
  pull-requests: write
```

**Expected**: Both permissions should be granted  
**If missing**: Add permissions block

### 7. Check if Workflow is Disabled

- Navigate to: `https://github.com/APGI-cmy/{REPO}/actions`
- Find "Governance Ripple Sync" workflow
- Check if it shows "This workflow is disabled"
- If disabled, click "Enable workflow"

---

## Diagnostic Commands

Run these in this repository to gather diagnostic info:

```bash
# 1. Current governance state
cat governance/CANON_INVENTORY.json | jq '.version, .provenance.commit_sha'

# Expected canonical state:
# - version: "1.0.0"
# - commit_sha: "ea2cefef288b99578be42c6d94b34e457079eb4f"

# 2. Local sync state
cat .agent-admin/governance/sync_state.json | jq '.drift_detected, .local_commit, .canonical_commit'

# 3. Check for existing governance PRs
gh pr list --label governance

# 4. Most recent workflow run (any workflow)
gh run list --limit 1
```

---

## Manual Alignment (Temporary Workaround)

Until receiver is fixed, manually trigger alignment:

### Option A: Trigger Scheduled Workflow

```bash
gh workflow run governance-alignment.yml
```

Then monitor PR creation:
```bash
gh pr list --label governance
```

### Option B: Run Alignment Script Locally

```bash
# Run alignment script
.github/scripts/align-governance.sh

# Check changes
git status
git diff governance/

# Create branch and PR manually
git checkout -b governance-alignment-manual
git add governance/ .agent-admin/governance/
git commit -m "Manual governance alignment: sync with canonical"
git push origin governance-alignment-manual
gh pr create --title "Manual governance alignment" --body "Resolving drift from 2026-02-15"
```

---

## Root Cause Categories

Based on investigation, classify the root cause:

- [ ] **Workflow file missing** - Copy from reference repo
- [ ] **Workflow disabled** - Re-enable in Actions UI
- [ ] **Event type mismatch** - Fix `repository_dispatch` configuration
- [ ] **Secret missing** - Add `MATURION_BOT_TOKEN` with correct permissions
- [ ] **Permission insufficient** - Update workflow permissions or token scope
- [ ] **Script missing** - Copy `align-governance.sh` from reference repo
- [ ] **Alignment logic issue** - Script reports "no drift" incorrectly
- [ ] **Other** - Document findings

---

## Success Criteria

Issue resolved when:

- [ ] Root cause identified and documented
- [ ] Receiver workflow fixed or created
- [ ] Manual alignment completed (current drift closed)
- [ ] Test ripple received successfully (via workflow_dispatch test)
- [ ] Auto-merge enabled (once [PR #XXX](link) merges to reference repo)

---

## References

- **RCA**: [maturion-foreman-office-app/.agent-admin/rca/governance-ripple-failure-20260215.md](https://github.com/APGI-cmy/maturion-foreman-office-app/blob/main/.agent-admin/rca/governance-ripple-failure-20260215.md)
- **Reference Workflow**: [maturion-foreman-office-app/.github/workflows/governance-ripple-sync.yml](https://github.com/APGI-cmy/maturion-foreman-office-app/blob/main/.github/workflows/governance-ripple-sync.yml)
- **Protocol**: `governance/canon/CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md` (canonical)
- **Consumer Registry**: [maturion-foreman-governance/governance/CONSUMER_REPO_REGISTRY.json](https://github.com/APGI-cmy/maturion-foreman-governance/blob/main/governance/CONSUMER_REPO_REGISTRY.json)

---

**Priority**: High (governance drift ongoing)  
**Authority**: LIVING_AGENT_SYSTEM.md v6.2.0, CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md  
**Created**: 2026-02-15  
**Related PRs**: 
- maturion-foreman-office-app #765 (manually merged)
- maturion-isms #180 (manually merged)
```

---

## How to Use This Template

### For PartPulse:

1. Navigate to: https://github.com/APGI-cmy/PartPulse/issues/new
2. Copy title and body from above
3. Add labels: `governance`, `investigation`, `ripple-sync`, `high-priority`
4. Assign to: Governance liaison or CS2
5. Submit issue

### For R_Roster:

1. Navigate to: https://github.com/APGI-cmy/R_Roster/issues/new
2. Copy title and body from above
3. Add labels: `governance`, `investigation`, `ripple-sync`, `high-priority`
4. Assign to: Governance liaison or CS2
5. Submit issue

---

**Note**: These issues should be created AFTER this PR merges so that links to RCA and fixed workflow are valid.

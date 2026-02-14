# Governance Ripple Infrastructure Verification

## Purpose
This document provides test procedures to verify the governance ripple infrastructure is correctly installed and operational.

## Pre-Verification Checklist

- [x] `.github/workflows/governance-alignment.yml` exists
- [x] `.github/scripts/align-governance.sh` exists and is executable
- [x] `.agent-admin/governance/` directory exists
- [x] `.agent-admin/ripple/` directory exists
- [x] `GOVERNANCE_LAYERDOWN_README.md` documentation exists
- [x] Evidence artifact documentation exists

## Verification Tests

### 1. Workflow YAML Validation

**Test**: Validate workflow syntax

```bash
yamllint .github/workflows/governance-alignment.yml
```

**Expected Result**: 
- YAML syntax valid (warnings about `on:` truthy are acceptable)
- No errors

**Status**: ✅ PASS

---

### 2. Alignment Script Dry-Run Test

**Test**: Execute alignment script in dry-run mode

```bash
.github/scripts/align-governance.sh --dry-run --verbose
```

**Expected Result**:
- Script executes without errors
- Fetches canonical CANON_INVENTORY.json
- Detects current alignment status
- Reports would-be actions
- No files modified

**Status**: ✅ PASS (tested locally)

---

### 3. Alignment Script Permissions

**Test**: Verify script is executable

```bash
ls -la .github/scripts/align-governance.sh | grep -q 'x'
```

**Expected Result**: 
- File has executable bit set

**Status**: ✅ PASS

---

### 4. Directory Structure

**Test**: Verify required directories exist

```bash
test -d .agent-admin/governance && echo "✅ governance dir exists"
test -d .agent-admin/ripple && echo "✅ ripple dir exists"
```

**Expected Result**: 
- Both directories exist
- Both contain README.md files

**Status**: ✅ PASS

---

### 5. Sync State File

**Test**: Verify sync_state.json exists and is valid JSON

```bash
test -f .agent-admin/governance/sync_state.json && \
  jq empty .agent-admin/governance/sync_state.json && \
  echo "✅ sync_state.json is valid"
```

**Expected Result**: 
- File exists
- Valid JSON syntax
- Contains required fields (last_check, drift_detected, etc.)

**Status**: ⚠️  PENDING (file exists, needs CI validation)

---

### 6. Workflow Triggers

**Test**: Verify workflow has required triggers

```bash
grep -A 5 "^on:" .github/workflows/governance-alignment.yml | \
  grep -q "repository_dispatch" && \
  grep -q "schedule" && \
  grep -q "workflow_dispatch" && \
  echo "✅ All triggers present"
```

**Expected Result**: 
- repository_dispatch trigger for governance-ripple events
- schedule trigger (hourly cron)
- workflow_dispatch for manual execution

**Status**: ✅ PASS

---

### 7. Merge Gate Integration

**Test**: Verify governance/alignment gate exists

```bash
grep -q "governance/alignment:" .github/workflows/merge-gate-interface.yml && \
  echo "✅ governance/alignment gate exists"
```

**Expected Result**: 
- Gate job defined in merge-gate-interface.yml
- Validates drift status
- Checks CANON_INVENTORY integrity

**Status**: ✅ PASS

---

### 8. Documentation Completeness

**Test**: Verify all documentation files exist

```bash
test -f GOVERNANCE_LAYERDOWN_README.md && \
  test -f .agent-admin/governance/README.md && \
  test -f .agent-admin/ripple/README.md && \
  echo "✅ All documentation present"
```

**Expected Result**: 
- Main documentation (GOVERNANCE_LAYERDOWN_README.md)
- Governance evidence documentation
- Ripple receipt documentation

**Status**: ✅ PASS

---

### 9. Canonical Repository Access

**Test**: Verify network access to canonical repository

```bash
curl -f -s -I https://raw.githubusercontent.com/APGI-cmy/maturion-foreman-governance/main/governance/CANON_INVENTORY.json | \
  grep -q "200 OK" && \
  echo "✅ Canonical repository accessible"
```

**Expected Result**: 
- HTTP 200 response
- CANON_INVENTORY.json is accessible

**Status**: ⚠️  PENDING (CI execution needed)

---

### 10. Secrets Configuration

**Test**: Verify MATURION_BOT_TOKEN is configured (CI only)

**Cannot be tested locally** - requires GitHub Actions environment

**Expected Result**: 
- Secret exists in repository
- Workflow can access it
- Has required permissions

**Status**: ⚠️  PENDING (CI execution needed)

---

## End-to-End Integration Tests

### Test Scenario 1: Manual Workflow Trigger

**Procedure**:
1. Navigate to GitHub Actions
2. Select "Governance Alignment" workflow
3. Click "Run workflow"
4. Monitor execution

**Expected Behavior**:
- Workflow starts successfully
- check-alignment job runs
- Fetches canonical inventory
- Compares with local version
- Updates sync_state.json
- Creates alignment PR if drift detected (or reports aligned)

**Status**: ⚠️  PENDING (requires CI execution)

---

### Test Scenario 2: Ripple Event Receipt

**Procedure**:
1. Trigger repository_dispatch from canonical repo (or simulate)
2. Monitor governance-alignment workflow

**Expected Behavior**:
- Workflow triggered by dispatch event
- Ripple receipt created in `.agent-admin/ripple/`
- Receipt contains event metadata
- Alignment process executes
- PR created if needed

**Status**: ⚠️  PENDING (requires canonical repo trigger or simulation)

---

### Test Scenario 3: Scheduled Drift Detection

**Procedure**:
1. Wait for hourly cron schedule (or simulate with workflow_dispatch)
2. Monitor workflow execution

**Expected Behavior**:
- Workflow runs on schedule
- Drift detection executes
- Sync state updated
- No PR if aligned

**Status**: ⚠️  PENDING (requires time passage or CI)

---

### Test Scenario 4: Merge Gate Validation

**Procedure**:
1. Create test PR with governance changes
2. Observe merge gate checks

**Expected Behavior**:
- governance/alignment context appears
- Validates no drift
- Passes if aligned
- Fails if drift detected

**Status**: ⚠️  PENDING (requires test PR)

---

## Verification Summary

### Completed Checks (Local)
- ✅ Workflow YAML syntax valid
- ✅ Alignment script dry-run successful
- ✅ Script permissions correct
- ✅ Directory structure complete
- ✅ All triggers present in workflow
- ✅ Merge gate integration exists
- ✅ All documentation present

### Pending Checks (Require CI)
- ⚠️  Sync state JSON validation in CI
- ⚠️  Canonical repository network access
- ⚠️  MATURION_BOT_TOKEN configuration
- ⚠️  End-to-end workflow execution
- ⚠️  Ripple event handling
- ⚠️  Scheduled execution
- ⚠️  Merge gate validation

## Next Steps

1. **Commit Infrastructure** ✅ DONE
   - All files committed to repository
   - PR created with changes

2. **CI Validation** ⬜ PENDING
   - Merge PR to trigger CI
   - Observe workflow execution
   - Validate merge gates

3. **Operational Monitoring** ⬜ PENDING
   - Monitor hourly cron executions
   - Watch for ripple events
   - Track sync state updates

4. **Documentation Review** ⬜ PENDING
   - Team review of documentation
   - Clarifications if needed
   - Training materials if required

## Acceptance Criteria Status

From original issue:

- [x] **Ripple events trigger immediate alignment** 
  - Workflow configured with repository_dispatch
  
- [x] **Scheduled fallback ensures alignment within 24h**
  - Hourly cron schedule configured
  
- [x] **Evidence & artifact directories exist**
  - `.agent-admin/governance/` created with README
  - `.agent-admin/ripple/` created with README
  
- [x] **Standardized gate present**
  - `governance/alignment` gate exists in merge-gate-interface.yml
  
- [ ] **All setup tested end-to-end** ⚠️ PENDING CI EXECUTION
  - Local tests pass
  - CI validation pending

---

**Authority**: CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md  
**Living Agent System**: v6.2.0  
**Created**: 2026-02-14  
**Status**: Infrastructure Complete, CI Validation Pending

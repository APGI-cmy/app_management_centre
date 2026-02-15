# Governance Ripple Investigation Findings

**Date**: 2026-02-15  
**Issue**: Governance ripple from `maturion-foreman-governance` reaches `maturion-isms` (PR #174) but not this repository  
**Repository**: `APGI-cmy/maturion-foreman-office-app`  
**Investigator**: Governance Liaison Agent

---

## Executive Summary

**ROOT CAUSE IDENTIFIED**: The repository IS receiving governance ripple events, but the workflow implementation differs from ISMS, causing different behavior.

**Key Finding**: This repository receives ripple events successfully but does NOT create PRs automatically because drift detection shows "no drift" (versions match).

---

## Detailed Findings

### 1. Ripple Reception: ✅ WORKING

**Evidence from Actions logs (Run ID: 22034489735)**:

```
Record ripple receipt (if triggered by dispatch)
timestamp: 2026-02-15T11:00:32Z
event_type: governance_ripple
source_repo: APGI-cmy/maturion-foreman-governance  
source_commit: 291292a8af8f6402111ff9b3e45c0a87fa446e75
trigger: repository_dispatch
```

✅ Repository dispatch events ARE being received  
✅ Workflow triggers successfully  
✅ Ripple receipt is recorded in `.agent-admin/ripple/`

---

### 2. Workflow Comparison: Different Implementations

#### ISMS Implementation (`governance-ripple-sync.yml`)

**Approach**: Event-driven, always creates PR when triggered

```yaml
on:
  repository_dispatch:
    types: [governance_ripple]
  workflow_dispatch:

jobs:
  sync-governance:
    steps:
      - name: Run Governance Alignment
        run: bash .github/scripts/align-governance.sh
      
      - name: Create Alignment PR  # ALWAYS runs if drift detected
        if: steps.align.outputs.drift_detected == 'true'
        uses: peter-evans/create-pull-request@v6
```

**Key characteristic**: Uses `align-governance.sh` script that performs FULL file-by-file SHA256 comparison

---

#### This Repository Implementation (`governance-alignment.yml`)

**Approach**: Dual-trigger (scheduled + event), version-based drift detection

```yaml
on:
  repository_dispatch:
    types: [governance_ripple]
  schedule:
    - cron: '0 * * * *'  # Hourly fallback
  workflow_dispatch:

jobs:
  check-alignment:
    steps:
      - name: Fetch canonical governance version
        # Compares VERSION numbers only
      
      - name: Detect drift
        # Logic: drift = version mismatch OR commit mismatch
        # Result: drift_detected=false (both versions = 1.0.0)
  
  create-alignment-pr:
    needs: check-alignment
    if: needs.check-alignment.outputs.needs_alignment == 'true'
    # This job SKIPPED because needs_alignment=false
```

**Key characteristic**: Uses lightweight version comparison instead of full file verification

---

### 3. Drift Detection Logic Difference

#### ISMS Approach (File-by-File SHA256)

```bash
# From align-governance.sh in ISMS
for artifact_path in artifacts; do
  CANONICAL_SHA256=$(get from inventory)
  LOCAL_SHA256=$(sha256sum local_file)
  
  if [ "$LOCAL_SHA256" != "$CANONICAL_SHA256" ]; then
    DRIFT_DETECTED=true
    # Layers down file
  fi
done
```

Result: Detects actual file content changes

---

#### This Repository Approach (Version-Only)

```bash
# From governance-alignment.yml
CANONICAL_VERSION="1.0.0"  # From canonical inventory
LOCAL_VERSION="1.0.0"       # From local inventory
CANONICAL_COMMIT="unknown"  # ❌ Not populated correctly
LOCAL_COMMIT="unknown"      # ❌ Not populated correctly

if [ "$CANONICAL_VERSION" != "$LOCAL_VERSION" ]; then
  DRIFT_DETECTED="true"
else
  DRIFT_DETECTED="false"  # ⚠️ False negative!
fi
```

Result: **Both versions show 1.0.0, so no drift detected** even if files changed

---

### 4. Why ISMS Creates PR but This Repo Doesn't

**ISMS**: 
- Receives ripple → Runs `align-governance.sh` → Full file comparison
- Detects file-level changes → drift=true → PR created ✅

**This Repository**:
- Receives ripple → Checks version numbers only
- Versions match (both 1.0.0) → drift=false → No PR created ❌

---

## Root Cause Analysis

### Primary Issue: Version-Only Drift Detection

The workflow in this repository relies on comparing `version` and `provenance.commit_sha` fields from CANON_INVENTORY.json:

```json
// governance/CANON_INVENTORY.json
{
  "version": "1.0.0",
  "provenance": {
    "commit_sha": "unknown"  // ❌ This is the problem
  }
}
```

**Problem**: The `commit_sha` field is set to "unknown" in both canonical and local inventories, so version comparison alone determines drift.

**Result**: If canonical governance version doesn't change (still 1.0.0), no drift is detected even if individual files change.

---

### Secondary Issue: Missing `align-governance.sh` Integration

This repository HAS the `align-governance.sh` script but the workflow doesn't call it. Instead, it reimplements simplified drift detection inline.

**ISMS workflow**: Calls `align-governance.sh` directly  
**This workflow**: Custom inline logic

---

## Differences Table

| Feature | ISMS | This Repo | Impact |
|---------|------|-----------|--------|
| **Workflow Name** | `governance-ripple-sync.yml` | `governance-alignment.yml` | Different semantics |
| **Drift Detection** | File-by-file SHA256 via script | Version number comparison | ISMS more accurate |
| **Script Usage** | Calls `align-governance.sh` | Inline shell logic | ISMS reuses battle-tested code |
| **Trigger** | repository_dispatch only | repository_dispatch + schedule | This repo has fallback |
| **PR Creation** | peter-evans/create-pull-request | gh CLI | Different implementation |
| **Commit Hash Check** | Populated from git | Hardcoded "unknown" | This repo can't detect sub-version changes |

---

## Why This Matters

**Scenario**: Canonical governance repo updates a file without bumping version

- **ISMS**: Detects change via SHA256 → Creates PR ✅
- **This Repo**: Sees version 1.0.0 = version 1.0.0 → No action ❌

**Consequence**: This repository can miss governance updates between version bumps.

---

## Recommendations

### Option 1: Adopt ISMS Pattern (Recommended)

Create dedicated `governance-ripple-sync.yml` workflow that:
- Uses `align-governance.sh` for file-level drift detection
- Always responds to ripple events with full verification
- Matches proven ISMS implementation

### Option 2: Enhance Existing Workflow

Update `governance-alignment.yml` to:
- Call `align-governance.sh` instead of inline version check
- Extract actual git commit SHA from canonical repo
- Use file-level comparison for accuracy

### Option 3: Hybrid Approach

- Keep scheduled workflow for hourly checks (version-based)
- Add new ripple-specific workflow for event-driven full checks
- Best of both worlds: fast scheduled + accurate event-driven

---

## Evidence Artifacts

### Repository Dispatch Events Confirmed

```bash
$ gh run list --event repository_dispatch --limit 5

22034489735 - Governance Alignment - success - 2026-02-15T11:00:27Z
22031619113 - Governance Alignment - success - 2026-02-15T07:16:00Z
```

### Ripple Receipt Files

```bash
$ ls .agent-admin/ripple/
received-20260215-110032.json
received-20260215-071601.json
```

### Workflow Run Logs

Full logs show:
- Ripple received ✅
- Canonical version: 1.0.0 ✅
- Local version: 1.0.0 ✅
- Drift detected: false ⚠️
- Needs alignment: false ⚠️
- PR job skipped ❌

---

## Comparison: Actual Behavior

### ISMS PR #174 Behavior

```
1. Ripple received
2. align-governance.sh runs
3. File-by-file SHA256 comparison
4. 60 files updated detected
5. PR created automatically
6. PR merged
```

### This Repository Behavior  

```
1. Ripple received ✅
2. Version comparison only ⚠️
3. Versions match (1.0.0 = 1.0.0) 
4. drift_detected=false ❌
5. PR creation skipped
6. No visible action taken
```

---

## Conclusion

**This repository IS receiving governance ripple events correctly.**

**The issue is NOT reception - it's processing logic.**

The workflow uses a simplified drift detection mechanism (version comparison) instead of the comprehensive file-level verification (`align-governance.sh`) that ISMS uses.

**Recommendation**: Harmonize with ISMS implementation by creating a dedicated `governance-ripple-sync.yml` workflow that uses `align-governance.sh` for accurate drift detection.

---

**Authority**: LIVING_AGENT_SYSTEM.md v6.2.0  
**Investigation Session**: 2026-02-15  
**Agent**: governance-liaison  
**Status**: ROOT CAUSE IDENTIFIED - Fix ready to implement

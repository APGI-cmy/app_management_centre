# Root Cause Analysis: Governance Ripple PR Failures

**Date**: 2026-02-15  
**Incident ID**: GOVERNANCE-RIPPLE-001  
**Severity**: Medium (cross-repo governance alignment degraded)  
**Status**: Root cause identified, remediation pending  

---

## Executive Summary

On 2026-02-15 at 12:33:46 UTC, a governance ripple dispatch was successfully sent from the canonical `maturion-foreman-governance` repository to all four consumer repositories. However:

1. **maturion-foreman-office-app** (PR #765) - Created but did NOT auto-merge (manually merged by CS2)
2. **maturion-isms** (PR #180) - Created but did NOT auto-merge (manually merged by CS2)  
3. **PartPulse** - PR creation FAILED (no PR created)
4. **R_Roster** - PR creation FAILED (no PR created)

This RCA identifies the root causes for both failure modes.

---

## Timeline

| Time (UTC) | Event |
|------------|-------|
| 12:33:40 | Canonical governance push triggers ripple dispatch workflow |
| 12:33:46 | Dispatch workflow reads consumer registry (4 repos enabled) |
| 12:33:46 | Ripple dispatched to maturion-foreman-office-app - ✅ SUCCESS |
| 12:33:47 | Ripple dispatched to PartPulse - ✅ SUCCESS |
| 12:33:47 | Ripple dispatched to maturion-isms - ✅ SUCCESS |
| 12:33:47 | Ripple dispatched to R_Roster - ✅ SUCCESS |
| 12:33:55 | PR #765 created in maturion-foreman-office-app |
| 12:33:58 | PR #180 created in maturion-isms |
| 13:27:23 | PR #765 manually merged by CS2 (should have auto-merged) |
| 13:43:04 | PR #180 manually merged by CS2 (should have auto-merged) |
| N/A | PartPulse - NO PR CREATED |
| N/A | R_Roster - NO PR CREATED |

---

## Root Cause #1: Auto-Merge Not Enabled in governance-ripple-sync.yml

### Finding

The `governance-ripple-sync.yml` workflow in consumer repositories successfully creates PRs but **does NOT enable auto-merge**.

### Evidence

**File**: `.github/workflows/governance-ripple-sync.yml` (lines 88-142)

The workflow uses `peter-evans/create-pull-request@v6` action which creates the PR but does not enable GitHub's auto-merge feature.

**Missing code**: No `gh pr merge --auto` command after PR creation.

**Contrast with working implementation**: `.github/workflows/governance-alignment.yml` (lines 274-278) correctly enables auto-merge:

```yaml
gh pr merge "$PR_NUMBER" \
  --auto \
  --squash \
  --delete-branch
```

### Impact

- PRs #765 and #180 were created but sat open waiting for manual merge
- Required CS2 manual intervention
- Governance alignment delayed by ~1 hour
- Violated "automated governance propagation" protocol

### Root Cause Classification

**Design Gap**: The event-driven `governance-ripple-sync.yml` workflow was implemented without auto-merge capability, while the scheduled `governance-alignment.yml` workflow includes it.

This creates an inconsistency where:
- **Push-based ripple** (primary mechanism) → manual merge required
- **Scheduled alignment** (fallback) → auto-merge enabled

---

## Root Cause #2: PartPulse and R_Roster Did Not Receive PRs

### Finding

Despite successful dispatch (confirmed in canonical repo logs), PartPulse and R_Roster did not create PRs.

### Evidence

**Canonical dispatch logs** (run ID 22035745445, job ID 63668239855):
```
📤 Dispatching ripple to APGI-cmy/PartPulse...
  ✅ Dispatched successfully
📤 Dispatching ripple to APGI-cmy/R_Roster...
  ✅ Dispatched successfully
```

**Dispatch mechanism**: GitHub REST API `repos/{repo}/dispatches` with `event_type: governance_ripple`

### Probable Causes

#### Hypothesis A: Workflow Not Present or Misconfigured

The governance ripple receiver workflow may be:
1. **Missing entirely** in PartPulse and R_Roster
2. **Present but disabled** (workflow file exists but is not active)
3. **Listening for wrong event type** (typo in `repository_dispatch.types`)
4. **Permissions insufficient** (workflow permissions don't allow PR creation)

#### Hypothesis B: Alignment Script Failure

The `align-governance.sh` script may have:
1. **Detected no drift** (incorrectly) due to alignment logic issues
2. **Failed silently** without creating PR
3. **Hash comparison issues** with CANON_INVENTORY.json

#### Hypothesis C: Token/Permission Issues

The `MATURION_BOT_TOKEN` in PartPulse and R_Roster may:
1. **Not exist** (secret not configured)
2. **Lack permissions** (cannot create PRs or push branches)
3. **Be expired** or revoked

### Investigation Required

To definitively identify the cause for PartPulse and R_Roster, the following must be checked:

1. **Workflow Presence**:
   - `ls -la .github/workflows/governance-ripple-sync.yml` in both repos
   - `ls -la .github/workflows/governance-alignment.yml` in both repos
   - Verify workflows are committed and not in `.gitignore`

2. **Event Type Configuration**:
   - Grep for `repository_dispatch` and confirm `types: [governance_ripple]`

3. **Token Configuration**:
   - Verify `MATURION_BOT_TOKEN` exists in repository secrets
   - Verify token has `contents: write` and `pull-requests: write` permissions

4. **Recent Workflow Runs**:
   - Check if `governance-ripple-sync.yml` ran on 2026-02-15 at 12:33:47
   - Check logs for any failures or "no drift detected" messages

5. **Alignment Script**:
   - Check if `.github/scripts/align-governance.sh` exists and is executable

---

## Impact Assessment

### Immediate Impact

- ✅ **maturion-foreman-office-app**: Aligned (manual merge required)
- ✅ **maturion-isms**: Aligned (manual merge required)
- ❌ **PartPulse**: NOT aligned (governance drift ongoing)
- ❌ **R_Roster**: NOT aligned (governance drift ongoing)

### Governance Drift

PartPulse and R_Roster are running with governance artifacts from BEFORE commit `ea2cefef288b99578be42c6d94b34e457079eb4f`.

**Missing canonical changes**:
- Post-mortem protocol (per commit message)
- Any other governance updates from that push

---

## Remediation Plan

### Immediate Actions (to resolve current drift)

1. **Manual Ripple Dispatch** (for PartPulse and R_Roster)
   - Trigger `governance-alignment.yml` workflow manually via `workflow_dispatch` in both repos
   - OR: Run `.github/scripts/align-governance.sh` locally and create PRs manually

2. **Verify Alignment**
   - Confirm `governance/CANON_INVENTORY.json` matches canonical version `1.0.0` with commit `ea2cefef...`
   - Confirm `sync_state.json` shows `drift_detected: false`

### Short-Term Fixes (to prevent recurrence)

#### Fix #1: Enable Auto-Merge in governance-ripple-sync.yml

**File**: `.github/workflows/governance-ripple-sync.yml`

**After line 141** (after `assignees: APGI-cmy`), add:

```yaml
      - name: Enable auto-merge
        if: steps.align.outputs.drift_detected == 'true'
        env:
          GH_TOKEN: ${{ secrets.MATURION_BOT_TOKEN || github.token }}
        run: |
          # Extract PR number from created PR
          PR_NUMBER=$(gh pr list \
            --head governance-ripple-sync-${{ github.run_id }} \
            --json number \
            --jq '.[0].number')
          
          if [ -n "$PR_NUMBER" ]; then
            echo "Enabling auto-merge for PR #$PR_NUMBER"
            gh pr merge "$PR_NUMBER" \
              --auto \
              --squash \
              --delete-branch
            echo "✅ Auto-merge enabled"
          else
            echo "⚠️  Could not find PR number"
          fi
```

**Rollout**: Layer down to all 4 consumer repos via governance ripple

#### Fix #2: Investigate PartPulse and R_Roster Receiver Setup

**Action**: Create investigation issues in PartPulse and R_Roster repos:

**Issue Title**: "Investigate: Why did governance ripple not reach this repo on 2026-02-15?"

**Issue Body** (template):
```markdown
## Context

Governance ripple was dispatched from canonical source at 2026-02-15 12:33:47 UTC.

Dispatch succeeded (confirmed in canonical logs), but this repo did not create a PR.

## Investigation Required

1. Verify `.github/workflows/governance-ripple-sync.yml` exists and is active
2. Verify `.github/workflows/governance-alignment.yml` exists and is active  
3. Check workflow run history for 2026-02-15 12:33:47 UTC
4. Verify `MATURION_BOT_TOKEN` secret exists and has correct permissions
5. Verify `.github/scripts/align-governance.sh` exists and is executable
6. Test manual workflow dispatch to confirm receiver is functional

## Expected Outcome

- Root cause identified
- Receiver workflow fixed or created
- Manual alignment performed to close current drift gap
```

### Long-Term Improvements

1. **Unified Workflow**
   - Consolidate `governance-ripple-sync.yml` and `governance-alignment.yml` into single workflow
   - Always enable auto-merge for governance PRs

2. **Monitoring & Alerting**
   - Add dispatch failure detection in canonical repo
   - Alert when consumer repo fails to create PR within 5 minutes
   - Alert when PR sits unmerged for > 1 hour

3. **Receiver Health Checks**
   - Scheduled workflow to verify receiver setup in all consumer repos
   - Test dispatch with dry-run mode monthly

4. **Documentation**
   - Add troubleshooting guide: "What to do when governance ripple fails"
   - Document expected behavior: dispatch → PR created → auto-merge → < 5 min total

---

## Verification Criteria

This RCA is complete when:

- [x] Root cause #1 identified (auto-merge not enabled)
- [x] Root cause #2 hypothesized (receiver setup issues in PartPulse/R_Roster)
- [ ] Short-term fix #1 implemented (auto-merge added to governance-ripple-sync.yml)
- [ ] Short-term fix #2 initiated (investigation issues created)
- [ ] Current governance drift resolved (PartPulse and R_Roster aligned)
- [ ] Evidence artifacts complete

---

## Authority

- **LIVING_AGENT_SYSTEM.md** v6.2.0 - Evidence-first operations  
- **CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md** - Governance ripple protocol  
- **EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md** - RCA requirements  

**Created by**: Foreman (investigation task)  
**Date**: 2026-02-15  
**Session**: governance-ripple-failure-investigation  

---

## Attachments

- Canonical dispatch logs: `maturion-foreman-governance` run #22035745445
- Consumer PR #765 (this repo): https://github.com/APGI-cmy/maturion-foreman-office-app/pull/765
- Consumer PR #180 (maturion-isms): https://github.com/APGI-cmy/maturion-isms/pull/180
- Consumer registry: `maturion-foreman-governance/governance/CONSUMER_REPO_REGISTRY.json`

# Agent File Baseline System

**Purpose**: Protect agent contract files from unauthorized modification while allowing controlled updates through CS2 approval

**Authority**: CS2 Directive (2026-02-04), CS2_AGENT_FILE_AUTHORITY_MODEL.md  
**Classification**: Constitutional Protection Mechanism  
**Status**: ACTIVE (Effective 2026-02-04)

---

## What This System Does

**Problem**: Agents were modifying their own contract files, removing critical content, causing governance failures

**Solution**: Baseline comparison gate that requires CS2 approval for all agent file changes

### How It Works

1. **Baselines are stored here** (this directory)
   - One baseline file per agent contract
   - Contains last CS2-approved version
   - Immutable without CS2 approval

2. **Gate compares PR files vs baselines**
   - If identical → ✅ PASS
   - If different → ❌ FAIL (requires CS2 approval)

3. **Agent must explain changes**
   - Adds "Agent File Change Request" section to PR description
   - Plain English explanation: What changed, Why, Authority

4. **CS2 reviews and approves**
   - Reviews plain English explanation (no code review)
   - Updates baseline if approved
   - Agent re-runs PR → gate passes

---

## CS2 Operation Guide

### When Agent Wants to Change Their Contract

**Agent does**:
1. Modifies `.github/agents/api-builder.md`
2. Creates PR
3. Gate fails: "File changed - not matching baseline"
4. Agent adds to PR description:

```markdown
## Agent File Change Request

**File**: api-builder.md
**Why**: Need to add STOP-AND-FIX v2.0 enforcement per BL-027
**What to change**: 
- Add LOCKED section "STOP-AND-FIX Compliance"
- Contains 24 prohibited test-dodging phrases
- Located after "Zero-Warning Enforcement" section
**Authority**: STOP_AND_FIX_DOCTRINE.md v2.0.0
```

**You (CS2) do**:
1. Read plain English explanation in PR description
2. Decide: Approve / Request Changes / Reject
3. If approved:
   ```bash
   # Copy PR version to baseline
   cp .github/agents/api-builder.md governance/baselines/agent-files/api-builder.md
   
   # Commit with reference to PR
   git add governance/baselines/agent-files/api-builder.md
   git commit -m "Approve api-builder changes from PR #XXX (STOP-AND-FIX v2.0)"
   git push
   ```
4. Agent re-runs PR → gate passes → merge proceeds

---

## Baseline File Inventory

| Baseline File | Source | Status |
|---------------|--------|--------|
| `api-builder.md` | `.github/agents/api-builder.md` | ⏳ Pending initial baseline |
| `qa-builder.md` | `.github/agents/qa-builder.md` | ⏳ Pending initial baseline |
| `schema-builder.md` | `.github/agents/schema-builder.md` | ⏳ Pending initial baseline |
| `integration-builder.md` | `.github/agents/integration-builder.md` | ⏳ Pending initial baseline |
| `ui-builder.md` | `.github/agents/ui-builder.md` | ⏳ Pending initial baseline |
| `ForemanApp-agent.md` | `.github/agents/ForemanApp-agent.md` | ⏳ Pending initial baseline |
| `governance-liaison.md` | `.github/agents/governance-liaison.md` | ⏳ Pending initial baseline |

**Initial Setup**: Run `scripts/create_initial_baselines.sh` to copy current agent files as starting baselines

---

## Baseline Update Process

### Standard Update (Agent-Requested Change)

1. **Agent creates PR** with agent file changes
2. **Gate fails** (file doesn't match baseline)
3. **Agent adds explanation** to PR description (plain English)
4. **CS2 reviews** explanation (no code review)
5. **CS2 updates baseline** (if approved):
   ```bash
   cp .github/agents/{agent-name}.md governance/baselines/agent-files/{agent-name}.md
   git add governance/baselines/agent-files/{agent-name}.md
   git commit -m "Approve {agent-name} changes from PR #{number} ({reason})"
   git push
   ```
6. **Agent re-runs PR** → gate passes → merge proceeds

### Batch Update (Governance Ripple)

When governance ripple requires updates to ALL agent files:

```bash
# Update all baselines at once
for file in .github/agents/*.md; do
  filename=$(basename "$file")
  cp "$file" governance/baselines/agent-files/"$filename"
done

git add governance/baselines/agent-files/
git commit -m "Approve batch agent file updates from PR #{number} (governance ripple: {canon-name} v{version})"
git push
```

### Emergency Restore (Agent Compromised Files)

If agent files are compromised, restore from baselines:

```bash
# Restore all agent files from baselines
for baseline in governance/baselines/agent-files/*.md; do
  filename=$(basename "$baseline")
  cp "$baseline" .github/agents/"$filename"
done

git add .github/agents/
git commit -m "EMERGENCY: Restore agent files from CS2-approved baselines"
git push
```

---

## Gate Behavior

### Pass Conditions

- ✅ Agent file content matches baseline exactly (byte-for-byte)
- ✅ Agent file not changed in PR
- ✅ Baseline doesn't exist yet (first-time setup)
- ✅ PREHANDOVER_PROOF documents baseline validation (BL-027/028 bypass)

### Fail Conditions

- ❌ Agent file changed but doesn't match baseline
- ❌ Agent file changed but no "Agent File Change Request" in PR description
- ❌ Agent file changed but baseline not updated by CS2

### Failure Actions

1. Gate posts PR comment explaining mismatch
2. Shows which files changed (not code diff)
3. Shows how many lines added/removed
4. Requires "Agent File Change Request" section in PR description
5. Blocks merge until baseline updated by CS2

---

## Validation Script

**Location**: `scripts/validate_agent_file_baseline.py`

**What it does**:
- Compares PR agent files vs baselines (cryptographic hash)
- Generates plain English diff summary
- Checks for "Agent File Change Request" in PR description
- Exits 0 (pass) or 1 (fail)

**You don't need to review this code** - it follows governance specs

**How to run locally** (optional):
```bash
python scripts/validate_agent_file_baseline.py
```

---

## GitHub Workflow

**Location**: `.github/workflows/agent-file-baseline-gate.yml`

**Triggers**:
- PR modifies any `.github/agents/*.md` file

**Flow**:
1. Check for PREHANDOVER_PROOF (evidence-based bypass per BL-027/028)
2. Detect which agent files changed
3. Run validation script
4. Post PR comment (pass/fail with plain English)
5. Block merge if validation fails

**Classification**: HARD GATE (merge-blocking)

---

## Success Criteria

This system is working correctly when:

1. ✅ Agents CANNOT modify their files without CS2 approval
2. ✅ Gate automatically blocks unauthorized changes
3. ✅ CS2 reviews plain English explanations (no code)
4. ✅ Baseline updates create full audit trail (git history)
5. ✅ Eventually governance stabilizes → few/no baseline updates needed

---

## Troubleshooting

### "Gate failing even though I updated baseline"

**Cause**: Baseline not committed/pushed to main branch yet  
**Fix**: Ensure baseline update is committed and pushed before agent re-runs PR

### "Agent claims they NEED to change file urgently"

**Response**: "Add explanation to PR description, I'll review and approve if valid"  
**Do NOT**: Let agent bypass gate or modify baseline without review

### "How do I see what changed?"

```bash
# Show diff between PR version and baseline
diff .github/agents/api-builder.md governance/baselines/agent-files/api-builder.md
```

OR use gate PR comment - shows plain English summary of changes

---

## Governance Authority

**Constitutional Authority**: CS2_AGENT_FILE_AUTHORITY_MODEL.md

**Who Can Update Baselines**: CS2 (Johan Ras) ONLY

**Modification Protocol**: 
1. Agent proposes change (plain English explanation)
2. CS2 reviews and approves/denies
3. CS2 updates baseline manually
4. Git history provides audit trail

**Prohibited**:
- ❌ Agents updating baselines directly
- ❌ Automated baseline updates
- ❌ Baseline updates without CS2 approval
- ❌ Bypassing gate without PREHANDOVER_PROOF evidence

---

## References

- **Authority**: CS2_AGENT_FILE_AUTHORITY_MODEL.md
- **Pattern**: Industry standard (infrastructure-as-code baseline comparison)
- **Similar To**: Terraform plan/apply, Kubernetes ConfigMap promotion
- **Bootstrap Learning**: TBD (will create BL-028 after system validated)

---

## Version History

| Version | Date | Change | Authority |
|---------|------|--------|-----------|
| 1.0.0 | 2026-02-04 | Initial implementation | CS2 Directive |

---

**This system ensures agent files remain under CS2 control while allowing agents to propose necessary changes through governed process.
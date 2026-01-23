# Scope Declaration: Batch 5 Governance Liaison + Architecture Layer-Down

**Date**: 2026-01-23  
**Authority**: governance-liaison agent  
**Canonical Source**: APGI-cmy/maturion-foreman-governance  
**Protocol**: CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md, GOVERNANCE_RIPPLE_MODEL.md

---

## Objective

Execute Batch 5 of the office-app governance alignment plan: Layer down governance liaison specialization and architecture requirement canons.

**Batch**: 5 of 10  
**Canon Count**: 10 files  
**Agent File Updates**: None (all agents complete after Batch 4)

---

## Files to be Modified

### New Governance Canons (10 files)

All files will be added to `governance/canon/`:

1. **GOVERNANCE_LIAISON_MINIMUM_APPOINTMENT_REQUIREMENTS.md** (42,602 bytes)
   - Purpose: Governance liaison minimum requirements
   - Source: canonical governance repo

2. **GOVERNANCE_LIAISON_MINIMUM_REQUIREMENTS_VALIDATION.md** (20,579 bytes)
   - Purpose: Governance liaison validation protocol
   - Source: canonical governance repo

3. **GOVERNANCE_LIAISON_ROLE_SURVEY.md** (17,918 bytes)
   - Purpose: Governance liaison role survey
   - Source: canonical governance repo

4. **GOVERNANCE_LIAISON_TRAINING_PROTOCOL.md** (30,173 bytes)
   - Purpose: Governance liaison training
   - Source: canonical governance repo

5. **ARCHITECTURE_COMPLETENESS_REQUIREMENTS.md** (36,602 bytes)
   - Purpose: Architecture completeness requirements
   - Source: canonical governance repo

6. **APP_STARTUP_REQUIREMENTS_DECLARATION.md** (42,109 bytes)
   - Purpose: Application startup requirements
   - Source: canonical governance repo

7. **BUILD_EFFECTIVENESS_STANDARD.md** (1,695 bytes)
   - Purpose: Build effectiveness measurement
   - Source: canonical governance repo

8. **BUILD_TREE_EXECUTION_MODEL.md** (39,040 bytes)
   - Purpose: Build dependency tree model
   - Source: canonical governance repo

9. **BUILD_NODE_INSPECTION_MODEL.md** (32,317 bytes)
   - Purpose: Build node inspection protocol
   - Source: canonical governance repo

10. **COMBINED_TESTING_PATTERN.md** (23,260 bytes)
    - Purpose: Combined testing patterns
    - Source: canonical governance repo

### Updated Documentation (1 file)

**GOVERNANCE_ARTIFACT_INVENTORY.md**
- Update total canon count: 42 → 50
- Add Batch 5 section with 10 canons
- Update batch summary
- Update last-updated timestamp

---

## Pre-Existing State

**Current Canon Count**: 42 canons (from Batches 1-4 + earlier batch labeled "5")  
**Target Canon Count**: 50 canons (42 + 10 new)  
**Current Agent LOCKED Sections**: 5/5 builder agents (100% complete)

---

## Success Criteria

- [x] All 10 canons verified present in canonical governance repository
- [ ] All 10 canons copied to local `governance/canon/` directory
- [ ] GOVERNANCE_ARTIFACT_INVENTORY.md updated with Batch 5 section
- [ ] Total canon count: 50 (verified)
- [ ] All gates pass locally (exit code 0):
  - yamllint validation
  - scope-to-diff validation
  - JSON validation (if applicable)
- [ ] PREHANDOVER_PROOF created with all validation evidence

---

## Dependencies

**Requires**: Batches 1-4 complete (✅ Done)  
**Blocks**: Batch 6 (Memory, Platform & Compliance)

---

## Change Type

**Type**: Governance Layer-Down  
**Risk Level**: LOW (read-only governance canon additions)  
**Test Impact**: None (no code changes)  
**Documentation Impact**: GOVERNANCE_ARTIFACT_INVENTORY.md updated

---

## Validation Commands

```bash
# YAML validation
yamllint .github/agents/*.md

# Scope-to-diff validation
.github/scripts/validate-scope-to-diff.sh

# JSON validation (if applicable)
find governance -name "*.json" -exec jq empty {} \;

# File format checks
git diff --check
```

---

**Authority**: governance-liaison agent per CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md  
**Canonical Governance Source**: APGI-cmy/maturion-foreman-governance  
**Layer-Down Timestamp**: 2026-01-23T12:42:00Z

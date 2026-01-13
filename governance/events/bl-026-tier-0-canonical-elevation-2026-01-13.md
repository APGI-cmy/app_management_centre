# Governance Event: BL-026 Elevated to Tier-0 Constitutional Status

**Event ID**: GOV-EVENT-2026-01-13-T0-015  
**Date**: 2026-01-13  
**Type**: Tier-0 Canon Addition / Constitutional Elevation  
**Status**: Visibility Pending  
**Authority**: Governance Liaison  
**Target**: Foreman (FM) + All 5 Builders

---

## Summary

BL-026 Automated Deprecation Detection Gate has been elevated to **Tier-0 Constitutional Status** as **T0-015**, ensuring all agents are engrained with deprecation gate requirements at runtime, not just via documentation.

This prevents future PRs from being handed over with BL-026 violations by making deprecation detection a constitutional governance requirement.

---

## What Changed

### 5 Core Files Updated (Tier-0 Ripple Pattern)

**Files Modified**:
1. `governance/TIER_0_CANON_MANIFEST.json` - Added T0-015 entry, updated version to 1.3.0
2. `.agent` - Added T0-015 to constitutional_documents, updated manifest_version to 1.3.0
3. `scripts/validate_tier0_activation.py` - Updated EXPECTED_TIER0_COUNT from 14 to 15
4. `.github/agents/ForemanApp-agent.md` - Updated all references from 14 to 15 Tier-0 documents
5. `.github/workflows/tier0-activation-gate.yml` - Updated document count and added BL-026 to list

### T0-015 Specification

```json
{
  "id": "T0-015",
  "path": "governance/policies/AUTOMATED_DEPRECATION_DETECTION_GATE.md",
  "title": "Automated Deprecation Detection Gate (BL-026)",
  "authority": "Constitutional Authority",
  "purpose": "Prohibits entry or retention of deprecated APIs in repository; enforces build-to-green and zero-debt requirements",
  "validation_required": true,
  "immutable": true,
  "gate_type": "PRE_COMMIT_GATE"
}
```

---

## Why This Change

### Problem

Recent PRs were handed over with BL-026 violations because:
- BL-026 existed as Tier-1 constitutional policy
- BL-026 was NOT part of the 14 Tier-0 canon documents agents load on execution
- Agents had no runtime awareness of deprecation requirements
- Documentation, tooling, and gates referenced BL-026, but agents themselves didn't "know" it

### Root Cause

**Governance-Runtime Synchronization Gap**: BL-026 was canonical in documentation and tooling but not engrained in agent runtime context via the Tier-0 canon loading mechanism.

### Solution

Elevate BL-026 to Tier-0 status (T0-015) so:
- Agents load BL-026 requirements on every execution
- BL-026 violations are treated as constitutional failures
- Deprecation gate becomes unbreakable, like Zero Test Debt and Build-to-Green

---

## Impact on FM

### Immediate Changes

**FM MUST now**:
1. **Recognize T0-015** as constitutional authority (same as T0-001 through T0-014)
2. **Block builds** on any BL-026 violation (deprecated API usage)
3. **Treat violations** as catastrophic governance failures
4. **Escalate exceptions** per BL-026 exception process (FM approval + quarterly review)

### FM Authority Enhanced

FM now has **constitutional backing** to:
- Reject PRs with deprecated API usage (Python 3.12+ patterns required)
- Block handover on deprecation warnings
- Enforce zero-deprecation-debt as unbreakable requirement
- Grant exceptions only with explicit approval + documented justification

### No Behavioral Change Required

**Why**: FM already enforces BL-026 via:
- Pre-commit hooks (`.githooks/pre-commit-deprecation`)
- CI gate (`.github/workflows/deprecation-detection-gate.yml`)
- Zero Warning Test Debt doctrine

**Change**: BL-026 now has **constitutional authority**, not just policy authority.

---

## Impact on Builders

### Immediate Changes

**All 5 builders MUST now**:
1. **Recognize** BL-026 as Tier-0 constitutional requirement (not just policy)
2. **Execute** `ruff check --select UP` before all handovers
3. **Remediate** all deprecated API usage before PR creation
4. **Cannot waive** BL-026 violations (FM approval required for exceptions)

### Enforcement Elevation

**Before**: BL-026 = Tier-1 policy, violations = build blocker  
**After**: BL-026 = Tier-0 constitutional requirement, violations = catastrophic failure

**Consequence**: BL-026 violations now escalate to FM/Johan, not just gate failures.

### Behavioral Change

**PROHIBITED** (now constitutional violation):
- Using `datetime.utcnow()` (deprecated Python 3.12+)
- Using `datetime.utcfromtimestamp()` (deprecated Python 3.12+)
- Using `typing.Dict`, `typing.List` (obsolete Python 3.9+)
- Any deprecated pattern detected by `ruff --select UP`

**REQUIRED**:
- Modern datetime patterns (`datetime.now(timezone.utc)`)
- Built-in type hints (`dict[str, int]` not `Dict[str, int]`)
- Run `ruff check --select UP --fix` before handover
- Include deprecation check in PREHANDOVER_PROOF

---

## Grace Period & Enforcement Timeline

### Compliance Deadline

**IMMEDIATE** - No grace period

**Why**: 
- BL-026 enforcement already active via pre-commit hooks + CI gate
- All existing code already compliant (per Wave 3.1 remediation)
- Builders already executing deprecation checks
- This change adds constitutional backing, not new behavior

### Enforcement

**Effective 2026-01-13**:
- All new PRs MUST pass BL-026 Tier-0 validation
- Violations block merge (constitutional failure)
- Exceptions require FM approval + quarterly review

---

## FM Adjustments Needed

### None Required

**Why**:
- BL-026 enforcement already operational (pre-commit + CI)
- FM already blocks on deprecation violations
- This change elevates authority level, not enforcement mechanism

**FM Benefit**: 
- Constitutional backing for rejections ("T0-015 violation" vs "policy violation")
- Clearer escalation path (constitutional failures go to Johan)
- Stronger position when granting/denying exceptions

---

## Builder Notification Required

**FM MUST notify all 5 builders**:

**To**: api-builder, schema-builder, ui-builder, integration-builder, qa-builder

**Subject**: CONSTITUTIONAL ELEVATION: BL-026 Now Tier-0 (T0-015)

**Message**:
```
BL-026 Automated Deprecation Detection Gate has been elevated to Tier-0 Constitutional Status (T0-015).

EFFECTIVE IMMEDIATELY:
- BL-026 is now a Tier-0 constitutional requirement (same as Zero Test Debt, Build-to-Green)
- Deprecated API usage = CONSTITUTIONAL VIOLATION (not just policy violation)
- No PRs may be handed over with BL-026 violations
- Exceptions require FM approval + quarterly review

WHAT THIS MEANS FOR YOU:
- Continue running `ruff check --select UP` before handover (already required)
- BL-026 violations now escalate to FM/Johan (constitutional failure)
- Cannot waive or skip deprecation checks (constitutional enforcement)

NO BEHAVIORAL CHANGE:
- You already execute deprecation checks (pre-commit + CI)
- This change adds constitutional authority, not new requirements

TECHNICAL DETAILS:
- T0-015 path: governance/policies/AUTOMATED_DEPRECATION_DETECTION_GATE.md
- Prohibited: datetime.utcnow(), typing.Dict, typing.List, etc.
- Required: datetime.now(timezone.utc), dict[str, int], etc.
- Auto-fix: ruff check --select UP --fix

COMPLIANCE: IMMEDIATE (no grace period - already compliant)

Questions? Contact FM.
```

---

## Ripple Validation Results

**Consistency Validator**: ✅ ALL CHECKS PASSED  
**Activation Validator**: ✅ ALL CHECKS PASSED  

**Files Synchronized**:
- ✅ governance/TIER_0_CANON_MANIFEST.json (version 1.3.0, 15 documents)
- ✅ .agent (manifest_version 1.3.0, 15 constitutional_documents)
- ✅ scripts/validate_tier0_activation.py (EXPECTED_TIER0_COUNT = 15)
- ✅ .github/agents/ForemanApp-agent.md (all references updated to 15)
- ✅ .github/workflows/tier0-activation-gate.yml (document count + list updated)

**Ripple Completeness**: ✅ COMPLETE (5/5 files updated)

---

## References

- **T0-015 Policy**: `governance/policies/AUTOMATED_DEPRECATION_DETECTION_GATE.md`
- **Tier-0 Manifest**: `governance/TIER_0_CANON_MANIFEST.json` (v1.3.0)
- **Pre-commit Hook**: `.githooks/pre-commit-deprecation`
- **CI Gate**: `.github/workflows/deprecation-detection-gate.yml`
- **Previous RCA**: Issue #576 (Why agents handed over unclean PRs)
- **BL-026 Learning**: `BOOTSTRAP_EXECUTION_LEARNINGS.md` (Bootstrap Learning BL-026)

---

## Status

**Tier-0 Canon Updated**: ✅ COMPLETE (15 documents)  
**5-File Ripple**: ✅ COMPLETE (all files synchronized)  
**Validation Passing**: ✅ COMPLETE (consistency + activation)  
**FM Visibility**: 📍 PENDING (this event)  
**Builder Notification**: ⏸️ PENDING (FM to execute)

---

**Authority**: Governance Liaison  
**Date**: 2026-01-13  
**Compliance Deadline**: IMMEDIATE (no grace period)  
**Tier-0 Canon Version**: 1.3.0 (was 1.2.0)  
**Total Tier-0 Documents**: 15 (was 14)

---

**END OF GOVERNANCE EVENT**

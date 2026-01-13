# Governance Event: Builder Contract Pre-Handover Execution Protocol Update

**Event ID**: GOV-EVENT-2026-01-12-BL-028  
**Date**: 2026-01-12  
**Type**: Governance Change / Builder Contract Update  
**Status**: Visibility Pending  
**Authority**: Governance Liaison  
**Target**: Foreman (FM) + All 5 Builders

---

## Summary

All 5 builder contracts have been updated to include explicit "Pre-Handover Execution Protocol (MANDATORY v2.0.0+)" sections in response to two recent protocol violations (PR #546, PR #572).

This change enforces the existing Execution Bootstrap Protocol v2.0.0+ requirements directly within builder contracts, eliminating the governance-contract synchronization gap.

---

## What Changed

### Builder Contracts Updated (5 files)

**Files**:
- `.github/agents/api-builder.md`
- `.github/agents/schema-builder.md`
- `.github/agents/ui-builder.md`
- `.github/agents/integration-builder.md`
- `.github/agents/qa-builder.md`

**Changes**: Added new section "Pre-Handover Execution Protocol (MANDATORY v2.0.0+)" containing:

1. **7 Required Steps** before handover:
   - Identify execution artifacts
   - Execute ALL checks locally
   - Verify exit codes = 0
   - Capture evidence
   - Create PREHANDOVER_PROOF
   - Create PR only after all checks pass

2. **Hard Rule**: "CI is confirmation, NOT diagnostic"

3. **Consequences** for violations:
   - 1st violation: PR rejected, must remediate
   - 2nd violation: Contract review with FM
   - 3rd violation: Builder replacement

4. **Pre-handover Checklist** (6 items, all must be checked)

5. **Domain-specific execution examples** for each builder

### PR Template Updated

**File**: `.github/PULL_REQUEST_TEMPLATE.md`

**Changes**: Added new section "Pre-Handover Execution Evidence (Required for ALL PRs)" requiring:
- Execution Bootstrap Protocol v2.0.0+ compliance checklist
- Local execution summary with commands
- Evidence documentation
- Clear instruction: "If any box unchecked: Close PR and execute locally first"

### Governance Learning Created

**File**: `bootstrap/learnings/BL-028-BUILDER-PREHANDOVER-EXECUTION-ENFORCEMENT.md`

**Content**: Full governance learning document capturing:
- Problem statement (2 protocol violations)
- Root cause analysis (governance-contract synchronization gap)
- Resolution actions (this update)
- Prevention measures
- Lessons learned
- Proposal for BL-029 (long-term contract synchronization protocol)

---

## Why This Change

### Problem

Two builders submitted PRs without executing local checks:
- **PR #546** (Governance Liaison): BL-026 violations discovered in CI
- **PR #572** (integration-builder): BL-026 violations discovered in CI

### Root Cause

Builder contracts referenced Execution Bootstrap Protocol v2.0.0+ in governance bindings but did NOT explicitly spell out the mandatory pre-handover steps. Builders may not have been aware they needed to execute checks locally before creating PRs.

### Solution

Make protocol requirements explicit and actionable within builder contracts themselves, not just via governance references.

---

## Impact on FM

### FM Review Responsibility

FM now has explicit grounds to reject PRs that:
- Do NOT include PREHANDOVER_PROOF (for execution-related PRs)
- Fail CI checks (indicating builder didn't execute locally)
- Lack evidence of local execution

### FM Enforcement

FM should:
1. **Verify** all new PRs include pre-handover execution evidence
2. **Reject** PRs missing evidence or failing CI
3. **Track** violations per builder (1st, 2nd, 3rd strike)
4. **Escalate** to contract review on 2nd violation
5. **Consider** builder replacement on 3rd violation

### FM Benefit

- Reduces time wasted reviewing PRs with CI failures
- Enforces "CI is confirmation, NOT diagnostic" principle
- Establishes clear accountability for protocol violations
- Provides explicit grounds for PR rejection

---

## Impact on Builders

### Immediate Changes

**All 5 builders MUST**:
1. Read updated contract section "Pre-Handover Execution Protocol"
2. Execute ALL checks locally before creating PR
3. Verify ALL exit codes = 0
4. Capture evidence of local execution
5. Create PREHANDOVER_PROOF (for execution-related PRs)
6. Complete pre-handover checklist

**CANNOT**:
- Rely on CI to discover failures
- Submit PR with failing checks
- Skip local execution

### Behavioral Change

**Before**: Builder could create PR → CI discovers failures → Builder fixes → CI re-runs

**After**: Builder MUST execute locally → Verify GREEN → Create PR → CI confirms GREEN

**Consequence**: CI failures now indicate protocol violation, not normal workflow

---

## Grace Period & Enforcement Timeline

### Compliance Deadline

**2026-02-11** (per existing Execution Bootstrap Protocol v2.0.0+)

### Grace Period

**1 month** (2026-01-12 to 2026-02-11):
- Builders notified of contract changes
- First violations result in warning + PR rejection
- No builder replacement during grace period

### Post-Grace Enforcement

**After 2026-02-11**:
- 3-strike policy fully enforced
- No grace for protocol violations
- Violations tracked in `governance/incidents/protocol-violations/`

---

## FM Adjustments Needed

### None Required

**Why**: This change aligns with existing governance:
- Execution Bootstrap Protocol v2.0.0+ already canonical
- FM already enforces protocol at PR gate
- This change makes requirements explicit in contracts

**FM Action**: Continue current enforcement, now with explicit contract backing

---

## Builder Notification Required

**FM MUST notify all 5 builders**:

**To**: api-builder, schema-builder, ui-builder, integration-builder, qa-builder

**Subject**: MANDATORY CONTRACT UPDATE: Pre-Handover Execution Protocol (v2.0.0+)

**Message**:
```
Your builder contract has been updated to include mandatory Pre-Handover Execution Protocol requirements.

EFFECTIVE IMMEDIATELY:
- Execute ALL checks locally BEFORE creating PR
- Verify ALL exit codes = 0
- Provide PREHANDOVER_PROOF (for execution-related PRs)
- CI is CONFIRMATION, NOT diagnostic

CONSEQUENCES:
- 1st violation: PR rejected
- 2nd violation: Contract review
- 3rd violation: Builder replacement

READ YOUR UPDATED CONTRACT:
.github/agents/[your-builder].md
Section: "Pre-Handover Execution Protocol (MANDATORY v2.0.0+)"

COMPLIANCE DEADLINE: 2026-02-11
GRACE PERIOD: 1 month (warnings only)

Questions? Contact FM.
```

---

## References

- **Canonical Protocol**: `governance/canon/EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md`
- **Builder Contracts**: `.github/agents/*.md`
- **PR Template**: `.github/PULL_REQUEST_TEMPLATE.md`
- **BL-028 Learning**: `bootstrap/learnings/BL-028-BUILDER-PREHANDOVER-EXECUTION-ENFORCEMENT.md`
- **Incident PR #546**: Governance Liaison BL-026 violation
- **Incident PR #572**: integration-builder BL-026 violation

---

## Status

**Governance Change**: ✅ COMPLETE  
**Builder Contracts Updated**: ✅ COMPLETE (5/5)  
**PR Template Updated**: ✅ COMPLETE  
**BL-028 Documented**: ✅ COMPLETE  
**FM Visibility**: 📍 PENDING (this event)  
**Builder Notification**: ⏸️ PENDING (FM to execute)

---

**Authority**: Governance Liaison  
**Date**: 2026-01-12  
**Compliance Deadline**: 2026-02-11  
**Next Review**: Q2 2026 Quarterly Monitoring Report (2026-04-14)

---

**END OF GOVERNANCE EVENT**

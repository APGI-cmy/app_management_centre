# BL-028: Builder Pre-Handover Execution Enforcement

**ID**: BL-028  
**Category**: Governance Learning / Builder Protocol Violation  
**Date**: 2026-01-12  
**Status**: Active  
**Authority**: CS2 (Johan Ras) + FM  
**Severity**: HIGH

---

## Problem Statement

**Two builder protocol violations** occurred where builders submitted PRs without executing local checks, relying on CI as diagnostic tool:

1. **PR APGI-cmy/maturion-foreman-office-app#546** (Governance Liaison): Submitted governance script with BL-026 violations
2. **PR APGI-cmy/maturion-foreman-office-app#572** (integration-builder): Submitted Wave 3.1 code with BL-026 violations

**Root Cause**: Builder contracts did NOT explicitly mandate Execution Bootstrap Protocol (v2.0.0+) steps before handover.

**Impact**: 
- Builders use CI as diagnostic tool instead of confirmation
- Wastes reviewer time
- Breaks "CI is confirmation, NOT diagnostic" principle
- Creates delivery friction
- Governance protocol exists but not enforced through contracts

---

## Root Cause Analysis

### Timeline

1. **Builder contracts created** (Wave 0.1, Dec 2025)
   - Defined roles, responsibilities, scope
   - Did NOT include pre-handover execution requirements

2. **Execution Bootstrap Protocol v2.0.0 created** (PR #546, Jan 2026)
   - Created AFTER builder contracts
   - Created in response to governance needs
   - Never retrofitted into existing contracts

3. **Gap**:  Protocol created but not propagated to builder contracts

### Why The Gap Exists

**Probable reasons**:

1. **Temporal gap**: 
   - Builder contracts:  Early (Wave 0.1 recruitment)
   - Execution Protocol v2.0.0: Later (governance evolution)
   - Contracts not updated when protocol created

2. **Ownership ambiguity**:
   - Who owns keeping contracts current?  (FM?  Governance Liaison?)
   - No process for "when governance changes, update contracts"

3. **Implicit assumption**:
   - Assumed builders would "know" to run checks locally
   - Protocol documented in governance but not pushed to builders
   - Builders read contracts, not governance docs

4. **No contract versioning/sync**:
   - Contracts are static after creation
   - No mechanism to push governance updates to contracts
   - No "contract v3.1" when protocol v2.0.0 released

### Governance Gap:  Contract Synchronization

**The real issue**: 

```
Governance evolves → New protocols created → Contracts not updated
```

**Missing process**:
```
Governance change → Contract impact analysis → Contract update → Builder notification
```

---

## Resolution (This Issue)

### Actions Taken

#### Action 1: Updated ALL 5 Builder Contracts

**Files updated**:
- `.github/agents/api-builder.md` ✅
- `.github/agents/schema-builder.md` ✅
- `.github/agents/ui-builder.md` ✅
- `.github/agents/integration-builder.md` ✅
- `.github/agents/qa-builder.md` ✅

**Added section**: "Pre-Handover Execution Protocol (MANDATORY v2.0.0+)"

**Content**:
- 7 required steps before handover
- Local execution mandate
- Hard rule: "CI is confirmation, NOT diagnostic"
- Consequences for violations (1st: rejection, 2nd: review, 3rd: replacement)
- Pre-handover checklist

#### Action 2: Updated PR Template

**File**: `.github/PULL_REQUEST_TEMPLATE.md` ✅

**Added**:
- "Pre-Handover Execution Evidence (Required for ALL PRs)" section
- Execution Bootstrap Protocol v2.0.0+ compliance checklist
- Local execution summary requirement
- Evidence documentation requirement

#### Action 3: Verified Builder Onboarding

**Files checked**:
- `governance/AGENT_ONBOARDING.md` ✅ (already includes protocol training)
- `governance/BUILDER_TRAINING_CHECKLIST.md` ✅ (already includes protocol training)

**Status**: Onboarding materials already compliant (added in previous governance updates)

#### Action 4: Created BL-028 Documentation

**This document** serves as the governance learning record.

---

## Prevention

### Immediate Prevention (This Issue)

1. ✅ Builder contracts now explicitly mandate pre-handover execution
2. ✅ PR template requires evidence of local execution
3. ✅ Training materials already include protocol compliance
4. ✅ Consequences clearly stated (3-strike policy)

### Long-Term Prevention (BL-029 Proposal)

**Proposed**: BL-029: Governance-Contract Synchronization Protocol

**Need**: Process to ensure governance changes propagate to builder contracts

**Components**:
1. **Contract Impact Analysis**: When governance protocol changes, analyze impact on builder contracts
2. **Contract Update Process**: Systematic process to update contracts when governance evolves
3. **Builder Notification**: Mechanism to notify builders of contract changes
4. **Contract Versioning**: Version contracts when material changes occur
5. **Governance-Contract Binding**: Explicit linkage between governance changes and contract updates

**Status**: PARKED - Route to FM/Johan for consideration

---

## Governance Impact

### Governance Canon Updates Required

None - existing protocol already documented in:
- `governance/canon/EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md`

### Compliance Requirements

**For all builders**:
- Must execute all checks locally before creating PR
- Must verify exit codes = 0
- Must provide PREHANDOVER_PROOF for execution-related PRs
- Must NOT rely on CI to discover failures

**Compliance Deadline**: 2026-02-11 (per existing protocol)  
**First Monitoring Report**: 2026-04-14 (Q2 2026)

### Enforcement

**Violations tracked as**:
- 1st violation: PR rejected, remediation required
- 2nd violation: Contract review with FM
- 3rd violation: Builder replacement consideration

**Incident tracking**: All violations logged in `governance/incidents/protocol-violations/`

---

## Builder Communication

### Communication Required

**To**: All 5 builders (api-builder, schema-builder, ui-builder, integration-builder, qa-builder)

**Message**:
```
MANDATORY CONTRACT UPDATE: Pre-Handover Execution Protocol (v2.0.0+)

All builder contracts updated to include mandatory pre-handover execution protocol.

REQUIREMENTS:
- Execute ALL checks locally BEFORE creating PR
- Verify ALL exit codes = 0
- Provide PREHANDOVER_PROOF for execution-related PRs
- CI is CONFIRMATION, NOT diagnostic

CONSEQUENCES:
- 1st violation: PR rejected
- 2nd violation: Contract review
- 3rd violation: Builder replacement

READ YOUR UPDATED CONTRACT: .github/agents/[your-builder].md
COMPLIANCE DEADLINE: 2026-02-11

Questions? Contact FM.
```

---

## Related Issues

- **PR #546**: Governance Liaison BL-026 violation (first incident)
- **PR #572**: integration-builder BL-026 violation (second incident)
- **Issue #[NUMBER]**: This remediation issue

---

## Lessons Learned

### What Went Wrong

1. **Contract-Governance Desynchronization**: Governance evolved faster than contracts updated
2. **Implicit Protocol Assumption**: Assumed builders would read governance docs, not just contracts
3. **No Synchronization Process**: No systematic process to propagate governance to contracts
4. **Temporal Gap**: Protocol created after contracts recruited builders

### What Went Right

1. **Violations Detected Quickly**: Both violations caught at PR review stage
2. **Root Cause Identified**: Clear understanding of contract-governance gap
3. **Comprehensive Fix**: All 5 contracts updated simultaneously
4. **Training Already Present**: Onboarding materials already compliant
5. **Clear Consequences**: 3-strike policy clearly communicated

### Process Improvements

1. **Contract Updates**: Governance changes now trigger contract review
2. **Explicit Protocol Steps**: Pre-handover steps explicitly listed in contracts
3. **Evidence Requirement**: PR template requires execution evidence
4. **Communication Plan**: Builders notified of contract changes

---

## Monitoring & Effectiveness

### Success Criteria

**Short-term (1 month)**:
- [ ] Zero protocol violations from builders
- [ ] All PRs include PREHANDOVER_PROOF (when applicable)
- [ ] All PRs pass CI on first run (confirmation, not diagnostic)

**Long-term (3 months)**:
- [ ] Builder habit established: local execution before handover
- [ ] No violations requiring escalation beyond 1st strike
- [ ] CI used purely as confirmation mechanism

### Monitoring

**Quarterly Report**: Include in Execution Bootstrap Protocol Quarterly Monitoring Report (template: `governance/templates/EXECUTION_BOOTSTRAP_PROTOCOL_QUARTERLY_MONITORING_REPORT.md`)

**Metrics**:
- Number of protocol violations by builder
- Number of PRs with PREHANDOVER_PROOF
- CI pass rate on first run (should be 100%)

---

## References

- **Canonical Protocol**: `governance/canon/EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md`
- **Builder Contracts**: `.github/agents/*.md`
- **PR Template**: `.github/PULL_REQUEST_TEMPLATE.md`
- **Training**: `governance/BUILDER_TRAINING_CHECKLIST.md`
- **Incident PR #546**: Governance Liaison BL-026 violation
- **Incident PR #572**: integration-builder BL-026 violation

---

## Status Summary

**Learning Captured**: ✅ COMPLETE  
**Contracts Updated**: ✅ COMPLETE  
**PR Template Updated**: ✅ COMPLETE  
**Training Verified**: ✅ COMPLETE  
**Documentation Created**: ✅ COMPLETE  
**Builder Communication**: ⏸️ PENDING (FM to execute)  
**BL-029 Proposal**: 📦 PARKED (route to FM/Johan)

---

**Authority**: CS2 (Johan Ras) + FM  
**Governance Learning ID**: BL-028  
**Compliance Deadline**: 2026-02-11  
**Next Review**: Q2 2026 Quarterly Monitoring Report (2026-04-14)

---

**END OF BL-028 GOVERNANCE LEARNING**

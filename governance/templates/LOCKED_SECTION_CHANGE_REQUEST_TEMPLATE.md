# Locked Section Change Request

**Request ID**: LSCR-[YYYY-MM-DD]-[NNN]  
**Date**: [YYYY-MM-DD]  
**Requester**: [Name/Role]  
**Agent Affected**: [Agent Name]  
**Status**: [PENDING / APPROVED / REJECTED]

---

## Section to Modify

**Section Title**: [e.g., "Contract Modification Prohibition (LOCKED)"]  
**Agent File**: [e.g., `.github/agents/governance-liaison.md`]  
**Current Lock Date**: [YYYY-MM-DD]  
**Current Authority**: [e.g., AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0]

---

## Proposed Change

### Current Content
```markdown
[Paste exact current content of locked section]
```

### Proposed Content
```markdown
[Paste exact proposed new content]
```

### Diff Summary
[Describe what is being changed, added, or removed]

---

## Constitutional Justification

### Reason for Change
[Explain WHY this locked section must be modified]

### Alignment with BUILD_PHILOSOPHY.md
[Explain how this change supports One-Time Build Correctness, Zero Regression, or other constitutional principles]

### Governance Impact Analysis
**Impact on**:
- [ ] Other agents: [YES/NO - describe]
- [ ] Builder orchestration: [YES/NO - describe]
- [ ] PR gate enforcement: [YES/NO - describe]
- [ ] Tier-0 canonical governance: [YES/NO - describe]
- [ ] Agent authority boundaries: [YES/NO - describe]

---

## Risk Assessment

### Risks if Change is APPROVED
[What could go wrong if we make this change?]

### Risks if Change is REJECTED
[What could go wrong if we DON'T make this change?]

### Mitigation Plan
[How will we prevent negative consequences?]

---

## Alternatives Considered

1. **Alternative 1**: [Describe]
   - Pros: [List]
   - Cons: [List]
   - Rejected because: [Reason]

2. **Alternative 2**: [Describe]
   - Pros: [List]
   - Cons: [List]
   - Rejected because: [Reason]

---

## Implementation Plan

### Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Affected Files
- [ ] `.github/agents/[agent-name].md`
- [ ] `governance/canon/AGENT_CONTRACT_PROTECTION_PROTOCOL.md` (if protocol update needed)
- [ ] `.github/scripts/check_locked_sections.py` (if detection logic update needed)
- [ ] [Other files]

### Rollback Plan
[How do we revert if this causes problems?]

---

## Approval Section

### CS2 Review (Johan Ras / Governance Administrator)

**Reviewed By**: ___________________________  
**Date**: ___________________________  
**Decision**: [ ] APPROVED  [ ] REJECTED  [ ] NEEDS MORE INFO  

**Rationale**:
```
[CS2 explains decision]
```

**Override Code** (if approved): `CS2-OVERRIDE-LSCR-[ID]`

---

## Implementation Record

**Implemented By**: [Agent Contract Administrator]  
**Implementation Date**: [YYYY-MM-DD]  
**Commit SHA**: [commit hash]  
**PR Number**: [PR #]

**Verification**:
- [ ] Locked section modified as approved
- [ ] CI gate updated (if needed)
- [ ] Audit trail updated
- [ ] Protection registry updated
- [ ] All affected agents validated

---

## Audit Trail

| Date | Action | Actor | Notes |
|------|--------|-------|-------|
| [YYYY-MM-DD] | Request Created | [Name] | Initial submission |
| [YYYY-MM-DD] | Review Started | [CS2] | Under constitutional review |
| [YYYY-MM-DD] | Decision | [CS2] | [APPROVED/REJECTED] |
| [YYYY-MM-DD] | Implemented | [Agent Contract Administrator] | Changes applied |

---

## Notes

[Any additional context, concerns, or follow-up items]

---

**Template Version**: 1.0.0  
**Authority**: governance/canon/AGENT_CONTRACT_PROTECTION_PROTOCOL.md

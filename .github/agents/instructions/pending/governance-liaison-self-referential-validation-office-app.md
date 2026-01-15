# Contract Update Request: governance-liaison Self-Referential Validation

**Date**: 2026-01-14  
**Requesting Agent**: governance-liaison  
**Target Contract**: `.github/agents/governance-liaison.md`  
**Request Type**: Enhancement (add missing requirements)  
**Authority**: Agent Contract Administrator  
**Incident**: PR #612 gate bypass (office-app)

---

## Request Summary

Add self-referential validation requirement to governance-liaison contract to prevent future incidents where agent creates new gates without testing them against the creating PR.

---

## Context

**Incident**: PR #612 created Pre-Implementation Behavior Review Gate and submitted PR without validating the new gate would correctly handle the creating PR (self-referential enforcement paradox).

**Root Cause**: Contract requires "PR-Gate Preflight" but doesn't explicitly cover validation of gates created IN THIS PR.

**Impact**: Catastrophic - agent handed over work claiming "READY FOR MERGE" despite HARD GATE blocking the PR.

**RCA**: See `.agent-admin/rca/rca_pr612_gate_bypass_office_app_2026-01-14.md`

---

## Proposed Contract Updates

### Update 1: Add Self-Referential Validation Requirement

**Location**: Section "Mandatory PR-Gate Preflight" (after line 45)

**Proposed Addition**:
```markdown
### Self-Referential Validation (New Gates)

When PR creates or modifies CI gate workflows, agent MUST validate the new/modified gate logic would correctly handle THIS PR:

**Requirement**: Test new gates against current PR before handover.

**Method**:
1. Review new gate's detection/validation logic
2. Simulate gate execution against current PR description/files  
3. If gate would block: either fix PR to satisfy gate OR declare exemption
4. Update PR description to satisfy new gate's requirements
5. Document simulation results in PREHANDOVER_PROOF

**Blocking**: YES - Handover prohibited if new gate would block without declared exemption.

**Rationale**: Prevents self-referential enforcement paradoxes where PR creates gate that blocks the creating PR.
```

### Update 2: Add Pre-Implementation Behavior Review Protocol Binding

**Location**: Section "Governance Bindings" (after line 29, before "Reference:")

**Proposed Addition**:
```markdown
- governance/canon/PRE_IMPLEMENTATION_BEHAVIOR_REVIEW_PROTOCOL.md (protocol-awareness)
```

### Update 3: Clarify "New Gates" in PR-Gate Preflight

**Location**: Section "Mandatory PR-Gate Preflight" (lines 39-45, inline clarification)

**Current Text**:
```
Before handover: MUST perform **PR-Gate Preflight** using CI definitions (workflows, scripts, policies). 
Execute in agent environment.
```

**Proposed Revision**:
```
Before handover: MUST perform **PR-Gate Preflight** using CI definitions (workflows, scripts, policies). 
Execute in agent environment.

**Gate Scope**:
- **Existing gates**: Gates present in base branch (run normally via CI scripts)
- **New gates**: Gates created/modified IN THIS PR (simulate execution manually - see Self-Referential Validation)

Agent MUST validate BOTH existing gates (run via scripts) AND new gates (simulate manually) before handover.
```

### Update 4: Add Work Classification Guidance

**Location**: New section after "FM Office Visibility | Delivery | Enhancement" (after line 71)

**Proposed Addition**:
```markdown
## Work Classification Guidance

**Purpose**: Distinguish governance infrastructure work from application enhancement work.

### Governance Infrastructure Work

**Definition**: Work that creates, modifies, or enforces governance mechanisms (gates, validators, protocols, templates, contracts).

**Protocol Applicability**: Governance infrastructure work is "documentation-only" and exempt from enhancement protocols unless it enhances application functionality.

### Application Enhancement Work

**Definition**: Work that modifies application runtime behavior (features, performance, APIs, schemas, UI/UX).

**Protocol Applicability**: Application enhancement work requires Pre-Implementation Behavior Review Protocol compliance.

### Classification Rule

**Decision criterion**: "Does this change application runtime behavior?"
- **YES** = Application enhancement (protocol required)
- **NO** = Governance infrastructure (protocol exempt)
```

---

## Justification

### Why These Updates Are Needed

1. **Update 1**: Prevents recurrence of PR #612 scenario
2. **Update 2**: Ensures agent understands protocol applicability
3. **Update 3**: Makes explicit that preflight includes new gates
4. **Update 4**: Provides clear classification framework

---

**Submitted by**: governance-liaison  
**Submission Date**: 2026-01-14  
**Review Required**: Agent Contract Administrator

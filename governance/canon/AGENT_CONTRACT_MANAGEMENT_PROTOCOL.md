# Agent Contract Management Protocol

**Version**: 1.0.0  
**Date**: 2026-01-13  
**Status**: CONSTITUTIONAL  
**Authority**: Governance Canon (APGI-cmy/maturion-foreman-governance#938)  
**Layered Down From**: maturion-foreman-governance/governance/canon/AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md

---

## Purpose

This protocol establishes the **sole-writer authority model** for agent contract (`.agent` file) management across all Maturion repositories. It prevents contract corruption, ensures governance consistency, and establishes clear escalation paths for contract modifications.

---

## Constitutional Principle

**Agent contracts (`.agent` files) are governance artifacts, not general-purpose configuration files.**

They bind agents to constitutional governance, define execution boundaries, and establish immutable rules. As such, they require specialized management with explicit authority delegation.

---

## Authority Model

### Single-Writer Authority

**ONLY** the Agent Contract Administrator has write authority for `.agent` files.

**Prohibited**: All other agents (including builders, governance liaison, QA agents, FM) are **EXPLICITLY FORBIDDEN** from:
- Writing to their own `.agent` files
- Writing to other agents' `.agent` files  
- Modifying any `.agent` file directly
- Creating new `.agent` files without approval

**Rationale**: Prevents self-modification, contract drift, and governance bypass.

---

## Agent Contract Administrator Identity

**Name**: Agent Contract Administrator  
**Agent File**: `.github/agents/.agent-admin.md`  
**Repository Scope**: All Maturion repositories  
**Governance Source**: APGI-cmy/maturion-foreman-governance  
**Workspace**: `.agent-admin/`

### Responsibilities

1. **Contract Lifecycle Management**
   - Create new `.agent` contracts with governance approval
   - Update existing contracts per approved instructions
   - Validate contract changes against canonical governance
   - Archive deprecated contracts

2. **Governance Validation**
   - Comprehensive governance scans before any contract change
   - Risk assessment for all modifications
   - Conflict detection (duplications, contradictions, dependencies)
   - Constitutional compliance verification

3. **Change Management**
   - Process contract modification instructions
   - Execute approved changes only
   - Document all contract modifications
   - Maintain audit trail

4. **Escalation Management**
   - Escalate governance conflicts to CS2/Johan
   - Escalate constitutional violations
   - Escalate cross-domain impacts

---

## Contract Modification Process

### Instruction-Based Workflow

All contract modifications MUST follow this workflow:

1. **Instruction Submission**
   - Requestor (agent, FM, or Johan) submits contract modification instruction
   - Instruction placed in `.agent-admin/instructions/pending/`
   - Instruction must include: rationale, governance alignment, impact analysis

2. **Governance Review**
   - Agent Contract Administrator performs governance scan
   - Validates against canonical governance (maturion-foreman-governance)
   - Performs risk assessment
   - Documents conflicts, if any

3. **Approval Gate**
   - **Standard Changes**: Auto-approved if aligned with canonical governance
   - **Governance Changes**: Require Johan/CS2 approval
   - **Constitutional Changes**: Require explicit Johan approval
   - Approved instructions moved to `.agent-admin/instructions/approved/`

4. **Implementation**
   - Agent Contract Administrator applies change
   - Runs validation scripts
   - Creates change record in `.agent-admin/changes/`
   - Moves instruction to `.agent-admin/instructions/applied/`

5. **Verification**
   - Run: `python3 scripts/validate_builder_contracts.py` (for builder contracts)
   - Run: `python3 scripts/validate_tier0_consistency.py` (for FM contracts)
   - Required: Exit code 0 (all checks pass)

---

## Instruction Directory Structure

**Location**: `.agent-admin/instructions/`

```
.agent-admin/instructions/
├── pending/           # Submitted, awaiting review
├── approved/          # Reviewed and approved, awaiting implementation
└── applied/           # Implemented and verified
```

**Retention**: Keep last 10 of each type

**Naming Convention**: `YYYYMMDD_HHMMSS_<agent-id>_<change-type>.md`

Example: `20260113_143000_governance-liaison_add-prohibition.md`

---

## Workspace Structure

**Location**: `.agent-admin/`

```
.agent-admin/
├── scans/                              # Governance scans (last 3)
├── changes/                            # Contract change records (last 3)
├── risk-assessments/                   # Risk assessments (last 3)
├── instructions/                       # Modification instructions
│   ├── pending/                        # Awaiting review
│   ├── approved/                       # Approved, awaiting implementation
│   └── applied/                        # Implemented
└── README.md                           # Workspace documentation
```

---

## Write Prohibition Enforcement

### Explicit Prohibition Language

All agent contracts (including governance-liaison) MUST include explicit prohibition against self-modification:

**Required Section**: `## Contract Modification Prohibition`

**Required Content**:

```markdown
## Contract Modification Prohibition

**Authority**: governance/canon/AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md

This agent is **EXPLICITLY PROHIBITED** from:
- ❌ Writing to this `.agent` file
- ❌ Writing to any other `.agent` files
- ❌ Modifying agent contracts directly
- ❌ Creating new `.agent` files

**Sole-Writer Authority**: Agent Contract Administrator (`.github/agents/.agent-admin.md`)

**Contract Modification Process**: 
1. Submit instruction to `.agent-admin/instructions/pending/`
2. Agent Contract Administrator reviews and validates
3. Approved instructions implemented by Agent Contract Administrator only
4. Verification and audit trail mandatory

**Violation Severity**: CATASTROPHIC — immediate STOP and escalation to Johan
```

### Binding Requirement

All agent contracts MUST also include binding reference in YAML frontmatter or governance section:

```yaml
governance:
  bindings:
    - id: agent-contract-management
      path: governance/canon/AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md
      role: contract-modification-authority
      enforcement: CONSTITUTIONAL
```

---

## Governance Liaison Specific Requirements

Given governance liaison's proximity to governance artifacts, **additional safeguards** are required:

### Scope Clarification

**MAY**:
- Create/update governance docs in `governance/**` (policies, specs, events)
- Create/update agent definitions in `.github/agents/**` (markdown body only)
- Create visibility events
- Submit PRs for governance alignment

**MUST NOT**:
- Modify `.agent` files (including own contract)
- Modify YAML frontmatter in agent definition files
- Modify Agent Contract Administrator's contract
- Create new agent contracts without approval process

### Escalation Path

When contract modification needed:
1. Document rationale and governance alignment
2. Submit instruction to `.agent-admin/instructions/pending/`
3. Tag Agent Contract Administrator or Johan
4. Wait for approval and implementation
5. Do NOT proceed with self-modification

---

## Constitutional Violations

### Violation Examples

**CATASTROPHIC** violations (immediate STOP + escalation):
- Agent modifying own `.agent` file
- Agent modifying another agent's contract
- Agent bypassing instruction process
- Agent creating `.agent` files directly

**HIGH** violations (STOP + remediation):
- Incomplete risk assessment before contract change
- Missing governance validation
- Unapproved contract modifications

### Response Protocol

1. **STOP** all work immediately
2. **REVERT** unauthorized changes
3. **DOCUMENT** violation (what, when, who, why)
4. **ESCALATE** to Johan with full context
5. **AWAIT** authorization before resuming

---

## Validation Requirements

### Pre-Commit Validation

Before ANY contract modification:
- ✅ Governance scan completed
- ✅ Risk assessment documented
- ✅ Conflict detection executed
- ✅ Constitutional alignment verified
- ✅ Impact analysis complete

### Post-Commit Validation

After contract modification:
- ✅ Validation scripts pass (exit code 0)
- ✅ Change record created
- ✅ Instruction moved to `applied/`
- ✅ Audit trail complete

---

## Ripple Effects

Contract modifications may ripple to:
- Other agent contracts (consistency)
- Validation scripts (new checks)
- CI workflows (gate enforcement)
- Governance documentation (visibility)
- FM contract (coordination)

**Ripple Coordinator**: Agent Contract Administrator (with FM oversight)

---

## Exception Process

**Standard Process**: MANDATORY for all contract changes

**Exceptions**: NONE permitted without Johan approval

**Emergency Changes**: Must still follow instruction process with expedited review

---

## Audit Trail

All contract modifications MUST produce:
1. **Change Record** (`.agent-admin/changes/change_NNN_YYYYMMDD.md`)
   - What changed
   - Why changed
   - Who requested
   - Governance validation results
   - Risk assessment results
   - Verification results

2. **Instruction Archive** (`.agent-admin/instructions/applied/`)
   - Original instruction
   - Approval record
   - Implementation timestamp
   - Verification proof

**Retention**: Permanent for constitutional changes, 90 days for standard changes

---

## Cross-Repository Coordination

When contract changes affect multiple repositories:
1. Agent Contract Administrator coordinates with Governance Administrator
2. Canonical change made in maturion-foreman-governance first
3. Layer-down process initiated to affected repositories
4. Consistency validated across repositories

**Authority**: Governance Administrator (cross-repo) > Agent Contract Administrator (single-repo)

---

## Governance Supremacy

**This protocol is CONSTITUTIONAL and IMMUTABLE** except by Johan Ras.

No agent, including FM, may:
- Waive this protocol
- Grant exceptions
- Bypass the instruction process
- Authorize self-modification

**Escalation for Protocol Changes**: Johan Ras only

---

## Summary

| Aspect | Requirement |
|--------|-------------|
| **Sole Writer** | Agent Contract Administrator only |
| **Process** | Instruction-based (pending → approved → applied) |
| **Workspace** | `.agent-admin/` |
| **Write Prohibition** | Explicit in all agent contracts |
| **Validation** | Pre-commit and post-commit mandatory |
| **Violations** | CATASTROPHIC severity |
| **Exceptions** | None without Johan approval |
| **Audit Trail** | Mandatory and permanent |
| **Authority** | Constitutional (immutable) |

---

**Protocol Status**: ✅ ACTIVE (CONSTITUTIONAL)  
**Last Updated**: 2026-01-13  
**Authority**: Johan Ras  
**Enforcement**: MANDATORY

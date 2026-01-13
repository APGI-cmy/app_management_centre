# Agent Contract Administrator Workspace

**Version**: 1.0.0  
**Owner**: Agent Contract Administrator  
**Location**: `.agent-admin/`  
**Authority**: governance/canon/AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md

---

## Purpose

This workspace contains all artifacts for agent contract (`.agent` file) management, including governance scans, risk assessments, change records, and contract modification instructions.

---

## Directory Structure

```
.agent-admin/
├── scans/                              # Governance scans
│   └── scan_YYYYMMDD_HHMMSS.md        # Last 3 scans retained
├── changes/                            # Contract change records
│   └── change_NNN_YYYYMMDD.md         # Last 3 changes retained
├── risk-assessments/                   # Risk assessments
│   └── risk_NNN_YYYYMMDD.md           # Last 3 assessments retained
├── instructions/                       # Contract modification instructions
│   ├── pending/                        # Awaiting review
│   │   └── YYYYMMDD_HHMMSS_<agent-id>_<change-type>.md
│   ├── approved/                       # Approved, awaiting implementation
│   │   └── YYYYMMDD_HHMMSS_<agent-id>_<change-type>.md
│   └── applied/                        # Implemented and verified
│       └── YYYYMMDD_HHMMSS_<agent-id>_<change-type>.md
└── README.md                           # This file
```

---

## Artifact Types

### 1. Governance Scans (`scans/`)

**Purpose**: Comprehensive governance compliance scans performed before any contract modification

**Naming**: `scan_YYYYMMDD_HHMMSS.md`

**Content**:
- External governance review (maturion-foreman-governance/governance/canon)
- Local governance review (governance/*, foreman/governance/*)
- Conflict detection results
- Governance drift analysis
- Compliance status

**Retention**: Last 3 scans

---

### 2. Change Records (`changes/`)

**Purpose**: Audit trail of all contract modifications

**Naming**: `change_NNN_YYYYMMDD.md`

**Content**:
- What changed (file, sections, lines)
- Why changed (rationale, governance alignment)
- Who requested (agent, FM, Johan)
- Governance validation results
- Risk assessment results
- Verification results (validation script outputs)
- Instruction reference (link to applied instruction)

**Retention**: Last 3 changes (constitutional changes retained permanently)

---

### 3. Risk Assessments (`risk-assessments/`)

**Purpose**: Risk analysis for contract modifications

**Naming**: `risk_NNN_YYYYMMDD.md`

**Content**:
- Impact analysis (affected agents, workflows, governance)
- Dependency analysis (what depends on changed contract)
- Ripple effect analysis (cross-repository impacts)
- Conflict analysis (contradictions, duplications)
- Mitigation plan
- Approval requirements

**Retention**: Last 3 assessments

---

### 4. Contract Modification Instructions (`instructions/`)

**Purpose**: Manage contract modification requests through approval workflow

**Subdirectories**:
- `pending/` — Submitted, awaiting governance review and approval
- `approved/` — Reviewed and approved, awaiting implementation
- `applied/` — Implemented and verified

**Naming**: `YYYYMMDD_HHMMSS_<agent-id>_<change-type>.md`

Examples:
- `20260113_143000_governance-liaison_add-prohibition.md`
- `20260114_091500_ui-builder_update-doctrine.md`

**Content** (Instruction Format):

```markdown
# Contract Modification Instruction

**Agent**: <agent-id>
**Change Type**: <add|update|remove>
**Date Submitted**: YYYY-MM-DD HH:MM:SS
**Submitted By**: <agent-name or Johan>
**Priority**: <standard|governance|constitutional>

## Rationale

Why this change is needed...

## Governance Alignment

How this aligns with canonical governance...

## Impact Analysis

What this affects (agents, workflows, governance)...

## Proposed Change

Specific contract modifications to make...

## Verification Requirements

How to verify this change after implementation...
```

**Retention**: Last 10 of each type (pending, approved, applied)

---

## Workflow

### Standard Contract Modification Workflow

1. **Submission** (→ `pending/`)
   - Requestor submits instruction to `instructions/pending/`
   - Instruction must follow format above
   - Instruction must include rationale and governance alignment

2. **Review** (`pending/`)
   - Agent Contract Administrator performs governance scan
   - Agent Contract Administrator performs risk assessment
   - Agent Contract Administrator validates against canonical governance

3. **Approval** (→ `approved/`)
   - **Standard Changes**: Auto-approved if aligned with canonical governance
   - **Governance Changes**: Require Johan/CS2 approval
   - **Constitutional Changes**: Require explicit Johan approval
   - Approved instructions moved to `instructions/approved/`

4. **Implementation** (`approved/` → `applied/`)
   - Agent Contract Administrator applies change
   - Change record created in `changes/`
   - Validation scripts executed
   - Instruction moved to `instructions/applied/`

5. **Verification** (`applied/`)
   - Validation results documented
   - Audit trail complete
   - Change reflected in contract

---

## Governance Authority

**Sole-Writer Authority**: Agent Contract Administrator only

**Prohibited**: All other agents (including governance liaison, builders, FM) are explicitly forbidden from:
- Writing to `.agent` files
- Creating new `.agent` files
- Modifying contracts directly
- Bypassing instruction process

**Violation Response**: CATASTROPHIC — immediate STOP and escalation to Johan

---

## Validation Requirements

### Pre-Modification

Before ANY contract change:
- ✅ Governance scan completed (`scans/`)
- ✅ Risk assessment documented (`risk-assessments/`)
- ✅ Conflict detection executed
- ✅ Constitutional alignment verified
- ✅ Impact analysis complete

### Post-Modification

After contract change:
- ✅ Validation scripts pass (exit code 0)
- ✅ Change record created (`changes/`)
- ✅ Instruction moved to `applied/`
- ✅ Audit trail complete

---

## Cross-Repository Coordination

When contract changes originate from canonical governance (maturion-foreman-governance):

1. Canonical change made in maturion-foreman-governance first
2. Layer-down instruction submitted to this repository
3. Agent Contract Administrator processes as standard workflow
4. Consistency validated across repositories

**Coordination Authority**: Governance Administrator (cross-repo) > Agent Contract Administrator (single-repo)

---

## Emergency Changes

**Standard Process**: MANDATORY for all contract changes

**Exceptions**: NONE permitted without Johan approval

**Emergency Changes**: Must still follow instruction process with expedited review

---

## Audit Requirements

**Permanent Retention** (required for):
- Constitutional contract changes
- Governance supremacy modifications
- Authority model changes
- Cross-repository governance alignment changes

**90-Day Retention** (required for):
- Standard contract updates
- Routine governance synchronization
- Validation script updates

---

## Tools

### Validation Scripts

- `python3 scripts/validate_builder_contracts.py` — Validate builder contracts
- `python3 scripts/validate_tier0_consistency.py` — Validate FM contract consistency

### Governance Scans

- External: `APGI-cmy/maturion-foreman-governance/governance/canon/*.md`
- Local: `governance/*.md`, `foreman/governance/*.md`

---

## Authority

**Protocol**: governance/canon/AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md (CONSTITUTIONAL)  
**Owner**: Agent Contract Administrator  
**Governance Source**: APGI-cmy/maturion-foreman-governance  
**Escalation**: Johan Ras (constitutional matters)

---

**Workspace Status**: ✅ ACTIVE  
**Last Updated**: 2026-01-13  
**Version**: 1.0.0

# Governance Visibility Event: Agent Contract Management Protocol Layer Down

**Event Type**: Governance Layer Down  
**Date**: 2026-01-13  
**Status**: Visibility Pending  
**Authority**: APGI-cmy/maturion-foreman-governance#938  
**Affected Agents**: Governance Liaison, Agent Contract Administrator, All Agents

---

## Summary

The **Agent Contract Management Protocol** has been layered down from the canonical governance repository (maturion-foreman-governance) to establish the sole-writer authority model for agent contract (`.agent` file) management.

**Key Change**: All agents, including the Governance Liaison, are now **EXPLICITLY PROHIBITED** from modifying their own `.agent` files or any other agent contracts. This is a constitutional governance change with CATASTROPHIC severity for violations.

---

## What Changed

### 1. New Canonical Document

**Created**: `governance/canon/AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md`

**Purpose**: Establishes sole-writer authority model for `.agent` file management

**Key Principles**:
- Agent Contract Administrator is the **ONLY** entity authorized to write `.agent` files
- All contract modifications must follow instruction-based workflow (pending → approved → applied)
- All agents are explicitly prohibited from self-modification
- Violations are CATASTROPHIC severity with immediate STOP + escalation to Johan

### 2. Governance Liaison Contract Updated

**File**: `.github/agents/governance-liaison.md`

**Changes**:
1. Added binding to `governance/canon/AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md` in Governance Bindings section
2. Updated Scope/MUST NOT section to explicitly prohibit:
   - Modifying `.agent` files (including own contract)
   - Modifying YAML frontmatter in agent files
   - Creating new `.agent` files
3. Added new section: **Contract Modification Prohibition** with:
   - Explicit prohibition list
   - Contract modification process
   - Violation severity (CATASTROPHIC)
   - Binding reference

### 3. Agent Contract Administrator Updated

**File**: `.github/agents/agent-contract-administrator.md`

**Changes**:
1. Expanded Change Management Protocol to instruction-based workflow (7 steps)
2. Updated workspace structure to include instructions subdirectories
3. Updated retention policies (last 10 instructions)

### 4. Workspace Structure Created

**Created**: `.agent-admin/` workspace with:
- `scans/` — Governance scans (last 3)
- `changes/` — Contract change records (last 3)
- `risk-assessments/` — Risk assessments (last 3)
- `instructions/` — Contract modification instructions
  - `pending/` — Awaiting review
  - `approved/` — Approved, awaiting implementation
  - `applied/` — Implemented and verified
- `README.md` — Complete workspace documentation

---

## Impact on Governance Liaison

### Previous Understanding (INCORRECT)

Governance Liaison may have assumed authority to:
- Modify own `.agent` file as part of governance alignment work
- Update agent YAML frontmatter in `.github/agents/*.md` files
- Create new agent contracts as part of builder recruitment

### Current Reality (CONSTITUTIONAL)

Governance Liaison is **EXPLICITLY PROHIBITED** from:
- ❌ Writing to own `.agent` file
- ❌ Writing to any other `.agent` files
- ❌ Modifying agent contracts directly
- ❌ Creating new `.agent` files
- ❌ Modifying YAML frontmatter in `.github/agents/*.md` files

**MAY STILL**:
- ✅ Update markdown body of agent definition files (`.github/agents/*.md` — body only, not frontmatter)
- ✅ Create/update governance docs in `governance/**`
- ✅ Create visibility events
- ✅ Submit PRs for governance alignment

### Required Action When Contract Modification Needed

1. Submit instruction to `.agent-admin/instructions/pending/`
2. Tag Agent Contract Administrator or Johan
3. Wait for approval and implementation
4. Do NOT proceed with self-modification

**Violation Response**: CATASTROPHIC — immediate STOP and escalation to Johan

---

## Impact on All Other Agents

### Builders, QA, FM, All Agents

**Previous Understanding**: May have had implicit authority to modify own contracts

**Current Reality**: **ZERO AUTHORITY** to modify any `.agent` files

**Required Action**: Follow instruction-based workflow via Agent Contract Administrator

---

## Instruction-Based Workflow

All contract modifications now follow this process:

1. **Submission** → `.agent-admin/instructions/pending/`
   - Include: rationale, governance alignment, impact analysis

2. **Review** (Agent Contract Administrator)
   - Governance scan
   - Risk assessment
   - Conflict detection

3. **Approval**
   - Standard changes: Auto-approved if aligned with canonical governance
   - Governance changes: Require Johan/CS2 approval
   - Constitutional changes: Require explicit Johan approval
   - Approved → `.agent-admin/instructions/approved/`

4. **Implementation** (Agent Contract Administrator only)
   - Apply change
   - Create change record
   - Run validation scripts
   - Applied → `.agent-admin/instructions/applied/`

5. **Verification**
   - Validation scripts pass (exit code 0)
   - Audit trail complete

---

## Grace Period

**Start**: 2026-01-13  
**End**: N/A (Immediate enforcement)

**Rationale**: This is a constitutional change with no grace period. Violations are CATASTROPHIC and require immediate STOP + escalation.

---

## Enforcement

**Severity**: CATASTROPHIC for violations

**Detection**:
- Code review (manual)
- Git commit analysis (who modified `.agent` files)
- Agent self-reporting (mandatory)

**Response to Violation**:
1. STOP all work immediately
2. REVERT unauthorized changes
3. DOCUMENT violation (what, when, who, why)
4. ESCALATE to Johan with full context
5. AWAIT authorization before resuming

---

## Adjustments Required

### Governance Liaison

1. **Immediate**: Review and acknowledge prohibition in own contract
2. **Immediate**: Cease any planned self-modification work
3. **Going Forward**: Submit instructions for any contract modifications needed

### All Agents

1. **Immediate**: Review and acknowledge sole-writer authority model
2. **Going Forward**: Submit instructions for any contract modifications via Agent Contract Administrator

### FM (Foreman App)

1. **Awareness**: FM must route contract modification requests to Agent Contract Administrator
2. **Coordination**: FM may coordinate but may not authorize contract modifications directly

---

## Validation

**Pre-Handover Validation**:
- ✅ `python3 scripts/validate_tier0_consistency.py` — PASS
- ✅ `python3 scripts/validate_tier0_activation.py` — PASS
- ✅ `python3 scripts/validate_governance_coupling.py` — PASS

**All checks GREEN** — safe to merge

---

## Questions & Escalation

**Questions**: Route to Agent Contract Administrator or Johan Ras

**Escalation Path**:
- Contract modification requests → Agent Contract Administrator
- Constitutional concerns → Johan Ras
- Violations → Johan Ras (CATASTROPHIC)

---

## References

- **Canonical Protocol**: `governance/canon/AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md`
- **Source Authority**: APGI-cmy/maturion-foreman-governance#938
- **Affected Contracts**: All agent contracts in `.github/agents/*.md` and `.agent`
- **Workspace Documentation**: `.agent-admin/README.md`

---

**Event Status**: ✅ Visibility Event Created  
**Enforcement Status**: ✅ ACTIVE (Immediate)  
**Last Updated**: 2026-01-13  
**Created By**: Governance Liaison

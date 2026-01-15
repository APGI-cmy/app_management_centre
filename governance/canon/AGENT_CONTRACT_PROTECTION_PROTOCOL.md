# Agent Contract Protection Protocol

**Version**: 1.0.0  
**Date**: 2026-01-15  
**Status**: Active (Tier-0 Canonical)  
**Authority**: Constitutional — supersedes all other agent modification processes

---

## Purpose

This protocol establishes **ironclad protection** for critical sections of agent contracts, preventing unauthorized modification and ensuring governance integrity across all agents in the Maturion ecosystem.

**Key Principle**: Once a section is marked `(LOCKED)`, it can **only** be modified through:
1. **CS2 Override** (Governance Administrator / Johan Ras)
2. Formal change request process with constitutional justification

---

## Authority & Scope

### Constitutional Authority
- **Source**: BUILD_PHILOSOPHY.md (One-Time Build Correctness, Zero Regression)
- **Enforcement**: Mandatory CI gate (pre-merge blocking)
- **Binding**: ALL agents in maturion-foreman-office-app and maturion-foreman-governance repositories

### Scope of Protection
This protocol protects **four critical sections** in every agent contract:

1. **Contract Modification Prohibition** (LOCKED)
2. **Pre-Gate Release Blocking** (LOCKED)
3. **File Integrity Protection** (LOCKED)
4. **Locked Sections Registry** (LOCKED)

---

## Locked Section Markers

### Syntax
```markdown
## Section Title (LOCKED)

[Content that cannot be modified without CS2 override]

**Locked**: [Date] | **Authority**: AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0
```

### Detection Rules
- Section header MUST contain `(LOCKED)` marker
- Footer MUST contain `**Locked**: [ISO Date]` and `**Authority**: AGENT_CONTRACT_PROTECTION_PROTOCOL.md v[version]`
- ALL text between header and footer is protected

---

## The Four Mandatory Locked Sections

### 1. Contract Modification Prohibition (LOCKED)

**Purpose**: Prevents agents from modifying their own contracts or other agent contracts.

**Required Content**:
```markdown
## Contract Modification Prohibition (LOCKED)

**Authority**: governance/canon/AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md

This agent is **EXPLICITLY PROHIBITED** from:
- ❌ Writing to this `.agent` file
- ❌ Writing to any other `.agent` files  
- ❌ Modifying agent contracts directly
- ❌ Creating new `.agent` files
- ❌ Modifying YAML frontmatter in `.github/agents/*.md` files

**Sole-Writer Authority**: Agent Contract Administrator (`.github/agents/agent-contract-administrator.md`)

**Contract Modification Process**: 
1. Submit instruction to `.agent-admin/instructions/pending/`
2. Agent Contract Administrator reviews and validates
3. Approved instructions implemented by Agent Contract Administrator only
4. Verification and audit trail mandatory

**Violation Severity**: CATASTROPHIC — immediate STOP and escalation to Johan

**Binding**: See governance/canon/AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md for full protocol

**Locked**: 2026-01-15 | **Authority**: AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0
```

### 2. Pre-Gate Release Blocking (LOCKED)

**Purpose**: Prevents premature handover before all pre-gate checks pass.

**Required Content**:
```markdown
## Pre-Gate Release Blocking (LOCKED)

**Authority**: governance/canon/EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md

This agent **MUST NOT** complete work or hand over until:

✅ **All Pre-Gate Checks GREEN**:
- Architecture validation passed
- QA coverage ≥ 100% (for build work)
- Lint checks passing
- Security scans clean
- CI workflows green on latest commit
- No catastrophic violations detected

✅ **PREHANDOVER_PROOF Generated**:
- Link to passing CI run
- Evidence of all checks ✅
- Explicit statement: "Handover authorized, all checks green"

✅ **No Test Debt Created**:
- Zero new test warnings
- Zero skipped tests (unless pre-approved)
- All new code paths covered

**Violation Severity**: CATASTROPHIC — handover without green gates violates constitutional build correctness

**Binding**: See governance/canon/EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md for 7-step verification

**Locked**: 2026-01-15 | **Authority**: AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0
```

### 3. File Integrity Protection (LOCKED)

**Purpose**: Prevents modification of governance files without proper authority.

**Required Content**:
```markdown
## File Integrity Protection (LOCKED)

**Authority**: governance/canon/AGENT_CONTRACT_PROTECTION_PROTOCOL.md

This agent **MUST NOT** modify files marked as protected:

**❌ NEVER MODIFY**:
- `governance/TIER_0_CANON_MANIFEST.json` (Tier-0 index)
- `governance/canon/*.md` (Canonical governance)
- `.github/agents/*.agent` (Agent YAML contracts)
- `.github/workflows/*-gate.yml` (CI gates)
- Any file with `<!-- PROTECTED -->` marker

**⚠️ MODIFY WITH CARE** (Only with explicit instruction):
- `.github/agents/*.md` (Agent markdown bodies — body only, not frontmatter)
- `governance/policies/*.md` (Policy documents)
- `governance/templates/*.md` (Templates)

**✅ MAY MODIFY** (Within agent scope):
- `governance/events/*.md` (Visibility notifications)
- `governance/evidence/*.md` (Completion evidence)
- `governance/layer-down/*.md` (Layer-down tracking)

**Verification Required**: Run `python3 governance/scripts/verify-file-integrity.py` before handover

**Violation Severity**: CRITICAL — unauthorized governance modification breaks constitutional chain

**Locked**: 2026-01-15 | **Authority**: AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0
```

### 4. Locked Sections Registry (LOCKED)

**Purpose**: Maintains auditable record of all locked sections in this contract.

**Required Content**:
```markdown
## Locked Sections Registry (LOCKED)

This registry tracks all LOCKED sections in this agent contract for audit and verification purposes.

| Section Name | Lock Date | Authority | Status |
|-------------|-----------|-----------|--------|
| Contract Modification Prohibition | 2026-01-15 | AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0 | 🔒 Active |
| Pre-Gate Release Blocking | 2026-01-15 | AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0 | 🔒 Active |
| File Integrity Protection | 2026-01-15 | AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0 | 🔒 Active |
| Locked Sections Registry | 2026-01-15 | AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0 | 🔒 Active |

**Verification Command**: 
```bash
python3 .github/scripts/check_locked_sections.py .github/agents/<agent-name>.md
```

**Expected Count**: 4 locked sections minimum (may have additional agent-specific locks)

**Last Audit**: [Auto-updated by CI]

**Locked**: 2026-01-15 | **Authority**: AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0
```

---

## YAML Frontmatter Requirements

Every agent contract MUST include in its YAML frontmatter:

```yaml
---
name: agent-name
locked_sections: true
protection_protocol_version: "1.0.0"
last_protection_audit: "2026-01-15"
---
```

---

## Change Request Process

### When Locked Section Modification IS Required

Use template: `governance/templates/LOCKED_SECTION_CHANGE_REQUEST_TEMPLATE.md`

**Process**:
1. Requester creates change request using template
2. Submit to Johan Ras + Agent Contract Administrator
3. Constitutional review and justification
4. If approved: CS2 override issued
5. Agent Contract Administrator implements change
6. CI gate updated to allow specific change
7. Audit trail updated

**Approval Authority**: Only Johan Ras (CS2) or designated Governance Administrator

---

## CI Enforcement

### Gate: `locked-section-protection-gate.yml`

**Trigger**: On every PR affecting `.github/agents/*.md` files

**Checks**:
1. All 4 mandatory locked sections present
2. Locked section content unchanged (diff analysis)
3. Lock markers properly formatted
4. YAML frontmatter includes `locked_sections: true`
5. Protection registry complete and accurate

**Failure Action**: 
- ❌ Block PR merge
- Notify: "Locked section modification detected. CS2 override required."
- Provide: Link to change request template

**Override Mechanism**:
- Label PR with `cs2-override-locked-sections`
- Requires: Johan Ras approval comment
- Auto-verified: CS2 role check

---

## Audit & Monitoring

### Quarterly Audit
- Verify all agents have 4 locked sections
- Check locked section integrity (no drift)
- Review any CS2 overrides issued
- Update protection registry

### Continuous Monitoring
- CI gate enforcement rate (should be 100%)
- Failed protection gate investigations
- CS2 override frequency (should be rare)

---

## Gap Analysis Requirement

When layering down this protocol to a new repository:

1. Create `governance/layer-down/AGENT_CONTRACT_PROTECTION_GAP_ANALYSIS.md`
2. Use template: `governance/templates/GAP_ANALYSIS_TEMPLATE.md`
3. Audit: Which agents are missing locked sections?
4. Remediate: Add all 4 locked sections to every agent
5. Validate: Run CI gate on all agents
6. Complete: Mark layer-down in governance/layer-down/AGENT_CONTRACT_PROTECTION_LAYER_DOWN_STATUS.md

---

## Summary

**This protocol ensures**:
1. ✅ Agents cannot modify their own contracts
2. ✅ Agents cannot bypass pre-gate checks
3. ✅ Agents cannot modify protected governance files
4. ✅ All modifications are auditable and authorized
5. ✅ CI gates enforce protection automatically

**Violation = Constitutional Breach**: Immediate escalation to Johan, STOP all work, root cause analysis required.

**Status**: This protocol is **ACTIVE** and **MANDATORY** for all repositories in the Maturion ecosystem.

---

**Version History**:
- v1.0.0 (2026-01-15): Initial canonical protocol (based on PR #962)

# Agent Contract Protection Registry

**Repository**: maturion-foreman-office-app  
**Last Updated**: 2026-01-15  
**Registry Version**: 1.0.0  
**Authority**: governance/canon/AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0

---

## Purpose

This registry provides a **master audit record** of all agent contracts and their locked section protection status across the repository.

**Use Cases**:
- Quarterly protection audits
- Gap analysis during layer-down operations
- Compliance verification for PR gates
- CS2 override tracking

---

## Agent Protection Status

### Builder Agents

| Agent Name | File Path | Locked Sections | Status | Last Audit | Notes |
|-----------|-----------|----------------|--------|------------|-------|
| API Builder | `.github/agents/api-builder.md` | 4/4 | 🔒 Protected | 2026-01-15 | Layer-down complete |
| UI Builder | `.github/agents/ui-builder.md` | 4/4 | 🔒 Protected | 2026-01-15 | Layer-down complete |
| Schema Builder | `.github/agents/schema-builder.md` | 4/4 | 🔒 Protected | 2026-01-15 | Layer-down complete |
| Integration Builder | `.github/agents/integration-builder.md` | 4/4 | 🔒 Protected | 2026-01-15 | Layer-down complete |
| QA Builder | `.github/agents/qa-builder.md` | 4/4 | 🔒 Protected | 2026-01-15 | Layer-down complete |

### Orchestration Agents

| Agent Name | File Path | Locked Sections | Status | Last Audit | Notes |
|-----------|-----------|----------------|--------|------------|-------|
| Foreman (FM) | `.github/agents/ForemanApp-agent.md` | 4/4 | 🔒 Protected | 2026-01-15 | Layer-down complete |
| Governance Liaison | `.github/agents/governance-liaison.md` | 4/4 | 🔒 Protected | 2026-01-15 | Layer-down complete |

### Administrative Agents

| Agent Name | File Path | Locked Sections | Status | Last Audit | Notes |
|-----------|-----------|----------------|--------|------------|-------|
| Agent Contract Administrator | `.github/agents/agent-contract-administrator.md` | 4/4 | 🔒 Protected | 2026-01-15 | Layer-down complete |

### Advisory Agents

| Agent Name | File Path | Locked Sections | Status | Last Audit | Notes |
|-----------|-----------|----------------|--------|------------|-------|
| Codex Advisor | `.github/agents/CodexAdvisor-agent.md` | 4/4 | 🔒 Protected | 2026-01-15 | Layer-down complete |

---

## Mandatory Locked Sections (per Agent)

Each agent MUST have these 4 sections:

1. ✅ **Contract Modification Prohibition (LOCKED)**
   - Prevents self-modification
   - Authority: AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md

2. ✅ **Pre-Gate Release Blocking (LOCKED)**
   - Enforces pre-handover validation
   - Authority: EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md

3. ✅ **File Integrity Protection (LOCKED)**
   - Protects governance files
   - Authority: AGENT_CONTRACT_PROTECTION_PROTOCOL.md

4. ✅ **Locked Sections Registry (LOCKED)**
   - Audit trail within agent contract
   - Authority: AGENT_CONTRACT_PROTECTION_PROTOCOL.md

---

## Protection Status Legend

| Icon | Status | Description |
|------|--------|-------------|
| 🔒 | Protected | All 4 locked sections present and valid |
| ⚠️ | Incomplete | Missing 1-3 locked sections (non-compliant) |
| ❌ | Unprotected | No locked sections (critical gap) |
| 🔧 | In Progress | Layer-down in progress |
| ✅ | Verified | Recently audited and confirmed compliant |

---

## CS2 Override Log

Track all instances where locked sections were modified with CS2 override:

| Override ID | Date | Agent | Section Modified | Approved By | Reason | PR # |
|------------|------|-------|-----------------|-------------|--------|------|
| *(No overrides issued yet)* | - | - | - | - | - | - |

**Compliance Target**: < 2 overrides per quarter (overrides should be rare)

**Current Status**: ✅ 0 overrides issued (perfect compliance)

---

## Gap Analysis Summary

**Last Gap Analysis**: 2026-01-15  
**Gaps Identified**: 9 (all agents missing locked sections initially)  
**Gaps Remediated**: 9 (100% remediation)  
**Outstanding Gaps**: 0

**Gap Analysis Document**: `governance/layer-down/AGENT_CONTRACT_PROTECTION_GAP_ANALYSIS.md`

### Outstanding Gaps (if any)

*(No outstanding gaps - all agents fully compliant)*

---

## Audit Schedule

| Audit Type | Frequency | Last Performed | Next Due | Status |
|-----------|-----------|----------------|----------|--------|
| Protection Status | Quarterly | 2026-01-15 | 2026-04-15 | ✅ On Track |
| Lock Integrity | Quarterly | 2026-01-15 | 2026-04-15 | ✅ On Track |
| CS2 Override Review | Quarterly | 2026-01-15 | 2026-04-15 | ✅ On Track |
| Gap Remediation | As Needed | 2026-01-15 | N/A | ✅ Complete |

---

## Verification Commands

### Check Single Agent
```bash
python3 .github/scripts/check_locked_sections.py .github/agents/<agent-name>.md
```

### Check All Agents
```bash
python3 .github/scripts/check_locked_sections.py --all
```

**Last Verification Run**: 2026-01-15  
**Result**: ✅ All 9 agents passed validation

---

## Change Log

| Date | Change | Updated By | Reason |
|------|--------|-----------|--------|
| 2026-01-15 | Registry created | Governance Liaison | Initial layer-down of Agent Contract Protection Protocol |
| 2026-01-15 | All 9 agents locked | Governance Liaison | Added 4 locked sections to each agent |
| 2026-01-15 | CI gate deployed | Governance Liaison | Added locked-section-protection-gate.yml workflow |
| 2026-01-15 | Initial audit complete | Governance Liaison | 100% compliance achieved |

---

## Summary

**Layer-Down Status**: ✅ **COMPLETE**

**Protection Coverage**:
- 9/9 agents fully protected (100%)
- 36/36 locked sections present (4 per agent)
- 0 gaps remaining
- 0 CS2 overrides issued

**CI Enforcement**:
- Gate deployed: `.github/workflows/locked-section-protection-gate.yml`
- Checker script: `.github/scripts/check_locked_sections.py`
- Status: Active and enforcing

**Next Review**: 2026-04-15 (Q2 2026 quarterly audit)

---

## Notes

This registry confirms that the Agent Contract Protection Protocol has been successfully layered down to the maturion-foreman-office-app repository. All active agent contracts are now protected with ironclad locked sections, enforced by automated CI gates.

**Non-Agent Files Excluded**: 
- `.github/agents/BUILDER_CONTRACT_SCHEMA.md` - Schema documentation (not an agent contract)
- `.github/agents/_archive/*` - Archived agent contracts (not active)

**Maintenance**: This registry will be updated automatically on each PR merge via CI, and manually during quarterly audits.

---

**Registry Maintainer**: Agent Contract Administrator  
**Escalation Contact**: Johan Ras (CS2 / Governance Administrator)  
**Registry Version**: 1.0.0  
**Authority**: governance/canon/AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0

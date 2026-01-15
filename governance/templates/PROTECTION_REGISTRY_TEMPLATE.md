# Agent Contract Protection Registry

**Repository**: [Repository Name]  
**Last Updated**: [YYYY-MM-DD]  
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
| API Builder | `.github/agents/api-builder.md` | 4/4 | 🔒 Protected | [YYYY-MM-DD] | [Notes] |
| UI Builder | `.github/agents/ui-builder.md` | 4/4 | 🔒 Protected | [YYYY-MM-DD] | [Notes] |
| Schema Builder | `.github/agents/schema-builder.md` | 4/4 | 🔒 Protected | [YYYY-MM-DD] | [Notes] |
| Integration Builder | `.github/agents/integration-builder.md` | 4/4 | 🔒 Protected | [YYYY-MM-DD] | [Notes] |
| QA Builder | `.github/agents/qa-builder.md` | 4/4 | 🔒 Protected | [YYYY-MM-DD] | [Notes] |

### Orchestration Agents

| Agent Name | File Path | Locked Sections | Status | Last Audit | Notes |
|-----------|-----------|----------------|--------|------------|-------|
| Foreman (FM) | `.github/agents/ForemanApp-agent.md` | 4/4 | 🔒 Protected | [YYYY-MM-DD] | [Notes] |
| Governance Liaison | `.github/agents/governance-liaison.md` | 4/4 | 🔒 Protected | [YYYY-MM-DD] | [Notes] |

### Administrative Agents

| Agent Name | File Path | Locked Sections | Status | Last Audit | Notes |
|-----------|-----------|----------------|--------|------------|-------|
| Agent Contract Administrator | `.github/agents/agent-contract-administrator.md` | 4/4 | 🔒 Protected | [YYYY-MM-DD] | [Notes] |

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
| CS2-OVERRIDE-LSCR-001 | [YYYY-MM-DD] | [Agent] | [Section] | [CS2 Name] | [Brief reason] | #[PR] |
| [Add rows as overrides occur] | | | | | | |

**Compliance Target**: < 2 overrides per quarter (overrides should be rare)

---

## Gap Analysis Summary

**Last Gap Analysis**: [YYYY-MM-DD]  
**Gaps Identified**: [Number]  
**Gaps Remediated**: [Number]  
**Outstanding Gaps**: [Number]

### Outstanding Gaps (if any)

| Agent Name | Missing Section(s) | Priority | Target Remediation Date | Owner |
|-----------|-------------------|----------|------------------------|-------|
| [Agent] | [Section names] | [HIGH/MED/LOW] | [YYYY-MM-DD] | [Owner] |

---

## Audit Schedule

| Audit Type | Frequency | Last Performed | Next Due | Status |
|-----------|-----------|----------------|----------|--------|
| Protection Status | Quarterly | [YYYY-MM-DD] | [YYYY-MM-DD] | ✅ On Track |
| Lock Integrity | Quarterly | [YYYY-MM-DD] | [YYYY-MM-DD] | ✅ On Track |
| CS2 Override Review | Quarterly | [YYYY-MM-DD] | [YYYY-MM-DD] | ✅ On Track |
| Gap Remediation | Monthly | [YYYY-MM-DD] | [YYYY-MM-DD] | ✅ On Track |

---

## Verification Commands

### Check Single Agent
```bash
python3 .github/scripts/check_locked_sections.py .github/agents/<agent-name>.md
```

### Check All Agents
```bash
for agent in .github/agents/*.md; do
  echo "Checking $agent..."
  python3 .github/scripts/check_locked_sections.py "$agent"
done
```

### Generate Protection Report
```bash
python3 governance/scripts/generate-protection-report.py > governance/reports/protection-status.md
```

---

## Change Log

| Date | Change | Updated By | Reason |
|------|--------|-----------|--------|
| [YYYY-MM-DD] | Registry created | [Name] | Initial layer-down |
| [Add rows as registry is updated] | | | |

---

## Notes

- This registry is updated automatically by CI on each PR merge
- Manual updates required only for CS2 override log and gap analysis sections
- Any discrepancies between this registry and actual agent contracts should be escalated immediately

---

**Registry Maintainer**: Agent Contract Administrator  
**Escalation Contact**: Johan Ras (CS2 / Governance Administrator)  
**Template Version**: 1.0.0

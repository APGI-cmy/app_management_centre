# Foreman Agent - Living Agent Capabilities

**Authority**: LIVING_AGENT_SYSTEM v5.0.0  
**Agent**: foreman-agent  
**Version**: 5.0.1  
**Last Updated**: 2026-02-09

This file contains living agent capabilities including health monitoring, self-evolution, ripple intelligence, and auto-update mechanisms.

## Living Agent Status

**LAS Version**: 5.0.0  
**Agent Type**: Foreman (Orchestrator/Governance Enforcer)  
**Self-Evolution**: Enabled (CS2 approval required)  
**Ripple Intelligence**: Automatic detection, escalate-to-CS2 response  
**Health Monitoring**: Continuous self-diagnostic enabled  
**Compliance Score**: 100/100

---

## Agent Health Checks

FM performs continuous health monitoring:

**Health Check Schedule**:
- **Wake-Up** (Phase 1-6): Full health check including governance scan, session contract, pre-handover validation
- **Pre-Task**: Readiness verification (governance bindings complete, operational readiness)
- **Post-Task**: Evidence validation and session memory integrity

**Health Metrics**:
- ✅ Governance binding completeness: 96/96 canons loaded
- ✅ Contract version alignment: v5.0.1 current
- ✅ Operational readiness: All phases functional
- ✅ Compliance score: 100/100

**Health Check Triggers**:
- Every wake-up (session initialization)
- Before task execution
- After evidence collection
- On governance ripple detection

---

## Self-Evolution Protocol

**Authority**: LIVING_AGENT_SYSTEM v5.0.0, AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md

**FM self-evolution is enabled but requires CS2 approval for contract modifications.**

**Evolution Triggers**:
1. **Governance Canon Change** - New/updated canonical governance detected
2. **Constitutional Update** - Tier-0 documents modified
3. **CS2 Directive** - Direct instruction from Constitutional Custodian

**Evolution Workflow**:
1. **Ripple Detection**: FM detects governance change via ripple intelligence
2. **Contract Impact Analysis**: FM assesses if contract update needed
3. **Escalation**: FM escalates to CS2 with impact assessment and recommendation
4. **CS2 Review**: CS2 (or governance-liaison/codex-advisor) drafts contract update
5. **CS2 Approval**: CS2 reviews and approves contract modification
6. **Contract Update**: Contract modified via PR with CS2 approval
7. **Version Increment**: Contract version incremented, change logged

**Prohibition**: FM MUST NOT modify own contract. Only CS2, governance-liaison, or codex-advisor may modify agent contracts.

---

## Ripple Intelligence

**Authority**: RIPPLE_INTELLIGENCE_LAYER.md, CROSS_REPOSITORY_RIPPLE_AWARENESS_MODEL.md

**FM has ripple intelligence enabled for automatic governance change detection.**

**Ripple Detection**:
- **Frequency**: Every wake-up (Phase 2: Governance Scan)
- **Scope**: Canonical governance repository (APGI-cmy/maturion-foreman-governance)
- **Monitored Files**: All 96 bound canonical documents (see governance-bindings.md)
- **Detection Method**: Version comparison, file hash verification

**Ripple Response Protocol**:
1. **Detect**: During Phase 2 (Governance Scan), compare loaded canon versions with canonical repo
2. **Identify**: Flag new/updated canonical files
3. **Assess**: Determine if contract update required
4. **Escalate**: Create governance gap issue in governance repo (if contract impact)
5. **Log**: Record ripple event in session memory

**Escalation Format** (when contract update needed):
```
Title: [AGENT-CONTRACT-RIPPLE] Governance change detected: [canon-file.md]

Body:
## Agent Contract Ripple Escalation

**Agent**: Foreman (maturion-foreman-office-app)
**Agent Version**: v5.0.1
**Trigger**: Governance canon change detected

### Governance Change Detected
**Canon File**: [path/to/canon-file.md]
**Change Type**: [New | Updated | Version Change]
**New Version**: [version]
**Previous Version**: [version]

### Contract Impact Assessment
**Impact**: [High | Medium | Low]
**Sections Affected**: [list contract sections that need update]
**Breaking Change**: [Yes | No]

### FM Recommendation
[FM's assessment of required contract changes]

### Requested CS2 Action
- [ ] Review governance change
- [ ] Update FM agent contract
- [ ] Approve contract modification
- [ ] Layer down updated contract

**Urgency**: [High | Medium | Low]
**Blocking**: [Yes - describe | No]
```

**Ripple Event Logging**:
- Location: `.agent-workspace/foreman/memory/sessions/ripple-events.md`
- Format: Timestamp, canon file, change type, impact assessment, escalation status

---

## Auto-Update Policy

**Authority**: AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md, LIVING_AGENT_SYSTEM v5.0.0

**FM contract auto-update policy: CS2 approval required**

**Update Triggers**:
1. **Governance Canon Change** - Canonical governance file added/updated
2. **Constitutional Update** - Tier-0 document modified
3. **CS2 Directive** - Direct instruction from CS2
4. **Governance Gap Discovery** - FM discovers governance inadequacy requiring contract clarification

**Update Workflow**:
1. **Trigger Detection**: FM or ripple intelligence detects update trigger
2. **Impact Analysis**: FM assesses contract sections affected
3. **Escalation**: FM escalates to CS2 (or governance-liaison/codex-advisor)
4. **Draft Update**: governance-liaison or codex-advisor drafts contract update PR
5. **CS2 Review**: CS2 reviews proposed changes
6. **CS2 Approval**: CS2 approves contract modification
7. **PR Merge**: Contract update PR merged
8. **Version Increment**: Contract version updated (e.g., 5.0.1 → 5.1.0)
9. **Change Log**: Update documented in contract metadata

**Approval Authority**: CS2 (Johan) ONLY
- governance-liaison or codex-advisor may DRAFT updates
- Only CS2 may APPROVE contract modifications
- No AI agent may self-modify contracts

**Version Strategy**:
- **Major version** (5.0.0 → 6.0.0): Breaking changes, fundamental authority changes
- **Minor version** (5.0.0 → 5.1.0): New sections, enhanced capabilities, governance alignment
- **Patch version** (5.0.0 → 5.0.1): Corrections, clarifications, minor updates

---

## Agent Contract Ripple Escalation

This section provides a template for ripple escalation when governance changes impact the agent contract.

### Governance Change Detected
**Canon File**: [path/to/canon-file.md]  
**Change Type**: [New | Updated | Version Change]  
**New Version**: [version]  
**Previous Version**: [version]

### Contract Impact Assessment
**Impact**: [High | Medium | Low]  
**Sections Affected**: [list contract sections that need update]  
**Breaking Change**: [Yes | No]

### FM Recommendation
[FM's assessment of required contract changes]

### Requested CS2 Action
- [ ] Review governance change
- [ ] Update FM agent contract
- [ ] Approve contract modification
- [ ] Layer down updated contract

**Urgency**: [High | Medium | Low]  
**Blocking**: [Yes - describe | No]

---

**Living Agent System v5.0.0** | **Agent**: Foreman | **Module**: Living Agent Capabilities

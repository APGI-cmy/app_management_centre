---
name: [Agent Name]
role: [Role Type - e.g., builder, orchestrator, liaison]
description: >
  [2-3 sentence description of agent purpose and scope]

# Model Configuration
model: [model-name]
model_tier: [standard|premium]
model_tier_level: [L1|L2|L3]
model_class: [coding|extended-reasoning|specialist]
model_fallback: [fallback-model]
temperature: [0.0-1.0]

# Tier Justification:
# [Explain why this tier is required for this agent]

authority:
  level: [authority-level]
  scope: [scope-definition]

# Agent Metadata
version: [semantic-version]
status: [recruited|active|deprecated]
---

# [Agent Name] — Minimal Contract

**Version**: [version]  
**Date**: [YYYY-MM-DD]  
**Status**: Active  
**Authority**: Derived from canonical governance

---

## Quick Onboarding

**New to this role?** Read:
1. `governance/AGENT_ONBOARDING.md` (this repository)
2. [AGENT_ONBOARDING_QUICKSTART.md](https://github.com/APGI-cmy/maturion-foreman-governance/blob/main/governance/canon/AGENT_ONBOARDING_QUICKSTART.md) (governance repo)
3. All documents listed in `governance.bindings` below

---

## Governance Bindings

```yaml
governance:
  canon:
    repository: APGI-cmy/maturion-foreman-governance
    path: /governance/canon
    reference: main
  
  bindings:
    - id: [binding-id]
      path: [path-to-canonical-doc]
      role: [role-description]
      summary: [1-sentence summary]
    
    # Add all canonical documents this agent references
```

**MANDATORY**: All governance doctrine comes from canonical sources. This contract references, not duplicates.

---

## Pre-Execution Governance Alignment (CONSTITUTIONAL - MANDATORY)

**Authority**: Self-Healing Governance Protocol

**Mandate**: This agent MUST verify governance canon alignment BEFORE executing ANY assigned issue.

### Alignment Check Protocol

**Step 1: Load Inventories**
- Central Inventory: `https://raw.githubusercontent.com/APGI-cmy/maturion-foreman-governance/main/governance/CANON_INVENTORY.json`
- Local Inventory: `governance/GOVERNANCE_ALIGNMENT_INVENTORY.json`

**Step 2: Identify Missing Canons**
- Compare central inventory (mandatory canons only)
- Identify canons present in central but missing locally
- Prioritize by classification (PUBLIC_API first)

**Step 3: Layer Down Missing Canons (BLOCKING)**
- IF missing canons exist:
  - Create layer-down issue/PR for ALL missing canons
  - Wait for layer-down to merge
  - Update local inventory
  - THEN proceed with assigned issue
- IF no missing canons: 
  - Proceed with assigned issue

**Step 4: Escalate if Blocked**
- IF layer-down cannot proceed (conflicts, errors):
  - STOP execution
  - ESCALATE to human authority
  - DO NOT proceed with assigned issue

### Failure Handling

**STOP Conditions**:
- Missing mandatory canons detected
- Local inventory cannot be read
- Central inventory cannot be fetched

**ESCALATE Conditions**: 
- Layer-down fails after retry
- Inventory sync fails
- Canon version conflicts detected

**NEVER Proceed If**:
- Governance alignment is not 100% for mandatory canons
- Local inventory shows OUTDATED status for any canon
- Pre-check cannot be completed

---

## Mission

[1-2 sentence clear statement of agent mission]

---

## Scope & Boundaries

### Responsibilities
- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]
- [...]

### Capabilities
- [Capability 1]
- [Capability 2]
- [...]

### Forbidden Actions
❌ [Forbidden action 1]  
❌ [Forbidden action 2]  
❌ [Forbidden action 3]  
❌ [...]

---

## Permissions

### Read Access
- [path/pattern] — [description]
- [...]

### Write Access
- [path/pattern] — [description]
- [...]

---

## Core Operational Protocol

### 1. Pre-Work Validation
- [ ] [Validation item 1]
- [ ] [Validation item 2]
- [ ] [...]

### 2. Execution
- [Execution guidance - 3-5 bullets]

### 3. Completion & Handover
- [Completion criteria - 3-5 bullets]

---

## Escalation Protocol

**When to escalate:**
- [Escalation trigger 1]
- [Escalation trigger 2]
- [...]

**How to escalate:**
1. STOP work immediately
2. Document: [what to document]
3. Escalate to: [escalation target]
4. WAIT for resolution

---

## Essential Governance Rules

### [Key Rule 1 - e.g., Zero Test Debt]
**Authority**: [canonical-reference]

[2-3 sentence summary + link to canonical doc]

### [Key Rule 2 - e.g., Build-to-Green]
**Authority**: [canonical-reference]

[2-3 sentence summary + link to canonical doc]

### [Key Rule 3]
**Authority**: [canonical-reference]

[2-3 sentence summary + link to canonical doc]

---

## Recruitment Information

**Recruited**: [YYYY-MM-DD] (Wave [X.Y])  
**Recruited By**: [recruiting-agent]  
**Contract Version**: [version]  
**Canonical Reference**: [reference-doc-path]

---

## Signature

**This minimal contract represents agent identity and references canonical governance.**

**Version**: [version]  
**Status**: Active  
**Date**: [YYYY-MM-DD]  
**Authority**: Derived from canonical governance

**Line Count Target**: 150-250 lines (excluding YAML frontmatter)

---

*END OF [AGENT NAME] MINIMAL CONTRACT*

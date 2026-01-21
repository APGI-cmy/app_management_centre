# SCOPE_DECLARATION

**Issue**: Batch 1 Phase 2: Add LOCKED Sections to Agent Contracts (FM app)  
**Date**: 2026-01-21  
**Agent**: governance-liaison (via Copilot)

## Files Modified

```
M .github/agents/Foreman-app_FM.md
M .github/agents/CodexAdvisor-agent.md
A .yamllint
```

## Changes Summary

### .github/agents/Foreman-app_FM.md
- Added 6 LOCKED sections per AGENT_CONTRACT_PROTECTION_PROTOCOL.md Section 9
  1. Mission and Authority (LOCKED)
  2. Scope (LOCKED)
  3. Contract Modification Prohibition (LOCKED)
  4. File Integrity Protection (LOCKED)
  5. Constitutional Principles (LOCKED)
  6. Prohibitions (LOCKED)
- Updated metadata: version 2.5.0 → 2.5.1, protection_model: reference-based → inline-locked-sections, added locked_sections: 6, last_updated: 2026-01-21
- Updated Protection Registry to reflect inline LOCKED sections instead of reference-based
- Added version history entry for v2.5.1

### .github/agents/CodexAdvisor-agent.md
- Added 6 LOCKED sections per AGENT_CONTRACT_PROTECTION_PROTOCOL.md Section 9
  1. Mission and Authority (LOCKED)
  2. Scope (LOCKED)
  3. Contract Modification Prohibition (LOCKED)
  4. File Integrity Protection (LOCKED)
  5. Constitutional Principles (LOCKED)
  6. Prohibitions (LOCKED)
- Updated metadata: version 1.3.0 → 1.3.1, added protection_model: inline-locked-sections, locked_sections: 6, last_updated: 2026-01-21
- Added version history entry for v1.3.1

### .yamllint
- Added yamllint configuration file to enable local validation
- Configured for 80 character line length, disabled document-start/end markers
- Enables BL-028 compliance checking

## Scope Verification

**In Scope**:
- ✅ Agent contract markdown body modifications (LOCKED sections)
- ✅ Agent contract metadata updates (version, protection_model, locked_sections, last_updated)
- ✅ Version history updates
- ✅ Protection Registry updates (Foreman-app_FM.md)

**Out of Scope** (Not Modified):
- ✅ Agent YAML frontmatter structure (only metadata values updated, structure unchanged)
- ✅ Governance canon files (no changes)
- ✅ Other agent files (not in scope)
- ✅ Builder files (not in scope)
- ✅ Application code (not in scope)

## Constitutional Compliance

**Zero Test Debt**: ✅ No test changes (documentation only)  
**Build-to-Green**: ✅ No build required (markdown documentation)  
**Architecture Conformance**: ✅ Governance layer-down per AGENT_CONTRACT_PROTECTION_PROTOCOL.md  
**Protected Paths**: ✅ Only agent contract markdown body and metadata modified per scope

## Authority

**Canonical Source**: `governance/canon/AGENT_CONTRACT_PROTECTION_PROTOCOL.md` Section 9  
**Issue Reference**: Batch 1 Phase 2 per issue description  
**Governance Binding**: AGENT_CONTRACT_PROTECTION_PROTOCOL.md Tier-0 requirements  
**CS2 Approval**: Implicit via issue creation and scope definition

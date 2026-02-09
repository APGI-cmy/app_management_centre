# SCOPE DECLARATION

**SCOPE_SCHEMA_VERSION**: v1  
**PR_ID**: TBD (Will be assigned when PR created)  
**OWNER**: Copilot (coding-agent)  
**DATE_UTC**: 2026-02-09

---

## PR Responsibility Domain

**RESPONSIBILITY_DOMAIN**: FM Agent File Living Agent System v5.0.0 Alignment

---

## Explicitly In Scope

**IN_SCOPE**:
- Restructure `.github/agents/foreman.agent.md` to follow Living Agent System v5.0.0 specification
- Add Wake-Up Protocol section with 4-level memory loading bash script
- Add POLC Framework sections (Planning, Organizing, Leading, Control)
- Add Session Closure Protocol section with bash script
- Add Agent Protection Registry section
- Reorganize existing FM content into POLC structure
- Reference (not duplicate) canonical governance protocols in LOCKED sections
- Preserve all existing governance bindings in YAML frontmatter
- Create `SCOPE_DECLARATION.md` following canonical schema
- Create `PREHANDOVER_PROOF.md` with execution log and completeness checklist
- Update agent file version to 1.0.0 with LAS v5.0.0 compliance
- Backup original foreman.agent.md as foreman.agent.md.backup

---

## Explicitly Out of Scope

**OUT_OF_SCOPE**:
- Modifying canonical governance content in `governance/canon/` directory
- Creating or modifying builder agent files (ui-builder, api-builder, etc.)
- Modifying governance-liaison or CodexAdvisor agent files
- Changes to wake-up or session closure scripts (if they exist as separate files in `.github/scripts/`)
- Creating evidence-based validation scripts (if not already existing)
- Modifying TIER_0_CANON_MANIFEST.json
- Creating new governance protocols
- Modifying BUILD_PHILOSOPHY.md or FM_ROLE_CANON.md
- Changes to CI/CD workflows
- Database migrations
- Email configuration
- Logging infrastructure
- Audit systems
- Deployment configuration
- Infrastructure changes
- Production code changes
- Test suite modifications (unless governance validation tests directly related to agent file structure)

---

## Expected Verification Signal

**EXPECTED_VERIFICATION**:
- **CI**: GREEN (all existing gates pass)
- **TESTS**: UNCHANGED (or GREEN if governance validation tests exist)
- **GOVERNANCE_GATES**: GREEN
- **YAML_FRONTMATTER**: VALID (passes YAML validation)
- **AGENT_FILE_STRUCTURE**: VALID (follows LAS v5.0.0 specification)
- **LOCKED_SECTIONS**: VALID (references canonical governance, no duplication)
- **SCOPE_DECLARATION**: PRESENT and VALID
- **PREHANDOVER_PROOF**: PRESENT and COMPLETE

---

## Scope Freeze Declaration

**SCOPE_FROZEN**: YES

This scope is frozen as of 2026-02-09. Any scope expansion requires PR closure and restart per SCOPE_DECLARATION_SCHEMA.md.

---

## Additional Context

### Why This Work
- Problem Statement: FM agent file exists but does NOT follow Living Agent System v5.0.0 structure
- Missing: Wake-Up Protocol, POLC Framework, Session Closure Protocol
- Required: LAS v5.0.0 compliance to enable FM autonomous operation with proper memory management

### Governance Authority
- `governance/canon/LIVING_AGENT_SYSTEM.md` (defines LAS v5.0.0)
- `governance/canon/SCOPE_DECLARATION_SCHEMA.md` (defines this document's structure)
- `governance/canon/FOREMAN_MEMORY_PROTOCOL.md` (defines 4-level memory hierarchy)
- `governance/canon/AGENT_CONTRACT_PROTECTION_PROTOCOL.md` (defines agent file protection)

### Evidence Requirements
- SCOPE_DECLARATION.md (this file)
- PREHANDOVER_PROOF.md (to be created)
- Both must pass evidence-based validation gate

---

**End of Scope Declaration**

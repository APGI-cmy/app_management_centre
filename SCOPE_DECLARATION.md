# Scope Declaration - Agent Contract Governance Binding Alignment to v3.0.0

**Issue**: [GOVERNANCE REMEDIATION] Align all agent contracts with full universal and agent-specific governance bindings  
**PR**: TBD  
**Date**: 2026-01-19  
**Agent**: agent-contract-administrator v3.0.0  
**Authority**: Phase 3-4 Governance Binding Audit, PR #975 manifest fix, CS2 mandate, BL-027/BL-028

---

## Files Modified

### Precondition Artifacts (Created BEFORE work)
A .agent-admin/scans/scan_20260119_135304.md
A .agent-admin/risk-assessments/risk_001_20260119.md

### Agent Contracts Upgraded (7 files - all to v3.0.0)
M .github/agents/governance-liaison.md
M .github/agents/ForemanApp-agent.md
M .github/agents/api-builder.md
M .github/agents/integration-builder.md
M .github/agents/qa-builder.md
M .github/agents/schema-builder.md
M .github/agents/ui-builder.md

---

## Not Modified

- `.github/agents/agent-contract-administrator.md` - Already at v3.0.0 (reference contract, self-modification prohibited)
- `.github/agents/CodexAdvisor-agent.md` - Not in scope (invisible to agents, CS2 only)
- `.github/agents/BUILDER_CONTRACT_SCHEMA.md` - Schema documentation (not an agent contract)
- All other repository files - Out of scope for this upgrade

---

## Changes Summary

**Upgrade Type**: Complete governance binding overhaul to align with agent-contract-administrator v3.0.0

**Key Changes Per Contract**:
1. Added 10 universal governance bindings (ALL agents):
   - governance-purpose-scope (supreme authority)
   - build-philosophy (comprehensive version)
   - zero-test-debt (canonical path)
   - **bootstrap-learnings (BL-027/BL-028 - NEW, CRITICAL)**
   - constitutional-sandbox (autonomous judgment)
   - pre-gate-merge-validation (guaranteed success)
   - opojd (terminal states)
   - mandatory-enhancement (continuous improvement)
   - agent-contract-protection (self-modification prohibition)
   - ci-confirmatory (local validation)

2. Added/verified agent-specific bindings:
   - governance-liaison: 4 liaison-specific
   - ForemanApp: 7 Foreman-specific + extended set
   - Builders (all 5): 3 builder-specific + extended governance set

3. Fixed YAML syntax errors (# comment in path field) in 5 builder files
4. Updated all contracts to version 3.0.0 with complete version history
5. Removed duplicate bindings now covered by universal set
6. Removed deprecated execution-bootstrap-protocol (replaced by bootstrap-learnings)

**Lines Changed**:
- Total agent contracts modified: 7
- YAML syntax fixes: 5 builder files
- Approximate total lines modified: ~1000+ (binding additions + reorganization + version history)

---

## Validation

### BL-027: Scope Declaration
- ✅ SCOPE_DECLARATION.md created (this file)
- ✅ ALL modified files listed above
- ⏳ Scope-to-diff validation pending (next step)

### BL-028: yamllint Compliance
- ✅ Exit code 0 achieved for all 7 agent contracts
- ✅ Zero warnings, zero errors
- ✅ No rationalizations, no exceptions

### Validation Commands

**Scope-to-Diff Validation** (BL-027):
```bash
.github/scripts/validate-scope-to-diff.sh
```
Expected: Exit code 0

**yamllint Validation** (BL-028):
```bash
yamllint .github/agents/governance-liaison.md \
         .github/agents/ForemanApp-agent.md \
         .github/agents/api-builder.md \
         .github/agents/integration-builder.md \
         .github/agents/qa-builder.md \
         .github/agents/schema-builder.md \
         .github/agents/ui-builder.md
```
Expected: Exit code 0 ✅ (ACHIEVED - verified locally)

---

## Governance Compliance

**Constitutional Principles Applied**:
- Zero Test Debt (yamllint warnings treated as errors)
- No Warning Escalations (all warnings fixed, not rationalized)
- 100% Handovers (scope fully declared, validations documented)
- Continuous Improvement (precondition artifacts created, risk assessed)
- Fail Once Doctrine (BL-027/BL-028 now bound to prevent 2-day ecosystem failures)

**Bootstrap Learnings Applied**:
- BL-027: Scope Declaration Mandatory Before PR Handover ✅
- BL-028: Yamllint Warnings Are Errors - Zero Test Debt ✅
- All 28 learnings now referenced in every agent via bootstrap-learnings binding

**Canonical Authority**:
- `governance/canon/BOOTSTRAP_EXECUTION_LEARNINGS.md` (NEW BINDING - CRITICAL)
- `governance/canon/GOVERNANCE_PURPOSE_AND_SCOPE.md` (NEW BINDING)
- `governance/canon/AGENT_CONTRACT_PROTECTION_PROTOCOL.md`
- `governance/canon/MANDATORY_ENHANCEMENT_CAPTURE_STANDARD.md` v2.0.0
- `governance/opojd/OPOJD_DOCTRINE.md` (NEW BINDING)
- `governance/canon/CI_CONFIRMATORY_NOT_DIAGNOSTIC.md` (NEW BINDING)

---

**Agent**: agent-contract-administrator v3.0.0  
**Date**: 2026-01-19  
**Status**: Scope declared, awaiting gate validation execution

# SCOPE DECLARATION

## Metadata
`SCOPE_SCHEMA_VERSION: v1`  
`PR_ID:` TBD (will be assigned by GitHub)  
`OWNER:` governance-liaison agent  
`DATE_UTC:` 2026-01-21

---

## PR Responsibility Domain

`RESPONSIBILITY_DOMAIN:` Batch 3 PR Gates & Quality Alignment Layer-Down (10 canons + 2 agent LOCKED sections)

---

## Explicitly In Scope

`IN_SCOPE:`
- Download and layer down 10 PR gate and quality canons from maturion-foreman-governance repository:
  1. PR_GATE_EVALUATION_AND_ROLE_PROTOCOL.md (new)
  2. PR_GATE_PRECONDITION_RULE.md (new)
  3. PR_SCOPE_CONTROL_POLICY.md (new)
  4. BRANCH_PROTECTION_ENFORCEMENT.md (new)
  5. BUILDER_FIRST_PR_MERGE_MODEL.md (new)
  6. QA_CATALOG_ALIGNMENT_GATE_CANON.md (new)
  7. INITIALIZATION_COMPLETENESS_GATE.md (new)
  8. WARNING_DISCOVERY_BLOCKER_PROTOCOL.md (new)
  9. GATE_PREDICTIVE_COMPLIANCE_ANALYSIS.md (new)
  10. MERGE_GATE_PHILOSOPHY.md (new)
- Add 6 LOCKED sections to schema-builder.md (.github/agents/schema-builder.md)
- Add 6 LOCKED sections to integration-builder.md (.github/agents/integration-builder.md)
- Create GOVERNANCE_ARTIFACT_INVENTORY.md (document all 39 canons: 29 existing + 10 new)
- Create governance/reports/batch-3-layerdown-log.txt
- Create governance/reports/batch-3-gate-execution.md
- Update this SCOPE_DECLARATION.md for Batch 3
- Validate all gates locally before PR creation

---

## Explicitly Out of Scope

`OUT_OF_SCOPE:`
- ❌ Foreman-app_FM.md modifications (already has LOCKED sections)
- ❌ CodexAdvisor-agent.md modifications (already has LOCKED sections)
- ❌ ui-builder.md modifications (already has LOCKED sections from Batch 2)
- ❌ api-builder.md modifications (already has LOCKED sections from Batch 2)
- ❌ qa-builder.md modifications (reserved for future batch)
- ❌ Tests (no test changes in this governance layer-down)
- ❌ CI workflow modifications
- ❌ Application code changes
- ❌ Gate script modifications
- ❌ Architecture changes
- ❌ Batch 4+ canons (reserved for future batches)

---

## Expected Verification Signal

`EXPECTED_VERIFICATION:`
- `CI: GREEN` - All applicable CI gates must pass
- `TESTS: UNCHANGED` - No test suite modifications expected
- `GOVERNANCE_GATES: GREEN` - Governance compliance gates must pass
- `SCOPE_TO_DIFF: ALIGNED` - Scope declaration matches actual file changes
- `YAML_LINT: PASS` - All YAML/markdown syntax validation passes
- `FILE_COUNT: 10_NEW_CANONS + 2_AGENT_FILES + 1_INVENTORY` - Exactly as declared

---

## Scope Freeze Declaration

`SCOPE_FROZEN: YES`

This scope is frozen as of 2026-01-21. Any deviation from this declared scope requires this PR to be closed and restarted with updated scope declaration.

---

## Authority

**Canonical Reference**: `CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md`  
**Alignment Plan**: `governance/reports/alignment-plan-office-app-20260121.md` (Batch 3)  
**Issue Reference**: [Governance Layer-Down] Batch 3: PR Gates & Quality Alignment (10 canons + 2 agent LOCKED sections)
**Dependencies**: ✅ Batch 1 Complete, ✅ Batch 2 Complete

---

**Status**: ACTIVE  
**Governance Liaison**: ✅ APPROVED

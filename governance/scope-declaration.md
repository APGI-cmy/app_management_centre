# SCOPE DECLARATION

## Metadata
`SCOPE_SCHEMA_VERSION: v1`  
`PR_ID:` TBD (will be assigned by GitHub)  
`OWNER:` governance-liaison agent  
`DATE_UTC:` 2026-01-21

---

## PR Responsibility Domain

`RESPONSIBILITY_DOMAIN:` Batch 4 FM-Specific & Learning Alignment Layer-Down (10 canons + 2 agent file updates)

---

## Explicitly In Scope

`IN_SCOPE:`
- Download and layer down 10 FM-specific and learning loop canons from maturion-foreman-governance repository:
  1. FM_GOVERNANCE_LOADING_PROTOCOL.md (new)
  2. FM_BUILDER_APPOINTMENT_PROTOCOL.md (new)
  3. FM_PREAUTH_CHECKLIST_CANON.md (new)
  4. FM_RUNTIME_ENFORCEMENT_AND_AWARENESS_MODEL.md (new)
  5. FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md (new)
  6. LEARNING_INTAKE_AND_PROMOTION_MODEL.md (new)
  7. LEARNING_PROMOTION_RULE.md (new)
  8. FAILURE_PROMOTION_RULE.md (new)
  9. BUILD_INTERVENTION_AND_ALERT_MODEL.md (new)
  10. CASCADING_FAILURE_CIRCUIT_BREAKER.md (new)
- Add 6 LOCKED sections to qa-builder.md (.github/agents/qa-builder.md)
- Add protection note to BUILDER_CONTRACT_SCHEMA.md (.github/agents/BUILDER_CONTRACT_SCHEMA.md)
- Update GOVERNANCE_ARTIFACT_INVENTORY.md (document all 40 canons: 30 existing + 10 new)
- Create governance/reports/batch-4-layerdown-log.txt
- Create governance/reports/batch-4-gate-execution.md
- Update this SCOPE_DECLARATION.md for Batch 4
- Validate all gates locally before PR creation

---

## Explicitly Out of Scope

`OUT_OF_SCOPE:`
- ❌ Foreman-app_FM.md modifications (already has LOCKED sections)
- ❌ CodexAdvisor-agent.md modifications (already has LOCKED sections)
- ❌ ui-builder.md modifications (already has LOCKED sections from Batch 2)
- ❌ api-builder.md modifications (already has LOCKED sections from Batch 2)
- ❌ schema-builder.md modifications (already has LOCKED sections from Batch 3)
- ❌ integration-builder.md modifications (already has LOCKED sections from Batch 3)
- ❌ Tests (no test changes in this governance layer-down)
- ❌ CI workflow modifications
- ❌ Application code changes
- ❌ Gate script modifications
- ❌ Architecture changes
- ❌ Batch 5+ canons (reserved for future batches)

---

## Expected Verification Signal

`EXPECTED_VERIFICATION:`
- `CI: GREEN` - All applicable CI gates must pass
- `TESTS: UNCHANGED` - No test suite modifications expected
- `GOVERNANCE_GATES: GREEN` - Governance compliance gates must pass
- `SCOPE_TO_DIFF: ALIGNED` - Scope declaration matches actual file changes
- `YAML_LINT: PASS` - All YAML/markdown syntax validation passes
- `LOCKED_SECTIONS: PASS` - LOCKED section validation passes
- `FILE_COUNT: 10_NEW_CANONS + 1_QA_BUILDER + 1_SCHEMA_UPDATE + 1_INVENTORY` - Exactly as declared

---

## Scope Freeze Declaration

`SCOPE_FROZEN: YES`

This scope is frozen as of 2026-01-21. Any deviation from this declared scope requires this PR to be closed and restarted with updated scope declaration.

---

## Authority

**Canonical Reference**: `CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md`  
**Alignment Plan**: `governance/reports/alignment-plan-office-app-20260121.md` (Batch 4)  
**Issue Reference**: [Governance Layer-Down] Batch 4: FM-Specific & Learning Alignment (10 canons + 2 agent file updates)  
**Dependencies**: ✅ Batch 1 Complete, ✅ Batch 2 Complete, ✅ Batch 3 Complete

---

**Status**: ACTIVE  
**Governance Liaison**: ✅ APPROVED

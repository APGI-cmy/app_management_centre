# SCOPE DECLARATION

## Metadata
`SCOPE_SCHEMA_VERSION: v1`  
`PR_ID:` TBD (will be assigned by GitHub)  
`OWNER:` governance-liaison agent  
`DATE_UTC:` 2026-01-21

---

## PR Responsibility Domain

`RESPONSIBILITY_DOMAIN:` Batch 2 Agent Governance Layer-Down (10 canons + 2 agent LOCKED sections)

---

## Explicitly In Scope

`IN_SCOPE:`
- Download and layer down 10 agent governance canons from maturion-foreman-governance repository:
  1. AGENT_FILE_BINDING_REQUIREMENTS.md (verify/update existing)
  2. AGENT_CANONICAL_CONTEXT_SYNCHRONISATION_PROTOCOL.md (new)
  3. AGENT_RECRUITMENT.md (new)
  4. AGENT_RIPPLE_AWARENESS_OBLIGATION.md (new)
  5. AGENT_ROLE_GATE_APPLICABILITY.md (new)
  6. AGENT_ONBOARDING_QUICKSTART.md (new)
  7. BUILDER_CONTRACT_BINDING_CHECKLIST.md (new)
  8. COGNITIVE_CAPABILITY_ORCHESTRATION_MODEL.md (new)
  9. DELEGATION_INSTRUCTION_AND_AUDIT_MODEL.md (new)
  10. DOMAIN_OWNERSHIP_ACCOUNTABILITY.md (new)
- Add 6 LOCKED sections to ui-builder.md (.github/agents/ui-builder.md)
- Add 6 LOCKED sections to api-builder.md (.github/agents/api-builder.md)
- Create governance/reports/batch-2-layerdown-log.txt
- Create governance/reports/batch-2-gate-execution.md
- Update this SCOPE_DECLARATION.md for Batch 2
- Validate all gates locally before PR creation

---

## Explicitly Out of Scope

`OUT_OF_SCOPE:`
- ❌ Foreman-app_FM.md modifications (already has LOCKED sections)
- ❌ CodexAdvisor-agent.md modifications (already has LOCKED sections)
- ❌ schema-builder.md modifications (reserved for future batch)
- ❌ qa-builder.md modifications (reserved for future batch)
- ❌ integration-builder.md modifications (reserved for future batch)
- ❌ Tests (no test changes in this governance layer-down)
- ❌ CI workflow modifications
- ❌ Application code changes
- ❌ Gate script modifications
- ❌ Architecture changes
- ❌ Batch 3+ canons (reserved for future batches)

---

## Expected Verification Signal

`EXPECTED_VERIFICATION:`
- `CI: GREEN` - All applicable CI gates must pass
- `TESTS: UNCHANGED` - No test suite modifications expected
- `GOVERNANCE_GATES: GREEN` - Governance compliance gates must pass
- `SCOPE_TO_DIFF: ALIGNED` - Scope declaration matches actual file changes
- `YAML_LINT: PASS` - All YAML/markdown syntax validation passes
- `FILE_COUNT: 9_NEW_CANONS + 1_UPDATED_CANON + 2_AGENT_FILES` - Exactly as declared

---

## Scope Freeze Declaration

`SCOPE_FROZEN: YES`

This scope is frozen as of 2026-01-21. Any deviation from this declared scope requires this PR to be closed and restarted with updated scope declaration.

---

## Authority

**Canonical Reference**: `CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md`  
**Alignment Plan**: `governance/reports/alignment-plan-office-app-20260121.md` (Batch 2)  
**Issue Reference**: [Governance Layer-Down] Batch 2: Agent Governance Alignment (10 canons + 2 agent LOCKED sections)
**Dependencies**: ✅ Batch 1 Complete

---

**Status**: ACTIVE  
**Governance Liaison**: ✅ APPROVED

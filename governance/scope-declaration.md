# SCOPE DECLARATION

## Metadata
`SCOPE_SCHEMA_VERSION: v1`  
`PR_ID:` TBD (will be assigned by GitHub)  
`OWNER:` governance-liaison agent  
`DATE_UTC:` 2026-01-21

---

## PR Responsibility Domain

`RESPONSIBILITY_DOMAIN:` Batch 1 Governance Canon Layer-Down

---

## Explicitly In Scope

`IN_SCOPE:`
- Download and verify 10 critical canonical governance files from maturion-foreman-governance repository
- Layer down canons to local `governance/canon/` directory:
  1. AGENT_CONTRACT_PROTECTION_PROTOCOL.md
  2. MANDATORY_ENHANCEMENT_CAPTURE_STANDARD.md
  3. CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md
  4. GOVERNANCE_RIPPLE_MODEL.md
  5. CI_CONFIRMATORY_NOT_DIAGNOSTIC.md
  6. SCOPE_DECLARATION_SCHEMA.md
  7. SCOPE_TO_DIFF_RULE.md
  8. GOVERNANCE_PURPOSE_AND_SCOPE.md
  9. AGENT_RECRUITMENT_AND_CONTRACT_AUTHORITY_MODEL.md
  10. CS2_AGENT_FILE_AUTHORITY_MODEL.md
- Create SCOPE_DECLARATION.md (this file)
- Create BATCH_1_INITIATION_SUMMARY.md documenting scope and objectives
- Create BATCH_1_PREHANDOVER_PROOF.md documenting validation execution
- Update governance documentation references to align with Batch 1 canons
- Validate all governance markdown files for formatting correctness
- Ensure canonical governance version tracking documentation

---

## Explicitly Out of Scope

`OUT_OF_SCOPE:`
- ❌ Agent file modifications (Foreman-app_FM.md, CodexAdvisor-agent.md) - Reserved for Batch 1 Phase 2
- ❌ Tests (no test changes in this governance layer-down)
- ❌ CI workflow modifications
- ❌ Migrations or database changes
- ❌ Email or notification system changes
- ❌ Logging or audit system modifications
- ❌ Deployment or infrastructure changes
- ❌ Application code changes
- ❌ Implementation of any governance requirements beyond layer-down
- ❌ Gate script modifications
- ❌ Builder contract updates
- ❌ QA catalog modifications
- ❌ Architecture changes
- ❌ Batch 2-10 canons (reserved for future batches)
- ❌ Version alignment of existing local canons (to be addressed separately if needed)

---

## Expected Verification Signal

`EXPECTED_VERIFICATION:`
- `CI: GREEN` - All applicable CI gates must pass
- `TESTS: UNCHANGED` - No test suite modifications expected
- `GOVERNANCE_GATES: GREEN` - Governance compliance gates must pass
- `SCOPE_TO_DIFF: ALIGNED` - Scope declaration matches actual file changes
- `FILE_COUNT: 10_CANONS + 3_DOCS` - Exactly 10 canon files + 3 documentation files created

---

## Scope Freeze Declaration

`SCOPE_FROZEN: YES`

This scope is frozen as of 2026-01-21. Any deviation from this declared scope requires this PR to be closed and restarted with updated scope declaration.

---

## Authority

**Canonical Reference**: `CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md`  
**Gap Analysis**: `governance/reports/gap-analysis-office-app-20260121.md`  
**Alignment Plan**: `governance/reports/alignment-plan-office-app-20260121.md`  
**Issue Reference**: Batch 1 Initiation: FM App Governance Canon Layer-Down

---

**Status**: ACTIVE  
**Governance Liaison**: ✅ APPROVED

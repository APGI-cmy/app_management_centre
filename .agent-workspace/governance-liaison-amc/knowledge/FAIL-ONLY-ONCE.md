# FAIL-ONLY-ONCE Breach Registry — governance-liaison-amc

**Workspace**: governance-liaison-amc  
**Created**: 2026-04-08  
**Status**: CLEAR TO PROCEED

## Open Breaches

None.

## Closed Breaches

None.

---

## Systemic Rules (from IAA A-036)

The following rules are added per IAA session-026 systemic promotion (A-036, ENV_BOOTSTRAP_LIAISON_AMC_PRE_COMMIT_OMISSION):

| Rule ID | Description | Added | Source |
|---------|-------------|-------|--------|
| FAIL-GL-001 | Session memory `iaa_invocation_result` MUST NEVER contain `PHASE_A_ADVISORY`. Under PHASE_B_BLOCKING, valid values are: AWAITING, ASSURANCE-TOKEN received, or REJECTION-PACKAGE received. | 2026-04-08 | IAA-026 REJECTION-PACKAGE |
| FAIL-GL-002 | ALL session artifacts (PREHANDOVER proof, session memory, evidence bundle) MUST be committed to HEAD before invoking IAA. Invoking IAA before committing = ENVIRONMENT_BOOTSTRAP failure. | 2026-04-08 | IAA-026 REJECTION-PACKAGE (A-036 systemic) |

---

*This registry is maintained per AGENT_PREFLIGHT_PATTERN.md §1.5. Any open breach must be resolved before new work is accepted.*

# How to Use Evidence-Based Validation (BL-027/028)

**Pattern**: Evidence-Based CI Gate Validation  
**Authority**: BL-027/028 Bootstrap Execution Learnings  
**Status**: Active in FM Office App

---

## Overview

Evidence-based validation allows you to submit a PR with pre-executed validation evidence instead of requiring CI to re-run all gate validation scripts. This implements the "CI is confirmatory, not diagnostic" principle from BL-027/028.

---

## When to Use

Use evidence-based validation when:
- You have already run all validation scripts locally
- All validations passed with exit code 0
- You want to demonstrate BL-027/028 compliance
- You want faster CI execution (gates skip re-running validations)

---

## How It Works

### Step 1: Run Validations Locally

Execute all required validation scripts locally and capture evidence:

```bash
# Example: Run tier-0 validation
python scripts/validate_tier0_activation.py
# Capture: Exit code, timestamp, output

# Example: Run agent boundary validation
python governance/scripts/validate_agent_boundaries.py --reports "..." --current-repo "..."
# Capture: Exit code, timestamp, output

# Continue for all applicable gates...
```

### Step 2: Create PREHANDOVER_PROOF

Create a file named `PREHANDOVER_PROOF.md` (or `PREHANDOVER_PROOF_*.md`) containing:

```markdown
# PREHANDOVER_PROOF

**Agent**: [Your Name/Role]
**PR**: #[PR Number]
**Date**: [ISO 8601 Date]

## Gate Validation Evidence

### Tier-0 Activation Validation
**Method**: Evidence-Based
**Gate**: tier0-activation-gate.yml

**Evidence**:
\```bash
$ python scripts/validate_tier0_activation.py
✅ All checks passed
\```

**Exit Code**: 0
**Timestamp**: 2026-01-19T16:30:00Z

### Agent Boundary Validation
**Method**: Evidence-Based
**Gate**: agent-boundary-gate.yml

**Evidence**:
\```bash
$ python governance/scripts/validate_agent_boundaries.py
✅ All boundaries valid
\```

**Exit Code**: 0
**Timestamp**: 2026-01-19T16:30:00Z

[... Continue for each gate ...]
```

### Step 3: Submit PR

When you submit the PR:
1. CI gates detect the PREHANDOVER_PROOF file
2. Gates search for their specific keywords
3. If found: Gate skips execution and accepts evidence
4. If not found: Gate runs normally

### Step 4: Verify in CI Logs

Check CI logs to confirm evidence-based validation:

```
=== Evidence-Based Validation Check (BL-027/028) ===
Gate: Tier-0 Activation Validation

✅ Found PREHANDOVER_PROOF.md with Tier-0 validation
✅ ACCEPTING evidence-based validation per BL-027/028
```

---

## Supported Gates

The following gates support evidence-based validation:

| Gate | Workflow File | Keywords |
|------|---------------|----------|
| Tier-0 Activation | `tier0-activation-gate.yml` | `Tier.*0`, `tier0`, `Tier-0` |
| Agent Boundary | `agent-boundary-gate.yml` | `agent.*boundar`, `Agent.*Boundar`, `QA.*Boundar` |
| Agent Contract Governance | `agent-contract-governance.yml` | `contract.*line`, `Contract.*Governance`, `agent.*contract` |
| Code Review Closure | `code-review-closure-gate.yml` | `code.*review`, `Code.*Review`, `review.*closure` |
| Builder Modular Links | `builder-modular-link-validation.yml` | `builder.*modular`, `Builder.*Modular`, `modular.*link` |
| Governance Coupling | `governance-coupling-gate.yml` | `governance.*coupling`, `Governance.*Coupling`, `coupling.*rule` |

---

## PREHANDOVER_PROOF Template

Use this template to create your PREHANDOVER_PROOF:

```markdown
# PREHANDOVER_PROOF

**Agent**: [Your Agent Name]
**PR**: #[PR Number]
**Branch**: [Branch Name]
**Date**: [YYYY-MM-DD]
**Protocol Version**: v2.0.0+

---

## Gate Validation Evidence

### [Gate Name]
**Method**: Evidence-Based
**Gate**: [workflow-file-name.yml]

**Evidence**:
\```bash
[Command executed]
[Output summary]
\```

**Exit Code**: 0
**Timestamp**: [ISO 8601 Timestamp]

---

[Repeat for each gate]

---

## Summary

All gates validated locally:
- [x] Gate 1
- [x] Gate 2
...

**Compliance**: BL-027/028
**Status**: READY FOR HANDOVER
```

---

## Keywords Reference

Each gate searches for specific keywords in your PREHANDOVER_PROOF. Include these in your gate documentation:

### Tier-0 Activation
- "Tier-0" or "tier0" or "Tier 0"
- Example: "Tier-0 Activation Validation"

### Agent Boundary
- "agent boundary" or "Agent Boundary" or "QA Boundary"
- Example: "Agent Boundary Validation"

### Agent Contract Governance
- "contract line" or "Contract Governance" or "agent contract"
- Example: "Agent Contract Governance"

### Code Review Closure
- "code review" or "Code Review" or "review closure"
- Example: "Code Review Closure Validation"

### Builder Modular Links
- "builder modular" or "Builder Modular" or "modular link"
- Example: "Builder Modular Link Validation"

### Governance Coupling
- "governance coupling" or "Governance Coupling" or "coupling rule"
- Example: "Governance Coupling Validation"

---

## Benefits

1. **Faster CI**: Gates skip re-running validations
2. **BL-027/028 Compliance**: Demonstrates local validation before PR
3. **Auditability**: Evidence preserved in PREHANDOVER_PROOF
4. **Flexibility**: Can still run validations if evidence not provided

---

## Fallback Behavior

If PREHANDOVER_PROOF is not provided or doesn't contain evidence for a gate:
- Gate runs validation script normally
- No change in gate behavior
- PR can still pass if validation succeeds

This ensures backward compatibility and safety.

---

## Example

See `PREHANDOVER_PROOF_TEST_BL_027_028.md` in this repository for a complete example demonstrating evidence for all 6 gates.

---

## References

- **Pattern Source**: [PartPulse PR #188](https://github.com/APGI-cmy/PartPulse/pull/188)
- **Governance Pattern**: [maturion-foreman-governance PR #981](https://github.com/APGI-cmy/maturion-foreman-governance/pull/981)
- **BL-027/028**: `governance/canon/BOOTSTRAP_EXECUTION_LEARNINGS.md`
- **BL-028 Details**: `bootstrap/learnings/BL-028-BUILDER-PREHANDOVER-EXECUTION-ENFORCEMENT.md`

---

**Authority**: BL-027/028  
**Implementation**: Issue #[TBD]  
**Status**: Active and Ready for Use

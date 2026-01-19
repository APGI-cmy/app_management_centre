# Evidence-Based Validation (BL-027/028)

**Version**: 1.0.0  
**Date**: 2026-01-19  
**Authority**: BL-027, BL-028, BOOTSTRAP_EXECUTION_LEARNINGS.md  
**Status**: Active

---

## Overview

This directory contains documentation and tools for **evidence-based validation**, an alternative to automated script execution for PR gate validation. Evidence-based validation allows agents to manually verify gate requirements and provide attestation when automated scripts are unavailable or impractical.

---

## Quick Start

### For Automated Validation (Preferred)

```bash
# 1. Run validation script
./scripts/validate-scope-to-diff.sh

# 2. Check exit code
echo $?  # MUST be 0

# 3. Document in PREHANDOVER_PROOF
python3 scripts/generate-prehandover-proof-template.py
./scripts/prehandover-capture.sh -- "./scripts/validate-scope-to-diff.sh"
```

### For Evidence-Based Validation (Alternative)

```bash
# 1. Create SCOPE_DECLARATION.md
cat > SCOPE_DECLARATION.md << 'EOF'
# Scope Declaration - [PR Title]

**Issue**: #[number]
**Date**: 2026-01-19
**Agent**: [Your Name]

## Files Modified
1. `path/to/file.ext` - M - [Description]
EOF

# 2. Verify against git diff
git diff --name-status HEAD~1 HEAD > /tmp/git-diff.txt

# 3. Document in PREHANDOVER_PROOF
# See governance/schemas/evidence-based-validation-schema.md

# 4. Validate evidence completeness
python3 governance/scripts/validate_evidence_based.py PREHANDOVER_PROOF.md
```

---

## Two Validation Modes

All PR gates in the Maturion ecosystem support **TWO validation modes**:

| Mode | When to Use | Exit Code | Documentation |
|------|-------------|-----------|---------------|
| **Automated** | Script available and practical | Exit code 0 required | Minimal (command + exit code) |
| **Evidence-Based** | Script unavailable/impractical | N/A | Extensive (steps, evidence, attestation) |

**Preference**: Always use automated validation when available. Evidence-based validation requires more rigorous documentation.

---

## Files in This Implementation

### Schemas
- **`evidence-based-validation-schema.md`**: Complete specification of evidence-based validation requirements
  - Two validation modes defined
  - Required components for evidence-based mode
  - SCOPE_DECLARATION.md requirements
  - YAML validation requirements (BL-028)
  - Examples for all gates

### Scripts
- **`validate_evidence_based.py`**: Validates evidence-based validation completeness
  - Checks mode declaration
  - Validates reason, method, steps
  - Verifies evidence artifacts
  - Confirms attestation with confidence level

### CI Workflows
- **`.github/workflows/prehandover-proof-validation.yml`**: Updated to recognize both modes
  - Detects validation mode from PREHANDOVER_PROOF
  - Runs appropriate validator
  - Reports mode in PR comments

### Configuration
- **`.yamllint`**: YAMLlint configuration for BL-028 compliance
  - Line length: 120 chars (relaxed for GitHub Actions)
  - Zero warnings, zero errors enforced

---

## Evidence-Based Validation Requirements

When using evidence-based validation, you MUST provide:

1. **Mode Declaration**: Explicitly state "Evidence-Based" mode
2. **Reason**: Why evidence-based validation used (e.g., "Script not present")
3. **Method**: How verification was performed (e.g., "Manual git diff comparison")
4. **Verification Steps**: Minimum 3 steps documenting what you did
5. **Evidence Artifacts**: At least one concrete evidence (logs, screenshots, outputs)
6. **Findings**: Document compliance status for each requirement
7. **Attestation**: Personal attestation with date and confidence level

**All 7 components are mandatory.** Incomplete evidence = gate failure.

---

## Common Use Cases

### 1. Scope Declaration (BL-027)

**Automated**:
```bash
./scripts/validate-scope-to-diff.sh  # Exit code 0
```

**Evidence-Based**:
```markdown
**Validation Mode**: Evidence-Based (Script Not Present)
**Method**: Manual git diff comparison

**Verification Steps**:
1. Created SCOPE_DECLARATION.md
2. Ran `git diff --name-status HEAD~1 HEAD`
3. Verified files match

**Evidence**:
```
M       file1.ext
A       file2.ext
```

**Attestation**: I attest SCOPE_DECLARATION.md is accurate.
```

### 2. YAML Syntax (BL-028)

**Automated**:
```bash
yamllint .github/agents/*.md  # Exit code 0
```

**Evidence-Based**:
```markdown
**Validation Mode**: Evidence-Based
**Method**: Manual yamllint execution

**Verification Steps**:
1. Installed yamllint
2. Ran yamllint on all YAML files
3. Verified exit code 0
4. Verified zero warnings (BL-028)

**Evidence**:
```bash
$ yamllint file.yml
$ echo $?
0
```

**BL-028 Compliance**: ✅ Zero warnings, zero errors

**Attestation**: I attest yamllint produced zero warnings/errors.
```

### 3. Branch Protection

**Evidence-Based** (API verification):
```markdown
**Validation Mode**: Evidence-Based (Requires API Access)
**Method**: GitHub web UI inspection

**Verification Steps**:
1. Navigated to Settings > Branches
2. Verified main branch protection enabled
3. Checked required status checks
4. Verified administrator enforcement

**Evidence**:
- Screenshot: `evidence/branch-protection.png`
- API Response: `evidence/api-response.json`

**Findings**:
- ✅ Branch protection: COMPLIANT
- ✅ Required checks: COMPLIANT (3 configured)
- ✅ Admin enforcement: COMPLIANT

**Attestation**: I attest all requirements are compliant.
```

---

## CI Workflow Behavior

### Detection Logic

```yaml
if grep -q "Validation Mode.*Evidence-Based" PREHANDOVER_PROOF.md; then
  echo "📋 Evidence-Based Mode"
  python3 governance/scripts/validate_evidence_based.py PREHANDOVER_PROOF.md
else
  echo "🤖 Automated Mode"
  ./scripts/validate-gate.sh  # Exit code 0 required
fi
```

### PR Comments

**Evidence-Based Mode Pass**:
```
✅ PREHANDOVER_PROOF Validation Gate - PASS

**Validation Mode**: Evidence-Based (Manual Verification + Attestation)

All evidence requirements met:
- ✅ Mode declared
- ✅ Reason documented
- ✅ Method documented
- ✅ Verification steps (5 steps)
- ✅ Evidence artifacts provided
- ✅ Findings documented
- ✅ Attestation present

Authority: BL-027/028
```

**Evidence-Based Mode Fail**:
```
❌ PREHANDOVER_PROOF Validation Gate - INCOMPLETE

**Validation Mode**: Evidence-Based (Incomplete)

Missing requirements:
- ❌ Verification steps insufficient (found 2, minimum 3)
- ❌ No evidence artifacts provided
- ❌ Attestation missing confidence level

Fix: See governance/schemas/evidence-based-validation-schema.md
```

---

## Zero Test Debt Compatibility

Evidence-based validation maintains zero-test-debt principles:

1. **100% Coverage**: All requirements MUST be verified (no partial verification)
2. **No Rationalization**: Cannot skip requirements
3. **Higher Bar**: Evidence-based requires MORE documentation than automated
4. **Remediation**: Non-compliance MUST be fixed
5. **Attestation Risk**: Agent personally attests to accuracy

**Prohibition**: Evidence-based validation CANNOT be used to circumvent requirements.

---

## Migration Path

For repositories adopting evidence-based validation:

### Phase 1: Document Current State
- Identify which gates lack automation
- List validation requirements for each gate

### Phase 2: Create Evidence Requirements
- Define evidence schema for each gate
- Document what constitutes "complete evidence"

### Phase 3: Update CI Workflows
- Add evidence-based validation logic
- Update PR comment templates

### Phase 4: Train Agents
- Ensure agents understand evidence requirements
- Provide examples and templates

### Phase 5: Validate First PR
- Confirm evidence-based path works end-to-end
- Use this PR (#979) as reference

### Phase 6: Monitor Quality
- Track evidence quality and completeness
- Identify patterns requiring automation

### Phase 7: Automate Over Time
- Build automated scripts to replace evidence-based validation
- Prefer automation when feasible

**Goal**: Evidence-based validation is a bridge, not a destination.

---

## Examples

### Complete Example: Scope Declaration (Evidence-Based)

See `PREHANDOVER_PROOF.md` in this PR (#979) for a working example of evidence-based validation for scope declaration.

### Template

```markdown
### Gate: [Gate Name] (BL-027/028)

**Validation Mode**: Evidence-Based ([Reason])
**Reason**: [Why evidence-based validation used]
**Method**: [How verification was performed]

**Verification Steps**:
1. [First step]
2. [Second step]
3. [Third step]
4. [Additional steps...]

**Evidence**:
[Concrete evidence: logs, screenshots, outputs, diffs]

**Findings**:
- ✅ [Requirement 1]: COMPLIANT - [details]
- ✅ [Requirement 2]: COMPLIANT - [details]

**Attestation**:
I, [Agent Name], attest that I have manually verified all requirements
for [Gate Name] and documented complete evidence above.

**Date**: [ISO 8601 timestamp]
**Verification Confidence**: [HIGH | MEDIUM | LOW]
```

---

## Validation Scripts

### validate_evidence_based.py

```bash
# Check if PREHANDOVER_PROOF uses evidence-based validation
python3 governance/scripts/validate_evidence_based.py PREHANDOVER_PROOF.md

# Check specific gate
python3 governance/scripts/validate_evidence_based.py PREHANDOVER_PROOF.md "Scope Declaration"

# Exit codes:
# 0 - Evidence complete and valid
# 1 - Evidence incomplete or invalid
# 3 - Not evidence-based mode (automated mode detected)
```

**What it checks**:
- Mode declaration present
- Reason documented
- Method documented
- Verification steps (minimum 3)
- Evidence artifacts present
- Findings documented with compliance status
- Attestation present with date and confidence

---

## Authority & Enforcement

**Constitutional Authority**: BUILD_PHILOSOPHY.md Section II  
**Governance Authority**: BOOTSTRAP_EXECUTION_LEARNINGS.md (BL-027, BL-028)  
**Enforcement**: CI gates + human review  
**Non-Negotiable**: Zero test debt, no rationalization, complete documentation

---

## References

- **BL-027**: Scope Declaration Mandatory Before PR Handover
- **BL-028**: YAMLlint Warnings ARE Errors
- **Schema**: `governance/schemas/evidence-based-validation-schema.md`
- **Validator**: `governance/scripts/validate_evidence_based.py`
- **BOOTSTRAP_EXECUTION_LEARNINGS.md**: All bootstrap learnings
- **AGENT_CONTRACT_PROTECTION_PROTOCOL.md**: Pre-gate validation requirements

---

## Support

For questions or issues with evidence-based validation:

1. **Read the schema**: `governance/schemas/evidence-based-validation-schema.md`
2. **Check examples**: See this PR (#979) PREHANDOVER_PROOF.md
3. **Run validator locally**: `python3 governance/scripts/validate_evidence_based.py --help`
4. **Escalate to Governance Liaison**: For governance interpretation
5. **Escalate to FM**: For execution decisions

---

**Status**: ✅ ACTIVE  
**Last Updated**: 2026-01-19  
**Maintained By**: Governance Liaison + FM

---

**END OF DOCUMENTATION**

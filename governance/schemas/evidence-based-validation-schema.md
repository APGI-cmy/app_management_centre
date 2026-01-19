# Evidence-Based Validation Schema (BL-027/028)

**Version**: 1.0.0  
**Date**: 2026-01-19  
**Authority**: BL-027, BL-028, BOOTSTRAP_EXECUTION_LEARNINGS.md  
**Status**: Active

---

## Purpose

This schema defines the requirements for evidence-based validation as an alternative to automated script execution for PR gate validation. Evidence-based validation allows agents to manually verify gate requirements and provide attestation when automated scripts are unavailable, impractical, or when manual verification is more appropriate.

---

## Two Validation Modes

All PR gates in the Maturion ecosystem support **TWO validation modes**:

### Mode 1: Automated Script Execution (Preferred)
- Execute validation script locally
- Capture exit code (MUST be 0)
- Document command and output in PREHANDOVER_PROOF
- CI confirmatory run validates same

### Mode 2: Evidence-Based Validation (Alternative)
- Manually verify gate requirements
- Document verification steps and findings
- Provide attestation of compliance
- Include evidence artifacts (screenshots, logs, outputs)
- Document in PREHANDOVER_PROOF with evidence markers

---

## When to Use Evidence-Based Validation

Evidence-based validation is appropriate when:

1. **Script Not Available**: Validation script does not exist in repository
2. **Script Impractical**: Script requires access/credentials not available locally
3. **Manual Inspection**: Requirements are better verified through human inspection
4. **Bootstrap Phase**: During initial setup before automation infrastructure exists
5. **One-Time Checks**: For checks that don't benefit from automation

**Note**: Automated validation is always preferred when available. Evidence-based validation requires more rigorous documentation.

---

## Evidence-Based Validation Requirements

### Required Components

#### 1. Explicit Mode Declaration
PREHANDOVER_PROOF MUST explicitly state validation mode:

```markdown
### Gate: [Gate Name]

**Validation Mode**: Evidence-Based (Manual Verification)  
**Reason**: [Why evidence-based validation used]  
**Method**: [How verification was performed]
```

#### 2. Verification Steps
Document exact steps taken to verify compliance:

```markdown
**Verification Steps**:
1. [First step taken]
2. [Second step taken]
3. [Third step taken]
...
```

#### 3. Evidence Artifacts
Provide concrete evidence of verification:

```markdown
**Evidence**:
- Screenshot: [description]
- Log output: [description]
- File contents: [description]
- Git diff: [description]
```

#### 4. Findings Documentation
Document what was found during verification:

```markdown
**Findings**:
- ✅ [Requirement 1]: COMPLIANT - [details]
- ✅ [Requirement 2]: COMPLIANT - [details]
- ❌ [Requirement 3]: NON-COMPLIANT - [details]
```

#### 5. Attestation
Agent must attest to verification completeness:

```markdown
**Attestation**:
I, [Agent Name], attest that I have manually verified all requirements for [Gate Name] and documented complete evidence above. All requirements marked COMPLIANT have been thoroughly verified. Any non-compliance is documented with remediation plan.

**Date**: [ISO 8601 timestamp]  
**Verification Confidence**: [HIGH | MEDIUM | LOW]
```

#### 6. Remediation (if needed)
If non-compliance found, document remediation:

```markdown
**Remediation**:
- Issue: [What was non-compliant]
- Action Taken: [How it was fixed]
- Verification: [How fix was verified]
- Status: ✅ RESOLVED
```

---

## SCOPE_DECLARATION.md Requirements

For evidence-based validation of scope declaration (BL-027):

### Manual Scope-to-Diff Verification

When `validate-scope-to-diff.sh` script is not available:

1. **Create SCOPE_DECLARATION.md**:
   ```markdown
   # Scope Declaration - [PR Title]
   
   **Issue**: #[number]
   **PR**: #[number] (or TBD)
   **Date**: [ISO 8601 date]
   **Agent**: [Agent name]
   **Authority**: BL-027
   
   ---
   
   ## Files Modified
   
   ### [Category] ([count] files)
   1. `path/to/file1.ext` - [M/A/D] - [Brief description]
   2. `path/to/file2.ext` - [M/A/D] - [Brief description]
   
   ---
   
   ## Files NOT Modified
   
   - [Explicitly list related files NOT changed]
   - [This demonstrates scope awareness]
   ```

2. **Verify Against Git Diff**:
   ```bash
   git diff --name-status HEAD~1 HEAD
   # OR
   git diff --name-status main HEAD
   ```

3. **Document in PREHANDOVER_PROOF**:
   ```markdown
   ### Gate: Scope Declaration Validation (BL-027)
   
   **Validation Mode**: Evidence-Based (Script Not Present)  
   **Reason**: `validate-scope-to-diff.sh` not present in repository  
   **Method**: Manual git diff comparison
   
   **Verification Steps**:
   1. Created SCOPE_DECLARATION.md listing all changed files
   2. Executed `git diff --name-status HEAD~1 HEAD`
   3. Compared SCOPE_DECLARATION.md entries to git diff output
   4. Verified all files in git diff are listed in SCOPE_DECLARATION.md
   5. Verified no extra files listed in SCOPE_DECLARATION.md
   
   **Git Diff Output**:
   ```
   M       file1.ext
   A       file2.ext
   D       file3.ext
   ```
   
   **SCOPE_DECLARATION.md Content**: ✅ Created and matches git diff  
   **File Count Match**: ✅ Yes (3 files in both)  
   **File Paths Match**: ✅ Yes (all paths identical)  
   **Status**: ✅ PASS
   
   **Attestation**:
   I attest that SCOPE_DECLARATION.md accurately lists all files changed in this PR and matches git diff output exactly.
   
   **Date**: 2026-01-19T15:00:00Z  
   **Verification Confidence**: HIGH
   ```

---

## YAML Validation Requirements (BL-028)

For yamllint validation:

### Automated (Preferred)
```markdown
### Gate: YAML Syntax Validation (BL-028)

**Validation Mode**: Automated Script Execution  
**Command**: `yamllint .github/agents/*.md`  
**Exit Code**: 0  
**Status**: ✅ PASS

**Output**:
```
(no output - zero warnings, zero errors)
```
```

### Evidence-Based (If Needed)
```markdown
### Gate: YAML Syntax Validation (BL-028)

**Validation Mode**: Evidence-Based (Verification Through Linter)  
**Reason**: [Why not automated execution]  
**Method**: Manual yamllint execution and output verification

**Verification Steps**:
1. Installed yamllint locally
2. Executed `yamllint .github/agents/[file].md`
3. Verified exit code 0
4. Verified zero warnings (BL-028: warnings ARE errors)
5. Verified zero errors

**Evidence**:
```bash
$ yamllint .github/agents/governance-liaison.md
$ echo $?
0
```

**BL-028 Compliance**: ✅ PASS
- Exit Code: 0
- Warnings: 0 (BL-028 requires zero)
- Errors: 0

**Attestation**:
I attest that yamllint produced zero warnings and zero errors for all YAML files modified in this PR, in compliance with BL-028.

**Date**: 2026-01-19T15:00:00Z  
**Verification Confidence**: HIGH
```

---

## CI Workflow Recognition

CI workflows MUST recognize both validation modes:

### Workflow Logic Pattern

```yaml
- name: Validate [Gate Name]
  run: |
    # Check if PREHANDOVER_PROOF exists
    if [ -f "PREHANDOVER_PROOF.md" ]; then
      # Check validation mode in PREHANDOVER_PROOF
      if grep -q "Validation Mode.*Evidence-Based" PREHANDOVER_PROOF.md; then
        echo "Evidence-based validation detected"
        echo "Verifying evidence completeness..."
        
        # Validate evidence requirements met
        python3 governance/scripts/validate_evidence_based.py PREHANDOVER_PROOF.md
        
        if [ $? -eq 0 ]; then
          echo "✅ Evidence-based validation ACCEPTED"
          exit 0
        else
          echo "❌ Evidence-based validation INCOMPLETE"
          exit 1
        fi
      else
        echo "Automated validation mode"
        # Run automated validation
        ./scripts/validate-[gate].sh
        exit $?
      fi
    else
      echo "No PREHANDOVER_PROOF - running automated validation"
      ./scripts/validate-[gate].sh
      exit $?
    fi
```

---

## Evidence Completeness Validation

Script `governance/scripts/validate_evidence_based.py` MUST verify:

1. **Mode Declaration**: Explicit "Evidence-Based" mode stated
2. **Reason**: Valid reason for using evidence-based validation
3. **Method**: Verification method documented
4. **Steps**: Verification steps listed (minimum 3)
5. **Evidence**: At least one evidence artifact provided
6. **Findings**: Requirements documented with compliance status
7. **Attestation**: Agent attestation present with timestamp
8. **Confidence**: Verification confidence stated

**Exit Code**:
- 0: All evidence requirements met
- 1: Evidence incomplete or invalid

---

## Examples

### Example 1: Scope Declaration (Evidence-Based)

See "SCOPE_DECLARATION.md Requirements" section above.

### Example 2: Branch Protection Verification (Evidence-Based)

```markdown
### Gate: Branch Protection Verification

**Validation Mode**: Evidence-Based (API Verification)  
**Reason**: Requires GitHub API access not available in automated script  
**Method**: GitHub web UI inspection and API verification

**Verification Steps**:
1. Navigated to repository Settings > Branches
2. Verified main branch protection rules
3. Checked required status checks configuration
4. Verified administrator enforcement
5. Documented current configuration

**Evidence**:
- Screenshot: `evidence/branch-protection-main.png`
- API Response: `evidence/branch-protection-api.json`

**Findings**:
- ✅ Branch protection enabled: COMPLIANT
- ✅ Required status checks: COMPLIANT (3 checks configured)
- ✅ Administrator enforcement: COMPLIANT (enabled)
- ✅ Force push blocked: COMPLIANT

**Attestation**:
I attest that I have manually verified branch protection configuration through GitHub web UI and API, and all requirements are compliant.

**Date**: 2026-01-19T15:00:00Z  
**Verification Confidence**: HIGH
```

### Example 3: Builder Contract Validation (Evidence-Based)

```markdown
### Gate: Builder Contract Validation

**Validation Mode**: Evidence-Based (Manual Schema Compliance Check)  
**Reason**: Schema validation script not yet implemented  
**Method**: Manual review against builder contract schema

**Verification Steps**:
1. Opened builder contract schema definition
2. Reviewed `.github/agents/ui-builder.md` structure
3. Verified all required fields present
4. Verified YAML frontmatter validity
5. Verified markdown body structure
6. Cross-referenced with canonical template

**Evidence**:
```yaml
# Required fields verified:
- name: ui-builder ✅
- description: [present] ✅
- agent.id: ui-builder ✅
- agent.class: builder ✅
- capabilities: [listed] ✅
```

**Findings**:
- ✅ YAML frontmatter: COMPLIANT (all required fields)
- ✅ Markdown body: COMPLIANT (all sections present)
- ✅ Schema adherence: COMPLIANT
- ✅ Canonical template match: COMPLIANT

**Attestation**:
I attest that ui-builder.md complies with builder contract schema v2.0.0 and contains all required fields and sections.

**Date**: 2026-01-19T15:00:00Z  
**Verification Confidence**: HIGH
```

---

## Zero Test Debt Compatibility

Evidence-based validation MUST maintain zero-test-debt principles:

1. **100% Coverage**: All requirements MUST be verified (no partial verification)
2. **No Rationalization**: Cannot use evidence-based mode to skip requirements
3. **Higher Bar**: Evidence-based requires MORE documentation than automated
4. **Remediation**: Any non-compliance MUST be fixed (cannot be "noted" and ignored)
5. **Attestation Risk**: Agent personally attests to accuracy

**Prohibition**: Evidence-based validation CANNOT be used to circumvent gate requirements or lower standards.

---

## Migration Path

For repositories transitioning to evidence-based validation:

1. **Document Current State**: Identify which gates lack automation
2. **Create Evidence Schema**: Define evidence requirements for each gate
3. **Update Workflows**: Add evidence-based validation logic to CI
4. **Train Agents**: Ensure agents understand evidence requirements
5. **Validate First PR**: Confirm evidence-based path works end-to-end
6. **Monitor Quality**: Track evidence quality and completeness
7. **Automate Over Time**: Build automated scripts to replace evidence-based validation

**Goal**: Evidence-based validation is a bridge, not a destination. Automate when feasible.

---

## Authority & Enforcement

**Constitutional Authority**: BUILD_PHILOSOPHY.md Section II (Governance Supremacy)  
**Governance Authority**: BOOTSTRAP_EXECUTION_LEARNINGS.md (BL-027, BL-028)  
**Enforcement**: CI gates + human review  
**Non-Negotiable**: Zero test debt, no rationalization, complete documentation

---

## References

- BL-027: Scope Declaration Mandatory Before PR Handover
- BL-028: YAMLlint Warnings ARE Errors
- BOOTSTRAP_EXECUTION_LEARNINGS.md: All bootstrap learnings
- AGENT_CONTRACT_PROTECTION_PROTOCOL.md: Pre-gate validation requirements
- CI_CONFIRMATORY_NOT_DIAGNOSTIC.md: Local validation requirement

---

**END OF SCHEMA**

# Builder Training Guide - Test Execution Protocol & BL-026

**Purpose**: Guide for conducting synchronous builder training on Agent Test Execution Protocol and BL-026 Automated Deprecation Detection  
**Authority**: Governance Administrator + FM  
**Version**: 1.0.0  
**Date**: 2026-01-13  
**Target Completion**: 2026-01-27

---

## Training Overview

### Objectives

By completion, each builder will:
1. ✅ Understand CI is confirmatory, not diagnostic
2. ✅ Know how to execute tests locally before PR creation
3. ✅ Create proper PREHANDOVER_PROOF documentation
4. ✅ Understand BL-026/T0-015 constitutional status
5. ✅ Run deprecation detection and remediate violations
6. ✅ Submit signed attestations for both protocols

### Training Method

**Synchronous training session** for all 5 builders:
- ui-builder
- api-builder
- schema-builder
- integration-builder
- qa-builder

**Duration**: 1-2 hours per session  
**Format**: Interactive with practical exercises  
**Trainers**: FM + Governance Administrator

---

## Training Agenda

### Part 1: Agent Test Execution Protocol (45 min)

#### 1.1 Introduction (10 min)
- **Constitutional Authority**
  - Build Philosophy: One-Time Build Correctness
  - Zero Test Debt Constitutional Rule (T0-003)
  - Build-to-Green Enforcement (T0-011)
  
- **Core Principle**
  - CI is confirmation, NOT diagnostic
  - Tests MUST be run locally before PR
  - PREHANDOVER_PROOF is mandatory
  
- **Why This Matters**
  - Prevents test debt entering PR workflow
  - Respects reviewer time and CI resources
  - Enforces One-Time Build Correctness

#### 1.2 Protocol Requirements (15 min)

Walk through:
1. `governance/runbooks/AGENT_TEST_EXECUTION_PROTOCOL.md`
2. `.github/PULL_REQUEST_TEMPLATE.md` (PREHANDOVER_PROOF section)

**Key Points**:
- Mandatory test execution before PR
- 100% GREEN requirement (zero failures, zero warnings)
- Complete execution evidence documentation
- Attestation signature requirement

**Show Examples**:
- Good PREHANDOVER_PROOF examples
- Bad PREHANDOVER_PROOF examples (what NOT to do)
- CI failure scenarios that should have been caught locally

#### 1.3 Practical Exercise (20 min)

Each builder demonstrates:

**Exercise 1: Run Tests Locally**
```bash
# Navigate to repo
cd /path/to/maturion-foreman-office-app

# Run tests
pytest tests/ -v --strict-warnings

# Verify exit code
echo $?  # Should be 0
```

**Exercise 2: Create PREHANDOVER_PROOF**
- Document test execution
- Include commands, exit codes, timestamps
- Sign attestation

**Exercise 3: Interpret Results**
- Identify test failures
- Understand warning messages
- Know when to escalate

---

### Part 2: BL-026 Deprecation Detection (45 min)

#### 2.1 Introduction (10 min)

- **Constitutional Authority**
  - T0-015 in Tier-0 canon manifest
  - Zero Test Debt Constitutional Rule
  - Zero Warning Test Debt Doctrine
  
- **Why BL-026 Exists**
  - Deprecated APIs cause runtime failures
  - Security vulnerabilities in deprecated patterns
  - Maintenance burden on version upgrades
  - Prevention is mandatory
  
- **Constitutional Status**
  - Tier-0 requirement (T0-015)
  - CANNOT be waived
  - Violations block build-to-green

#### 2.2 Protocol Requirements (15 min)

Walk through:
1. `governance/policies/AUTOMATED_DEPRECATION_DETECTION_GATE.md`
2. Enforcement mechanisms (pre-commit hook, CI gate)

**Key Points**:
- Automatic deprecation detection via ruff
- Common violations (datetime.utcnow, typing generics)
- Auto-fix capability (with review requirement)
- Exception process (rare, requires FM approval)

**Show Examples**:
- Deprecated datetime usage
- Deprecated typing imports
- Correct modern replacements
- How to read ruff output

#### 2.3 Practical Exercise (20 min)

Each builder demonstrates:

**Exercise 1: Run Deprecation Check**
```bash
# Check for deprecated APIs
ruff check --select UP .

# Check specific domain
ruff check --select UP foreman/[domain]/

# View available fixes
ruff check --select UP --diff .
```

**Exercise 2: Interpret Results**
- Understand UP rule codes
- Identify violation severity
- Know which violations to fix first

**Exercise 3: Remediate Violations**
```bash
# Auto-fix (review required)
ruff check --select UP --fix [file.py]

# Verify fix
ruff check --select UP [file.py]

# Run tests after fix
pytest tests/[affected]/ -v
```

**Exercise 4: Exception Scenario**
- When to request exception
- How to document justification
- FM approval process

---

## Attestation Collection

### After Training Completion

Each builder submits TWO attestation files:

#### 1. Test Execution Protocol Attestation

**File**: `governance/evidence/builder-attestations/test-execution-protocol/[builder-id]-attestation.md`

**Template**:
```markdown
# Builder Agent Test Execution Protocol Attestation

**Agent**: [Builder Name]  
**Builder ID**: [builder-id]  
**Date**: 2026-01-XX

## I acknowledge and agree to:

1. ✅ CI is confirmatory, not diagnostic
2. ✅ All tests must be executed locally before PR creation
3. ✅ PREHANDOVER_PROOF is mandatory for all PRs
4. ✅ Zero test failures/warnings before handover
5. ✅ Exception process requires FM approval
6. ✅ Violations are catastrophic and block work

## I understand:

- Creating PR without local test execution is prohibited
- CI-discovered failures indicate protocol violation
- Test execution evidence is non-negotiable
- FM has authority to reject PRs lacking evidence

## Training Completion:

- ✅ Read AGENT_TEST_EXECUTION_PROTOCOL.md
- ✅ Completed practical exercises
- ✅ Demonstrated local test execution
- ✅ Created sample PREHANDOVER_PROOF

**Builder Signature**: @[builder-username]  
**Training Date**: 2026-01-XX  
**Trainer**: [FM|Governance]  
**Protocol Version**: 1.0.0

**Verified by**: [FM/Governance]  
**Verification Date**: [date]
```

#### 2. BL-026 Deprecation Attestation

**File**: `governance/evidence/builder-attestations/bl-026-deprecation/[builder-id]-attestation.md`

**Template**:
```markdown
# Builder Agent BL-026 Deprecation Detection Attestation

**Agent**: [Builder Name]  
**Builder ID**: [builder-id]  
**Date**: 2026-01-XX

## I acknowledge and agree to:

1. ✅ BL-026 is Tier-0 constitutional (T0-015)
2. ✅ Running `ruff check --select UP` before all PRs
3. ✅ Remediating all deprecated API violations
4. ✅ Zero deprecation debt is mandatory
5. ✅ Exception process requires FM approval
6. ✅ Violations constitute test debt and block build-to-green

## I understand:

- Deprecated APIs cause runtime failures
- BL-026 violations block build-to-green
- Auto-fix must be reviewed before commit
- Exception requests require strong justification
- Quarterly review of all exceptions

## Common Deprecations I Will Fix:

- ✅ datetime.utcnow() → datetime.now(timezone.utc)
- ✅ typing.Dict/List/Tuple → dict/list/tuple (Python 3.9+)
- ✅ Unnecessary 'r' mode in file operations
- ✅ All other UP rule violations

## Training Completion:

- ✅ Read AUTOMATED_DEPRECATION_DETECTION_GATE.md
- ✅ Ran ruff check --select UP
- ✅ Interpreted deprecation warnings
- ✅ Remediated sample violations
- ✅ Demonstrated auto-fix with review

**Builder Signature**: @[builder-username]  
**Training Date**: 2026-01-XX  
**Trainer**: [FM|Governance]  
**BL-026 Version**: 1.0.0

**Verified by**: [FM/Governance]  
**Verification Date**: [date]
```

---

## Verification & Approval

### FM/Governance Responsibilities

For each builder:

1. **Verify Training Completion**
   - Builder attended full training session
   - Completed all practical exercises
   - Demonstrated understanding

2. **Review Attestations**
   - Both attestation files submitted
   - Properly signed and dated
   - All checkboxes marked

3. **Update Training Records**
   - Update `training-records.json`
   - Mark status as "COMPLETE"
   - Remove task assignment block

4. **Authorize Task Assignment**
   - Builder can now receive tasks
   - Monitor first 5 PRs for compliance
   - Provide feedback on PREHANDOVER_PROOF quality

---

## Post-Training Monitoring

### First 5 PRs Review

After training, FM reviews first 5 PRs from each builder:

**Check**:
- [ ] PREHANDOVER_PROOF present and complete
- [ ] Test execution evidence documented
- [ ] BL-026 check included
- [ ] Attestation signature present
- [ ] No CI-discovered failures

**Feedback**:
- Provide constructive feedback on evidence quality
- Clarify protocol requirements if misunderstood
- Escalate repeated violations

### Quarterly Protocol Review

Every quarter:
- Review all builder attestations
- Track protocol violations
- Assess training effectiveness
- Update protocols if needed
- Collect re-attestations for major changes

---

## Training Schedule

| Date | Session | Builders | Trainer | Status |
|------|---------|----------|---------|--------|
| 2026-01-XX | Session 1 | All 5 | FM + Governance | SCHEDULED |

**Target Completion**: 2026-01-27

---

## References

- **Test Execution Protocol**: `governance/runbooks/AGENT_TEST_EXECUTION_PROTOCOL.md`
- **BL-026 Policy**: `governance/policies/AUTOMATED_DEPRECATION_DETECTION_GATE.md`
- **PR Template**: `.github/PULL_REQUEST_TEMPLATE.md`
- **Attestation Directory**: `governance/evidence/builder-attestations/`
- **Training Records**: `governance/evidence/builder-attestations/training-records.json`

---

## Contact

- **Training Questions**: FM (Foreman)
- **Governance Questions**: Governance Administrator
- **Constitutional Matters**: Johan Ras

---

**Status**: ACTIVE - Training Scheduled  
**Next Update**: After training completion

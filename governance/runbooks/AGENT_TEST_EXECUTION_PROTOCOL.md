# Agent Test Execution Protocol

**Authority**: Governance Administrator + FM  
**Version**: 1.0.0  
**Date**: 2026-01-13  
**Status**: ACTIVE - MANDATORY  
**Scope**: All agents (FM, Builders, Governance)

---

## Constitutional Authority

This protocol is a **Tier-1 Constitutional requirement** enforced by:

1. **Build Philosophy**: One-Time Build Correctness mandates pre-verified execution
2. **Zero Test Debt Constitutional Rule**: CI-discovered failures constitute test debt
3. **Build-to-Green Enforcement**: All checks must be GREEN before handover
4. **Execution Bootstrap Protocol v2.0.0+**: 7-step verification mandate

**This protocol CANNOT be waived. Exceptions require explicit FM approval.**

---

## Core Principle: CI is Confirmatory, Not Diagnostic

### The Iron Rule

**CI is confirmation, NOT diagnostic.**

- **PROHIBITED**: Creating PR and relying on CI to discover test failures
- **PROHIBITED**: Using CI as a debugging tool for test execution
- **PROHIBITED**: Handover with "tests should pass" without local verification
- **REQUIRED**: All tests executed locally and verified GREEN before PR creation
- **REQUIRED**: Complete execution evidence in PREHANDOVER_PROOF

### Rationale

CI failures discovered after PR creation indicate:
- Agent did not validate work locally
- Test debt introduced into PR workflow
- Build Philosophy violation (One-Time Build Correctness)
- Wasted CI resources and review time

**Prevention is mandatory.** Tests must be executed and verified locally before any PR.

---

## Mandatory Test Execution Requirements

### Before Creating ANY Pull Request

All agents MUST:

1. **Identify All Affected Tests**
   - Determine which test domains are affected by changes
   - Include unit tests, integration tests, domain-specific tests
   - Document test scope in work notes

2. **Execute Tests Locally**
   - Run ALL affected tests in agent environment
   - Use exact commands that CI will execute
   - Capture complete test output (stdout, stderr)
   - Record execution timestamps

3. **Verify 100% GREEN Status**
   - All tests MUST pass (exit code 0)
   - Zero test failures permitted
   - Zero warnings permitted
   - Zero skipped tests (unless documented in QA catalog)

4. **Execute Domain-Specific Checks**
   - Run linters (ruff, eslint, etc.)
   - Execute code formatting checks
   - Run type checkers (mypy, typescript)
   - Execute deprecation detection (ruff check --select UP)
   - Run any custom validation scripts

5. **Document Execution Evidence**
   - Create PREHANDOVER_PROOF document
   - Include all test commands executed
   - Include exit codes (all must be 0)
   - Include summary of test results
   - Include timestamps and commit hash

6. **Attest to GREEN Status**
   - Agent signature: "All checks GREEN on commit [hash]"
   - List all checks with ✅ status
   - Confirm CI will be confirmatory only

### Test Execution Commands by Domain

#### Python Backend Tests
```bash
# Run all tests
pytest tests/ -v

# Run specific domain
pytest tests/[domain]/ -v

# With coverage
pytest tests/ -v --cov=foreman --cov-report=term-missing

# Zero warnings requirement
pytest tests/ -v --strict-warnings
```

#### Deprecation Detection (BL-026)
```bash
# Check for deprecated APIs
ruff check --select UP .

# Check specific domain
ruff check --select UP foreman/[domain]/

# Auto-fix (review changes before committing)
ruff check --select UP --fix .
```

#### Code Quality Checks
```bash
# Ruff linting
ruff check .

# Type checking (if applicable)
mypy foreman/

# Format checking
ruff format --check .
```

#### Integration/Runtime Tests
```bash
# Foreman integration tests
pytest test-foreman-integration.py -v

# Runtime validation
python scripts/validate_runtime_[component].py
```

---

## PREHANDOVER_PROOF Requirements

### Mandatory Evidence Sections

Every PR MUST include PREHANDOVER_PROOF with:

#### 1. Test Execution Summary
```markdown
## Test Execution Evidence

**Execution Date**: 2026-01-13  
**Commit Hash**: abc123def456  
**Agent**: [Agent Name]

### Tests Executed

| Test Suite | Command | Exit Code | Status |
|------------|---------|-----------|--------|
| Unit Tests | pytest tests/unit/ -v | 0 | ✅ PASS |
| Integration Tests | pytest tests/integration/ -v | 0 | ✅ PASS |
| Deprecation Check | ruff check --select UP . | 0 | ✅ PASS |
| Linting | ruff check . | 0 | ✅ PASS |

**Total Tests**: 42  
**Passed**: 42  
**Failed**: 0  
**Warnings**: 0  
**Duration**: 23.5s
```

#### 2. Command Outputs
```markdown
## Execution Logs

### Unit Tests
```
$ pytest tests/unit/ -v
================================ test session starts =================================
...
================================ 42 passed in 15.2s =================================
```

### Deprecation Detection
```
$ ruff check --select UP .
All checks passed!
```
```

#### 3. Attestation
```markdown
## Agent Attestation

I, [Agent Name], attest that:
- ✅ All tests executed locally before PR creation
- ✅ All exit codes = 0 (SUCCESS)
- ✅ Zero test failures
- ✅ Zero warnings
- ✅ CI is confirmatory only (not diagnostic)
- ✅ Changes validated on commit abc123def456

**Agent Signature**: @[agent-username]  
**Date**: 2026-01-13T10:30:00Z
```

---

## Exception Process

### When Exceptions Are Justified

Exceptions are **rare** and only justified when:

1. **Infrastructure Failures**: CI infrastructure unavailable (agent environment works)
2. **Environmental Differences**: Genuine environment-specific behavior (must be documented)
3. **Flaky Tests**: Known test flakiness documented in QA catalog
4. **Emergency Fixes**: Critical production issues requiring immediate merge

### Exception Request Process

1. **Document Justification**
   - Create issue with `test-execution-exception` label
   - Explain why exception is needed
   - Provide evidence of local execution attempts
   - Document environmental differences
   - Propose remediation plan

2. **FM Review & Approval**
   - FM reviews technical merit
   - FM approves or rejects with rationale
   - Approval logged in `governance/evidence/test-execution-exceptions.json`
   - Exception tracked for quarterly review

3. **PR Annotation**
   ```markdown
   ## Test Execution Exception
   
   **Exception ID**: TEST-EX-001  
   **Justification**: [Detailed explanation]  
   **Approved by**: FM (2026-01-13)  
   **Remediation**: [Plan to fix]  
   **Review date**: 2026-04-13
   
   See: governance/evidence/test-execution-exceptions.json
   ```

4. **Quarterly Review**
   - All exceptions reviewed every quarter
   - Expired exceptions must be remediated or renewed
   - Renewal requires updated justification

---

## Integration with PR Workflow

### PR Template Requirements

`.github/PULL_REQUEST_TEMPLATE.md` MUST include:

- [ ] Pre-Handover Execution Evidence section
- [ ] Test execution commands and results
- [ ] BL-026 deprecation check evidence
- [ ] Agent attestation signature
- [ ] Link to PREHANDOVER_PROOF document

### CI Gate Behavior

CI gates operate as **confirmation only**:
- Validate that work already verified locally is still GREEN
- Detect environment drift or merge conflicts
- Provide public validation record
- MUST NOT be first discovery of test failures

### Failure Handling

If CI discovers failures that passed locally:

1. **STOP**: Do not proceed with merge
2. **Investigate**: Determine root cause (environment, merge conflict, flake)
3. **Document**: Update PREHANDOVER_PROOF with findings
4. **Remediate**: Fix issue and re-execute locally
5. **Re-verify**: Update PR with new evidence
6. **Escalate**: If genuinely environmental, request exception

---

## Builder Agent Requirements

### Training Requirements

All builder agents MUST:
- Complete test execution protocol training
- Sign attestation acknowledging protocol
- Demonstrate local test execution capability
- Show PREHANDOVER_PROOF creation proficiency

### Attestation Format

```markdown
# Builder Agent Test Execution Protocol Attestation

**Agent**: [Agent Name]  
**Builder ID**: [builder-id]  
**Date**: 2026-01-13

## I acknowledge and agree to:

1. ✅ CI is confirmatory, not diagnostic
2. ✅ All tests must be executed locally before PR creation
3. ✅ PREHANDOVER_PROOF is mandatory for all PRs
4. ✅ Zero test failures/warnings before handover
5. ✅ BL-026 deprecation check is mandatory
6. ✅ Exception process requires FM approval
7. ✅ Violations are catastrophic and block work

## I understand:

- Creating PR without local test execution is prohibited
- CI-discovered failures indicate protocol violation
- Test execution evidence is non-negotiable
- FM has authority to reject PRs lacking evidence

**Builder Signature**: @[builder-username]  
**Training Completed**: 2026-01-13  
**Protocol Version**: 1.0.0
```

### Training Checklist

- [ ] Read this protocol document completely
- [ ] Execute tests locally in practice environment
- [ ] Create sample PREHANDOVER_PROOF
- [ ] Complete attestation
- [ ] Submit attestation to governance/evidence/builder-attestations/

---

## Monitoring & Enforcement

### Protocol Compliance Metrics

Track quarterly:
- Number of PRs with PREHANDOVER_PROOF
- Number of PRs without PREHANDOVER_PROOF (violations)
- Number of CI failures after local GREEN attestation
- Number of exceptions granted
- Average time to PR readiness

### Violation Handling

**First Violation**: Warning + mandatory protocol re-training  
**Second Violation**: Builder suspended until re-trained  
**Third Violation**: Builder recruitment revoked

### Quarterly Review

Every quarter, review:
- Protocol effectiveness
- Exception patterns
- Training adequacy
- CI/local environment drift
- Protocol updates needed

---

## Integration with Existing Governance

### Related Documents

- **BUILD_PHILOSOPHY.md**: One-Time Build Correctness supreme authority
- **governance/canon/EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md**: 7-step verification
- **governance/policies/zero-test-debt-constitutional-rule.md**: Test debt prohibition
- **governance/policies/AUTOMATED_DEPRECATION_DETECTION_GATE.md**: BL-026 enforcement
- **governance/specs/build-to-green-enforcement-spec.md**: GREEN requirement

### Tier-0 Relationship

This protocol supports but is NOT part of Tier-0 canon. It is a **Tier-1 operational protocol** that enforces Tier-0 principles:

- Supports T0-003 (Zero Test Debt)
- Supports T0-011 (Build-to-Green)
- Supports T0-015 (BL-026 Deprecation Detection)
- Enforces EXECUTION_BOOTSTRAP_PROTOCOL v2.0.0+

---

## Summary: Agent Responsibilities

### Before EVERY Pull Request

1. ✅ Execute ALL affected tests locally
2. ✅ Verify 100% GREEN (zero failures, zero warnings)
3. ✅ Run BL-026 deprecation check
4. ✅ Run all domain-specific checks
5. ✅ Create PREHANDOVER_PROOF document
6. ✅ Include complete execution evidence
7. ✅ Sign attestation
8. ✅ Confirm CI will be confirmatory only

### NEVER

- ❌ Create PR without local test execution
- ❌ Use CI as test debugging tool
- ❌ Handover with "tests should pass"
- ❌ Skip PREHANDOVER_PROOF documentation
- ❌ Ignore warnings or failures
- ❌ Bypass protocol without FM approval

---

## References

### Canonical Governance
- **Source**: maturion-foreman-governance (this protocol establishes new requirement)
- **Authority**: Governance Administrator + FM
- **Enforcement**: PR template, agent contracts, quarterly review

### Technical References
- **pytest Documentation**: https://docs.pytest.org/
- **ruff Documentation**: https://docs.astral.sh/ruff/
- **PREHANDOVER_PROOF Template**: governance/templates/PREHANDOVER_PROOF_TEMPLATE.md

### Repository Files
- PR template: `.github/PULL_REQUEST_TEMPLATE.md`
- Agent contracts: `.github/agents/*.md`
- Evidence directory: `governance/evidence/test-execution-exceptions.json`
- Attestations: `governance/evidence/builder-attestations/`

---

## Revision History

| Version | Date | Changes | Authority |
|---------|------|---------|-----------|
| 1.0.0 | 2026-01-13 | Initial protocol creation | Governance Liaison |

---

**Status**: ACTIVE - MANDATORY  
**Next Review**: 2026-04-13 (Quarterly)  
**Contact**: FM for exceptions, Johan for constitutional matters

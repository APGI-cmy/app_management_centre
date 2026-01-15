# Build-to-Green Checklist

**Purpose**: Verify build-to-green compliance before submitting PR

**Constitutional Authority**: `BUILD_PHILOSOPHY.md` Section II.1 - One-Time Build Correctness

---

## Pre-PR Build-to-Green Verification

Before submitting your PR, verify ALL of the following:

### Pre-Implementation Behavior Review (MANDATORY for Enhancement Work)

- [ ] **Enhancement work identification completed**
  - Determined if work is enhancement (vs net-new, bug fix, or documentation)
  - Enhancement includes: feature enhancements, performance optimization, behavior modifications, API changes, schema enhancements, UI/UX improvements, refactoring with behavior impact

- [ ] **Pre-Implementation Behavior Review Protocol completed** (if enhancement work)
  - Step 1: Reviewed current implementation in detail
  - Step 2: Documented actual current behavior (GIVEN/WHEN/THEN)
  - Step 3: Identified enhancement delta (preserved/changed/new behaviors)
  - Step 4: Designed tests validating all behavior categories
  - Created Pre-Implementation Behavior Review Report
  - PRESERVE tests run against current implementation and pass
  - Report reviewed and approved by FM/Senior Builder
  - **Template**: `governance/templates/PRE_IMPLEMENTATION_BEHAVIOR_REVIEW_REPORT.template.md`
  - **Authority**: `governance/canon/PRE_IMPLEMENTATION_BEHAVIOR_REVIEW_PROTOCOL.md`

- [ ] **Exemption obtained** (if enhancement work but protocol not applicable)
  - Documented why protocol not applicable
  - Obtained explicit FM exemption in writing
  - Documented exemption rationale

### QA-to-Red Tests Now Pass

- [ ] **All QA-to-Red tests identified for this task now pass**
  - Located QA-to-Red test suite for this task
  - Ran all tests locally
  - All tests PASS (zero failures)
  - Test results captured in Builder QA Report

- [ ] **No new failing tests introduced**
  - All pre-existing passing tests still pass
  - No regressions in unrelated functionality
  - Test suite status improved or maintained (never degraded)

### Architecture Requirements Met

- [ ] **All architecture requirements for this task implemented**
  - Reviewed architecture specification for this task
  - Implemented all required components
  - No scope creep beyond assigned task
  - No architectural drift introduced

- [ ] **Architecture alignment verified**
  - No deviations from canonical architecture
  - Module boundaries respected
  - Integration contracts honored
  - Naming conventions followed

### Scope Control

- [ ] **No scope creep beyond assigned task**
  - Implemented ONLY what was specified in task
  - Did NOT add "bonus" features
  - Did NOT fix unrelated issues
  - Did NOT refactor unrelated code (unless explicitly part of task)

- [ ] **Task requirements fully met**
  - All acceptance criteria satisfied
  - All deliverables produced
  - All evidence artifacts generated
  - Task can be marked COMPLETE

### Evidence Requirements

- [ ] **Builder QA Report generated and READY**
  - Report exists at specified location
  - Report validates against schema
  - Report declares `qa_status: READY`
  - Report includes complete evidence chain

- [ ] **Evidence chain complete**
  - All required evidence artifacts present
  - All evidence artifacts schema-compliant
  - Evidence artifacts immutable (`immutable: true`)
  - Evidence chain traceable end-to-end

### Local PR Gate Validation

- [ ] **Local PR gate validation passes**
  - Ran gate validation scripts locally
  - All gates report PASS
  - No gate failures or warnings
  - Ready for CI confirmation (not discovery)

---

## Build-to-Green Principle

**Build-to-Green means**:
- Start with failing QA-to-Red tests
- Implement ONLY what makes those tests pass
- Stop when tests pass (no gold-plating)
- Verify zero regression
- Submit PR with READY status

**Build-to-Green does NOT mean**:
- ❌ Implement features not in QA-to-Red
- ❌ Add "nice to have" features
- ❌ Fix unrelated bugs
- ❌ Refactor working code unnecessarily
- ❌ Over-engineer the solution

---

## Violation Detection

If any checklist item is NOT checked, you are **NOT ready for PR**.

### What to Do

1. **STOP** - Do not submit PR
2. **Review** - Identify which requirement is not met
3. **Complete** - Finish the incomplete work
4. **Verify** - Re-check this checklist
5. **Only then submit PR**

---

## Common Build-to-Green Violations

### Scope Creep
- Implementing features beyond task specification
- Adding "improvements" not required by QA-to-Red
- Fixing bugs not related to current task

**Fix**: Remove scope creep, restore to task specification only

### Premature PR
- Submitting PR with failing tests
- Submitting PR before QA-to-Red complete
- Submitting PR with NOT_READY status

**Fix**: Complete all work, verify all tests pass, only then submit

### Incomplete Evidence
- Missing Builder QA Report
- Report with NOT_READY status
- Incomplete evidence chain

**Fix**: Generate all required evidence, verify completeness, then submit

---

## CI Role (Confirmatory Only)

**Remember**: CI confirms what you already know locally.

- ✅ If local verification passes → CI SHOULD pass
- ❌ If CI fails → You submitted prematurely OR gate infrastructure issue

**CI failure is NOT**:
- A debugging tool (debug locally first)
- A discovery mechanism (discover issues locally first)
- An iterative feedback loop (verify locally, submit once)

---

## References

- **One-Time Build Correctness**: `BUILD_PHILOSOPHY.md` Section II.1
- **Build-to-Green Gate**: `.github/workflows/build-to-green-enforcement.yml`
- **QA-to-Red Specification**: `foreman/qa/qa-to-red-spec.md` (when available)

---

**Version**: 1.0.0  
**Last Updated**: 2025-12-30

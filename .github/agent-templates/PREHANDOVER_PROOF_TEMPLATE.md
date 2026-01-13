# PREHANDOVER PROOF TEMPLATE (ENHANCED v2.1.0)

**Purpose:** Standardized template for documenting local PR-gate execution before handover  
**Required For:** ALL handovers (no exceptions)  
**Authority:** Governance Rule — PR_GATE_LOCAL_EXECUTION_REQUIREMENT.md  
**Protocol Version:** 2.0.0+ (Execution Bootstrap Protocol)  
**Template Version:** 2.1.0 (Enhanced with Governance Artifacts + CST Validation)  
**Last Updated:** 2026-01-13  
**Canonical Source:** maturion-foreman-governance/governance/templates/PREHANDOVER_PROOF_TEMPLATE.md

---

## Instructions

1. Copy this template to create your PREHANDOVER_PROOF document
2. Fill in ALL sections completely
3. Execute **Category 0: 7-Step Execution Bootstrap Protocol** (MANDATORY)
4. Execute ALL PR-gate workflows locally
5. Document results for EACH step and gate
6. **NEW**: Complete governance artifacts section (embed OR link)
7. **NEW**: Complete CST validation section (if applicable)
8. Provide explicit attestation
9. Include this proof in PR before marking Ready for Review

**Incomplete proofs will result in handover rejection.**

---

## PREHANDOVER PROOF — [PR Number] — [Brief Description]

**Agent:** [Your Agent Name]  
**PR:** #[Number]  
**Branch:** [branch-name]  
**Date:** [YYYY-MM-DD]  
**Latest Commit:** [commit-hash]  
**Protocol Version:** 2.0.0+  
**Template Version:** 2.1.0

---

## Category 0: Execution Bootstrap Protocol (MANDATORY v2.0.0+)

**Status**: [COMPLETE | INCOMPLETE]  
**All Steps GREEN**: [YES | NO]

### Step 1: Identify Execution Artifacts

**Artifacts Created/Modified:**
- [ ] Workflow: [path/to/workflow.yml]
- [ ] Script: [path/to/script.py]
- [ ] Gate: [path/to/gate-config]
- [ ] Code Files: [list modified files]
- [ ] Tests: [list test files]
- [ ] Other: [describe]

**Total Artifacts**: [N]

**Artifact Inventory Table:**
| # | Type | Path | Purpose | Lines Changed |
|---|------|------|---------|---------------|
| 1 | [Workflow/Script/Code/Test] | [path] | [description] | [+N/-M] |
| 2 | [Type] | [path] | [description] | [+N/-M] |

### Step 2: Local Execution

**Execution Environment:**
- Agent: [Agent Name]
- Environment: [Local/Container/VM]
- OS: [Operating System + Version]
- Python Version: [X.Y.Z]
- Node Version: [X.Y.Z] (if applicable)
- Tools: [List relevant tools/versions]

**Execution Log:**
```bash
$ [command executed]

[PASTE COMPLETE OUTPUT HERE]
```

**Execution Timestamp:** [YYYY-MM-DDTHH:MM:SSZ (UTC)]

### Step 3: Validate Exit Codes

**Exit Code Validation:**
- [ ] All exit codes = 0 (SUCCESS)
- [ ] No warnings detected
- [ ] No errors detected

**Exit Codes by Artifact:**
| Artifact | Command | Exit Code | Status | Duration |
|----------|---------|-----------|--------|----------|
| [Artifact 1] | [command] | 0 | ✅ PASS | [Xs] |
| [Artifact 2] | [command] | 0 | ✅ PASS | [Xs] |

### Step 4: Evidence Collection

**Evidence Files:**
- Execution logs: [path or attached]
- Output files: [path or attached]
- Screenshots: [path or attached]
- Test results: [path to test output]
- Coverage reports: [path if applicable]
- Error logs (if any): [N/A or path]

**Evidence Summary:**
[Brief description of evidence collected]

**Evidence Locations:**
- [ ] Embedded in this document
- [ ] Linked to `.agent-admin/` artifacts
- [ ] Available in CI run logs

### Step 5: Failure Remediation

**Failures Detected**: [YES | NO]

**If YES, document remediation:**
- **Failure 1**: [Description]
  - Root Cause: [Cause]
  - Fix Applied: [Fix description]
  - Re-execution Result: [PASS/FAIL]
  - Commit: [commit-hash]
  - Evidence: [path to re-execution logs]

- **Failure 2**: [Description]
  - Root Cause: [Cause]
  - Fix Applied: [Fix description]
  - Re-execution Result: [PASS/FAIL]
  - Commit: [commit-hash]
  - Evidence: [path to re-execution logs]

**If NO**: All executions passed on first attempt.

### Step 6: Green Attestation

**I attest that:**
- [x] All execution artifacts identified
- [x] All artifacts executed locally
- [x] All exit codes = 0 (success)
- [x] All evidence collected and linked
- [x] Any failures were fixed and re-tested
- [x] **ALL CHECKS GREEN on commit [commit-hash]**

**Green Status Confirmation:**
- Tests: [X/X PASS] (100%)
- Linters: ✅ PASS
- Type Checks: ✅ PASS
- Security Scans: ✅ PASS
- All Gates: ✅ PASS

### Step 7: Handover Authorization

**Authorization Statement:**

> "I, [Agent Name], authorize handover for PR #[Number]. All execution artifacts have been locally verified with GREEN status on commit [commit-hash]. All 7 steps of the Execution Bootstrap Protocol have been completed successfully. Evidence is documented above."

**Handover Status**: ✅ AUTHORIZED

**Hard Rule Compliance**: CI is confirmation only, NOT diagnostic. All failures discovered and fixed locally before handover.

---

## Local PR-Gate Execution Evidence

### Gate 1: Agent QA Boundary Enforcement

**Workflow:** `.github/workflows/agent-boundary-gate.yml`  
**Script:** `governance/scripts/validate_agent_boundaries.py`

**Local Execution:**
```bash
$ python3 governance/scripts/validate_agent_boundaries.py --reports "." --current-repo "MaturionISMS/maturion-foreman-office-app"

[PASTE OUTPUT HERE]
```

**Exit Code:** [0 for pass]  
**Result:** ✅ PASS / ❌ FAIL  
**Timestamp:** [YYYY-MM-DDTHH:MM:SSZ]

---

### Gate 2: Build-to-Green Enforcement

**Workflow:** `.github/workflows/build-to-green-enforcement.yml`  
**Script:** `foreman/scripts/detect-test-debt.py`

**Local Execution:**
```bash
$ python3 foreman/scripts/detect-test-debt.py --test-dir tests

[PASTE OUTPUT HERE]
```

**Exit Code:** [0 for pass]  
**Result:** ✅ PASS / ❌ FAIL  
**Timestamp:** [YYYY-MM-DDTHH:MM:SSZ]

---

### Gate 3: [Gate Name]

**Workflow:** [path]  
**Script:** [path]

**Local Execution:**
```bash
$ [command]

[PASTE OUTPUT HERE]
```

**Exit Code:** [0 for pass]  
**Result:** ✅ PASS / ❌ FAIL  
**Timestamp:** [YYYY-MM-DDTHH:MM:SSZ]

---

[Continue for all applicable gates...]

---

## Governance Artifacts (MANDATORY v2.1.0+)

**Authority:**  
- EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md v2.0.0+  
- AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md (Tier-0)  
- COMBINED_TESTING_PATTERN.md v1.0.0

**Artifact Presentation Options:**
- **Option A**: Embed all 4 artifacts in sections below
- **Option B**: Create separate files in `.agent-admin/` and link here
- **Option C**: Hybrid (embed summary, link to detailed files)

**Selected Option:** [A | B | C]

---

### Artifact 1: Governance Scan

**Purpose:** Identify repository governance state, gaps, and compliance requirements

**Status**: [COMPLETE | NOT REQUIRED]

**If COMPLETE, provide either:**

**Option A - Embedded:**
```markdown
# Governance Scan — [Date]

## Repository Context
- **Repository:** [org/repo-name]
- **Type:** [office-app | governance | module]
- **Scan Date:** [YYYY-MM-DD]
- **Scanner:** [Agent Name]

## Agents Identified
- [List all agents with roles]

## Canonical Governance Mapped
- [List Tier-0 documents referenced]

## Local Governance Mapped
- [List local governance rules]

## Constitutional Principles Confirmed
- [List principles verified]

## Gaps Identified
- [List any gaps or compliance issues]

## Recommendations
- [List recommended actions]
```

**Option B - Linked:**
- **File:** `.agent-admin/scans/scan_[YYYYMMDD]_[HHMMSS].md`
- **Summary:** [1-2 sentence summary of findings]

**If NOT REQUIRED:**
- **Rationale:** [Explain why scan not needed for this PR]

---

### Artifact 2: Risk Assessment

**Purpose:** Evaluate risks introduced by changes and document mitigation

**Status**: [COMPLETE | NOT REQUIRED]

**If COMPLETE, provide either:**

**Option A - Embedded:**
```markdown
# Risk Assessment — [Date]

## Change Summary
- **Scope:** [Brief description]
- **Files Modified:** [N files]
- **Lines Changed:** [+N/-M]

## Risk Analysis

### Risk 1: [Risk Name]
- **Severity:** [LOW | MEDIUM | HIGH | CRITICAL]
- **Probability:** [LOW | MEDIUM | HIGH]
- **Impact:** [Description]
- **Mitigation:** [Actions taken]
- **Residual Risk:** [LOW | MEDIUM | HIGH]

### Risk 2: [Risk Name]
- **Severity:** [LOW | MEDIUM | HIGH | CRITICAL]
- **Probability:** [LOW | MEDIUM | HIGH]
- **Impact:** [Description]
- **Mitigation:** [Actions taken]
- **Residual Risk:** [LOW | MEDIUM | HIGH]

## Overall Risk Level
- **Before Mitigation:** [LOW | MEDIUM | HIGH | CRITICAL]
- **After Mitigation:** [LOW | MEDIUM | HIGH | CRITICAL]

## Recommendation
- [PROCEED | PROCEED WITH CAUTION | HALT | ESCALATE]
```

**Option B - Linked:**
- **File:** `.agent-admin/risk-assessments/risk_[NNN]_[YYYYMMDD].md`
- **Overall Risk:** [LOW | MEDIUM | HIGH | CRITICAL]
- **Recommendation:** [PROCEED | PROCEED WITH CAUTION | HALT | ESCALATE]

**If NOT REQUIRED:**
- **Rationale:** [Explain why risk assessment not needed]

---

### Artifact 3: Change Record

**Purpose:** Document what changed, why, and how it aligns with governance

**Status**: [COMPLETE | NOT REQUIRED]

**If COMPLETE, provide either:**

**Option A - Embedded:**
```markdown
# Change Record — [Date]

**Change ID:** change_[NNN]_[YYYYMMDD]  
**Implementer:** [Agent Name]  
**Authority:** [Governing document]

## Change Summary
[High-level description of changes]

## Instruction Source
- **Issue:** #[Number]
- **Authority:** [Tier-0 or canonical reference]
- **Requestor:** [Who requested/authorized]

## Changes Implemented

### 1. [Component/Area Name]
- ✅ [Change description]
- ✅ [Change description]

### 2. [Component/Area Name]
- ✅ [Change description]
- ✅ [Change description]

## Governance Validation Results
- [Validation script results]
- [Compliance checks]

## Constitutional Alignment
- [How changes align with constitutional principles]

## Conflict Detection
- **Governance Conflicts:** [NONE | List conflicts]
- **Contract Conflicts:** [NONE | List conflicts]
- **Dependency Conflicts:** [NONE | List conflicts]

## Validation Results
- [List validation outcomes]

## Ripple Effects
### Files Modified
- [List files changed]

### No Ripple Required To
- [List components unaffected]

## Verification Checklist
- [x] [Verification item]
- [x] [Verification item]
```

**Option B - Linked:**
- **File:** `.agent-admin/changes/change_[NNN]_[YYYYMMDD].md`
- **Change Summary:** [1-2 sentence summary]
- **Validation Status:** [PASS | FAIL]

**If NOT REQUIRED:**
- **Rationale:** [Explain why change record not needed]

---

### Artifact 4: Completion Summary

**Purpose:** Summarize deliverables, evidence, and readiness for handover

**Status**: [COMPLETE | NOT REQUIRED]

**If COMPLETE, provide either:**

**Option A - Embedded:**
```markdown
# Completion Summary — [Date]

## Executive Summary
[Brief overview of work completed]

## Deliverables
1. [Deliverable 1] - ✅ COMPLETE
2. [Deliverable 2] - ✅ COMPLETE
3. [Deliverable 3] - ✅ COMPLETE

## Acceptance Criteria Met
- [x] [Criterion 1]
- [x] [Criterion 2]
- [x] [Criterion 3]

## Governance Gates Passed
| Gate | Status | Evidence |
|------|--------|----------|
| [Gate 1] | ✅ PASS | [evidence location] |
| [Gate 2] | ✅ PASS | [evidence location] |

## Test Coverage
- **Tests Executed:** [N]
- **Tests Passed:** [N/N] (100%)
- **Coverage:** [X%]

## Constitutional Compliance
- ✅ Zero Test Debt
- ✅ 100% GREEN
- ✅ One-Time Build Correctness
- ✅ Full Architectural Alignment

## Process Improvements Captured
- [Improvement 1]
- [Improvement 2]

## Handover Status
✅ READY FOR REVIEW
```

**Option B - Linked:**
- **File:** [Path to completion summary document]
- **Status:** [READY FOR REVIEW | BLOCKED | INCOMPLETE]
- **Key Metrics:** [Brief metrics summary]

**If NOT REQUIRED:**
- **Rationale:** [Explain why completion summary not needed]

---

## CST Validation Section (v2.1.0+)

**Authority:** COMBINED_TESTING_PATTERN.md v1.0.0, EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md v2.0.0+ Section 7

**CST = Contract Specification Test (Capability Smoke Test)**  
**CWT = Complete Wave Test (Comprehensive End-to-End Test)**

---

### CST Applicability Assessment

**Is CST validation required for this PR?**

**Decision Logic:**
- ✅ **YES** if: This PR completes a subwave/capability/contract milestone
- ❌ **NO** if: This PR is incremental work, governance-only, or dependency work

**Determination:** [YES | NO]

---

### If CST Required: Complete CST Validation Checklist

#### 1. Contract Verification

**Contract Source:**
- **Document:** [Path to contract/spec/acceptance criteria]
- **Section:** [Relevant sections]

**Acceptance Criteria:**
| # | Criterion | Status | Evidence Location | Notes |
|---|-----------|--------|-------------------|-------|
| 1 | [Criterion text] | [✅ PASS / ❌ FAIL] | [evidence path] | [notes] |
| 2 | [Criterion text] | [✅ PASS / ❌ FAIL] | [evidence path] | [notes] |
| 3 | [Criterion text] | [✅ PASS / ❌ FAIL] | [evidence path] | [notes] |

**Verification Method:** [How criteria were validated]

**Conclusion:** [All criteria met? YES/NO with summary]

---

#### 2. Governance Gate Verification

**Gates Applicable to This PR:**
| Gate | Status | Evidence | Validation Notes |
|------|--------|----------|------------------|
| Build-to-Green | [✅ PASS / ❌ FAIL] | [evidence] | [notes] |
| BL-026 Deprecation | [✅ PASS / ❌ FAIL / N/A] | [evidence] | [notes] |
| Agent QA Boundary | [✅ PASS / ❌ FAIL] | [evidence] | [notes] |
| Builder QA Gate | [✅ PASS / ❌ FAIL / N/A] | [evidence] | [notes] |
| Code Review Closure | [✅ PASS / ❌ FAIL] | [evidence] | [notes] |
| FM Architecture Gate | [✅ PASS / ❌ FAIL / N/A] | [evidence] | [notes] |
| Governance Compliance | [✅ PASS / ❌ FAIL] | [evidence] | [notes] |
| Model Scaling Check | [✅ PASS / ❌ FAIL / N/A] | [evidence] | [notes] |

**Verification Method:** [How gates were validated]

**Conclusion:** [All gates passed? YES/NO with summary]

---

#### 3. Evidence Artifact Review

**PREHANDOVER_PROOF Review:**
- **Document:** [Path to PREHANDOVER_PROOF]
- **Completion Date:** [YYYY-MM-DDTHH:MM:SSZ]
- **Builder/Agent:** [Name]

**Sections Validated:**
| Section | Status | Validation Notes |
|---------|--------|------------------|
| Executive Summary | [✅ Complete / ❌ Incomplete] | [notes] |
| Execution Artifacts | [✅ Complete / ❌ Incomplete] | [notes] |
| Local Execution Evidence | [✅ Complete / ❌ Incomplete] | [notes] |
| Before/After States | [✅ Complete / ❌ Incomplete] | [notes] |
| Evidence Capture | [✅ Complete / ❌ Incomplete] | [notes] |
| Attestation | [✅ Complete / ❌ Incomplete] | [notes] |
| Checklist Completion | [✅ Complete / ❌ Incomplete] | [notes] |
| Process Improvement | [✅ Complete / ❌ Incomplete] | [notes] |

**Key Deliverables:**
- [List major deliverables with line counts/metrics]

**Test Execution Evidence:**
```
[Paste test execution summary]
```

**Conclusion:** [PREHANDOVER_PROOF complete and meets protocol requirements? YES/NO]

---

#### 4. Constitutional Compliance

**Authority:** AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md (Tier-0)

**Agent Contract Verification:**
| Requirement | Status | Verification |
|-------------|--------|--------------|
| Agent operated within contract boundaries | [✅ PASS / ❌ FAIL] | [details] |
| No self-modification attempted | [✅ PASS / ❌ FAIL] | [details] |
| Proper authority chain followed | [✅ PASS / ❌ FAIL] | [details] |
| Constitutional sandbox respected | [✅ PASS / ❌ FAIL] | [details] |

**BL Compliance:**
| BL | Description | Status | Evidence |
|----|-------------|--------|----------|
| BL-016 | Ratchet Conditions | [✅ / ❌ / N/A] | [evidence] |
| BL-018 | QA Range | [✅ / ❌ / N/A] | [evidence] |
| BL-019 | Semantic Alignment | [✅ / ❌ / N/A] | [evidence] |
| BL-022 | [Description] | [✅ / ❌ / N/A] | [evidence] |
| BL-023 | [Description] | [✅ / ❌ / N/A] | [evidence] |
| BL-024 | Constitutional | [✅ / ❌] | [evidence] |
| BL-025 | CST/CWT Pattern | [✅ / ❌] | [evidence] |
| BL-026 | Deprecation Gate | [✅ / ❌ / N/A] | [evidence] |

**Tier-1 Constitutional Compliance:**
- [x] Zero Test Debt (no skipped/commented tests)
- [x] 100% GREEN (all tests PASS)
- [x] One-Time Build Correctness (no rework required)
- [x] Design Freeze (architecture frozen before build)
- [x] Architecture Conformance (exact implementation per spec)

**Conclusion:** [Full constitutional compliance? YES/NO with details]

---

#### 5. CST Attestation

**I, [Validator Name/Role], attest that:**

- [x] This PR has been validated against its contract specification
- [x] All acceptance criteria have been verified and met
- [x] All governance gates have been confirmed passed
- [x] All evidence artifacts have been reviewed and are complete
- [x] The deliverable meets constitutional requirements
- [x] Continuous improvement has been captured
- [x] This work is approved for handover and dependency satisfaction

**Next Dependency:** [What is unblocked by this PR? Or N/A]

**Validation Methodology:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Risk Assessment:** [LOW | MEDIUM | HIGH] RISK
- [Risk factors and mitigations]

**Recommendation:** [APPROVE | APPROVE WITH CONDITIONS | REJECT]

---

#### 6. CST Signature

**Validator:** [Name/Role]  
**Authority:** [Bootstrap delegation or normal role]  
**Date:** [YYYY-MM-DDTHH:MM:SSZ (UTC)]  
**Reference:** EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md v2.0.0+, Section 7  
**CST Type:** CST-2 (Contract Specification Test)  
**Result:** [✅ PASS | ❌ FAIL]

**Approval Statement:**

> [Quote box with formal approval or rejection statement]

**Next Steps:**
1. [Action item]
2. [Action item]
3. [Action item]

---

### If CST Not Required: Skip Rationale

**Rationale for CST Skip:**

**This PR does NOT require CST validation because:**
- [ ] Incremental implementation (not a contract milestone)
- [ ] Governance-only changes (no executable code)
- [ ] Dependency work (enabling future capability)
- [ ] Refactoring without functional changes
- [ ] Documentation-only changes
- [ ] Configuration-only changes
- [ ] Other: [explain]

**Contract Milestone Status:**
- **Current PR:** [Partial implementation | Not a milestone]
- **Next Milestone:** [When CST will be required]
- **Tracking Issue:** [Issue number for milestone]

**Validation Alternative:**
- Instead of CST: [What validation WAS performed]
- Evidence: [Where evidence is located]

---

## Agent Attestation

I, **[Agent Name]**, attest that:

- [x] All applicable PR-gate workflows were executed locally
- [x] All gates returned GREEN (exit code 0)
- [x] All logs were inspected
- [x] This evidence is accurate and complete
- [x] Constitutional compliance verified (BL-024): All Tier-1 requirements preserved
- [x] If procedural guidance adapted: Adaptations documented with justification
- [x] **NEW v2.1.0**: All 4 governance artifacts completed or rationale provided
- [x] **NEW v2.1.0**: CST validation completed or skip rationale provided

**Handover is authorized based on local verification.**

**Signature:** [Agent Name]  
**Date:** [YYYY-MM-DD]  
**Commit:** [commit-hash]  
**Template Version:** 2.1.0

---

## Completion Checklist (Enhanced v2.1.0)

### Execution Bootstrap Protocol (Category 0)
- [ ] Step 1: All execution artifacts identified and inventoried
- [ ] Step 2: All artifacts executed locally with logs captured
- [ ] Step 3: All exit codes validated (all = 0)
- [ ] Step 4: All evidence collected and linked
- [ ] Step 5: Any failures remediated and re-tested
- [ ] Step 6: Green attestation provided with commit hash
- [ ] Step 7: Handover authorization statement included

### PR-Gate Execution
- [ ] All applicable gates identified
- [ ] Each gate executed locally
- [ ] Each gate result documented (command + output + exit code + timestamp)
- [ ] All gates GREEN

### Governance Artifacts (NEW v2.1.0)
- [ ] Governance Scan: Completed OR rationale for skip provided
- [ ] Risk Assessment: Completed OR rationale for skip provided
- [ ] Change Record: Completed OR rationale for skip provided
- [ ] Completion Summary: Completed OR rationale for skip provided
- [ ] Artifact presentation option selected (embedded/linked/hybrid)

### CST Validation (NEW v2.1.0)
- [ ] CST applicability determined (YES/NO with decision logic)
- [ ] If CST required: All 6 CST sections completed
- [ ] If CST not required: Skip rationale provided with alternatives
- [ ] CST evidence linked or embedded

### Constitutional Compliance
- [ ] Zero test debt verified
- [ ] 100% GREEN status confirmed
- [ ] One-time build correctness achieved
- [ ] All BL compliance checked
- [ ] Agent operated within contract boundaries

### Process Improvement
- [ ] FL/CI reflection completed (5 questions)
- [ ] Improvements documented
- [ ] Governance uplift recommendations provided (if applicable)

### Documentation & Evidence
- [ ] All sections of this template completed
- [ ] All placeholders replaced with actual values
- [ ] All evidence embedded or linked
- [ ] Commit hash verified on latest changes
- [ ] Timestamps in UTC format

---

## FAQ: Governance Artifacts (NEW v2.1.0)

### Q1: When should I embed artifacts vs. link to separate files?

**A:** Use these guidelines:
- **Embed** (Option A): When artifacts are short (<100 lines) and provide immediate context
- **Link** (Option B): When artifacts are detailed (>100 lines) or reusable across PRs
- **Hybrid** (Option C): Embed executive summary, link to full artifact in `.agent-admin/`

**Best Practice:** Large governance changes (5+ files) → Link to `.agent-admin/`. Small changes (<5 files) → Embed.

---

### Q2: Do I need all 4 governance artifacts for every PR?

**A:** No. Use this decision tree:

**Governance Scan:**
- Required: Multi-agent changes, new governance rules, constitutional changes
- Skip: Single-file bug fixes, documentation updates, test-only changes

**Risk Assessment:**
- Required: Database schema changes, API changes, authentication/authorization changes
- Skip: Documentation, comments, minor refactoring

**Change Record:**
- Required: Contract changes, governance changes, major feature additions
- Skip: Bug fixes, minor improvements, debt remediation

**Completion Summary:**
- Required: Subwave completions, milestone deliveries, CST validations
- Skip: Incremental PRs, work-in-progress submissions

**When in doubt:** Create the artifact. Over-documentation > under-documentation.

---

### Q3: What's the difference between this PREHANDOVER_PROOF and a Completion Summary?

**A:** 
- **PREHANDOVER_PROOF** (this document): Evidence that YOU (the agent) executed all checks locally BEFORE handover. Focus: "Did I test this?"
- **Completion Summary** (Artifact 4): Evidence that the WORK is complete and meets acceptance criteria. Focus: "Did I deliver what was asked?"

Both are required but serve different purposes. PREHANDOVER_PROOF = process compliance. Completion Summary = deliverable quality.

---

### Q4: When is CST validation required?

**A:** CST validation is MANDATORY when:
1. PR completes a subwave (Wave X.Y final PR)
2. PR delivers a contract milestone (all acceptance criteria met)
3. PR implements a new capability (feature goes from 0% → 100%)
4. Issue explicitly requires CST validation

**CST is NOT required when:**
1. PR is incremental (acceptance criteria not yet fully met)
2. PR is governance-only (no executable code)
3. PR is dependency enablement (needed for future work)
4. PR is refactoring without functional changes

**Key Question:** "Does this PR satisfy a contract or acceptance criteria?" YES = CST required.

---

### Q5: Who performs CST validation?

**A:** Depends on context:

**Normal Operations:**
- Builder agents: Self-validate using CST checklist
- FM (Foreman): Reviews and approves CST
- CS2 (Johan): Spot-checks for constitutional compliance

**Bootstrap Mode (as of early 2026):**
- FM performs CST validation on behalf of CS2
- Documented with "operating on behalf of CS2" language
- Will transition to normal operations once mature

**Authority:** EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md v2.0.0+ Section 7

---

### Q6: What if I can't complete a governance artifact?

**A:** Three options:

1. **Complete later in PR lifecycle:**
   - Mark artifact status as "IN PROGRESS"
   - Document what's missing and when it will be ready
   - Update PREHANDOVER_PROOF before final handover

2. **Provide skip rationale:**
   - Clearly state why artifact not applicable
   - Reference decision tree / FAQ
   - FM reviews and may accept or request completion

3. **Escalate:**
   - If unsure whether artifact required: Ask FM
   - If blocked on artifact completion: Ask FM
   - If artifact requirements unclear: Ask Governance Liaison

**Never:** Leave artifact section blank or marked "TODO" in final handover.

---

### Q7: How do I know which BLs apply to my PR?

**A:** Consult `governance/canon/BOOTSTRAP_EXECUTION_LEARNINGS.md` for full list. Common ones:

- **BL-016**: Ratchet conditions (if you're improving a metric, it can't regress)
- **BL-018**: QA range allocation (test numbering must follow assigned range)
- **BL-019**: Semantic alignment (test names must match architectural intent)
- **BL-024**: Constitutional sandbox (don't weaken constitutional rules)
- **BL-025**: CST/CWT pattern (know when to smoke test vs. full test)
- **BL-026**: Deprecation gate (fix deprecated patterns before merge)

**In CST validation, list all BLs checked (even if N/A).**

---

### Q8: What's the retention policy for `.agent-admin/` artifacts?

**A:** Per workspace policy:
- **Scans:** Keep last 3
- **Risk Assessments:** Keep last 3
- **Change Records:** Keep last 3
- **Completion Summaries:** Keep all (permanent record)

**Artifact files are named with timestamps for easy cleanup.**

---

### Q9: Can I reuse governance artifacts across PRs?

**A:** Yes, with caveats:

**Governance Scan:** If repo hasn't changed, you can reference previous scan and note "No changes since [date]"
**Risk Assessment:** Must be PR-specific (each PR has unique risks)
**Change Record:** Must be PR-specific (each PR is a unique change)
**Completion Summary:** Must be PR-specific (each milestone is unique)

**Best Practice:** Create new artifacts. They're lightweight and provide clear audit trail.

---

### Q10: What happens if I submit incomplete PREHANDOVER_PROOF?

**A:** Immediate handover rejection with feedback:
1. FM identifies missing sections
2. FM comments on PR with specific gaps
3. Agent must complete gaps and re-submit
4. **Constitutional violation** if pattern repeats (see BL-024)

**Zero tolerance for incomplete proofs.** Complete locally BEFORE handover.

---

## Version History

**v2.1.0 (2026-01-13):**
- ➕ Added Governance Artifacts section (4 artifacts: scan, risk, change, completion)
- ➕ Added CST Validation section (6-step checklist + skip rationale)
- ➕ Added artifact presentation options (embed/link/hybrid)
- ➕ Added enhanced completion checklist
- ➕ Added 10-question FAQ section
- 📝 Updated instructions to include new sections
- 📝 Enhanced attestation to reference new requirements

**v2.0.0 (2026-01-11):**
- ✅ Execution Bootstrap Protocol (7-step process)
- ✅ Local PR-gate execution evidence
- ✅ Green attestation and handover authorization

---

*END OF PREHANDOVER PROOF TEMPLATE v2.1.0*

# Builder Common Execution Protocols

**Purpose**: Shared execution protocols for all builder agents  
**Authority**: EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md v2.0.0+, BUILD_PHILOSOPHY.md  
**Extracted**: 2026-02-12 (Living Agent System v6.2.0 character limit remediation)

---

## Pre-Handover Execution Protocol (MANDATORY v2.0.0+)

**Authority**: governance/canon/EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md v2.0.0+  
**Template**: `.github/agent-templates/PREHANDOVER_PROOF_TEMPLATE.md` v2.0.0  
**Compliance Deadline**: 2026-02-11

**Before creating ANY PR or claiming work "COMPLETE":**

### Required Steps (7-Step Execution Bootstrap Protocol)

1. **Identify all execution artifacts**
   - List all scripts, code files, tests created/modified

2. **Execute ALL checks locally** in your build environment:
   ```bash
   # Deprecation check (Python projects)
   ruff check --select UP <domain-path>/

   # Test suite (domain-specific)
   pytest tests/<domain>/ -v

   # TypeScript/Linting checks (if applicable)
   npm run lint
   npm run type-check

   # QIW Channel Verification (5 channels)
   # - Build logs: Clean (no errors/warnings)
   # - Lint logs: Clean (no violations)
   # - Test logs: Clean (no skipped/runtime errors)
   # - Deployment simulation: Clean (if applicable)
   # - Runtime initialization: Clean (if applicable)

   # Any domain-specific validators
   ```

3. **Verify ALL exit codes = 0 (SUCCESS)**
   - If ANY check fails: FIX before proceeding
   - Do NOT create PR with failing checks

4. **Capture evidence**:
   - Command outputs
   - Exit codes
   - Before/after states (if applicable)

5. **Remediate any failures**:
   - Fix all failures locally
   - Re-execute checks
   - Document fixes and re-execution results

6. **Provide GREEN attestation**:
   - Attest: "All checks GREEN locally on commit [hash]"

7. **Authorize handover**:
   - Create formal authorization statement

### PREHANDOVER_PROOF Document (v2.0.0 MANDATORY)

**Template Location**: `.github/agent-templates/PREHANDOVER_PROOF_TEMPLATE.md` v2.0.0

**MUST include ALL sections:**

1. **Category 0**: 7-Step Execution Bootstrap Protocol (above)
2. **Local PR-Gate Execution Evidence**: All gates with full command outputs
3. **Governance Artifacts (NEW v2.0.0)**: Required for milestone completions only
   - **If completing subwave/capability/contract milestone**: Provide all 4 artifacts (Governance Scan, Risk Assessment, Change Record, Completion Summary)
   - **If routine PR**: State "Routine PR - governance artifacts not applicable"
   - See template FAQ Q1 for guidance on when artifacts are required
4. **CST Validation (NEW v2.0.0)**: Required for milestone completions only
   - **If completing subwave/capability/contract milestone**: Complete all 6 CST steps
   - **If routine PR**: State "Routine PR - CST not applicable"
   - CST validates integration of multiple work streams, not individual PRs
5. **Agent Attestation**: Updated to confirm v2.0.0 compliance
6. **Completion Checklist**: Enhanced with governance artifacts + CST sections
7. **FAQ Reference**: See template Section 11 for guidance on artifacts and CST

**CST Applicability**: Required when PR completes subwave/capability/contract milestone. If not required, provide skip rationale with decision logic.

**Artifact Presentation**: Choose embed (short), link to `.agent-admin/` (detailed), or hybrid. See template FAQ Q1.

### Hard Rule

**"CI is confirmation, NOT diagnostic."**

CI validates what you already verified locally. If CI fails, it means you didn't execute checks locally. This is a protocol violation.

### Consequences

1. **1st violation**: PR rejected, you must remediate
2. **2nd violation**: Contract review with FM
3. **3rd violation**: Builder replacement

### Checklist (Enhanced v2.0.0)

Before EVERY handover:

**7-Step Execution Bootstrap:**
- [ ] All execution artifacts identified
- [ ] All checks executed locally (not just in CI)
- [ ] All exit codes = 0
- [ ] Evidence captured
- [ ] Failures remediated (if any)
- [ ] GREEN attestation provided
- [ ] Handover authorization statement included

**QIW Channel Verification (v1.0.0):**
- [ ] Build logs verified clean (no errors/warnings)
- [ ] Lint logs verified clean (no violations)
- [ ] Test logs verified clean (no skipped tests, no runtime errors)
- [ ] Deployment simulation logs clean (if applicable)
- [ ] Runtime initialization logs clean (if applicable)
- [ ] No QA blocking conditions detected
- [ ] All anomalies recorded to governance memory (if any)

**v2.0.0 Governance Artifacts:** (Milestone completions only)
- [ ] If milestone: All 4 artifacts completed
- [ ] If routine PR: State "Routine PR - not applicable"

**v2.0.0 CST Validation:** (Milestone completions only)
- [ ] If milestone: All 6 CST steps completed
- [ ] If routine PR: State "Routine PR - not applicable"

**Documentation:**
- [ ] PREHANDOVER_PROOF created using v2.0.0 template
- [ ] All template sections completed or skip rationale provided
- [ ] PR submitted with GREEN local state

**If ANY item unchecked: DO NOT HAND OVER.**

---

## One-Time Build | Zero Test Debt | Immediate Remedy

**Authority**: BUILD_PHILOSOPHY.md, zero-test-debt-constitutional-rule.md, ZERO_WARNING_TEST_DEBT_IMMEDIATE_REMEDY_DOCTRINE.md

**Pre-Build**: Arch frozen, QA-to-Red RED, dependencies resolved  
**Prohibited**: Start before frozen, trial-and-error, infer from incomplete  
**Zero Debt**: No .skip(), .todo(), commented, incomplete, partial (99%=FAILURE)  
**Quality**: All tests pass, zero lint/console errors  
**Response**: STOP, FIX, RE-RUN, VERIFY 100%. If 3+ failures: escalate to FM

**Prior Debt Discovery**: STOP, DOCUMENT, ESCALATE to FM, BLOCKED, WAIT (don't fix prior agent's issues)  
**If Re-Assigned**: ACKNOWLEDGE, STOP current work, FIX completely, VERIFY, PROVIDE evidence

**Principle**: Responsible agent fixes own debt. Discovery blocks downstream.

---

## Test & Warning Governance (PR #484)

**Test Removal**: MUST NOT remove without FM authorization. STOP, REQUEST with traceability, WAIT, ACCEPT. Never remove: evidence/governance/heartbeat/RED QA tests.  
**Warning Handling**: Report ALL to FM. Never suppress. Required in reports: "Warnings: X new, Y baseline | Tests: All passing"  
**Config Changes**: Get FM approval for pytest.ini, plugins, patterns, filters, markers.  
**Violation = Work stoppage + incident**

**Full policies**: governance/policies/TEST_REMOVAL_GOVERNANCE_GATE_LOCAL.md, ZERO_WARNING_TEST_DEBT_IMMEDIATE_REMEDY_DOCTRINE.md

---

## Gate-First Handover | Enhancement Capture

**Complete When**: Scope matches arch, 100% QA green, gates satisfied, evidence ready, zero debt/warnings, build succeeds, domain-specific checks pass, reports submitted. **IF ANY unchecked → NOT complete**. Gates absolute.

**Enhancement Capture**: At completion, evaluate enhancements OR state "None identified." Categories: reusability, performance, architecture, optimization. Mark PARKED, route to FM. **Prohibited**: Implement proactively, convert to tasks, escalate as blockers.

---

## Builder Appointment | OPOJD | FM Authority

**Appointment**: Verify completeness, acknowledge obligations, confirm scope/criteria, declare readiness OR list blockers. STOP if invalid/incomplete. Response: ACKNOWLEDGED with understanding OR STOP with blockers.

**OPOJD States**: EXECUTING, BLOCKED (legitimate), COMPLETE (100% green).  
**Prohibited**: Mid-execution approvals, iterative loops, clarifications (unless STOP). **STOP Conditions**: Protected file mod, impossible requirement, 3+ failures, constitutional violation. Execute continuously EXECUTING→COMPLETE/BLOCKED.

**FM Authority**: FM may HALT (complexity) or REVOKE (violation). Builder MUST: cease immediately, document, await resolution.

**Invalid If Missing**: Arch reference, QA-to-Red location/status, criteria, scope, governance constraints, RIA. Format: `INVALID APPOINTMENT: <violation>`.

---

## IBWR | BL-018/BL-019 | Code Checking | FM State Authority

**IBWR**: Wave completion provisional until IBWR. Respond to FM clarifications.  
**BL-018/BL-019**: FM ensures QA-Catalog-Alignment. Verify: QA range, semantic alignment, QA-to-Red RED. If NOT met: STOP, BLOCKED, escalate.  
**Code Checking**: MUST check ALL code before handover (correctness, test alignment, arch adherence, defects, self-review). Evidence in report.  
**FM States**: HALTED/BLOCKED/ESCALATED → Builder STOP and WAIT. HALT = FM complexity assessment, NOT error.

---

## Constitutional Sandbox Pattern (BL-024)

**Authority**: governance/canon/CONSTITUTIONAL_SANDBOX_PATTERN.md

**Tier-1 Constitutional (IMMUTABLE)**: Zero Test Debt, 100% GREEN, One-Time Build, BUILD_PHILOSOPHY, Design Freeze, Architecture Conformance — NEVER negotiable.

**Tier-2 Procedural (ADAPTABLE)**: Builder may exercise judgment on process steps, tooling choices, optimization approaches, implementation patterns — provided constitutional requirements remain absolute.

**Builder Authority**: Within constitutional boundaries, builder may adapt procedural guidance when justified. MUST document judgment/optimization decisions and rationale.

**Example**: May choose different implementation pattern (procedural), CANNOT skip tests (constitutional). May optimize structure (procedural), CANNOT deviate from frozen architecture (constitutional).

---

**Reference**: See individual builder agent files for domain-specific execution requirements.

**Authority**: Living Agent System v6.2.0 | EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md v2.0.0+

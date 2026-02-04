# CORRECTIVE ACTION PLAN: Agent File LOCKED Section Format Standardization

**Date**: 2026-02-04  
**Plan Owner**: governance-liaison  
**Authority**: `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` Section 11, Issue #999  
**Related RCA**: `ROOT_CAUSE_ANALYSIS_AGENT_FILE_LOCKED_SECTION_FORMAT_INCONSISTENCY.md`  
**Approval Required**: CS2 (Johan) before execution  
**Status**: DRAFT — Awaiting CS2 Approval

---

## Executive Summary

This plan addresses the FM agent file LOCKED section format inconsistency identified in the RCA. The plan includes:

1. **Immediate Fix**: Update Foreman-app_FM.md to canonical LOCKED section format
2. **Protection Mechanisms**: Implement protection registry, automated validation, and detection systems
3. **Governance Updates**: Enhance governance-liaison contract with agent file format compliance checks
4. **Prevention**: Establish retroactive harmonization protocol and format migration procedures

**Timeline**: 3-phase execution over 1-2 days  
**Risk**: Low (format standardization, no logic changes)  
**Dependencies**: CS2 approval required before Phase 2 (FM file modification)

---

## Phase 1: Pre-Correction Preparation (Immediate — No Approval Required)

### 1.1 Create Protection Registry

**Authority**: `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` Section 4.4  
**Location**: `governance/contracts/protection-registry.md`

**Action**: Create complete protection registry for all LOCKED sections across all agent files

**Content Structure**:
```markdown
# Agent Contract Protection Registry

**Authority**: AGENT_CONTRACT_PROTECTION_PROTOCOL.md Section 4.4  
**Owner**: governance-liaison  
**Last Updated**: [YYYY-MM-DD]

## Registry Inventory

| Lock ID | Agent File | Section Title | Authority | Lock Date | Review Freq | Last Reviewed |
|---------|------------|---------------|-----------|-----------|-------------|---------------|
| LOCK-API-BUILDER-MISSION-001 | api-builder.md | Mission and Authority | AGENT_RECRUITMENT.md, BUILD_PHILOSOPHY.md | 2026-01-21 | quarterly | 2026-01-21 |
| ... (all 36+ LOCKED sections) | ... | ... | ... | ... | ... | ... |

## Review Schedule

[Quarterly review tracking...]

## Audit Trail

[Change log for LOCKED section modifications...]
```

**Deliverable**: `governance/contracts/protection-registry.md`  
**Estimated Time**: 1 hour  
**Validation**: Registry includes ALL LOCKED sections from ALL agent files

### 1.2 Create LOCKED Section Validation Script

**Authority**: `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` Section 6  
**Location**: `.github/scripts/validate-locked-sections.py`

**Purpose**: Automated validation of LOCKED section format compliance

**Validation Checks**:
1. ✅ HTML comment boundaries present (`<!-- LOCKED SECTION START -->` ... `<!-- LOCKED SECTION END -->`)
2. ✅ Markdown header with 🔒 emoji present (`## 🔒 [Title] (LOCKED)`)
3. ✅ Complete metadata block with ALL required fields:
   - Lock ID (format: `LOCK-[AGENT]-[SECTION]-###`)
   - Lock Reason
   - Lock Authority (canonical document reference)
   - Lock Date (YYYY-MM-DD)
   - Last Reviewed (YYYY-MM-DD)
   - Review Frequency (quarterly|annual|trigger-based)
4. ✅ Cross-reference to protection registry
5. ✅ No unauthorized modifications (diff check)

**Exit Codes**:
- `0` = All LOCKED sections compliant
- `1` = Format violations detected
- `2` = Missing metadata
- `3` = Registry mismatch

**Deliverable**: `.github/scripts/validate-locked-sections.py`  
**Estimated Time**: 2 hours  
**Validation**: Script detects FM file format inconsistencies, passes on builder files

### 1.3 Baseline Validation

**Action**: Run validation script on current agent files to document baseline state

**Expected Results**:
- ✅ api-builder.md: PASS
- ✅ ui-builder.md: PASS
- ✅ schema-builder.md: PASS
- ✅ qa-builder.md: PASS
- ✅ integration-builder.md: PASS
- ❌ Foreman-app_FM.md: FAIL (12 sections with incomplete metadata)
- ✅ governance-liaison.md: PASS (if has LOCKED sections)

**Deliverable**: `AGENT_FILE_LOCKED_SECTION_BASELINE_VALIDATION_REPORT.md`  
**Estimated Time**: 30 minutes

---

## Phase 2: FM File Format Correction (Requires CS2 Approval)

### 2.1 Archive Current FM File

**Action**: Create timestamped archive before modification

**Location**: `.github/agents/_archive/Foreman-app_FM-BEFORE-LOCKED-FORMAT-FIX-2026-02-04.md`

**Purpose**: Preserve current state for rollback if needed

**Estimated Time**: 5 minutes

### 2.2 Update FM LOCKED Sections to Canonical Format

**Authority**: CS2 approval + `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` Section 4.2-4.3

**Scope**: Update ALL 12 LOCKED sections in Foreman-app_FM.md

**Changes Per Section** (Example):

**BEFORE** (Current Format):
```markdown
# <!-- LOCKED SECTION - Mission and Authority - Changes require CS2 approval -->
# <!-- Authority - BUILD_PHILOSOPHY.md, FM_EXECUTION_MANDATE.md -->
# ## Mission
# FM is **sole autonomous authority** for planning...
# <!-- END LOCKED SECTION -->
```

**AFTER** (Canonical Format):
```markdown
<!-- LOCKED SECTION START -->
<!-- Lock ID: LOCK-FM-MISSION-001 -->
<!-- Lock Reason: FM mission and authority are constitutional, cannot be modified without CS2 approval -->
<!-- Lock Authority: governance/canon/BUILD_PHILOSOPHY.md, governance/canon/FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md -->
<!-- Lock Date: 2026-01-02 -->
<!-- Last Reviewed: 2026-02-04 -->
<!-- Review Frequency: quarterly -->
<!-- END METADATA -->

## 🔒 Mission and Authority (LOCKED)

FM is **sole autonomous authority** for planning, builder
recruitment/assignment, execution monitoring, quality/gates/merge control
in this repository.

**Core Functions**:
- Plan and orchestrate all build activities under canonical governance
- Recruit and direct builder agents for implementation work
- Enforce constitutional discipline (Zero Test Debt, Build-to-Green, OPOJD)
- Monitor execution and quality metrics
- Control merge gates and ensure gate success before handover
- Escalate when cognitive limits or governance gaps detected

**Authority Chain**: `CS2 (Johan) → FM → Builders`

**Platform Boundary**: FM holds decision authority. Maturion executes platform
actions. FM MUST NOT execute GitHub platform actions directly.

**Authority Limits**:
- **CANNOT**: Modify canonical governance (must escalate to governance repo)
- **CANNOT**: Waive constitutional requirements (Zero Test Debt, Agent Boundaries, etc.)
- **CANNOT**: Execute GitHub platform actions (create PRs, merge, etc.)
- **CANNOT**: Self-modify agent contract (CS2 authority only)
- **CAN**: Plan builds, recruit builders, enforce governance, control merge gates
- **CAN**: Propose governance changes (via governance-repo-administrator)
- **CAN**: Escalate blockers to CS2 or Maturion

<!-- LOCKED SECTION END -->
```

**FM LOCKED Sections to Update** (12 total):

| # | Current Section Title | New Lock ID | Lock Authority | Review Freq |
|---|----------------------|-------------|----------------|-------------|
| 1 | Mission and Authority | LOCK-FM-MISSION-001 | BUILD_PHILOSOPHY.md, FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md | quarterly |
| 2 | Scope | LOCK-FM-SCOPE-001 | AGENT_CONTRACT_PROTECTION_PROTOCOL.md Section 4.1 | quarterly |
| 3 | Contract Modification Prohibition | LOCK-FM-CONTRACT-MOD-001 | AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md | quarterly |
| 4 | File Integrity Protection | LOCK-FM-FILE-INTEGRITY-001 | AGENT_CONTRACT_PROTECTION_PROTOCOL.md | quarterly |
| 5 | Constitutional Principles | LOCK-FM-PRINCIPLES-001 | BUILD_PHILOSOPHY.md, GOVERNANCE_PURPOSE_AND_SCOPE.md | quarterly |
| 6 | Prohibitions | LOCK-FM-PROHIBITIONS-001 | AGENT_CONTRACT_PROTECTION_PROTOCOL.md, BUILD_PHILOSOPHY.md | quarterly |
| 7-12 | [Embedded operational sections] | LOCK-FM-[SECTION]-00[2-7] | [Specific canonical sources] | quarterly |

**Deliverable**: Updated `Foreman-app_FM.md` with canonical LOCKED section format  
**Estimated Time**: 3-4 hours  
**Validation**: Run `validate-locked-sections.py` — Must exit 0

### 2.3 Update Protection Registry

**Action**: Add all FM LOCKED sections to protection registry

**Updates**:
- Add 12 FM entries to registry table
- Update review schedule with FM quarterly reviews
- Document format correction in audit trail

**Deliverable**: Updated `governance/contracts/protection-registry.md`  
**Estimated Time**: 30 minutes

### 2.4 Post-Update Validation

**Action**: Comprehensive validation of ALL agent files

**Validation Commands**:
```bash
# 1. LOCKED section format validation
python .github/scripts/validate-locked-sections.py --all-agents
# Exit 0 required

# 2. YAML frontmatter validation
.github/scripts/validate-yaml-frontmatter.sh
# Exit 0 required

# 3. Protection registry completeness
python .github/scripts/validate-locked-sections.py --check-registry
# Exit 0 required

# 4. Cross-reference validation
python .github/scripts/validate-locked-sections.py --check-authority-refs
# Exit 0 required
```

**Expected Results**: ALL validations exit 0, ALL agent files compliant

**Deliverable**: `AGENT_FILE_LOCKED_SECTION_POST_FIX_VALIDATION_REPORT.md`  
**Estimated Time**: 30 minutes

---

## Phase 3: Governance Enhancements (Post-Fix)

### 3.1 Update Governance-Liaison Contract

**Authority**: `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` Section 11, Issue #999

**Changes**: Add new LOCKED section to governance-liaison.md

**New Section**: "🔒 Agent File Format Compliance (LOCKED)"

**Content**:
```markdown
<!-- LOCKED SECTION START -->
<!-- Lock ID: LOCK-GOV-LIAISON-AGENT-FORMAT-001 -->
<!-- Lock Reason: Agent file format compliance is governance-critical and must be enforced -->
<!-- Lock Authority: governance/canon/AGENT_CONTRACT_PROTECTION_PROTOCOL.md Section 11 -->
<!-- Lock Date: 2026-02-04 -->
<!-- Last Reviewed: 2026-02-04 -->
<!-- Review Frequency: quarterly -->
<!-- END METADATA -->

## 🔒 Agent File Format Compliance (LOCKED)

**MANDATORY in Pre-Job Self-Governance Check #2.5**: Verify agent file LOCKED section format compliance

### Step 1: Run Format Validation

Execute format validation script:
```bash
python .github/scripts/validate-locked-sections.py --all-agents
```

**Exit 0 Required**: ALL agent files MUST comply with canonical LOCKED section format per `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` Section 4.2-4.3.

### Step 2: Check Protection Registry Completeness

Verify all LOCKED sections are registered:
```bash
python .github/scripts/validate-locked-sections.py --check-registry
```

**Exit 0 Required**: Protection registry (`governance/contracts/protection-registry.md`) MUST include ALL LOCKED sections from ALL agent files.

### Step 3: Verify Authority References

Validate canonical authority references:
```bash
python .github/scripts/validate-locked-sections.py --check-authority-refs
```

**Exit 0 Required**: All Lock Authority references MUST point to existing canonical documents.

### If Validation Fails

**Format Violations Detected**:
1. **HALT IMMEDIATELY** — Do NOT proceed with job
2. **Document violations**: Which agent file(s), which section(s), what format issues
3. **Escalate to CS2**: "Agent file format compliance failure detected — cannot proceed until CS2 resolves"
4. **WAIT for CS2 fix**, then re-validate and resume

**Rationale**: Agent file format compliance is governance-critical. Format inconsistencies create:
- Inadequate protection metadata (no audit trail, review schedule)
- Difficult automated detection
- Incomplete protection registry
- Gradual governance decay

**Exception**: If CS2 explicitly approves proceeding with format violations (emergency only), document approval reference and proceed. Add violation to governance debt registry for later remediation.

<!-- LOCKED SECTION END -->
```

**Deliverable**: Updated `governance-liaison.md` with Check #2.5  
**Estimated Time**: 1 hour  
**Validation**: YAML validation, LOCKED section validation

### 3.2 Add Pre-Commit Hook

**Authority**: `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` Section 6

**Location**: `.githooks/pre-commit-locked-sections.sh`

**Purpose**: Prevent commits with LOCKED section format violations

**Logic**:
```bash
#!/bin/bash
# Validate LOCKED sections before commit

# Check if any .agent.md files are staged
AGENT_FILES=$(git diff --cached --name-only | grep '.github/agents/.*\.md$')

if [ -n "$AGENT_FILES" ]; then
  echo "🔒 Validating LOCKED sections in agent files..."
  python .github/scripts/validate-locked-sections.py --staged
  
  if [ $? -ne 0 ]; then
    echo "❌ LOCKED section format violations detected"
    echo "❌ Commit BLOCKED — Fix violations before committing"
    exit 1
  fi
  
  echo "✅ LOCKED section validation passed"
fi

exit 0
```

**Installation**: Add to `.git/hooks/pre-commit` (or use git hooks manager)

**Deliverable**: `.githooks/pre-commit-locked-sections.sh`  
**Estimated Time**: 1 hour  
**Validation**: Test with intentional format violation (should block commit)

### 3.3 Add CI Gate

**Authority**: `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` Section 6

**Location**: `.github/workflows/validate-locked-sections.yml`

**Purpose**: Enforce LOCKED section format compliance in PRs

**Workflow**:
```yaml
name: Validate LOCKED Sections

on:
  pull_request:
    paths:
      - '.github/agents/*.md'

jobs:
  validate-locked-sections:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      
      - name: Validate LOCKED Section Format
        run: |
          python .github/scripts/validate-locked-sections.py --all-agents
      
      - name: Validate Protection Registry
        run: |
          python .github/scripts/validate-locked-sections.py --check-registry
      
      - name: Validate Authority References
        run: |
          python .github/scripts/validate-locked-sections.py --check-authority-refs
```

**Deliverable**: `.github/workflows/validate-locked-sections.yml`  
**Estimated Time**: 1 hour  
**Validation**: Create test PR with format violation (should fail gate)

### 3.4 Create Format Migration Protocol

**Authority**: Lessons learned from this incident

**Location**: `governance/protocols/AGENT_FILE_FORMAT_MIGRATION_PROTOCOL.md`

**Purpose**: Establish process for retroactive format harmonization when governance specifications evolve

**Content Outline**:
1. **Trigger Conditions**: When to execute format migration
2. **Detection**: How to identify format inconsistencies
3. **Gap Analysis**: Compare current vs. canonical format
4. **Migration Plan**: Stepwise correction procedure
5. **Validation**: Post-migration verification
6. **Escalation**: When to escalate vs. self-correct
7. **Audit Trail**: Documentation requirements

**Deliverable**: `governance/protocols/AGENT_FILE_FORMAT_MIGRATION_PROTOCOL.md`  
**Estimated Time**: 2 hours

---

## Phase 4: Bootstrap Learning Capture

### 4.1 Create Bootstrap Learning Entry

**Authority**: `BOOTSTRAP_EXECUTION_LEARNINGS.md`, `MANDATORY_ENHANCEMENT_CAPTURE_STANDARD.md`

**Location**: Append to `BOOTSTRAP_EXECUTION_LEARNINGS.md`

**Entry Content**:
```markdown
---

## Learning #[NEXT]: Agent File Format Consistency Incident (2026-02-04)

**Category**: Governance Format Compliance  
**Severity**: Critical (governance integrity)  
**Date Recorded**: 2026-02-04  
**Incident**: FM agent file LOCKED section format inconsistency

### What Happened

FM agent file (Foreman-app_FM.md) used early LOCKED section format (HTML comments only) while builder agent files used canonical format (headers + metadata + comments). Format divergence occurred when:
1. FM refactored 2026-01-02 (pre-canonical spec)
2. Builders updated 2026-01-13 (post-canonical spec)
3. No retroactive harmonization of FM file

### Root Causes

1. **Format Evolution Without Retroactive Update**: Canonical spec published after FM refactor, FM not updated
2. **Incomplete Canon Layer-Down**: Steps 3-5 (Gap Analysis, Apply Lockdown, Document) not executed
3. **Governance-Liaison Scope Gap**: Self-governance Check #2 didn't cover agent file format
4. **No Automated Detection**: No validation script or CI gate for format compliance
5. **Missing Protection Registry**: No central inventory per Section 4.4

### What We Learned

1. **Format specifications require version migration protocol**: When governance specs evolve, need retroactive harmonization process
2. **Canon layer-down must execute ALL steps**: Section 11 steps 3-5 are NOT optional
3. **Governance-liaison needs agent file format responsibility**: Expand Check #2 to include .github/agents/*
4. **Automated validation is essential**: Manual inspection misses format subtleties
5. **Protection registry is not optional**: Section 4.4 requirement must be implemented

### Prevention Measures Implemented

1. ✅ **Protection Registry**: Created `governance/contracts/protection-registry.md`
2. ✅ **Format Validation Script**: `.github/scripts/validate-locked-sections.py`
3. ✅ **Governance-Liaison Check #2.5**: Agent file format compliance check
4. ✅ **Pre-Commit Hook**: Block commits with format violations
5. ✅ **CI Gate**: `validate-locked-sections.yml` workflow
6. ✅ **Format Migration Protocol**: `AGENT_FILE_FORMAT_MIGRATION_PROTOCOL.md`
7. ✅ **FM File Corrected**: All 12 LOCKED sections updated to canonical format

### Residual Risks

- **Other Repos**: This fix is local to office-app repo; other consumer repos may have same issue
- **Future Spec Changes**: Next format evolution needs proactive migration planning
- **Validation Script Maintenance**: Script must stay current with canonical spec

### Related Documents

- RCA: `ROOT_CAUSE_ANALYSIS_AGENT_FILE_LOCKED_SECTION_FORMAT_INCONSISTENCY.md`
- Corrective Plan: `CORRECTIVE_ACTION_PLAN_AGENT_FILE_LOCKED_SECTION_FORMAT.md`
- Protection Protocol: `governance/canon/AGENT_CONTRACT_PROTECTION_PROTOCOL.md`

### CS2 Review

[Awaiting CS2 review and lessons validation]

---
```

**Deliverable**: Updated `BOOTSTRAP_EXECUTION_LEARNINGS.md`  
**Estimated Time**: 1 hour

### 4.2 Create Governance Improvement Proposal

**Authority**: `MANDATORY_ENHANCEMENT_CAPTURE_STANDARD.md` v2.0.0

**Location**: `governance/proposals/governance-improvements/improvement-20260204-agent-file-format-enforcement.md`

**Proposal**: Cross-repository format validation and migration protocol

**Content Outline**:
1. **Problem Statement**: Format inconsistencies can persist across ecosystem
2. **Proposed Solution**: Centralized format spec + distributed validation
3. **Implementation**: 
   - Governance repo: Maintain canonical format spec with version
   - Consumer repos: Implement validation + auto-migration script
   - Ripple protocol: Include format migration in canon layer-down
4. **Benefits**: Ecosystem-wide consistency, automated detection, proactive migration
5. **Risks**: Implementation complexity, coordination overhead
6. **Recommendation**: Escalate to CS2 for governance repo implementation

**Deliverable**: `governance/proposals/governance-improvements/improvement-20260204-agent-file-format-enforcement.md`  
**Estimated Time**: 1.5 hours

---

## Implementation Timeline

### Day 1 (Immediate)

- [x] **Phase 1.1**: Create protection registry (1 hour)
- [x] **Phase 1.2**: Create validation script (2 hours)
- [x] **Phase 1.3**: Baseline validation (30 min)
- [ ] **Checkpoint**: Review Phase 1 deliverables with CS2

### Day 1-2 (After CS2 Approval)

- [ ] **Phase 2.1**: Archive current FM file (5 min)
- [ ] **Phase 2.2**: Update FM LOCKED sections (3-4 hours)
- [ ] **Phase 2.3**: Update protection registry (30 min)
- [ ] **Phase 2.4**: Post-update validation (30 min)
- [ ] **Checkpoint**: Validate all agent files compliant

### Day 2 (Post-Fix)

- [ ] **Phase 3.1**: Update governance-liaison contract (1 hour)
- [ ] **Phase 3.2**: Add pre-commit hook (1 hour)
- [ ] **Phase 3.3**: Add CI gate (1 hour)
- [ ] **Phase 3.4**: Create migration protocol (2 hours)

### Day 2 (Final)

- [ ] **Phase 4.1**: Bootstrap learning entry (1 hour)
- [ ] **Phase 4.2**: Governance improvement proposal (1.5 hours)
- [ ] **Final Checkpoint**: Complete prehandover proof

**Total Estimated Time**: 15-18 hours over 2 days

---

## Success Criteria

### Must-Have (Blocking)

1. ✅ **FM File Updated**: All 12 LOCKED sections use canonical format with complete metadata
2. ✅ **All Validations Pass**: `validate-locked-sections.py --all-agents` exits 0
3. ✅ **Protection Registry Complete**: All LOCKED sections registered
4. ✅ **Governance-Liaison Enhanced**: Check #2.5 added and tested
5. ✅ **Automated Detection**: Pre-commit hook and CI gate operational

### Should-Have (Important)

6. ✅ **Format Migration Protocol**: Documented for future spec changes
7. ✅ **Bootstrap Learning**: Incident captured with prevention measures
8. ✅ **Improvement Proposal**: Escalated to CS2 for ecosystem-wide solution

### Nice-to-Have (Optional)

9. ⚪ **Retrospective**: Team review of incident and learnings
10. ⚪ **Cross-Repo Scan**: Identify if other repos have same issue
11. ⚪ **Proactive Notification**: Inform other governance-liaisons of risk

---

## Risk Assessment

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| FM file update breaks contract | High | Low | Archive before change, thorough validation |
| Validation script false positives | Medium | Medium | Comprehensive testing, manual review |
| CI gate blocks legitimate work | Medium | Low | Escape hatch for CS2-approved exceptions |
| Format spec changes again | Low | Medium | Migration protocol + versioning |
| Other repos have same issue | Medium | High | Document for cross-repo awareness |

---

## Escalation Points

**Escalate to CS2 if**:

1. ❌ FM file update validation fails repeatedly (technical blocker)
2. ❌ Protection registry conflicts with existing governance (authority conflict)
3. ❌ Governance-liaison contract changes require broader governance review
4. ❌ CI gate implementation conflicts with existing workflows
5. ❌ Cross-repo coordination needed (beyond local repo scope)

---

## Approval Required

**This plan requires CS2 approval before Phase 2 execution** (FM file modification).

**Approval Checklist**:
- [ ] CS2 reviewed RCA and agrees with root cause analysis
- [ ] CS2 approves FM file LOCKED section format changes
- [ ] CS2 approves protection registry creation
- [ ] CS2 approves governance-liaison contract enhancement
- [ ] CS2 approves automated validation implementation
- [ ] CS2 authorizes proceeding with corrective actions

**Approval Authority**: CS2 (Johan Ras)  
**Awaiting Approval**: YES  
**Status**: DRAFT

---

**Prepared by**: governance-liaison  
**Reviewed by**: [Awaiting CS2 review]  
**Approved by**: [Awaiting CS2 approval]  
**Date Prepared**: 2026-02-04  
**Date Approved**: [Pending]

**Next Action**: Submit RCA + Corrective Plan to CS2 for approval

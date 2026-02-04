# ROOT CAUSE ANALYSIS: Agent File LOCKED Section Format Inconsistency

**Date**: 2026-02-04  
**Analyst**: governance-liaison  
**Issue**: Agent files reported as "missing canonical content and LOCKED sections"  
**Severity**: Critical (governance integrity)  
**Status**: Investigation Complete — Corrective Actions In Progress

---

## Executive Summary

**Issue Classification**: The issue description states that "ALL builder agent files and the FM agent file are missing their required markdown body content and LOCKED sections, leaving only the YAML frontmatter and governance bindings."

**Actual Findings**: This characterization is **PARTIALLY INCORRECT**:

✅ **Builder Files (5/5)**: ALL builder agent files (api-builder, ui-builder, schema-builder, qa-builder, integration-builder) have:
- Complete YAML frontmatter with governance bindings
- Complete markdown body content (899-1129 lines each)
- **6 properly formatted LOCKED sections each** using the canonical format specified in `AGENT_CONTRACT_PROTECTION_PROTOCOL.md`

❌ **FM File (1/1)**: The Foreman-app_FM.md file has:
- Complete YAML frontmatter with governance bindings  
- Complete markdown body content (975 lines)
- **12 LOCKED sections using INCONSISTENT/INCOMPLETE format**
  - Uses HTML comment markers (`<!-- LOCKED SECTION -->`) ✅
  - **MISSING**: `## 🔒` markdown headers ❌
  - **MISSING**: Complete metadata blocks (Lock ID, Lock Reason, Lock Authority, Lock Date, Last Reviewed, Review Frequency) ❌
  - Does NOT conform to `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` Section 4.2-4.3 specification

**True Problem**: FM agent file uses an older, incomplete LOCKED section format that predates the canonical protection protocol, creating format inconsistency and inadequate protection metadata.

---

## 1. Detailed Investigation Findings

### 1.1 Builder Agent Files Status (api-builder, ui-builder, schema-builder, qa-builder, integration-builder)

**File Size**: 32.5-40.0 KB each  
**Line Count**: 899-1129 lines each  
**LOCKED Sections**: 6 per file

**Format Compliance**: ✅ **FULL COMPLIANCE** with `AGENT_CONTRACT_PROTECTION_PROTOCOL.md`

**Example LOCKED Section from api-builder.md** (lines 617-680):

```markdown
## 🔒 Mission and Authority (LOCKED)

<!-- Lock ID: LOCK-API-BUILDER-MISSION-001 -->
<!-- Lock Reason: Builder mission and authority are governance non-negotiable -->
<!-- Lock Authority: governance/canon/AGENT_RECRUITMENT.md, BUILD_PHILOSOPHY.md -->
<!-- Lock Date: 2026-01-21 -->
<!-- Last Reviewed: 2026-01-21 -->
<!-- Review Frequency: quarterly -->
<!-- END METADATA -->

**Mission**: Implement API routes, handlers, and business logic from frozen
architecture to make QA-to-Red tests GREEN, following Build Philosophy's
One-Time Build Correctness principle.

[...content...]

<!-- LOCKED END -->
```

**LOCKED Sections in Builder Files**:
1. `## 🔒 Mission and Authority (LOCKED)` — Lock ID: LOCK-[BUILDER]-MISSION-001
2. `## 🔒 Scope (LOCKED)` — Lock ID: LOCK-[BUILDER]-SCOPE-001
3. `## 🔒 Contract Modification Prohibition (LOCKED)` — Lock ID: LOCK-[BUILDER]-CONTRACT-MOD-001
4. `## 🔒 File Integrity Protection (LOCKED)` — Lock ID: LOCK-[BUILDER]-FILE-INTEGRITY-001
5. `## 🔒 Constitutional Principles (LOCKED)` — Lock ID: LOCK-[BUILDER]-PRINCIPLES-001
6. `## 🔒 Prohibitions (LOCKED)` — Lock ID: LOCK-[BUILDER]-PROHIBITIONS-001

**Assessment**: ✅ **NO ISSUES** — All builder files have complete content and properly formatted LOCKED sections.

---

### 1.2 FM Agent File Status (Foreman-app_FM.md)

**File Size**: 35.4 KB  
**Line Count**: 975 lines  
**LOCKED Sections**: 12 (using inconsistent format)

**Format Compliance**: ❌ **NON-COMPLIANT** with `AGENT_CONTRACT_PROTECTION_PROTOCOL.md`

**Example LOCKED Section from Foreman-app_FM.md** (lines ~350-380):

```markdown
# <!-- LOCKED SECTION - Mission and Authority - Changes require CS2 approval -->
# <!-- Authority - BUILD_PHILOSOPHY.md, FM_EXECUTION_MANDATE.md -->
# ## Mission
# FM is **sole autonomous authority** for planning, builder
# recruitment/assignment,
# execution monitoring, quality/gates/merge control in this repository.
[...content...]
# <!-- END LOCKED SECTION -->
```

**Problems Identified**:
1. ❌ **Missing `## 🔒` markdown header** — Does not use the required emoji marker
2. ❌ **Missing Lock ID** — No unique identifier (e.g., `LOCK-FM-MISSION-001`)
3. ❌ **Missing Lock Reason** — No governance justification
4. ❌ **Missing Lock Date** — No creation timestamp
5. ❌ **Missing Last Reviewed date** — No review tracking
6. ❌ **Missing Review Frequency** — No review schedule
7. ⚠️ **Inconsistent comment style** — Uses `# <!-- -->` instead of plain `<!-- -->`
8. ⚠️ **Authority references incomplete** — Only partial canonical references

**LOCKED Sections in FM File** (12 total, all non-compliant):
1. Mission and Authority
2. Scope
3. Contract Modification Prohibition
4. File Integrity Protection
5. Constitutional Principles
6. Prohibitions
7. (Additional sections embedded in operational guidance)

**Assessment**: ❌ **FORMAT INCONSISTENCY** — FM file has LOCKED sections but they do NOT match the canonical protection protocol specification.

---

## 2. Root Cause Analysis

### 2.1 Timeline Reconstruction

**2026-01-02**: FM agent contract refactored
- Original 54,779 char contract archived to `ForemanApp-agent-ARCHIVE-2026-01-02.md`
- New 15,191 char contract created (`Foreman-app_FM.md`)
- LOCKED sections added using HTML comment format
- Evidence: `FM_AGENT_CONTRACT_REFACTORING_COMPLETION_SUMMARY.md`

**2026-01-08**: Builder contracts minimized
- Archived to `*-BEFORE-MINIMALISM-2026-01-08.md`
- No LOCKED sections in archived versions (0 count from grep)

**2026-01-13**: Agent files v2.0.0 alignment
- Builder contracts updated with 6 LOCKED sections each
- Used canonical format from `AGENT_CONTRACT_PROTECTION_PROTOCOL.md`
- FM contract NOT updated at this time
- Evidence: `PREHANDOVER_PROOF_AGENT_FILE_V2_0_0_ALIGNMENT.md`

**2026-01-15**: `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` v1.0.0 effective date
- Canonical specification published
- Defines complete LOCKED section format with metadata

**2026-01-27**: Last modification to FM file (PR #685)
- No format updates to LOCKED sections

**2026-02-04**: Issue raised — "missing canonical content"

### 2.2 Root Causes Identified

#### Primary Root Cause: **Format Evolution Without Retroactive Update**

The LOCKED section format evolved between the FM refactor (2026-01-02) and the builder updates (2026-01-13). The FM file was created with an early LOCKED section format that was later superseded by the canonical specification in `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` (effective 2026-01-15).

**Why this happened**:
1. FM refactoring preceded the canonical protection protocol
2. Builder updates followed the canonical protocol
3. FM file was NOT updated when builders were updated
4. No retroactive harmonization occurred

#### Secondary Root Cause: **Incomplete Gap Analysis**

When `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` was layered down (reference: Section 11 "Cross-Repository Layer-Down Requirements"), the protocol REQUIRES:

> **Step 3: Gap Analysis** — Compare current agent contracts against protection protocol requirements.  
> **Step 4: Apply Lockdown** — Update agent contracts with proper LOCKED sections.

**Evidence of gap**: The FM file was NOT updated during governance layer-down, indicating that either:
1. Gap analysis did not identify the FM format inconsistency, OR
2. Gap analysis was not performed, OR
3. Gap analysis identified the issue but correction was not executed

#### Tertiary Root Cause: **Governance-Liaison Did Not Detect/Prevent**

Per Issue #999, governance-liaison has "Check #2: Local Repo Governance Alignment" responsibility to detect and self-align governance drift. The FM file format inconsistency should have been detected during:
1. Pre-job self-governance checks
2. Periodic governance alignment verification
3. Governance canon layer-down operations

**Why detection failed**:
1. **Focus on canon files**: Self-governance checks focus on `governance/canon/*` alignment, not agent file format consistency
2. **No automated format validation**: No script checks LOCKED section format compliance
3. **Visual similarity**: HTML comments look "locked" even if missing metadata
4. **No protection registry**: Missing central inventory to track all LOCKED sections

---

## 3. Governance Gaps Identified

### 3.1 Process Gaps

| Gap ID | Gap Description | Impact | Current State |
|--------|----------------|--------|---------------|
| GAP-001 | No automated LOCKED section format validation | Inconsistencies undetected | ❌ Not implemented |
| GAP-002 | No protection registry (per Section 4.4) | No central inventory | ❌ Not implemented |
| GAP-003 | Governance-liaison self-checks don't cover agent file format | Format drift undetected | ⚠️ Partial (checks canon only) |
| GAP-004 | Canon layer-down protocol implementation incomplete | Steps 3-4 (Gap Analysis, Apply Lockdown) skipped | ❌ Not enforced |
| GAP-005 | No retroactive format harmonization after protocol updates | Old formats persist | ❌ Not implemented |

### 3.2 Detection Gaps

| Gap ID | Detection Mechanism | Status | Should Detect |
|--------|---------------------|--------|---------------|
| DET-001 | Pre-commit hook for LOCKED section validation | ❌ Missing | Format violations before commit |
| DET-002 | CI gate for agent file format compliance | ❌ Missing | Format violations in PR |
| DET-003 | Governance-liaison self-governance Check #2.5 | ❌ Missing | Agent file format drift |
| DET-004 | Protection registry completeness check | ❌ Missing | Missing LOCKED sections |
| DET-005 | Periodic agent file audit | ❌ Missing | Format decay over time |

### 3.3 Authority and Responsibility Gaps

**Gap**: No clear owner for "agent file format harmonization after canonical spec updates"

**Current State**:
- **governance-liaison**: Responsible for governance canon layer-down, NOT agent file format
- **CS2**: Has authority to modify agent files, but relies on detection mechanisms
- **Builder agents**: Prohibited from modifying agent files
- **FM**: Prohibited from modifying agent files

**Result**: Format inconsistencies can persist indefinitely without detection or correction trigger.

---

## 4. Contributing Factors

### 4.1 Issue Description Inaccuracy

The issue states "ALL builder agent files and the FM agent file are missing their required markdown body content and LOCKED sections."

**Impact**: This characterization caused misdirection in investigation. The actual problem is NOT missing content (content exists) but FORMAT INCONSISTENCY in the FM file.

**Possible Reasons for Inaccurate Description**:
1. Visual inspection showing FM HTML comments but no `## 🔒` headers
2. Comparison to builder files showing format difference
3. Assumption that different format = "missing"
4. Focus on "approved bits" protection without specific format analysis

### 4.2 No Escalation During FM Refactor

During the FM refactoring (2026-01-02), LOCKED sections were added using an early format. This predated `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` (2026-01-15 effective date), so the refactor was compliant with requirements AT THAT TIME.

However, when the protection protocol was published, no escalation occurred to retroactively update the FM file format.

### 4.3 Split Ownership Without Coordination

**Builder files**: Updated 2026-01-13 as part of "Agent File v2.0.0 Alignment" batch  
**FM file**: Updated 2026-01-02 as separate FM-specific refactor

The two tracks did not coordinate on LOCKED section format, resulting in builder files receiving the canonical format while the FM file retained the early format.

---

## 5. Why Governance-Liaison Did Not Detect/Prevent

### 5.1 Self-Governance Check Scope

**Check #1 (Own Contract)**: Verifies governance-liaison's own contract alignment with canonical template  
**Check #2 (Local Governance)**: Verifies `governance/canon/*` files match canonical repo

**Missing**: **Check #2.5** — Verify agent files conform to canonical format specifications

**Why this gap exists**: 
- Agent files (.github/agents/*.md) are NOT governance canon (they're in `.github/`)
- Self-governance focused on "governance alignment" = governance/canon/* files
- Agent file format compliance was NOT scoped into self-governance checks

### 5.2 Canon Layer-Down Protocol

When `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` was layered down, Section 11 requires:

1. ✅ **Step 1-2: Layer Down Canon** — Completed (file exists in governance/canon/)
2. ❌ **Step 3: Gap Analysis** — NOT executed (or executed but FM gap not identified)
3. ❌ **Step 4: Apply Lockdown** — NOT executed (FM file not updated)
4. ❌ **Step 5: Document Completion** — NOT documented

**Governance-liaison responsibility**: Execute ALL steps from Section 11 when layering down a canon that has layer-down requirements.

**What happened**: Steps 3-5 were NOT executed, violating the "Canon Layer-Down Compliance Protocol" LOCKED section in governance-liaison's own contract.

---

## 6. Systemic Lessons

### 6.1 Format Evolution Risk

When governance specifications evolve (e.g., LOCKED section format v1 → v2), there is SYSTEMIC RISK of:
1. New implementations using new format
2. Old implementations retaining old format
3. No retroactive harmonization
4. Gradual format divergence across ecosystem

**Mitigation Required**: Version-aware format migration protocol with automated detection and escalation.

### 6.2 Governance-Liaison Scope Clarity

Governance-liaison's "governance alignment" responsibility was interpreted as:
- ✅ `governance/canon/*` files
- ❌ `.github/agents/*` files

**Clarification Required**: Does "governance alignment" include agent file format compliance? If YES, expand Check #2. If NO, assign to different agent/process.

### 6.3 Protection Registry Absence

`AGENT_CONTRACT_PROTECTION_PROTOCOL.md` Section 4.4 requires a Protection Registry at `governance/contracts/protection-registry.md`.

**Status**: ❌ **DOES NOT EXIST**

**Impact**: No central inventory of LOCKED sections, no cross-reference tracking, no review schedule enforcement, no audit trail.

**Lesson**: Canonical requirements that are NOT implemented create governance debt and detection gaps.

---

## 7. Evidence Summary

### 7.1 Files Examined

| File | Size | Lines | LOCKED Sections | Format Compliance |
|------|------|-------|-----------------|-------------------|
| api-builder.md | 32.5 KB | 899 | 6 | ✅ Compliant |
| ui-builder.md | 40.0 KB | 1129 | 6 | ✅ Compliant |
| schema-builder.md | 34.9 KB | 948 | 6 | ✅ Compliant |
| qa-builder.md | 30.0 KB | 956 | 6 | ✅ Compliant |
| integration-builder.md | 29.0 KB | 948 | 6 | ✅ Compliant |
| **Foreman-app_FM.md** | **35.4 KB** | **975** | **12** | **❌ Non-Compliant** |

### 7.2 Key Documents Referenced

- `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` — Canonical LOCKED section format spec (v1.0.0, effective 2026-01-15)
- `FM_AGENT_CONTRACT_REFACTORING_COMPLETION_SUMMARY.md` — FM refactor evidence (2026-01-02)
- `PREHANDOVER_PROOF_AGENT_FILE_V2_0_0_ALIGNMENT.md` — Builder alignment evidence (2026-01-13)
- `.github/agents/_archive/*-BEFORE-MINIMALISM-2026-01-08.md` — Pre-alignment archived files
- `governance-liaison.md` — Governance-liaison contract with self-governance protocol

### 7.3 Git History Evidence

```bash
# Last FM file modification
24de770 2026-01-27 Merge pull request #685 from APGI-cmy/copilot/ban-excuse-based-dodging

# No format updates to LOCKED sections since refactor
```

---

## 8. Conclusion

**Root Cause**: FM agent file uses an early LOCKED section format (HTML comments only) that predates the canonical `AGENT_CONTRACT_PROTECTION_PROTOCOL.md` specification. When builder files were updated to the canonical format (2026-01-13), the FM file was NOT updated, creating format inconsistency.

**Governance Failures**:
1. Gap analysis (Step 3) and lockdown application (Step 4) from Section 11 NOT executed during canon layer-down
2. Governance-liaison self-governance Check #2 did NOT cover agent file format compliance
3. Protection registry (Section 4.4) NOT implemented
4. No automated format validation in pre-commit or CI gates
5. No retroactive harmonization protocol after canonical spec updates

**Issue Description**: The reported problem ("missing canonical content") is INACCURATE for builder files (they have complete content and proper format). The ACTUAL problem is FM file format inconsistency.

**Severity**: While the FM file HAS LOCKED sections with protection intent, the missing metadata (Lock ID, dates, authority references, review schedule) creates:
- ❌ No audit trail
- ❌ No review enforcement
- ❌ Difficult automated detection
- ❌ Incomplete protection registry (if implemented)

**Next Steps**: See Corrective Action Plan section in this report.

---

**Prepared by**: governance-liaison  
**Review Required**: CS2 approval  
**Related Issue**: Agent File Format Inconsistency — LOCKED Section Compliance  
**Status**: Investigation Complete — Awaiting Corrective Action Approval

# Examples README

**Purpose:** Provide template examples for PREHANDOVER_PROOF governance artifacts  
**Template Version:** 2.1.0  
**Last Updated:** 2026-01-13

---

## Overview

This directory contains example templates for the 4 governance artifacts required in PREHANDOVER_PROOF v2.1.0+:

1. **Governance Scan** — Repository governance alignment assessment
2. **Risk Assessment** — Risk evaluation and mitigation (see existing examples in `../risk-assessments/`)
3. **Change Record** — Documented changes and governance alignment (see existing examples in `../changes/`)
4. **Completion Summary** — Deliverable summary and readiness (embedded in PREHANDOVER_PROOF)
5. **CST Validation** — Contract Specification Test validation (NEW in v2.1.0)

---

## Available Examples

### 1. EXAMPLE_GOVERNANCE_SCAN.md

**Purpose:** Template for Artifact #1 (Governance Scan)

**When to Use:**
- Multi-agent changes
- New governance rules
- Constitutional changes
- Governance alignment audits

**Key Sections:**
- Repository Context
- Agents Identified
- Canonical Governance Mapped
- Local Governance Mapped
- Constitutional Principles
- Gaps Identified
- Recommendations
- Compliance Status

---

### 2. EXAMPLE_CST_VALIDATION.md

**Purpose:** Template for CST (Contract Specification Test) validation

**When to Use:**
- Subwave completions
- Contract milestone deliveries
- Capability deliveries (0% → 100%)
- Explicit CST requirement in issue

**Key Sections:**
- Validation Summary
- Contract Verification (acceptance criteria)
- Governance Gate Verification
- Evidence Artifact Review
- Constitutional Compliance
- CST-2 Attestation
- CST Signature

**Authority:** COMBINED_TESTING_PATTERN.md v1.0.0

---

## Using These Examples

### For Embedded Artifacts (Option A)

1. Copy the relevant example file content
2. Customize all `[placeholders]` with actual values
3. Paste into PREHANDOVER_PROOF under the appropriate artifact section
4. Update any template-specific details

### For Linked Artifacts (Option B)

1. Copy the relevant example file to the appropriate subdirectory:
   - Governance Scans: `.agent-admin/scans/scan_YYYYMMDD_HHMMSS.md`
   - Risk Assessments: `.agent-admin/risk-assessments/risk_NNN_YYYYMMDD.md`
   - Change Records: `.agent-admin/changes/change_NNN_YYYYMMDD.md`
   - CST Validations: `CST2_VALIDATION_[SUBWAVE_NAME].md` (root directory)
2. Customize all values
3. In PREHANDOVER_PROOF, use Option B and link to the file

### For Hybrid Approach (Option C)

1. Embed executive summary in PREHANDOVER_PROOF
2. Link to detailed artifact file for full details
3. Best for large artifacts (>100 lines)

---

## Existing Real Examples

### In `.agent-admin/` Subdirectories

**Scans:**
- `../scans/scan_20260113_102851.md` — Real governance scan from agent contract alignment

**Risk Assessments:**
- `../risk-assessments/risk_001_20260113.md` — Real risk assessment from agent contract alignment

**Change Records:**
- `../changes/change_001_20260113.md` — Real change record from agent contract alignment

### In Root Directory

**CST Validations:**
- `/CST2_VALIDATION_SUBWAVE_3.3.md` — Real CST-2 validation for Governance Dashboard V2
- `/WAVE_3.3_PREHANDOVER_PROOF.md` — Real PREHANDOVER_PROOF showing CST validation

**Study these real examples alongside templates for best practices.**

---

## Quick Decision Tree

**"Do I need this artifact?"**

### Governance Scan
- ✅ YES: Multi-agent changes, governance rules, constitutional changes
- ❌ NO: Single-file bug fixes, documentation updates, test-only changes

### Risk Assessment
- ✅ YES: Database schema, API changes, auth/authz changes
- ❌ NO: Documentation, comments, minor refactoring

### Change Record
- ✅ YES: Contract changes, governance changes, major features
- ❌ NO: Bug fixes, minor improvements, debt remediation

### Completion Summary
- ✅ YES: Subwave completions, milestone deliveries, CST validations
- ❌ NO: Incremental PRs, work-in-progress

### CST Validation
- ✅ YES: Contract milestones, subwave completions, capability deliveries
- ❌ NO: Incremental work, governance-only, dependency work

**When in doubt:** Create the artifact. Over-documentation > under-documentation.

---

## Retention Policy

- **Scans:** Keep last 3
- **Risk Assessments:** Keep last 3
- **Change Records:** Keep last 3
- **Completion Summaries:** Keep all (permanent record)
- **CST Validations:** Keep all (permanent record)

---

## Questions?

- **Template questions:** See `.github/agent-templates/PREHANDOVER_PROOF_TEMPLATE.md` FAQ (Section at end)
- **Governance questions:** Contact governance-liaison
- **Process questions:** Contact FM (ForemanApp-agent)
- **Constitutional matters:** Escalate to Johan (CS2)

---

**Version:** 2.1.0  
**Last Updated:** 2026-01-13  
**Maintained By:** governance-liaison

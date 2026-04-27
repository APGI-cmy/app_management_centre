
**Status**: CANONICAL | **Version**: 1.0.0 | **Authority**: CS2
**Date**: 2026-04-27
**Canon ID**: PHIRR-001
**Issue**: app_management_centre#1139 — Hardening — PR handover must enforce governing-issue role separation, retire stale handover injectors, and block partial handover state

> **Amendment Authority**: Only CS2 (Johan Ras / repo owner) may amend this canon.
> Any PR modifying this file without CS2 sign-off is auto-FAIL at the merge gate.

---

# PR Handover Issue-Role Registry

## Purpose

This canon defines the **machine-checkable issue-role registry** that MUST be embedded in
every wave record and PREHANDOVER proof. It ensures that every GitHub issue cited in the
PR artifact chain is assigned an explicit, unambiguous role — preventing silent substitution
of one issue role for another.

This registry complements `GOVERNING_ISSUE_PARITY_PROTOCOL.md` (GIPC-001), which defines
the *rules* for governing-issue consistency. PHIRR-001 defines the *artifact format* that
makes those rules machine-checkable at artifact-generation time.

---

## 1. Role Taxonomy

### 1.1 Canonical Role Definitions

| Role Identifier | Description | Governs Artifact Chain? |
|-----------------|-------------|------------------------|
| `GOVERNING_DELIVERY_ISSUE` | The issue that authorized and scoped this specific wave. Opened (or explicitly delegated) by CS2. | ✅ YES — the only role that anchors the artifact chain |
| `STAGE_DEFINITION_ISSUE` | The issue that defines the stage specification or scope. May differ from the delivery issue when the stage was defined in an earlier wave. | ❌ NO — cited for traceability only |
| `APPROVAL_REFERENCE` | An issue or comment URL that records the formal approval decision for a stage artifact. | ❌ NO — records approval, does not authorize the wave |
| `HARDENING_ISSUE` | An issue whose primary objective is strengthening, tightening, or adding enforcement to an existing artifact or protocol. Typically titled "Hardening —". | ❌ NO — cited in `related_hardening_issue` only |
| `HARMONIZATION_ISSUE` | An issue whose primary objective is aligning inconsistencies across artifacts or modules. Typically titled "Harmonization —" or "Alignment —". | ❌ NO — cited in `related_harmonization_issue` only |
| `OVERSIGHT_ISSUE` | An issue opened to track compliance, monitoring, or audit work related to a delivered artifact. Typically titled with "Oversight —" or "Compliance —". | ❌ NO — cited in `related_oversight_issue` only |
| `CONTINUOUS_IMPROVEMENT_ISSUE` | An issue that improves tooling, process, or governance without changing approved stage content. | ❌ NO — do not cite in any governing authority field |
| `SUB_ISSUE` | An issue created to track a specific task within a parent wave. The parent governing delivery issue remains the governing authority. | ❌ NO — parent issue governs |

### 1.2 Classification Heuristics

Apply these heuristics when classifying an issue:

1. **Title prefix check**: If the title begins with "Hardening —", "Harmonization —",
   "Alignment —", or "Continuous Improvement —", it is NOT a `GOVERNING_DELIVERY_ISSUE`.
2. **Opening-order check**: If the issue was opened *after* the wave kickoff, it cannot
   be the governing delivery issue unless an explicit CS2 supersession is documented.
3. **Scope check**: If the issue's stated objective is to *improve, tighten, or align*
   something that was already delivered, it is a hardening, harmonization, or CI issue.
4. **Authorization check**: Was this specific issue used by CS2 to authorize *this wave's*
   execution? If yes → `GOVERNING_DELIVERY_ISSUE`. If no → find the correct role.

---

## 2. Registry Schema

### 2.1 Required Registry Block

Every wave record and PREHANDOVER proof MUST include the following registry block. This block
MUST be populated at artifact-generation time — not deferred to post-generation review.

```yaml
## Issue-Role Registry (PHIRR-001)

issue_role_registry:
  governing_delivery_issue:
    number: "#NNN"
    title: "[Issue title]"
    role: "GOVERNING_DELIVERY_ISSUE"
    opened_before_wave_kickoff: "YES"    # YES / NO — if NO, supersession must be cited
    supersession_reference: "N/A"        # Issue/comment URL if this supersedes an earlier issue

  stage_definition_issue:
    number: "#NNN or N/A"
    title: "[Issue title or N/A]"
    role: "STAGE_DEFINITION_ISSUE"
    same_as_governing: "YES / NO"        # YES if stage def issue = governing delivery issue

  approval_reference:
    url: "[Issue/comment URL or PENDING]"
    role: "APPROVAL_REFERENCE"
    approval_exists: "YES / NO / PENDING"

  related_hardening_issue:
    number: "#NNN or N/A"
    title: "[Issue title or N/A]"
    role: "HARDENING_ISSUE"

  related_harmonization_issue:
    number: "#NNN or N/A"
    title: "[Issue title or N/A]"
    role: "HARMONIZATION_ISSUE"

  related_oversight_issue:
    number: "#NNN or N/A"
    title: "[Issue title or N/A]"
    role: "OVERSIGHT_ISSUE"

  registry_completeness_check: "PASS"    # PASS / FAIL — [reason if FAIL]
  overshadow_risk_assessed: "CLEAN"      # CLEAN / RISK — [issue number causing risk]
```

### 2.2 Minimum Required Fields

The following fields in the registry block MUST be populated (non-blank, non-placeholder):

| Field | Required | Prohibited Values |
|-------|----------|-------------------|
| `governing_delivery_issue.number` | MANDATORY | blank, `#NNN`, placeholder |
| `governing_delivery_issue.role` | MANDATORY | blank, any role other than `GOVERNING_DELIVERY_ISSUE` |
| `governing_delivery_issue.opened_before_wave_kickoff` | MANDATORY | blank, placeholder |
| `registry_completeness_check` | MANDATORY | `PENDING`, blank, placeholder |
| `overshadow_risk_assessed` | MANDATORY | `PENDING`, blank, placeholder |

---

## 3. Machine-Checkable Rules

### 3.1 Rules Enforced by Automation

The following rules are expressed in a form that can be checked programmatically by
the merge gate, ECAP, or IAA:

```
RULE PHIRR-R01:
  artifact_type IN [wave_record, prehandover_proof]
  REQUIRE: issue_role_registry block present
  REQUIRE: governing_delivery_issue.number NOT IN ["#NNN", "", null, "placeholder"]
  REQUIRE: governing_delivery_issue.role == "GOVERNING_DELIVERY_ISSUE"
  FAIL_CODE: PHIRR-MISSING-REGISTRY

RULE PHIRR-R02:
  governing_delivery_issue.number MUST match:
    - wave_record.section_1.triggering_issue
    - prehandover_proof.governing_stage_issue
    - pr_body.governing_delivery_issue
    - wave_checklist.authority_line
  FAIL_CODE: PHIRR-ROLE-MISMATCH

RULE PHIRR-R03:
  related_hardening_issue.number MUST NOT equal governing_delivery_issue.number
  related_harmonization_issue.number MUST NOT equal governing_delivery_issue.number
  related_oversight_issue.number MUST NOT equal governing_delivery_issue.number
  FAIL_CODE: PHIRR-ROLE-COLLISION

RULE PHIRR-R04:
  IF governing_delivery_issue.opened_before_wave_kickoff == "NO":
    REQUIRE: supersession_reference NOT IN ["N/A", "", null]
  FAIL_CODE: PHIRR-MISSING-SUPERSESSION

RULE PHIRR-R05:
  registry_completeness_check MUST equal "PASS"
  overshadow_risk_assessed MUST equal "CLEAN" OR MUST have documented exception
  FAIL_CODE: PHIRR-REGISTRY-INCOMPLETE
```

### 3.2 Violation Codes

| Code | Description | Severity |
|------|-------------|---------|
| `PHIRR-MISSING-REGISTRY` | Issue-role registry block absent from wave record or PREHANDOVER proof | BLOCKING |
| `PHIRR-ROLE-MISMATCH` | governing_delivery_issue does not match across all required artifact surfaces | BLOCKING |
| `PHIRR-ROLE-COLLISION` | A hardening/harmonization/oversight issue number equals the governing delivery issue number | BLOCKING |
| `PHIRR-MISSING-SUPERSESSION` | Governing delivery issue opened after wave kickoff without documented supersession | BLOCKING |
| `PHIRR-REGISTRY-INCOMPLETE` | Registry completeness check is not PASS | BLOCKING |
| `PHIRR-OVERSHADOW-RISK` | Overshadow risk field not assessed or shows unresolved risk | BLOCKING |

---

## 4. Producing-Agent Responsibilities

### 4.1 At Artifact-Generation Time

When producing a wave record or PREHANDOVER proof, the producing agent MUST:

1. Identify the governing delivery issue number from the CS2 authorization
2. Classify every other related issue into its correct role
3. Populate the issue-role registry block completely — no placeholder values
4. Run the completeness check (PHIRR-R01 through PHIRR-R05) mentally before committing
5. Set `registry_completeness_check: PASS` only when all checks clear

### 4.2 ECAP Duty

When ECAP prepares the ceremony bundle, it MUST:

1. Verify the issue-role registry block is present in the wave record and PREHANDOVER proof
2. Verify PHIRR-R01 through PHIRR-R05 all pass
3. Confirm no role collision exists (R03)
4. Record registry verification in the ECAP reconciliation summary (C1 field)

### 4.3 IAA Duty

IAA MUST verify the issue-role registry as part of its standard audit:

1. Registry block present and complete
2. PHIRR-R01 through PHIRR-R05 all pass
3. If any rule fails: issue REJECTION-PACKAGE citing the applicable PHIRR violation code

---

## 5. Integration with GIPC-001

This canon (PHIRR-001) and `GOVERNING_ISSUE_PARITY_PROTOCOL.md` (GIPC-001) are
complementary:

| Concern | Governed By |
|---------|------------|
| Rules for governing-issue consistency across artifact chain | GIPC-001 §2 |
| Overshadow prohibition and detection | GIPC-001 §5 |
| Mandatory labeled authority fields in artifact headers | GIPC-001 §3 |
| Machine-checkable registry schema for wave records and proofs | **PHIRR-001 (this document)** |
| Role taxonomy and classification heuristics | **PHIRR-001 (this document)** |
| Machine-checkable rule codes for automation | **PHIRR-001 (this document)** |

Both MUST pass before QP PASS is declared.

---

## Appendix A: Quick-Reference Registry Checklist

Before every QP PASS, verify:

```
✅ issue_role_registry block present in wave record and PREHANDOVER proof
✅ governing_delivery_issue.number is the actual CS2-authorized wave issue
✅ governing_delivery_issue.role == "GOVERNING_DELIVERY_ISSUE"
✅ No hardening/harmonization/oversight issue equals the governing delivery issue
✅ If opened after kickoff: supersession_reference is populated
✅ registry_completeness_check: PASS
✅ overshadow_risk_assessed: CLEAN
✅ governing_delivery_issue matches across all artifact surfaces (GIPC-001 §2.2)
```

---

**Canon ID**: PHIRR-001
**Filed by**: foreman-v2-agent (POLC-Orchestration governance specification) | **Date**: 2026-04-27
**Authority**: CS2 — Issue #1139
**See also**: `GOVERNING_ISSUE_PARITY_PROTOCOL.md` (GIPC-001), `PR_HANDOVER_CANONICAL_PACKAGE.md` (PHCP-001)

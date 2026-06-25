# AMC Build Progress Tracker

**Module**: App Management Centre (AMC)  
**Module Slug**: AMC  
**Last Updated**: 2026-06-25  
**Updated By**: foreman-v2-agent (wave: amc-stage1-4-functional-delivery-retrofit-20260625 — issue #1185; PR #1186; Stage 1-4 functional-delivery retrofit artifacts produced for CS2 review; Stage 2 CTA/API/Data/Audit matrix aligned to canonical quota and ARC contracts; Stage 5/5a/6/7 must import or explicitly disposition retrofit obligations before Stage 8 may start; prior: amc-stage7-pbfag-20260428 — Stage 7 PBFAG pack produced approval-pending; issue #1152)

> **Classification**: ACTIVE  
> **Document Role**: PRIMARY LIVE CONTROL DOCUMENT — This is the designated primary operational monitor for AMC pre-build stage progress. CS2 should use this document as the main live progress dashboard.  
> **Canon Reference**: `PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0 plus current ISMS/MMM functional-delivery retrofit lessons  
> **Current Issue**: [app_management_centre#1185](https://github.com/APGI-cmy/app_management_centre/issues/1185)  
> **Current PR**: [app_management_centre#1186](https://github.com/APGI-cmy/app_management_centre/pull/1186)  
> **Update Rule**: This document MUST be updated immediately after every AMC stage issue, wave completion, approval, or readiness/blocker change. Stale tracker text is a governance defect.

> ⚠️ **GOVERNANCE OVERSIGHT NOTE (issue #1133, 2026-04-26)**: A mandatory deployment execution
> planning stage has been added as Stage 5a between Stage 5 (Architecture) and Stage 6 (QA-to-Red).
> Architecture/platform topology alone is insufficient — the deployment execution strategy must be
> frozen and CS2-approved before build execution begins. See
> `modules/amc/governance-oversight/DEPLOYMENT_STRATEGY_OVERSIGHT.md` for the formal oversight
> record, Stage 5a definition, required content specification, anti-drift rules, and corrective
> action roadmap. Stage 6 (QA-to-Red) is BLOCKED until Stage 5a is complete and CS2-approved.

> ⚠️ **FUNCTIONAL DELIVERY RETROFIT NOTE (issue #1185, PR #1186, 2026-06-25)**: AMC Stages 1-4 are undergoing a governed functional-delivery retrofit based on ISMS/MMM learning. The retrofit adds Stage 1 functional-delivery definition, Stage 2 CTA/API/Data/Audit matrix, Stage 3 FR-1900, Stage 4 TR-1900, and a Stage 1-4 change-propagation audit. This wave does not start Stage 8, does not appoint builders, and does not certify AMC build-readiness. Stages 5, 5a, 6, and 7 must import or explicitly disposition these retrofit obligations before Stage 8 may begin.

---

## Lifecycle Model

**Canonical 12-Stage Pre-Build Sequence** (PRE_BUILD_STAGE_MODEL_CANON.md v1.0.0)  
**Tracker Authority**: Repo-local — tracks AMC-specific stage completion within this repository

> ⚠️ This tracker reflects the AMC repo-local pre-build state. It does not duplicate or replace any ISMS-level module tracker. Both must remain consistent.

---

## Stage Summary

| Stage | Name | Status | Notes |
|-------|------|--------|-------|
| 1 | App Description | ✅ COMPLETE + 🟡 RETROFIT ADDENDUM PRODUCED | CS2-approved 2026-04-22. Functional-delivery addendum produced in #1186 for CS2 review: `modules/amc/00-app-description/functional-delivery-definition.md`. |
| 2 | UX Workflow & Wiring Spec | ✅ COMPLETE + 🟡 RETROFIT ADDENDUM PRODUCED | CS2-approved 2026-04-22. CTA/API/Data/Audit matrix produced in #1186: `modules/amc/01-ux-workflow-wiring-spec/cta-api-data-audit-contract-matrix.md`. Matrix must stay aligned with canonical quota and ARC TRS contracts. |
| 3 | FRS | ✅ COMPLETE — CS2 APPROVED + 🟡 RETROFIT ADDENDUM PRODUCED | CS2-approved for Stage 4 progression. FR-1900 functional-delivery requirement family produced in #1186: `modules/amc/02-frs/functional-delivery-requirements-addendum.md`. |
| 4 | TRS | ✅ TREATED AS APPROVED + 🟡 RETROFIT ADDENDUM PRODUCED | Treated as approved for Stage 5 progression per #1131. TR-1900 technical functional-delivery family produced in #1186: `modules/amc/03-trs/functional-delivery-technical-requirements-addendum.md`. |
| 1-4 Retrofit | Functional Delivery Retrofit | 🟡 PRODUCED FOR CS2 REVIEW | Issue #1185 / PR #1186. Adds full-functional-delivery controls and change-propagation audit. Must be CS2-dispositioned and propagated into Stages 5/5a/6/7 before Stage 8 starts. |
| 5 | Architecture | 🟡 IN PROGRESS — Produced Approval-Pending | Stage 5 Architecture Specification v1.0 produced 2026-04-26. Awaiting CS2 approval. Must import/disposition FR-1900/TR-1900 and CTA/API/Data/Audit obligations before Stage 8. |
| **5a** | **Deployment Execution Strategy** | **🟡 IN PROGRESS — Produced Approval-Pending** | Stage 5a artifacts produced 2026-04-27. Awaiting CS2 approval. Must import/disposition TR-1910 deployment-execution carry-forward before Stage 8. |
| 6 | QA-to-Red | 🟡 IN PROGRESS — Produced Approval-Pending | Stage 6 QA-to-Red pack produced 2026-04-27. Must import/disposition dead CTA, missing backend, missing audit, authority bypass, degraded-mode, placeholder leakage, and journey-level completion tests from #1186. |
| 7 | PBFAG | 🟡 IN PROGRESS — Produced Approval-Pending | Stage 7 PBFAG pack produced 2026-04-28. Must import/disposition #1186 retrofit as a hard functional-delivery gate before Stage 8. |
| 8 | Implementation Plan | ⬜ Not Started | 🔴 BLOCKED — must not start until Stages 5, 5a, 6, 7 and the #1186 retrofit obligations are CS2-dispositioned/imported. |
| 9 | Builder Checklist | ⬜ Not Started | 🔴 BLOCKED |
| 10 | IAA Pre-Brief | ⬜ Not Started | 🔴 BLOCKED |
| 11 | Builder Appointment | ⬜ Not Started | 🔴 BLOCKED — no builders appointed by #1186. |
| 12 | Build | ⬜ Not Started | 🔴 BLOCKED — no implementation/build authorization created by #1186. |

**Legend**: ✅ Complete | 🟡 Active / Produced / In Progress | ⬜ Not Started | 🔴 Blocked | 📋 Defined (awaiting prerequisites)

---

## Stage Detail

### Stage 1 — App Description

**Status**: ✅ COMPLETE — CS2 APPROVED; 🟡 functional-delivery retrofit addendum produced for CS2 review  
**Location**: `modules/amc/00-app-description/`  
**Key Artifacts**:
- [x] `app-description.md` — Authoritative AMC App Description v1.0 (approved 2026-04-22)
- [x] `app-description-approval.md` — Formal Stage 1 approval record (completed 2026-04-22)
- [x] `functional-delivery-definition.md` — Stage 1 retrofit addendum produced in issue #1185 / PR #1186
- [ ] `amc-role-authority-and-operating-model.md` — Stage 1 companion artifact (placeholder/follow-on; does not block Stage 2)

**Retrofit note**: Stage 1 now carries an explicit fully functional delivery definition. A user-visible AMC capability is not complete unless the user action, backend/API target, authority enforcement, state effect, audit event, dependency/degraded behavior, visible confirmation, test/evidence path, and placeholder declaration requirements are satisfied or explicitly dispositioned by CS2.

---

### Stage 2 — UX Workflow & Wiring Spec

**Status**: ✅ COMPLETE — CS2 APPROVED; 🟡 functional-delivery retrofit addendum produced for CS2 review  
**Location**: `modules/amc/01-ux-workflow-wiring-spec/`  
**Key Artifacts Created**:
- [x] `ux-workflow-wiring-spec.md` — Complete user journey maps, screen/surface model, wiring tables, cross-system integration wiring, degraded-mode patterns, Stage 1 traceability index. Harmonization pass v1.1 applied 2026-04-23.
- [x] `wiring-artifact-index.md` — Wiring artifact inventory; document-control reconciliation remains required because its header/status posture may lag the v1.1 approved/harmonized Stage 2 posture.
- [x] `cta-api-data-audit-contract-matrix.md` — Stage 2 retrofit matrix produced in issue #1185 / PR #1186.

**Retrofit note**: Stage 2 now carries per-action CTA/API/Data/Audit/Degraded/Confirmation/QA mapping. The matrix has been corrected to use the canonical quota adjustment route and canonical ARC item model. Any later architecture or QA work must not derive from superseded quota or ARC routes/events.

---

### Stage 3 — Functional Requirements Specification (FRS)

**Status**: ✅ COMPLETE — CS2 APPROVED; 🟡 functional-delivery retrofit addendum produced for CS2 review  
**Location**: `modules/amc/02-frs/`  
**Key Artifacts Created**:
- [x] `functional-requirements-specification.md` — Existing Stage 3 FRS with FR-100 through FR-1800 families.
- [x] `app-description-to-frs-traceability.md` — Stage 1 + Stage 2 to FRS traceability matrix.
- [x] `functional-delivery-requirements-addendum.md` — FR-1900 fully functional delivery requirement family produced in issue #1185 / PR #1186.

**Retrofit note**: FR-1900 is a cross-cutting requirement family. It does not replace FR-100 through FR-1800; it constrains how every AMC functional requirement must be delivered and evidenced.

---

### Stage 4 — Technical Requirements Specification (TRS)

**Status**: ✅ TREATED AS APPROVED; 🟡 functional-delivery retrofit addendum produced for CS2 review  
**Location**: `modules/amc/03-trs/`  
**Key Artifacts Created**:
- [x] `technical-requirements-specification.md` — Existing TRS v1.1 with TR-100 through TR-1800 families.
- [x] `frs-to-trs-traceability.md` — Existing FRS-to-TRS traceability matrix.
- [x] `functional-delivery-technical-requirements-addendum.md` — TR-1900 fully functional delivery technical requirement family produced in issue #1185 / PR #1186.

**Retrofit note**: TR-1900 adds CTA-to-route, typed response, atomic audit, authority-before-side-effects, dependency non-bypass, state/projection boundary, user-visible state binding, no frontend-only/backend-only completion, QA-evidence binding, and deployment-execution carry-forward requirements.

---

### Stage 5 — Architecture

**Status**: 🟡 IN PROGRESS — Produced Approval-Pending  
**Location**: `modules/amc/04-architecture/`  
**Key Artifacts Created**:
- [x] `architecture-specification.md` — Stage 5 Architecture Specification v1.0 (produced 2026-04-26)
- [x] `trs-to-architecture-traceability.md` — TRS to Architecture Traceability v1.0

**Current gate note**: Stage 5 approval/disposition must account for the #1186 retrofit. Architecture must import or explicitly disposition route-to-capability, action-to-state, audit-event, external dependency/degraded-mode, and no-placeholder requirements before Stage 8 starts.

---

### Stage 5a — Deployment Execution Strategy

**Status**: 🟡 IN PROGRESS — Produced Approval-Pending  
**Location**: `modules/amc/05a-deployment-execution-strategy/`  
**Key Artifacts Created**:
- [x] `deployment-execution-strategy.md` — Primary Stage 5a artifact v1.0
- [x] `deployment-surface-ownership-table.md` — Supporting artifact v1.0
- [x] `runner-and-environment-constraints.md` — Supporting artifact v1.0

**Current gate note**: Stage 5a approval/disposition must account for TR-1910 and the ISMS/MMM deployment-execution no-speculation lesson before Stage 8 starts.

---

### Stage 6 — QA-to-Red

**Status**: 🟡 IN PROGRESS — Produced Approval-Pending  
**Location**: `modules/amc/05-qa-to-red/`  
**Key Artifacts**:
- [x] `qa-to-red-specification.md` v1.0
- [x] `architecture-and-des-to-qa-traceability.md` v1.0
- [x] `red-test-catalog.md` v1.0 — 79 test cases across 20 families

**Current gate note**: Stage 6 approval/disposition must account for #1186 tests: dead CTA, missing backend target, missing audit event, authority bypass, non-bypass boundary, degraded-mode, placeholder leakage, and journey-level completion.

---

### Stage 7 — PBFAG

**Status**: 🟡 IN PROGRESS — Produced Approval-Pending  
**Location**: `modules/amc/06-pbfag/`  
**Key Artifacts Created**:
- [x] `pre-build-final-assurance-gate.md` v1.0
- [x] `pbfag-evidence-matrix.md` v1.0
- [x] `pbfag-findings-and-verdict.md` v1.0
- [x] `pbfag-checklist.md`
- [x] `stage1-4-functional-delivery-change-propagation-audit.md` — Stage 1-4 retrofit audit produced in issue #1185 / PR #1186

**Current gate note**: Stage 7 must fail or conditionally block Stage 8 if material actions lack CTA/API/Data/Audit/QA coverage, if Stage 2 status/version drift remains unresolved/undispositioned, if deployment execution remains ambiguous, or if undeclared placeholders cover high-risk executive actions.

---

### Stage 8 — Implementation Plan

**Status**: ⬜ Not Started  
**Location**: `modules/amc/07-implementation-plan/`  
**Current blocker**: Stage 8 remains blocked until Stages 5, 5a, 6, 7 and the #1186 functional-delivery retrofit obligations are CS2-dispositioned/imported. This tracker update does not start Stage 8.

---

### Stage 9 — Builder Checklist

**Status**: ⬜ Not Started  
**Location**: `modules/amc/08-builder-checklist/`  
**Current blocker**: Stage 9 remains blocked because Stage 8 has not started.

---

### Stage 10 — IAA Pre-Brief

**Status**: ⬜ Not Started  
**Location**: `modules/amc/09-iaa-pre-brief/`  
**Current blocker**: Stage 10 remains blocked because Stage 9 has not started.

---

### Stage 11 — Builder Appointment

**Status**: ⬜ Not Started  
**Location**: `modules/amc/10-builder-appointment/`  
**Current blocker**: No builders appointed. Stage 11 remains blocked.

---

### Stage 12 — Build

**Status**: ⬜ Not Started  
**Location**: `modules/amc/11-build/`  
**Current blocker**: Build remains blocked. PR #1186 does not authorize implementation.

---

## Next Action

1. Review and merge PR #1186 if CS2 accepts the Stage 1-4 functional-delivery retrofit production.
2. Reconcile Stage 2 `wiring-artifact-index.md` header/status drift or explicitly disposition it.
3. Review Stages 5, 5a, 6, and 7 against the #1186 retrofit obligations.
4. Do not start Stage 8 until the above propagation/disposition work is complete.
5. Do not appoint builders until the canonical pre-build sequence authorizes Stage 11.

---

## References

- [PRE_BUILD_STAGE_MODEL_CANON.md](../../governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md)
- [APP_DESCRIPTION_REQUIREMENT_POLICY.md](../../governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md)
- [DEPLOYMENT_STRATEGY_OVERSIGHT.md](./governance-oversight/DEPLOYMENT_STRATEGY_OVERSIGHT.md)
- [functional-delivery-definition.md](./00-app-description/functional-delivery-definition.md)
- [cta-api-data-audit-contract-matrix.md](./01-ux-workflow-wiring-spec/cta-api-data-audit-contract-matrix.md)
- [functional-delivery-requirements-addendum.md](./02-frs/functional-delivery-requirements-addendum.md)
- [functional-delivery-technical-requirements-addendum.md](./03-trs/functional-delivery-technical-requirements-addendum.md)
- [stage1-4-functional-delivery-change-propagation-audit.md](./06-pbfag/stage1-4-functional-delivery-change-propagation-audit.md)
- [AMC_STAGE1_4_FUNCTIONAL_DELIVERY_RETROFIT_INDEX.md](./AMC_STAGE1_4_FUNCTIONAL_DELIVERY_RETROFIT_INDEX.md)
- [AMC_PRE_BUILD_ARTIFACT_INDEX.md](./AMC_PRE_BUILD_ARTIFACT_INDEX.md)
- [REPO_REALIGNMENT_NOTE.md](./REPO_REALIGNMENT_NOTE.md)

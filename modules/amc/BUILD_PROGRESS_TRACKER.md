# AMC Build Progress Tracker

**Module**: App Management Centre (AMC)  
**Module Slug**: AMC  
**Last Updated**: 2026-04-23  
**Updated By**: foreman-v2-agent (wave: amc-stage3-frs-20260423 — Stage 3 FRS produced approval-ready, issue #1152)

> **Classification**: ACTIVE  
> **Document Role**: PRIMARY LIVE CONTROL DOCUMENT — This is the designated primary operational monitor for AMC pre-build stage progress. CS2 should use this document as the main live progress dashboard.  
> **Canon Reference**: `PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0  
> **Issue**: [app_management_centre#1152](https://github.com/APGI-cmy/app_management_centre/issues/1152)  
> **Update Rule**: This document MUST be updated immediately after every AMC stage issue, wave completion, approval, or readiness/blocker change. Stale tracker text is a governance defect.

---

## Lifecycle Model

**Canonical 12-Stage Pre-Build Sequence** (PRE_BUILD_STAGE_MODEL_CANON.md v1.0.0)  
**Tracker Authority**: Repo-local — tracks AMC-specific stage completion within this repository

> ⚠️ This tracker reflects the AMC repo-local pre-build state. It does not duplicate or replace any ISMS-level module tracker. Both must remain consistent.

---

## Stage Summary

| Stage | Name | Status | Notes |
|-------|------|--------|-------|
| 1 | App Description | ✅ COMPLETE | CS2-approved 2026-04-22. Canonical source: `modules/amc/00-app-description/app-description.md` v1.0. Approval ref: #1117. |
| 2 | UX Workflow & Wiring Spec | ✅ COMPLETE | CS2-approved (issue #1121). Canonical source: `modules/amc/01-ux-workflow-wiring-spec/`. Stage 3 authorized to proceed. |
| 3 | FRS | 🟡 APPROVAL PENDING — Produced approval-ready 2026-04-23. Awaiting CS2 approval before Stage 4 may begin. | Stage 3 artifacts produced by foreman-v2-agent (wave: amc-stage3-frs-20260423). CS2 approval required before TRS derivation begins. |
| 4 | TRS | ⬜ Not Started | |
| 5 | Architecture | ⬜ Not Started | Pre-existing FM-era architecture material exists in `docs/architecture/` but is classified as historical/reference only — not active Stage 5 lifecycle input. See Stage Detail below. |
| 6 | QA-to-Red | ⬜ Not Started | |
| 7 | PBFAG | ⬜ Not Started | |
| 8 | Implementation Plan | ⬜ Not Started | |
| 9 | Builder Checklist | ⬜ Not Started | |
| 10 | IAA Pre-Brief | ⬜ Not Started | |
| 11 | Builder Appointment | ⬜ Not Started | |
| 12 | Build | ⬜ Not Started | |

**Legend**: ✅ Complete | 🟡 Active / In Progress | ⬜ Not Started | 🔴 Blocked

---

## Stage Detail

### Stage 1 — App Description

**Status**: ✅ COMPLETE — CS2 APPROVED  
**Location**: `modules/amc/00-app-description/`  
**Key Artifacts**:
- [x] `app-description.md` — Authoritative AMC App Description v1.0 (approved 2026-04-22)
- [x] `app-description-approval.md` — Formal Stage 1 approval record (completed 2026-04-22)
- [ ] `amc-role-authority-and-operating-model.md` — Stage 1 companion artifact (⬜ Placeholder — follow-on; does not block Stage 2)

**Completion Date**: 2026-04-22  
**Approval Required**: Yes
- [x] Approved by designated authority
**Approval Date**: 2026-04-22  
**Approved By**: CS2 (Johan Ras / @APGI-cmy)  
**Approval Reference**: app_management_centre#1117  
**Notes**: Stage 1 App Description (`app-description.md` v1.0) formally approved by CS2 via issue #1117
(2026-04-22). Canonical source decision resolved — `modules/amc/00-app-description/app-description.md`
is the sole authoritative Stage 1 source for all downstream derivation (FRS, TRS, Architecture,
Build Planning). The FM-era transitional source (`docs/governance/FM_APP_DESCRIPTION.md`) is
superseded as active canonical authority and is retained as historical/provenance reference only.
Stage 1 formally closed. Stage 2 (UX Workflow & Wiring Spec) is authorized to begin.

---

### Stage 2 — UX Workflow & Wiring Spec

**Status**: ✅ COMPLETE — CS2 APPROVED  
**Location**: `modules/amc/01-ux-workflow-wiring-spec/`  
**Entry Condition**: ✅ Stage 1 complete and approved  
**Objective**: Produce a complete UX workflow and wiring specification that maps all user journeys,
screen interactions, data flows, and explicit wiring between UI elements, API endpoints, schema
tables, and reporting outputs. All primary and secondary user paths must be documented with
explicit wiring between the UI layer and backend. No gaps between stated journeys and wired
system behaviour are permitted.  
**Key Artifacts Created**:
- [x] `ux-workflow-wiring-spec.md` — Complete user journey maps, screen/surface model, wiring tables, cross-system integration wiring, degraded-mode patterns, Stage 1 traceability index (v1.0, produced 2026-04-22)
- [x] `wiring-artifact-index.md` — Wiring artifact inventory: journey-to-wiring map, surface catalog, data object index, external service index, audit event catalog, cross-system boundary invariants, degraded-mode coverage, Stage 1 source references (v1.0, produced 2026-04-22)
**Wave**: amc-stage2-ux-wiring-spec-20260422  
**Produced By**: foreman-v2-agent (POLC_ORCHESTRATION)  
**CS2 Authorization**: issue #1121  
**Prerequisites**: ✅ Stage 1 complete  
**Completion Date**: 2026-04-22 (CS2 approval confirmed per issue #1121)  
**Approved By**: CS2 (Johan Ras / @APGI-cmy)  
**Approval Reference**: app_management_centre#1121

---

### Stage 3 — Functional Requirements Specification (FRS)

**Status**: 🟡 APPROVAL PENDING — Produced approval-ready 2026-04-23. Awaiting CS2 approval.  
**Location**: `modules/amc/02-frs/`  
**Entry Condition**: ✅ Stage 2 complete and CS2-approved  
**Objective**: Translate the approved Stage 1 App Description and Stage 2 UX Workflow & Wiring Spec into explicit, verifiable, architecture-ready functional requirements. Define what AMC must do, under what conditions, for which actors, with what constraints, and with what required outcomes. Produce a complete traceability artifact showing Stage 1 and Stage 2 derivation.  
**Key Artifacts Created**:
- [x] `functional-requirements-specification.md` — Complete FRS with 17 requirement families (FR-100 to FR-1700), 60+ individual requirements, actor model, authority constraints, business rules, and downstream derivation groupings (v1.0, produced 2026-04-23)
- [x] `app-description-to-frs-traceability.md` — Stage 1 + Stage 2 to FRS traceability matrix demonstrating derivation coverage, cross-system boundary traceability, and dropped/deferred commitment disclosure (v1.0, produced 2026-04-23)
**Wave**: amc-stage3-frs-20260423  
**Produced By**: foreman-v2-agent (POLC_ORCHESTRATION)  
**CS2 Authorization**: issue #1152  
**Prerequisites**: ✅ Stage 1 complete; ✅ Stage 2 complete and CS2-approved (issue #1121)  
**Approval Required**: Yes — CS2 approval required before Stage 4 (TRS) may begin

---

### Stage 4 — Technical Requirements Specification (TRS)

**Status**: ⬜ Not Started  
**Location**: `modules/amc/03-trs/`  
**Prerequisites**: Stage 3 complete and approved  
**Key Artifacts to Create**:
- [ ] `technical-requirements-specification.md`
- [ ] `frs-to-trs-traceability.md` — Traceability matrix

---

### Stage 5 — Architecture

**Status**: ⬜ Not Started  
**Location**: `modules/amc/04-architecture/`  
**Prerequisites**: Stage 4 complete and approved  
**Note — Pre-existing FM-era material**: The `docs/architecture/` directory contains architecture
documents produced for the FM Office app during the FM-origin era. These artifacts are classified
as historical/reference material for the purposes of the new `modules/amc/` 12-stage lifecycle.
Their existence does **not** mean Stage 5 is complete or in progress. Stage 5 (Architecture)
remains Not Started until CS2 explicitly adopts or commissions architecture artifacts through
the canonical lifecycle sequence.

---

### Stage 6 — QA-to-Red

**Status**: ⬜ Not Started  
**Location**: `modules/amc/05-qa-to-red/`  
**Prerequisites**: Stage 5 complete and approved  

---

### Stage 7 — PBFAG

**Status**: ⬜ Not Started  
**Location**: `modules/amc/06-pbfag/`  
**Prerequisites**: Stage 6 complete and approved  
**Note**: PBFAG is a hard gate. It is not situational. It cannot be bypassed without explicit CS2-documented exception.

---

### Stage 8 — Implementation Plan

**Status**: ⬜ Not Started  
**Location**: `modules/amc/07-implementation-plan/`  
**Prerequisites**: Stage 7 (PBFAG) gate passed  

---

### Stage 9 — Builder Checklist

**Status**: ⬜ Not Started  
**Location**: `modules/amc/08-builder-checklist/`  
**Prerequisites**: Stage 8 complete and approved  

---

### Stage 10 — IAA Pre-Brief

**Status**: ⬜ Not Started  
**Location**: `modules/amc/09-iaa-pre-brief/`  
**Prerequisites**: Stage 9 complete and approved  

---

### Stage 11 — Builder Appointment

**Status**: ⬜ Not Started  
**Location**: `modules/amc/10-builder-appointment/`  
**Prerequisites**: Stages 1–10 complete. IAA Pre-Brief published.  
**Note**: No delegation to builders until all Stages 1–10 are complete and gate-passed (HALT-008).

---

### Stage 12 — Build

**Status**: ⬜ Not Started  
**Location**: `modules/amc/11-build/`  
**Prerequisites**: All Stages 1–11 complete. PBFAG PASS.  
**Note**: Build authorization requires all Stages 1–11 complete and PBFAG gate (Stage 7) passed.

---

## Next Action

1. ✅ Stage 1 complete — App Description approved by CS2 (issue #1117, 2026-04-22)
2. ✅ Stage 2 complete — UX Workflow & Wiring Spec approved by CS2 (issue #1121, 2026-04-22)
3. ✅ Stage 3 artifacts produced approval-ready — Awaiting CS2 approval (issue #1152, 2026-04-23)
4. ▶️ CS2 to review and approve Stage 3 FRS before Stage 4 (TRS) begins

---

## References

- [PRE_BUILD_STAGE_MODEL_CANON.md](../../governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md)
- [APP_DESCRIPTION_REQUIREMENT_POLICY.md](../../governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md)
- [app-description.md](./00-app-description/app-description.md) — ✅ approved Stage 1 canonical source
- [app-description-approval.md](./00-app-description/app-description-approval.md) — Stage 1 formal approval record
- [ux-workflow-wiring-spec.md](./01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md) — ✅ Stage 2 artifact (CS2-approved, issue #1121)
- [wiring-artifact-index.md](./01-ux-workflow-wiring-spec/wiring-artifact-index.md) — ✅ Stage 2 artifact (CS2-approved, issue #1121)
- [functional-requirements-specification.md](./02-frs/functional-requirements-specification.md) — 🟡 Stage 3 artifact (pending CS2 approval)
- [app-description-to-frs-traceability.md](./02-frs/app-description-to-frs-traceability.md) — 🟡 Stage 3 artifact (pending CS2 approval)
- [AMC_PRE_BUILD_ARTIFACT_INDEX.md](./AMC_PRE_BUILD_ARTIFACT_INDEX.md)
- [REPO_REALIGNMENT_NOTE.md](./REPO_REALIGNMENT_NOTE.md)

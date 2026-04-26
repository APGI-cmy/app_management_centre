# AMC Build Progress Tracker

**Module**: App Management Centre (AMC)  
**Module Slug**: AMC  
**Last Updated**: 2026-04-26  
**Updated By**: foreman-v2-agent (wave: amc-stage5-architecture-20260426 — Stage 5 Architecture produced; Stage 4 TRS treated as approved per CS2 #1131; issue #1131)

> **Classification**: ACTIVE  
> **Document Role**: PRIMARY LIVE CONTROL DOCUMENT — This is the designated primary operational monitor for AMC pre-build stage progress. CS2 should use this document as the main live progress dashboard.  
> **Canon Reference**: `PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0  
> **Issue**: [app_management_centre#1131](https://github.com/APGI-cmy/app_management_centre/issues/1131)  
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
| 2 | UX Workflow & Wiring Spec | ✅ COMPLETE | CS2-approved 2026-04-22 (issue #1121). Canonical source: `modules/amc/01-ux-workflow-wiring-spec/`. Harmonization pass v1.1 applied 2026-04-23. |
| 3 | FRS | ✅ COMPLETE — CS2 APPROVED | CS2-approved for Stage 4 progression (issue #1123). Harmonization pass v1.1 applied 2026-04-23 (FR-1800 ARC Governance Console family; FR-606/FR-607 quota management). Canonical source: `modules/amc/02-frs/`. |
| 4 | TRS | ✅ TREATED AS APPROVED | Produced approval-ready 2026-04-23, hardened to v1.1 2026-04-23. CS2 authorized Stage 5 progression per issue #1131 ("Stage 4 is now being treated as approved by CS2 and Stage 5 becomes the active governed stage"). Canonical source: `modules/amc/03-trs/`. |
| 5 | Architecture | 🟡 IN PROGRESS — Produced Approval-Pending | Stage 5 Architecture Specification v1.0 produced 2026-04-26. Awaiting CS2 approval. Canonical artifact: `modules/amc/04-architecture/architecture-specification.md`. |
| 6 | QA-to-Red | ⬜ Not Started | 🔴 BLOCKED — requires Stage 5 complete and approved. |
| 7 | PBFAG | ⬜ Not Started | 🔴 BLOCKED |
| 8 | Implementation Plan | ⬜ Not Started | 🔴 BLOCKED |
| 9 | Builder Checklist | ⬜ Not Started | 🔴 BLOCKED |
| 10 | IAA Pre-Brief | ⬜ Not Started | 🔴 BLOCKED |
| 11 | Builder Appointment | ⬜ Not Started | 🔴 BLOCKED |
| 12 | Build | ⬜ Not Started | 🔴 BLOCKED |

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
- [x] `ux-workflow-wiring-spec.md` — Complete user journey maps, screen/surface model, wiring tables, cross-system integration wiring, degraded-mode patterns, Stage 1 traceability index (v1.0, produced 2026-04-22). Harmonization pass v1.1 applied 2026-04-23: explicit ARC Governance Console journey and Dynamic Upload Quota Management Console journey added.
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

**Status**: ✅ COMPLETE — CS2 APPROVED (for Stage 4 progression; harmonization pass applied 2026-04-23)
**Location**: `modules/amc/02-frs/`
**Entry Condition**: ✅ Stage 2 complete and CS2-approved
**Objective**: Translate the approved Stage 1 App Description and Stage 2 UX Workflow & Wiring Spec into explicit, verifiable, architecture-ready functional requirements. Define what AMC must do, under what conditions, for which actors, with what constraints, and with what required outcomes. Produce a complete traceability artifact showing Stage 1 and Stage 2 derivation.
**Key Artifacts Created**:
- [x] `functional-requirements-specification.md` — Complete FRS with 18 requirement families (FR-100 to FR-1800), 65+ individual requirements, actor model, authority constraints, business rules, and downstream derivation groupings (v1.0 produced 2026-04-23; harmonization pass v1.1 applied 2026-04-23: FR-1800 ARC Governance Console family added; operational quota management requirements enhanced)
- [x] `app-description-to-frs-traceability.md` — Stage 1 + Stage 2 to FRS traceability matrix demonstrating derivation coverage, cross-system boundary traceability, and dropped/deferred commitment disclosure (v1.0, produced 2026-04-23)
**Wave**: amc-stage3-frs-20260423; harmonization pass: amc-harmonize-stages1-4-20260423
**Produced By**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: issue #1123 (original Stage 3 approval and harmonization pass trace reference; harmonization wave: amc-harmonize-stages1-4-20260423)
**Prerequisites**: ✅ Stage 1 complete; ✅ Stage 2 complete and CS2-approved (issue #1121)
**Approval Required**: Yes — CS2-approved for Stage 4 (TRS) progression
**Completion Date**: 2026-04-23
**Approved By**: CS2 (Johan Ras / @APGI-cmy) — approved for Stage 4 progression
**Approval Reference**: app_management_centre#1123
**Notes**: Stage 3 FRS formally CS2-approved for Stage 4 progression (issue #1123). Harmonization pass v1.1 applied 2026-04-23: FR-1800 ARC Governance Console family added; FR-606/FR-607 operational quota management requirements added.

---

### Stage 4 — Technical Requirements Specification (TRS)

**Status**: ✅ TREATED AS APPROVED — CS2 authorized Stage 5 progression per issue #1131 (2026-04-26)
**Location**: `modules/amc/03-trs/`
**Entry Condition**: ✅ Stage 3 complete and CS2-approved
**Objective**: Translate the approved Stage 3 FRS into explicit technical requirements without drifting from upstream truth. Define the technical realization constraints for AMC, including API/interface requirements, event and action contracts, data/state ownership and persistence rules, schema-facing technical requirements, integration requirements for AMC ↔ AIMC ↔ AIMCC ↔ KUC ↔ knowledge/memory system ↔ Foreman/agents, authentication/authorization enforcement requirements, degraded-mode technical behavior, audit/provenance technical requirements, ARC technical domain, operational quota management technical domain, and state consistency and cross-device continuity requirements.
**Key Artifacts Created**:
- [x] `technical-requirements-specification.md` — Complete TRS v1.1 with 18 TR domain families (TR-100 to TR-1800), API contract definitions, schema requirements, integration contracts, ARC technical domain, dynamic upload quota management console, alert timing/retry/escalation contract family, audit delivery atomicity, inter-service trust boundary, state/auth/audit contract family declarations, deferred items register, and CS2 sign-off section (v1.1, hardened 2026-04-23; upstream sources updated to v1.1 per harmonization pass)
- [x] `frs-to-trs-traceability.md` — FRS to TRS traceability matrix v1.1: 17 FRS families + ARC domain traced, 18 business rules realized, no family dropped, 30 Stage-5 deferrals disclosed, ARC and quota console coverage added (v1.1, hardened 2026-04-23)
**Wave**: amc-harmonize-stages1-4-20260423; amc-stage4-trs-hardening-20260423
**Produced By**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: issue #1125; harmonization wave: amc-harmonize-stages1-4-20260423
**Hardening Wave**: issue #1127 (harmonization/hardening follow-on)
**Prerequisites**: ✅ Stage 1 complete; ✅ Stage 2 complete and CS2-approved; ✅ Stage 3 complete and CS2-approved (issue #1123)
**Approval Required**: Yes — CS2 approval required before Stage 5 (Architecture) may begin

---

### Stage 5 — Architecture

**Status**: 🟡 IN PROGRESS — Produced Approval-Pending (2026-04-26)
**Location**: `modules/amc/04-architecture/`
**Entry Condition**: ✅ Stage 4 TRS treated as approved per CS2 issue #1131 (2026-04-26)
**Objective**: Translate the approved Stage 4 TRS into an explicit, non-contradictory system architecture for AMC, including component boundaries, service responsibilities, data/state ownership, trust boundaries, integration paths, event flows, and deployment-shaping architectural decisions.
**Key Artifacts Created**:
- [x] `architecture-specification.md` — Complete Stage 5 Architecture Specification v1.0 (produced 2026-04-26): core architecture structure, ARC domain, Dynamic Upload Quota Management console, cross-system interaction architecture, state/audit/resilience architecture, trust boundaries, deployment-shaping decisions, CS2 sign-off section
- [x] `trs-to-architecture-traceability.md` — TRS to Architecture Traceability v1.0 (produced 2026-04-26): 18/18 TRS families realized, 0 silently dropped, Stage 6 deferrals disclosed, cross-system boundary preservation check, acceptance criteria verification
**Wave**: amc-stage5-architecture-20260426
**Produced By**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: issue #1131 (Stage 5 kickoff; Stage 4 treated as approved for Stage 5 progression)
**Prerequisites**: ✅ Stage 4 TRS v1.1 produced and treated as approved per CS2 (#1131)
**Approval Required**: Yes — CS2 approval required before Stage 6 (QA-to-Red) may begin
**Note — Pre-existing FM-era material**: The `docs/architecture/` directory contains architecture documents from the FM-origin era. These remain classified as historical/reference material only. The canonical Stage 5 architecture is `modules/amc/04-architecture/architecture-specification.md` v1.0. The `architecture.md` placeholder stub has been updated with a superseded notice pointing to the canonical artifact.

---

### Stage 6 — QA-to-Red

**Status**: ⬜ Not Started  
**Location**: `modules/amc/05-qa-to-red/`  
**Prerequisites**: Stage 5 complete and **CS2 approved** — 🔴 BLOCKED pending Stage 5 CS2 approval

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

1. ✅ Stage 1 complete — App Description approved by CS2 (issue #1117, 2026-04-22). Harmonization pass v1.1 applied 2026-04-23.
2. ✅ Stage 2 complete — UX Workflow & Wiring Spec approved by CS2 (issue #1121, 2026-04-22). Harmonization pass v1.1 applied 2026-04-23.
3. ✅ Stage 3 complete — FRS CS2-approved for Stage 4 progression (issue #1123, 2026-04-23). Harmonization pass v1.1 applied 2026-04-23.
4. ✅ Stage 4 TRS artifacts produced approval-ready and hardened to v1.1 (issue #1125, hardened in #1127, 2026-04-23). CS2 authorized Stage 5 progression per issue #1131 — Stage 4 treated as approved.
5. 🟡 Stage 5 Architecture Specification v1.0 produced approval-pending (wave amc-stage5-architecture-20260426, 2026-04-26).
6. ▶️ CS2 to review and approve Stage 5 Architecture before Stage 6 (QA-to-Red) begins.

---

## References

- [PRE_BUILD_STAGE_MODEL_CANON.md](../../governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md)
- [APP_DESCRIPTION_REQUIREMENT_POLICY.md](../../governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md)
- [app-description.md](./00-app-description/app-description.md) — ✅ approved Stage 1 canonical source (harmonization pass v1.1 applied 2026-04-23)
- [app-description-approval.md](./00-app-description/app-description-approval.md) — Stage 1 formal approval record
- [ux-workflow-wiring-spec.md](./01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md) — ✅ Stage 2 artifact (CS2-approved, issue #1121; harmonization pass v1.1 applied 2026-04-23)
- [wiring-artifact-index.md](./01-ux-workflow-wiring-spec/wiring-artifact-index.md) — ✅ Stage 2 artifact (CS2-approved, issue #1121)
- [functional-requirements-specification.md](./02-frs/functional-requirements-specification.md) — ✅ Stage 3 artifact (CS2-approved, issue #1123; harmonization pass v1.1 applied 2026-04-23)
- [app-description-to-frs-traceability.md](./02-frs/app-description-to-frs-traceability.md) — ✅ Stage 3 artifact (CS2-approved, issue #1123)
- [technical-requirements-specification.md](./03-trs/technical-requirements-specification.md) — ✅ Stage 4 artifact (treated as approved per CS2 issue #1131; Stage 5 progression authorized)
- [frs-to-trs-traceability.md](./03-trs/frs-to-trs-traceability.md) — ✅ Stage 4 artifact (treated as approved per CS2 issue #1131)
- [architecture-specification.md](./04-architecture/architecture-specification.md) — 🟡 Stage 5 artifact (produced approval-pending, 2026-04-26; wave amc-stage5-architecture-20260426; CS2 authorization: issue #1131)
- [trs-to-architecture-traceability.md](./04-architecture/trs-to-architecture-traceability.md) — 🟡 Stage 5 artifact (produced approval-pending, 2026-04-26)
- [AMC_PRE_BUILD_ARTIFACT_INDEX.md](./AMC_PRE_BUILD_ARTIFACT_INDEX.md)
- [REPO_REALIGNMENT_NOTE.md](./REPO_REALIGNMENT_NOTE.md)

# AMC Pre-Build Artifact Index

**Module**: App Management Centre (AMC)  
**Lifecycle Model**: 12-Stage Pre-Build Sequence (PRE_BUILD_STAGE_MODEL_CANON.md v1.0.0)  
**Last Updated**: 2026-04-23  
**Authority**: Maturion Foreman / CS2

---

## Purpose

This index catalogs all pre-build artifacts for the AMC module, mapped to their lifecycle stage. It tracks what exists, where it lives, and what its current authority status is.

---

## Stage 1 — App Description

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| App Description | `modules/amc/00-app-description/app-description.md` | ✅ Approved Canonical | v1.0, CS2-approved 2026-04-22. Sole authoritative Stage 1 source. Approval ref: #1117. |
| App Description Approval | `modules/amc/00-app-description/app-description-approval.md` | ✅ Complete | Formal Stage 1 approval record. All fields populated. CS2 ref: #1117. |
| AMC Role Authority & Operating Model | `modules/amc/00-app-description/amc-role-authority-and-operating-model.md` | ⬜ Placeholder | Not complete — document remains a placeholder; authority wording updated to reflect Stage 1 approval. Follow-on work required. Does not block Stage 2. |
| FM App Description (superseded) | `docs/governance/FM_APP_DESCRIPTION.md` | 📦 Superseded | Retained as historical/provenance reference only. No longer the active canonical Stage 1 source. |
| App Description (root pointer) | `APP_DESCRIPTION.md` | 📌 Reference Only | Follow-on update to point to new canonical location pending |

---

## Stage 2 — UX Workflow & Wiring Spec

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| UX Workflow & Wiring Spec | `modules/amc/01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md` | 🟡 Approval Pending | v1.0, approval pending. Index status held to match current document header until CS2 approval is reflected in the artifact. Issue #1121. |
| Wiring Artifact Index | `modules/amc/01-ux-workflow-wiring-spec/wiring-artifact-index.md` | 🟡 Approval Pending | v1.0, approval pending. Index status held to match current document header until CS2 approval is reflected in the artifact. Issue #1121. |

---

## Stage 3 — FRS

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Functional Requirements Specification | `modules/amc/02-frs/functional-requirements-specification.md` | 🟡 Approval Pending | v1.0, produced approval-ready 2026-04-23. CS2 approval required before Stage 4 begins. Issue #1123. |
| App Description to FRS Traceability | `modules/amc/02-frs/app-description-to-frs-traceability.md` | 🟡 Approval Pending | v1.0, produced approval-ready 2026-04-23. Stage 1 + Stage 2 to FRS derivation matrix. Issue #1123. |

---

## Stage 4 — TRS

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Technical Requirements Specification | `modules/amc/03-trs/technical-requirements-specification.md` | ⬜ Placeholder | Not started |
| FRS to TRS Traceability | `modules/amc/03-trs/frs-to-trs-traceability.md` | ⬜ Placeholder | Not started |

---

## Stage 5 — Architecture

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Architecture | `modules/amc/04-architecture/architecture.md` | ⬜ Placeholder | Not started |
| Architecture Decision Records | `modules/amc/04-architecture/architecture-decision-records.md` | ⬜ Placeholder | Not started |
| Architecture Completeness Checklist | `modules/amc/04-architecture/architecture-completeness-checklist.md` | ⬜ Placeholder | Not started |

> **Note — Pre-existing FM-era architecture material**: `docs/architecture/` contains architecture documents produced for the FM Office app during the FM-origin era. These artifacts are classified as **FM-era / pre-12-stage reference material** and are preserved for historical context and traceability only. They have **not** been adopted as the canonical Stage 5 architecture for the new `modules/amc/` lifecycle. Stage 5 therefore remains **Not Started**. Any adoption or migration of those artifacts into the AMC 12-stage lifecycle requires explicit classification, a migration/adoption note, a tracker update, and CS2-approved lifecycle interpretation.

---

## Stage 6 — QA-to-Red

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| QA-to-Red Suite | `modules/amc/05-qa-to-red/qa-to-red-suite.md` | ⬜ Placeholder | Not started |
| QA Catalog Alignment | `modules/amc/05-qa-to-red/qa-catalog-alignment.md` | ⬜ Placeholder | Not started |

---

## Stage 7 — PBFAG

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| PBFAG Checklist | `modules/amc/06-pbfag/pbfag-checklist.md` | ⬜ Placeholder | Gate artifact — not started |
| Golden Path Verification Pack | `modules/amc/06-pbfag/golden-path-verification-pack.md` | ⬜ Placeholder | Not started |
| Runtime Deployment Contract | `modules/amc/06-pbfag/runtime-deployment-contract.md` | ⬜ Placeholder | Not started |

---

## Stage 8 — Implementation Plan

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Implementation Plan | `modules/amc/07-implementation-plan/implementation-plan.md` | ⬜ Placeholder | Not started |
| Wave Breakdown | `modules/amc/07-implementation-plan/wave-breakdown.md` | ⬜ Placeholder | Not started |

---

## Stage 9 — Builder Checklist

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Builder Checklist | `modules/amc/08-builder-checklist/builder-checklist.md` | ⬜ Placeholder | Not started |
| Builder Readiness Attestations | `modules/amc/08-builder-checklist/builder-readiness-attestations.md` | ⬜ Placeholder | Not started |

---

## Stage 10 — IAA Pre-Brief

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| IAA Pre-Brief | `modules/amc/09-iaa-pre-brief/iaa-pre-brief.md` | ⬜ Placeholder | Not started |
| IAA Pre-Brief Response | `modules/amc/09-iaa-pre-brief/iaa-pre-brief-response.md` | ⬜ Placeholder | Not started |

---

## Stage 11 — Builder Appointment

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Builder Appointment | `modules/amc/10-builder-appointment/builder-appointment.md` | ⬜ Placeholder | Not started |
| Builder Contract | `modules/amc/10-builder-appointment/builder-contract.md` | ⬜ Placeholder | Not started |

---

## Stage 12 — Build

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Build Evidence Index | `modules/amc/11-build/build-evidence-index.md` | ⬜ Placeholder | Not started |
| QA-to-Green Evidence | `modules/amc/11-build/qa-to-green-evidence.md` | ⬜ Placeholder | Not started |
| Handover | `modules/amc/11-build/handover.md` | ⬜ Placeholder | Not started |

---

## Legacy

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| FM-era artifacts | `modules/amc/_legacy/foreman-app-origin/` | 📦 Legacy Area | Designated holding location for FM-origin historical artifacts. No artifacts moved yet — pending identification and CS2 approval. |

---

**Legend**: ✅ Active/Complete | 📌 Reference Only | ⬜ Placeholder/Not Started | 📦 Legacy Area

# AMC Pre-Build Artifact Index

**Module**: App Management Centre (AMC)  
**Lifecycle Model**: 12-Stage Pre-Build Sequence + Stage 5a (PRE_BUILD_STAGE_MODEL_CANON.md v1.0.0; AMC-GOV-OVERSIGHT-001)  
**Last Updated**: 2026-07-01 (CS2 disposition pack for Stages 5, 5a, 6, and 7 added for review - PR #1194. Stage 7 PBFAG functional-delivery / deployment-execution / QA retrofit artifacts produced for CS2 review - wave amc-stage7-pbfag-retrofit-20260630; issue #1193; PR #1194. Prior: Stage 6 QA-to-Red functional-delivery retrofit merged as approval-pending reference input - issue #1191; PR #1192. Prior: Stage 5a retrofit merged as approval-pending reference input - issue #1189; PR #1190. Prior: Stage 5 architecture retrofit merged as approval-pending reference input - issue #1187; PR #1188. Prior: Stage 1-4 retrofit merged - issue #1185; PR #1186.)  
**Authority**: Maturion Foreman / CS2

---

## Purpose

This index catalogs all pre-build artifacts for the AMC module, mapped to their lifecycle stage. It tracks what exists, where it lives, and what its current authority status is.

---

## Stage 1 - App Description

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| App Description | `modules/amc/00-app-description/app-description.md` | ✅ Approved Canonical | v1.0, CS2-approved 2026-04-22. Sole authoritative Stage 1 source. Approval ref: #1117. |
| App Description Approval | `modules/amc/00-app-description/app-description-approval.md` | ✅ Complete | Formal Stage 1 approval record. |
| Functional Delivery Definition | `modules/amc/00-app-description/functional-delivery-definition.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1186. Adds fully functional delivery definition. CS2 disposition required as part of retrofit chain. |
| AMC Role Authority & Operating Model | `modules/amc/00-app-description/amc-role-authority-and-operating-model.md` | ⬜ Placeholder | Follow-on work required. Does not block Stage 2. |
| FM App Description (superseded) | `docs/governance/FM_APP_DESCRIPTION.md` | 📦 Superseded | Retained as historical/provenance reference only. |
| App Description (root pointer) | `APP_DESCRIPTION.md` | 📌 Reference Only | Follow-on update to point to canonical location pending. |

---

## Stage 2 - UX Workflow & Wiring Spec

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| UX Workflow & Wiring Spec | `modules/amc/01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md` | ✅ Approved Canonical | v1.1, CS2-approved 2026-04-22. |
| Wiring Artifact Index | `modules/amc/01-ux-workflow-wiring-spec/wiring-artifact-index.md` | ✅ Approved Canonical | v1.0, CS2-approved 2026-04-22. |
| CTA/API/Data/Audit Contract Matrix | `modules/amc/01-ux-workflow-wiring-spec/cta-api-data-audit-contract-matrix.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1186. Canonical endpoint/event authority remains with Stage 4 TRS. CS2 disposition required as part of retrofit chain. |

---

## Stage 3 - FRS

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Functional Requirements Specification | `modules/amc/02-frs/functional-requirements-specification.md` | ✅ Approved Canonical | v1.1, CS2-approved for Stage 4 progression 2026-04-23. |
| App Description to FRS Traceability | `modules/amc/02-frs/app-description-to-frs-traceability.md` | ✅ Approved Canonical | v1.0, CS2-approved for Stage 4 progression 2026-04-23. |
| Functional Delivery Requirements Addendum | `modules/amc/02-frs/functional-delivery-requirements-addendum.md` | 🟡 Retrofit Reference Input | FR-1900 produced/merged in PR #1186. CS2 disposition required as part of retrofit chain. |

---

## Stage 4 - TRS

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Technical Requirements Specification | `modules/amc/03-trs/technical-requirements-specification.md` | 🟠 Treated as Approved | v1.1, hardened approval-ready 2026-04-23. Formal CS2 approval pending. |
| FRS to TRS Traceability | `modules/amc/03-trs/frs-to-trs-traceability.md` | 🟠 Treated as Approved | v1.1, hardened 2026-04-23. |
| Functional Delivery Technical Requirements Addendum | `modules/amc/03-trs/functional-delivery-technical-requirements-addendum.md` | 🟡 Retrofit Reference Input | TR-1900, including TR-1910, produced/merged in PR #1186. CS2 disposition required as part of retrofit chain. |

---

## Stage 5 - Architecture

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Architecture Specification | `modules/amc/04-architecture/architecture-specification.md` | 🟡 Approval Pending | v1.0, produced 2026-04-26. CS2 approval required. |
| TRS-to-Architecture Traceability | `modules/amc/04-architecture/trs-to-architecture-traceability.md` | 🟡 Approval Pending | v1.0, produced 2026-04-26. |
| Functional Delivery Architecture Addendum | `modules/amc/04-architecture/functional-delivery-architecture-addendum.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1188. CS2 disposition required. |
| Functional Delivery Architecture Map | `modules/amc/04-architecture/functional-delivery-architecture-map.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1188. Route/action/state/audit/degraded-mode map for Stage 6/7 derivation. CS2 disposition required. |
| Stage 5 Functional Delivery Change-Propagation Audit | `modules/amc/04-architecture/stage5-functional-delivery-change-propagation-audit.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1188. Conditional pass for retrofit production; not build-ready and not Stage-8-ready. |
| Stage 5 Review Notes | `modules/amc/04-architecture/stage5-review-notes.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1188. |
| Stage 5 Coverage Note | `modules/amc/04-architecture/extra-review-note.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1188. |
| Architecture (superseded placeholder) | `modules/amc/04-architecture/architecture.md` | ⛔ Superseded | `architecture-specification.md` is the canonical Stage 5 artifact. |
| Architecture Decision Records | `modules/amc/04-architecture/architecture-decision-records.md` | ⬜ Placeholder | Not started. |
| Architecture Completeness Checklist | `modules/amc/04-architecture/architecture-completeness-checklist.md` | ⬜ Placeholder | Not started / remains a placeholder unless separately populated. |

---

## Stage 5a - Deployment Execution Strategy

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Deployment Execution Strategy | `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` | 🟡 Approval Pending | v1.0, produced 2026-04-27. CS2 approval required. |
| Deployment Surface Ownership Table | `modules/amc/05a-deployment-execution-strategy/deployment-surface-ownership-table.md` | 🟡 Approval Pending | v1.0, produced 2026-04-27. |
| Runner and Environment Constraints | `modules/amc/05a-deployment-execution-strategy/runner-and-environment-constraints.md` | 🟡 Approval Pending | v1.0, produced 2026-04-27. |
| Functional Delivery Deployment Execution Addendum | `modules/amc/05a-deployment-execution-strategy/functional-delivery-deployment-execution-addendum.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1190. Imports TR-1910, Stage 5 architecture map, deployment evidence, runtime health/smoke validation, dependency readiness, and no-operational-speculation controls. CS2 disposition required. |
| Deployment Execution Validation Matrix | `modules/amc/05a-deployment-execution-strategy/deployment-execution-validation-matrix.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1190. Adds workflow, environment, migration, protected approval, health, rollback, dependency, audit, and evidence validation obligations for Stage 6/7 derivation. CS2 disposition required. |
| Stage 5a Functional Delivery Change-Propagation Audit | `modules/amc/05a-deployment-execution-strategy/stage5a-functional-delivery-change-propagation-audit.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1190. Conditional pass for Stage 5a retrofit production; not build-ready and not Stage-8-ready. |
| Governance Oversight Record | `modules/amc/governance-oversight/DEPLOYMENT_STRATEGY_OVERSIGHT.md` | ✅ Complete | Formal oversight record. CS2 auth: #1133. |

---

## Stage 6 - QA-to-Red

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| QA-to-Red Specification | `modules/amc/05-qa-to-red/qa-to-red-specification.md` | 🟡 Approval Pending | v1.0, produced 2026-04-27. Must be reviewed with Stage 6 retrofit artifacts. |
| Architecture and DES to QA Traceability | `modules/amc/05-qa-to-red/architecture-and-des-to-qa-traceability.md` | 🟡 Approval Pending | v1.0, produced 2026-04-27. Must be reconciled with Stage 5/5a retrofit maps before Stage 8. |
| Red Test Catalog | `modules/amc/05-qa-to-red/red-test-catalog.md` | 🟡 Approval Pending | v1.0, produced 2026-04-27. 79 test cases across 20 families. Retrofit adds QA-FD and QA-DEPLOY families. |
| Functional Delivery QA-to-Red Addendum | `modules/amc/05-qa-to-red/functional-delivery-qa-to-red-addendum.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1192. Imports Stage 1-5a functional-delivery and deployment-execution obligations into Stage 6. CS2 disposition required. |
| Functional Delivery RED Test Expansion Matrix | `modules/amc/05-qa-to-red/functional-delivery-red-test-expansion-matrix.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1192. Defines QA-FD and QA-DEPLOY RED test families. CS2 disposition required. |
| Stage 6 Functional Delivery Change-Propagation Audit | `modules/amc/05-qa-to-red/stage6-functional-delivery-change-propagation-audit.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1192. Conditional pass for Stage 6 retrofit production; not build-ready and not Stage-8-ready. |
| QA-to-Red Suite (superseded placeholder) | `modules/amc/05-qa-to-red/qa-to-red-suite.md` | ⛔ Superseded | Placeholder superseded by qa-to-red-specification.md v1.0. |
| QA Catalog Alignment (superseded placeholder) | `modules/amc/05-qa-to-red/qa-catalog-alignment.md` | ⛔ Superseded | Placeholder superseded by architecture-and-des-to-qa-traceability.md v1.0. |

---

## Stage 7 - PBFAG

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Pre-Build Final Assurance Gate | `modules/amc/06-pbfag/pre-build-final-assurance-gate.md` | 🟡 Approval Pending | Must be reconciled with Stage 5/5a/6 retrofit obligations before Stage 8. |
| PBFAG Evidence Matrix | `modules/amc/06-pbfag/pbfag-evidence-matrix.md` | 🟡 Approval Pending | Must include tracker/index agreement for new retrofit artifacts before final Stage 8 disposition. |
| PBFAG Findings and Verdict | `modules/amc/06-pbfag/pbfag-findings-and-verdict.md` | 🟡 Approval Pending | Stage 8 gate remains conditional. |
| PBFAG Checklist | `modules/amc/06-pbfag/pbfag-checklist.md` | 🟡 Approval Pending | References canonical PBFAG artifacts. |
| Stage 1-4 Functional Delivery Change-Propagation Audit | `modules/amc/06-pbfag/stage1-4-functional-delivery-change-propagation-audit.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1186 chain and retained as upstream disposition input. CS2 disposition required. |
| Functional Delivery PBFAG Addendum | `modules/amc/06-pbfag/functional-delivery-pbfag-addendum.md` | 🟡 Retrofit Produced for CS2 Review | Produced in issue #1193 / PR #1194. Imports Stage 5/5a/6 retrofit obligations into Stage 7. |
| PBFAG Retrofit Evidence Matrix | `modules/amc/06-pbfag/pbfag-retrofit-evidence-matrix.md` | 🟡 Retrofit Produced for CS2 Review | Produced in issue #1193 / PR #1194. Maps Stage 5/5a/6 obligations to PBFAG gate checks. |
| Stage 7 Functional Delivery Change-Propagation Audit | `modules/amc/06-pbfag/stage7-functional-delivery-change-propagation-audit.md` | 🟡 Retrofit Produced for CS2 Review | Produced in issue #1193 / PR #1194. Conditional pass for Stage 7 retrofit production; not build-ready and not Stage-8-ready. |
| CS2 Disposition Pack - Stages 5, 5a, 6, and 7 | `modules/amc/06-pbfag/cs2-disposition-pack-stages-5-5a-6-7.md` | 🟡 Prepared for CS2 Review | Produced in PR #1194. Summarises readiness, blockers, risks, conditions, and recommended CS2 disposition. Does not authorize Stage 8. |

---

## Stage 8 - Implementation Plan

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Implementation Plan | `modules/amc/07-implementation-plan/implementation-plan.md` | ⬜ Placeholder | Not started. |
| Wave Breakdown | `modules/amc/07-implementation-plan/wave-breakdown.md` | ⬜ Placeholder | Not started. |

---

## Stage 9 - Builder Checklist

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Builder Checklist | `modules/amc/08-builder-checklist/builder-checklist.md` | ⬜ Placeholder | Not started. |
| Builder Readiness Attestations | `modules/amc/08-builder-checklist/builder-readiness-attestations.md` | ⬜ Placeholder | Not started. |

---

## Stage 10 - IAA Pre-Brief

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| IAA Pre-Brief | `modules/amc/09-iaa-pre-brief/iaa-pre-brief.md` | ⬜ Placeholder | Not started. |
| IAA Pre-Brief Response | `modules/amc/09-iaa-pre-brief/iaa-pre-brief-response.md` | ⬜ Placeholder | Not started. |

---

## Stage 11 - Builder Appointment

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Builder Appointment | `modules/amc/10-builder-appointment/builder-appointment.md` | ⬜ Placeholder | Not started. |
| Builder Contract | `modules/amc/10-builder-appointment/builder-contract.md` | ⬜ Placeholder | Not started. |

---

## Stage 12 - Build

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Build Evidence Index | `modules/amc/11-build/build-evidence-index.md` | ⬜ Placeholder | Not started. |
| QA-to-Green Evidence | `modules/amc/11-build/qa-to-green-evidence.md` | ⬜ Placeholder | Not started. |
| Handover | `modules/amc/11-build/handover.md` | ⬜ Placeholder | Not started. |

---

## Legacy

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| FM-era artifacts | `modules/amc/_legacy/foreman-app-origin/` | 📦 Legacy Area | Historical artifacts only. |

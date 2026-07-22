# AMC Pre-Build Artifact Index

**Module**: App Management Centre (AMC)  
**Lifecycle Model**: 12-Stage Pre-Build Sequence + Stage 5a (`PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0; AMC-GOV-OVERSIGHT-001)  
**Last Updated**: 2026-07-22 (PR #1209 merged the W1 reconciliation and explicit BLOCKED CS2 disposition. Issue #1210 / PR #1211 is the sole residual-blocker closure and final candidate re-attestation wave. Stages 10–12 remain blocked.)  
**Authority**: Maturion Foreman / CS2

---

## Purpose

This index catalogs all pre-build artifacts for the AMC module, mapped to their lifecycle stage. It tracks what exists, where it lives, and what its current authority status is.

---

## Stage 1 — App Description

| Artifact | Location | Status | Notes |
|---|---|---|---|
| App Description | `modules/amc/00-app-description/app-description.md` | ✅ Approved Canonical | v1.0, CS2-approved 2026-04-22. Sole authoritative Stage 1 source. Approval ref: #1117. |
| App Description Approval | `modules/amc/00-app-description/app-description-approval.md` | ✅ Complete | Formal Stage 1 approval record. |
| Functional Delivery Definition | `modules/amc/00-app-description/functional-delivery-definition.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1186. Adds fully functional delivery definition. |
| AMC Role Authority & Operating Model | `modules/amc/00-app-description/amc-role-authority-and-operating-model.md` | ⬜ Placeholder | Follow-on work required. Does not block Stage 2. |
| FM App Description (superseded) | `docs/governance/FM_APP_DESCRIPTION.md` | 📦 Superseded | Retained as historical/provenance reference only. |
| App Description (root pointer) | `APP_DESCRIPTION.md` | 📌 Reference Only | Follow-on update to point to canonical location pending. |

---

## Stage 2 — UX Workflow & Wiring Spec

| Artifact | Location | Status | Notes |
|---|---|---|---|
| UX Workflow & Wiring Spec | `modules/amc/01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md` | ✅ Approved Canonical | v1.1, CS2-approved 2026-04-22. |
| Wiring Artifact Index | `modules/amc/01-ux-workflow-wiring-spec/wiring-artifact-index.md` | ✅ Approved Canonical | v1.0, CS2-approved 2026-04-22. |
| CTA/API/Data/Audit Contract Matrix | `modules/amc/01-ux-workflow-wiring-spec/cta-api-data-audit-contract-matrix.md` | 🟡 Retrofit Reference Input | Produced/merged in PR #1186. Canonical endpoint/event authority remains with Stage 4 TRS. |

---

## Stage 3 — FRS

| Artifact | Location | Status | Notes |
|---|---|---|---|
| Functional Requirements Specification | `modules/amc/02-frs/functional-requirements-specification.md` | ✅ Approved Canonical | v1.1, CS2-approved for Stage 4 progression 2026-04-23. |
| App Description to FRS Traceability | `modules/amc/02-frs/app-description-to-frs-traceability.md` | ✅ Approved Canonical | v1.0, CS2-approved for Stage 4 progression 2026-04-23. |
| Functional Delivery Requirements Addendum | `modules/amc/02-frs/functional-delivery-requirements-addendum.md` | 🟡 Retrofit Reference Input | FR-1900 produced/merged in PR #1186. |

---

## Stage 4 — TRS

| Artifact | Location | Status | Notes |
|---|---|---|---|
| Technical Requirements Specification | `modules/amc/03-trs/technical-requirements-specification.md` | 🟠 Treated as Approved | v1.1, hardened approval-ready 2026-04-23. Formal CS2 approval pending. |
| FRS to TRS Traceability | `modules/amc/03-trs/frs-to-trs-traceability.md` | 🟠 Treated as Approved | v1.1, hardened 2026-04-23. |
| Functional Delivery Technical Requirements Addendum | `modules/amc/03-trs/functional-delivery-technical-requirements-addendum.md` | 🟡 Retrofit Reference Input | TR-1900, including TR-1910, produced/merged in PR #1186. |

---

## Stage 5 — Architecture

| Artifact | Location | Status | Notes |
|---|---|---|---|
| Architecture Specification | `modules/amc/04-architecture/architecture-specification.md` | ✅ CS2 Approved with Conditions | Approved by CS2 decision record in issue #1197; Stage 5 retrofit obligations remain binding inputs. |
| TRS-to-Architecture Traceability | `modules/amc/04-architecture/trs-to-architecture-traceability.md` | ✅ CS2 Approved with Conditions | Approved by CS2 decision record in issue #1197. |
| Functional Delivery Architecture Addendum | `modules/amc/04-architecture/functional-delivery-architecture-addendum.md` | ✅ CS2 Approved with Conditions | Produced/merged in PR #1188. Binding downstream input. |
| Functional Delivery Architecture Map | `modules/amc/04-architecture/functional-delivery-architecture-map.md` | ✅ CS2 Approved with Conditions | Route/action/state/audit/degraded-mode map remains binding. |
| Stage 5 Functional Delivery Change-Propagation Audit | `modules/amc/04-architecture/stage5-functional-delivery-change-propagation-audit.md` | ✅ CS2 Approved with Conditions | Conditions carried forward. |
| Stage 5 Review Notes | `modules/amc/04-architecture/stage5-review-notes.md` | ✅ CS2 Approved with Conditions | Produced/merged in PR #1188. |
| Stage 5 Coverage Note | `modules/amc/04-architecture/extra-review-note.md` | ✅ CS2 Approved with Conditions | Produced/merged in PR #1188. |
| Architecture (superseded placeholder) | `modules/amc/04-architecture/architecture.md` | ⛔ Superseded | `architecture-specification.md` is the canonical Stage 5 artifact. |
| Architecture Decision Records | `modules/amc/04-architecture/architecture-decision-records.md` | ⬜ Placeholder | Not started. |
| Architecture Completeness Checklist | `modules/amc/04-architecture/architecture-completeness-checklist.md` | ⬜ Placeholder | Not started. |

---

## Stage 5a — Deployment Execution Strategy

| Artifact | Location | Status | Notes |
|---|---|---|---|
| Deployment Execution Strategy | `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` | ✅ CS2 Approved with Conditions | Approved by CS2 decision record in issue #1197. |
| Deployment Surface Ownership Table | `modules/amc/05a-deployment-execution-strategy/deployment-surface-ownership-table.md` | ✅ CS2 Approved with Conditions | Deployment ownership remains binding. |
| Runner and Environment Constraints | `modules/amc/05a-deployment-execution-strategy/runner-and-environment-constraints.md` | ✅ CS2 Approved with Conditions | Runner and environment constraints remain binding. |
| Functional Delivery Deployment Execution Addendum | `modules/amc/05a-deployment-execution-strategy/functional-delivery-deployment-execution-addendum.md` | ✅ CS2 Approved with Conditions | Produced/merged in PR #1190. Binding downstream input. |
| Deployment Execution Validation Matrix | `modules/amc/05a-deployment-execution-strategy/deployment-execution-validation-matrix.md` | ✅ CS2 Approved with Conditions | CI, preview, secret, migration, rollback, health/smoke, and dependency conditions remain binding. |
| Stage 5a Functional Delivery Change-Propagation Audit | `modules/amc/05a-deployment-execution-strategy/stage5a-functional-delivery-change-propagation-audit.md` | ✅ CS2 Approved with Conditions | Conditions carried forward. |
| Governance Oversight Record | `modules/amc/governance-oversight/DEPLOYMENT_STRATEGY_OVERSIGHT.md` | ✅ Complete | Formal oversight record. CS2 auth: #1133. |

---

## Stage 6 — QA-to-Red

| Artifact | Location | Status | Notes |
|---|---|---|---|
| QA-to-Red Specification | `modules/amc/05-qa-to-red/qa-to-red-specification.md` | ✅ CS2 Approved with Conditions | Approved by CS2 decision record in issue #1197. |
| Architecture and DES to QA Traceability | `modules/amc/05-qa-to-red/architecture-and-des-to-qa-traceability.md` | ✅ CS2 Approved with Conditions | Must be carried downstream. |
| Red Test Catalog | `modules/amc/05-qa-to-red/red-test-catalog.md` | ✅ CS2 Approved with Conditions | Retrofit adds QA-FD and QA-DEPLOY families. |
| Functional Delivery QA-to-Red Addendum | `modules/amc/05-qa-to-red/functional-delivery-qa-to-red-addendum.md` | ✅ CS2 Approved with Conditions | Produced/merged in PR #1192. Binding downstream input. |
| Functional Delivery RED Test Expansion Matrix | `modules/amc/05-qa-to-red/functional-delivery-red-test-expansion-matrix.md` | ✅ CS2 Approved with Conditions | QA-FD and QA-DEPLOY rows remain binding. |
| Stage 6 Functional Delivery Change-Propagation Audit | `modules/amc/05-qa-to-red/stage6-functional-delivery-change-propagation-audit.md` | ✅ CS2 Approved with Conditions | Conditions carried forward. |
| QA-to-Red Suite (superseded placeholder) | `modules/amc/05-qa-to-red/qa-to-red-suite.md` | ⛔ Superseded | Placeholder superseded by `qa-to-red-specification.md` v1.0. |
| QA Catalog Alignment (superseded placeholder) | `modules/amc/05-qa-to-red/qa-catalog-alignment.md` | ⛔ Superseded | Placeholder superseded by `architecture-and-des-to-qa-traceability.md` v1.0. |

---

## Stage 7 — PBFAG

| Artifact | Location | Status | Notes |
|---|---|---|---|
| Pre-Build Final Assurance Gate | `modules/amc/06-pbfag/pre-build-final-assurance-gate.md` | ✅ CS2 Approved with Conditions | Conditions remain binding. |
| PBFAG Evidence Matrix | `modules/amc/06-pbfag/pbfag-evidence-matrix.md` | ✅ CS2 Approved with Conditions | Tracker/index agreement and Stage 8 gate conditions remain binding. |
| PBFAG Findings and Verdict | `modules/amc/06-pbfag/pbfag-findings-and-verdict.md` | ✅ CS2 Approved with Conditions | Stage 8 opened by issue #1199 only as planning wave. |
| PBFAG Checklist | `modules/amc/06-pbfag/pbfag-checklist.md` | ✅ CS2 Approved with Conditions | References canonical PBFAG artifacts. |
| Stage 1–4 Functional Delivery Change-Propagation Audit | `modules/amc/06-pbfag/stage1-4-functional-delivery-change-propagation-audit.md` | ✅ CS2 Approved with Conditions | Retained as upstream input. |
| Functional Delivery PBFAG Addendum | `modules/amc/06-pbfag/functional-delivery-pbfag-addendum.md` | ✅ CS2 Approved with Conditions | Binding downstream input. |
| PBFAG Retrofit Evidence Matrix | `modules/amc/06-pbfag/pbfag-retrofit-evidence-matrix.md` | ✅ CS2 Approved with Conditions | PBFAG-FD, PBFAG-DEPLOY, PBFAG-QA, PBFAG-TRACK, and PBFAG-STAGE8 rows remain binding. |
| Stage 7 Functional Delivery Change-Propagation Audit | `modules/amc/06-pbfag/stage7-functional-delivery-change-propagation-audit.md` | ✅ CS2 Approved with Conditions | Conditions carried forward. |
| CS2 Disposition Pack — Stages 5, 5a, 6, and 7 | `modules/amc/06-pbfag/cs2-disposition-pack-stages-5-5a-6-7.md` | ✅ Used for CS2 Decision | Source for issue #1197 decision record. |
| CS2 Decision Record — Stages 5, 5a, 6, and 7 | `modules/amc/06-pbfag/cs2-decision-record-stages-5-5a-6-7.md` | ✅ Current Authority | Explicit CS2 approval with conditions. |
| Current Authority Note — Stages 5, 5a, 6, and 7 | `modules/amc/06-pbfag/current-authority-note-stages-5-5a-6-7.md` | ✅ Current Authority Note | Clarifies current status source. |

---

## Stage 8 — Implementation Plan

| Artifact | Location | Status | Notes |
|---|---|---|---|
| Implementation Plan | `modules/amc/07-implementation-plan/implementation-plan.md` | ✅ CS2 Approved with Conditions | Produced in issue #1199 / PR #1200. Approved by issue #1201 / merged PR #1202 disposition record. Header aligned in PR #1209. |
| Wave Breakdown | `modules/amc/07-implementation-plan/wave-breakdown.md` | ✅ CS2 Approved with Conditions | Produced in issue #1199 / PR #1200. Approved by merged PR #1202 disposition. Header aligned in PR #1209. |
| Condition Import Matrix | `modules/amc/07-implementation-plan/condition-import-matrix.md` | ✅ CS2 Approved with Conditions | Maps CS2 conditions into Stage 8 planning waves. Header aligned in PR #1209. |
| CS2 Decision Record — Stage 8 | `modules/amc/07-implementation-plan/cs2-decision-record-stage-8.md` | ✅ Current Authority | Records Stage 8 acceptance with conditions. PR #1202 merged. |

---

## Stage 9 — Builder Checklist

| Artifact | Location | Status | Notes |
|---|---|---|---|
| Builder Checklist | `modules/amc/08-builder-checklist/builder-checklist.md` | ✅ Produced / Merged | PR #1204 merged the universal and W1–W8 readiness gates. |
| Builder Readiness Attestations | `modules/amc/08-builder-checklist/builder-readiness-attestations.md` | ✅ Produced / Merged | PR #1204 merged the controlled candidate/Foreman attestation template. |
| W1 Candidate Readiness Checklist — `integration-builder` | `modules/amc/08-builder-checklist/executions/w1/integration-builder-readiness-checklist.md` | 🔴 BLOCKED | Historical execution merged in PR #1206; reconciled in merged PR #1209. |
| Historical W1 Candidate Readiness Attestation — `integration-builder` | `modules/amc/08-builder-checklist/executions/w1/integration-builder-readiness-attestation.md` | 🟠 EXECUTED / 🔴 BLOCKED | Historical candidate attestation; `CA-02 = NO` and `CA-07 = NO` remain provenance. |
| Final W1 Candidate Re-Attestation — `integration-builder` | `modules/amc/08-builder-checklist/executions/w1/integration-builder-final-reattestation-20260722.md` | 🟡 PENDING CANDIDATE | Issue #1210 / PR #1211. Candidate-only RA-01 through RA-24 must be completed by `integration-builder`. |
| W1 Environment and Dependency Register | `modules/amc/08-builder-checklist/executions/w1/w1-environment-and-dependency-register.md` | 🔴 BLOCKED | Supabase production and `develop` exist; candidate-specific permissions and operational enforcement remain incomplete. |
| W1 Access and Isolation Evidence | `modules/amc/08-builder-checklist/executions/w1/w1-access-isolation-evidence-20260722.md` | 🟡 PARTIAL EVIDENCE | Records GitHub gate execution, successful Vercel Preview, Supabase branch separation and protected-production boundaries without exposing secret values. |
| W1 RED-Test and Evidence Map | `modules/amc/08-builder-checklist/executions/w1/w1-red-test-and-evidence-map.md` | 🟡 Defined / BLOCKED | W1 obligations mapped; later implementation evidence remains required. |
| W1 Environment Evidence Update | `modules/amc/08-builder-checklist/executions/w1/w1-environment-evidence-update-20260721.md` | 🟡 Partial Evidence | Records Vercel/Supabase resources and AMC secret-name presence without values. |
| W1 Readiness Reconciliation | `modules/amc/08-builder-checklist/executions/w1/w1-readiness-reconciliation-20260722.md` | 🔴 Historical BLOCKED | Issue #1208 / merged PR #1209 reconciled the post-merge record. |
| CS2 Decision Record — Stage 9 W1 | `modules/amc/08-builder-checklist/cs2-decision-record-stage-9-w1.md` | 🔴 Current Disposition: BLOCKED | Explicitly withholds Stage 10, appointment and build authorization pending a later evidence-complete PASS. |

Stage 9 W1 candidate readiness remains BLOCKED while the final candidate re-attestation and independent Foreman verification are incomplete. Passing PR ceremony gates does not approve the candidate or authorize Stage 10–12.

---

## Stage 10 — IAA Pre-Brief

| Artifact | Location | Status | Notes |
|---|---|---|---|
| IAA Pre-Brief | `modules/amc/09-iaa-pre-brief/iaa-pre-brief.md` | ⬜ Placeholder — 🔴 Blocked | Not started. Blocked by the Stage 9 W1 CS2 disposition. |
| IAA Pre-Brief Response | `modules/amc/09-iaa-pre-brief/iaa-pre-brief-response.md` | ⬜ Placeholder — 🔴 Blocked | Not started. |

---

## Stage 11 — Builder Appointment

| Artifact | Location | Status | Notes |
|---|---|---|---|
| Builder Appointment | `modules/amc/10-builder-appointment/builder-appointment.md` | ⬜ Placeholder — 🔴 Blocked | No builders appointed. |
| Builder Contract | `modules/amc/10-builder-appointment/builder-contract.md` | ⬜ Placeholder — 🔴 Blocked | Not started. |

---

## Stage 12 — Build

| Artifact | Location | Status | Notes |
|---|---|---|---|
| Build Evidence Index | `modules/amc/11-build/build-evidence-index.md` | ⬜ Placeholder — 🔴 Blocked | Not started. |
| QA-to-Green Evidence | `modules/amc/11-build/qa-to-green-evidence.md` | ⬜ Placeholder — 🔴 Blocked | Not started. |
| Handover | `modules/amc/11-build/handover.md` | ⬜ Placeholder — 🔴 Blocked | Not started. |

---

## Legacy

| Artifact | Location | Status | Notes |
|---|---|---|---|
| FM-era artifacts | `modules/amc/_legacy/foreman-app-origin/` | 📦 Legacy Area | Historical artifacts only. |
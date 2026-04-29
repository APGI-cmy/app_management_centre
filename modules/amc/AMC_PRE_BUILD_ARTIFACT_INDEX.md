# AMC Pre-Build Artifact Index

**Module**: App Management Centre (AMC)  
**Lifecycle Model**: 12-Stage Pre-Build Sequence + Stage 5a (PRE_BUILD_STAGE_MODEL_CANON.md v1.0.0; AMC-GOV-OVERSIGHT-001)  
**Last Updated**: 2026-04-28 (Stage 7 PBFAG artifacts produced approval-pending — wave amc-stage7-pbfag-20260428; issue #1152; Stage 6 red test count corrected to 79 tests/20 families; prior: Stage 6 QA-to-Red pack produced approval-pending — wave amc-stage6-qa-to-red-20260427; issue #1141; prior: Stage 5a Deployment Execution Strategy artifacts produced approval-pending — wave amc-stage5a-deployment-execution-strategy-20260427; issue #1137; prior: Stage 5a Deployment Execution Strategy defined; Stage 5 Architecture artifacts updated to canonical — wave amc-stage5-architecture-20260426; Stage 4 treated as approved for Stage 5 progression per issue #1131; Stage 3 marked CS2-approved; Stage 2 confirmed CS2-approved; Stages 1–3 harmonization pass applied)  
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
| UX Workflow & Wiring Spec | `modules/amc/01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md` | ✅ Approved Canonical | v1.1, CS2-approved 2026-04-22. Harmonization pass applied 2026-04-23: ARC Governance Console journey and Dynamic Upload Quota Management Console journey added. Issue #1121. |
| Wiring Artifact Index | `modules/amc/01-ux-workflow-wiring-spec/wiring-artifact-index.md` | ✅ Approved Canonical | v1.0, CS2-approved 2026-04-22. Issue #1121. |

---

## Stage 3 — FRS

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Functional Requirements Specification | `modules/amc/02-frs/functional-requirements-specification.md` | ✅ Approved Canonical | v1.1, CS2-approved for Stage 4 progression 2026-04-23. Harmonization pass applied 2026-04-23: FR-1800 ARC Governance Console family added; FR-606/FR-607 operational quota management requirements added. Approval ref: #1123. |
| App Description to FRS Traceability | `modules/amc/02-frs/app-description-to-frs-traceability.md` | ✅ Approved Canonical | v1.0, CS2-approved for Stage 4 progression 2026-04-23. Approval ref: #1123. |

---

## Stage 4 — TRS

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Technical Requirements Specification | `modules/amc/03-trs/technical-requirements-specification.md` | 🟠 Treated as Approved | v1.1, hardened approval-ready 2026-04-23. ARC domain (TR-1800), quota console (TR-605–TR-609), alert contract family (TR-207–TR-209), audit/auth/state contract family declarations added. Upstream sources updated to v1.1 per harmonization pass. Stage 4 treated as approved for Stage 5 progression per CS2 #1131. Formal CS2 approval pending. Issue #1125 (hardened in #1127). |
| FRS to TRS Traceability | `modules/amc/03-trs/frs-to-trs-traceability.md` | 🟠 Treated as Approved | v1.1, hardened 2026-04-23. 18 domain families traced (17 FRS + ARC), 30 deferred items disclosed, quota console and ARC coverage added. Stage 4 treated as approved for Stage 5 progression per CS2 #1131. Issue #1125 (hardened in #1127). |

---

## Stage 5 — Architecture

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Architecture Specification | `modules/amc/04-architecture/architecture-specification.md` | 🟡 Approval Pending | v1.0, produced 2026-04-26. Canonical Stage 5 artifact. CS2 approval required. Wave: amc-stage5-architecture-20260426. CS2 auth: #1131. |
| TRS-to-Architecture Traceability | `modules/amc/04-architecture/trs-to-architecture-traceability.md` | 🟡 Approval Pending | v1.0, produced 2026-04-26. 18/18 TRS families realized. CS2 auth: #1131. |
| Architecture (superseded placeholder) | `modules/amc/04-architecture/architecture.md` | 📦 Superseded | Updated 2026-04-26 with SUPERSEDED notice. `architecture-specification.md` is the canonical Stage 5 artifact. |
| Architecture Decision Records | `modules/amc/04-architecture/architecture-decision-records.md` | ⬜ Placeholder | Not started |
| Architecture Completeness Checklist | `modules/amc/04-architecture/architecture-completeness-checklist.md` | ⬜ Placeholder | Not started |

---

## Stage 5a — Deployment Execution Strategy *(AMC-local mandatory stage)*

> **Stage 5a Definition Authority**: `modules/amc/governance-oversight/DEPLOYMENT_STRATEGY_OVERSIGHT.md` (AMC-GOV-OVERSIGHT-001 v1.0)  
> **CS2 Authorization**: app_management_centre#1133  
> **Governing Delivery Issue**: app_management_centre#1137  
> **Status**: 🟡 Artifacts produced — CS2 approval pending  
> **Entry Condition**: Stage 5 complete and CS2-approved (Stage 5 approval still pending)  
> **Blocks**: Stage 6 (QA-to-Red) and all subsequent stages

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Deployment Execution Strategy | `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` | 🟡 Approval Pending | v1.0, produced 2026-04-27. All 8 DES mandatory fields answered (DES-001 through DES-008). No TBD fields. Single approved migration mechanism: Supabase CLI. CS2 sign-off section included. CS2 approval required. Wave: amc-stage5a-deployment-execution-strategy-20260427. |
| Deployment Surface Ownership Table | `modules/amc/05a-deployment-execution-strategy/deployment-surface-ownership-table.md` | 🟡 Approval Pending | v1.0, produced 2026-04-27. 5-surface ownership matrix (SURF-001–005). All surfaces owned. No ownership gaps. CS2 approval required. |
| Runner and Environment Constraints | `modules/amc/05a-deployment-execution-strategy/runner-and-environment-constraints.md` | 🟡 Approval Pending | v1.0, produced 2026-04-27. GitHub-hosted runners only (ubuntu-latest). Protected environment configuration. CI-safe/preview-safe/live-only safety table. Environment prerequisites and network assumptions. CS2 approval required. |
| Governance Oversight Record | `modules/amc/governance-oversight/DEPLOYMENT_STRATEGY_OVERSIGHT.md` | ✅ COMPLETE — v1.0 | Formal oversight record: gap declaration, Stage 5a definition, required content specification (8 mandatory fields), implementation-plan requirements, anti-drift governance language, corrective action roadmap. CS2 auth: #1133. |

---

## Stage 6 — QA-to-Red

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| QA-to-Red Specification | `modules/amc/05-qa-to-red/qa-to-red-specification.md` | 🟡 Approval Pending | v1.0, produced 2026-04-27. Core Stage 6 spec: pass/fail philosophy, 4-level severity model, blocker/non-blocker rules, retest protocol, evidence requirements. 12 architecture-derived coverage families (§7) + 7 DES-derived coverage families (§8) + literal-operability checks (§9) + anti-drift posture (§10) + CS2 sign-off section. CS2 approval required. Governing issue: #1141. |
| Architecture and DES to QA Traceability | `modules/amc/05-qa-to-red/architecture-and-des-to-qa-traceability.md` | 🟡 Approval Pending | v1.0, produced 2026-04-27. Traceability matrix: all 12 Stage 5 Architecture domains + all 8 DES fields (DES-001 through DES-008) traced to Stage 6 red test IDs. Zero silently omitted. Explicit omission register for Stage 12 deferrals. Coverage completeness verdict: 12/12 Architecture domains, 8/8 DES fields. |
| Red Test Catalog | `modules/amc/05-qa-to-red/red-test-catalog.md` | 🟡 Approval Pending | v1.0, produced 2026-04-27. **79 test cases across 20 families** (corrected from prior erroneous count of 69/17). Each entry: test ID, source artifact, scenario, exact fail condition, exact pass condition, severity (CRITICAL/HIGH/MEDIUM/LOW), blocker classification, evidence type. 21 CRITICAL, 54 HIGH, 4 MEDIUM tests; 75 blockers. |
| QA-to-Red Suite (superseded placeholder) | `modules/amc/05-qa-to-red/qa-to-red-suite.md` | ⛔ Superseded | Placeholder superseded by qa-to-red-specification.md v1.0. Retained for path continuity. |
| QA Catalog Alignment (superseded placeholder) | `modules/amc/05-qa-to-red/qa-catalog-alignment.md` | ⛔ Superseded | Placeholder superseded by architecture-and-des-to-qa-traceability.md v1.0. Retained for path continuity. |

> **Gate condition**: Stage 7 (PBFAG) is BLOCKED until Stage 5 (Architecture), Stage 5a (DES), and Stage 6 (QA-to-Red) all receive CS2 approval. Governing issue: app_management_centre#1141.

---

## Stage 7 — PBFAG

> **Stage 7 Governing Delivery Issue**: app_management_centre#1152
> **CS2 Authorization**: app_management_centre#1152 (CS2 authorized parallel production while Stages 5/5a/6 are approval-pending)
> **Wave**: amc-stage7-pbfag-20260428
> **Status**: 🟡 Artifacts produced — CS2 approval pending
> **Entry Condition**: EXCEPTION — Stages 5, 5a, and 6 still approval-pending; CS2 authorized Stage 7 parallel production per #1152
> **Blocks**: Stage 8 (Implementation Plan) and all subsequent stages

| Artifact | Location | Status | Notes |
|----------|----------|--------|-------|
| Pre-Build Final Assurance Gate | `modules/amc/06-pbfag/pre-build-final-assurance-gate.md` | 🟡 Approval Pending | v1.0, produced 2026-04-28. Master PBFAG gate artifact. 10-category evaluation of Stages 1–6. CONDITIONAL PASS verdict. Stage 8 gate conditions explicit. CS2 sign-off section included. CS2 approval required. |
| PBFAG Evidence Matrix | `modules/amc/06-pbfag/pbfag-evidence-matrix.md` | 🟡 Approval Pending | v1.0, produced 2026-04-28. 81 checks across 10 categories. PASS: 53, PASS-WITH-NOTE: 1, CONDITIONAL: 27, FAIL: 0. All checks verified against canonical upstream artifacts. CS2 approval required. |
| PBFAG Findings and Verdict | `modules/amc/06-pbfag/pbfag-findings-and-verdict.md` | 🟡 Approval Pending | v1.0, produced 2026-04-28. Verdict: CONDITIONAL PASS. 0 blocking findings. Stage 8 gate condition: 4 CS2 approvals required (Stages 5, 5a, 6, 7). CS2 approval required. |
| PBFAG Checklist | `modules/amc/06-pbfag/pbfag-checklist.md` | 🟡 Active Wave | Updated to active wave posture; references canonical PBFAG artifacts. |

> **Gate condition**: Stage 8 (Implementation Plan) is BLOCKED until Stage 5 (Architecture), Stage 5a (DES), Stage 6 (QA-to-Red), AND Stage 7 (PBFAG) all receive CS2 approval. Governing issue: app_management_centre#1152.

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

**Legend**: ✅ Active/Complete | 🟡 Approval Pending | 🟠 Treated as Approved | 📌 Reference Only | ⬜ Placeholder/Not Started | 📦 Legacy Area

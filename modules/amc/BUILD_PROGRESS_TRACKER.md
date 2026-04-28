# AMC Build Progress Tracker

**Module**: App Management Centre (AMC)  
**Module Slug**: AMC  
**Last Updated**: 2026-04-27
**Updated By**: foreman-v2-agent (wave: amc-stage6-qa-to-red-20260427 — Stage 6 QA-to-Red pack produced approval-pending; issue #1141; prior: amc-stage5a-deployment-execution-strategy-20260427 — Stage 5a artifacts produced approval-pending; all 8 DES fields answered; issue #1137; prior: amc-governance-deployment-oversight-20260426 — Stage 5a defined; amc-stage5-architecture-20260426 — Stage 5 Architecture produced)

> **Classification**: ACTIVE  
> **Document Role**: PRIMARY LIVE CONTROL DOCUMENT — This is the designated primary operational monitor for AMC pre-build stage progress. CS2 should use this document as the main live progress dashboard.  
> **Canon Reference**: `PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0  
> **Issue**: [app_management_centre#1137](https://github.com/APGI-cmy/app_management_centre/issues/1137)  
> **Update Rule**: This document MUST be updated immediately after every AMC stage issue, wave completion, approval, or readiness/blocker change. Stale tracker text is a governance defect.

> ⚠️ **GOVERNANCE OVERSIGHT NOTE (issue #1133, 2026-04-26)**: A mandatory deployment execution
> planning stage has been added as Stage 5a between Stage 5 (Architecture) and Stage 6 (QA-to-Red).
> Architecture/platform topology alone is insufficient — the deployment execution strategy must be
> frozen and CS2-approved before build execution begins. See
> `modules/amc/governance-oversight/DEPLOYMENT_STRATEGY_OVERSIGHT.md` for the formal oversight
> record, Stage 5a definition, required content specification, anti-drift rules, and corrective
> action roadmap. Stage 6 (QA-to-Red) is BLOCKED until Stage 5a is complete and CS2-approved.

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
| **5a** | **Deployment Execution Strategy** | **🟡 IN PROGRESS — Produced Approval-Pending** | Stage 5a artifacts produced 2026-04-27 (wave amc-stage5a-deployment-execution-strategy-20260427, issue #1137). All 8 DES fields answered. Awaiting CS2 approval. Artifacts: `modules/amc/05a-deployment-execution-strategy/`. |
| 6 | QA-to-Red | 🟡 IN PROGRESS — Produced Approval-Pending | Stage 6 QA-to-Red pack produced 2026-04-27 (wave amc-stage6-qa-to-red-20260427, issue #1141). Awaiting CS2 approval. Artifacts: `modules/amc/05-qa-to-red/`. **GATE CONDITION**: Stage 7 remains BLOCKED until Stage 6, Stage 5, and Stage 5a all receive CS2 approval. |
| 7 | PBFAG | ⬜ Not Started | 🔴 BLOCKED — requires Stage 5, Stage 5a, AND Stage 6 complete and CS2-approved |
| 8 | Implementation Plan | ⬜ Not Started | 🔴 BLOCKED — must reference approved Stage 5a Deployment Execution Strategy. |
| 9 | Builder Checklist | ⬜ Not Started | 🔴 BLOCKED |
| 10 | IAA Pre-Brief | ⬜ Not Started | 🔴 BLOCKED |
| 11 | Builder Appointment | ⬜ Not Started | 🔴 BLOCKED |
| 12 | Build | ⬜ Not Started | 🔴 BLOCKED — all builders bound to approved Stage 5a deployment execution strategy. |

**Legend**: ✅ Complete | 🟡 Active / In Progress | ⬜ Not Started | 🔴 Blocked | 📋 Defined (awaiting prerequisites)

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
**Approval Required**: Yes — CS2 approval required before Stage 5a (Deployment Execution Strategy) may begin
**Note — Pre-existing FM-era material**: The `docs/architecture/` directory contains architecture documents from the FM-origin era. These remain classified as historical/reference material only. The canonical Stage 5 architecture is `modules/amc/04-architecture/architecture-specification.md` v1.0. The `architecture.md` placeholder stub has been updated with a superseded notice pointing to the canonical artifact.

---

### Stage 5a — Deployment Execution Strategy

**Status**: 🟡 IN PROGRESS — Produced Approval-Pending (2026-04-27)  
**Location**: `modules/amc/05a-deployment-execution-strategy/`  
**Entry Condition**: Stage 5 complete and **CS2 approved** — ⚠️ Stage 5 approval still pending; Stage 5a produced in parallel per CS2 authorization (issue #1133)  
**Definition Authority**: `modules/amc/governance-oversight/DEPLOYMENT_STRATEGY_OVERSIGHT.md` (AMC-GOV-OVERSIGHT-001 v1.0, 2026-04-26, issue #1133)  
**Objective**: Freeze the deployment execution strategy for AMC before QA-to-Red begins. Produce
a CS2-approved artifact that explicitly defines: workflow surface ownership, runner authorization
boundaries, migration execution path, CI/preview/production execution boundaries, safety
classification of each surface, manual/protected approval requirements, and environment/network
assumption validation approach. Architecture/platform topology alone is insufficient — the
deployment execution strategy must also be frozen.  
**Key Artifacts Created**:
- [x] `deployment-execution-strategy.md` — Primary Stage 5a artifact v1.0 (produced 2026-04-27): all 8 mandatory DES fields answered (DES-001 through DES-008), no TBD fields, CS2 sign-off section. DES-001: 5 surfaces owned. DES-002: GitHub-hosted runner authorization defined. DES-003: No self-hosted runners required. DES-004: Supabase CLI (`supabase db push`) frozen as sole migration mechanism. DES-005: PR/preview/production/manual dispatch boundaries defined. DES-006: CI-safe/preview-safe/live-only classification table. DES-007: Production environment approval gate, manual validation. DES-008: Pre-flight env var, Supabase CLI, Vercel credential checks.
- [x] `deployment-surface-ownership-table.md` — Supporting artifact v1.0 (produced 2026-04-27): 5-surface ownership matrix; SURF-001–005; trigger class; environment scope; approval requirement; runner type. No unowned surface.
- [x] `runner-and-environment-constraints.md` — Supporting artifact v1.0 (produced 2026-04-27): runner type (GitHub-hosted only); protected environment configuration; CI-safe/preview-safe/live-only safety table; environment prerequisites and network assumptions.
**Wave**: amc-stage5a-deployment-execution-strategy-20260427  
**Produced By**: foreman-v2-agent (POLC_ORCHESTRATION)  
**CS2 Authorization**: issue #1133  
**Prerequisites**: Stage 5 complete and **CS2 approved** — Stage 5 approval pending; Stage 5a produced per authorized issue scope  
**Approval Required**: Yes — CS2 approval required before Stage 6 (QA-to-Red) may begin  
**Note — Mandatory Content**: All 8 DES fields answered per §3.1 of `DEPLOYMENT_STRATEGY_OVERSIGHT.md`. No field left TBD. Single approved migration mechanism: Supabase CLI.

---

### Stage 6 — QA-to-Red

**Status**: 🟡 IN PROGRESS — Produced Approval-Pending
**Location**: `modules/amc/05-qa-to-red/`
**Prerequisites**: Stage 5 complete and **CS2 approved** AND Stage 5a complete and **CS2 approved** — ⚠️ GATE CONDITION ACTIVE — Stage 6 artifacts produced conditionally per CS2 authorization in issue #1141 while Stage 5 and Stage 5a await approval. Stage 7 remains BLOCKED until all three approvals are received.
**Key Artifacts**:
- [x] `qa-to-red-specification.md` v1.0 — Core Stage 6 spec: pass/fail philosophy, 4-level severity model, blocker/non-blocker rules, retest protocol, evidence requirements, 12 architecture-derived coverage families (§7), 7 DES-derived coverage families (§8), literal-operability checks (§9), anti-drift posture (§10), CS2 sign-off section. Produced 2026-04-27.
- [x] `architecture-and-des-to-qa-traceability.md` v1.0 — Traceability matrix: all 12 Stage 5 Architecture domains and all 8 DES fields (DES-001 through DES-008) traced to Stage 6 red test IDs. Zero silently omitted. Explicit omission register for Stage 12 deferrals. Produced 2026-04-27.
- [x] `red-test-catalog.md` v1.0 — 79 test cases across 20 families (21 CRITICAL / 54 HIGH / 4 MEDIUM; 75 blockers). Each entry: test ID, source artifact, scenario, exact fail condition, exact pass condition, severity, blocker classification, evidence type. Produced 2026-04-27.
- [x] `qa-to-red-suite.md` — Superseded notice (canonical artifacts listed above)
- [x] `qa-catalog-alignment.md` — Superseded notice (traceability covered by architecture-and-des-to-qa-traceability.md)

**Completion Date**: Pending CS2 approval
**Approval Required**: Yes — CS2 approval required before Stage 7 (PBFAG) may begin
**Governing Issue**: app_management_centre#1141
**Wave**: amc-stage6-qa-to-red-20260427

**Note**: QA-to-Red covers deployment-surface boundary violations per the approved Stage 5a strategy. All 8 DES fields are explicitly represented in the red test catalog (QA-DES family). All Stage 5 architecture commitments are represented (QA-ARCH, QA-ARC, QA-QUOTA, QA-STATE, QA-AUDIT, QA-AUTH, QA-DEGRADE, QA-ALERT, QA-SESSION, QA-RT, QA-CONFIG, QA-SCHED families). Literal-operability failure modes are explicitly represented (QA-LITOP family).

---

### Stage 7 — PBFAG

**Status**: ⬜ Not Started  
**Location**: `modules/amc/06-pbfag/`  
**Prerequisites**: Stage 6 complete and approved  
**Note**: PBFAG is a hard gate. It is not situational. It cannot be bypassed without explicit CS2-documented exception. PBFAG must verify that Stage 5a (Deployment Execution Strategy) is present, complete, and non-contradictory with Stage 5 (Architecture).

---

### Stage 8 — Implementation Plan

**Status**: ⬜ Not Started  
**Location**: `modules/amc/07-implementation-plan/`  
**Prerequisites**: Stage 7 (PBFAG) gate passed  
**Mandatory Requirement**: The Implementation Plan must include a dedicated section referencing the approved Stage 5a Deployment Execution Strategy document by path and version. An Implementation Plan that lacks this section or proposes a deployment model inconsistent with Stage 5a is a blocking defect. See `DEPLOYMENT_STRATEGY_OVERSIGHT.md` §4.1.

---

### Stage 9 — Builder Checklist

**Status**: ⬜ Not Started  
**Location**: `modules/amc/08-builder-checklist/`  
**Prerequisites**: Stage 8 complete and approved  
**Mandatory Requirement**: Must include an attestation confirming builder(s) have read and will implement only the approved Stage 5a deployment execution strategy.

---

### Stage 10 — IAA Pre-Brief

**Status**: ⬜ Not Started  
**Location**: `modules/amc/09-iaa-pre-brief/`  
**Prerequisites**: Stage 9 complete and approved  

---

### Stage 11 — Builder Appointment

**Status**: ⬜ Not Started  
**Location**: `modules/amc/10-builder-appointment/`  
**Prerequisites**: Stages 1–10 complete (including Stage 5a). IAA Pre-Brief published.  
**Note**: No delegation to builders until all Stages 1–10 (including Stage 5a) are complete and gate-passed (HALT-008).

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
6. 🟡 Stage 5a Deployment Execution Strategy artifacts produced approval-pending (wave amc-stage5a-deployment-execution-strategy-20260427, 2026-04-27, issue #1137). All 8 DES fields answered. See `modules/amc/05a-deployment-execution-strategy/`.
7. ▶️ CS2 to review and approve Stage 5 Architecture and Stage 5a Deployment Execution Strategy.
8. 🟡 Stage 6 QA-to-Red pack produced approval-pending (wave amc-stage6-qa-to-red-20260427, 2026-04-27, issue #1141). 79 red test cases across 20 families. CS2 conditionally authorized Stage 6 artifact production while Stage 5 and Stage 5a await approval. Stage 7 BLOCKED until Stage 5, Stage 5a, and Stage 6 all receive CS2 approval.
9. ▶️ CS2 to review and approve Stage 5, Stage 5a, and Stage 6 (may be concurrent or sequential at CS2 discretion).

---

## References

- [PRE_BUILD_STAGE_MODEL_CANON.md](../../governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md)
- [APP_DESCRIPTION_REQUIREMENT_POLICY.md](../../governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md)
- [DEPLOYMENT_STRATEGY_OVERSIGHT.md](./governance-oversight/DEPLOYMENT_STRATEGY_OVERSIGHT.md) — ✅ Stage 5a definition, oversight record, anti-drift rules (issue #1133, 2026-04-26)
- [deployment-execution-strategy.md](./05a-deployment-execution-strategy/deployment-execution-strategy.md) — 🟡 Stage 5a primary artifact (produced approval-pending, 2026-04-27; all 8 DES fields; wave amc-stage5a-deployment-execution-strategy-20260427; governing delivery issue: #1137; CS2 authorization: #1133)
- [deployment-surface-ownership-table.md](./05a-deployment-execution-strategy/deployment-surface-ownership-table.md) — 🟡 Stage 5a supporting artifact (produced approval-pending, 2026-04-27)
- [runner-and-environment-constraints.md](./05a-deployment-execution-strategy/runner-and-environment-constraints.md) — 🟡 Stage 5a supporting artifact (produced approval-pending, 2026-04-27)
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

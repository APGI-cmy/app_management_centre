# AMC Wave Record — Stage 6 QA-to-Red

**Wave Slug**: amc-stage6-qa-to-red-20260427
**Session**: session-034
**Date**: 2026-04-27
**Producing Agent**: foreman-v2-agent (POLC_ORCHESTRATION)
**Governing Delivery Issue**: [app_management_centre#1141](https://github.com/APGI-cmy/app_management_centre/issues/1141) — "Stage 6 — Create AMC QA-to-Red pack and keep tracker/index aligned" (opened by CS2 @APGI-cmy)
**Repository**: APGI-cmy/app_management_centre
**Wave Record Author**: independent-assurance-agent (Phase 0 Pre-Brief — session-058-20260427)

---

## Section 1 — Wave Identity

| Field | Value |
|-------|-------|
| wave_slug | amc-stage6-qa-to-red-20260427 |
| session | session-034 |
| date | 2026-04-27 |
| producing_agent | foreman-v2-agent |
| agent_class | POLC_ORCHESTRATION |
| governing_issue | app_management_centre#1141 |
| governing_issue_author | @APGI-cmy (CS2 / OWNER) |
| wave_type | PRE_BUILD_STAGE — Stage 6 QA-to-Red |
| task_count | 7 |
| ecap_ceremony_admin | NONE |
| iaa_pre_brief_session | session-058-20260427 |

---

## Section 2 — IAA Pre-Brief (Phase 0)

> **Pre-Brief Embedded By**: independent-assurance-agent — session-058-20260427 — 2026-04-27
> **Authority**: Phase 0 of IAA contract v6.2.0; INDEPENDENT_ASSURANCE_AGENT_CANON.md §Pre-Brief

### 2.1 — Wave Classification

| Field | Value |
|-------|-------|
| pr_category | PRE_BUILD_STAGE |
| iaa_required_at_final_assurance | YES — MANDATORY |
| trigger_rule | iaa-trigger-table.md Step 7 — Stage 6 QA-to-Red artifacts produced under `modules/amc/05-qa-to-red/` |
| ambiguity | CLEAR — no ambiguity |
| overlay_at_final_assurance | OVL-PBG-010, OVL-PBG-011, OVL-PBG-012, OVL-PBG-013, OVL-PBG-014, OVL-PBG-016, OVL-PBG-ADM-003 + CORE-020 + CORE-021 |
| ecap_applicable | NO — POLC_ORCHESTRATION documentation wave; no ECAP ceremony admin appointed |
| acr_01_through_acr_11 | NOT APPLICABLE — no ECAP ceremony admin |

### 2.2 — Task Classification

| Task ID | Description | Classification | Qualifying for Final Assurance? |
|---------|-------------|---------------|--------------------------------|
| TASK-034-01 | Create `modules/amc/05-qa-to-red/qa-to-red-specification.md` v1.0 | PRIMARY SUBSTANTIVE — Stage 6 core specification | ✅ YES — mandatory coverage |
| TASK-034-02 | Create `modules/amc/05-qa-to-red/architecture-and-des-to-qa-traceability.md` v1.0 | PRIMARY SUBSTANTIVE — traceability matrix | ✅ YES — mandatory coverage |
| TASK-034-03 | Create `modules/amc/05-qa-to-red/red-test-catalog.md` v1.0 | PRIMARY SUBSTANTIVE — red test catalog | ✅ YES — mandatory coverage |
| TASK-034-04 | Update `modules/amc/05-qa-to-red/qa-to-red-suite.md` — superseded notice | CEREMONY — placeholder retirement | ✅ YES — existence check |
| TASK-034-05 | Update `modules/amc/05-qa-to-red/qa-catalog-alignment.md` — superseded notice | CEREMONY — placeholder retirement | ✅ YES — existence check |
| TASK-034-06 | Update `modules/amc/BUILD_PROGRESS_TRACKER.md` | CEREMONY / ALIGNMENT — tracker update | ✅ YES — gate condition preservation |
| TASK-034-07 | Update `modules/amc/AMC_PRE_BUILD_ARTIFACT_INDEX.md` | CEREMONY / ALIGNMENT — index update | ✅ YES — gate condition preservation |

**Qualifying Tasks for IAA Final Assurance**: All 7 tasks are in scope.  
**Substantive Focus Tasks** (90/10 mandate): TASK-034-01, TASK-034-02, TASK-034-03.

### 2.3 — Governing Issue Verification

**Issue #1141** — Verified by IAA directly against GitHub:
- Opened by: @APGI-cmy (OWNER / CS2) ✅
- Title: "Stage 6 — Create AMC QA-to-Red pack and keep tracker/index aligned" ✅
- Body: Contains explicit authorization for Stage 6 issue creation now, with explicit gate condition that Stage 6 execution must not bypass the live gate condition ✅
- Issue status: OPEN (wave is in progress) ✅

> ⚠️ **IAA DISCREPANCY FLAG — GOVERNING ISSUE REFERENCE ERROR**
>
> The Pre-Brief request submitted by the invoking agent states **"Triggering Issue: app_management_centre#1140"**. This is **incorrect**.
>
> Issue #1140 is an **open pull request** titled "feat(governance): PR handover hardening — issue-role registry, stale injector retirement, pre-PR blocking gate, entry-condition exception schema, operational sanity-check (issue #1139)". It is a separate governance hardening PR and is NOT the Stage 6 governing delivery issue.
>
> The correct governing delivery issue is **app_management_centre#1141**, which was opened by CS2 (@APGI-cmy as OWNER) and is titled "Stage 6 — Create AMC QA-to-Red pack and keep tracker/index aligned".
>
> **Required Foreman Action**: Correct the wave checklist (`.agent-admin/waves/wave-amc-stage6-qa-to-red-20260427-current-tasks.md`) to reference issue #1141 as the triggering/governing issue. All Stage 6 artifacts must cite #1141 as the governing delivery issue in their headers. This wave record already records #1141 as the canonical governing issue.
>
> This is classified as **Risk Flag 1** (see §2.4).

### 2.4 — Risk Flags

**Risk Flag 1 — GOVERNING ISSUE REFERENCE ERROR (HIGH)**

- **Issue**: Wave checklist and Pre-Brief request both reference issue #1140 as the triggering issue. Issue #1140 is an unmerged governance hardening PR, not the Stage 6 governing delivery issue. The correct governing delivery issue is #1141 (CS2-authored, OWNER authority confirmed).
- **Impact**: If Stage 6 artifacts cite #1140 as the governing authority, the PHIRR-001 issue-role registry rules (once that canon is live) will flag this as a role mismatch. Even under current governance, citing a PR rather than an issue as the governing delivery authorization is a substantive governance identity defect.
- **Required Foreman Mitigation**: (a) Update wave checklist to reference #1141. (b) Ensure all Stage 6 artifact headers cite `app_management_centre#1141` as the governing delivery issue. (c) This wave record has already recorded the correct reference.
- **IAA Verification at Final Assurance**: All Stage 6 artifacts will be checked for correct #1141 citation. Any artifact citing #1140 as the governing issue will trigger OVL-PBG-ADM-003 (document identity and authority) FAIL.

---

**Risk Flag 2 — STAGE ENTRY CONDITION EXCEPTION POSTURE (MEDIUM)**

- **Issue**: Issue #1141 explicitly states that Stage 6 is being opened before Stage 5 and Stage 5a receive CS2 approval. This is a conditional parallel-production scenario: artifacts are produced approval-pending, but Stage 6 execution may not proceed to Stage 7 until Stage 5 and Stage 5a are approved. This must be consistently and unambiguously stated across all Stage 6 artifacts, the wave record, and the tracker/index update.
- **New Canon Context**: PR #1140 (currently OPEN, not yet merged) introduces `STAGE_ENTRY_CONDITION_EXCEPTION_CANON.md` (SECC-001), which would require recording a formal exception block with fields `normal_entry_condition`, `exception_authorized_by`, `exception_scope`, `exception_reason`, `parallel_production_authorized`, `exception_changes_next_stage_gate`. Since PR #1140 is **not merged**, SECC-001 is not yet live governance. However, Foreman should be aware that if PR #1140 merges before this wave's PR is opened, SECC-001 compliance may be required.
- **Impact**: If the exception posture is inconsistently stated (e.g., some artifacts say "blocked" while the tracker shows a different state, or the tracker is updated to "in progress" before prerequisites are met), this creates a governance drift defect.
- **Required Foreman Mitigation**: (a) All Stage 6 artifacts must carry the standard "Produced — Approval Pending" status notation. (b) The tracker update (TASK-034-06) must preserve Stage 6 status as "Produced — Approval Pending" (not "active" or "in progress" in the execution sense). (c) Stage 7 must remain BLOCKED in both tracker and index. (d) No artifact may state or imply that Stage 6 execution was authorized before Stage 5 and Stage 5a approval. (e) Monitor: if PR #1140 is merged before the Foreman's PR is opened, apply SECC-001 exception block format to the wave record §3c.
- **IAA Verification at Final Assurance**: Gate condition wording will be checked across all artifacts for consistency. Any inconsistency will trigger OVL-PBG-016 (downstream gate preservation) or CORE-020 FAIL.

---

**Risk Flag 3 — NEW GOVERNANCE CANONS FROM PR #1140 — HANDOVER LAYER IMPACT (MEDIUM)**

- **Issue**: PR #1140 (OPEN) introduces several canons with direct handover implications:
  - `PR_HANDOVER_CANONICAL_PACKAGE.md` (PHCP-001) — PR body schema, token-carrier rule, bundle requirements
  - `PR_HANDOVER_ISSUE_ROLE_REGISTRY.md` (PHIRR-001) — 8 issue roles with YAML block required in wave records and PREHANDOVER proofs; 5 machine-checkable rules (PHIRR-R01–R05)
  - `STALE_HANDOVER_INJECTOR_RETIREMENT_REGISTER.md` (SHIRR-001) — 8 anti-pattern detection rules
  - `OPERATIONAL_STRATEGY_SANITY_CHECK_PROTOCOL.md` (OSSCP-001) — 6-dimension literal implementation sanity-check
  - `END_OF_WAVE_CLOSEOUT_SWEEP_CANON.md` v1.1.0 — adds §8 "Pre-PR Blocking Gate" with 5 new wave record §3c evidence fields
- **Current Status**: PR #1140 is NOT YET MERGED. None of these canons are currently live.
- **Impact**: If PR #1140 merges before the Foreman's Stage 6 PR is opened, all of the above will apply to this wave's handover requirements. The EWCS-001 v1.1.0 Pre-PR Blocking Gate specifically adds 5 mandatory wave record §3c evidence fields that must be non-absent/non-failing before a PR opens as review-ready.
- **Required Foreman Mitigation**: (a) Before opening the Stage 6 PR, check whether PR #1140 has merged. (b) If merged: apply PHIRR-001 YAML block to wave record, satisfy EWCS-001 v1.1.0 §3c evidence fields, check SHIRR-001 anti-patterns. (c) If not merged: standard handover applies (no SECC-001, no PHIRR-001 required).
- **IAA Verification at Final Assurance**: IAA will check the merge state of PR #1140 at the time of final assurance invocation. If merged, the new canons will be applied. This is a monitoring risk flag, not a current blocker.

---

**Risk Flag 4 — UPSTREAM SOURCE DERIVATION CLARITY (LOW)**

- **Issue**: Issue #1141 explicitly lists the canonical upstream sources. All three Stage 5a DES artifacts are required sources for Stage 6 red coverage. The Stage 6 artifacts must demonstrate derivation from both the Architecture Specification v1.0 and all three Stage 5a artifacts (deployment-execution-strategy.md, deployment-surface-ownership-table.md, runner-and-environment-constraints.md).
- **Impact**: If Stage 6 artifacts only reference the Architecture and the DES top-level document but not the surface ownership table and runner constraints, Stage 6 traceability will be incomplete. These sub-artifacts contain the specific deployment boundary commitments that require explicit red test coverage.
- **Required Foreman Mitigation**: (a) `architecture-and-des-to-qa-traceability.md` must explicitly reference all 8 DES fields (DES-001 through DES-008) and also cover the deployment surface ownership table and runner/environment constraints as separate source artifacts. (b) `red-test-catalog.md` must include test cases sourced from the runner-and-environment-constraints.md (not just the top-level DES document).
- **IAA Verification at Final Assurance**: Traceability artifact will be checked for explicit coverage of all 8 DES fields and all three Stage 5a artifacts. Missing source coverage will trigger OVL-PBG-011 (completeness) FAIL.

### 2.5 — Pre-Brief Summary

| Field | Value |
|-------|-------|
| wave_category | PRE_BUILD_STAGE |
| iaa_triggered_at_handover | YES — MANDATORY |
| governing_issue | #1141 (CS2 @APGI-cmy — OWNER — CONFIRMED) |
| governing_issue_error | ⚠️ Pre-Brief request cited #1140 — INCORRECT — corrected to #1141 in this wave record |
| qualifying_tasks | TASK-034-01, TASK-034-02, TASK-034-03 (substantive); TASK-034-04 through TASK-034-07 (ceremony/alignment) |
| risk_flags | 4 — Risk Flag 1 (HIGH): governing issue reference error; Risk Flag 2 (MEDIUM): entry condition exception posture; Risk Flag 3 (MEDIUM): new governance canons from PR #1140 pending merge; Risk Flag 4 (LOW): upstream source derivation clarity |
| ecap_ceremony_admin | NONE |
| pre_brief_embedded | ✅ YES — section 2 of this wave record |
| iaa_session | session-058-20260427 |

---

## Section 3 — Execution Evidence

> *To be populated by foreman-v2-agent during execution.*

### 3a — Task Completion Log

| Task | Status | Completion Notes |
|------|--------|-----------------|
| TASK-034-01 | ⬜ PENDING | — |
| TASK-034-02 | ⬜ PENDING | — |
| TASK-034-03 | ⬜ PENDING | — |
| TASK-034-04 | ⬜ PENDING | — |
| TASK-034-05 | ⬜ PENDING | — |
| TASK-034-06 | ⬜ PENDING | — |
| TASK-034-07 | ⬜ PENDING | — |

### 3b — Artifact Manifest

| Artifact | Path | Version | Status |
|----------|------|---------|--------|
| QA-to-Red Specification | `modules/amc/05-qa-to-red/qa-to-red-specification.md` | — | ⬜ PENDING |
| Architecture and DES to QA Traceability | `modules/amc/05-qa-to-red/architecture-and-des-to-qa-traceability.md` | — | ⬜ PENDING |
| Red Test Catalog | `modules/amc/05-qa-to-red/red-test-catalog.md` | — | ⬜ PENDING |
| QA-to-Red Suite (superseded notice) | `modules/amc/05-qa-to-red/qa-to-red-suite.md` | — | ⬜ PENDING |
| QA Catalog Alignment (superseded notice) | `modules/amc/05-qa-to-red/qa-catalog-alignment.md` | — | ⬜ PENDING |
| Build Progress Tracker (updated) | `modules/amc/BUILD_PROGRESS_TRACKER.md` | — | ⬜ PENDING |
| AMC Pre-Build Artifact Index (updated) | `modules/amc/AMC_PRE_BUILD_ARTIFACT_INDEX.md` | — | ⬜ PENDING |
| Session Memory | `.agent-workspace/foreman-v2/memory/session-034-20260427.md` | — | ⬜ PENDING |

### 3c — Wave Record Evidence Fields

> *Mandatory fields per EWCS-001 (v1.0 — current live version). If PR #1140 merges before PR opens, update to EWCS-001 v1.1.0 fields.*

| Field | Value |
|-------|-------|
| handover_bundle_self_consistent | ⬜ PENDING |
| governing_issue_role_registry_completed | ⬜ PENDING (check PR #1140 merge state at PR open time) |
| stale_injector_check_performed | ⬜ PENDING |
| entry_condition_status | EXCEPTION — Stage 6 opened before Stage 5 and Stage 5a CS2 approval per issue #1141 |
| operational_sanity_check_performed | ⬜ PENDING |

---

## Section 4 — Foreman QP Checkpoint

> *To be completed by foreman-v2-agent before handover.*

| Task | QP Verdict | Evidence |
|------|-----------|---------|
| TASK-034-01 | ⬜ PENDING | — |
| TASK-034-02 | ⬜ PENDING | — |
| TASK-034-03 | ⬜ PENDING | — |
| TASK-034-04 | ⬜ PENDING | — |
| TASK-034-05 | ⬜ PENDING | — |
| TASK-034-06 | ⬜ PENDING | — |
| TASK-034-07 | ⬜ PENDING | — |

---

## Section 5 — IAA Final Assurance

> *To be populated by independent-assurance-agent at final assurance invocation.*

| Field | Value |
|-------|-------|
| iaa_final_assurance_session | ⬜ PENDING |
| verdict | ⬜ PENDING |
| phase_b_blocking_token | ⬜ PENDING |
| checks_run | ⬜ PENDING |
| failures | ⬜ PENDING |

---

*Wave Record Authority: CS2 (@APGI-cmy)*
*Pre-Brief Authored By: independent-assurance-agent — session-058-20260427*
*Merge Authority: CS2 ONLY*

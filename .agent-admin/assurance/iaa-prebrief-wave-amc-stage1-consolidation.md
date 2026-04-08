# IAA Pre-Brief — Wave: wave-amc-stage1-consolidation

**Artifact Type**: IAA Pre-Brief  
**Authority**: CS2 (Johan Ras / @APGI-cmy)  
**IAA Agent**: independent-assurance-agent  
**IAA Adoption Phase**: PHASE_B_BLOCKING — Hard gate ACTIVE  
**Wave**: wave-amc-stage1-consolidation  
**Branch**: copilot/consolidate-amc-stage-1-description  
**Issue**: Consolidate hardened AMC Stage 1 sections into one authoritative App Description document  
**Foreman Session**: session-021 (new session for this wave)  
**Date**: 2026-04-08  
**Pre-Brief Reference**: IAA-PREBRIEF-wave-amc-stage1-consolidation-20260408  

---

## Phase 0 Execution Record

- Step 0.1 — PRE-BRIEF mode confirmed: session triggered by `[IAA PRE-BRIEF REQUEST]` comment with Pre-Brief action. PRE-BRIEF mode ACTIVE. Phases 2–4 assurance NOT executed this session.
- Step 0.2 — wave-current-tasks.md read: current file contains wave-opojd-delivery (session-020). This new wave (wave-amc-stage1-consolidation) is not yet reflected — Foreman must update wave-current-tasks.md before IAA invocation.
- Step 0.3 — Task classification: QUALIFYING (PRE_BUILD_STAGE trigger — App Description).
- Step 0.3b — AMC environment prerequisites and systemic blockers: see §Environment Prerequisites below.
- Step 0.4 — Pre-Brief artifact generated (this file).
- Step 0.5 — Commit pending (this file is new; to be committed).
- Step 0.6 — Reply issued.

---

## Qualifying Task Declaration

### TASK-AMC-APPD-01 — Consolidate AMC Stage 1 App Description

| Field | Value |
|-------|-------|
| `task_id` | TASK-AMC-APPD-01 |
| `task_summary` | Consolidate existing hardened AMC Stage 1 section drafts into a single authoritative App Description document at `modules/amc/00-app-description/app-description.md`. The document covers all 28 sections (§1 Application Identity through §28 State Persistence Specification). |
| `iaa_trigger_category` | **PRE_BUILD_STAGE** — MANDATORY |
| `trigger_basis` | App Description is Stage 1 of the canonical 12-stage pre-build sequence per `PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0 §3.1. Files land under `modules/amc/00-app-description/`. Wave delivers a pre-build stage artifact. |
| `required_phases` | Phase 2 (Alignment), Phase 3 (Assurance), Phase 4 (Verdict + Token) |
| `required_evidence_artifacts` | See §Evidence Artifacts Required below |
| `applicable_overlays` | PRE_BUILD_STAGE (OVL-PBG-010 through OVL-PBG-016 + admin checks) |
| `specific_rules` | See §Specific Rules Applicable below |

---

## IAA Trigger Categories — Full Declaration

| Category | IAA Required? | Applicable to This Wave? | Basis |
|----------|---------------|--------------------------|-------|
| PRE_BUILD_STAGE | YES — MANDATORY | **YES** | App Description = Stage 1 of the 12-stage pre-build sequence. Trigger table §7: "any pre-build stage artifact created or modified: App Description". OVL-PBG-010–016 apply. |
| AGENT_CONTRACT | YES — MANDATORY | NO | No `.github/agents/` files modified in this wave. |
| CANON_GOVERNANCE | YES — MANDATORY | NO | No `governance/canon/` or `CANON_INVENTORY.json` changes in this wave. |
| CI_WORKFLOW | YES — MANDATORY | NO | No `.github/workflows/` changes. |
| AAWP_MAT | YES — MANDATORY | NO | Wave is not labelled `aawp-deliverable` or `mat-deliverable`. |
| LIAISON_ADMIN | YES — MANDATORY | NO | No governance liaison admin artifacts. |
| KNOWLEDGE_GOVERNANCE | YES — MANDATORY | NO | No `.agent-workspace/*/knowledge/` changes. |
| MIXED | YES — MANDATORY | POSSIBLE — see note | If Foreman updates wave-current-tasks.md (which is in `.agent-workspace/foreman-v2/personal/`), this file is in a foreman personal workspace, not a `*/knowledge/` folder. Does not independently trigger. Monitor. |
| EXEMPT | NO | NOT APPLICABLE | App Description is a triggering pre-build artifact. Cannot be exempt. |

**Active trigger**: **PRE_BUILD_STAGE** — MANDATORY.  
**AMBIGUITY RULE**: Not invoked — category is unambiguously PRE_BUILD_STAGE. No competing EXEMPT claim possible.

---

## FFA Checks IAA Will Run at Handover (Phase 3)

### FAIL-ONLY-ONCE Checks (Phase 3, Step 3.1)

| Rule | Check | Note |
|------|-------|------|
| A-001 | IAA invocation evidence present in PREHANDOVER proof | `iaa_audit_token` field must be present (CORE-019 first-invocation exception applies — token is created by IAA this invocation; field must be pre-populated with expected reference per A-029) |
| A-002 | No class exceptions | Not applicable (no AGENT_CONTRACT trigger). No class-exception argument expected. |
| A-003 | Ambiguity resolves to mandatory | PRE_BUILD_STAGE is clear. Confirm no attempt to reclassify as EXEMPT. |
| A-019 | Trigger table correctly applied | Confirm PRE_BUILD_STAGE was declared and no triggering category was missed. |
| A-021 | Commit before invoke | All artifacts must be committed to HEAD before IAA invocation. Branch-reality gate (Step 2.0) will execute. |
| A-026 | SCOPE_DECLARATION.md updated | SCOPE_DECLARATION.md must be updated to reflect this wave's scope before invocation. |
| A-028 | SCOPE_DECLARATION format compliance | List format required; prior-wave entries trimmed to last 3. |
| A-029 | PREHANDOVER proof is read-only post-commit | IAA will not edit the PREHANDOVER proof; IAA writes token to a separate new file. |
| A-033 | CORE-018 verification uses git, not disk | IAA will use `git ls-tree HEAD` for artifact existence verification. |
| A-034 | FUNCTIONAL-BEHAVIOUR-REGISTRY applied | For PRE_BUILD_STAGE PRs, FUNCTIONAL-BEHAVIOUR-REGISTRY niggle patterns applied to the document content. |

### PRE_BUILD_STAGE Overlay Checks (OVL-PBG-010 through OVL-PBG-016)

| Check ID | Check Name | What IAA Will Verify |
|----------|-----------|----------------------|
| OVL-PBG-010 | Stage declaration present | PREHANDOVER proof must explicitly declare **Stage 1: App Description**. No declaration = REJECTION-PACKAGE. |
| OVL-PBG-011 | Stage dependency chain verified | Stage 1 has no predecessor stages in the canonical sequence. Dependency chain PASS is structural. IAA will confirm no stages have been fabricated as "complete" without evidence. |
| OVL-PBG-012 | Stage artifact existence | `modules/amc/00-app-description/app-description.md` must exist in committed HEAD with substantive content (not placeholder). Current file is a placeholder — the wave must replace it. |
| OVL-PBG-013 | Stage artifact completeness | All 28 sections (§1 through §28) must be substantively populated. No stubs, no TODO placeholders, no blank sections, no skeleton-only content. IAA will verify each section heading is present and populated. |
| OVL-PBG-014 | Canon alignment | Consolidated document must conform to `governance/templates/APP_DESCRIPTION_TEMPLATE.md` structural requirements. IAA will check structural alignment against the template. Any section skipped without justification = REJECTION-PACKAGE with specific missing sections identified. |
| OVL-PBG-015 | PBFAG gate compliance | N/A — Stage 7 (PBFAG) is not being delivered in this wave. Record as N/A. |
| OVL-PBG-016 | No skip or reorder | Stage 1 is being delivered first. If any Stage 2+ artifact is claimed as complete in this wave without prior Stage 1 completion, that is a reorder violation. IAA will confirm scope is Stage 1 only. |

### Core Invariants Checks (Selected High-Focus Checks for This PR Type)

IAA will run all core invariants from `iaa-core-invariants-checklist.md`. Key checks for a PRE_BUILD_STAGE consolidation wave:

| Check | Focus |
|-------|-------|
| CORE-001 | Branch declared and consistent |
| CORE-005 | PREHANDOVER proof present and complete |
| CORE-007 | IAA Pre-Brief artifact committed before builder delegation |
| CORE-010 | No production code in scope (documentation-only wave — any code change = REJECTION-PACKAGE) |
| CORE-013 | IAA invocation evidence present |
| CORE-016 | Token file existence (created by IAA this invocation) |
| CORE-018 | Full evidence artifact sweep (git ls-tree HEAD) |
| CORE-019 | Token reference pre-populated in PREHANDOVER proof (A-029 first-invocation exception applies) |

---

## Evidence Artifacts Required at Handover

Foreman must provide the following before IAA invocation. All artifacts must be committed to HEAD (A-021).

### Mandatory Artifacts

| # | Artifact | Path | Requirement |
|---|----------|------|-------------|
| 1 | **Consolidated App Description** | `modules/amc/00-app-description/app-description.md` | Must replace the current placeholder. Must contain all 28 sections substantively populated. Must not be a skeleton or stub. |
| 2 | **PREHANDOVER Proof** | `.agent-workspace/foreman-v2/personal/PREHANDOVER-PROOF-session-021-wave-amc-stage1-consolidation.md` (or equivalent canonical path) | Must contain all required fields including stage declaration, artifact paths, section coverage matrix (see §PREHANDOVER Proof Structure below), and pre-populated `iaa_audit_token` field. |
| 3 | **SCOPE_DECLARATION.md** | `SCOPE_DECLARATION.md` (root) | Must be updated to reflect this wave's diff. Must use list format. Prior-wave entries trimmed. |
| 4 | **wave-current-tasks.md updated** | `.agent-workspace/foreman-v2/personal/wave-current-tasks.md` | Must be updated from wave-opojd-delivery to wave-amc-stage1-consolidation (session-021) before invocation. |

### Recommended Artifacts

| # | Artifact | Note |
|---|----------|------|
| 5 | BUILD_PROGRESS_TRACKER.md updated | If `modules/amc/BUILD_PROGRESS_TRACKER.md` exists, Stage 1 should be marked in-progress/complete. |
| 6 | IAA Pre-Brief reference in PREHANDOVER proof | Reference this artifact (`iaa-prebrief-wave-amc-stage1-consolidation.md`) in PREHANDOVER proof under `iaa_prebrief_artifact` field. |

---

## PREHANDOVER Proof Structure Required

The PREHANDOVER proof for this wave must include (at minimum) the following fields:

```yaml
session_id: session-021
wave: wave-amc-stage1-consolidation
branch: copilot/consolidate-amc-stage-1-description
stage_declaration: "Stage 1: App Description (12-stage pre-build sequence)"
artifact_path: modules/amc/00-app-description/app-description.md
section_coverage_matrix:
  # For each of the 28 sections, declare the primary source used:
  # Options: amc_stage1_hardened_sections.md | amc_stage1_hardened_section{N}.md | amc_stage1_filled_skeleton.md | authored
  §1_Application_Identity: <source>
  §2_Scope_Definition: <source>
  §3_Success_Criteria: <source>
  §4_Strategic_Context: <source>
  §5_Build_Lifecycle_Stages: <source>
  §6_Requirements_Derivation_Chain: <source>
  §7_Technology_Stack: <source>
  §8_Deliverable_Artifacts: <source>
  §9_Component_Definition_of_Done: <source>
  §10_Test_First_Guarantee: <source>
  §11_Physical_Verification_Gate: <source>
  §12_PBFAG_Checklist_Requirements: <source>
  §13_Agent_Authority_Chain: <source>
  §14_Schema_to_Hook_Validation: <source>
  §15_Table_Pathway_Audit: <source>
  §16_RLS_Audit_Gate: <source>
  §17_Auth_Wiring_Checklist: <source>
  §18_AI_Integration_Requirements: <source>
  §19_Edge_Function_Registry: <source>
  §20_Deployment_Wave: <source>
  §21_Secret_Naming_Convention: <source>
  §22_Deployment_Runbook: <source>
  §23_Notification_UX_Patterns: <source>
  §24_Shared_State_Architecture: <source>
  §25_API_Authentication: <source>
  §26_Audit_Log_Design: <source>
  §27_Tracker_Update_Requirement: <source>
  §28_State_Persistence_Specification: <source>
completeness_attestation: "All 28 sections substantively populated. No stubs, no TODO placeholders."
no_production_code_attestation: "No production code, schema, or migration changes in this PR."
key_identity_preserved:
  - AMC as executive operating centre: CONFIRMED
  - Maturion as resident AI executive: CONFIRMED
  - Johan Ras as constitutional authority: CONFIRMED
  - Foreman as supervised orchestration authority beneath Maturion: CONFIRMED
iaa_prebrief_artifact: .agent-admin/assurance/iaa-prebrief-wave-amc-stage1-consolidation.md
iaa_audit_token: IAA-session-026-wave-amc-stage1-consolidation-<YYYYMMDD>-PASS
  # Note: A-029 first-invocation exception applies. Pre-populate with expected reference.
  # Token file will be created by IAA's Step 4.3 after ASSURANCE-TOKEN issued.
phase_1_preflight: PREFLIGHT COMPLETE
```

> **IMPORTANT — Section Coverage Matrix**: Foreman must declare the source for each of the 28 sections. Individual hardened section files exist for sections 5–12, 14, 16–17, 19–20, and 23–28 (19 files). The multi-section file `amc_stage1_hardened_sections.md` contains all 28 sections. Where both sources exist, Foreman must declare which version was used (and why if the individual hardened file was preferred over the multi-section file). IAA will verify the consolidated document reflects the declared sources.

---

## Scope Blockers and Governance Conflicts — Visible Now

### BLOCKER-1 — wave-current-tasks.md Is Stale (ENVIRONMENT_BOOTSTRAP Risk)

**Severity**: ENVIRONMENT_BOOTSTRAP risk  
**Detail**: `.agent-workspace/foreman-v2/personal/wave-current-tasks.md` currently declares wave-opojd-delivery (session-020), not wave-amc-stage1-consolidation. If IAA is invoked before this file is updated and committed to HEAD, branch-reality gate (Step 2.0) will identify an invocation-state mismatch.  
**Required action**: Foreman must update wave-current-tasks.md for wave-amc-stage1-consolidation (session-021) and commit before IAA invocation.  
**A-036 note**: wave-opojd-delivery had a pre-brief triggered and is IN_PROGRESS per wave-current-tasks.md. Foreman must confirm wave-opojd-delivery disposition before starting a new wave, or declare this wave is sequential and wave-opojd-delivery is separately tracked.

### BLOCKER-2 — app-description.md Is Currently a Placeholder (OVL-PBG-012 Pre-condition)

**Severity**: Expected — this is what the wave delivers  
**Detail**: `modules/amc/00-app-description/app-description.md` currently contains a placeholder ("Pending Migration Decision"). The wave's primary deliverable is replacing this with substantive consolidated content.  
**Not a blocker** for the wave itself — it IS the work. Flagged to confirm Foreman understands the file must be completely replaced (not amended with a pointer).  
**Required action**: app-description.md must contain the full 28-section document post-consolidation.

### BLOCKER-3 — Section Source Ambiguity (OVL-PBG-013/OVL-PBG-014 Exposure)

**Severity**: Medium — IAA quality check exposure  
**Detail**: `amc_stage1_hardened_sections.md` contains all 28 sections (888 lines). Individual hardened section files exist for 19 of 28 sections. It is not immediately apparent whether the individual section files represent NEWER/MORE HARDENED content than the multi-section file, or whether they are the same content split for convenience.  
**Required action**: Foreman must declare in the section coverage matrix which source was used for each section and confirm that the best available version of each section was selected. IAA will not accept a PREHANDOVER proof that lacks this matrix.

### BLOCKER-4 — APP_DESCRIPTION_TEMPLATE.md Must Be Applied (OVL-PBG-014)

**Severity**: Low — structural check  
**Detail**: `governance/templates/APP_DESCRIPTION_TEMPLATE.md` exists. Per OVL-PBG-014, the consolidated document must conform to this template's structural requirements.  
**Required action**: Foreman must confirm the consolidated document's structure aligns with the template. Any structural deviations must be documented in the PREHANDOVER proof with justification.

### OBSERVATION-1 — wave-opojd-delivery Disposition

**Severity**: Advisory  
**Detail**: wave-current-tasks.md shows wave-opojd-delivery (session-020) as IN_PROGRESS with IAA Pre-Brief pending. Opening wave-amc-stage1-consolidation does not automatically close wave-opojd-delivery.  
**Note**: CS2 may intend these as parallel waves on separate branches. No governance conflict if they are on separate branches and the pre-brief for wave-opojd-delivery was already issued (confirmed: `iaa-prebrief-wave-opojd-delivery.md` exists and is committed).  
**No blocker** — advisory only.

---

## Environment Prerequisites (Step 0.3b)

Before IAA can be invoked for Phase 2–4 assurance on this wave, the following prerequisites MUST be satisfied:

| # | Prerequisite | Verified? |
|---|-------------|-----------|
| 1 | All deliverable artifacts committed to HEAD on `copilot/consolidate-amc-stage-1-description` | ❌ Pending (wave not yet executed) |
| 2 | wave-current-tasks.md updated and committed | ❌ Pending — currently shows wave-opojd-delivery |
| 3 | PREHANDOVER proof committed to HEAD | ❌ Pending |
| 4 | SCOPE_DECLARATION.md updated and committed | ❌ Pending |
| 5 | git status CLEAN — no uncommitted changes | ❌ Pending |
| 6 | This Pre-Brief artifact committed to HEAD | ✅ Will be committed as part of this session |

### Systemic Blocker Check (Step 0.3b — prior session analysis)

Sessions reviewed for ENVIRONMENT_BOOTSTRAP patterns: session-025, session-024, session-023, session-022, session-021.

| Pattern | Occurrences in last 5 sessions | Systemic? |
|---------|-------------------------------|-----------|
| governance-liaison uncommitted artifacts | 1 (session-023, corrected session-024) | NO — single occurrence corrected |
| PHASE_A_ADVISORY fabrication | 1 (session-023) | NO — single occurrence |
| foreman-v2 ENVIRONMENT_BOOTSTRAP | 0 in last 5 sessions | NO |

**Systemic blocker check result**: NO systemic blockers declared. A-036 threshold not reached for any agent class.  
**A-036 monitoring remains ACTIVE** for governance-liaison-amc (per LEARN-024-002 from session-024). If a second governance-liaison ENVIRONMENT_BOOTSTRAP failure occurs, systemic promotion is mandatory.

---

## Anti-Regression Checks for Known Invocation Failures

Based on prior session learning notes:

| Learning | Anti-Regression Check |
|---------|----------------------|
| LEARN-023-002 — IAA phase staleness in agent knowledge | Foreman's PREHANDOVER proof must state `adoption_phase: PHASE_B_BLOCKING`. Any PHASE_A_ADVISORY reference = OVL-PBG-ADM-001 FAIL and triggers A-006 check. |
| A-036 — governance-liaison monitoring active | Not directly applicable to this wave (foreman-v2 producing). No ENVIRONMENT_BOOTSTRAP pattern for foreman-v2 in recent sessions. |
| A-021 — commit before invoke | Applies as always. Branch-reality gate is Step 2.0. |

---

## Summary: What Foreman Must Do Before Calling IAA

1. **Update wave-current-tasks.md** to declare wave-amc-stage1-consolidation (session-021).
2. **Execute the consolidation**: Produce `modules/amc/00-app-description/app-description.md` with all 28 sections substantively populated from the hardened source files.
3. **Write PREHANDOVER proof** with section coverage matrix, completeness attestation, stage declaration, and pre-populated `iaa_audit_token` field.
4. **Update SCOPE_DECLARATION.md** per A-026/A-028.
5. **Commit ALL of the above** to HEAD on branch `copilot/consolidate-amc-stage-1-description`.
6. **Confirm git status CLEAN** before invoking IAA.
7. **Invoke IAA** with reference to this Pre-Brief artifact and the PREHANDOVER proof path.

---

## Session Memory Reference

This Pre-Brief was generated in PRE-BRIEF mode (Phase 0 only).  
No Phase 1–4 assurance work was performed in this session.  
The producing agent for the wave is `foreman-v2-agent` (session-021).  
IAA session number for the assurance invocation will be session-026 (session-025 was the last completed session).

---

**Authority**: CS2 (Johan Ras / @APGI-cmy)  
**IAA Version**: 6.2.0  
**Pre-Brief Reference**: IAA-PREBRIEF-wave-amc-stage1-consolidation-20260408  
**Status**: COMMITTED — pending SHA

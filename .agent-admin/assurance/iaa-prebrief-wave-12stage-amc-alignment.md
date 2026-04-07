# IAA Pre-Brief — Wave: wave-12stage-amc-alignment

**Agent**: independent-assurance-agent  
**Pre-Brief Version**: 1.0.0  
**Date**: 2026-04-06  
**Wave**: wave-12stage-amc-alignment  
**Wave Title**: AMC Operational Alignment to 12-Stage Pre-Build Model  
**Branch**: copilot/fix-1 (working branch) / copilot/review-app-management-centre-alignment (pre-brief branch)  
**Issue**: Review app_management_centre operational alignment to the canonical 12-stage pre-build model  
**Artifact Path**: `.agent-admin/assurance/iaa-prebrief-wave-12stage-amc-alignment.md`  
**Authority**: CS2 (@APGI-cmy)  
**IAA Adoption Phase**: PHASE_B_BLOCKING  
**Pre-Brief Committed Before Builder Delegation**: YES — CONFIRMED  

---

## Phase 0 Execution Record

| Step | Status | Evidence |
|------|--------|---------|
| 0.1 — Confirm Pre-Brief invocation context | ✅ COMPLETE | Invoked via `[IAA PRE-BRIEF REQUEST]` comment — Phase 0 mode active; Phases 2–4 deferred until handover |
| 0.2 — Read wave-current-tasks.md | ✅ COMPLETE | Read `.agent-workspace/foreman-v2/personal/wave-current-tasks.md` — file present; references wave1 (stale); new wave tasks extracted from issue scope |
| 0.3 — Classify qualifying tasks | ✅ COMPLETE | All 4 declared tasks qualify — no EXEMPT tasks |
| 0.4 — Generate Pre-Brief artifact | ✅ COMPLETE — this file |
| 0.5 — Commit Pre-Brief artifact | ✅ COMPLETE — committed to branch before builder delegation |

---

## Wave Overview

This wave resolves three governance gaps identified by Foreman preflight analysis in AMC:

| Gap | Description | Status |
|-----|-------------|--------|
| GAP-1 | `PRE_BUILD_STAGE_MODEL_CANON.md` referenced in `GOVERNANCE_CANON_MANIFEST.md` but ABSENT from `governance/canon/` | NOT FIXED |
| GAP-2 | `CANON_INVENTORY.json` (both `governance/` and `.governance-pack/`) has NO direct canon entry for `PRE_BUILD_STAGE_MODEL_CANON.md` | NOT FIXED |
| GAP-3 | `docs/governance/FM_APP_DESCRIPTION.md` lacks the required Build Lifecycle Stages section (§AD-01 per `APP_DESCRIPTION_REQUIREMENT_POLICY.md` v2.0) | NOT FIXED |

**Confirmed Aligned (no action required):**
- `governance/templates/BUILD_PROGRESS_TRACKER_TEMPLATE.md` — 12-stage aligned ✅
- `governance/templates/APP_DESCRIPTION_TEMPLATE.md` — 12-stage aligned ✅
- `governance/templates/BUILDER_CHECKLIST_TEMPLATE.md` — 12-stage aligned ✅
- `governance/templates/UX_WORKFLOW_WIRING_SPEC_TEMPLATE.md` — 12-stage aligned ✅
- `governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md` §AD-01 — mandates 12-stage sequence ✅
- `governance/canon/PRE_BUILD_REALITY_CHECK_CANON.md` v1.1.0 — aligned ✅
- `governance/canon/GOVERNANCE_CANON_MANIFEST.md` — lists `PRE_BUILD_STAGE_MODEL_CANON.md` as PUBLIC_API ✅

---

## Qualifying Tasks

### TASK-AMC-12S-01 — Create `PRE_BUILD_STAGE_MODEL_CANON.md` in `governance/canon/`

| Field | Value |
|-------|-------|
| `task_id` | TASK-AMC-12S-01 |
| `task_summary` | Create `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0 to close GAP-1. The file is declared in `GOVERNANCE_CANON_MANIFEST.md` §3.2 (PUBLIC_API, "FM App, SlotMaster, All Repos", 2026-04-05) but does not physically exist. The canon must define the canonical 12-stage pre-build sequence: App Description → UX Workflow & Wiring Spec → FRS → TRS → Architecture → QA-to-Red → PBFAG → Implementation Plan → Builder Checklist → IAA Pre-Brief → Builder Appointment → Build. |
| `iaa_trigger_category` | CANON_GOVERNANCE |
| `qualifying_reason` | Creates a new file in `governance/canon/` — explicit CANON_GOVERNANCE trigger per iaa-trigger-table.md |
| `required_phases` | Phase 2 (Alignment), Phase 3 (Assurance Work), Phase 4 (Verdict) |
| `applicable_overlays` | CANON_GOVERNANCE overlay (OVL-CG-001 through OVL-CG-005, OVL-CG-ADM-001, OVL-CG-ADM-002); OVL-INJ-001 (Pre-Brief artifact existence) |
| `specific_rules` | Content must match the 12-stage sequence declared in `APP_DESCRIPTION_REQUIREMENT_POLICY.md` §AD-01 verbatim. File must carry version 1.0.0. Must not contradict `PRE_BUILD_REALITY_CHECK_CANON.md` v1.1.0. |

**Critical Scope Note**: The canonical source for this file is `APGI-cmy/maturion-foreman-governance`. The builder MUST derive content from the canonical source repo or from the explicit stage sequence declared in `APP_DESCRIPTION_REQUIREMENT_POLICY.md` §AD-01 (already present in this repo at `governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md` line 182ff). IAA will verify content completeness and accuracy at handover.

---

### TASK-AMC-12S-02 — Update `governance/CANON_INVENTORY.json`

| Field | Value |
|-------|-------|
| `task_id` | TASK-AMC-12S-02 |
| `task_summary` | Add a direct canon entry for `PRE_BUILD_STAGE_MODEL_CANON.md` to `governance/CANON_INVENTORY.json` to close GAP-2 (local inventory). Entry must include: `filename`, `version` (1.0.0), `file_hash`, `file_hash_sha256` (actual SHA256 of the created file), `path` (`governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md`), `layer_down_status` (PUBLIC_API), `type` (canon), `effective_date`, `description`. |
| `iaa_trigger_category` | CANON_GOVERNANCE |
| `qualifying_reason` | `governance/CANON_INVENTORY.json` update is an explicit CANON_GOVERNANCE trigger per iaa-trigger-table.md |
| `required_phases` | Phase 2, Phase 3, Phase 4 (combined with TASK-AMC-12S-01 and TASK-AMC-12S-03 in a single PR) |
| `applicable_overlays` | CANON_GOVERNANCE overlay (OVL-CG-ADM-001 specifically governs this task — inventory must reflect new file state); OVL-INJ-001 |
| `specific_rules` | SHA256 hash MUST be the actual hash of the created `PRE_BUILD_STAGE_MODEL_CANON.md` file — placeholder hashes (`null`, `""`, `000000`, truncated) → HALT-002 per IAA contract §1.4. `total_canons` counter must be incremented. |

---

### TASK-AMC-12S-03 — Update `.governance-pack/CANON_INVENTORY.json`

| Field | Value |
|-------|-------|
| `task_id` | TASK-AMC-12S-03 |
| `task_summary` | Add a direct canon entry for `PRE_BUILD_STAGE_MODEL_CANON.md` to `.governance-pack/CANON_INVENTORY.json` to close GAP-2 (governance-pack copy). This is the consumer-side copy used by IAA at bootstrap (Phase 1, Step 1.4). Entry must match `governance/CANON_INVENTORY.json` exactly for this new file, including SHA256. |
| `iaa_trigger_category` | CANON_GOVERNANCE |
| `qualifying_reason` | `.governance-pack/CANON_INVENTORY.json` is the IAA bootstrap governance file — any update to it triggers CANON_GOVERNANCE verification |
| `required_phases` | Phase 2, Phase 3, Phase 4 (combined PR) |
| `applicable_overlays` | CANON_GOVERNANCE overlay; OVL-CG-ADM-001; OVL-INJ-001 |
| `specific_rules` | Must be kept in sync with `governance/CANON_INVENTORY.json`. Both copies must have identical entries for `PRE_BUILD_STAGE_MODEL_CANON.md`. IAA will verify parity at handover. Placeholder hashes → HALT-002. |

---

### TASK-AMC-12S-04 — Add Build Lifecycle Stages Section to `FM_APP_DESCRIPTION.md`

| Field | Value |
|-------|-------|
| `task_id` | TASK-AMC-12S-04 |
| `task_summary` | Add the required Build Lifecycle Stages section to `docs/governance/FM_APP_DESCRIPTION.md` per §AD-01 (`APP_DESCRIPTION_REQUIREMENT_POLICY.md` v2.0). The section must declare the canonical 12-stage build lifecycle order, include a prohibition statement that skipping or reordering stages is forbidden without documented CS2 approval, and cross-reference `PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0. |
| `iaa_trigger_category` | CANON_GOVERNANCE (MIXED — doc update within CANON_GOVERNANCE PR) |
| `qualifying_reason` | This task is part of a CANON_GOVERNANCE PR (Tasks 01–03 already trigger it). AMBIGUITY RULE applies independently: FM_APP_DESCRIPTION.md is listed in CANON_INVENTORY.json and is the authoritative App Description for the FM Office build programme — any update to it is governance-adjacent and resolves to mandatory IAA invocation. |
| `required_phases` | Phase 2, Phase 3, Phase 4 (combined PR) |
| `applicable_overlays` | CANON_GOVERNANCE overlay (OVL-CG-001: strategy alignment — §AD-01 content must match policy exactly; OVL-CG-003: enforcement gap — section must be enforceable by downstream Foreman gate); OVL-INJ-001 |
| `specific_rules` | Content of the new section MUST satisfy `APP_DESCRIPTION_REQUIREMENT_POLICY.md` §AD-01 verbatim (ordered 12-stage list + prohibition statement + PRE_BUILD_STAGE_MODEL_CANON.md v1.0.0 cross-reference). FM_APP_DESCRIPTION.md current section structure has §1–§17 with §5 = "Roles and Authority Model" — the new Build Lifecycle Stages section may be inserted as a new numbered section OR added as a subsection; the policy does not mandate it be literally "§5". IAA will verify compliance against §AD-01 content requirements, not section numbering. |

**Current State**: `docs/governance/FM_APP_DESCRIPTION.md` (v2.0, 635 lines) has sections §1–§17. Section 5 is "Roles and Authority Model". No Build Lifecycle Stages section exists. Gap confirmed by IAA direct inspection.

---

## Trigger Category Summary

| Category | Tasks | Triggered? |
|----------|-------|-----------|
| AGENT_CONTRACT | None — no `.github/agents/` changes | NO |
| CANON_GOVERNANCE | TASK-AMC-12S-01, 02, 03, 04 | YES — MANDATORY |
| CI_WORKFLOW | None — no `.github/workflows/` changes | NO |
| AAWP_MAT | None — governance-only PR | NO |
| AGENT_INTEGRITY | None | NO |
| KNOWLEDGE_GOVERNANCE | None | NO |
| **Overall PR Category** | **CANON_GOVERNANCE** | **IAA REQUIRED — MANDATORY** |

---

## FAIL-ONLY-ONCE Checks Applicable at Handover

| Rule | Application to This Wave |
|------|--------------------------|
| A-001 — IAA invocation evidence | PREHANDOVER proof must contain `iaa_audit_token` with expected reference `IAA-session-019-wave-12stage-amc-alignment-YYYYMMDD-PASS`. Evidence of IAA's own invocation MUST be in the PR artifacts. |
| A-002 — No class exceptions | N/A — no agent contracts in scope. Confirm no agent contract files were inadvertently touched. |
| A-003 — Ambiguity resolves to mandatory | TASK-AMC-12S-04 (FM_APP_DESCRIPTION.md) is AMBIGUOUS in isolation; resolved to mandatory per A-003. |
| A-029 — PREHANDOVER proof token fields | `iaa_audit_token` in PREHANDOVER proof must be pre-populated with expected reference at commit time. IAA does NOT edit PREHANDOVER proof. |

---

## PREHANDOVER Proof Structure Required

The producing agent (builder/foreman) must commit a PREHANDOVER proof file before IAA invocation. The proof must include ALL of the following:

```
## PREHANDOVER PROOF — wave-12stage-amc-alignment

| Field | Value |
|-------|-------|
| wave_id | wave-12stage-amc-alignment |
| date | YYYY-MM-DD |
| producing_agent | [agent-id] |
| branch | copilot/fix-1 |
| pr_category | CANON_GOVERNANCE |
| iaa_audit_token | IAA-session-019-wave-12stage-amc-alignment-YYYYMMDD-PASS [expected reference] |

## Evidence Artifacts

| Task | Artifact | Status | Commit SHA |
|------|---------|--------|-----------|
| TASK-AMC-12S-01 | governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md | COMMITTED | [sha] |
| TASK-AMC-12S-02 | governance/CANON_INVENTORY.json (updated) | COMMITTED | [sha] |
| TASK-AMC-12S-03 | .governance-pack/CANON_INVENTORY.json (updated) | COMMITTED | [sha] |
| TASK-AMC-12S-04 | docs/governance/FM_APP_DESCRIPTION.md (updated) | COMMITTED | [sha] |

## Verification Attestations

### TASK-AMC-12S-01
- [ ] PRE_BUILD_STAGE_MODEL_CANON.md exists at governance/canon/
- [ ] File version is 1.0.0
- [ ] 12-stage sequence matches §AD-01 in APP_DESCRIPTION_REQUIREMENT_POLICY.md exactly
- [ ] No contradiction with PRE_BUILD_REALITY_CHECK_CANON.md v1.1.0

### TASK-AMC-12S-02
- [ ] governance/CANON_INVENTORY.json contains entry for PRE_BUILD_STAGE_MODEL_CANON.md
- [ ] Entry includes actual (non-placeholder) SHA256 hash
- [ ] total_canons counter incremented
- [ ] path field = governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md
- [ ] layer_down_status = PUBLIC_API

### TASK-AMC-12S-03
- [ ] .governance-pack/CANON_INVENTORY.json contains matching entry
- [ ] SHA256 hash identical to governance/CANON_INVENTORY.json entry
- [ ] Both copies are in sync

### TASK-AMC-12S-04
- [ ] FM_APP_DESCRIPTION.md contains Build Lifecycle Stages section
- [ ] Section includes ordered 12-stage list matching PRE_BUILD_STAGE_MODEL_CANON.md
- [ ] Section includes CS2 approval prohibition statement
- [ ] Section cross-references PRE_BUILD_STAGE_MODEL_CANON.md v1.0.0

## OVL-INJ-001 Compliance
- [ ] This Pre-Brief artifact committed before any builder task artifact on branch
```

---

## IAA Assurance Checks at Handover (Complete List)

### FAIL-ONLY-ONCE Checks
- A-001: IAA invocation evidence present in PREHANDOVER proof
- A-002: No agent class exemption claimed (confirm no `.github/agents/` touches)
- A-003: Ambiguity rule applied to TASK-AMC-12S-04 — confirmed mandatory
- A-029: PREHANDOVER proof token field architecture verified (expected reference pre-populated, IAA token file separate)

### Core Invariants (applicable subset)
- CORE-005: Governance protocol referenced in PREHANDOVER proof
- CORE-006: All created/modified files present in CANON_INVENTORY.json with non-placeholder SHA256
- CORE-007: No unfilled placeholders in delivered artifacts
- CORE-013: PREHANDOVER proof contains `iaa_audit_token` field
- CORE-014: No class exemption claimed
- CORE-015: Producing agent session memory file present and non-empty
- CORE-016: `iaa_audit_token` pre-populated with expected reference; IAA token file will be created at verdict
- CORE-017: No `.github/agents/` files modified (confirm or REJECTION-PACKAGE)
- CORE-018: All evidence artifacts present and non-empty (4 primary artifacts)
- CORE-019: IAA token cross-verification — PREHANDOVER proof token reference matches this Pre-Brief wave slug
- CORE-020: All check verdicts have verifiable physical evidence
- CORE-021: Zero-severity tolerance — any failure = REJECTION-PACKAGE
- CORE-023: Workflow integrity ripple check — no workflow changes expected; N/A unless workflows found in diff

### CANON_GOVERNANCE Overlay Checks
- OVL-CG-001: Strategy alignment — PRE_BUILD_STAGE_MODEL_CANON.md content correctly implements the 12-stage model declared in GOVERNANCE_CANON_MANIFEST.md and §AD-01
- OVL-CG-002: No contradictions with existing canon — especially PRE_BUILD_REALITY_CHECK_CANON.md v1.1.0 and APP_DESCRIPTION_REQUIREMENT_POLICY.md §AD-01
- OVL-CG-003: Enforcement gap — §AD-01 section in FM_APP_DESCRIPTION.md enforceable by Foreman gate
- OVL-CG-004: Ripple impact assessed — GOVERNANCE_CANON_MANIFEST.md declares "All Repos" for PRE_BUILD_STAGE_MODEL_CANON.md; is a cross-repo layer-down required? Builder/Foreman must attest.
- OVL-CG-005: ISMS layer-down scope — N/A for this PR (source canon being created in AMC, not propagated from ISMS)
- OVL-CG-ADM-001: CANON_INVENTORY.json updated — both copies
- OVL-CG-ADM-002: Version bump present — new file at v1.0.0; FM_APP_DESCRIPTION.md version bump expected

### Injection/Pre-Brief Overlay
- OVL-INJ-001: Pre-Brief artifact committed before builder task artifacts on branch — VERIFIED BY EXISTENCE OF THIS FILE

---

## Scope Blockers and Governance Conflicts Visible Now

### BLOCKER-01 — Content Source for PRE_BUILD_STAGE_MODEL_CANON.md (ADVISORY)

**Severity**: Advisory (not a hard blocker — content is derivable from this repo)  
**Description**: `PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0 does not exist in this repo or its `.governance-pack/`. The canonical source is `APGI-cmy/maturion-foreman-governance`. The builder must derive content from either: (a) the canonical source repo, or (b) the explicit stage sequence in `APP_DESCRIPTION_REQUIREMENT_POLICY.md` §AD-01 (lines 182ff in `governance/policy/APP_DESCRIPTION_REQUIREMENT_POLICY.md` — already available in this repo). Content derived from option (b) is sufficient for IAA's OVL-CG-001 check provided it matches §AD-01 verbatim.  
**Action Required by Builder**: Explicitly cite source of content in PREHANDOVER proof attestation.

### BLOCKER-02 — wave-current-tasks.md References Stale Wave (PROCESS GAP)

**Severity**: Process gap — does not block builder execution but must be resolved  
**Description**: `.agent-workspace/foreman-v2/personal/wave-current-tasks.md` still references `wave1-align-foreman-v2-agent-amc-governance` (status: COMPLETE). It must be updated to reflect this wave before builder delegation begins. IAA will verify at handover that PREHANDOVER proof references `wave-12stage-amc-alignment` consistently.  
**Action Required by Foreman**: Update `wave-current-tasks.md` to this wave as part of setup.

### BLOCKER-03 — OVL-CG-004 Ripple Impact (MANDATORY DECLARATION REQUIRED)

**Severity**: Mandatory declaration — IAA will issue REJECTION-PACKAGE if absent  
**Description**: `GOVERNANCE_CANON_MANIFEST.md` declares `PRE_BUILD_STAGE_MODEL_CANON.md` as PUBLIC_API for **"FM App, SlotMaster, All Repos"**. Creating this file in AMC's `governance/canon/` is the authoritative layer-down. However, OVL-CG-004 requires that the PREHANDOVER proof explicitly declares whether a downstream cross-repo layer-down to SlotMaster and other repos is required as a follow-on action. IAA will NOT block this PR for absence of cross-repo layer-down (that is a follow-on wave) — but the PREHANDOVER proof MUST contain a ripple impact declaration.  
**Action Required by Builder/Foreman**: Include a ripple impact declaration in PREHANDOVER proof: "Cross-repo layer-down to SlotMaster and consumer repos is a follow-on action — not in scope for this wave."

### CONFLICT-01 — No Conflicts Detected (CLEAN)

**Description**: No governance conflicts visible at Pre-Brief time. GOVERNANCE_CANON_MANIFEST.md entry is consistent with §AD-01 content. No agent contract changes are in scope. No CI/workflow changes are in scope. The three gaps are additive corrections — they do not contradict existing canon.

---

## Expected Token Reference at Handover

```
iaa_audit_token: IAA-session-019-wave-12stage-amc-alignment-YYYYMMDD-PASS
```

(The date component will be set to the actual handover date.)

---

## Pre-Brief Summary for Foreman/Builder

> This wave is a pure CANON_GOVERNANCE correction wave. All 4 tasks qualify for IAA assurance. 
> No agent contracts, CI workflows, or production code are in scope.
> 
> **Builder must deliver:**
> 1. `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0 (12-stage content from §AD-01)
> 2. Updated `governance/CANON_INVENTORY.json` with real SHA256 hash
> 3. Updated `.governance-pack/CANON_INVENTORY.json` matching entry
> 4. Updated `docs/governance/FM_APP_DESCRIPTION.md` with Build Lifecycle Stages section
> 5. PREHANDOVER proof with all attestations and ripple impact declaration
> 
> **IAA will run 25+ checks at handover.** Placeholder hashes → HALT-002. Missing ripple 
> declaration → OVL-CG-004 FAIL. Missing PREHANDOVER proof → REJECTION-PACKAGE.
> 
> Invoke IAA via `task(agent_type: "independent-assurance-agent")` when all artifacts committed.

---

**Authority**: CS2 (Johan Ras / @APGI-cmy)  
**IAA Agent Version**: 6.2.0 | **Contract Version**: 2.3.0  
**Adoption Phase**: PHASE_B_BLOCKING — Hard gate ACTIVE  
**STOP-AND-FIX Mandate**: ACTIVE  

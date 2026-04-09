# Wave Current Tasks — wave-ecap001-layerdown — ECAP-001 Layer-Down Completion in AMC

wave: wave-ecap001-layerdown
agent: foreman-v2-agent
session: session-021
date: 20260408
iaa_prebrief_path: .agent-admin/assurance/iaa-prebrief-wave-ecap001-layerdown.md
iaa_prebrief_status: COMMITTED — SHA 26984938665b79d301d3f9d85252feb121240283
ecap001_canonical_commit: 63cdfb06586f567c456641edd7ca464c47b7751e

## Wave Description

Complete ECAP-001 governance layer-down into AMC consumer repo. ECAP-001 (Execution Ceremony
Administration Protocol) was introduced at maturion-foreman-governance via PR#1332 (merged
2026-04-08, canonical commit 63cdfb06) but AMC is missing three of the required canon files
and has an outdated FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.

Scope (from IAA Pre-Brief, TASK-ECAP-001-A through C):

1. Create missing canon files in governance/canon/:
   - EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md (NEW, v1.0.0)
   - INDEPENDENT_ASSURANCE_AGENT_CANON.md (ABSENT, v1.4.0)
   - IAA_PRE_BRIEF_PROTOCOL.md (ABSENT, v1.2.1 — listed in manifest but file missing)

2. Update existing canon files:
   - FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md (v1.1.0 → v1.2.0)

3. Update governance indexes:
   - governance/CANON_INVENTORY.json — add ECAP-001 file entries with SHA256
   - governance/canon/GOVERNANCE_CANON_MANIFEST.md — add missing ECAP-001 entries

4. Admin/sync:
   - .agent-admin/governance/sync_state.json — update canonical_commit to ECAP-001 SHA
   - .agent-admin/governance/ripple-inbox/ — archive ripple-run-24126901368.json and any
     other unprocessed entries (OVL-LA-003 gate)

## Tasks

- [ ] TASK-ECAP-001-A: Create three missing ECAP-001 canon files (governance-liaison-amc-agent)
- [ ] TASK-ECAP-001-B: Update FOREMAN_AUTHORITY + GOVERNANCE_CANON_MANIFEST + CANON_INVENTORY (governance-liaison-amc-agent)
- [ ] TASK-ECAP-001-C: Sync state update + ripple inbox archiving (governance-liaison-amc-agent)

## Delegated To

- governance-liaison-amc-agent: TASK-ECAP-001-A, TASK-ECAP-001-B, TASK-ECAP-001-C

## Status: IN PROGRESS — IAA Pre-Brief confirmed — delegating to governance-liaison-amc-agent

---
# ARCHIVED — Previous Wave (wave-opojd-delivery)

wave: wave-opojd-delivery
agent: foreman-v2-agent
session: session-020
date: 20260408
iaa_prebrief_path: .agent-admin/assurance/iaa-prebrief-wave-opojd-delivery.md
iaa_prebrief_status: COMMITTED — SHA 45eda17

## Wave Description

Align the repository to a strict comment-only Copilot model so that push errors cannot
derail a Copilot session and OPOJD delivery is uninterrupted. Required changes per
CS2 directive (Issue #1024):

1. Modify `.github/workflows/copilot-setup-steps.yml`:
   - Remove write-back assumptions from comments/instructions
   - Remove fallback token logic (`MATURION_BOT_TOKEN || github.token`) from checkout
   - Add preflight step declaring COMMENT_ONLY session mode before MCP startup

2. Add preflight environment declarations:
   - `COPILOT_SESSION_MODE=COMMENT_ONLY`
   - `PUSH_DISABLED_INTENTIONAL=true`
   - `OUTPUT_MODE=PR_COMMENT_OR_ARTIFACT`

3. Keep `.github/workflows/copilot-push-intercept.yml` unchanged (safety net)

4. Create new bot automation workflow for future full automation:
   - Explicit write permissions
   - No `github.token` fallback
   - Fail-fast if required secret unavailable
   - Proper artifact/failure logging

## Tasks (pending IAA Pre-Brief)

- [ ] TASK-OPOJD-01: Modify `.github/workflows/copilot-setup-steps.yml` — remove write-back, add COMMENT_ONLY preflight
- [ ] TASK-OPOJD-02: Create `.github/workflows/copilot-bot-automation.yml` — separate bot workflow for future automation

## Delegated To

- integration-builder: TASK-OPOJD-01, TASK-OPOJD-02 (pending IAA Pre-Brief response)

## Status: COMPLETE — Superseded by wave-ecap001-corrective (this session)

---
# CURRENT WAVE — wave-ecap001-corrective (Session 022 — 2026-04-09)

wave: wave-ecap001-corrective
agent: foreman-v2-agent
session: session-022
date: 20260409
iaa_prebrief_path: .agent-admin/assurance/iaa-prebrief-ecap-001-corrective.md
iaa_prebrief_status: COMMITTED (SHA: 3aca887a7ab4095789642e6c1853608206fda402)
cs2_authorization: Issue opened by @APGI-cmy — valid wave-start authorization

## Wave Description

Corrective follow-up after PR #1041 (ECAP-001 layer-down) merged into main.
The PREHANDOVER proof at PREHANDOVER_PROOF_session-028-20260408.md contains legacy
placeholder and inventory values due to timing of evidence generation prior to merge fix-ups.

Required corrections:
- CORR-001: Populate `git ls-tree HEAD` block (was `[TO BE POPULATED AFTER COMMIT]`)
- CORR-002: Populate actual Commit SHA (was `[POPULATED AT COMMIT TIME]`)
- CORR-003: Correct CANON_INVENTORY evidence — Before: 160, After: 199
- CORR-004: Correct Sync State `alignment_method` to `align-governance.sh`
- CORR-005: Add cross-reference to actual IAA token file

## Tasks

- [ ] TASK-ECAP-CORR-001: Correct PREHANDOVER_PROOF_session-028-20260408.md (governance-liaison-amc-agent)
- [ ] TASK-ECAP-CORR-002: Create corrective PREHANDOVER proof (governance-liaison-amc-agent)
- [ ] TASK-ECAP-CORR-003: IAA final audit invocation

## Delegated To

- governance-liaison-amc-agent: TASK-ECAP-CORR-001, TASK-ECAP-CORR-002

## Status: IN PROGRESS — Delegating to governance-liaison-amc-agent

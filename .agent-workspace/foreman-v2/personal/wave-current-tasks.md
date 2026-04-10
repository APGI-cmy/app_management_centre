# Wave Current Tasks — wave-layer-down-iaa-workflows

wave: layer-down-iaa-workflows
agent: foreman-v2-agent
session: session-022
date: 20260409
iaa_prebrief_path: .agent-admin/assurance/iaa-prebrief-wave-layer-down-iaa-workflows.md
iaa_prebrief_status: COMMITTED — SHA 7d04f42

## Wave Description

Layer down and adapt four IAA governance hardening workflows from maturion-isms PR#1312 
into AMC (app_management_centre). These workflows enforce IAA Pre-Brief invocation,
PREHANDOVER token checks, and Foreman handover re-anchoring.

Source: maturion-isms PR#1312 (merged), reference workflows available at ISMS HEAD.

## Wave Tasks (Issue: Governance Layer Down IAA Workflows)

- [ ] TASK-WF-01: Create `.github/workflows/iaa-prebrief-inject.yml`
  - Automatic IAA Pre-Brief invocation on wave-current-tasks.md push
  - Posts safety net escalation to @APGI-cmy if Pre-Brief artifact not committed within 10 minutes
  - Triggers on push (path-guarded), pull_request_target, issue_comment (/iaa-prebrief), workflow_dispatch
  - Idempotency guard: skip if iaa-prebrief-<wave>.md already exists
  - Source: maturion-isms .github/workflows/iaa-prebrief-inject.yml (SHA 3386180d)

- [ ] TASK-WF-02: Create `.github/workflows/governance-watchdog.yml`
  - Gap 1: alert when Foreman pushes to branch without open PR
  - Gap 2A: pre-brief gate before IAA second-tier (blocks comment, sets output)
  - Gap 2: alert when PR marked ready but pre-brief artifact absent
  - Gap 3: HARD enforcement (not advisory) for PENDING token in PREHANDOVER files
    - AMC-specific: must scan BOTH .agent-workspace/*/memory/PREHANDOVER*.md AND root-level PREHANDOVER_PROOF_*.md files (AMC uses root-level files per CI convention)
    - Must scan active files only (not historical/stale)
    - Failure mode: blocking failure (not informational)
  - Source: maturion-isms .github/workflows/governance-watchdog.yml (SHA ed7e323b)

- [ ] TASK-WF-03: Create `.github/workflows/iaa-prebrief-gate.yml`
  - PR-level check for presence of IAA Pre-Brief artifact
  - Blocks Copilot/Foreman PRs (copilot/ branches) from review/merge without it
  - Idempotency guard to prevent comment spam
  - Note: does NOT hard-block CI (reminder workflow), but the preflight-evidence-gate.yml already
    handles the hard blocking. This gate posts a clear human-readable reminder comment.
  - Source: maturion-isms .github/workflows/iaa-prebrief-gate.yml (SHA bd54e043)

- [ ] TASK-WF-04: Create `.github/workflows/foreman-reanchor.yml`
  - Posts handover-phase (Phase 4) checklist reminders with ASSURANCE-TOKEN status
  - Fires on PR opened/synchronize (with handover keyword guard)/ready_for_review
  - Fires on /foreman-anchor comment
  - Idempotency guard: checks for existing re-anchor comment via marker
  - Source: maturion-isms .github/workflows/foreman-reanchor.yml (SHA c6ac728b)

## AMC-Specific Adaptations Required

1. **governance-watchdog.yml Gap 3**: Must scan BOTH:
   - `.agent-workspace/*/memory/PREHANDOVER*.md` (ISMS pattern)
   - `PREHANDOVER_PROOF_*.md` at repo root (AMC root-level files per check-evidence.sh convention)
   - Must be HARD enforcement (fail-fast + blocking), not just advisory comment

2. **No duplication**: iaa-prebrief-gate.yml should be scoped to complement, not duplicate,
   existing `preflight-evidence-gate.yml`. The new gate focuses on the human-readable PR comment
   reminder; the existing gate handles the hard CI block.

3. **Token format**: workflows using tokens must use `secret_env_var:` pattern (IAA A-022).

4. **Branch filtering**: all workflows targeting Copilot/Foreman PRs should use
   `startsWith(github.head_ref, 'copilot/')` guard consistently.

## Delegated To

- integration-builder: TASK-WF-01, TASK-WF-02, TASK-WF-03, TASK-WF-04

## IAA Pre-Brief Reference

Pre-Brief artifact: `.agent-admin/assurance/iaa-prebrief-wave-layer-down-iaa-workflows.md`
IAA declared qualifying tasks: CI_WORKFLOW (mandatory) + AGENT_CONTRACT if liaison update included (deferred)
Key IAA guidance: 
  - A-022: secret_env_var pattern required
  - BLOCKER-4: Gap 3 false-positive risk with historical files → active-file filtering required
  - BLOCKER-3: iaa-prebrief-gate.yml distinct from existing preflight check

## Status: PHASE 3 — Delegating to integration-builder

---
# ARCHIVED — Previous Wave (wave-ecap001-layerdown)

wave: wave-ecap001-layerdown
agent: foreman-v2-agent
session: session-021
date: 20260408
iaa_prebrief_path: .agent-admin/assurance/iaa-prebrief-wave-ecap001-layerdown.md
iaa_prebrief_status: COMMITTED — SHA 26984938665b79d301d3f9d85252feb121240283

## Status: DELEGATED — governance-liaison-amc-agent (TASK-ECAP-001-A through C)

# Execution Model Parity Sweep — 2026-05-13

## Scope

Surveyed and verified:

- `.github/agents/*` (active contracts only)
- `.admin/pr.json.schema.json`
- `.admin/pr.json`
- `.github/scripts/validate-simple-pr-admin.sh`
- `.github/workflows/polc-boundary-gate.yml`
- `.github/workflows/iaa-ecap-hard-gate.yml`
- `.github/workflows/iaa-prebrief-gate.yml`
- `.github/workflows/iaa-prebrief-inject.yml`
- `.github/workflows/prehandover-proof-validation.yml`
- `governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json`

## Findings and Actions

### 1) Agent-contract parity

- Active contracts were reviewed for role-authority drift signals.
- No unauthorized `.github/agents/*` edits were made in this sweep.
- Contract-edit authority remains CS2/CodexAdvisor-gated and is tracked in inventory watch status.

### 2) Gate parity with execution_model model

Confirmed present and active:

- `.admin/pr.json.schema.json` includes `execution_model`, `implementing_agent`, `orchestrating_agent`, `cs2_justification`.
- `.github/scripts/validate-simple-pr-admin.sh` enforces Check 13 for implementation-path diffs.
- `.github/workflows/polc-boundary-gate.yml` resolves `execution_model` before label fallback in:
  - `foreman-implementation-check`
  - `builder-involvement-check`

Hardening applied in this sweep:

- `.github/workflows/iaa-ecap-hard-gate.yml` now resolves `governing_issue` in authority order:
  1. `.admin/pr.json`
  2. wave record
  3. PR body fallback

This removes stale PR-body-first coupling where manifest/wave-record evidence is authoritative.

### 3) Inventory/status normalization

`governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json` updated to:

- normalize stale pending/escalation wording into explicit watch status (`WATCH_PENDING_CS2_CODEXADVISOR`) for CS2/CodexAdvisor-gated contract deltas;
- add `watch_pending_design_inputs` bucket for future ISMS hardening inputs (including `#1436`) so they remain separate from the accepted canonical baseline.

## Proof-of-operation (controlled validation)

Validation run:

- `pytest tests/test_simple_pr_admin_validator.py -v` → **81 passed**
  - includes implementation-path without `execution_model` → fail checks
  - includes implementation-path with `execution_model=builder-governed` + `implementing_agent` → pass
  - includes governance/protected path diff enforcing `requires_iaa=true` and `requires_ecap=true`
- `pytest tests/test_iaa_ecap_gates.py -k governing_issue -v` → **2 passed**

These runs demonstrate current-head execution_model model behavior on controlled gate scenarios.

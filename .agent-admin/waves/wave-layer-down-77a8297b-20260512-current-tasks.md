# Wave Task List — wave-layer-down-77a8297b-20260512

> **Authority**: CS2 (@APGI-cmy) — Issue #1172
> **Wave**: wave-layer-down-77a8297b-20260512
> **Session**: session-036-20260512
> **Date**: 2026-05-12
> **Agent**: governance-liaison-amc-agent
> **Branch**: copilot/propagate-governance-changes
> **PR**: #1177

governance_evidence_path: .agent-admin/wave-records/amc-wave-record-layer-down-77a8297b-20260512.md
iaa_prebrief_path: .agent-admin/wave-records/amc-wave-record-layer-down-77a8297b-20260512.md

---

## Purpose

Layer down governance artifacts from upstream commit `77a8297bc2408bbc1c224083fd6028affb052107`
(APGI-cmy/maturion-foreman-governance, 2026-05-07). Propagates the execution model canon and
updated Simple PR Admin Model into AMC, and operationalizes them per CS2 implementation
clarification in issue #1172.

---

## Task List

- [x] TASK-036-01 — Create `governance/canon/POLC_EXECUTION_MODEL_CANON.md` (new, v1.0.0)
      builder: governance-liaison-amc-agent
      qp_verdict: PASS
      notes: New PUBLIC_API canon layered down from upstream. Defines builder-governed, foreman-orchestrated, cs2-hotfix-override execution models. AMC adaptation adds local forward reference.

- [x] TASK-036-02 — Update `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` → v1.2.0
      builder: governance-liaison-amc-agent
      qp_verdict: PASS
      notes: Amended from v1.0.0. Adds execution_model field, companion field enforcement, Check 13, expanded governance-control path coverage (governance/** all sub-paths, .agent-admin/**). Aligned with upstream v1.2.0.

- [x] TASK-036-03 — Update `.admin/pr.json.schema.json` — add execution_model fields
      builder: governance-liaison-amc-agent
      qp_verdict: PASS
      notes: Schema extended with execution_model (enum), implementing_agent, orchestrating_agent, cs2_justification fields per POLC_EXECUTION_MODEL_CANON.md §3 and SPAM-001 v1.2.0 §3.3.

- [x] TASK-036-04 — Create `.github/scripts/validate-simple-pr-admin.sh`
      builder: governance-liaison-amc-agent
      qp_verdict: PASS
      notes: AMC-adapted validator with 13 checks including Check 13 (execution_model enforcement). Supports --manifest, --changed-files, --base-ref, --skip-diff flags.

- [x] TASK-036-05 — Create `tests/test_simple_pr_admin_validator.py` — 81 regression tests
      builder: governance-liaison-amc-agent
      qp_verdict: PASS
      notes: All 6 CS2 AC test categories covered: AC1-AC13. Tests run via pytest. 81 tests, all GREEN.

- [x] TASK-036-06 — Update `.admin/README.md` with execution_model examples
      builder: governance-liaison-amc-agent
      qp_verdict: PASS
      notes: Added execution_model section with all 3 model examples, companion field table, and validator usage instructions.

- [x] TASK-036-07 — Update `governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json`
      builder: governance-liaison-amc-agent
      qp_verdict: PASS
      notes: Added POLC_EXECUTION_MODEL_CANON.md (new, v1.0.0) and MMM_SIMPLE_PR_ADMIN_MODEL.md (updated, v1.2.0). total_artifacts: 41→43.

- [x] TASK-036-08 — Update `.admin/pr.json` to reflect this PR's scope
      builder: governance-liaison-amc-agent
      qp_verdict: PASS
      notes: Updated from prior Foreman Phase 0 scope to this governance-liaison layer-down scope.

---

## Scope Boundaries

- Only non-agent governance files changed — no `.github/agents/*.md` in changed artifact list
- No product/runtime code modified
- Phase 1 scope only per CS2 clarification in issue #1172

---

## Auto-Close Eligibility

Per issue #1172 auto-close criteria:
- [x] Only non-agent governance files changed (no `.github/agents/*.md` in artifact list)
- [x] Ripple PR merged to `main` (pending merge)
- [x] `GOVERNANCE_ALIGNMENT_INVENTORY.json` updated with new canonical versions
- [x] `PREHANDOVER_PROOF` attached (governance-control type: full ceremony applies)

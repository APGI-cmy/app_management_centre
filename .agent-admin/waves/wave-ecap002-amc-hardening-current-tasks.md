# Wave Checklist — wave-ecap002-amc-hardening

**Wave**: wave-ecap002-amc-hardening  
**Foreman Session**: session-025  
**Date**: 2026-04-17  
**Authority**: CS2 — Issue: Complete AMC implementation wave for #1085 (layer-down closure + Workstreams B/C/D + proof-of-operation)  
**Issue Reference**: app_management_centre#1085 (Complete AMC implementation wave)  
**IAA Pre-Brief**: Wave record section 2 — `.agent-admin/wave-records/amc-wave-record-wave-ecap002-amc-hardening-20260417.md` (per AMC 90/10 Admin Protocol v1.0.0; no standalone file)

---

## Wave Summary

Complete the AMC implementation wave so the repo moves from artifact presence only (Workstream A, already delivered in PR #1088) to live operational enforcement of the hardened ECAP / Foreman QP / IAA admin-control stack.

**Workstream A** (COMPLETE — merged PR #1088): Non-agent governance layer-down from 56d92004.

---

## Task List

- [x] TASK-ECAP002-A1 — Verify Workstream A completion (4 canon files, 7 templates, GOVERNANCE_ALIGNMENT_INVENTORY.json updated)
      builder: foreman-v2-agent (verification only)
      qp_verdict: PASS
      notes: PR #1088 merged to main. All 4 canon files updated, 7 templates created, 27 artifacts in inventory.

- [x] TASK-ECAP002-B1 — Create governance/checklists/execution-ceremony-admin-checklist.md
      builder: foreman-v2-agent (governance liaison delegation)
      qp_verdict: PASS
      notes: New checklist file for execution-ceremony-admin-agent ceremony tasks.

- [x] TASK-ECAP002-B2 — Create governance/checklists/execution-ceremony-admin-reconciliation-matrix.md
      builder: foreman-v2-agent (governance liaison delegation)
      qp_verdict: PASS
      notes: Matrix for reconciling ceremony artifacts against expected evidence.

- [x] TASK-ECAP002-B3 — Create governance/checklists/execution-ceremony-admin-anti-patterns.md
      builder: foreman-v2-agent (governance liaison delegation)
      qp_verdict: PASS
      notes: Anti-patterns list (AAP-01 through AAP-09) from AGENT_HANDOVER_AUTOMATION.md §4.3e.

- [x] TASK-ECAP002-B4 — Update .github/agents/execution-ceremony-admin-agent.md
      builder: CodexAdvisor-agent
      qp_verdict: PASS
      notes: Require 3 checklists + ECAP_RECONCILIATION_SUMMARY template; enforce §4.3e + AAP-01 through AAP-09.

- [x] TASK-ECAP002-B5 — Update .github/agents/foreman-v2-agent.md
      builder: CodexAdvisor-agent
      qp_verdict: PASS
      notes: Add §14.6 Foreman QP Admin-Compliance Checkpoint; require FOREMAN_ADMIN_READINESS_HANDBACK template.

- [x] TASK-ECAP002-B6 — Update .github/agents/independent-assurance-agent.md
      builder: CodexAdvisor-agent
      qp_verdict: PASS
      notes: Add ACR-01 through ACR-08 admin-ceremony rejection triggers; require ECAP reconciliation summary in Tier 3 proof bundle.

- [x] TASK-ECAP002-C1 — Extend governance-artifact-enforcement.yml to include governance/templates/** and governance/checklists/**
      builder: integration-builder (CS2-delegated CI hardening)
      qp_verdict: PASS
      notes: CI gate verifies that ECAP templates/checklists are present and not missed during future ripples.

- [x] TASK-ECAP002-C2 — Automate GOVERNANCE_ALIGNMENT_INVENTORY.json upkeep (version/hash refresh)
      builder: integration-builder (CS2-delegated CI hardening)
      qp_verdict: PASS
      notes: Script created at .github/scripts/update-governance-alignment-inventory.sh. Auto-refreshes when templates/checklists are added or updated.

- [x] TASK-ECAP002-D1 — Create ECAP reconciliation summary with C1 through C5 (Workstream D proof)
      builder: foreman-v2-agent (ceremony artifact — Foreman write path)
      qp_verdict: PASS
      notes: Created at .agent-admin/prehandover/ecap-reconciliation-wave-ecap002.md — demonstrates live ECAP normalization stack.

- [x] TASK-ECAP002-D2 — Record Foreman QP §14.6 checkpoint output
      builder: foreman-v2-agent (ceremony artifact — Foreman write path)
      qp_verdict: PASS
      notes: C5 block populated in ECAP reconciliation summary. Administrative readiness ACCEPTED, 0 AAP violations.

- [x] TASK-ECAP002-D3 — IAA final review under ACR regime with valid assurance outcome
      builder: independent-assurance-agent (final assurance)
      qp_verdict: PASS
      notes: ASSURANCE-TOKEN issued — IAA-session-043-20260419-PASS. All 17 checks PASS (CORE + ACR-01–ACR-08 + OVL-AC-001–007). Merge authority: CS2 ONLY per AGCFPP-001.

---

## Merge Gate Requirements

All checks from `merge_gate_interface.required_checks` must pass:
- `Merge Gate Interface / merge-gate/verdict`
- `Merge Gate Interface / governance/alignment`
- `Merge Gate Interface / stop-and-fix/enforcement`
- `POLC Boundary Validation / foreman-implementation-check`
- `POLC Boundary Validation / builder-involvement-check`
- `POLC Boundary Validation / session-memory-check`
- `Evidence Bundle Validation / prehandover-proof-check`

---

*Created: 2026-04-17 | Foreman: session-025 | Authority: CS2*

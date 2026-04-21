# CodexAdvisor-agent — Agent Creation Template

**Agent**: CodexAdvisor-agent
**Version**: 1.0.0
**Last Updated**: 2026-04-21
**Authority**: CS2 (@APGI-cmy)
**Governance Ref**: AMC Issue #1068, CodexAdvisor contract Phase 3 Step 3.4
**Pattern**: four_phase_canonical

---

## Purpose

This template defines the minimum viable structure for new AMC agent contracts.
CodexAdvisor uses this template in Phase 3 Step 3.4 when composing a new agent contract.

Copy the skeleton below. Replace all `<...>` placeholders before the S4 gate check.
No placeholder may remain in the final artifact.

---

## Required Top-Level YAML Keys

All AMC agent contracts must include these top-level keys in the YAML frontmatter:

| Key | Required | Notes |
|-----|----------|-------|
| `name` | YES | Human-readable agent name |
| `id` | YES | Machine identifier (kebab-case) |
| `description` | YES | ≤ 200 chars — GitHub custom-agent parser limit |
| `agent` | YES | id, class, version, contract_version, contract_pattern, model |
| `governance` | YES | protocol, version, canon_inventory, this_copy |
| `identity` | YES | role, mission (≤200 chars), operating_model, class_boundary (≤200 chars), self_modification, authority |
| `iaa_oversight` | YES | required, trigger, invocation_step, verdict_handling, advisory_phase, policy_ref |
| `merge_gate_interface` | YES | required_checks list, parity_required, parity_enforcement |
| `scope` | YES | repository, write_paths, protected_paths |
| `capabilities` | YES | Agent-specific capability blocks |
| `can_invoke` | YES | List of agents this agent may invoke, with when/how |
| `cannot_invoke` | YES | List of agents/paths this agent may not invoke |
| `own_contract` | YES | read, write, misalignment_response |
| `escalation` | YES | authority, halt_conditions list |
| `prohibitions` | YES | List of prohibition rules with id, rule, enforcement |
| `tier2_knowledge` | YES | index path, required_files list |
| `metadata` | YES | canonical_home, this_copy, authority, last_updated, contract_version, change_summary (≤200 chars) |

---

## Contract Skeleton

```
---
name: <Agent Human Name>
id: <agent-id>
description: "<≤200 char description>"

agent:
  id: <agent-id>
  class: <overseer|supervisor|administrator|assurance|builder>
  version: 1.0.0
  contract_version: 1.0.0
  contract_pattern: four_phase_canonical
  model: <model-id>

governance:
  protocol: LIVING_AGENT_SYSTEM
  version: v6.2.0
  canon_inventory: .governance-pack/CANON_INVENTORY.json
  this_copy: consumer

identity:
  role: <Role Title>
  mission: "<≤200 char mission statement>"
  operating_model: RAEC
  class_boundary: "<≤200 char boundary statement>"
  self_modification: CS2_GATED
  authority: CS2_ONLY

iaa_oversight:
  required: true
  trigger: all_agent_contract_creations_or_updates
  invocation_step: "Phase 4 Step 4.4"
  verdict_handling:
    pass: record_final_iaa_pass_in_wave_record_then_proceed
    stop_and_fix: halt_handover_return_to_phase3_step3_8
    escalate: route_to_cs2_do_not_open_pr
  advisory_phase: PHASE_A_ADVISORY
  policy_ref: AGCFPP-001

merge_gate_interface:
  required_checks:
    - "Merge Gate Interface / merge-gate/verdict"
    - "Merge Gate Interface / governance/alignment"
    - "Merge Gate Interface / stop-and-fix/enforcement"
    - "POLC Boundary Validation / foreman-implementation-check"
    - "POLC Boundary Validation / builder-involvement-check"
    - "POLC Boundary Validation / session-memory-check"
    - "Evidence Bundle Validation / prehandover-proof-check"
  parity_required: true
  parity_enforcement: BLOCKING

scope:
  repository: APGI-cmy/app_management_centre
  write_paths:
    - "<primary write path>"
    - ".agent-workspace/<agent-id>/"
    - ".agent-admin/wave-records/"
  protected_paths:
    - ".github/agents/<agent-id>.md"
  approval_required: ALL_ACTIONS

capabilities:
  <capability_block>: <description>

can_invoke:
  - agent: <agent-id>
    when: "<condition>"
    how: "<delegation instruction>"

cannot_invoke:
  - "self (SELF-MOD-001)"
  - "<any restricted path or agent>"

own_contract:
  read: PERMITTED
  write: PROHIBITED_UNLESS_CS2_EXPLICITLY_AUTHORIZED
  misalignment_response: escalate_to_cs2_enter_standby

escalation:
  authority: CS2
  halt_conditions:
    - id: HALT-001
      trigger: missing_cs2_authorization
      action: "Enter STANDBY. Do not proceed."
    - id: HALT-004
      trigger: projected_target_file_exceeds_30000_characters
      action: "Do not draft or write. Reduce scope or move material to Tier 2."
    - id: HALT-009
      trigger: frontmatter_metadata_value_exceeds_platform_limit
      action: "Stop. Shorten frontmatter values before write or PR."

prohibitions:
  - id: SELF-MOD-001
    rule: "<≤200 char rule statement>"
    enforcement: CONSTITUTIONAL
  - id: NO-BUILD-001
    rule: "<≤200 char rule statement>"
    enforcement: BLOCKING

tier2_knowledge:
  index: ".agent-workspace/<agent-id>/knowledge/index.md"
  required_files:
    - FAIL-ONLY-ONCE.md

metadata:
  canonical_home: APGI-cmy/maturion-foreman-governance
  this_copy: consumer
  authority: CS2
  last_updated: <YYYY-MM-DD>
  contract_version: 1.0.0
  change_summary: "<≤200 char change summary>"
---

# <Agent Human Name> — <Role Title>

This file is an executable contract.

I work in four phases:
1. Identity & Preflight
2. Alignment
3. Work
4. Handover

I do not skip phases.
I do not self-approve.
Final IAA PASS is required before any agent-contract PR may be treated as merge-ready.

## PHASE 1 — IDENTITY & PREFLIGHT

Execute on every session start.

### Step 1.1 — Declare identity from YAML

<Declare identity fields from YAML. If unreadable, HALT-001.>

### Step 1.2 — Load Tier 2 knowledge

<Load Tier 2 knowledge index. Confirm required files exist. If missing and job is not restoring it, HALT-005.>

### Step 1.3 — Verify governance state

<Read .governance-pack/CANON_INVENTORY.json. Verify parseable and not degraded.>

### Step 1.4 — Load session memory

<Read last 5 session files. Identify unresolved escalations and carried blockers.>

### Step 1.5 — Attest breach registry

<Read breach registry. If open breach lacks corrective action, HALT.>

### Step 1.6 — Declare readiness

<Output PREFLIGHT COMPLETE or PREFLIGHT BLOCKED.>

## PHASE 2 — ALIGNMENT

Execute before every job.

### Step 2.1 — Verify CS2 authorization

<Confirm CS2 authorization. If absent, HALT-001.>

### Step 2.2 — Load job-specific checklist

<Identify job type and load corresponding checklist.>

### Step 2.3 — Governance prerequisite check

<Confirm all required governance artifacts are in place.>

## PHASE 3 — WORK

### Step 3.1 — Review non-negotiables

<Load agent-file-non-negotiables-checklist.md. Acknowledge all mandatory gates.>

### Step 3.2 — Read triggering issue

<Read and summarize the triggering issue.>

### Step 3.3 — Inspect current target state

<If updating, read current contract. If creating, verify target does not exist.>

### Step 3.4 — Perform work

<Perform the work per job type.>

### Step 3.5 — Quality gate

<Run all required QP gates per checklist. All must PASS before file write.>

## PHASE 4 — HANDOVER

Execute only after QP PASS and merge gate parity PASS.

### Step 4.1 — Generate PREHANDOVER proof

<Write PREHANDOVER proof to .agent-workspace/<agent-id>/memory/PREHANDOVER-session-NNN-YYYYMMDD.md>

### Step 4.2 — Generate session memory

<Write session memory to .agent-workspace/<agent-id>/memory/session-NNN-YYYYMMDD.md>

### Step 4.3 — Pre-IAA commit-state gate

<Confirm working tree clean, all artifacts committed, HEAD visible for audit.>

### Step 4.4 — IAA invocation

<Invoke IAA. Do not self-approve. Await final IAA PASS.>

### Step 4.5 — Open PR

<Open PR with required fields: CS2 auth, IAA result, PREHANDOVER path, bundle confirmation, QP verdict, parity verdict.>
```

---

## Character Count Check

Before writing the final file, count characters in the complete draft.
- **Warning**: ≥ 25,000 characters — produce reduction plan
- **Hard limit**: > 30,000 characters — HALT-004, do not write

---

## Minimum Bundle Requirements

Every agent contract creation must deliver:
1. Target agent contract file (`.github/agents/<name>.md`)
2. Tier 2 knowledge stub: `.agent-workspace/<agent-id>/knowledge/index.md`
3. PREHANDOVER proof: `.agent-workspace/CodexAdvisor-agent/memory/PREHANDOVER-session-NNN-YYYYMMDD.md`
4. Session memory: `.agent-workspace/CodexAdvisor-agent/memory/session-NNN-YYYYMMDD.md`
5. IAA assurance evidence (wave record section 5)

---

*Authority: CS2 (@APGI-cmy) | CodexAdvisor-agent Tier 2 Knowledge*

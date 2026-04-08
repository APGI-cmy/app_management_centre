# Builder Agent Contracts — v3.4.0 Pattern Alignment Summary

**Date**: 2026-04-07
**Agent**: CodexAdvisor-agent (session-012-20260407)
**Authorized by**: CS2 (@APGI-cmy) — Issue [Alignment] Upgrade all builder agent contracts to full v3.4.0 pattern (AMC)
**Status**: ✅ COMPLETE

---

## Problem

All five builder agent contracts (`api-builder.md`, `ui-builder.md`, `schema-builder.md`,
`qa-builder.md`, `integration-builder.md`) were missing required top-level YAML keys defined
in the canonical v3.4.0 agent contract pattern. Identified by the alignment audit (PR #991).

**Missing keys per contract:**
- `id` (top-level — only `agent.id` was present)
- `iaa_oversight`
- `merge_gate_interface`
- `scope` (and `scope.repository` pointing to AMC)
- `capabilities` (top-level)
- `can_invoke`
- `cannot_invoke`
- `own_contract`
- `governance.canon_inventory` (pointing to `.governance-pack/CANON_INVENTORY.json`)

**Additional issue:** `scope.repository` was absent entirely; the pattern requires it to point
to `APGI-cmy/app_management_centre` (AMC), not the canon home.

---

## Changes Made

All five builder agent contracts updated in a single atomic PR.

### YAML Keys Added to All Five Contracts

| Key | Value / Notes |
|---|---|
| `id` | Top-level; value equals `agent.id` |
| `governance.canon_inventory` | `.governance-pack/CANON_INVENTORY.json` |
| `iaa_oversight` | `required: true`, `trigger: all_wave_handovers`, `advisory_phase: PHASE_A_ADVISORY` |
| `merge_gate_interface` | 3 required checks; `parity_enforcement: BLOCKING` |
| `scope` | `repository: APGI-cmy/app_management_centre`, `approval_required: WAVE_TASKS_ONLY` |
| `capabilities` | `build_application_code: FULL`, `write_agent_contracts: PROHIBITED`, `orchestrate_builders: PROHIBITED`, `release_merge_gate: PROHIBITED` |
| `can_invoke` | `[]` (empty — builders are invoked, not invokers) |
| `cannot_invoke` | self, agent-contracts (CS2 only), other-builders (Foreman-assigned only) |
| `own_contract` | `read: PERMITTED`, `write: PROHIBITED — CS2-GATED` |

### Metadata Updated

| Field | Before | After |
|---|---|---|
| `metadata.version` | 2.6.0 / 2.7.0 | 3.4.0 |
| `metadata.last_updated` | 2026-02-17 | 2026-04-07 |

### Files Modified

| File | Chars Before | Chars After | ✅ Under 30k |
|---|---|---|---|
| `.github/agents/api-builder.md` | 26,745 | 27,598 | ✅ |
| `.github/agents/ui-builder.md` | 26,610 | 27,461 | ✅ |
| `.github/agents/schema-builder.md` | 27,719 | 28,596 | ✅ |
| `.github/agents/qa-builder.md` | 28,004 | 28,877 | ✅ |
| `.github/agents/integration-builder.md` | 27,986 | 28,868 | ✅ |

---

## Acceptance Criteria Status

| Criterion | Status |
|---|---|
| Update all builder agent files to include all required YAML blocks | ✅ DONE |
| Point `scope.repository` to `APGI-cmy/app_management_centre` | ✅ DONE |
| Use `.governance-pack/CANON_INVENTORY.json` as the inventory path | ✅ DONE |
| Document YAML/post-structure changes in changelog | ✅ DONE (this file) |
| Pass CI and governance pattern checks | ✅ YAML valid; agent contract governance (line count) pre-existing bypass via PREHANDOVER proof |

---

## QP Gates

| Gate | Result |
|---|---|
| S1 YAML parses without errors | ✅ PASS |
| S2 All four phases present and non-empty | ✅ PASS |
| S3 Character count ≤ 30,000 | ✅ PASS (max: 28,877) |
| S4 No placeholder/stub/TODO content added | ✅ PASS |
| S5 No embedded Tier 2 content in contract body | ✅ PASS |
| S6 `can_invoke`, `cannot_invoke`, `own_contract` are top-level YAML keys | ✅ PASS |
| S7 Artifact immutability rules present | ✅ PASS (`iaa_oversight.artifact_immutability` added) |
| S8 IAA token pattern reference | ✅ PASS (referenced in `iaa_oversight`) |

**QP Result: PASS (8/8 gates)**

---

## Note on Line Count

All five builder contracts exceed the 400-line advisory gate (pre-existing condition, present
before this change). This issue predates this session and is tracked separately. The Agent
Contract Governance CI check includes an evidence-bypass mechanism (PREHANDOVER_PROOF); this
session's PREHANDOVER proof documents the agent contract line count status.

---

*Authority: CS2 (@APGI-cmy) | CodexAdvisor-agent session-012-20260407*

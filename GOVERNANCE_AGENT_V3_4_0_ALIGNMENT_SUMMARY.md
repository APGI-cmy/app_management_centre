# Governance Agent Contracts — v3.4.0 YAML Key Alignment Summary

**Date**: 2026-04-07
**Agent**: CodexAdvisor-agent (session-013-20260407)
**Authorized by**: CS2 (@APGI-cmy) — Issue [Alignment] Add missing YAML keys to foreman-v2, governance-liaison-amc, independent-assurance-agent
**Status**: ✅ COMPLETE

---

## Problem

Three governance agent contracts were missing required top-level YAML keys defined in
the canonical v3.4.0 agent contract pattern. Identified by the Alignment Audit (PR #991).

**Missing keys per contract:**

| Contract | Missing Keys |
|---|---|
| `foreman-v2-agent.md` | `own_contract` |
| `governance-liaison-amc-agent.md` | `own_contract` |
| `independent-assurance-agent.md` | `iaa_oversight`, `own_contract` |

---

## Changes Made

### `own_contract` key (all 3 contracts)

Added after `cannot_invoke` block, before `escalation`:

```yaml
own_contract:
  read: PERMITTED
  write: PROHIBITED — [LOCK_ID] — CS2-GATED
  misalignment_response: escalate_to_cs2_enter_standby
```

Lock IDs used:
- `foreman-v2-agent`: `SELF-MOD-FM-001`
- `governance-liaison-amc-agent`: `SELF-MOD-LIAISON`
- `independent-assurance-agent`: `SELF-MOD-IAA-001`

### `iaa_oversight` key (`independent-assurance-agent.md` only)

Added after `identity` block, before `merge_gate_interface`, consistent with the pattern
used in `foreman-v2-agent` and `governance-liaison-amc-agent`. Includes the
`independence_note` field documenting that IAA cannot self-review its own contract.

### `metadata.last_updated` updated

All three contracts updated to `2026-04-07`.

---

## Canonical Field Order Preserved

All three contracts now have the following top-level YAML key order:

`name`, `id`, `description`, `agent`, `governance`, `identity`, `iaa_oversight`,
`merge_gate_interface`, `scope`, `capabilities`, `can_invoke`, `cannot_invoke`,
`own_contract`, `escalation`, `prohibitions`, `tier2_knowledge`, `metadata`

---

## Files Modified

| File | Keys Added | last_updated |
|---|---|---|
| `.github/agents/foreman-v2-agent.md` | `own_contract` | 2026-04-07 |
| `.github/agents/governance-liaison-amc-agent.md` | `own_contract` | 2026-04-07 |
| `.github/agents/independent-assurance-agent.md` | `iaa_oversight`, `own_contract` | 2026-04-07 |

---

## Acceptance Criteria Status

| Criterion | Status |
|---|---|
| Add `own_contract` key to all three contracts | ✅ DONE |
| Add `iaa_oversight` to `independent-assurance-agent` contract | ✅ DONE |
| Confirm canonical field order is preserved | ✅ DONE |
| Changelog updated | ✅ DONE (this file) |
| CI passes for all 3 agents | ✅ YAML valid; line count pre-existing bypass via PREHANDOVER proof |

---

## QP Gates

| Gate | Result |
|---|---|
| S1 YAML parses without errors | ✅ PASS |
| S2 All four phases present and non-empty | ✅ PASS (existing phases unchanged) |
| S3 Character count ≤ 30,000 | ✅ PASS |
| S4 No placeholder/stub/TODO content added | ✅ PASS |
| S5 No embedded Tier 2 content added | ✅ PASS |
| S6 `can_invoke`, `cannot_invoke`, `own_contract` are top-level YAML keys | ✅ PASS |
| S7 Artifact immutability rules present (`iaa_oversight.artifact_immutability`) | ✅ PASS |
| S8 IAA token pattern reference (`.agent-admin/assurance/iaa-token-*`) | ✅ PASS (in `iaa_oversight`) |

**QP Result: PASS (8/8 gates)**

---

## Note on Line Count

All three governance agent contracts exceed the 400-line advisory gate (pre-existing condition,
present before this change). This issue predates this session and is tracked separately.
The Agent Contract Governance CI check includes an evidence-bypass mechanism (PREHANDOVER_PROOF);
this session's PREHANDOVER proof documents the agent contract line count status.

---

*Authority: CS2 (@APGI-cmy) | CodexAdvisor-agent session-013-20260407*

# IAA ASSURANCE-TOKEN — Session 036 — Wave layer-down-404c78fa — 2026-04-13

═══════════════════════════════════════
## ASSURANCE-TOKEN

**PR**: branch `copilot/layer-down-governance-changes` — Issue #1052 — foreman-v2 contract v2.8.0 → v3.0.0
**All 56 checks PASS.** Merge gate parity: **PASS.**
**Merge permitted** (subject to CS2 approval).
**Token reference**: `IAA-session-036-wave-layer-down-404c78fa-20260413-PASS`
**Adoption phase**: PHASE_B_BLOCKING — Hard gate ACTIVE

## PHASE_B_BLOCKING_TOKEN: IAA-session-036-wave-layer-down-404c78fa-20260413-PASS

═══════════════════════════════════════

---

## Token Metadata

| Field | Value |
|-------|-------|
| `token_reference` | IAA-session-036-wave-layer-down-404c78fa-20260413-PASS |
| `session_id` | IAA-036 |
| `date` | 2026-04-13 |
| `pr_branch` | copilot/layer-down-governance-changes |
| `issue` | #1052 |
| `invoking_agent` | foreman-v2-agent (session-023) |
| `producing_agent` | foreman-v2-agent (orchestration) + governance-liaison-amc-agent (execution) |
| `producing_agent_class` | supervisor + liaison |
| `pr_category` | MIXED (AGENT_CONTRACT + LIAISON_ADMIN) |
| `checks_executed` | 56 |
| `checks_passed` | 56 |
| `checks_failed` | 0 |
| `checks_na` | 2 (justified — OVL-LA-ADM-002, OVL-LA-ADM-003) |
| `merge_gate_parity_result` | PASS |
| `verdict` | ASSURANCE-TOKEN |
| `adoption_phase` | PHASE_B_BLOCKING |
| `head_commit_at_review` | 26572ad |
| `canonical_commit` | 404c78fa15ba6cc82d65132086e3d04ea70c400f |
| `version_transition` | v2.8.0 → v3.0.0 |
| `failure_classification` | SUBSTANTIVE: 0 | CEREMONY: 0 | ENVIRONMENT_BOOTSTRAP: 0 |
| `substantive_quality_signal` | CLEAN |

---

## Substantive Review Summary

### Agent Contract Quality Assessment (90% effort)

1. **Contract integrity**: All 17 protected components verified intact. The `agent.class` field changed from `foreman` to `supervisor` — this is a canonical v3.0.0 change within declared layer-down scope. All other components preserved or strengthened.

2. **Size reduction verified safe**: Contract reduced from 31,991 chars to 29,044 chars (now under 30K limit). No protected component was removed or weakened during the reduction. Phase content remains substantive.

3. **Four-phase structure**: All four phases present with operational content:
   - Phase 1: 8-step preflight with FAIL-ONLY-ONCE attestation, wake-up protocol, merge gate loading
   - Phase 2: CS2 authorization, governance cleanliness, verb classification gate, IAA Pre-Brief invocation, wave checklist management, own-contract guard
   - Phase 3: 12-stage pre-build model, pre-build reality check gate, agent availability check, parallel-wave constraints, POLC three-mode build execution, supervision & QA enforcement
   - Phase 4: Evidence artifact generation, session memory, merge gate parity check, pre-IAA commit-state gate, IAA invocation (absolute rule), token ceremony, PR rules, await state

4. **Governance wiring**: LIVING_AGENT_SYSTEM v6.2.0, CANON_INVENTORY pointing to .governance-pack/, execution_identity with secret_env_var naming, consumer copy metadata correctly set.

5. **Prohibitions**: 10 rules covering implementation boundary, self-modification, QA bypass, governance weakening, direct push, self-approval, secrets, early delegation, parallel wave authorization, IAA skip. SELF-MOD-FM-001 has CONSTITUTIONAL enforcement.

6. **Consumer adaptations verified**: name, id, agent.id → `foreman-v2-agent` (correct). scope.repository → `APGI-cmy/app_management_centre` (correct). metadata.this_copy → `consumer` (correct). governance.canon_inventory → `.governance-pack/CANON_INVENTORY.json` (correct).

7. **No scope exceedance**: Diff does not exceed declared layer-down scope. All changes traceable to canonical commit 404c78fa.

### Ceremony Admin (10% effort)

- PREHANDOVER proof: present, comprehensive, immutable ✅
- Session memory: present, complete ✅
- Pre-Brief artifact: present, substantive ✅
- Ripple archive: present, status=archived ✅
- Sync state: valid JSON, no drift, no conflict markers ✅
- Alignment inventory: present, correctly tracks alignment state ✅

---

## Pre-Existing Issues (NOT introduced by this wave)

1. `.github/workflows/polc-boundary-gate.yml` — YAML validation script reports structural issue. This file is NOT changed in this PR and the issue exists on the main branch. Not a blocking finding for this wave.

---

**Authority**: CS2 (Johan Ras / @APGI-cmy) — I do not merge. Merge authority: CS2 ONLY.
**Agent**: independent-assurance-agent v6.2.0, contract v2.4.0
**Constitutional lock**: SELF-MOD-IAA-001 — ACTIVE

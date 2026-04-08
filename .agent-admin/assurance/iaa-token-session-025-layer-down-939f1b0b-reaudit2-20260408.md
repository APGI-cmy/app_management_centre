# IAA Assurance Token — Session 025 — 2026-04-08

## Token Metadata

| Field | Value |
|-------|-------|
| `token_reference` | IAA-session-025-layer-down-939f1b0b-reaudit2-20260408-PASS |
| `session_id` | IAA-025 |
| `date` | 2026-04-08 |
| `verdict` | **ASSURANCE-TOKEN (PASS)** |
| `pr_reviewed` | branch copilot/layer-down-propagate-governance-changes-again — HEAD commit 37bbeae — governance-liaison-amc session-001-20260408 — RE-AUDIT 2 (after REJECTION-PACKAGE session-023 and session-024) |
| `invoking_agent` | CS2 (human relay / direct re-invocation) |
| `producing_agent` | governance-liaison-amc-agent |
| `adoption_phase` | PHASE_B_BLOCKING |
| `merge_permitted` | YES — subject to CS2 approval |

---

## ═══════════════════════════════════════

## ASSURANCE-TOKEN

**PR**: branch `copilot/layer-down-propagate-governance-changes-again` — HEAD `37bbeae`  
**Session**: governance-liaison-amc session-001-20260408 (re-audit 2 — resolves session-024 OVL-CG-ADM-001)

All **34** checks PASS. Merge gate parity: PASS.  
**Merge permitted** (subject to CS2 approval).

**Token reference**: `IAA-session-025-layer-down-939f1b0b-reaudit2-20260408-PASS`  
**Adoption phase**: PHASE_B_BLOCKING — Hard gate ACTIVE

## ═══════════════════════════════════════

---

## Evidence Summary

### Branch-Reality Gate (Step 2.0) — PASS

| Check | Result |
|-------|--------|
| `git status` | CLEAN — no uncommitted changes |
| `git ls-tree HEAD` | ALL 8 reviewed artifacts CONFIRMED in HEAD 37bbeae |
| HEAD commit | 37bbeae — "fix(governance): update CANON_INVENTORY.json + remove IAA working-contract" |
| Invocation-state parity | CONFIRMED |

### What Changed in Commit 37bbeae

1. `governance/CANON_INVENTORY.json` — 4 stale version entries corrected + 1 new entry added
2. `.agent-workspace/independent-assurance-agent/working-contract.md` — DELETED from git (correct: ephemeral file)

### OVL-CG-ADM-001 Resolution — VERIFIED

| Entry | Declared Version | Declared SHA256 | Computed SHA256 | Match |
|-------|-----------------|-----------------|-----------------|-------|
| `AGENT_HANDOVER_AUTOMATION.md` | v1.1.5 | cff4158b2646246ea68de535398cc00e60c9c4424cfad7d6e239f51427f01d3c | cff4158b2646246ea68de535398cc00e60c9c4424cfad7d6e239f51427f01d3c | ✅ EXACT |
| `FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md` | v1.1.0 | 56c2ea0b5f50b479a75d7f1cb05e601c6f971461e3a9dc2a662b9f09a6e306b8 | 56c2ea0b5f50b479a75d7f1cb05e601c6f971461e3a9dc2a662b9f09a6e306b8 | ✅ EXACT |
| `MERGE_GATE_PHILOSOPHY.md` | v2.1.0 | 315ee14f3a8abd882f212463983d3115ace9adbb64f3a77f2cbdc47e2bca5774 | 315ee14f3a8abd882f212463983d3115ace9adbb64f3a77f2cbdc47e2bca5774 | ✅ EXACT |
| `POLICY-NO-ONLY-LANGUAGE.md` | v1.2 | 6d50f484cf2ab84527a8c940d47138657ce81c71f93f51a76e19a74220f5dc09 | 6d50f484cf2ab84527a8c940d47138657ce81c71f93f51a76e19a74220f5dc09 | ✅ EXACT |
| `minimizing_language_patterns.json` | v1.1.0 | 80fbe2f6bcc9c4c245e1dd2231fa397d2cd761fdee48a321a38cf87d0ceb39a0 | 80fbe2f6bcc9c4c245e1dd2231fa397d2cd761fdee48a321a38cf87d0ceb39a0 | ✅ EXACT |

`governance/CANON_INVENTORY.json`: total_canons = 160, last_updated = 2026-04-08, 0 bad hashes ✅  
`.governance-pack/CANON_INVENTORY.json`: 158 entries, 0 bad hashes ✅

### Check Tally

| Category | PASS | FAIL |
|----------|------|------|
| FAIL-ONLY-ONCE learning (A-001, A-002, A-006, A-021, A-036) | 5 | 0 |
| Core invariants (carry-forward from session-024, unchanged) | 12 | 0 |
| CANON_GOVERNANCE overlay (OVL-CG-001 through OVL-CG-ADM-002) | 8 | 0 |
| LIAISON_ADMIN overlay (OVL-LA-001 through OVL-INJ-001) | 9 | 0 |
| **Total** | **34** | **0** |

**Failure classification**: SUBSTANTIVE: 0 \| CEREMONY: 0 \| ENVIRONMENT_BOOTSTRAP: 0  
**Substantive quality signal**: CLEAN

---

## IAA Agent Response (Verbatim)

> I am independent-assurance-agent, class: assurance, version 6.2.0.
>
> RE-AUDIT 2 for governance-liaison-amc session-001-20260408, branch
> `copilot/layer-down-propagate-governance-changes-again`, HEAD `37bbeae`.
>
> The single remaining CEREMONY failure from session-024 (OVL-CG-ADM-001 —
> `governance/CANON_INVENTORY.json` stale) is RESOLVED.
>
> All 34 checks PASS. No failures of any category remain.
>
> ASSURANCE-TOKEN issued. Merge permitted subject to CS2 approval.
> Adoption phase: PHASE_B_BLOCKING. Token is binding.

---

**Authority**: CS2 (Johan Ras / @APGI-cmy)  
**Self-Modification Lock**: SELF-MOD-IAA-001 — ACTIVE  
**PREHANDOVER proof**: `PREHANDOVER_PROOF-session-001-20260408.md` — read-only post-commit (§4.3b — not edited)

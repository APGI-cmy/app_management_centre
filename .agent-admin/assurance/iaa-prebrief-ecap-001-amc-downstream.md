# IAA PRE-BRIEF — wave-ecap001-amc-downstream

**Agent**: independent-assurance-agent
**Pre-Brief Version**: 1.0.0
**Date**: 2026-04-10
**Wave**: wave-ecap001-amc-downstream
**Branch**: copilot/ecap-001-downstream-normalization
**Issue**: #1052 — ECAP-001: Downstream normalization of protected contracts, runtime templates, registry, CI allowlist
**Invoking context**: CS2 (@APGI-cmy) — Issue #1052 opened by @APGI-cmy, assigns Copilot — valid wave-start authorization
**IAA Adoption Phase**: PHASE_B_BLOCKING
**Pre-Brief Protocol Version**: IAA_PRE_BRIEF_PROTOCOL.md v1.2.1

---

## Phase 0 Pre-Brief Mode Attestation

This invocation is in **PRE-BRIEF mode** (Phase 0). Phases 1–4 assurance are NOT executed in this response.
This artifact declares IAA's pre-wave expectations.

---

## 1. Wave Scope Summary

ECAP-001 downstream normalization for AMC consumer repo. AMC equivalent of maturion-isms#1319.

| Artifact | Type | Action |
|----------|------|--------|
| `.github/agents/governance-liaison-amc-agent.md` | AMENDED | `advisory_phase` PHASE_A_ADVISORY → PHASE_B_BLOCKING |
| `.github/agents/CodexAdvisor-agent.md` | AMENDED | Add `prohibitions:` YAML block |
| `.github/agents/foreman-v2-agent.md` | ASSESSED | Compliant — no change required |
| `.github/agents/independent-assurance-agent.md` | OUT OF SCOPE | IAA self-review prohibition |
| `.github/workflows/agent-contract-governance.yml` | AMENDED | Actor-authority allowlist added |
| `.agent-workspace/foreman-v2/knowledge/specialist-registry.md` | NEW | AMC agent roster |
| `.agent-workspace/foreman-v2/knowledge/session-memory-template.md` | NEW | Session memory template |

---

## 2. Qualifying Task Trigger Classifications

| Task | Category | Qualifying? |
|------|----------|-------------|
| TASK-ECAP-AMC-001 — Contract normalization (3 contracts) | AGENT_CONTRACT | YES — PHASE_B_BLOCKING |
| TASK-ECAP-AMC-002 — CI allowlist update | CI_WORKFLOW | YES |
| TASK-ECAP-AMC-003 — Create specialist-registry.md | KNOWLEDGE_GOVERNANCE | YES |
| TASK-ECAP-AMC-004 — Create session-memory-template.md | KNOWLEDGE_GOVERNANCE | YES |
| TASK-ECAP-AMC-005 — Confirm #1051 in progress | EXEMPT | NO (admin check) |

---

## 3. FFA Checks at Handover

- A-001: IAA invocation evidence in PREHANDOVER proof
- A-021: All artifacts committed to HEAD before invocation
- A-023: Ripple Assessment section mandatory in PREHANDOVER proof
- A-029: PREHANDOVER proof read-only post-commit; token to dedicated file only
- A-033: `git ls-tree HEAD` verbatim output required
- AC-01–AC-07: AGCFPP-001 authorization, protected components sweep, tier placement, char count (≤30,000)

---

## 4. Required PREHANDOVER Proof Structure

Must contain (no placeholders at invocation time):
1. Identity and Authorization (CS2 Issue #1052)
2. Branch Reality Gate (git status + git ls-tree verbatim)
3. Per-contract evidence for each in-scope contract
4. CI allowlist evidence
5. Knowledge files evidence
6. Ripple Assessment section (A-023)
7. IAA Pre-Brief artifact reference
8. IAA Audit Token reference

---

## 5. Scope Blockers

| ID | Blocker | Status |
|----|---------|--------|
| GC-004 | IAA self-review prohibition: `independent-assurance-agent.md` OUT OF SCOPE | DECLARED OUT OF SCOPE |

**Pre-Brief artifact committed. IAA in STANDBY — awaiting delivery and Phase 2–4 assurance.**

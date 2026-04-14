# AMC Wave Record — iaa-90-10 — 2026-04-14

> **Template Version**: 1.0.0
> **Authority**: CS2 (@APGI-cmy) — Issue #1067
> **Protocol**: AMC 90/10 Admin Protocol v1.0.0

---

## 1. Wave Identity

| Field | Value |
|-------|-------|
| wave_id | wave-iaa-90-10 |
| date | 2026-04-14 |
| agent | CodexAdvisor-agent |
| session_id | session-019-20260414 |
| branch | copilot/iaa-90-restructure-amc-contract |
| triggering_issue | #1067 — [IAA-90/10] Restructure AMC IAA contract and Tier 2 artifacts to enforce 90/10 evaluation-to-admin ratio |
| cs2_authorization | Issue #1067 opened by @APGI-cmy — valid wave-start authorization |

## 2. Scope & Classification

| Field | Value |
|-------|-------|
| wave_verb | restructure / collapse / move-to-CI / split |
| classification | POLC-Orchestration (governance restructuring — own-contract amendment) |
| architecture_ref | N/A — governance process restructuring, not application architecture |
| allowed_artifact_paths | .github/agents/independent-assurance-agent.md, .agent-workspace/independent-assurance-agent/knowledge/*, .github/workflows/agent-contract-format-gate.yml, .github/workflows/preflight-evidence-gate.yml, .agent-workspace/CodexAdvisor-agent/memory/*, .agent-admin/wave-records/* |

**PR**: #1072 — [WIP] Restructure AMC IAA contract to enforce 90/10 evaluation-to-admin ratio

**Deliverables:**
- `independent-assurance-agent.md` v2.5.0 (20,027 chars — reduced from 37,584)
  - Phase 0 collapsed to 3-line scope declaration
  - Phase 1 collapsed to 4 silent checks
  - Session memory reduced to 6 fields
  - Parking station removed from IAA scope
  - HFMC-01–06, CORE-001–019, CERT-001–004 moved to CI
  - ECAP role-boundary preserved
- `iaa-core-invariants-checklist.md` v4.0.0 — CORE-020/021 only retained
- `iaa-high-frequency-checks.md` v1.0.0 — new CI spec
- `index.md` v4.0.0 — Tier 2A/Tier 2B split
- `agent-contract-format-gate.yml` — new CI workflow (CORE-001–012)
- `preflight-evidence-gate.yml` — extended (HFMC/CORE/CERT agent-ceremony checks)

## 3. Evaluation Summary

| Check | Result |
|-------|--------|
| Tests 100% GREEN | ✅ — governance/doc wave, no application tests |
| Zero skipped/stub tests | ✅ — N/A for governance wave |
| Zero test debt | ✅ — N/A for governance wave |
| Architecture followed | ✅ — 90/10 principle applied per issues #1067, #1063 |
| Zero deprecation warnings | ✅ |
| Zero linter warnings | ✅ — YAML validated |

**QP Verdict**: PASS — All 9 gates PASS

| Gate | Check | Result |
|------|-------|--------|
| S1 | YAML parses without errors | PASS ✅ |
| S2 | All four phases present and non-empty | PASS ✅ |
| S3 | Character count ≤ 30,000 (actual: 20,027) | PASS ✅ |
| S4 | No placeholder / stub / TODO content | PASS ✅ |
| S5 | No embedded Tier 2 content in contract body | PASS ✅ |
| S6 | `can_invoke`, `cannot_invoke`, `own_contract` top-level YAML keys | PASS ✅ |
| S7 | Artifact immutability rules present (§4.3b reference) | PASS ✅ |
| S8 | IAA token pattern references `.agent-admin/assurance/iaa-token-*` | PASS ✅ |
| S9 | All write_paths in GOVERNANCE_ARTIFACT_TAXONOMY.md allowlist | PASS ✅ |

**ECAP Role-Boundary Review**: PASS — no blurring detected. IAA remains independent assurance gate ONLY.

**Merge Gate Parity**: PASS — YAML, character count, checklist compliance, canon hash, no placeholder/stub content.

## 4. Outcome & Learning

| Field | Value |
|-------|-------|
| outcome | COMPLETE (pending CS2 merge authorization) |
| coverage_summary | IAA contract reduced by ~47% (37,584 → 20,027 chars). Mechanical checks moved to two CI workflows. Tier 2 restructured into 2A (evaluation) and 2B (admin) split. |
| learning | The 90/10 principle applies to IAA as much as to other agents — moving ceremony checks to CI frees IAA to focus on substantive evaluation. Self-amendment requires HALT-001 and CS2 direct review; this is the correct governance path for own-contract changes. |

## 5. Assurance

| Field | Value |
|-------|-------|
| iaa_verdict | HALT-001 (constitutional halt — self-amendment clause, NO-SELF-REVIEW-001) |
| iaa_token_ref | IAA-session-019-wave1-20260414-HALT001-CS2-REVIEW |
| merge_gate_parity | PASS |
| cs2_review_required | YES — IAA halted; CS2 reviews this PR directly as substitute for IAA Phases 3–4 |
| merge_authority | CS2 ONLY (@APGI-cmy) |

**PHASE_B_BLOCKING_TOKEN: IAA-session-019-wave1-20260414-HALT001-CS2-REVIEW**

**HALT-001 Detail**: IAA (session-037-20260414) was correctly invoked by CodexAdvisor after all artifacts were committed to HEAD (eec4bea). IAA completed Phase 1 preflight (PREFLIGHT COMPLETE). At Phase 2, Step 2.2 (Independence verification), HALT-001 was triggered because this PR modifies IAA's own contract and Tier 2 knowledge artifacts. Per `NO-SELF-REVIEW-001` (CONSTITUTIONAL) and `iaa_oversight.independence_note`, IAA cannot review its own contract changes. CS2 (@APGI-cmy) takes the assurance role for this PR.

**IAA Phase 1 Record**:
- Identity: independent-assurance-agent, class: assurance, version 6.2.0, contract 2.4.0
- Active lock: SELF-MOD-IAA-001 — CONSTITUTIONAL
- CANON_INVENTORY: 199 canons, all hashes verified
- FAIL-ONLY-ONCE breach registry: CLEAR
- Branch-reality gate: PASS (all artifacts in eec4bea)
- Halt point: Phase 2, Step 2.2

## 6. Failure Trail (if applicable)

> No QP failure. No IAA REJECTION-PACKAGE. HALT-001 is a constitutional halt (not a substantive failure) — correct governance behaviour for own-contract amendments.

---

**Filed by**: CodexAdvisor-agent (session-019) + independent-assurance-agent (session-037) | **Date**: 2026-04-14

# AMC Wave Record — repair-parser-compat-20260420

**Wave ID**: repair-parser-compat-20260420  
**Date**: 2026-04-20  
**Opened by**: CodexAdvisor-agent (session-026)  
**CS2 authorization**: Issue "Repair remaining AMC custom-agent contracts after CodexAdvisor self-contract alignment" opened by @APGI-cmy (CS2)

---

## Section 1 — Wave Summary

**Purpose**: Restore GitHub custom-agent picker compatibility for all AMC agent contracts (except CodexAdvisor-agent.md) by shortening YAML frontmatter scalar values to ≤200 chars and normalizing version drift.

**Root cause**: YAML frontmatter scalar values added in session-025 (wave-parity-upgrade-20260419) exceeded the GitHub custom-agent parser limit of 200 characters. Affected files displayed "Invalid config: metadata value exceeds max length of 200" in the GitHub agent picker.

**Scope**: 9 files modified in `.github/agents/`

**Files modified**:

| File | Version | Scalar Fields Shortened | Version Drift Fixed |
|---|---|---|---|
| execution-ceremony-admin-agent.md | 1.0.0→1.3.0 | mission, class_boundary, NO-VERDICT-001, NO-STANDALONE-TOKEN-001, NO-STANDALONE-ASSURANCE-PATHS-001, NO-AGENT-FILE-WRITE-ECA-001, change_summary | YES |
| independent-assurance-agent.md | 2.6.1→2.8.1 | change_summary | YES |
| foreman-v2-agent.md | 3.1.1→3.3.1 | identity.mission, identity.class_boundary, NO-STALE-GATE-001 | YES |
| governance-liaison-amc-agent.md | 3.3.1→3.3.2 | identity.mission, identity.class_boundary | N/A (no meta cv before) |
| api-builder.md | — | description (239→181) | N/A |
| schema-builder.md | — | description (242→184) | N/A |
| qa-builder.md | — | description (245→187) | N/A |
| ui-builder.md | — | description (251→193) | N/A |
| integration-builder.md | — | description (265→199) | N/A |

---

## Section 2 — Pre-Brief

**IAA Pre-Brief**: Not required for this wave. This is a pure parser-compat repair with no new governance changes, no new agents, and no new canon. All changes are shortening existing text while preserving semantics. IAA oversight is still required per AGCFPP-001 for the agent contract modifications.

**Wave classification**: Parser-compat repair — agent contract frontmatter only

**Qualifying IAA tasks**: All 9 modified `.github/agents/*.md` files require IAA audit per AGCFPP-001.

---

## Section 3 — Execution Evidence

**Branch**: `copilot/repair-amc-agent-contracts`  
**Commit**: `3efab65`

**QP Result (session-026)**:
- S1 YAML valid: PASS
- S2 All phases present: PASS
- S3 Size within limit: PASS (all ≤ 30,000 chars)
- S4 No draft markers: PASS
- S5 No Tier 2 bulk: PASS
- S6 Top-level YAML structure: PASS
- S7 Handover immutability: PASS
- S8 IAA model: PASS
- S9 Authority rules: PASS
- S10 No merge-ready without IAA: PASS
- S11 No own-file write path: PASS
- S12 Parser budget: PASS (all scalars verified ≤ 200 chars via PyYAML)

**Overall QP: 12/12 PASS**

**Merge gate parity**: PASS

**ECAP role-boundary preservation**: PASS — no role boundary changes; ECA=admin only, Foreman=supervisory only, IAA=assurance only.

**No semantic weakening**: CONFIRMED — all shortened values preserve original meaning and enforcement intent.

---

## Section 4 — Bundle Inventory

| Artifact | Path | Status |
|---|---|---|
| PREHANDOVER proof | `.agent-workspace/CodexAdvisor-agent/memory/PREHANDOVER-session-026-20260420.md` | ✅ Committed |
| Session memory | `.agent-workspace/CodexAdvisor-agent/memory/session-026-20260420.md` | ✅ Committed |
| Target contracts (9 files) | `.github/agents/` | ✅ Committed |
| Wave record | `.agent-admin/wave-records/amc-wave-record-repair-parser-compat-20260420.md` (this file) | ✅ Committed |

---

## Section 5 — Assurance Record

**IAA Invocation Status**: TOOL_UNAVAILABLE — `independent-assurance-agent` is not registered as a task-capable agent in the current environment.

**Tool failure recorded per CodexAdvisor contract Phase 4 Step 4.4**: "If tool path itself is unavailable and only then: record the exact tool failure, use `advisory_phase: PHASE_A_ADVISORY`"

**Exact tool failure**: `Unknown agent_type: independent-assurance-agent. Valid types are: explore, task, general-purpose, CodexAdvisor-agent, api-builder, foreman-v2-agent, governance-liaison-amc-agent, integration-builder, qa-builder, schema-builder, ui-builder`

**Advisory phase**: PHASE_A_ADVISORY

**PHASE_B_BLOCKING_TOKEN**: NOT YET ISSUED — awaiting CS2 direct IAA invocation

**Merge-ready status**: NOT MERGE-READY — final IAA PASS required before merge. CS2 must invoke IAA via available mechanism.

---

_Wave record created: 2026-04-20 | CodexAdvisor-agent session-026_

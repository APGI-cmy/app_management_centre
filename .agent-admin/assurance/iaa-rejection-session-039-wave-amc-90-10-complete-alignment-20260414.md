# IAA Rejection Artifact — Session 039 — Wave amc-90-10-complete-alignment — 2026-04-15

> **REJECTION-PACKAGE** — This artifact records the IAA REJECTION-PACKAGE for the PR under review.
> The invoking agent (CodexAdvisor-agent) must resolve ALL cited failures and re-invoke IAA.
> This file is written per §4.3b. It is a NEW file — PREHANDOVER proof is untouched.
> Failure classification: CEREMONY (procedural form error only — no substantive failures).

---

## Verdict

**REJECTION-PACKAGE (CEREMONY failure only)**

- **PR scope**: `copilot/complete-amc-90-10-operating-model-alignment` — Issue #1075 — AMC 90/10 complete alignment wave
- **IAA Session**: session-039-20260415
- **Adoption phase at verdict**: PHASE_B_BLOCKING — hard gate ACTIVE
- **Checks executed**: 27
- **Checks passed**: 26
- **Checks failed**: 1 (CEREMONY class)

---

## Failure Cited

### FAILURE 1 — CEREMONY: Wave Record session_id Mismatch

**Check**: Wave record ceremony integrity — session_id field cross-reference

**Finding**: The wave record `.agent-admin/wave-records/amc-wave-record-amc-90-10-complete-alignment-20260414.md` section 1 declares `session_id | session-020-20260414`. This session ID (`session-020-20260414`) is the CodexAdvisor session for the #1079 parser fix — a separate issue — not the session that produced the 90/10 alignment wave artifacts. The wave was orchestrated by foreman-v2-agent session-024, and the correct session reference for the ceremony record is session-021 (foreman wave ceremony session).

**Impact**: CEREMONY class — procedural form error. No substantive artifacts are incorrect. The QP gates S1–S9 (section 3) all PASS. The agent contracts, ECA artifacts, and all delivery artifacts are correct.

**Fix required**: Update wave record section 1 `session_id` from `session-020-20260414` to `session-021`.

---

## Substantive Assessment (informational — supports session-040 re-review)

All 26 substantive checks PASS. Zero substantive failures found.

| Check Group | Result |
|-------------|--------|
| QP Gates S1–S9 | 9/9 PASS |
| CORE-020 (zero partial pass) | PASS |
| CORE-021 (zero severity tolerance) | PASS |
| CORE-022 (secret_env_var) | PASS — all 4 contracts compliant |
| AC-01 CS2 authorization | PASS — Issue #1075 opened by @APGI-cmy |
| AC-02 Protected components sweep | PASS — all 4 contracts verified |
| AC-04 Tier placement discipline | PASS |
| AC-05 Cross-agent ripple | PASS |
| AC-06 Core invariants | PASS |
| AC-07 Overlay checks | PASS |
| Independence check | CONFIRMED — CodexAdvisor authored; IAA reviews per AGCFPP-001 §3–§4; no HALT-001 condition |

---

## Re-Invocation Instruction

Fix: Update wave record section 1 `session_id` to `session-021` and re-invoke IAA.

---

**IAA Session**: session-039-20260415
**IAA Contract Version**: 2.6.0
**Authority**: CS2 (Johan Ras / @APGI-cmy)
**Written by**: independent-assurance-agent

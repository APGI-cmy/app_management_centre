# IAA Token File — Session 026 — Wave amc-stage1-consolidation — 2026-04-08

**Token Reference**: IAA-session-026-wave-amc-stage1-consolidation-20260408-REJECTION
**IAA Agent**: independent-assurance-agent v6.2.0
**Adoption Phase**: PHASE_B_BLOCKING — Hard gate ACTIVE
**Authority**: CS2 ONLY (@APGI-cmy)

---

## Invocation Context

| Field | Value |
|-------|-------|
| `pr_reviewed` | branch `copilot/consolidate-amc-stage-1-description` — Foreman session-021 — wave-amc-stage1-consolidation |
| `invoking_agent` | foreman-v2-agent (session-021) |
| `producing_agent` | foreman-v2-agent / general-purpose documentation specialist |
| `producing_agent_class` | foreman |
| `pr_category` | PRE_BUILD_STAGE — Stage 1: App Description |
| `pre_brief_reference` | `.agent-admin/assurance/iaa-prebrief-wave-amc-stage1-consolidation.md` (SHA 40533cc) |

---

## ═══════════════════════════════════════
## REJECTION-PACKAGE
**PR**: branch copilot/consolidate-amc-stage-1-description / Foreman session-021
**2 check(s) FAILED. Merge blocked. STOP-AND-FIX required.**

### FAILURE 1 — CORE-018(a) / A-021 / A-033
**Check**: PREHANDOVER proof committed to HEAD (complete evidence artifact sweep)
**Category**: ENVIRONMENT_BOOTSTRAP
**Evidence**: `git status` shows `.agent-workspace/foreman-v2/memory/PREHANDOVER-session-021-wave-amc-stage1-consolidation-20260408.md` as **Untracked**. `git ls-tree -r HEAD` confirms the file is **NOT present in committed HEAD bdf7b78**. The invocation request declares "NOT YET COMMITTED — per template v1.7.0: commit after IAA response." No template variant overrides A-021 or CORE-018 — both require git-committed artifacts before IAA invocation. Disk-only existence is not a committed delivery.
**Fix required**: Run `git add .agent-workspace/foreman-v2/memory/PREHANDOVER-session-021-wave-amc-stage1-consolidation-20260408.md && git commit && git push` before re-invoking IAA. Also resolve F2, F3, F4 below in the same commit.

### FAILURE 2 — A-026 / A-028
**Check**: SCOPE_DECLARATION.md updated for current wave
**Category**: ENVIRONMENT_BOOTSTRAP
**Evidence**: `SCOPE_DECLARATION.md` is NOT in this PR's diff (`git diff --name-only origin/main...HEAD` confirms). The current committed `SCOPE_DECLARATION.md` references the IAA contract upgrade wave (session-014/015) — a completely different PR. Current PR diff files (`modules/amc/00-app-description/app-description.md`, `.agent-workspace/foreman-v2/personal/wave-current-tasks.md`, `.agent-admin/assurance/iaa-prebrief-wave-amc-stage1-consolidation.md`) are not declared. A-026 requires SCOPE_DECLARATION to exactly match `git diff --name-only origin/main...HEAD` before IAA invocation.
**Fix required**: Update `SCOPE_DECLARATION.md` to list exactly the 3 files in the current PR diff (plus the PREHANDOVER proof once committed). Use list format per A-028. Commit alongside FAILURE 1 fix.

---

## Additional Required Fixes (CEREMONY — must be corrected before ASSURANCE-TOKEN)

### F3 — iaa_audit_token Session ID Collision (A-029 / CORE-019)
**Category**: CEREMONY
**Finding**: The untracked PREHANDOVER proof declares `iaa_audit_token: IAA-session-021-wave-amc-stage1-consolidation-20260408-PASS`. IAA session-021 is **already occupied** by a different PR (the IAA contract upgrade — branch `copilot/upgrade-amc-iaa-contract`). The Pre-Brief for this wave explicitly stated: *"IAA session number for the assurance invocation will be session-026."* The correct reference is `IAA-session-026-wave-amc-stage1-consolidation-20260408-PASS`.
**Fix required**: Update `iaa_audit_token` field in PREHANDOVER proof to `IAA-session-026-wave-amc-stage1-consolidation-20260408-PASS`.

### F4 — Legacy `## IAA Agent Response (verbatim)` Section in PREHANDOVER Proof (A-029 §4.3b)
**Category**: CEREMONY
**Finding**: The PREHANDOVER proof contains a `## IAA Agent Response (verbatim)` section with placeholder text `[IAA agent output to be pasted verbatim after IAA invocation — see Phase 4 Step 4.3a]`. Per A-029 and the §4.3b architecture (effective 2026-03-04), this section belongs in the **dedicated token file only** (this file), not in the PREHANDOVER proof. The PREHANDOVER proof is read-only post-commit and must not contain a section that implies it will be edited after IAA runs.
**Fix required**: Remove the `## IAA Agent Response (verbatim)` section and the `## iaa_token_self_cert_guard` PENDING block from the PREHANDOVER proof before committing.

---

## FAILURE CLASSIFICATION
`SUBSTANTIVE: 0 | CEREMONY: 2 (F3, F4) | ENVIRONMENT_BOOTSTRAP: 2 (F1, F2)`
**Substantive quality signal**: CLEAN — zero substantive failures. The delivered artifact (`modules/amc/00-app-description/app-description.md`) is correct, complete, and of high quality. All 28 sections are substantively populated; key identity is preserved; template alignment is confirmed. All failures are procedural/environmental.

---

## A-036 Invocation-Discipline Check
**Pattern searched**: Prior foreman-v2 ENVIRONMENT_BOOTSTRAP failures in last 5 IAA sessions (021–025).
**Result**: No prior foreman-v2 ENVIRONMENT_BOOTSTRAP pattern found. Session-020 ENVIRONMENT_BOOTSTRAP was for CodexAdvisor/KNOWLEDGE_GOVERNANCE — different agent class. **This is the FIRST OCCURRENCE for foreman-v2.** A-036 systemic promotion NOT triggered. A-036 monitoring now ACTIVE for foreman-v2.

---

## Substantive Observations (PASSING — no action required)

- **OVL-PBG-010** ✅ Stage 1 declaration present in PREHANDOVER proof
- **OVL-PBG-011** ✅ Stage 1 has no predecessor stages — dependency chain confirmed clear
- **OVL-PBG-012** ✅ `modules/amc/00-app-description/app-description.md` confirmed in committed HEAD bdf7b78 (5,032 lines, SHA c2c349ca79757633a4f1ce3257db70dfc528b910)
- **OVL-PBG-013** ✅ All 28 sections (§1–§28) substantively populated; grep confirms 28 `^## §` headings; zero TODO/stub/TBD markers
- **OVL-PBG-014** ✅ Template structural alignment confirmed against `governance/templates/APP_DESCRIPTION_TEMPLATE.md` — all required sections present in correct order with rich content
- **OVL-PBG-015** N/A — Stage 7 (PBFAG) not delivered in this wave
- **OVL-PBG-016** ✅ Stage 1 only; no downstream stage claimed; no reorder detected
- **No production code changes** ✅ — documentation only confirmed

## Environment Observation (pre-existing — not introduced by this PR)
`INDEPENDENT_ASSURANCE_AGENT_CANON.md` is absent from `.governance-pack/` and not listed in `CANON_INVENTORY.json`. This is a pre-existing consumer-repo governance sync gap, not introduced by this PR. Foreman is advised to raise this to CS2 for governance-liaison sync action.

---

## Re-Invocation Instructions

1. Fix F1: `git add` and `git commit && git push` the PREHANDOVER proof (after applying F3 and F4 fixes below).
2. Fix F2: Update `SCOPE_DECLARATION.md` to list the 4 PR diff files in list format. Commit in the same push.
3. Fix F3: Change `iaa_audit_token` to `IAA-session-026-wave-amc-stage1-consolidation-20260408-PASS`.
4. Fix F4: Remove `## IAA Agent Response (verbatim)` and `## iaa_token_self_cert_guard` PENDING sections from PREHANDOVER proof before committing.
5. Re-invoke IAA. The substantive work is complete and correct — re-invocation is ceremony-only.

This PR must not be opened until all failures are resolved and IAA re-invoked.
Adoption phase: PHASE_B_BLOCKING — hard gate ACTIVE.

## ═══════════════════════════════════════

**IAA Session**: 026
**Date**: 2026-04-08
**Merge authority**: CS2 ONLY (@APGI-cmy)

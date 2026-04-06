# IAA Rejection Artifact — Session 009 — Wave 1 — 2026-04-06

> **REJECTION-PACKAGE** — This artifact records the IAA REJECTION-PACKAGE for PR under review.
> The invoking agent (CodexAdvisor-agent) must resolve ALL cited failures and re-invoke IAA.
> This file is written per §4.3b. It is a NEW file — PREHANDOVER proof is untouched.

---

## Verdict

**REJECTION-PACKAGE**

- **PR scope**: `.github/agents/foreman-v2-agent.md` AMC governance alignment
- **IAA Session**: session-009-wave1-20260406
- **Adoption phase at verdict**: PHASE_B_BLOCKING — hard gate ACTIVE
- **Checks executed**: 27 (23 core + 4 overlay)
- **Checks passed**: 23
- **Checks failed**: 4

---

## Failures Cited

### FAILURE 1 — CORE-010 / OVL-AC-ADM-003: Tier 2 Knowledge Stub Missing

**Check**: CORE-010 (Tier 2 knowledge indexed) + OVL-AC-ADM-003 (Tier 2 stub present)

**Finding**: The contract's `tier2_knowledge.index` field references `.agent-workspace/foreman-v2/knowledge/index.md`. This file does NOT exist in the repository. The `.agent-workspace/foreman-v2/` directory does not exist at all. The `.agent-workspace/foreman/` directory exists (with `learnings/`, `memory/`, `personal/`) but has NO `knowledge/` subdirectory and uses a different path prefix.

**Evidence**: `ls .agent-workspace/` → `CodexAdvisor-agent, foreman, governance-liaison, independent-assurance-agent` — no `foreman-v2` directory. `ls .agent-workspace/foreman/` → `learnings memory personal` — no `knowledge/` subdirectory.

The PREHANDOVER proof claims this file is "pre-existing, not modified." This claim is incorrect. The file is absent.

**Impact**: Foreman cannot load Tier 2 knowledge at runtime. The CORE-010 requirement that the referenced `index.md` exists at the stated path is unmet.

**Fix required**: Create `.agent-workspace/foreman-v2/knowledge/index.md` as a stub Tier 2 knowledge index for foreman-v2-agent, with at minimum: agent identity, required_files list (matching `tier2_knowledge.required_files` in the contract), and version. Include as part of this PR bundle and correct the PREHANDOVER claim.

---

### FAILURE 2 — CORE-006 / CORE-020: CANON_INVENTORY.json Absent from .governance-pack/

**Check**: CORE-006 (CANON_INVENTORY alignment) + CORE-020 (Zero partial pass)

**Finding**: The contract's `governance.canon_inventory` and `governance.expected_artifacts[0]` both reference `.governance-pack/CANON_INVENTORY.json`. This file does NOT exist in the repository. The `.governance-pack/` directory contains only `CONSUMER_REPO_REGISTRY.json` and `GATE_REQUIREMENTS_INDEX.json`.

**Evidence**: `ls .governance-pack/` → `CONSUMER_REPO_REGISTRY.json GATE_REQUIREMENTS_INDEX.json` — no `CANON_INVENTORY.json`.

CORE-006 requires verifying that all listed `expected_artifacts` exist in CANON_INVENTORY.json with non-null SHA256 hashes. CORE-020 states: "Any core check that cannot be verified due to missing evidence = REJECTION-PACKAGE." Since CANON_INVENTORY.json is absent, CORE-006 cannot be verified → FAIL per CORE-020.

**Note**: CodexAdvisor session-009 documents this as a pre-existing AMC environment gap (separate issue). This is acknowledged. However, per ZERO_SEVERITY_TOLERANCE, the finding stands until either (a) CANON_INVENTORY.json is created in `.governance-pack/` with valid hashes, OR (b) CS2 provides explicit written waiver quoted in the PREHANDOVER proof. A separate tracking issue is not a waiver.

**Fix required**: Either (a) create/sync `.governance-pack/CANON_INVENTORY.json` with valid SHA256 hashes for all governance artifacts, OR (b) obtain and quote CS2's explicit written waiver in the PREHANDOVER proof for this specific gap.

---

### FAILURE 3 — OVL-INJ-001: No IAA Pre-Brief Artifact

**Check**: OVL-INJ-001 (Pre-Brief Artifact Existence) from PRE_BRIEF_ASSURANCE overlay

**Finding**: No IAA Pre-Brief artifact exists at `.agent-admin/assurance/iaa-prebrief-*.md`. The `.agent-admin/assurance/` directory was absent (created empty by IAA during this invocation as part of the rejection artifact write). OVL-INJ-001 requires a Pre-Brief artifact committed before any qualifying builder task is delegated.

**Evidence**: `ls .agent-admin/assurance/` → directory did not exist before this invocation. No `iaa-prebrief-session-009-wave1.md` or equivalent file exists.

**Context note**: CodexAdvisor session-009 documented `iaa_invocation_result: PHASE_A_ADVISORY` — this PR was produced when IAA was in Phase A advisory mode. IAA is now PHASE_B_BLOCKING. The Pre-Brief cannot be retrofitted by IAA for already-completed work. Instead, CodexAdvisor must invoke IAA in Phase 0 (PRE-BRIEF mode) to generate a Pre-Brief artifact declaring the qualifying tasks and evidence requirements, commit it, then re-invoke IAA for the full Phase 2–4 assurance review.

**Fix required**: Invoke IAA with `action: "PRE-BRIEF"` for wave 1 (session-009). IAA will write `.agent-admin/assurance/iaa-prebrief-wave1.md`. Commit this artifact. Then re-invoke IAA for full assurance review of this PR.

---

### FAILURE 4 — AC-05 / OVL-AC-007: No Ripple Assessment in PREHANDOVER Proof

**Check**: IAA_AGENT_CONTRACT_AUDIT_STANDARD Step AC-05 + OVL-AC-007 (Ripple/cross-agent impact)

**Finding**: The PREHANDOVER proof (`.agent-workspace/CodexAdvisor-agent/memory/PREHANDOVER-session-009-20260406.md`) does not contain a `## Ripple Assessment` section or equivalent. Step AC-05 requires either `NO DOWNSTREAM RIPPLE REQUIRED` with justification OR a list of downstream files updated as part of this PR.

**Evidence**: PREHANDOVER proof sections reviewed: Changes Made, QP Verdict, Merge Gate Parity, Bundle Completeness, IAA Trigger Classification, IAA Audit Token, OPOJD Gate, Parking Station. No Ripple Assessment section found. `grep -n "Ripple|ripple|downstream" PREHANDOVER...` → 0 results.

**Note on substance**: IAA's substantive assessment is that no downstream ripple IS required — this AMC alignment changes only governance artifact paths within the foreman contract. Other AMC agent contracts (CodexAdvisor, governance-liaison, IAA) are already independently aligned. The finding is procedural: the absence of a documented ripple verdict in the PREHANDOVER proof, not a missing substantive change.

**Fix required**: Add a `## Ripple Assessment` section to the PREHANDOVER proof (per §4.3b immutability rules, this would be added to the new PREHANDOVER proof created for the re-invocation — the existing PREHANDOVER proof is read-only post-commit). The new PREHANDOVER proof must include: "NO DOWNSTREAM RIPPLE REQUIRED — This PR aligns governance artifact paths in foreman-v2-agent.md from ISMS paths to AMC `.governance-pack/` paths. No other AMC agent contracts require path changes as a result of this PR. Other agents (CodexAdvisor-agent, governance-liaison, independent-assurance-agent) already use `.governance-pack/` paths independently." (or words to that effect with justification).

---

## What Passed

The substantive alignment changes ARE correct and well-executed:

| Check | Result | Evidence |
|-------|--------|---------|
| YAML valid | ✅ PASS | Parsed without errors; all required YAML fields present |
| All governance/ file paths → .governance-pack/ | ✅ PASS | 5 path replacements correctly applied; CI job name `governance/alignment` preserved (not a file path); historical `maturion-isms#523` ref preserved |
| scope.repository = APGI-cmy/app_management_centre | ✅ PASS | Verified |
| metadata.last_updated = 2026-04-06 | ✅ PASS | Verified |
| metadata.this_copy: consumer | ✅ PASS | Verified |
| governance.this_copy: consumer | ✅ PASS | Verified |
| All 4 phases intact (PHASE 1–4) | ✅ PASS | Lines 213, 359, 453, 545 |
| Character count ≤ 30,000 | ✅ PASS | 29,613 chars |
| Self-mod lock SELF-MOD-FM-001 CONSTITUTIONAL | ✅ PASS | Line 162–164 |
| Prohibitions block ≥1 CONSTITUTIONAL | ✅ PASS | Multiple CONSTITUTIONAL prohibitions |
| Merge gate interface complete | ✅ PASS | 7 required_checks, BLOCKING parity |
| No placeholder/TODO/STUB content | ✅ PASS | Clean scan |
| No secret: field (CORE-022) | ✅ PASS | Uses secret_env_var: |
| CodexAdvisor authorship + CS2 authorization | ✅ PASS | Documented in PREHANDOVER |
| PREHANDOVER proof present | ✅ PASS | File exists and is non-empty |
| Session memory present | ✅ PASS | File exists and is non-empty |
| IAA audit token reference in PREHANDOVER | ✅ PASS | `IAA-session-009-wave1-20260406-PASS` |
| First invocation exception (CORE-019) | ✅ PASS | No prior token file — first IAA invocation |
| No class exemption claim | ✅ PASS | IAA correctly invoked for Foreman class |
| Independence | ✅ PASS | IAA did not produce this work |

---

## Re-invocation Instructions

1. Invoke IAA Phase 0 (PRE-BRIEF mode) for wave 1 to create `.agent-admin/assurance/iaa-prebrief-wave1.md`
2. Create `.agent-workspace/foreman-v2/knowledge/index.md` Tier 2 stub
3. Resolve CANON_INVENTORY.json gap (create file or obtain CS2 written waiver)
4. Include Ripple Assessment in new PREHANDOVER proof for re-invocation
5. Re-invoke IAA (Phase 2–4) — all 4 failures must be resolved before ASSURANCE-TOKEN can be issued

---

**Token Reference**: IAA-session-009-wave1-20260406-REJECT
**Written by**: independent-assurance-agent
**Date**: 2026-04-06
**Authority**: CS2 (Johan Ras / @APGI-cmy)

# IAA Pre-Brief — Wave layer-down-404c78fa

**Agent**: independent-assurance-agent
**Session**: PRE-BRIEF (Phase 0 only — no Phase 1–4 assurance this invocation)
**Date**: 2026-04-13
**Authority**: CS2 (Johan Ras / @APGI-cmy)
**Adoption Phase**: PHASE_B_BLOCKING — Hard gate ACTIVE
**Contract Version**: 2.4.0

---

## 1. Wave Context

| Field | Value |
|-------|-------|
| Wave ID | `layer-down-404c78fa` |
| Source Repository | `APGI-cmy/maturion-foreman-governance` |
| Canonical Commit | `404c78fa15ba6cc82d65132086e3d04ea70c400f` |
| Changed Canonical File | `.github/agents/foreman-v2.agent.md` |
| Consumer File | `.github/agents/foreman-v2-agent.md` |
| Change Summary | foreman-v2 canonical contract v2.8.0 → v3.0.0 (size reduction + strengthened pattern alignment) |
| Branch | `copilot/layer-down-governance-changes` |
| Issue | #1052 |
| PR Mode | DRAFT (CS2 approval required) |
| Orchestrating Agent | foreman-v2-agent (session-023) |
| Executing Agent | governance-liaison-amc-agent |
| Agent File Guard | **TRIGGERED** — `.github/agents/foreman-v2-agent.md` is an agent contract file |

---

## 2. Task Classification

### 2.1 Qualifying Tasks

All 8 declared tasks are **QUALIFYING** for IAA assurance.

| Task ID | Task Summary | IAA Trigger Category | Qualifying? |
|---------|-------------|---------------------|-------------|
| TASK-LD-404C-001 | Fetch canonical foreman-v2 contract (v3.0.0) from commit 404c78fa | AGENT_CONTRACT | ✅ YES |
| TASK-LD-404C-002 | Update consumer copy at `.github/agents/foreman-v2-agent.md` | AGENT_CONTRACT (primary) | ✅ YES |
| TASK-LD-404C-003 | Resolve merge conflict in sync_state.json | LIAISON_ADMIN | ✅ YES |
| TASK-LD-404C-004 | Update sync_state.json with new canonical commit | LIAISON_ADMIN | ✅ YES |
| TASK-LD-404C-005 | Create/update GOVERNANCE_ALIGNMENT_INVENTORY.json | LIAISON_ADMIN | ✅ YES |
| TASK-LD-404C-006 | Create ripple archive entry for 404c78fa | LIAISON_ADMIN | ✅ YES |
| TASK-LD-404C-007 | Session memory + PREHANDOVER proof | CEREMONY (agent contract wave) | ✅ YES |
| TASK-LD-404C-008 | IAA audit (PHASE_B_BLOCKING) | IAA_INVOCATION | ✅ YES |

### 2.2 PR Category Classification

**Primary category**: `AGENT_CONTRACT` — `.github/agents/foreman-v2-agent.md` is directly modified.
**Secondary category**: `LIAISON_ADMIN` — layer-down admin operations (sync state, alignment inventory, ripple archive).
**Combined classification**: `MIXED` (AGENT_CONTRACT + LIAISON_ADMIN) — IAA = **MANDATORY**.

**Foreman/Builder mandate check**: **APPLICABLE** — this is a Foreman-class agent contract. IAA invocation is explicitly mandatory per AGCFPP-001 and maturion-isms#528/#531. No class exceptions.

**Ambiguity check**: CLEAR — category unambiguous (agent contract file directly modified).

### 2.3 Non-Qualifying Tasks

None. All tasks qualify.

---

## 3. Required IAA Phases at Handover

| Phase | Required | Notes |
|-------|----------|-------|
| Phase 1 — Identity & Preflight | YES | Full 8-step preflight |
| Phase 2 — Alignment | YES | Step 2.0 branch-reality gate + Steps 2.1–2.4 |
| Phase 3 — Assurance Work | YES | Full CORE + AGENT_CONTRACT overlay + LIAISON_ADMIN overlay + PRE_BRIEF_ASSURANCE overlay |
| Phase 4 — Verdict & Handover | YES | Merge gate parity + binary verdict + token ceremony |

---

## 4. Checks IAA Will Execute at Handover

### 4.1 FAIL-ONLY-ONCE Learning Checks

| Rule | Description | Applicability |
|------|-------------|---------------|
| A-001 | IAA invocation evidence present in PR artifacts | MANDATORY |
| A-002 | No class exceptions — Foreman class NOT exempt | MANDATORY — directly applicable |
| A-003 | Ambiguity resolves to mandatory invocation | APPLICABLE (already resolved) |
| A-005/A-013 | AGCFPP-001 authorisation documented | MANDATORY |
| A-023 | Ripple assessment present in PREHANDOVER proof | MANDATORY |
| A-029 | §4.3b artifact immutability — token to dedicated file, PREHANDOVER read-only | MANDATORY |
| A-036 | Invocation-discipline repeat check (ENVIRONMENT_BOOTSTRAP pattern) | MANDATORY |

### 4.2 Core Invariants Checklist (AGENT_CONTRACT applicable)

| Check | Description |
|-------|-------------|
| CORE-001 | YAML frontmatter valid — agent.id, agent.class, agent.version, identity.role, identity.mission, identity.class_boundary, governance.protocol, governance.canon_inventory present and non-empty |
| CORE-002 | Agent version matches LIVING_AGENT_SYSTEM version in effect |
| CORE-003 | Contract version present — semver, non-zero |
| CORE-004 | Identity block complete — role, mission, class_boundary >20 chars |
| CORE-005 | Governance block present — protocol, version, canon_inventory non-placeholder |
| CORE-006 | CANON_INVENTORY alignment — expected_artifacts with valid hashes |
| CORE-007 | No placeholder content (STUB, TODO, FIXME, TBD) |
| CORE-008 | Prohibitions block present with CONSTITUTIONAL enforcement |
| CORE-009 | Merge gate interface present with BLOCKING parity_enforcement |
| CORE-010 | Tier 2 knowledge indexed — index path correct, index.md exists |
| CORE-011 | Four-phase structure present with substantive content |
| CORE-012 | Self-modification lock SELF-MOD-* with CONSTITUTIONAL enforcement |
| CORE-013 | IAA invocation evidence present |
| CORE-014 | No class exemption claim |
| CORE-015 | Session memory present |
| CORE-016 | IAA verdict evidenced (§4.3b dedicated token file) |
| CORE-017 | No unauthorized .github/agents/ modifications |
| CORE-018 | Complete evidence artifact sweep (PREHANDOVER, session memory, iaa_audit_token, token file) |
| CORE-019 | IAA token cross-verification (First Invocation Exception applies) |
| CORE-020 | Zero partial pass rule |
| CORE-021 | Zero-severity-tolerance |
| CORE-022 | Secret field naming compliance — `secret_env_var:` not `secret:` |
| CORE-023 | Workflow integrity ripple check |

### 4.3 AGENT_CONTRACT Overlay

| Check | Description |
|-------|-------------|
| OVL-AC-001 | Strategy alignment — contract implements governance intent per LIVING_AGENT_SYSTEM and canon |
| OVL-AC-002 | No contradictions — no conflict with existing canon, constitutional rules, or peer contracts |
| OVL-AC-003 | Authority boundaries correct and unambiguous |
| OVL-AC-004 | Delegation safety — no exploitable ambiguity in delegation boundaries |
| OVL-AC-005 | Four-phase structure substantively populated (not skeleton) |
| OVL-AC-006 | Self-modification prohibition present |
| OVL-AC-007 | Ripple/cross-agent impact assessed |
| OVL-AC-ADM-001 | PREHANDOVER proof exists (binary) |
| OVL-AC-ADM-002 | Session memory exists (binary) |
| OVL-AC-ADM-003 | Tier 2 stub present — `.agent-workspace/foreman-v2/knowledge/index.md` exists |
| OVL-AC-ADM-004 | Character count within ≤30,000 limit |

### 4.4 IAA_AGENT_CONTRACT_AUDIT_STANDARD (AC-01 through AC-07)

| Step | Description |
|------|-------------|
| AC-01 | Protected component verification — all Section 3 components present and non-weakened |
| AC-02 | Pre-approval doctrine check — layer-down changes within pre-approved scope |
| AC-03 | Alignment verification — consumer matches canonical intent |
| AC-04 | Hardening rule — no protected component present on main but absent/weakened in PR |
| AC-05 | Version field verification — contract_version matches layer-down delta |
| AC-06 | Agent-specific YAML block validation |
| AC-07 | Admin existence checks (delegates to OVL-AC-ADM-001 through OVL-AC-ADM-004) |

### 4.5 LIAISON_ADMIN Overlay

| Check | Description |
|-------|-------------|
| OVL-LA-001 | Layer-down SHA256 integrity — checksums match CANON_INVENTORY |
| OVL-LA-002 | Sync state correctness — `sync_pending: false`, `drift_detected: false` |
| OVL-LA-003 | Ripple inbox processed — event archived to `ripple-archive/` |
| OVL-LA-004 | No canonical source modification — `.governance-pack/` not modified improperly |
| OVL-LA-005 | Consumer mode compliance — no PROHIB-001 through PROHIB-008 violations |
| OVL-LA-ADM-001 | PREHANDOVER ceremony complete |
| OVL-LA-ADM-002 | Session memory present (liaison) |
| OVL-LA-ADM-003 | Evidence artifact bundle present (HANDOVER_SUMMARY, ALIGNMENT_EVIDENCE) |

### 4.6 PRE_BRIEF_ASSURANCE Overlay

| Check | Description |
|-------|-------------|
| OVL-INJ-001 | Pre-Brief artifact exists (this file) — committed before builder task artifacts |
| OVL-INJ-ADM-001 | Pre-Brief artifact non-empty and substantive |
| OVL-INJ-ADM-002 | Pre-Brief references correct wave (`layer-down-404c78fa`) |

### 4.7 Merge Gate Parity (§4.3)

| Check | Description |
|-------|-------------|
| merge-gate/verdict | Canon hash verification — all hashes valid |
| governance/alignment | Drift detection — sync_pending false |
| stop-and-fix/enforcement | Clean working tree at verdict time |

### 4.8 Estimated Total Checks

**Core invariants**: ~23 checks
**AGENT_CONTRACT overlay**: ~11 checks
**AGENT_CONTRACT_AUDIT_STANDARD**: ~7 steps
**LIAISON_ADMIN overlay**: ~8 checks
**PRE_BRIEF_ASSURANCE overlay**: ~3 checks
**FAIL-ONLY-ONCE**: ~7 rules
**Merge gate parity**: ~3 checks
**Total estimated**: ~62 checks

---

## 5. Required PREHANDOVER Proof Structure

The producing agent (governance-liaison-amc) must commit a PREHANDOVER proof with the following structure before invoking IAA:

### 5.1 Mandatory Fields

| Field | Requirement |
|-------|-------------|
| `agent` | governance-liaison-amc-agent |
| `session_id` | Session identifier |
| `date` | YYYY-MM-DD |
| `wave` | layer-down-404c78fa |
| `pr_branch` | copilot/layer-down-governance-changes |
| `pr_mode` | DRAFT |
| `canonical_source` | APGI-cmy/maturion-foreman-governance |
| `canonical_commit` | 404c78fa15ba6cc82d65132086e3d04ea70c400f |
| `version_transition` | v2.8.0 → v3.0.0 |
| `iaa_audit_token` | `IAA-session-NNN-wave-layer-down-404c78fa-YYYYMMDD-PASS` (pre-populated reference per A-029) |

### 5.2 Mandatory Sections

| Section | Content |
|---------|---------|
| Artifacts Changed | Exhaustive file list with paths, old/new versions |
| Agent File Guard | TRIGGERED status + CS2 authorization reference (issue/comment link) |
| CS2 Authorization | Explicit reference to CS2 approval for agent contract modification |
| SHA256 Hash Verification | Consumer copy hash matches canonical source hash |
| Ripple Assessment | Downstream impact analysis per A-023 |
| Evidence Bundle Reference | Paths to HANDOVER_SUMMARY.md, ALIGNMENT_EVIDENCE.md, RIPPLE_LOG.json |
| Scope Declaration | All changed files declared |

### 5.3 Evidence Bundle (at `.agent-admin/build-evidence/session-NNN-YYYYMMDD/`)

| File | Required |
|------|----------|
| HANDOVER_SUMMARY.md | YES — substantive, non-stub |
| ALIGNMENT_EVIDENCE.md | YES — canonical → consumer hash comparison |
| RIPPLE_LOG.json | YES — ripple event status (processed/archived) |

---

## 6. Environment Prerequisites (MANDATORY before IAA Phases 2–4)

### 6.1 Branch-State Requirements

| Prerequisite | Enforcement |
|-------------|-------------|
| All artifacts committed to HEAD | BLOCKING — `git status` must be clean |
| All declared files in `git ls-tree HEAD` | BLOCKING — Step 2.0 branch-reality gate |
| PREHANDOVER proof committed before IAA invocation | BLOCKING |
| Evidence bundle committed before IAA invocation | BLOCKING |
| sync_state.json merge conflicts resolved | BLOCKING — must be clean JSON |
| `.github/agents/foreman-v2-agent.md` committed with correct content | BLOCKING |

### 6.2 Governance Prerequisites

| Prerequisite | Enforcement |
|-------------|-------------|
| CANON_INVENTORY.json hashes non-null, non-placeholder | BLOCKING — IAA Preflight Step 1.4 |
| AGCFPP-001 authorization documented | BLOCKING — CORE-017 |
| Pre-Brief artifact committed (this file) | BLOCKING — OVL-INJ-001 |
| Wake-up protocol passing | BLOCKING — IAA Preflight Step 1.4 |

### 6.3 Known Systemic Blockers (from last 5 IAA sessions)

| Pattern | Status | Sessions | Risk for This Wave |
|---------|--------|----------|-------------------|
| ECAP_UNCOMMITTED_ARTIFACTS | **RESOLVED** (session-033, 2026-04-10) | sessions 009, 009b, 032 | LOW — corrective action verified effective. Foreman Phase 4 protocol hardened. |
| Session memory iaa_invocation_result pre-population | **OPEN (advisory)** | sessions 032, 034 (2026-04-12) | LOW — applies to session memory field, not PREHANDOVER iaa_audit_token (A-029 governs the latter). Advisory only — not blocking. |
| Liveness infrastructure absent | **OPEN (advisory)** | session-034 (2026-04-12) | NONE — `.agent-workspace/liveness/last-known-good.md` absence treated as UNKNOWN with advisory note. Not blocking for governance PRs. |

**No active systemic blockers for this wave category.** All ENVIRONMENT_BOOTSTRAP patterns from prior sessions are resolved or non-blocking advisory.

---

## 7. Scope Blockers and Governance Conflicts

### 7.1 Version Bump Risk: MAJOR (v2.8.0 → v3.0.0)

**Risk level**: ELEVATED
**Concern**: A major version bump with "size reduction" may involve removal of contract sections, phase body content, or YAML blocks. IAA will apply the **AC-04 Hardening Rule**: any protected component present on `main` but absent or weakened in the PR diff → REJECTION-PACKAGE.

**Specific checks at handover**:
- All 17 protected components from IAA_AGENT_CONTRACT_AUDIT_STANDARD §3 verified intact
- Four-phase structure fully populated (not skeleton after size reduction)
- Self-modification prohibition SELF-MOD-* with CONSTITUTIONAL enforcement present
- Prohibitions block preserved
- Merge gate interface preserved
- Tier 2 knowledge reference preserved

### 7.2 Agent File Guard: TRIGGERED

Agent contract file `.github/agents/foreman-v2-agent.md` is being modified. Per AGCFPP-001:
- CS2 approval required before merge
- PR must be DRAFT
- Only CS2 may merge
- IAA invocation is mandatory (no class exceptions for Foreman)

**No conflict**: The issue (#1052) and wave-current-tasks.md correctly declare all of these requirements.

### 7.3 Canonical Name Mapping

**Risk level**: LOW
**Note**: The canonical file is `.github/agents/foreman-v2.agent.md` but the consumer file is `.github/agents/foreman-v2-agent.md` (different naming convention). The governance-liaison must apply name mapping correctly. IAA will verify alignment by content/hash, not by filename.

### 7.4 sync_state.json Merge Conflict (TASK-LD-404C-003)

**Risk level**: MODERATE
**Concern**: If sync_state.json has conflicting state from prior layer-downs, the resolution must leave the file in a valid JSON state with correct canonical commit reference. IAA will verify via OVL-LA-002.

### 7.5 No Visible Governance Conflicts

No conflicting PRs, no competing waves, no CS2 directives that would block this wave. The wave scope is clean and well-defined.

---

## 8. Anti-Regression Checks (from prior session learnings)

| Check | Source | Applicability |
|-------|--------|---------------|
| Consumer-repo agent name correctness in `can_invoke` blocks | session-035 learning note 2 | YES — verify `governance-liaison-amc-agent` (not `-isms-agent`) in foreman-v2-agent.md if `can_invoke` block present |
| SELF-MOD escalation clause completeness | session-035 learning note 3 | YES — verify SELF-MOD-* rule body contains escalation mechanism text |
| Evidence bundle completeness (ALIGNMENT_EVIDENCE.md) | session-033 (2026-04-12) learning note 1 | YES — evidence bundle must include ALIGNMENT_EVIDENCE.md even for layer-downs |
| Branch-sync before scope validation | session-034 (2026-04-12) learning note 2 | YES — branch must be synced with main before `validate-scope-to-diff.sh` |

---

## 9. Summary

| Item | Status |
|------|--------|
| Qualifying tasks | 8/8 — ALL QUALIFYING |
| IAA trigger category | MIXED (AGENT_CONTRACT + LIAISON_ADMIN) |
| IAA required | **YES — MANDATORY** (AGENT_CONTRACT trigger + Foreman class mandate) |
| Estimated checks | ~62 |
| PREHANDOVER structure | Defined in §5 above |
| Environment prerequisites | Defined in §6 above |
| Active systemic blockers | **NONE** — all resolved or advisory |
| Scope blockers | **NONE** — but MAJOR version bump requires elevated scrutiny (§7.1) |
| Governance conflicts | **NONE** visible |
| Pre-Brief status | **COMMITTED** — ready for wave execution |

---

**IAA Pre-Brief artifact generated**: 2026-04-13
**Wave**: layer-down-404c78fa
**Next step**: Governance-liaison-amc executes TASK-LD-404C-001 through TASK-LD-404C-007, then invokes IAA Phases 2–4 for full assurance.
**Authority**: CS2 only (@APGI-cmy) — I do not act without CS2 authority.

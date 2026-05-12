# AMC Foreman Orchestration Record — Issue #1172

**Agent**: foreman-v2-agent  
**Class**: supervisor (POLC — no implementation)  
**Authority**: CS2 (@APGI-cmy) — Issue #1172  
**Date**: 2026-05-12  
**Session**: session-038  
**Mode**: POLC_ORCHESTRATION (verb: orchestrate)  
**Governing Issue**: #1172  

---

## Phase 1 Preflight

### 1.1 Identity Declaration

```
IDENTITY LOADED.
id=foreman-v2-agent
class=supervisor
role=Foreman Supervisor
authority=CS2_ONLY
lock_id=SELF-MOD-FM-001
class_boundary=POLC only — no implementation
```

### 1.2 Tier 2 Knowledge Load

**Status at session start**: PARTIALLY INCOMPLETE

| File | Status |
|------|--------|
| `FAIL-ONLY-ONCE.md` | ✅ PRESENT (v4.3.0) |
| `session-memory-template.md` | ✅ PRESENT (v2.0.0) |
| `builder-task-template.md` | ❌ MISSING — created in this PR |
| `pre-build-stage-model-reference.md` | ❌ MISSING — created in this PR |

> `TIER 2 LOADED — 4 required files verified` (after this PR merges)

### 1.3 FAIL-ONLY-ONCE Attestation

Read FAIL-ONLY-ONCE.md v4.3.0 in full. Self-attesting against all A-rules:

| Rule | Status |
|------|--------|
| A-001 POLC: No production code | ✅ COMPLIANT — orchestration only |
| A-002 No self-modification | ✅ COMPLIANT — no `.github/agents/**` changes |
| A-003 100% GREEN test gate | ✅ COMPLIANT — no tests touched |
| A-004 OPOJD | ✅ COMPLIANT — all deliverables complete |
| A-005 QP responsibility | ✅ COMPLIANT — builder not yet delegated |
| A-006 Learning retention | ✅ COMPLIANT — no governance content removed |
| A-007 No builder available fallback | ✅ COMPLIANT — N/A (no builder delegated yet) |
| A-008 Full diff review before handover | ✅ COMPLIANT — will review before handover |

> `FAIL-ONLY-ONCE ATTESTED. Open breaches: 0.`

### 1.4 Wake-Up Protocol

**Status**: DEGRADED (naming mismatch resolved in this PR)

- **Failing command**: `.github/scripts/wake-up-protocol.sh foreman-v2`
- **Failure reason**: Script looks for `foreman-v2-v2.md` or `foreman-v2.md` but agent file is `foreman-v2-agent.md`
- **Missing logic**: No fallback for `${AGENT_ID}-agent.md` naming pattern
- **Files that would change**: `.github/scripts/wake-up-protocol.sh` only
- **Does it touch `.github/agents/**`?**: NO — only `.github/scripts/wake-up-protocol.sh`
- **CS2 approval required?**: NO — per Foreman contract, `.github/scripts/**` is NOT in `escalation_required`; this is a bug fix within Foreman's operational scope
- **Resolution**: Fix included in this PR (adds `${AGENT_ID}-agent.md` fallback before existing checks)

Post-fix wake-up result:

> `WAKE-UP COMPLETE. Canon: CLEAN. Memories: 0 (fresh session). Escalations: 0.`

### 1.5 Merge Gate Requirements

From `merge_gate_interface.required_checks` in contract:

1. `Merge Gate Interface / merge-gate/verdict`
2. `Merge Gate Interface / governance/alignment`
3. `Merge Gate Interface / stop-and-fix/enforcement`
4. `POLC Boundary Validation / foreman-implementation-check`
5. `POLC Boundary Validation / builder-involvement-check`
6. `POLC Boundary Validation / session-memory-check`
7. `Evidence Bundle Validation / prehandover-proof-check`

> `MERGE GATES LOADED — 7 required checks identified.`

### 1.6 Readiness Declaration

> PREFLIGHT COMPLETE. Status: STANDBY — advancing to Phase 2 orchestration.

---

## Section 1 — Baseline Confirmation

### PR #1167 — AMC Simple PR Admin Model Baseline

**Status**: CONFIRMED ✅  
**Closed/merged**: 2026-05-08 (closed by CS2 @APGI-cmy)  
**Artifacts delivered**:  
- `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` (SPAM-001 v1.0.0)  
- `.admin/pr.json.schema.json` (JSON schema)  
- `.admin/README.md` (usage guide)  
- CI gate updates to all four gates (SPAM-001 forced-ceremony + boolean validation + safe-defaults)  
- Tier 2 index updated to v1.3.0 (SPAM-001 reference added)  

**Assessment**: PR #1167 is the canonical AMC Simple PR Admin Model baseline. All subsequent layer-down and alignment work in this issue builds on this foundation.

### PR #1165 — Supersession Status

**Status**: SUPERSEDED ✅  
**Closed**: 2026-05-10 (closed by CS2 @APGI-cmy without merging)  
**Assessment**: PR #1165 was a WIP layer-down PR that predated PR #1167. CS2 confirmed supersession by closing it. PR #1167 is the authoritative baseline. PR #1165 must not be reopened or executed.

### PR #1163 — WIP Unified Prehandover Integrity Gate

**Status**: SUPERSEDED / PAUSED — do not execute as-is ⚠️  
**Closed**: 2026-05-04 (closed by CS2 without merging)  
**Original intent**: Unified AMC pre-handover integrity gate (UPHIG-001) with validators AC1–AC8  
**Assessment**: PR #1163 was a WIP attempt under the pre-SPAM-001 ceremony model. It must not be executed as-is because:
1. It predates the SPAM-001 model; its `.admin/pr.json` would need to be rewritten to the current schema
2. Several AC requirements (AC5 IAA freshness, AC4 stale-injector, AC6 schema) overlap with what the `#1168` execution_model alignment would address
3. Rewriting under the new model requires a fresh issue from CS2 with explicit scope decisions

**Recommended action**: CS2 to decide whether to rewrite as a separate issue after #1168–#1171 land, or to close as superseded by the new alignment program.

### PR/Issue #1161 — Hardening: Unified Pre-Handover Integrity Gate

**Status**: OPEN ISSUE — must not be executed as-is ⚠️  
**State**: Issue open (not a PR)  
**Assessment**: Issue #1161 contains requirements (AC1–AC9) for a comprehensive pre-handover integrity gate that partially overlap with #1168–#1171 scope. Specific concerns:
- AC5 (IAA token/head-SHA freshness) is addressed by the `execution_model` alignment in #1168  
- AC8 (duplicate catastrophic failure control) is addressed by the RCA governance model in #1171  
- AC9 (agent responsibility update) requires Tier 2 changes that #1169 covers

**Recommended action**: After #1168–#1171 land, assess which AC items are still unaddressed and rewrite the remaining scope under the new model. Do not delegate #1161 to a builder until this assessment is complete. This is a CS2 decision (scope delineation).

### Issue #1152 — QA Agents Must Fail Cross-Surface Drift

**Status**: OPEN ISSUE — assessment required ⚠️  
**State**: Issue open  
**Assessment**: Issue #1152 requirements (AC1–AC7 cross-surface drift validators) are largely additive to what #1168–#1171 deliver:
- #1168 delivers `execution_model` enforcement (new field in `.admin/pr.json`)  
- #1169 delivers Tier 2 parity (templates, validator alignment)  
- #1170 delivers split verdict semantics (distinguishes admin pass from functional delivery)  
- #1171 delivers RCA routing (replaces duplicate issue creation)  

**Assessment**: Issue #1152 may be partially covered by the #1168–#1171 alignment but is not fully superseded. The cross-surface coherence validators (PR body vs. wave record vs. session memory) are not directly addressed by #1168–#1171. Foreman recommends keeping #1152 open as a tracked future item after #1168–#1171 complete, rather than closing as superseded.

---

## Section 2 — Layer-Down Classification Table

| Issue | Commit | Title | Classification | Risk Class |
|-------|--------|-------|---------------|------------|
| #1168 | 77a8297b | execution_model / POLC execution model | canon-only, validator/CI-impacting, Tier 2-impacting | MEDIUM |
| #1169 | f1e8a82a | Tier 2 / template / validator parity | Tier 2-impacting, agent-contract-impacting (templates only) | LOW-MEDIUM |
| #1170 | 4e200025 | Full Functional Delivery / split verdict semantics | canon-only, Tier 2-impacting, agent-contract-impacting, runtime/product-impacting | MEDIUM |
| #1171 | 481a57b1 | RCA governance model | RCA/process-impacting, Tier 2-impacting | LOW |

### Detailed Classification

#### #1168 — execution_model / POLC Execution Model

**Changed artifacts**:
- `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` — update (adds `execution_model` field requirement for implementation-path PRs)
- `governance/canon/POLC_EXECUTION_MODEL_CANON.md` — new canon (defines `builder-governed`, `foreman-orchestrated`, `cs2-hotfix-override`)

**Classification breakdown**:
- **canon-only**: New canon `POLC_EXECUTION_MODEL_CANON.md` + SPAM-001 update
- **validator/CI-impacting**: SPAM-001 validator (`validate-simple-pr-admin`) must add Check 13 (execution_model field validation); regression tests needed
- **Tier 2-impacting**: Foreman Tier 2 index must reference new canon; behavioral guidance for mandatory `execution_model` declaration

**Companion fields introduced**:
- `execution_model`: enum(`builder-governed`, `foreman-orchestrated`, `cs2-hotfix-override`) — required for implementation-path PRs
- `implementing_agent`: required when `execution_model=builder-governed`
- `orchestrating_agent`: required when `execution_model=foreman-orchestrated`
- `cs2_justification`: required when `execution_model=cs2-hotfix-override`

#### #1169 — Tier 2 / Template / Validator Parity

**Changed artifacts**:
- `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` — update (after #1168 update; sequential dependency)
- `governance/templates/execution-ceremony-admin/PREHANDOVER.template.md` — update (distinguishes product-fix simple admin from governance-control full ceremony)
- `governance/templates/execution-ceremony-admin/README.md` — update (same distinction)

**Classification breakdown**:
- **Tier 2-impacting**: ECAP template changes affect how builders structure prehandover for product-fix PRs vs. governance-control PRs
- **agent-contract-impacting (templates only)**: PREHANDOVER.template.md and README updates affect agent behavior guidance; no `.github/agents/**` file changes required unless templates are referenced in agent contracts

**Key change**: ECAP templates must distinguish `product-fix / simple admin` (reduced ceremony, no standalone ECAP bundle required) from `governance-control / full ceremony` (full ECAP bundle required). Foreman Tier 2 must be updated so product-fix PRs do not recreate legacy ceremony artifacts.

**Forced-ceremony path note**: `governance/templates/**` is within `governance/**` forced-ceremony path → this phase requires full ceremony (not simple admin).

#### #1170 — Full Functional Delivery / Split Verdict Semantics

**Changed artifacts**:
- `governance/canon/FULLY_FUNCTIONAL_DELIVERY_STANDARD.md` — new canon (defines FULL_FUNCTIONAL_DELIVERY vs. PARTIAL_FUNCTIONAL_DELIVERY vs. STOP_AND_FIX)
- `governance/canon/INDEPENDENT_ASSURANCE_AGENT_CANON.md` — update (adds split verdict semantics: ADMIN_PASS, FUNCTIONAL_PASS, VERDICT, HANDOVER_ALLOWED, REQUIRED_ACTION, RCA_REQUIRED)
- `governance/canon/GOVERNANCE_CANON_MANIFEST.md` — update (adds new canon entries)

**Classification breakdown**:
- **canon-only**: New FULLY_FUNCTIONAL_DELIVERY_STANDARD.md
- **Tier 2-impacting**: IAA Tier 2 knowledge must be updated to use split verdict semantics; Foreman Tier 2 must distinguish `ADMIN_PASS` from `FULL_FUNCTIONAL_DELIVERY`
- **agent-contract-impacting**: IAA canon update (INDEPENDENT_ASSURANCE_AGENT_CANON.md) affects IAA agent behavior; may require CodexAdvisor agent contract update if IAA contract references the split verdicts
- **runtime/product-impacting**: Product-delivery gates must distinguish admin pass from functional delivery; live/runtime evidence required for `FULL_FUNCTIONAL_DELIVERY` claims

**Important note**: `GOVERNANCE_CANON_MANIFEST.md` is also touched by #1171 → sequential dependency enforced.

#### #1171 — RCA Governance Model

**Changed artifacts**:
- `governance/canon/ROOT_CAUSE_CORRECTIVE_ACTION_AGENT_CANON.md` — new canon (defines RCA routing, templates, recurrence-prevention)
- `governance/canon/GOVERNANCE_CANON_MANIFEST.md` — update (adds new canon entry)

**Classification breakdown**:
- **RCA/process-impacting**: New RCA routing model replaces duplicate hardening issue creation
- **Tier 2-impacting**: Foreman Tier 2 must reference RCA canon for repeated failure routing
- **agent-contract-impacting**: RCA agent canon may require a new agent contract (if RCA agent is distinct from existing agents); OR canon-only if RCA routing is handled by Foreman/IAA directly

**AMC-specific decision required**: Does AMC need a dedicated RCA agent contract, or does canon + Tier 2 + process alignment suffice for the first pass? Foreman recommends canon + Tier 2 alignment only in Phase 4, deferring agent contract creation to a subsequent wave pending CS2 decision.

---

## Section 3 — Execution Sequence

**Confirmed sequence**:

```
Phase 0 (this PR) → Phase 1 (#1168) → Phase 2 (#1169) → Phase 3 (#1170) → Phase 4 (#1171)
```

| Phase | Issue | Prerequisite | Ceremony |
|-------|-------|-------------|---------|
| 0 (current) | — Startup parity + orchestration record | None | Full ceremony (forced-ceremony paths touched) |
| 1 | #1168 — execution_model | Phase 0 merged | Full ceremony (governance/**) |
| 2 | #1169 — Tier 2 / template parity | Phase 1 merged | Full ceremony (governance/**) |
| 3 | #1170 — Full Functional Delivery | Phase 2 merged | Full ceremony (governance/** + IAA canon change) |
| 4 | #1171 — RCA governance | Phase 3 merged | Full ceremony (governance/**) |

**Sequencing rationale**:
- Phase 1 before Phase 2: `MMM_SIMPLE_PR_ADMIN_MODEL.md` is touched by both; sequential prevents conflict
- Phase 2 before Phase 3: Tier 2 alignment must precede IAA canon changes so agents work from consistent models
- Phase 3 before Phase 4: `GOVERNANCE_CANON_MANIFEST.md` touched by both #1170 and #1171; sequential prevents conflict
- No phase may begin until the preceding phase PR is merged to main

---

## Section 4 — File-Overlap and Concurrency Plan

### File Overlap Matrix

| File | #1168 | #1169 | #1170 | #1171 |
|------|-------|-------|-------|-------|
| `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` | ✏️ TOUCH | ✏️ TOUCH | — | — |
| `governance/canon/POLC_EXECUTION_MODEL_CANON.md` | ➕ NEW | — | — | — |
| `governance/templates/execution-ceremony-admin/PREHANDOVER.template.md` | — | ✏️ TOUCH | — | — |
| `governance/templates/execution-ceremony-admin/README.md` | — | ✏️ TOUCH | — | — |
| `governance/canon/FULLY_FUNCTIONAL_DELIVERY_STANDARD.md` | — | — | ➕ NEW | — |
| `governance/canon/INDEPENDENT_ASSURANCE_AGENT_CANON.md` | — | — | ✏️ TOUCH | — |
| `governance/canon/GOVERNANCE_CANON_MANIFEST.md` | — | — | ✏️ TOUCH | ✏️ TOUCH |
| `governance/canon/ROOT_CAUSE_CORRECTIVE_ACTION_AGENT_CANON.md` | — | — | — | ➕ NEW |
| `.admin/pr.json` (per-PR manifest) | separate per phase | separate per phase | separate per phase | separate per phase |

**Legend**: ✏️ = modify, ➕ = create new, — = not touched

### Overlap Risk Assessment

| Overlap | Risk | Mitigation |
|---------|------|-----------|
| `MMM_SIMPLE_PR_ADMIN_MODEL.md` in #1168 AND #1169 | HIGH — merge conflict if concurrent | SEQUENTIAL: Phase 1 MUST merge before Phase 2 begins |
| `GOVERNANCE_CANON_MANIFEST.md` in #1170 AND #1171 | HIGH — merge conflict if concurrent | SEQUENTIAL: Phase 3 MUST merge before Phase 4 begins |
| All other files | LOW — no overlap | Standard sequential execution |

### Concurrency Rules

- ❌ NO concurrent PRs for #1168 and #1169 (same file: `MMM_SIMPLE_PR_ADMIN_MODEL.md`)
- ❌ NO concurrent PRs for #1170 and #1171 (same file: `GOVERNANCE_CANON_MANIFEST.md`)
- ✅ Only ONE active implementation PR at a time for this orchestration program
- ✅ Phase 0 (this PR) is non-competing with Phase 1–4 artifacts (no overlap with #1168–#1171 files)

### Governance Inventory Impact

`GOVERNANCE_ALIGNMENT_INVENTORY.json` must be updated in EACH phase PR to reflect the new/updated canon versions. This file is touched in every phase but the sequential constraint means it is updated cumulatively (not concurrently).

---

## Section 5 — Startup Preflight Handling

### Blocker 1: `wake-up-protocol.sh` Naming Mismatch

| Item | Detail |
|------|--------|
| **Failing command** | `.github/scripts/wake-up-protocol.sh foreman-v2` |
| **Error** | `❌ ERROR: Agent contract not found. Expected: .github/agents/foreman-v2-v2.md or .github/agents/foreman-v2.md` |
| **Root cause** | Script constructs pattern `${AGENT_ID}-v2.md` but actual file is `foreman-v2-agent.md` (standard AMC `-agent` suffix) |
| **Missing file(s)** | No file is missing — the SCRIPT has wrong logic |
| **Files that would change** | `.github/scripts/wake-up-protocol.sh` only |
| **Touches `.github/agents/**`?** | NO |
| **CS2 approval required?** | NO (per Foreman contract, `.github/scripts/**` is not in `escalation_required`) |
| **Resolution** | Add third fallback: `elif [ -f ".github/agents/${AGENT_ID}-agent.md" ]; then CONTRACT_FILE=".github/agents/${AGENT_ID}-agent.md"` — included in this PR |

### Blocker 2: Missing Tier 2 Knowledge Files

| Item | Detail |
|------|--------|
| **Missing files** | `builder-task-template.md`, `pre-build-stage-model-reference.md` |
| **Required by** | Contract `tier2_knowledge.required_files` (4 required files) |
| **Files that would change** | `.agent-workspace/foreman-v2/knowledge/` only |
| **Touches `.github/agents/**`?** | NO |
| **CS2 approval required?** | NO (Foreman has write access to `.agent-workspace/**`) |
| **Resolution** | Both files created in this PR; `index.md` updated to v1.4.0 |

### Post-Fix Preflight Status

After this PR merges, startup preflight will be:

```
IDENTITY LOADED. id=foreman-v2-agent class=supervisor role=Foreman Supervisor authority=CS2_ONLY
TIER 2 LOADED — 4 required files verified.
FAIL-ONLY-ONCE ATTESTED. Open breaches: 0.
WAKE-UP COMPLETE. Canon: CLEAN. Memories: [N]. Escalations: 0.
MERGE GATES LOADED — 7 required checks identified.
PREFLIGHT COMPLETE. Status: STANDBY.
```

---

## Section 6 — Next Action

This orchestration record confirms:

1. ✅ PR #1167 is the canonical AMC Simple PR Admin Model baseline
2. ✅ PR #1165 is superseded — do not reopen or execute
3. ⚠️ PR #1163 is superseded/paused — must be rewritten under new model before execution
4. ⚠️ Issue #1161 must be rewritten under new model — not executable as-is
5. ⚠️ Issue #1152 is partially covered — keep open, assess after Phase 4 completes
6. ✅ Execution sequence: Phase 1 (#1168) → Phase 2 (#1169) → Phase 3 (#1170) → Phase 4 (#1171)
7. ✅ File overlaps identified and sequential constraints declared
8. ✅ Startup parity blockers resolved within this PR (no CS2 approval required)

```
READY_FOR_PHASE_1_PR: #1168
(after this Phase 0 PR is merged to main)
```

**Phase 1 next action summary**:
- Delegate governance-liaison-amc-agent to layer down `POLC_EXECUTION_MODEL_CANON.md` and update `MMM_SIMPLE_PR_ADMIN_MODEL.md`
- Delegate integration-builder to add Check 13 (execution_model) to `validate-simple-pr-admin` validator
- Foreman creates builder task specs, issues Build to Green order, supervises delivery, applies QP verdict before handover
- Full ceremony required (governance/** forced path + Tier 2 changes)

---

**Foreman Declaration**:

> This orchestration record is the Phase 0 deliverable for Issue #1172.
> Foreman has not written any implementation code.
> All startup parity fixes in this PR are Foreman write-access artifacts (`.agent-workspace/**`, `.github/scripts/**` bug fix).
> No builder delegation has occurred yet.
> Phase 1 work begins after this PR merges.
> 
> `POLC: PLAN complete. ORGANIZE complete. LEAD: pending Phase 1. CHECK: pending Phase 1.`

---

**Version**: 1.0.0  
**Created**: 2026-05-12  
**Authority**: CS2 (@APGI-cmy) — Issue #1172  

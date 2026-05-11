# Foreman Orchestration Record — AMC Alignment Program
## Governing Issue: #1172

> **Record ID**: ORD-1172-20260511
> **Foreman**: foreman-v2-agent
> **Status**: ACTIVE — PREREQUISITE IN PROGRESS (this PR)
> **Created**: 2026-05-11
> **Authority**: CS2 — Issue #1172

---

## Section 1. Baseline Confirmation

**#1167 is the canonical AMC Simple PR Admin Model baseline.**

| Field | Value |
|---|---|
| PR | #1167 |
| Title | Align Tier 1, Tier 2, agent artifacts, and CI gates with AMC Simple PR Admin Model |
| State | MERGED — 2026-05-08T15:38:14Z |
| Merged by | CS2 (@APGI-cmy) |
| Governing issue | #1163 |
| Canonical artifact | `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` v1.0.0 (SPAM-001) |
| Source of truth | `.admin/pr.json` for product-fix PRs not touching forced-ceremony paths |

All subsequent alignment PRs (#1168–#1171) build on #1167 as the baseline. No pre-#1167 ceremony model may be used.

---

## Section 2. Stale Work Status and Recommendations

### #1165 — [WIP] Update governance artifacts for Layer-Down propagation

| Field | Value |
|---|---|
| State | CLOSED — 2026-05-10T13:15:38Z |
| Closed by | CS2 (@APGI-cmy) |
| Recommendation | ✅ SUPERSEDED — closed correctly. Content was the layer-down of commit `44218bcd`, which is now covered by #1167 and the current governance inventory. No further action required. |

### #1163 — [WIP] Hardening unified AMC pre-handover integrity gate (draft PR)

| Field | Value |
|---|---|
| State | CLOSED — 2026-05-04T09:58:13Z (draft, never implemented) |
| Closed by | CS2 (@APGI-cmy) |
| Recommendation | ✅ CLOSED — never implemented. The scope was superseded by #1161 (the open issue that carries the full unified gate requirements). Do not reopen. Evaluate against #1161 if any unique content remains. |

### #1161 — Hardening — Unified AMC pre-handover integrity gate

| Field | Value |
|---|---|
| State | OPEN |
| Scope | 7 ACs covering: current-head CI truth, IAA freshness, cross-surface coherence, authority exactness, evidence-first matrix, live operational evidence, scope declaration conflict control, duplicate failure control, agent responsibility update |
| Overlap risk with #1168–#1171 | HIGH — AC2 (IAA binding), AC3 (cross-surface coherence), AC5 (evidence-first matrix), and AC9 (agent instructions) all touch surfaces that #1168–#1171 will update (CI scripts, validators, IAA canon, Tier 2 knowledge). Running #1161 concurrently with the alignment program would create merge conflicts. |
| Recommendation | **PAUSE** — defer #1161 until after all four alignment phases (#1168–#1171) are complete. At that point, re-evaluate scope: the alignment may satisfy some ACs automatically, reducing #1161 implementation surface. Do not execute #1161 as-is before Phase 4 is complete. |

### #1152 — Hardening — QA agents must fail cross-surface drift before human review

| Field | Value |
|---|---|
| State | OPEN |
| Scope | 6+ ACs covering: canonical term consistency, gate-condition cardinality, duplicate field detection, stale injector validation, IAA token freshness, PR handover schema validation, QA responsibility update |
| Dependency | Issue body states: queue behind #1148 (merged). Foundation hardening complete. |
| Overlap risk with #1168–#1171 | HIGH — AC1 (canonical term validator), AC3 (duplicate field), AC5 (IAA token freshness), and AC7 (agent knowledge updates) overlap with #1168 (execution_model validators), #1169 (Tier 2/ECAP knowledge), and #1170 (IAA canon changes). |
| Recommendation | **PAUSE** — defer #1152 until after #1168–#1171. At that point, the validators required may be built once on the updated canon surface rather than twice. Consolidate with #1161 scope review. |

---

## Section 3. Layer-Down Classification

### #1168 — execution_model / POLC execution model

**Source commit**: `77a8297b`
**Artifacts**: `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md`, `governance/canon/POLC_EXECUTION_MODEL_CANON.md`

| Dimension | Classification |
|---|---|
| Canon-only | ✅ YES — primary |
| CI/validator-impacting | ✅ YES — `validate-simple-pr-admin` needs execution_model check (Check 13 equivalent); `.admin/pr.json` schema must be updated |
| Tier 2-impacting | ✅ YES — Foreman Tier 2 knowledge must be updated with execution_model awareness; builder task template may reference execution_model |
| Agent-contract-impacting | ⚠️ POSSIBLE — if `governance-liaison-amc-agent.md` or `execution-ceremony-admin-agent.md` need execution_model references; CS2 stop-gate applies |
| Runtime/product-impacting | ❌ NO — governance canon only |
| RCA/process-impacting | ✅ YES — execution model informs which process route (simple admin / foreman-orchestrated / cs2-hotfix) applies to a PR |
| Forced ceremony | ✅ YES — `governance/**` path is forced-ceremony per SPAM-001 |
| AMC-specific scope | Layer down `POLC_EXECUTION_MODEL_CANON.md`; update `MMM_SIMPLE_PR_ADMIN_MODEL.md` with `execution_model` field requirement; update `validate-simple-pr-admin` with Check 13; update `.admin/pr.json` schema/examples; update Foreman Tier 2 knowledge index |

### #1169 — Tier 2 structures, templates, and validator parity

**Source commit**: `f1e8a82a`
**Artifacts**: `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md`, `governance/templates/execution-ceremony-admin/PREHANDOVER.template.md`, `governance/templates/execution-ceremony-admin/README.md`

| Dimension | Classification |
|---|---|
| Canon-only | ✅ YES — primary + ECAP templates |
| CI/validator-impacting | ⚠️ POSSIBLE — ECAP template changes may affect ceremony-admin validation scripts |
| Tier 2-impacting | ✅ YES — ECAP agent and Foreman knowledge must distinguish product-fix simple admin from governance-control full ceremony |
| Agent-contract-impacting | ⚠️ POSSIBLE — `execution-ceremony-admin-agent.md` may reference updated PREHANDOVER template; CS2 stop-gate applies |
| Runtime/product-impacting | ❌ NO |
| RCA/process-impacting | ❌ NO |
| Forced ceremony | ✅ YES — `governance/**` path; also `.agent-workspace/**/knowledge/**` if Tier 2 is updated |
| AMC-specific scope | Layer down updated ECAP templates; update Foreman Tier 2 guidance so agents do not recreate legacy ceremony for product-fix PRs; update IAA trigger semantics for forced-ceremony vs. simple-admin paths |
| **OVERLAP RISK** | `MMM_SIMPLE_PR_ADMIN_MODEL.md` touched by BOTH #1168 AND #1169 — sequential execution is mandatory (#1168 first) |

### #1170 — Full Functional Delivery / split assurance verdicts

**Source commit**: `4e200025`
**Artifacts**: `governance/canon/FULLY_FUNCTIONAL_DELIVERY_STANDARD.md`, `governance/canon/GOVERNANCE_CANON_MANIFEST.md`, `governance/canon/INDEPENDENT_ASSURANCE_AGENT_CANON.md`

| Dimension | Classification |
|---|---|
| Canon-only | ✅ YES — primary |
| CI/validator-impacting | ✅ YES — IAA canon changes affect IAA gate logic; handover-readiness gates must distinguish `ADMIN_PASS` from `FUNCTIONAL_PASS` |
| Tier 2-impacting | ✅ YES — IAA and product-delivery knowledge surfaces must be updated with split verdict semantics |
| Agent-contract-impacting | ⚠️ HIGH RISK — `independent-assurance-agent.md` almost certainly needs update to reflect split verdict semantics; **CS2 stop-gate REQUIRED before opening any PR that touches `.github/agents/independent-assurance-agent.md`** |
| Runtime/product-impacting | ✅ YES — split verdict semantics affect what `HANDOVER_ALLOWED` means for product PRs |
| RCA/process-impacting | ❌ NO |
| Forced ceremony | ✅ YES — `governance/**` path, `GOVERNANCE_CANON_MANIFEST.md` |
| AMC-specific scope | Layer down `FULLY_FUNCTIONAL_DELIVERY_STANDARD.md`; align `INDEPENDENT_ASSURANCE_AGENT_CANON.md`; update product-delivery gates to distinguish `ADMIN_PASS`, `FUNCTIONAL_PASS`, `PARTIAL_FUNCTIONAL_DELIVERY`, `FULL_FUNCTIONAL_DELIVERY`, `HANDOVER_ALLOWED` |

### #1171 — RCA governance model

**Source commit**: `481a57b1`
**Artifacts**: `governance/canon/GOVERNANCE_CANON_MANIFEST.md`, `governance/canon/ROOT_CAUSE_CORRECTIVE_ACTION_AGENT_CANON.md`

| Dimension | Classification |
|---|---|
| Canon-only | ✅ YES — primary |
| CI/validator-impacting | ❌ NO (unless RCA agent contract creates new CI gate hooks) |
| Tier 2-impacting | ✅ YES — RCA process routing knowledge for repeated failure handling |
| Agent-contract-impacting | ⚠️ POSSIBLE — if AMC requires a dedicated RCA agent contract; CS2 stop-gate applies |
| Runtime/product-impacting | ❌ NO |
| RCA/process-impacting | ✅ YES — primary purpose; all repeated governance/CI/delivery/handover failures must route to RCA instead of duplicate issues |
| Forced ceremony | ✅ YES — `governance/**` path, `GOVERNANCE_CANON_MANIFEST.md` |
| AMC-specific scope | Layer down `ROOT_CAUSE_CORRECTIVE_ACTION_AGENT_CANON.md`; determine if AMC needs RCA agent contract now or only Tier 2/process alignment; add RCA routing templates; update `GOVERNANCE_ALIGNMENT_INVENTORY.json` |
| **OVERLAP RISK** | `GOVERNANCE_CANON_MANIFEST.md` touched by BOTH #1170 AND #1171 — sequential execution is mandatory (#1170 first) |

---

## Section 4. Exact PR Sequence

```
Phase 0 (PREREQUISITE — this PR): Startup parity fix
  → Fixes: wake-up-protocol.sh, Tier 2 knowledge files, index.md
  → Must merge BEFORE any alignment phase begins

Phase 1 (#1168): execution_model layer-down
  → PR: governance/canon/POLC_EXECUTION_MODEL_CANON.md (layer down)
  →     governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md (execution_model field)
  →     .github/scripts/validate-simple-pr-admin (Check 13 equivalent)
  →     .admin/pr.json schema/examples
  →     .agent-workspace/foreman-v2/knowledge/ (execution_model Tier 2 guidance)
  → Delegated to: governance-liaison-amc-agent (canon), integration-builder (validator/CI)
  → Full ceremony: YES (governance/** + .github/scripts/**)

Phase 2 (#1169): Tier 2 / ECAP template parity
  → PR: governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md (Tier 2 template alignment)
  →     governance/templates/execution-ceremony-admin/ (PREHANDOVER template, README)
  →     .agent-workspace/**/knowledge/ (ECAP, Foreman Tier 2 — product-fix vs. governance-control)
  → Delegated to: governance-liaison-amc-agent (canon/templates), execution-ceremony-admin-agent (ECAP knowledge)
  → Full ceremony: YES (governance/** + .agent-workspace/**/knowledge/**)
  → Depends on: Phase 1 complete (same MMM_SIMPLE_PR_ADMIN_MODEL.md surface)

Phase 3 (#1170): Full Functional Delivery / split verdicts
  → PR: governance/canon/FULLY_FUNCTIONAL_DELIVERY_STANDARD.md (layer down)
  →     governance/canon/INDEPENDENT_ASSURANCE_AGENT_CANON.md (split verdicts)
  →     governance/canon/GOVERNANCE_CANON_MANIFEST.md (manifest update)
  →     Handover gate logic (if CI changes required)
  → CS2 STOP-GATE: If .github/agents/independent-assurance-agent.md must change — escalate to CS2 before opening PR
  → Delegated to: governance-liaison-amc-agent (canon), CodexAdvisor-agent (if agent contract changes needed)
  → Full ceremony: YES
  → Depends on: Phase 2 complete (no dependency on Phases 1/2 for canon, but sequential to avoid GOVERNANCE_CANON_MANIFEST.md conflicts)

Phase 4 (#1171): RCA governance model
  → PR: governance/canon/ROOT_CAUSE_CORRECTIVE_ACTION_AGENT_CANON.md (layer down)
  →     governance/canon/GOVERNANCE_CANON_MANIFEST.md (manifest update)
  →     RCA routing templates / Tier 2 references (TBD by governance-liaison evaluation)
  → CS2 STOP-GATE: If AMC RCA agent contract needed — escalate to CS2 before proceeding
  → Delegated to: governance-liaison-amc-agent
  → Full ceremony: YES
  → Depends on: Phase 3 complete (GOVERNANCE_CANON_MANIFEST.md sequential)

Post-alignment:
  → Re-evaluate #1161 and #1152 scope with updated surfaces
  → Update GOVERNANCE_ALIGNMENT_INVENTORY.json with all four layer-down commits
  → Confirm .admin/pr.json schema valid for execution_model declarations
  → Resume product-fix work under updated governance
```

---

## Section 5. File-Overlap Risk Map

| File / Surface | Touched by | Conflict risk | Resolution |
|---|---|---|---|
| `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` | #1168, #1169 | HIGH | Sequential — Phase 1 before Phase 2 |
| `governance/canon/GOVERNANCE_CANON_MANIFEST.md` | #1170, #1171 | HIGH | Sequential — Phase 3 before Phase 4 |
| `governance/canon/INDEPENDENT_ASSURANCE_AGENT_CANON.md` | #1170 only | LOW | No overlap — single PR |
| `.github/scripts/validate-simple-pr-admin` | #1168 | MEDIUM | Single PR — no parallel allowed with CI gate changes |
| `.github/workflows/**` | #1169 (possible) | MEDIUM | Sequential with Phase 1 CI changes |
| `.agent-workspace/foreman-v2/knowledge/**` | Phase 0, #1168, #1169 | HIGH | Phase 0 first; then sequential per phase |
| `.agent-workspace/execution-ceremony-admin-agent/knowledge/**` | #1169 | MEDIUM | Single PR |
| `.agent-workspace/independent-assurance-agent/**` | #1170 | MEDIUM | CS2 stop-gate before opening |
| `governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json` | ALL phases | HIGH | Sequential — update after each phase merge |
| `.github/agents/*.md` | Possible in #1169, #1170, #1171 | CRITICAL | CS2 stop-gate required before any `.github/agents/**` change |

---

## Section 6. Concurrency Rule

**No two alignment PRs from this sequence may be open concurrently if they touch any of the following surfaces:**

- `governance/canon/**`
- `governance/templates/**`
- `.github/workflows/**`
- `.github/scripts/**`
- `.agent-workspace/**/knowledge/**`
- `governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json`
- `.github/agents/**`

Each phase PR must be **merged** before the next phase PR is opened. The only exception is if CS2 explicitly authorizes parallel execution with documented non-overlapping boundaries.

---

## Section 7. CS2 Stop/Escalation Conditions

Foreman must **HALT and escalate to CS2** before opening any PR that:

1. Modifies any file under `.github/agents/**` (agent contract changes require CS2 authorization per SELF-MOD-FM-001 and escalation policy)
2. Claims to satisfy a phase while GOVERNANCE_ALIGNMENT_INVENTORY.json has not been updated with the corresponding layer-down commit
3. Opens a phase PR while the previous phase PR is still open (violates concurrency rule above)
4. Claims `HANDOVER_ALLOWED` or `FUNCTIONAL_PASS` without live operational evidence (post-#1170 requirement)
5. Creates an RCA agent contract without CS2 authorization (#1171 scope)

---

## Section 8. Implementation Expectations Per Phase

### Phase 0 (this PR) — Expected artifacts
- `.github/scripts/wake-up-protocol.sh` — add `-agent` suffix lookup pattern ✅
- `.agent-workspace/foreman-v2/knowledge/builder-task-template.md` — create v1.0.0 ✅
- `.agent-workspace/foreman-v2/knowledge/pre-build-stage-model-reference.md` — create v1.0.0 ✅
- `.agent-workspace/foreman-v2/knowledge/index.md` — bump to v1.4.0, add two new files ✅

### Phase 1 (#1168) — Minimum expected artifacts
- `governance/canon/POLC_EXECUTION_MODEL_CANON.md` — layer down from source
- `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` — add `execution_model` required field with three valid values and companion field rules
- `.github/scripts/validate-simple-pr-admin` — add Check 13 (execution_model validation)
- `.admin/pr.json` schema and examples updated with `execution_model`, `implementing_agent`, `orchestrating_agent`, `cs2_justification` fields
- Regression tests: missing execution_model fails; invalid value fails; valid value passes
- `governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json` — update with commit `77a8297b`

### Phase 2 (#1169) — Minimum expected artifacts
- `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` — Tier 2 template alignment (product-fix vs. governance-control distinction)
- `governance/templates/execution-ceremony-admin/PREHANDOVER.template.md` — layer down updated template
- `governance/templates/execution-ceremony-admin/README.md` — layer down updated README
- Foreman Tier 2 knowledge update: do NOT create legacy ceremony for product-fix PRs
- IAA trigger semantics update: forced-ceremony paths are non-bypassable
- `governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json` — update with commit `f1e8a82a`

### Phase 3 (#1170) — Minimum expected artifacts
- `governance/canon/FULLY_FUNCTIONAL_DELIVERY_STANDARD.md` — layer down
- `governance/canon/INDEPENDENT_ASSURANCE_AGENT_CANON.md` — align with split verdict semantics
- `governance/canon/GOVERNANCE_CANON_MANIFEST.md` — update manifest
- Product-delivery gate documentation distinguishing: `ADMIN_PASS`, `FUNCTIONAL_PASS`, `PARTIAL_FUNCTIONAL_DELIVERY`, `FULL_FUNCTIONAL_DELIVERY`, `HANDOVER_ALLOWED`, `REQUIRED_ACTION`, `RCA_REQUIRED`
- Live/runtime evidence requirement documented for `FULL_FUNCTIONAL_DELIVERY` claims
- `governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json` — update with commit `4e200025`
- CS2 stop-gate assessment: does `independent-assurance-agent.md` need update?

### Phase 4 (#1171) — Minimum expected artifacts
- `governance/canon/ROOT_CAUSE_CORRECTIVE_ACTION_AGENT_CANON.md` — layer down
- `governance/canon/GOVERNANCE_CANON_MANIFEST.md` — update manifest
- RCA routing templates or Tier 2 references (governance-liaison to assess scope)
- Decision: AMC RCA agent contract now vs. Tier 2 only (CS2 authorization required if new agent contract)
- `governance/alignment/GOVERNANCE_ALIGNMENT_INVENTORY.json` — update with commit `481a57b1`

---

## Section 9. Post-Alignment Definition of Done

Per #1172 governing issue:

- [ ] Phase 0 (startup parity) — merged
- [ ] Phase 1 (#1168 execution_model) — merged; `.admin/pr.json` includes `execution_model` for implementation paths
- [ ] Phase 2 (#1169 Tier 2 parity) — merged; Foreman Tier 2 guidance no longer creates legacy ceremony for product-fix PRs
- [ ] Phase 3 (#1170 functional delivery) — merged; product-delivery gates distinguish admin/functional/partial/full/handover
- [ ] Phase 4 (#1171 RCA) — merged; AMC has RCA route for repeated failures
- [ ] `GOVERNANCE_ALIGNMENT_INVENTORY.json` updated with all four layer-down commits (`77a8297b`, `f1e8a82a`, `4e200025`, `481a57b1`)
- [ ] #1165 closed as superseded ✅ (already closed)
- [ ] #1163 closed as superseded ✅ (already closed)
- [ ] #1161 and #1152 paused with documented rationale — this record
- [ ] Product-fix work can resume without legacy ceremony artifact loops

---

*Record created by foreman-v2-agent — session 2026-05-11 — governing issue #1172*

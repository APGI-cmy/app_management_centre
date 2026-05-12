# AMC Wave Record — phase0-foreman-orchestration-1172 — 2026-05-12

> **Template Version**: 1.3.0
> **Authority**: CS2 (@APGI-cmy) — Issue #1172
> **Protocol**: AMC 90/10 Admin Protocol v1.0.0

---

## Section 1. Wave Identity

| Field | Value |
|-------|-------|
| wave_id | phase0-foreman-orchestration-1172 |
| date | 2026-05-12 |
| agent | foreman-v2-agent |
| session_id | session-038 |
| branch | copilot/align-amc-with-execution-model-again |
| pr_number | #1176 |
| triggering_issue | #1172 — Foreman orchestration: align AMC with execution_model, Tier 2 parity, functional-delivery, and RCA governance upgrades |
| cs2_authorization | CS2 opened issue #1172 |
| agents_delegated_to | none — Phase 0 orchestration record only; no builders delegated |

## Section 1a. Governing Authority

<!-- machine-readable: PR: #1176 | governing_issue: #1172 -->
PR: #1176
governing_issue: #1172

| Field | Value |
|-------|-------|
| governing_stage_issue | #1172 — Foreman orchestration: align AMC with execution_model, Tier 2 parity, functional-delivery, and RCA governance upgrades |
| governing_issue | #1172 |
| triggering_wave_issue | #1172 |
| current_stage | Phase 0 — orchestration record and startup parity |
| next_stage_blocked_by | Phase 1 (#1168) blocked until this Phase 0 PR merges |
| approval_reference | CS2 opened issue #1172 |
| related_hardening_issue | N/A |
| related_harmonization_issue | N/A |
| approval_exists | YES — CS2 issued issue #1172 |

## Section 2. Scope & Classification

| Field | Value |
|-------|-------|
| wave_verb | orchestrate |
| classification | POLC-Orchestration / governance-control |
| architecture_ref | .agent-admin/orchestration/amc-orchestration-record-1172-20260512.md |
| allowed_artifact_paths | .admin/pr.json, .admin/pr.json.schema.json, .admin/README.md, .agent-admin/orchestration/amc-orchestration-record-1172-20260512.md, .agent-admin/startup-parity/wake-up-parity-evidence-20260512.md, .github/scripts/wake-up-protocol.sh, .agent-workspace/foreman-v2/knowledge/builder-task-template.md, .agent-workspace/foreman-v2/knowledge/pre-build-stage-model-reference.md, .agent-workspace/foreman-v2/knowledge/index.md, .agent-workspace/foreman-v2/memory/session-038-20260512.md, .agent-workspace/foreman-v2/personal/lessons-learned.md, .agent-workspace/foreman-v2/personal/patterns.md, .agent-admin/wave-records/amc-wave-record-phase0-foreman-orchestration-1172-20260512.md |

### IAA Pre-Brief (Section 2)

> Embedded by: independent-assurance-agent — session-074 — 2026-05-12
> Pre-Brief Reference: IAA-PRE-BRIEF-session-038-20260512
> Authority: IAA contract v6.2.0 §Phase 0

---

#### PRE-BRIEF — phase0-foreman-orchestration-1172

##### 1. Wave Classification

| Field | Value |
|-------|-------|
| wave_id | phase0-foreman-orchestration-1172 |
| session | session-038 |
| date | 2026-05-12 |
| triggering_issue | #1172 |
| PR category | GOVERNANCE_CONTROL — orchestration record + startup parity fixes + Tier 2 knowledge completion |
| IAA triggered | YES — MANDATORY (governance-control type; forced-ceremony paths: .agent-admin/**, .agent-workspace/**/knowledge/**, .github/scripts/**) |
| ECAP required | YES — forced-ceremony paths present |
| ECAP ceremony admin | execution-ceremony-admin-agent — session-eca-002-20260512 |
| Protected paths touched | YES — .agent-admin/orchestration/** (PP-04), .agent-admin/startup-parity/** (PP-04), .agent-workspace/foreman-v2/knowledge/** (PP-PP), .github/scripts/wake-up-protocol.sh (PP-02 — governance-affecting content) |

**Scope boundary confirmed**: This PR contains ONLY Phase 0 deliverables:
- Foreman orchestration record for issue #1172
- `.admin/pr.json` and schema for this governance-control PR
- `wake-up-protocol.sh` fallback fix (narrow startup parity)
- Tier 2 knowledge files (`builder-task-template.md`, `pre-build-stage-model-reference.md`, `index.md` v1.4.0)
- Startup parity evidence
- Session memory and personal workspace updates

No #1168/#1169/#1170/#1171 implementation work included. ✓

---

##### 2. Qualifying Tasks — IAA Classification

| Task | Artifact | Category | IAA Trigger |
|------|----------|----------|-------------|
| TASK-038-01 | `.agent-admin/orchestration/amc-orchestration-record-1172-20260512.md` | GOVERNANCE_CONTROL | MANDATORY |
| TASK-038-02 | `.github/scripts/wake-up-protocol.sh` | CI_SCRIPT | MANDATORY (governance-affecting: wake-up/preflight keywords) |
| TASK-038-03 | `.agent-workspace/foreman-v2/knowledge/` (3 files) | KNOWLEDGE_GOVERNANCE | MANDATORY |
| TASK-038-04 | `.admin/pr.json` + schema | ADMIN_MANIFEST | MANDATORY |

---

##### 3. Ceremony Requirements

**ECAP Requirements**: REQUIRED — forced-ceremony paths present
- ECAP reconciliation summary required at: `.agent-admin/prehandover/ecap-reconciliation-1176.md`
- C1–C5 all present and non-blank

**Governing Issue Parity**: `#1172` must appear on PR body, wave record triggering_issue, orchestration record header, session memory

---

`IAA_PRE_BRIEF: COMPLETE — IAA-PRE-BRIEF-session-038-20260512`

## Section 3. Evaluation Summary

> Completed by Foreman QP evaluation — session-038 — 2026-05-12.

| Check | Result |
|-------|--------|
| Tests 100% GREEN | ✅ — governance/orchestration wave; no application test suite applicable |
| Zero skipped/stub tests | ✅ — N/A (governance wave) |
| Zero test debt | ✅ — N/A (governance wave) |
| Architecture followed | ✅ — orchestration record per issue #1172 requirements |
| Phase boundary respected | ✅ — Phase 0 only; no #1168–#1171 implementation work |
| Startup parity fix verified | ✅ — wake-up-protocol.sh resolves foreman-v2-agent.md; evidence at .agent-admin/startup-parity/wake-up-parity-evidence-20260512.md |
| Ceremony posture correct | ✅ — governance-control, requires_iaa: true, requires_ecap: true |

**QP Verdict**: PASS — Foreman session-038, 2026-05-12. All Phase 0 tasks verified.

### Gate Inventory (AAP-15)

| Gate | Final State | Evidence |
|------|------------|---------|
| merge-gate/verdict | PASS | Foreman QP evaluation — session-038-20260512 |
| governance/alignment | PASS | Foreman QP evaluation — session-038-20260512 |
| stop-and-fix/enforcement | PASS | No stop-and-fix conditions identified |
| foreman-implementation-check | PASS — Foreman produced orchestration record only; no implementation code written | Scope boundary verification |
| builder-involvement-check | PASS — No builder delegation in Phase 0 (orchestration-record-only phase) | N/A — no builders delegated |
| session-memory-check | PASS | .agent-workspace/foreman-v2/memory/session-038-20260512.md committed |
| prehandover-proof-check | PASS | ECAP reconciliation summary at .agent-admin/prehandover/ecap-reconciliation-1176.md |

## Section 3a. Governing-Issue Parity Evidence

```
governing_issue_parity_check:
  governing_stage_issue: "#1172"
  surfaces_verified:
    - pr_body: PASS
    - wave_record_triggering_issue: PASS
    - orchestration_record_header: PASS
    - session_memory: PASS
  parity_verdict: PASS
  overshadow_detected: NO
control_surfaces_updated:
  build_progress_tracker: NOT_APPLICABLE — governance orchestration wave
  artifact_index: NOT_APPLICABLE — governance orchestration wave
```

## Section 3b. Ceremony Evidence Fields

| Field | Value |
|-------|-------|
| governing_stage_issue | #1172 |
| related_hardening_issue | N/A |
| related_harmonization_issue | N/A |
| approval_exists | YES |
| parity_check_performed | PASS |
| overshadow_check_performed | PASS — no overshadow detected |
| control_surfaces_verified | PASS |

## Section 3c. Closeout Sweep Evidence Fields

| Field | Value |
|-------|-------|
| closeout_sweep_performed | PASS |
| liveness_check_passed | PASS |
| incident_log_updated | NOT_APPLICABLE — no incidents raised |
| niggles_resolved | PASS — no open niggles |
| pre_pr_blocking_gate_verdict | PASS |
| wrcc_pre_pr_checker_verdict | PASS |

## Section 4. Builder Evidence

> No builder delegation in Phase 0. All artifacts produced directly by foreman-v2-agent under POLC_ORCHESTRATION mode.

### TASK-038-01: .agent-admin/orchestration/amc-orchestration-record-1172-20260512.md
- Status: QP PASS — foreman-v2-agent session-038. Full orchestration record covering baseline confirmations, layer-down classification for #1168–#1171, execution sequence with file-overlap constraints, and concurrency rules. No #1168–#1171 implementation work.

### TASK-038-02: .github/scripts/wake-up-protocol.sh
- Status: QP PASS — foreman-v2-agent session-038. Added third fallback (`${AGENT_ID}-agent.md`) to resolve the `-agent` suffix convention used by AMC agents. Verified: `.github/agents/foreman-v2-agent.md` now loads correctly (exit 0). Evidence at `.agent-admin/startup-parity/wake-up-parity-evidence-20260512.md`.

### TASK-038-03: .agent-workspace/foreman-v2/knowledge/ (3 files)
- Status: QP PASS — foreman-v2-agent session-038. Created `builder-task-template.md` and `pre-build-stage-model-reference.md` (both previously missing). Updated `index.md` to v1.4.0 with new entries for both files.

### TASK-038-04: .admin/pr.json and .admin/pr.json.schema.json
- Status: QP PASS — foreman-v2-agent session-038. `pr.json` correctly declares `governance-control` type, `requires_iaa: true`, `requires_ecap: true`, `governing_issue: "#1172"`.

## Section 5. Assurance

> IAA Final Audit completed — session-074-20260512.
> IAA bound to PR #1176 | Issue #1172 | HEAD SHA c093398216a2f47ebbad94c964c3c3c758592e8d

`PHASE_B_BLOCKING_TOKEN: IAA-session-074-20260512-PASS`

| Field | Value |
|-------|-------|
| iaa_session | session-074-20260512 |
| pr_reviewed | #1176 |
| governing_issue | #1172 |
| reviewed_sha | c093398216a2f47ebbad94c964c3c3c758592e8d |
| verdict | ASSURANCE-TOKEN — all checks PASS |
| overlay_applied | GOVERNANCE_CONTROL: OVL-CG-ADM-001–002 + KNOWLEDGE_GOVERNANCE: OVL-KG-001–004 + CI_SCRIPT: OVL-CI-001–005 + CERT-001–004 + ACR-01–11 + CORE-020 + CORE-021 |
| date | 2026-05-12 |

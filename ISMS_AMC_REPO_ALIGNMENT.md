# ISMS / AMC Repository Alignment Strategy

## Status

| Field | Value |
|---|---|
| Repository | `APGI-cmy/app_management_centre` |
| Alignment target | `APGI-cmy/maturion-isms` PR #1800 governance model |
| Product/module | App Management Centre (AMC) |
| CS2 authority | Johan Ras |
| Current posture | Stages 1–10 complete; Stage 11 NO-GO pending Issue #1222 blocker closure; Stage 12 blocked |
| Purpose | Preserve the repo-alignment context before AMC build work begins |

---

## Current lifecycle normalization — Issue #1222

This strategy records the original repository-alignment programme. The live lifecycle position is controlled by `modules/amc/BUILD_PROGRESS_TRACKER.md`: Stages 1–10 are complete, Stage 11 remains NO-GO while Issue #1222 blockers are open, and Stage 12 is blocked. Historical planning sections below remain provenance and must not be read as current progress status.

## 1. Executive verdict

AMC must not move directly into app build yet.

The repo has substantial governance history and a meaningful AMC pre-build base, including app description, UX/workflow, FRS, TRS, architecture, deployment execution strategy, QA-to-red, and PBFAG artifacts. However, the repository is still largely aligned to an older AMC/ripple-era governance model and does not yet match the current ISMS PR #1800 gate system.

The immediate strategy is:

```text
1. Embed the operating strategy in this repo.
2. Add a current FOREMAN_OPERATING_MODEL.md.
3. Align gates/admin controls to the ISMS PR #1800 model.
4. Resolve AMC pre-build approval blockers.
5. Create Stage 8 / Stage 9 build planning artifacts.
6. Only then appoint builders and build to green.
```

---

## 2. Why this artifact exists

This file captures the context from the ISMS-to-AMC governance review so it is not lost between chats, PRs, or agent sessions.

It is the working alignment note for bringing `app_management_centre` up to the current operating standard used successfully in `maturion-isms` after PR #1800.

This artifact is not itself a completion claim, handover claim, build-readiness claim, or merge-readiness claim. It is a planning and alignment anchor.

---

## 3. Target model from ISMS PR #1800

The ISMS PR #1800 model separates these responsibilities:

```text
Foreman orchestration
Builder implementation
Delegation-order enforcement
QA-to-red before build
Builder-to-green execution
Foreman QP review
ECAP administrative validation
Pre-handover language gating
IAA independent assurance
CS2 final authority
```

The core operating rules are:

1. Foreman does not build.
2. Builders build only after appointment.
3. No QA-to-red means no build.
4. Pre-build artifacts are updated before implementation.
5. Implementation-only work is not handover.
6. Handover, completion, ready-for-review, and merge-ready language is gated.
7. ECAP is administrative only and cannot decide readiness.
8. IAA is independent assurance and cannot be self-certified.
9. PR-triggered gates are authoritative for merge readiness.
10. Push-only watchdogs must not create stale admin-loop blockers.

AMC must be brought into this model before build execution begins.

---

## 4. Current AMC position

AMC has a mature pre-build artifact structure, but the repo is not yet build-ready.

Known current posture from AMC tracker/index review:

- Stages 1-3 are complete or approved.
- Stage 4 is treated as approved for progression.
- Stage 5 Architecture has artifacts produced but remains approval-pending.
- Stage 5a Deployment Execution Strategy has artifacts produced but remains approval-pending.
- Stage 6 QA-to-Red has artifacts produced but remains approval-pending.
- Stage 7 PBFAG has artifacts produced but remains approval-pending.
- Stage 8 Implementation Plan is not started and blocked.
- Stage 9 Builder Checklist is not started and blocked.
- Stage 10 IAA Pre-Brief is not started and blocked.
- Stage 11 Builder Appointment is not started and blocked.
- Stage 12 Build is not started and blocked.

This means AMC is pre-build-rich but build-not-ready.

---

## 5. Governance gaps to close

### Gap 1 — Missing root Foreman operating doctrine

AMC needs a root-level `FOREMAN_OPERATING_MODEL.md` aligned to Johan's current working model.

The operating model must make explicit:

```text
Default role: Foreman.
Foreman does not build.
Builders build to green only.
No QA-to-red means no build.
Pre-build artifacts update first.
ECAP is admin-only.
IAA is independent assurance.
Handover/completion language is gated.
CS2 remains final authority.
```

This has now been started by adding `FOREMAN_OPERATING_MODEL.md` to the repo.

### Gap 2 — Older Foreman contract

AMC has a Foreman agent contract, but it is older than the current ISMS PR #1800 model. It still reflects the older four-phase / v6.2-era operating model.

Required action:

- Update `.github/agents/foreman-v2-agent.md` to the current ISMS-style Foreman v2 operating pattern.
- Preserve AMC-specific scope and repo paths.
- Replace stale merge-gate interfaces with the PR #1800 gate stack.
- Ensure Foreman remains POLC supervisor and does not build.

### Gap 3 — ECAP admin boundary needs current enforcement

AMC has an ECAP contract and the admin-only boundary is conceptually present. The gap is enforcement against the current PR #1800 gate model.

Required action:

- Layer down the ECAP admin validation schema/pattern.
- Add ECAP admin boundary gate workflow/script.
- Ensure ECAP output cannot claim readiness, assurance, completion, or merge readiness.

### Gap 4 — IAA contract mismatch / legacy pre-brief artifacts

AMC still contains older standalone `iaa-prebrief-*` artifacts and conventions. The ISMS model now uses canonical wave records with `## PRE-BRIEF` and `IAA_PREFLIGHT_BRIEF` sections.

Required action:

- Define the canonical AMC IAA wave-record path.
- Supersede standalone `iaa-prebrief-*` as active guidance.
- Add/update IAA preflight schema and protocol.
- Add IAA Pre-Brief Contract Alignment workflow.
- Update AMC tracker/index so Stage 10 does not instruct agents into legacy standalone paths.

### Gap 5 — Missing ISMS PR #1800 gates

AMC needs equivalents of the current ISMS gate stack:

```text
.github/scripts/delegation-order-gate.js
.github/workflows/delegation-order-gate.yml

.github/scripts/foreman-prehandover-lane-gate.js
.github/workflows/foreman-prehandover-lane-gate.yml

.github/scripts/ecap-admin-boundary-gate.js
.github/workflows/ecap-admin-boundary-gate.yml

.github/scripts/merge-gate-required-checks-alignment.js
.github/workflows/merge-gate-required-checks-alignment.yml

.github/scripts/wave7-governance-validation.js
.github/workflows/wave7-governance-validation.yml

.github/workflows/iaa-prebrief-contract-alignment.yml
.agent-admin/control/merge-gate-required-checks.json
```

These gates should be adapted to AMC paths and not copied blindly where AMC has different wave-record paths.

### Gap 6 — Pre-build approvals remain unresolved

AMC Stage 5, 5a, 6, and 7 are produced but approval-pending. Stage 8 remains blocked until the necessary CS2 dispositions are recorded.

Required action:

- Record CS2 disposition for Stage 5 Architecture.
- Record CS2 disposition for Stage 5a Deployment Execution Strategy.
- Record CS2 disposition for Stage 6 QA-to-Red.
- Record CS2 disposition for Stage 7 PBFAG.
- Update `modules/amc/BUILD_PROGRESS_TRACKER.md`.
- Update `modules/amc/AMC_PRE_BUILD_ARTIFACT_INDEX.md`.

### Gap 7 — Build-to-green chain not ready

AMC has QA-to-red artifacts, but it does not yet have the current Stage 8/9/10/11 build chain.

Required action:

- Create Stage 8 Implementation Plan.
- Create Stage 8 Wave Breakdown.
- Create Stage 9 Builder Checklist.
- Create Stage 9 Builder Readiness Attestations.
- Create canonical IAA pre-brief wave record.
- Create Builder Appointment / Builder Contract.
- Then appoint builders to build to green.

---

## 6. Recommended PR sequence

### PR 1 — Strategy embed and Foreman operating model

Purpose: preserve context and anchor AMC to Johan's current operating model.

Artifacts:

```text
ISMS_AMC_REPO_ALIGNMENT.md
FOREMAN_OPERATING_MODEL.md
```

Status: started by this commit.

### PR 2 — Gate/admin alignment to ISMS PR #1800

Purpose: layer down the actual governance enforcement model.

Expected artifacts:

```text
.agent-admin/control/schemas/**
.agent-admin/control/protocols/**
.agent-admin/control/overlays/**
.agent-admin/control/templates/**
.agent-admin/control/checklists/**
.agent-admin/control/merge-gate-required-checks.json
.github/scripts/*gate*.js
.github/workflows/*gate*.yml
.github/workflows/iaa-prebrief-contract-alignment.yml
.github/workflows/governance-watchdog.yml
```

Exit condition: gate stack passes in AMC and no stale admin-loop behavior remains.

### PR 3 — IAA / wave-record contract migration

Purpose: eliminate old standalone prebrief confusion.

Expected artifacts:

```text
canonical AMC wave-record protocol
IAA_PREFLIGHT_BRIEF schema/protocol
supersession note for old iaa-prebrief-* artifacts
tracker/index updates for Stage 10
IAA prebrief alignment workflow
```

Exit condition: no active guidance tells agents to create standalone `iaa-prebrief-*` files.

### PR 4 — Pre-build closure / CS2 disposition PR

Purpose: resolve AMC's own tracker blockers.

Expected actions:

```text
Stage 5 approval or condition record
Stage 5a approval or condition record
Stage 6 QA-to-Red approval or condition record
Stage 7 PBFAG approval or condition record
updated BUILD_PROGRESS_TRACKER.md
updated AMC_PRE_BUILD_ARTIFACT_INDEX.md
```

Exit condition: Stage 8 becomes unblocked.

### PR 5 — Stage 8 / Stage 9 build planning PR

Purpose: create the implementation plan and builder checklist.

Expected artifacts:

```text
modules/amc/07-implementation-plan/implementation-plan.md
modules/amc/07-implementation-plan/wave-breakdown.md
modules/amc/08-builder-checklist/builder-checklist.md
modules/amc/08-builder-checklist/builder-readiness-attestations.md
canonical IAA pre-brief wave record
scope declaration
```

Exit condition: builder appointment can be issued.

### PR 6 — Builder appointment / build-to-green PR

Purpose: start build only after governance and pre-build readiness are in place.

Expected artifacts:

```text
builder appointment
builder contract
delegation-order evidence
implementation commits by builder
QA-to-green evidence
Foreman QP
ECAP admin bundle
IAA final assurance
handover only after gates pass
```

---

## 7. Build start rule

AMC build may start only when this rule is true:

```text
FOREMAN_OPERATING_MODEL.md exists
AND ISMS/PR1800 gate stack is aligned
AND IAA wave-record contract is canonical
AND Stage 5 / 5a / 6 / 7 blockers are resolved or explicitly dispositioned by CS2
AND Stage 8 Implementation Plan exists
AND Stage 9 Builder Checklist exists
AND canonical IAA pre-brief exists
AND Builder Appointment exists
```

Until then, any implementation work should be treated as premature.

---

## 8. Working conclusion

AMC is not a blank repo and should not be restarted from scratch. It has a valuable pre-build base. The next step is not build. The next step is controlled governance alignment so the same Foreman/Builder/ECAP/IAA model that is working in ISMS becomes the active operating model in AMC.

Once that alignment is complete, AMC can move into Stage 8/9 build planning and then into builder-led build-to-green execution.

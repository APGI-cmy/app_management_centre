# Execution Ceremony Admin Agent — Ceremony Bundle Checklist

**Agent**: execution-ceremony-admin-agent
**Version**: 1.0.0
**Last Updated**: 2026-04-14
**Authority**: CS2 (@APGI-cmy) — Issue #1075 | ECAP-001

---

## Purpose

Step-by-step checklist for preparing a complete ceremony bundle. Work through every item in order. Do not skip steps.

---

## PROHIBITED ARTIFACTS (Never Create These)

> ⚠️ **ABSOLUTE PROHIBITION** — CI-blocked per AMC 90/10 Admin Protocol v1.0.0:

| Path Pattern | Status | Replacement |
|---|---|---|
| `.agent-admin/assurance/iaa-token-*.md` | ❌ DEPRECATED / CI-BLOCKED | Wave record section 5 |
| `.agent-admin/assurance/iaa-prebrief-*.md` | ❌ DEPRECATED / CI-BLOCKED | Wave record section 1 |
| `.agent-admin/prehandover/PREHANDOVER_PROOF*.md` | ❌ DEPRECATED / CI-BLOCKED | Wave record section 3-4 |
| `.agent-admin/build-evidence/session-NNN/HANDOVER_SUMMARY.md` | ❌ DEPRECATED | Wave record |
| `.agent-admin/build-evidence/session-NNN/ALIGNMENT_EVIDENCE.md` | ❌ DEPRECATED | Wave record section 3 |
| `.agent-admin/build-evidence/session-NNN/RIPPLE_LOG.json` | ❌ DEPRECATED | Wave record section 2 |

---

## Stage 1 — Appointment Verification

- [ ] Confirm this session was initiated by Foreman appointment
- [ ] Extract `wave_id` from appointment
- [ ] Extract `artifact_scope` (list of artifacts produced)
- [ ] Extract `task_refs` (task reference list)
- [ ] Extract `expected_return` (what Foreman expects back)
- [ ] Confirm Foreman appointment is on the correct branch
- [ ] Output: `APPOINTMENT VERIFIED. Wave: [wave-id].`

---

## Stage 2 — Artifact Inventory

- [ ] List every artifact in `artifact_scope`
- [ ] For each artifact: confirm file exists at declared path
- [ ] For each artifact: note SHA or commit reference
- [ ] Identify any missing artifacts → escalate to Foreman immediately (HALT-001)
- [ ] Confirm all artifacts are committed to branch HEAD (`git status` clean for scope)
- [ ] Output: `ARTIFACT INVENTORY COMPLETE. [N] artifacts verified.`

---

## Stage 3 — Session Memory Preparation

- [ ] Determine session number (check `.agent-workspace/foreman-v2/memory/` for last session)
- [ ] Set file path: `.agent-workspace/foreman-v2/memory/session-NNN-YYYYMMDD.md`
- [ ] Populate mandatory fields — **none may be blank**:
  - [ ] `phase_1_preflight: PREFLIGHT COMPLETE` — mandatory CI gate field
  - [ ] `session_id: session-NNN-YYYYMMDD`
  - [ ] `wave_id: [wave-id from appointment]`
  - [ ] `date: YYYY-MM-DD`
  - [ ] `triggering_issue: [issue number and title]`
  - [ ] `outcome: [COMPLETE / PARTIAL / ESCALATED]`
  - [ ] `coverage_summary: [1-2 sentences describing what was delivered]`
  - [ ] `agents_delegated_to: [list from appointment]`
  - [ ] `learning: [key lesson — NEVER blank]`
  - [ ] `wave_record_path: [path to wave record]`
- [ ] Verify no field is blank or contains `N/A`, `TODO`, `TBD`, `PENDING`
- [ ] Output: `SESSION MEMORY DRAFTED. Path: [path].`

---

## Stage 4 — Wave Record Preparation (Sections 1-4)

> Section 5 (Assurance) is reserved for IAA. Pre-fill with PENDING.

- [ ] Load template: `.agent-admin/templates/amc-wave-record-template.md`
- [ ] Set file path: `.agent-admin/wave-records/amc-wave-record-{wave-id}-{YYYYMMDD}.md`
- [ ] **Section 1 — Wave Identity**: populate all fields from appointment
  - [ ] `wave_id`, `date`, `agent`, `session_id`, `branch`, `triggering_issue`, `cs2_authorization`
- [ ] **Section 2 — Scope & Classification**: 
  - [ ] `wave_verb`, `classification`, `architecture_ref`
  - [ ] `allowed_artifact_paths`: list ALL files created/modified in this wave
- [ ] **Section 3 — Evaluation Summary**:
  - [ ] Populate from builder evidence (tests GREEN, zero debt, architecture followed, etc.)
  - [ ] `QP Verdict: PASS / FAIL` — transcribe from builder/Foreman evidence; do NOT fabricate
  - [ ] If QP evidence not available: note gap and escalate to Foreman (ESC-001)
- [ ] **Section 4 — Outcome & Learning**:
  - [ ] `outcome`: from appointment context
  - [ ] `coverage_summary`: 1-2 sentences
  - [ ] `learning`: key lesson — NEVER blank
- [ ] **Section 5 — Assurance (PRE-FILL only)**:
  - [ ] `iaa_verdict: PENDING`
  - [ ] `iaa_token_ref: PENDING`
  - [ ] `merge_gate_parity: PENDING`
  - [ ] Add line: `PHASE_B_BLOCKING_TOKEN: PENDING`
  - [ ] Note: IAA will update section 5 — ceremony-admin does NOT write the final token
- [ ] Verify no mandatory section field is blank
- [ ] Output: `WAVE RECORD DRAFTED (sections 1-4). Path: [path].`

---

## Stage 5 — Commit-State Verification

- [ ] Run `git status` — confirm working tree clean for wave artifacts
- [ ] Run `git ls-tree HEAD -- [artifact paths]` — confirm all artifacts at HEAD
- [ ] Confirm session memory is committed at HEAD
- [ ] Confirm wave record (sections 1-4) is committed at HEAD
- [ ] Confirm all builder artifacts are committed at HEAD
- [ ] If anything is not committed: commit now before returning bundle
- [ ] Output: `COMMIT-STATE VERIFIED. All artifacts at HEAD.`

---

## Stage 6 — Bundle Hygiene Checks

- [ ] No `STUB`, `TODO`, `FIXME`, `TBD` in any mandatory field
- [ ] No deprecated path references in wave record (no `iaa-token-*.md`, `PREHANDOVER_PROOF*.md`)
- [ ] Wave record section 5 pre-filled with PENDING (not blank)
- [ ] Session memory `learning` field is non-blank and substantive
- [ ] All artifact paths in section 2 are real file paths (not examples or placeholders)
- [ ] Bundle character count reasonable (wave record < 10,000 chars recommended)
- [ ] Output: `BUNDLE HYGIENE: [PASS / ISSUES — [list]]`

---

## Stage 7 — Return-to-Foreman Documentation

- [ ] Compile bundle summary:
  - Session memory path
  - Wave record path
  - Artifact count
  - Any escalations / residual issues
- [ ] Output return statement (Phase 4 Step 4.3 format)
- [ ] Confirm: ceremony-admin role complete — Foreman takes over for IAA invocation
- [ ] Do NOT invoke IAA
- [ ] Do NOT open PR

---

## Quick Reference — AMC 90/10 Wave Record Model

```
Wave Record: .agent-admin/wave-records/amc-wave-record-{wave-slug}-{YYYYMMDD}.md
Session Memory: .agent-workspace/foreman-v2/memory/session-NNN-YYYYMMDD.md

Section 5 populated by IAA (not ceremony-admin):
  PHASE_B_BLOCKING_TOKEN: IAA-[session-ID]-[date]-PASS
```

---

**Authority**: ECAP-001 | AMC 90/10 Admin Protocol v1.0.0
**Knowledge Version**: 1.0.0 | **Last Updated**: 2026-04-14

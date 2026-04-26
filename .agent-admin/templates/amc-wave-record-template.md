# AMC Wave Record — [wave-slug] — [YYYY-MM-DD]

> **Template Version**: 1.2.0
> **Authority**: CS2 (@APGI-cmy) — Issue #1063
> **Protocol**: AMC 90/10 Admin Protocol v1.0.0
> **Amended**: 2026-04-24 — v1.2.0: Added §3b Ceremony Evidence Fields section with all 7 GIPC-001 §6.1 labeled fields as explicit rows; replaced evaluation-row representation with canonical labeled-field structure for unambiguous A-038 validation. Authority: CS2 — Issue #1129.
> **Amended**: 2026-04-23 — v1.1.0: Added Governing Authority table (GIPC-001 §3.3) and parity/overshadow check fields in Evaluation Summary (GIPC-001 §2.4, §5.3, §6.1). Authority: CS2 — Issue #1129.

---

## 1. Wave Identity

| Field | Value |
|-------|-------|
| wave_id | [wave-slug] |
| date | [YYYY-MM-DD] |
| agent | [agent-id] |
| session_id | [session-NNN] |
| branch | [branch-name] |
| triggering_issue | [#NNN — title] |
| cs2_authorization | [source — issue/comment link] |
| agents_delegated_to | [list of agent IDs and their role] |

## 1a. Governing Authority

> **Required per GIPC-001 §3.3** — populate at wave kickoff; do NOT change during the wave
> unless an explicit CS2-documented supersession occurs.

| Field | Value |
|-------|-------|
| governing_stage_issue | [#NNN — the Stage Kickoff Issue that authorized this wave] |
| triggering_wave_issue | [#NNN — same as governing_stage_issue unless explicitly superseded] |
| current_stage | [Stage N — Name, or N/A for non-stage governance waves] |
| next_stage_blocked_by | [blocker description, or N/A] |
| approval_reference | [blank until approval is formally recorded — do NOT pre-populate] |
| related_hardening_issue | [#NNN or N/A — for traceability only, not governing authority] |
| related_harmonization_issue | [#NNN or N/A — for traceability only, not governing authority] |
| approval_exists | [YES / NO / PENDING] |

## 2. Scope & Classification

| Field | Value |
|-------|-------|
| wave_verb | [verb from request] |
| classification | [POLC-Orchestration / Implementation Guard / Quality Professor] |
| architecture_ref | [path to frozen architecture, or N/A] |
| allowed_artifact_paths | [list of paths this wave may create/modify] |

## 3. Evaluation Summary

| Check | Result |
|-------|--------|
| Tests 100% GREEN | [✅ / ❌ — detail] |
| Zero skipped/stub tests | [✅ / ❌] |
| Zero test debt | [✅ / ❌] |
| Architecture followed | [✅ / ❌] |
| Zero deprecation warnings | [✅ / ❌] |
| Zero linter warnings | [✅ / ❌] |

**QP Verdict**: [PASS / FAIL]

## 3a. Governing-Issue Parity Evidence

> **Required per GIPC-001 §2.4** — complete before QP PASS; copy into PREHANDOVER proof.

```
governing_issue_parity_check:
  governing_stage_issue: "#NNN"
  surfaces_verified:
    - pr_body: [PASS / FAIL]
    - wave_record_triggering_issue: [PASS / FAIL]
    - wave_checklist_authority: [PASS / FAIL]
    - main_artifact_header: [PASS / FAIL / N/A]
    - traceability_artifact_header: [PASS / FAIL / N/A]
    - build_progress_tracker: [PASS / FAIL / N/A]
    - artifact_index: [PASS / FAIL / N/A]
    - sign_off_record: [PASS / FAIL / N/A]
    - prehandover_proof: [PASS / FAIL]
    - session_memory: [PASS / FAIL]
  parity_verdict: [PASS / FAIL]
  overshadow_detected: [NO / YES — issue number that was incorrectly used]
control_surfaces_updated:
  build_progress_tracker: [UPDATED / NOT_APPLICABLE — reason]
  artifact_index: [UPDATED / NOT_APPLICABLE — reason]
  sign_off_record: [UPDATED / NOT_APPLICABLE — reason]
```

## 3b. Ceremony Evidence Fields

> **Required per GIPC-001 §6.1 and A-038** — all 7 fields MUST be populated before QP PASS.
> A ceremony package with any field blank is a handover blocker (GIP-CEREMONY-INCOMPLETE).

| Field | Value |
|-------|-------|
| governing_stage_issue | [#NNN — must match triggering_issue in §1 and governing_stage_issue in §1a] |
| related_hardening_issue | [#NNN or N/A] |
| related_harmonization_issue | [#NNN or N/A] |
| approval_exists | [YES / NO / PENDING] |
| parity_check_performed | [PASS / FAIL / N/A — result of §3a parity check] |
| overshadow_check_performed | [CLEAN / DETECTED / N/A — result of §3a overshadow check] |
| control_surfaces_verified | [YES / N/A — whether tracker/artifact-index/sign-off were checked for parity] |

## 4. Outcome & Learning

| Field | Value |
|-------|-------|
| outcome | [COMPLETE / PARTIAL / ESCALATED] |
| coverage_summary | [what was delivered — 1-2 sentences] |
| learning | [key lesson — mandatory, never blank] |

## 5. Assurance

| Field | Value |
|-------|-------|
| iaa_verdict | [PASS / STOP-AND-FIX / ESCALATE / N/A] |
| iaa_token_ref | [token reference, or N/A] |
| merge_gate_parity | [PASS / FAIL] |

## 6. Failure Trail (if applicable)

> Only populate if QP FAIL, IAA STOP-AND-FIX, or merge gate failure occurred.
> This section replaces the legacy standalone rejection/failure files.

- **Failure type**: [QP FAIL / IAA STOP-AND-FIX / MERGE GATE FAIL]
- **Details**: [specific failures]
- **Remediation**: [actions taken]
- **Resolution**: [RESOLVED / PENDING]

---

**Filed by**: [agent-id] | **Date**: [YYYY-MM-DD]

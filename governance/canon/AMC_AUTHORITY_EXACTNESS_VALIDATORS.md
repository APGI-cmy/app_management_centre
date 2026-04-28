**Status**: CANONICAL | **Version**: 1.0.0 | **Authority**: CS2
**Date**: 2026-04-28
**Canon ID**: AAEV-001
**Issue**: app_management_centre — Umbrella: Upgrade AMC PR handover assurance to ISMS-level evidence-first protected-path scrutiny (Child 3)

> **Amendment Authority**: Only CS2 (Johan Ras / repo owner) may amend this canon.
> Any PR modifying this file without CS2 sign-off is auto-FAIL at the merge gate.

---

# AMC Authority Exactness Validators

## Purpose

This canon defines **machine-checkable field-level authority validators** for AMC artifact
surfaces. It is modeled on ISMS ISSUE-MISMATCH hardening but adapted to AMC's wave record,
PR body, tracker, index, session memory, and artifact header model.

The validators close the gap where authority-bearing fields across AMC artifacts contain
stale, missing, malformed, or mismatched governing issue references — and where PR body,
wave record, tracker, artifact index, session memory, and artifact headers disagree on core
authority facts.

This canon builds on and does not replace:
- `GOVERNING_ISSUE_PARITY_PROTOCOL.md` (GIPC-001)
- `END_OF_WAVE_CLOSEOUT_SWEEP_CANON.md` (EWCS-001)
- `PR_HANDOVER_CANONICAL_PACKAGE.md` (PHCP-001)
- `WAVE_RESULT_COHERENCE_CANON.md` (WRCC-001)

---

## 1. Validator Overview

AMC authority exactness validators are **machine-checkable rules** that can be evaluated
by scripts, CI checks, or IAA/ECAP without subjective interpretation.

Each validator has:
- A **Validator ID** (AAEV-NNN)
- The **surface** it checks (wave record, PR body, etc.)
- The **field** it checks
- The **exact match rule** (what it compares and what constitutes a match)
- The **failure class** triggered on mismatch

---

## 2. Core Authority Validators

### AAEV-001: Governing Issue Cross-Surface Match

**Surface**: All authority-bearing surfaces
**Rule**: The governing delivery issue number MUST be identical across all of the following surfaces. A single character difference (including leading `#`, different issue format, or stale issue number) is a match FAILURE.

| Surface | Field | Expected Value |
|---------|-------|----------------|
| Wave record §1 | `triggering_issue` | `#NNN` — governing delivery issue |
| Wave record §1 | `governing_stage_issue` (if present) | `#NNN` — same issue |
| Wave checklist | Authority line (e.g., `Authority: CS2 — Issue #NNN`) | `#NNN` — same issue |
| PR body | `governing_delivery_issue` field | `#NNN` — same issue |
| Main stage artifact header | `governing_stage_issue` or authority citation | `#NNN` — same issue |
| Session memory | `triggering_issue` field | `#NNN` — same issue |
| ECAP reconciliation summary | Governing issue reference | `#NNN` — same issue |
| Build progress tracker header | `Issue:` field | `#NNN` — same issue |

**Machine check**:
```bash
# Extract governing issue from wave record (canonical source)
GOVERNING=$(grep -m1 "triggering_issue" .agent-admin/wave-records/amc-wave-record-*.md | grep -oP '#\d+')

# Verify each surface
for f in .agent-admin/waves/*-current-tasks.md .agent-admin/prehandover/ecap-reconciliation-*.md; do
  FOUND=$(grep -oP '#\d+' "$f" | head -1)
  [ "$FOUND" != "$GOVERNING" ] && echo "MISMATCH: $f declares $FOUND, expected $GOVERNING"
done
```

**Failure class**: AAEV-ISSUE-MISMATCH

---

### AAEV-002: PHASE_B_BLOCKING_TOKEN Format Validator

**Surface**: Wave record §5
**Rule**: The `PHASE_B_BLOCKING_TOKEN` field MUST match the exact canonical format:
`PHASE_B_BLOCKING_TOKEN: IAA-[session-ID]-[date]-PASS`

Where:
- `[session-ID]` is a non-empty alphanumeric identifier
- `[date]` matches `YYYYMMDD` format
- The token ends with `-PASS` (not `-PENDING`, `-FAIL`, or any other suffix)

**Machine check**:
```bash
TOKEN=$(grep "PHASE_B_BLOCKING_TOKEN:" .agent-admin/wave-records/amc-wave-record-*.md | tail -1)
echo "$TOKEN" | grep -qP "PHASE_B_BLOCKING_TOKEN:\s+IAA-[A-Za-z0-9_-]+-\d{8}-PASS$" \
  && echo "TOKEN: VALID" || echo "TOKEN: INVALID or ABSENT — $TOKEN"
```

**Failure class**: AAEV-TOKEN-MALFORMED

---

### AAEV-003: Wave Record Section Completeness Validator

**Surface**: Wave record
**Rule**: Sections 1 through 5 MUST all be present and non-blank. The following section
markers MUST appear in the wave record in order:

```
## Section 1 — Wave Identity
## Section 2 — IAA Pre-Brief
## Section 3 — Evidence and Gate Results
## Section 4 — Foreman QP Admin-Compliance Checkpoint
## Section 5 — Assurance Token
```

Each section header MUST be followed by at least one non-blank line of content.

**Machine check**:
```bash
for SECTION in "Section 1" "Section 2" "Section 3" "Section 4" "Section 5"; do
  grep -q "## ${SECTION}" .agent-admin/wave-records/amc-wave-record-*.md \
    && echo "PRESENT: $SECTION" || echo "MISSING: $SECTION"
done
```

**Failure class**: AAEV-WAVE-RECORD-INCOMPLETE

---

### AAEV-004: PR Body Mandatory Field Completeness

**Surface**: PR body
**Rule**: All mandatory fields defined in `PR_HANDOVER_CANONICAL_PACKAGE.md` §1.1 MUST be
present in the PR body and non-blank/non-placeholder. Specifically:

| Field | Valid State | Invalid States |
|-------|-------------|----------------|
| `governing_delivery_issue` | `#NNN — [title]` | blank, `N/A`, `TBD`, placeholder text |
| `wave_record_path` | `.agent-admin/wave-records/amc-wave-record-*.md` pattern | blank, generic path, `TBD` |
| `qp_verdict` | `PASS` | blank, `PENDING`, `TBD`, any non-PASS value |
| `iaa_result` | `PHASE_B_BLOCKING_TOKEN: IAA-*-PASS` | blank, `PENDING`, `N/A`, generic text |
| `parity_check_verdict` | `PASS` | blank, `PENDING`, any non-PASS value |
| `closeout_sweep_verdict` | `PASS` | blank, `PENDING`, any non-PASS value |
| `pre_pr_blocking_gate` | `PASS` | blank, `PENDING`, any non-PASS value |
| `wave_checklist_status` | `ALL TICKED` or documented exceptions | blank, `PENDING`, `IN PROGRESS` |

**Machine check** (CI automation pattern):
```bash
# Extract PR body and check mandatory fields
PR_BODY=$(gh pr view $PR_NUMBER --json body -q '.body')

check_field() {
  local FIELD=$1; local VALID_PATTERN=$2
  VALUE=$(echo "$PR_BODY" | grep -oP "(?<=\| $FIELD \| ).*(?= \|)" | head -1 | xargs)
  echo "$VALUE" | grep -qP "$VALID_PATTERN" \
    && echo "VALID: $FIELD = $VALUE" \
    || echo "INVALID: $FIELD = '$VALUE' (expected pattern: $VALID_PATTERN)"
}

check_field "governing_delivery_issue" '#\d+'
check_field "qp_verdict" '^PASS$'
check_field "parity_check_verdict" '^PASS$'
check_field "pre_pr_blocking_gate" '^PASS$'
```

**Failure class**: AAEV-PR-BODY-FIELD-INVALID

---

### AAEV-005: Wave Record / Session Memory Consistency

**Surface**: Wave record §1 ↔ Session memory
**Rule**: The following fields MUST match exactly between the wave record and the session memory:

| Wave Record Field | Session Memory Field | Must Match |
|------------------|---------------------|------------|
| `wave_id` | `wave_id` | Exact string match |
| `triggering_issue` | `triggering_issue` | Exact issue number match (e.g., `#1234`) |
| `wave_record_path` | `wave_record_path` | Exact file path match |

**Machine check**:
```bash
WAVE_ID_WR=$(grep "wave_id" .agent-admin/wave-records/amc-wave-record-*.md | head -1 | grep -oP '(?<=: ).*')
WAVE_ID_SM=$(grep "wave_id" .agent-workspace/foreman-v2/memory/session-*.md | tail -1 | grep -oP '(?<=: ).*')
[ "$WAVE_ID_WR" = "$WAVE_ID_SM" ] && echo "WAVE_ID: MATCH" || echo "WAVE_ID: MISMATCH — WR=$WAVE_ID_WR SM=$WAVE_ID_SM"
```

**Failure class**: AAEV-WAVE-SESSION-MISMATCH

---

### AAEV-006: Artifact Header Authority Field Validator

**Surface**: Stage artifact headers
**Rule**: Any artifact that carries an authority declaration in its header MUST use the
canonical labeled field format (per GIPC-001 §3.1). Free-form authority lines are not
sufficient for artifacts produced from GIPC-001 enforcement date onwards.

Required labeled fields in artifact headers:
- `governing_stage_issue: #NNN` — MANDATORY, never blank
- `triggering_wave_issue: #NNN` — MANDATORY, same as governing_stage_issue unless explicit supersession

**Machine check**:
```bash
# Check that authority-bearing artifact headers use labeled fields
for f in $(git diff --name-only HEAD~1 | grep -E "\.md$" | grep -v ".agent-admin" | grep -v ".agent-workspace"); do
  if grep -q "Authority" "$f" && ! grep -q "governing_stage_issue:" "$f"; then
    echo "UNLABELED_AUTHORITY: $f lacks governing_stage_issue: field"
  fi
done
```

**Failure class**: AAEV-UNLABELED-AUTHORITY

---

### AAEV-007: Tracker / Index Governing Issue Match

**Surface**: Build progress tracker ↔ Artifact index ↔ Wave record
**Rule**: The governing issue reference in the build progress tracker header (`Issue:` field),
the artifact index governing issue citation, and the wave record `triggering_issue` MUST
all be identical.

**Machine check**:
```bash
TRACKER_ISSUE=$(grep "^Issue:" BUILD_PROGRESS_TRACKER*.md 2>/dev/null | grep -oP '#\d+' | head -1)
WAVE_ISSUE=$(grep "triggering_issue" .agent-admin/wave-records/amc-wave-record-*.md | grep -oP '#\d+' | head -1)
[ "$TRACKER_ISSUE" = "$WAVE_ISSUE" ] \
  && echo "TRACKER/WAVE: MATCH ($TRACKER_ISSUE)" \
  || echo "TRACKER/WAVE: MISMATCH — Tracker=$TRACKER_ISSUE Wave=$WAVE_ISSUE"
```

**Failure class**: AAEV-TRACKER-MISMATCH

---

### AAEV-008: Pre-PR Blocking Gate YAML Completeness

**Surface**: Wave record §3c `pre_pr_blocking_gate` YAML block
**Rule**: The `pre_pr_blocking_gate` fenced YAML block MUST be present in wave record §3c
and ALL sub-fields defined in PHCP-001 §4.1 MUST be populated with non-placeholder values.
The `pre_pr_blocking_gate_verdict` field MUST be `PASS`.

Additional PPEIA-001 and EFIA-001 fields required when applicable:

```yaml
# Required for all waves (PHCP-001 §4.1 base set + PPEIA-001/EFIA-001 additions):
pre_pr_blocking_gate:
  closeout_sweep_performed: "YES"
  tracker_header_parity_verified: "PASS | N/A"
  tracker_body_parity_verified: "PASS | N/A"
  wave_checklist_retired_from_kickoff_state: "YES"
  control_surfaces_finalized: "YES"
  handover_bundle_self_consistent: "YES"
  governing_issue_role_registry_completed: "YES"
  stale_injector_check_performed: "CLEAN"
  entry_condition_status: "NORMAL | EXCEPTION"
  operational_sanity_check_performed: "YES | N/A"
  # PPEIA-001 field (required for protected-path PRs):
  protected_path_ecap_ceremony_completed: "YES | N/A | WAIVED"
  # EFIA-001 fields:
  ac_evidence_matrix_populated: "YES | N/A"
  evidence_type_downgrade_check: "CLEAN"
  pre_pr_blocking_gate_verdict: "PASS"
```

**Machine check**:
```bash
VERDICT=$(grep "pre_pr_blocking_gate_verdict:" .agent-admin/wave-records/amc-wave-record-*.md | grep -oP 'PASS|FAIL')
[ "$VERDICT" = "PASS" ] && echo "PRE_PR_GATE: PASS" || echo "PRE_PR_GATE: FAIL or ABSENT"
```

**Failure class**: AAEV-PRE-PR-GATE-INCOMPLETE

---

### AAEV-009: Session Memory Mandatory Field Completeness

**Surface**: Session memory
**Rule**: All mandatory session memory fields (6-field model per AMC 90/10) MUST be populated
with non-blank, non-placeholder values:

| Field | Valid State | Invalid States |
|-------|-------------|----------------|
| `session_id` | Non-empty alphanumeric identifier | blank, `TBD`, `[fill in]` |
| `wave_id` | Non-empty wave identifier | blank, `TBD` |
| `date` | `YYYY-MM-DD` format | blank, relative dates |
| `triggering_issue` | `#NNN` format | blank, non-issue text |
| `outcome` | Non-empty result description | blank, `TBD`, `PENDING` |
| `wave_record_path` | Valid file path | blank, `TBD` |
| `phase_1_preflight` | `PREFLIGHT COMPLETE` (exact text) | blank, any other text |
| `learning` | Non-empty learning note | blank, `N/A`, single-word entry |

**Failure class**: AAEV-SESSION-MEMORY-INCOMPLETE

---

## 3. Validator Execution Context

### 3.1 Who Runs the Validators

| Validator | Minimum Execution Context |
|-----------|--------------------------|
| AAEV-001 | ECAP (before handback to Foreman) + IAA (as part of audit) |
| AAEV-002 | IAA (token format verification before PASS) |
| AAEV-003 | ECAP (completeness check) + Foreman §14.6 checkpoint |
| AAEV-004 | CI (automated PR body check) + IAA |
| AAEV-005 | ECAP (cross-artifact reconciliation per ECAP-001 §3.7) |
| AAEV-006 | Foreman QP (pre-handover check) + IAA |
| AAEV-007 | ECAP + IAA |
| AAEV-008 | Foreman §14.6 checkpoint + IAA |
| AAEV-009 | ECAP + Foreman §14.6 checkpoint |

### 3.2 Validator Failure = Wave Blocker

A failure in ANY AAEV validator is a **wave blocker**. It is not a post-merge cleanup item.
The validator failure must be resolved and the relevant check re-run before the wave may
proceed to the next stage.

### 3.3 Validator Results Recording

ECAP MUST record validator results in the reconciliation summary:

```yaml
aaev_validator_results:
  AAEV-001_governing_issue_cross_surface: "PASS | FAIL — [mismatch details]"
  AAEV-002_token_format: "PASS | FAIL — [token found]"
  AAEV-003_wave_record_completeness: "PASS | FAIL — [missing sections]"
  AAEV-004_pr_body_fields: "PASS | FAIL — [invalid fields]"
  AAEV-005_wave_session_consistency: "PASS | FAIL — [mismatch fields]"
  AAEV-006_artifact_header_authority: "PASS | FAIL | N/A — [unlabeled artifacts]"
  AAEV-007_tracker_index_match: "PASS | FAIL | N/A — [mismatch details]"
  AAEV-008_pre_pr_gate_completeness: "PASS | FAIL — [missing fields]"
  AAEV-009_session_memory_completeness: "PASS | FAIL — [missing fields]"
  aaev_overall_verdict: "PASS | FAIL — PASS only if all applicable validators show PASS"
```

IAA MUST verify `aaev_overall_verdict: PASS` before issuing an ASSURANCE-TOKEN.

---

## 4. Failure Classes

| Failure Class | Validator | Description |
|--------------|-----------|-------------|
| AAEV-ISSUE-MISMATCH | AAEV-001 | Governing issue number differs across authority-bearing surfaces |
| AAEV-TOKEN-MALFORMED | AAEV-002 | PHASE_B_BLOCKING_TOKEN absent or does not match canonical format |
| AAEV-WAVE-RECORD-INCOMPLETE | AAEV-003 | Wave record missing one or more required sections (1-5) |
| AAEV-PR-BODY-FIELD-INVALID | AAEV-004 | PR body mandatory field blank, placeholder, or non-PASS when PASS required |
| AAEV-WAVE-SESSION-MISMATCH | AAEV-005 | Wave record and session memory disagree on wave_id, triggering_issue, or wave_record_path |
| AAEV-UNLABELED-AUTHORITY | AAEV-006 | Artifact header uses free-form authority line instead of labeled `governing_stage_issue:` field |
| AAEV-TRACKER-MISMATCH | AAEV-007 | Tracker/index governing issue does not match wave record triggering_issue |
| AAEV-PRE-PR-GATE-INCOMPLETE | AAEV-008 | Pre-PR blocking gate YAML block missing, incomplete, or `pre_pr_blocking_gate_verdict ≠ PASS` |
| AAEV-SESSION-MEMORY-INCOMPLETE | AAEV-009 | Session memory missing mandatory fields or contains placeholder values |

---

## 5. Integration Requirements

### 5.1 GIPC-001 Alignment

AAEV-001 (governing issue cross-surface match) is aligned with GIPC-001 §2.2 (Mandatory
Governing-Issue Parity Check). AAEV-001 is the machine-checkable implementation layer for
the human-readable rules in GIPC-001. They are not alternatives — both must pass.

### 5.2 PHCP-001 Alignment

AAEV-004 (PR body mandatory field completeness) and AAEV-008 (pre-PR blocking gate YAML
completeness) are machine-checkable implementations of PHCP-001 §1.1 and §4.1 respectively.

### 5.3 WRCC-001 Alignment

WRCC-001 §3 treats any AAEV validator failure as a wave-result coherence failure. A wave
cannot declare COMPLETE state if AAEV validators have not been run and passed.

### 5.4 IAA Canon Alignment

IAA MUST check `aaev_overall_verdict: PASS` in the ECAP reconciliation summary as a
prerequisite for issuing an ASSURANCE-TOKEN (ACR-24, added to IAA canon v1.12.0).

---

## Appendix A: AAEV Validator Quick Reference Card

```
Before wave close / QP PASS, verify all AAEV validators:
✅ AAEV-001: governing issue #NNN consistent across all surfaces
✅ AAEV-002: PHASE_B_BLOCKING_TOKEN format: IAA-[id]-[date]-PASS
✅ AAEV-003: wave record sections 1-5 all present and populated
✅ AAEV-004: all PR body mandatory fields = PASS (not blank or PENDING)
✅ AAEV-005: wave_id and triggering_issue match between wave record and session memory
✅ AAEV-006: artifact headers use labeled governing_stage_issue: field
✅ AAEV-007: tracker Issue: field = wave record triggering_issue
✅ AAEV-008: pre_pr_blocking_gate YAML block complete and verdict = PASS
✅ AAEV-009: session memory all mandatory fields populated (non-blank, non-placeholder)
→ Record aaev_overall_verdict: PASS in ECAP reconciliation summary before invoking IAA.
```

---

**Canon ID**: AAEV-001
**Filed by**: foreman-v2-agent (POLC-Orchestration governance specification) | **Date**: 2026-04-28
**Authority**: CS2 — Umbrella: Upgrade AMC PR handover assurance to ISMS-level evidence-first protected-path scrutiny
**See also**: PPEIA-001, EFIA-001, WRCC-001, GIPC-001, PHCP-001, EWCS-001, ECAP-001

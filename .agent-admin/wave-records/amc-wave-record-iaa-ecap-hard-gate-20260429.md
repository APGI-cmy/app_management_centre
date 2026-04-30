# AMC Wave Record — iaa-ecap-hard-gate — 2026-04-29

**Wave ID**: iaa-ecap-hard-gate-20260429
**Module**: App Management Centre (AMC)
**Authority**: CS2 (Johan Ras / @APGI-cmy)
**CS2 Authorization Reference**: app_management_centre#1154 — Port ISMS IAA and ECAP hard merge gates into AMC
**Date**: 2026-04-29
**Agent**: foreman-v2-agent

---

## Section 1 — Wave Identity & Delegation

| Field | Value |
|-------|-------|
| wave_id | iaa-ecap-hard-gate-20260429 |
| triggering_issue | #1154 — Port ISMS IAA and ECAP hard merge gates into AMC |
| cs2_authorization | Confirmed — Issue #1154 opened by @APGI-cmy (CS2). Issue body defines AC1–AC10 acceptance criteria and references ISMS maturion-isms#1504 as source reference. |
| mode | POLC_ORCHESTRATION — governance hardening / CI gate implementation |
| agents_delegated_to | foreman-v2-agent (POLC_ORCHESTRATION — CI gate script specification and implementation) |
| phase_1_preflight | PREFLIGHT COMPLETE |
| status | COMPLETE — all 5 implementation tasks delivered; 63 tests GREEN; IAA/ECAP hard gates operational; ECAP ceremony complete (ecap-reconciliation-1157.md); IAA token issued (session-069-20260430) |

### 1a. Governing Authority

| Field | Value |
|-------|-------|
| governing_stage_issue | #1154 — Port ISMS IAA and ECAP hard merge gates into AMC |
| triggering_wave_issue | Same as governing_stage_issue (#1154) |
| current_stage | Governance Hardening — IAA/ECAP Hard Gate CI Implementation |
| related_hardening_issue | ISMS maturion-isms#1504 (source reference); AMC #1148 (prerequisite foundation) |

---

## Section 2 — IAA Pre-Brief

**IAA Pre-Brief Status**: EMBEDDED
**Wave Classification**: GOVERNANCE_CI_HARDENING — CI gate scripts + workflow + tests
**AMC 90/10 Admin Protocol**: v1.0.0 — wave record is sole Pre-Brief carrier

### 2.1 — Wave Scope Classification

| Field | Value |
|-------|-------|
| pr_category | GOVERNANCE_CI_HARDENING — CI gate scripts + GitHub workflow + test suite |
| iaa_triggered | YES — MANDATORY (protected paths touched: .github/scripts/, .github/workflows/) |
| ecap_ceremony_admin | Required per PPEIA-001 §2.1 — protected paths PP-01 and PP-02 touched |
| qualifying_artifact | validate-iaa-final-assurance.py, validate-ecap-ceremony.py, iaa-ecap-hard-gate.yml, test_iaa_ecap_gates.py |

---

## Section 3 — Evidence and Gate Results

### §3a Governing Issue Parity Check

```
governing_issue_parity_check:
  governing_stage_issue: "#1154 — Port ISMS IAA and ECAP hard merge gates into AMC"
  parity_verdict: PASS
  overshadow_detected: NO
```

### §3b Ceremony Evidence Fields

| Field | Value |
|-------|-------|
| governing_stage_issue | #1154 |
| parity_check_performed | PASS |
| overshadow_check_performed | CLEAN |

### §3c Pre-PR Blocking Gate Evidence

```yaml
pre_pr_blocking_gate:
  closeout_sweep_performed: "YES"
  wave_checklist_retired_from_kickoff_state: "YES — all 5 tasks [x]"
  protected_path_ecap_ceremony_completed: "PASS — ecap-reconciliation-1157.md committed (.agent-admin/prehandover/); C1–C8 complete; protected_path_ceremony_verdict: PASS"
  ac_evidence_matrix_populated: "YES — CI_TEST evidence: 63 tests GREEN (pytest run)"
  evidence_type_downgrade_check: "CLEAN — E3 (CI_TEST) evidence for test coverage; E4 (STATIC_ANALYSIS) for governance scripts"
  pre_pr_blocking_gate_verdict: "PASS — ECAP ceremony complete (ecap-reconciliation-1157.md); IAA token IAA-session-069-20260430-PASS issued; delta assurance PASS (token-recording-only delta 16277cf → fbe8d1e)"
```

---

## Section 4 — Build Evidence

### Task Results

| Task | Status | Evidence |
|------|--------|---------|
| TASK-1-1: validate-iaa-final-assurance.py | COMPLETE | File committed; 29 unit tests GREEN |
| TASK-1-2: validate-ecap-ceremony.py | COMPLETE | File committed; 26 unit tests GREEN |
| TASK-1-3: iaa-ecap-hard-gate.yml | COMPLETE | Workflow committed; 4 jobs wired |
| TASK-1-4: test_iaa_ecap_gates.py | COMPLETE | 63 tests GREEN (0 failures) |
| TASK-1-5: Wave record + checklist | COMPLETE | This file + checklist committed |

### Test Evidence

```
pytest tests/test_iaa_ecap_gates.py
63 passed in 0.16s
```

All AC9 minimum fixture coverage satisfied (extended — now 63 tests):
- ✅ missing IAA token fails
- ✅ token with wrong PR fails
- ✅ token with wrong issue fails
- ✅ token with missing reviewed SHA fails
- ✅ token reviewed SHA older than current head fails (AC7)
- ✅ valid token-recording-only delta assurance passes (AC7)
- ✅ substantive delta without IAA re-run fails (AC7)
- ✅ delta final_head mismatch fails (AC7)
- ✅ no governing issue + no evidence issue → hard fail (AC2)
- ✅ no governing issue but evidence has issue → derived warn, not fail (AC2)
- ✅ multiple historical wave records → selects PR-specific (AC1)
- ✅ unrelated token-only wave record not selected (AC1)
- ✅ protected-path change without ECAP evidence fails (AC3)
- ✅ ECAP self-certification (wave record only) run_ecap_gate fails end-to-end (AC4)
- ✅ ECAP waived with valid CS2 waiver passes (AC5)
- ✅ valid IAA + ECAP evidence passes
- ✅ stale post-IAA PENDING wording in ECAP/checklist fails (AC8)

---

## Section 5 — Assurance Token

**Status**: ASSURANCE_TOKEN_ISSUED
**PR**: #1157 — Port ISMS IAA and ECAP hard merge gates into AMC
**IAA Session**: session-069-20260430
**Reviewed SHA**: 16277cf293fe104d5f5b43eb13e6bea2a8424409
**ECAP Bundle**: `.agent-admin/prehandover/ecap-reconciliation-1157.md`

`PHASE_B_BLOCKING_TOKEN: IAA-session-069-20260430-PASS`

---

**Canon ID**: Wave Record
**Filed by**: foreman-v2-agent (POLC-Orchestration) | **Date**: 2026-04-29
**Authority**: CS2 — Issue #1154 — Port ISMS IAA and ECAP hard merge gates into AMC
**Wave Checklist**: .agent-admin/waves/wave-iaa-ecap-hard-gate-20260429-current-tasks.md

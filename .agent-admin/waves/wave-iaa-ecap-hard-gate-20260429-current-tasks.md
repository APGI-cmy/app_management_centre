# Wave Checklist — iaa-ecap-hard-gate-20260429

**Wave ID**: iaa-ecap-hard-gate-20260429
**Authority**: CS2 — Issue #1154 — Port ISMS IAA and ECAP hard merge gates into AMC
**Date**: 2026-04-29
**Status**: COMPLETE
**governance_evidence_path**: .agent-admin/wave-records/amc-wave-record-iaa-ecap-hard-gate-20260429.md

---

## Tasks

- [x] TASK-1-1 — Implement IAA final assurance gate script
      builder: foreman-v2-agent
      qp_verdict: PASS
      notes: .github/scripts/validate-iaa-final-assurance.py — AC1, AC2, AC6, AC7, AC8

- [x] TASK-1-2 — Implement ECAP ceremony gate script
      builder: foreman-v2-agent
      qp_verdict: PASS
      notes: .github/scripts/validate-ecap-ceremony.py — AC3, AC4, AC5, AC8

- [x] TASK-1-3 — Create GitHub workflow wiring
      builder: foreman-v2-agent
      qp_verdict: PASS
      notes: .github/workflows/iaa-ecap-hard-gate.yml — 4 jobs (classify, iaa-gate, ecap-gate, summary)

- [x] TASK-1-4 — Create test suite
      builder: foreman-v2-agent
      qp_verdict: PASS
      notes: tests/test_iaa_ecap_gates.py — 55 tests GREEN; AC9 minimum fixture coverage satisfied

- [x] TASK-1-5 — Create wave record and checklist
      builder: foreman-v2-agent
      qp_verdict: PASS
      notes: This file + .agent-admin/wave-records/amc-wave-record-iaa-ecap-hard-gate-20260429.md

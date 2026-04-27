# Wave Current Tasks — Stage 6 QA-to-Red

**Wave**: amc-stage6-qa-to-red-20260427
**Session**: session-034
**Date**: 2026-04-27
**Triggering Issue**: app_management_centre#1141
**CS2 Authorization**: @APGI-cmy (issue opener)
**Wave Purpose**: Produce Stage 6 QA-to-Red pack for AMC — qa-to-red-specification.md, architecture-and-des-to-qa-traceability.md, red-test-catalog.md; keep BUILD_PROGRESS_TRACKER.md and AMC_PRE_BUILD_ARTIFACT_INDEX.md aligned
**Gate Condition**: Stage 6 artifacts produced approval-pending. Stage 5 and Stage 5a CS2 approval required before Stage 6 execution proceeds to Stage 7 (PBFAG).

---

## Task List

- [ ] TASK-034-01 — Create `modules/amc/05-qa-to-red/qa-to-red-specification.md` v1.0
      builder: foreman-v2-agent (POLC_ORCHESTRATION — governance planning artifact)
      qp_verdict: PENDING
      notes: Core Stage 6 specification. Defines QA-to-Red purpose, scope, pass/fail philosophy, severity model, blocker classification, retest expectations, evidence expectations. Derived from Architecture v1.0 and DES v1.0.

- [ ] TASK-034-02 — Create `modules/amc/05-qa-to-red/architecture-and-des-to-qa-traceability.md` v1.0
      builder: foreman-v2-agent (POLC_ORCHESTRATION — governance planning artifact)
      qp_verdict: PENDING
      notes: Traceability matrix: Stage 5 Architecture commitments → Stage 6 red tests; Stage 5a DES fields (DES-001 through DES-008) → Stage 6 red tests. No critical family silently omitted. Deferred items disclosed.

- [ ] TASK-034-03 — Create `modules/amc/05-qa-to-red/red-test-catalog.md` v1.0
      builder: foreman-v2-agent (POLC_ORCHESTRATION — governance planning artifact)
      qp_verdict: PENDING
      notes: Full test catalog with test IDs, source requirement, scenario, fail condition, pass condition, severity, blocker classification, required evidence type.

- [ ] TASK-034-04 — Update `modules/amc/05-qa-to-red/qa-to-red-suite.md` (superseded notice)
      builder: foreman-v2-agent (POLC_ORCHESTRATION)
      qp_verdict: PENDING
      notes: Placeholder superseded by qa-to-red-specification.md

- [ ] TASK-034-05 — Update `modules/amc/05-qa-to-red/qa-catalog-alignment.md` (superseded notice)
      builder: foreman-v2-agent (POLC_ORCHESTRATION)
      qp_verdict: PENDING
      notes: Placeholder superseded by red-test-catalog.md and architecture-and-des-to-qa-traceability.md

- [ ] TASK-034-06 — Update `modules/amc/BUILD_PROGRESS_TRACKER.md`
      builder: foreman-v2-agent (POLC_ORCHESTRATION)
      qp_verdict: PENDING
      notes: Stage 6 status: produced approval-pending; Stage 7 remains blocked. Gate condition preserved.

- [ ] TASK-034-07 — Update `modules/amc/AMC_PRE_BUILD_ARTIFACT_INDEX.md`
      builder: foreman-v2-agent (POLC_ORCHESTRATION)
      qp_verdict: PENDING
      notes: Stage 6 artifacts cataloged with correct status (approval-pending). Gate condition preserved.

---

## IAA Pre-Brief Reference

Pre-Brief embedded in wave record section 2: `.agent-admin/wave-records/amc-wave-record-amc-stage6-qa-to-red-20260427.md`

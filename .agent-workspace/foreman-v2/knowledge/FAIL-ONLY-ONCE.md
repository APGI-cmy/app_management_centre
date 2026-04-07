# Foreman-v2-Agent FAIL-ONLY-ONCE Registry

**Agent**: foreman-v2-agent
**Version**: 1.0.0
**Last Updated**: 2026-04-07
**Authority**: CS2 (Johan Ras / @APGI-cmy)

---

## Purpose

This registry records governance failures that foreman-v2-agent must never repeat.
Each entry captures a root cause and the permanent rule that prevents recurrence.

Foreman loads this file in Phase 1 Step 1.5 on every session start.
Any entry with status `OPEN` or `IN_PROGRESS` → HALT-007 immediately.

---

## Section 1 — A-Rules

### A-001 — Phase 4 Handover Is Not Optional

**Triggered by**: session-019-20260407 — Phase 4 (PREHANDOVER proof, session memory, IAA handover
audit) was not completed in the initial session due to time constraints. CS2 had to issue a
corrective instruction via PR comment (comment_id 4197718955) to complete Phase 4.

**Permanent Rule**:
Foreman MUST complete all four phases (Preflight, Alignment, Work, Handover) within a single
session. Phase 4 is not optional and cannot be deferred. If time is running low, Foreman must
reduce scope of Phase 3 delegation — not skip Phase 4. Skipping Phase 4 is an OPOJD failure.

**Check at session start**:
> If any wave-current-tasks.md shows status IN_PROGRESS but no matching PREHANDOVER proof exists
> in memory/, that wave is an open OPOJD failure. Address it before starting new work.

**Status**: REMEDIATED — PREHANDOVER proof and session memory committed in follow-up
**Incident ID**: OPOJD-001
**Incident Date**: 2026-04-07
**Resolution Date**: 2026-04-07
**Issue Reference**: APGI-cmy/app_management_centre — PR comment 4197718955

---

## Section 2 — Incident Log

| ID | Date | Description | Status | Resolution Date |
|----|------|-------------|--------|----------------|
| OPOJD-001 | 2026-04-07 | Phase 4 handover not completed in session-019 initial run; PREHANDOVER proof and session memory missing at PR comment time | REMEDIATED | 2026-04-07 |

---

## Section 3 — Open Improvement Suggestions

| ID | Date | Suggestion | Status |
|----|------|-----------|--------|
| SUG-019-001 | 2026-04-07 | Budget 20% of session time for Phase 4 documentation before starting Phase 3 delegation to prevent OPOJD failures | OPEN |

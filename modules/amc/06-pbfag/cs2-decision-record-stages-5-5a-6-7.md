# AMC CS2 Decision Record - Stages 5, 5a, 6, and 7

**Module**: App Management Centre (AMC)  
**Document Type**: CS2 decision record  
**Decision Scope**: Stage 5 Architecture, Stage 5a Deployment Execution Strategy, Stage 6 QA-to-Red, Stage 7 PBFAG  
**Status**: CS2 decision recorded for PR review  
**Decision Authority**: CS2 - Johan Ras  
**Prepared By**: foreman-v2-agent as CS2 proxy  
**Date**: 2026-07-02  
**Related Issue**: app_management_centre#1197  
**Preceding PRs**: #1188, #1190, #1192, #1194  
**Non-scope**: This record does not begin Stage 8, create implementation work, create builder checklist, create IAA pre-brief, appoint builders, certify build-readiness, or start build.

---

## 1. Decision Context

PR #1194 merged the Stage 7 PBFAG retrofit and the CS2 disposition pack for AMC Stages 5, 5a, 6, and 7.

The tracker on `main` continued to require an explicit CS2 disposition before Stage 8 could be opened. This record provides that explicit CS2 disposition.

---

## 2. Authority Inputs Reviewed

This decision is based on the following approved or produced reference inputs:

1. Stage 5 Architecture canonical pack and Stage 5 retrofit artifacts from PR #1188.
2. Stage 5a Deployment Execution Strategy canonical pack and Stage 5a retrofit artifacts from PR #1190.
3. Stage 6 QA-to-Red canonical pack and Stage 6 retrofit artifacts from PR #1192.
4. Stage 7 PBFAG canonical pack and Stage 7 retrofit artifacts from PR #1194.
5. `modules/amc/06-pbfag/cs2-disposition-pack-stages-5-5a-6-7.md`.
6. `modules/amc/BUILD_PROGRESS_TRACKER.md`.
7. `modules/amc/AMC_PRE_BUILD_ARTIFACT_INDEX.md`.

---

## 3. CS2 Decision

CS2 records the following disposition:

| Stage | Decision | Conditions attached |
|---|---|---|
| Stage 5 - Architecture | APPROVED WITH CONDITIONS | Stage 5 retrofit obligations remain binding inputs for Stage 8 |
| Stage 5a - Deployment Execution Strategy | APPROVED WITH CONDITIONS | Deployment validation, CI, preview, secret, migration, rollback, health/smoke, and dependency conditions remain binding inputs for Stage 8 |
| Stage 6 - QA-to-Red | APPROVED WITH CONDITIONS | QA-FD and QA-DEPLOY rows remain binding inputs for Stage 8 and later QA-to-Green evidence |
| Stage 7 - PBFAG | APPROVED WITH CONDITIONS | PBFAG-FD, PBFAG-DEPLOY, PBFAG-QA, tracker/index, and Stage 8 block rows remain binding inputs for Stage 8 |

---

## 4. Conditions Carried Forward to Stage 8

Any later Stage 8 issue and implementation plan must import at minimum:

1. Stage 5 route/action/state/audit/degraded-mode map.
2. Stage 5a deployment validation matrix, including CI and preview boundaries.
3. Stage 6 QA-FD and QA-DEPLOY rows.
4. Stage 7 PBFAG-FD, PBFAG-DEPLOY, PBFAG-QA, PBFAG-TRACK, and PBFAG-STAGE8 rows.
5. First E2E `/alerts` acknowledgement path.
6. Placeholder/stub rejection rule.
7. Production approval gates.
8. Secret separation across PR, preview, staging, and production.
9. Supabase migration command freeze.
10. Rollback evidence planning.
11. Runtime health/smoke validation.
12. External dependency readiness and visible degraded-mode behavior.
13. Complete implementation evidence package.
14. Tracker and artifact-index updates.
15. No skipped, todo, stub-only, placeholder, or trivially passing test evidence may satisfy functional completion.

---

## 5. Stage 8 Authorization Boundary

This decision makes Stage 8 eligible to be opened next as a separate governed wave.

This decision does not itself create the Stage 8 implementation plan, does not create implementation tasks, does not appoint builders, and does not start build.

Stage 8 must be opened by a separate issue and PR that imports this decision record and all conditions above.

---

## 6. Decision Statement

CS2 approves AMC Stages 5, 5a, 6, and 7 with the conditions listed in this record.

Stage 8 may be proposed next, but only as a new governed Stage 8 wave.

---

## 7. Closure Statement

This record closes the explicit CS2 disposition gap identified after PR #1194.

No implementation work is authorized by this record.

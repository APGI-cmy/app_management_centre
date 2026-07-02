# AMC Stage 7 Addendum - Functional Delivery / Deployment Execution / QA PBFAG

**Stage**: 7 - PBFAG addendum  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: Produced for CS2 review  
**Wave**: amc-stage7-pbfag-retrofit-20260630  
**Issue**: app_management_centre#1193  
**Authority basis**: PR #1186, PR #1188, PR #1190, PR #1192, Stage 5 architecture map, Stage 5a deployment execution validation matrix, Stage 6 QA-FD and QA-DEPLOY RED families  
**Non-scope**: This addendum does not start Stage 8, builder checklist, IAA pre-brief, builder appointment, implementation, or build-readiness certification.

---

## 1. Purpose

This addendum imports the merged Stage 5, Stage 5a, and Stage 6 retrofit obligations into Stage 7 PBFAG.

The existing Stage 7 artifacts remain the primary PBFAG pack:

- `pre-build-final-assurance-gate.md`;
- `pbfag-evidence-matrix.md`;
- `pbfag-findings-and-verdict.md`;
- `pbfag-checklist.md`.

This addendum adds the functional-delivery, deployment-execution, and QA-to-Red gate layer created after the original Stage 7 pack was produced.

---

## 2. PBFAG Retrofit Rule

Stage 7 must verify that the pre-build chain prevents a non-functional build.

PBFAG must hard-gate whether the package defines testable proof for:

1. visible user action and CTA closure;
2. API or external service target coverage;
3. state owner, table, or projection coverage;
4. audit and provenance evidence;
5. server-side authority-gate proof;
6. user-visible degraded-mode behavior;
7. placeholder and stub rejection;
8. route and event naming authority;
9. omitted material-route prevention;
10. deployment execution validation;
11. environment and secret-boundary proof;
12. migration command and rollback proof;
13. runtime health and smoke proof;
14. external dependency readiness or degraded-mode proof;
15. first E2E `/alerts` acknowledgement proof.

If any item is missing, ambiguous, or only implied, Stage 7 must fail or condition Stage 8.

---

## 3. Stage 5 Import

Stage 7 must import the Stage 5 architecture map as a hard PBFAG input.

| Stage 5 obligation | PBFAG treatment |
|---|---|
| Material route inventory | Verify no material route is omitted from QA/PBFAG evidence |
| CTA/action mapping | Reject dead CTA or action-without-target completion claims |
| State/projection mapping | Require state ownership evidence for consequential actions |
| Audit/provenance mapping | Require audit/provenance proof for consequential actions |
| Authority-gate mapping | Require server-side authority proof before side effects |
| Degraded-mode mapping | Require visible degraded/stale/unavailable states |
| Placeholder control | Reject placeholder/stub evidence as completion proof |
| Route/event authority | Reject canonical-name drift without CS2 disposition |

---

## 4. Stage 5a Import

Stage 7 must import the Stage 5a deployment execution validation matrix as a hard PBFAG input.

| Stage 5a obligation | PBFAG treatment |
|---|---|
| Workflow ownership | Verify named workflow ownership is testable or CS2-dispositioned |
| Protected production gate | Fail if production deploy/migration lacks protected approval boundary |
| Secret isolation | Fail if PR/staging can access production secrets |
| Migration command freeze | Fail if migration command drift is allowed |
| Rollback evidence | Condition Stage 8 if rollback/revert/restore evidence is undefined |
| Environment template | Require runtime variable contract coverage |
| Runtime health/smoke | Require health/smoke validation evidence later |
| Dependency readiness | Require readiness or degraded evidence for AIMC, AIMCC, KUC, knowledge, Foreman, specialists, push, Supabase, and Vercel |
| Evidence package | Require deployed URL/API/state/audit/env/dependency/visual-log proof for implementation closure |
| Placeholder deployment proof | Reject placeholder screenshots/logs as completion proof |

---

## 5. Stage 6 Import

Stage 7 must import the Stage 6 QA-FD and QA-DEPLOY RED test families as blocker-grade PBFAG checks.

PBFAG must verify that Stage 6 covers, or explicitly dispositions, every `QA-FD-*` and `QA-DEPLOY-*` row before Stage 8 can be considered.

The Stage 7 verdict must remain conditional or fail if:

- any QA-FD row is missing from Stage 7 evidence;
- any QA-DEPLOY row is missing from Stage 7 evidence;
- any row can pass against a stub or placeholder;
- any row lacks exact RED/fail and GREEN/pass expectations;
- any row lacks a downstream evidence owner for implementation planning.

---

## 6. First E2E Path Binding

The first E2E evidence path is `/alerts` acknowledgement:

`/alerts` UI -> acknowledge CTA -> alert acknowledge API -> authority check -> alerts state update -> audit_events insert -> realtime update -> visible acknowledged state -> audit verification.

This path may not be treated as complete if only one layer passes. The evidence must prove the full user-visible and audit-visible journey.

---

## 7. Stage 8 Block Rule

Stage 8 remains blocked until CS2 explicitly dispositions:

1. Stage 5 original architecture plus Stage 5 retrofit package;
2. Stage 5a original DES pack plus Stage 5a retrofit package;
3. Stage 6 original QA-to-Red pack plus Stage 6 retrofit package;
4. Stage 7 original PBFAG pack plus this retrofit package.

This addendum does not approve any stage by itself and does not authorize Stage 8.

---

## 8. Disposition Statement

Stage 7 may be treated as functionally aligned only if this addendum, the PBFAG retrofit evidence matrix, and the Stage 7 change-propagation audit are reviewed and accepted or explicitly amended by CS2.

Until then, Stage 7 remains produced for review and Stage 8 remains blocked.

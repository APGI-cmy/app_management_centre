# AMC Stage 7 PBFAG Retrofit Evidence Matrix

**Stage**: 7 - PBFAG retrofit evidence matrix  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: Produced for CS2 review  
**Wave**: amc-stage7-pbfag-retrofit-20260630  
**Issue**: app_management_centre#1193  
**Authority basis**: PR #1186, PR #1188, PR #1190, PR #1192  
**Non-scope**: This matrix does not start Stage 8, builder checklist, IAA pre-brief, builder appointment, implementation, or build-readiness certification.

---

## 1. Purpose

This matrix maps the Stage 5, Stage 5a, and Stage 6 retrofit obligations into Stage 7 PBFAG checks.

It does not implement tests. It defines the gate evidence that must exist before Stage 8 can be considered by CS2.

---

## 2. Matrix

| Check ID | Source | PBFAG requirement | Pass condition | Fail / condition trigger | Stage 8 effect |
|---|---|---|---|---|---|
| PBFAG-FD-001 | Stage 5 architecture map | Material routes are covered | Every material route is listed in QA/PBFAG evidence or explicitly CS2-dispositioned | Material route omitted | BLOCK |
| PBFAG-FD-002 | Stage 5 architecture map | CTAs/actions have targets | Every material CTA maps to API/service/read-only declaration | Dead CTA or action target missing | BLOCK |
| PBFAG-FD-003 | Stage 5 architecture map | State/projection ownership is defined | Consequential actions have state owner/table/projection evidence | No state owner for action | BLOCK |
| PBFAG-FD-004 | FR-1900/TR-1900/Stage 5 map | Audit/provenance coverage exists | Consequential actions define audit/provenance proof | Success path lacks audit/provenance | BLOCK |
| PBFAG-FD-005 | ARC authority / Stage 5 map | Authority checks are server-side and pre-effect | Side effects require authority gate evidence | Side effect can occur before authority proof | BLOCK |
| PBFAG-FD-006 | Stage 5 map | Degraded-mode behavior is visible | Dependency failure maps to visible unavailable/stale/degraded state | Silent no-op, blank state, or false success | BLOCK |
| PBFAG-FD-007 | Stage 5 addendum | Placeholder/stub evidence is rejected | Placeholder evidence is excluded unless CS2-dispositioned | Placeholder counted as complete | BLOCK |
| PBFAG-FD-008 | Stage 2/TRS/Stage 5 map | Route/event naming authority is preserved | Canonical names are used or drift is dispositioned | Non-canonical route/event used without disposition | BLOCK |
| PBFAG-FD-009 | Stage 5 map | First E2E path is bound | `/alerts` acknowledgement path has full evidence requirement | Only UI/API/state/audit partial proof exists | BLOCK |
| PBFAG-DEPLOY-001 | Stage 5a matrix | Workflow ownership is testable | Named workflows or CS2-approved equivalents are identified | Workflow ownership unclear | BLOCK |
| PBFAG-DEPLOY-002 | Stage 5a matrix | Production approval gate is protected | Production deploy/migration requires protected environment approval | Ungated production action allowed | BLOCK |
| PBFAG-DEPLOY-003 | Stage 5a matrix | Secrets are isolated | Production secrets are scoped to production-only contexts | PR/staging can access production secrets | BLOCK |
| PBFAG-DEPLOY-004 | Stage 5a matrix | Migration command is frozen | Supabase migration command is fixed or amended by CS2 | Migration command drift allowed | BLOCK |
| PBFAG-DEPLOY-005 | Stage 5a matrix | Rollback evidence is required | Rollback/revert/restore evidence requirement exists | Rollback path undefined | CONDITION/BLOCK |
| PBFAG-DEPLOY-006 | Stage 5a matrix | Runtime variables are contracted | `.env.example` or equivalent runtime contract coverage exists | Required runtime var undocumented | BLOCK |
| PBFAG-DEPLOY-007 | Stage 5a matrix | Runtime health/smoke proof is required | Health/smoke proof is a closure requirement | Feature closure lacks smoke proof | BLOCK |
| PBFAG-DEPLOY-008 | Stage 5a matrix | Dependency readiness/degraded evidence is required | AIMC/AIMCC/KUC/knowledge/Foreman/specialist/push/Supabase/Vercel readiness or degraded evidence required | Dependency failure hidden | BLOCK |
| PBFAG-DEPLOY-009 | Stage 5a matrix | Deployment evidence package is defined | URL/API/state/audit/env/dependency/visual-log proof required | Feature marked complete without bundle | BLOCK |
| PBFAG-DEPLOY-010 | Stage 5a matrix | CI boundary is preserved | PR CI may lint/test/schema-check only and must not mutate production | PR CI can mutate production or use live credentials | BLOCK |
| PBFAG-DEPLOY-011 | Stage 5a matrix | Preview boundary is preserved | Preview deploy uses staging/preview resources only | Preview uses production data or production credentials | BLOCK |
| PBFAG-QA-001 | Stage 6 QA-FD family | QA-FD family imported | QA-FD-001 through QA-FD-015 are visible in PBFAG evidence | Any QA-FD row omitted | BLOCK |
| PBFAG-QA-002 | Stage 6 QA-DEPLOY family | QA-DEPLOY family imported | QA-DEPLOY-001 through QA-DEPLOY-010 are visible in PBFAG evidence | Any QA-DEPLOY row omitted | BLOCK |
| PBFAG-QA-003 | Stage 6 matrix | Fail/pass criteria are exact | Each QA-FD/QA-DEPLOY row has RED and GREEN expectations | Vague pass criteria | BLOCK |
| PBFAG-QA-004 | Stage 6 audit | Stage 7 import requirement preserved | Stage 7 explicitly imports QA-FD/QA-DEPLOY blockers | Stage 7 does not import Stage 6 retrofit | BLOCK |
| PBFAG-TRACK-001 | Tracker / index | Tracker and index agree | Tracker and artifact index list Stage 7 retrofit artifacts | Mismatch or stale current action | BLOCK |
| PBFAG-STAGE8-001 | Stage 7 verdict | Stage 8 block is preserved | Stage 8 remains blocked until Stage 5, 5a, 6, and 7 are dispositioned | Stage 8 starts early | BLOCK |

---

## 3. Required Stage 7 Evidence Package

Stage 7 review must include:

1. existing PBFAG pack;
2. Stage 5 architecture map and Stage 5 change-propagation audit;
3. Stage 5a deployment execution validation matrix and audit;
4. Stage 6 QA-FD/QA-DEPLOY expansion matrix and audit;
5. tracker and artifact-index alignment evidence;
6. explicit statement that Stage 8 remains blocked.

---

## 4. Verdict

This matrix makes the Stage 7 gate stricter and better aligned to fully functional build readiness.

It is not an implementation plan and does not authorize Stage 8.

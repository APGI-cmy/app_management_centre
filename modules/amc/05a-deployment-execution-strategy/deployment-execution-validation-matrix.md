# AMC Stage 5a Deployment Execution Validation Matrix

**Stage**: 5a — Deployment execution validation matrix  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: Produced for CS2 review  
**Wave**: amc-stage5a-deployment-execution-retrofit-20260629  
**Issue**: app_management_centre#1189  
**Authority basis**: TR-1910, Stage 5 architecture map, Stage 5 review notes, existing Stage 5a DES artifacts  
**Non-scope**: This matrix does not start Stage 6, Stage 7, Stage 8, builder checklist, IAA pre-brief, builder appointment, or implementation work.

---

## 1. Purpose

This matrix converts the Stage 5a deployment execution strategy into validation and evidence obligations. It exists so Stage 6 QA-to-Red and Stage 7 PBFAG can derive deployment-execution tests without guessing.

---

## 2. Validation Matrix

| Validation domain | Required execution rule | Evidence required later | Failure class if missing | Downstream owner |
|---|---|---|---|---|
| Workflow ownership | `ci.yml`, `deploy-frontend.yml`, and `db-migrate.yml` are the only named automated workflow families unless CS2 amends Stage 5a | workflow file names and trigger review | undocumented workflow ownership | Stage 6 / Stage 7 |
| Frontend/API deployment | frontend and Next.js API routes deploy as one Vercel unit | Vercel deployment log and deployed URL | frontend/backend split ambiguity | Stage 6 / Stage 8 |
| Production approval | production deploy and production migration use protected `production` environment | GitHub environment gate evidence | ungated production action | Stage 6 / Stage 7 |
| Migration mechanism | Supabase CLI `supabase db push --project-ref $SUPABASE_PROJECT_REF` only | workflow command inspection and migration log | speculative migration path | Stage 6 / Stage 7 |
| Migration rollback | rollback/revert procedure must be defined before implementation waves close | rollback note, backup/restore reference, migration revert plan | no rollback evidence | Stage 5a / Stage 8 |
| Environment template | root `.env.example` defines required variables and placeholders only | `.env.example` present and no committed secrets | missing configuration contract | Stage 6 |
| Secret isolation | production secrets only in `production` environment; no production DB credentials in PR/staging | workflow/env review | production secret leakage | Stage 6 / Stage 7 |
| CI boundary | PR CI may run lint/type/test/schema verification but no production mutation | workflow trigger and secret scope review | CI mutates production | Stage 6 / Stage 7 |
| Preview boundary | preview deploy uses staging/preview resources only | preview env config evidence | preview uses production data | Stage 6 / Stage 7 |
| Live validation | post-deployment manual validation executed by CS2/designated operator | validation checklist/log/screenshots where applicable | no live evidence | Stage 7 / Stage 8 |
| Runtime health | app health, API reachability, Supabase connectivity, realtime, and core route availability checked | smoke log or manual validation record | unvalidated runtime | Stage 6 / Stage 7 |
| Audit validation | consequential action creates audit/provenance event | audit record proof for first E2E path | missing audit proof | Stage 6 / Stage 7 |
| First E2E path | `/alerts` acknowledgement path is the first deployment evidence candidate | UI/API/state/audit evidence bundle | no end-to-end proof | Stage 6 / Stage 7 |
| AIMC readiness | AIMC unavailable state or successful action gateway verified | dependency status evidence | hidden AI dependency failure | Stage 6 / Stage 7 |
| AIMCC readiness | upload/quota status read degrades visibly when unavailable | status/stale evidence | hidden AIMCC failure | Stage 6 / Stage 7 |
| KUC readiness | upload submission path uses KUC and surfaces rejection/unavailable state | KUC response/evidence | direct AIMCC ingestion or hidden failure | Stage 6 / Stage 7 |
| Knowledge readiness | knowledge retrieval requires provenance/stale marker | retrieval proof | unproven/stale knowledge presented as truth | Stage 6 / Stage 7 |
| Foreman readiness | build-status feed and intervention dispatch boundaries validated | status/dispatch proof or N/A evidence | false Foreman readiness | Stage 6 / Stage 7 |
| Specialist agent readiness | workspace status/termination boundaries validated if enabled | status and approval-gate evidence | ungoverned workspace action | Stage 6 / Stage 7 |
| Push readiness | mobile/web push credentials and fallback route validation if enabled | push delivery/open evidence or N/A record | critical alert dead end | Stage 6 / Stage 7 |
| No placeholder deployment | placeholder deployment evidence cannot satisfy completion | placeholder register and CS2 disposition | placeholder counted complete | Stage 7 |

---

## 3. Required Evidence Package for Later Gates

Before any implementation wave can close, Stage 7/8 must require at least:

1. deployed URL or explicit non-deployment status;
2. API endpoint proof for affected routes;
3. state persistence/projection proof;
4. audit/provenance proof;
5. environment validation proof;
6. dependency readiness or degraded-mode proof;
7. rollback/migration evidence where database changes apply;
8. screenshots/video/logs for user-visible journeys where applicable;
9. test logs showing GREEN only after implementation exists.

---

## 4. Stage 6 Derivation Hints

Stage 6 should derive RED tests or validation checks for the following:

- missing workflow file;
- wrong workflow trigger;
- production job without protected environment;
- production secrets available to PR jobs;
- migration command drift;
- missing rollback plan;
- missing `.env.example` entry for required runtime variable;
- runtime health endpoint unavailable;
- missing audit event after first E2E path;
- external dependency unavailable but hidden from user;
- placeholder evidence counted as complete.

---

## 5. Verdict

This matrix makes the deployment-execution evidence path explicit enough for Stage 6 and Stage 7 to derive tests and gates.

It is not an implementation plan and does not authorize build work.
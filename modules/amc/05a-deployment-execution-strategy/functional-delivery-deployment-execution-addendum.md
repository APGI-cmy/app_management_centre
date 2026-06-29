# AMC Stage 5a Addendum — Functional Delivery Deployment Execution

**Stage**: 5a — Deployment Execution Strategy addendum  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: Produced for CS2 review  
**Wave**: amc-stage5a-deployment-execution-retrofit-20260629  
**Issue**: app_management_centre#1189  
**Authority basis**: PR #1186, PR #1188, TR-1910, Stage 5 functional-delivery architecture addendum, Stage 5 architecture map, Stage 5 change-propagation audit  
**Non-scope**: This addendum does not start Stage 6, Stage 7, Stage 8, builder checklist, IAA pre-brief, builder appointment, or implementation work.

---

## 1. Purpose

This addendum imports the merged Stage 1-5 functional-delivery controls into Stage 5a Deployment Execution Strategy.

The existing Stage 5a `deployment-execution-strategy.md`, `deployment-surface-ownership-table.md`, and `runner-and-environment-constraints.md` remain the primary deployment-execution artifacts. This addendum does not replace them. It adds a functional-delivery execution layer so deployment planning cannot become speculative or incomplete.

---

## 2. Stage 5a Functional Delivery Rule

A deployment execution strategy is not complete unless it defines how a later implemented capability can be proven live across:

1. workflow ownership;
2. runner and environment constraints;
3. environment variable availability;
4. migration execution and rollback;
5. deployment trigger and protected approval boundary;
6. runtime health validation;
7. dependency readiness validation;
8. audit/provenance validation;
9. visible user-facing validation;
10. deployment evidence capture.

Stage 5a must therefore bind the Stage 5 route/action/state/audit architecture map to deploy-time verification and evidence requirements.

---

## 3. TR-1910 Import

TR-1910 requires Stage 5/5a to freeze deployment and runtime execution behavior with enough precision that builders do not invent operational behavior.

Stage 5a satisfies TR-1910 only if the following are explicit:

| TR-1910 requirement | Stage 5a execution interpretation | Status after this addendum |
|---|---|---|
| Deployment surface ownership | `deployment-surface-ownership-table.md` assigns each surface to one owner | CLEAN |
| Workflow ownership | `deploy-frontend.yml`, `db-migrate.yml`, `ci.yml`, and manual validation are named | CLEAN |
| Environment/protected gate behavior | `runner-and-environment-constraints.md` defines production/staging boundary | CLEAN |
| Migration mechanism | Supabase CLI `supabase db push --project-ref $SUPABASE_PROJECT_REF` only | CLEAN |
| Live validation sequence | Added by `deployment-execution-validation-matrix.md` | CLEAN after retrofit |
| CI/preview/production boundaries | Existing DES and runner constraints define boundaries | CLEAN |
| Runtime smoke validation | Added by validation matrix | CLEAN after retrofit |
| No operational speculation | This addendum prohibits builder invention of workflow/env/migration behavior | CLEAN |

---

## 4. Functional Delivery Deployment Evidence Rule

Stage 6/7/8 may not treat a feature as deployment-ready unless later implementation evidence can show:

- a deployed frontend route or user-visible surface;
- a working API route or external service contract;
- state persistence or projection boundary;
- audit/provenance event creation where consequential;
- authority gate behavior;
- degraded-mode behavior for unavailable dependencies;
- environment variables resolved from the correct environment scope;
- no production secret leakage into PR/staging jobs;
- migration path executed or explicitly not applicable;
- runtime health/smoke result captured;
- screenshot/video/log evidence where applicable.

---

## 5. Approved Deployment Execution Boundary

The following remains frozen for downstream use unless CS2 approves a Stage 5a amendment:

| Surface | Owner | Deployment/validation rule |
|---|---|---|
| Frontend + API routes | `deploy-frontend.yml` | Unified Vercel deployment unit; production requires protected `production` environment approval |
| DB migration | `db-migrate.yml` | Manual dispatch only; Supabase CLI only; production requires protected approval |
| Schema verification | `ci.yml` | Read-only CI validation; no DB mutation |
| Live operational validation | CS2 or designated operator | Manual post-deployment validation with evidence capture |
| External dependency readiness | runtime smoke/manual validation | AIMC, AIMCC, KUC, knowledge/memory, Foreman, specialist agents, push providers, Supabase, and Vercel readiness must be checked or explicitly marked not applicable |

---

## 6. No-Speculation Rule

Builders and later agents must not invent:

- workflow file names;
- runner types;
- environment names;
- migration commands;
- production approval gates;
- rollback sequence;
- health/smoke validation steps;
- evidence requirements;
- external dependency readiness assumptions.

Any missing deployment-execution detail is a Stage 5a DRIFT or AMBIGUITY item, not a builder decision.

---

## 7. Downstream Carry-Forward

Stage 6 must create RED tests or validation checks for:

- required workflow presence and names;
- forbidden production secrets in PR/staging contexts;
- no production DB access from PR jobs;
- `supabase db push --project-ref $SUPABASE_PROJECT_REF` as the only migration command;
- no `supabase link` step before migrations;
- production approval gate presence;
- environment-variable validation;
- runtime health/smoke validation obligations;
- deployment evidence package completeness.

Stage 7 must fail or condition Stage 8 if Stage 5a deployment execution remains ambiguous.

Stage 8 remains blocked until Stage 5a, Stage 6, and Stage 7 are CS2-dispositioned.

---

## 8. Stage 5a Disposition Statement

Stage 5a may be treated as functionally aligned only if this addendum, the deployment execution validation matrix, and the Stage 5a change-propagation audit are reviewed and accepted or explicitly dispositioned by CS2.

This addendum does not approve Stage 5a by itself and does not authorize implementation.
# Deployment Surface Ownership Table — Stage 5a

**Stage**: 5a — Deployment Execution Strategy  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: 🟡 Produced — Approval Pending (CS2)  
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)  
**CS2 Authorization**: app_management_centre#1133  
**Wave**: amc-stage5a-deployment-execution-strategy-20260427  
**Date**: 2026-04-27  
**Parent Document**: `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` v1.0 (DES-001)

---

> **PURPOSE**: This artifact provides the definitive ownership matrix for all AMC deployment
> surfaces. It is a supporting artifact to `deployment-execution-strategy.md` and expands DES-001
> (Workflow Surface Ownership) into a complete, cross-referenced ownership table. No deployment
> surface may be executed without a named owning workflow or process in this table.

---

## Deployment Surface Ownership Matrix

| Surface ID | Deployment Surface | Owning Workflow / Process | Execution Trigger Class | Environment Scope | Approval Requirement | Runner Type | Notes |
|---|---|---|---|---|---|---|---|
| **SURF-001** | Frontend deploy | `deploy-frontend.yml` | Push to `main` (automatic after CI pass); manual dispatch | Production (Vercel production project) | ✅ `production` environment gate — CS2 approval required | GitHub-hosted (`ubuntu-latest`) | Deploys Next.js application to Vercel production. Unified deployment unit includes API routes. |
| **SURF-002** | Backend / API routes deploy | `deploy-frontend.yml` (same as SURF-001) | Push to `main` (automatic after CI pass); manual dispatch | Production (Vercel production project) | ✅ `production` environment gate — CS2 approval required | GitHub-hosted (`ubuntu-latest`) | Next.js API routes ship as part of the unified Next.js deployment. No separate backend deploy workflow exists. Same workflow, same deployment unit as SURF-001. |
| **SURF-003** | DB migration | `db-migrate.yml` | Manual dispatch only | Production (Supabase production project); Staging (Supabase staging project) | ✅ `production` environment gate — CS2 approval required (production only); no gate for staging | GitHub-hosted (`ubuntu-latest`) | Supabase CLI (`supabase db push`) is the only approved mechanism. See DES-004. `SUPABASE_PROJECT_REF` determines target environment. |
| **SURF-004** | Schema verification | `ci.yml` (CI gate) | Pull request (automatic on every PR targeting `main`) | CI / Staging (read-only; no DB mutation) | ❌ No approval gate — automated | GitHub-hosted (`ubuntu-latest`) | Part of the CI gate pipeline: lint → type check → dependency scan → unit → integration → E2E → schema verification. Read-only; does not mutate the database. |
| **SURF-005** | Live operational validation | Manual process — CS2 (@APGI-cmy) or CS2-designated operator | Post-deployment manual execution | Production | ✅ Manual — CS2 or designated operator executes post-deploy | N/A (manual) | Post-deployment health check confirming live environment is operational. Not automated. Executed after each production deployment and migration. |

---

## Coverage Verification

All five mandatory deployment surfaces defined in `DEPLOYMENT_STRATEGY_OVERSIGHT.md` §3.1 (DES-001) are present and owned:

| Required Surface (per DES-001) | Present in Matrix? | Owner |
|---|---|---|
| Frontend deploy | ✅ SURF-001 | `deploy-frontend.yml` |
| Backend deploy | ✅ SURF-002 | `deploy-frontend.yml` (unified with frontend) |
| DB migration | ✅ SURF-003 | `db-migrate.yml` |
| Schema verification | ✅ SURF-004 | `ci.yml` |
| Live operational validation | ✅ SURF-005 | Manual — CS2 |

**Ownership gap check**: ✅ No unowned surface. All five surfaces have exactly one named owner.

---

## Trigger Class Definitions

| Trigger Class | Definition |
|---|---|
| **Automatic — PR** | Triggered automatically on every pull request targeting `main`; no human dispatch required |
| **Automatic — Push to main** | Triggered automatically when a commit lands on `main` (after PR merge) |
| **Manual dispatch** | Triggered only by an authorized human explicitly dispatching the workflow via GitHub Actions UI or API |
| **Post-deployment manual** | Executed by a human operator after a deployment is confirmed live; no workflow trigger |

---

## Environment Scope Definitions

| Environment | Supabase Project | Vercel Project | Used By |
|---|---|---|---|
| Development | Developer-local Supabase project | Local Next.js dev server | Developer local work |
| Staging | Staging Supabase project (separate from production) | Vercel preview deployments (PR) | CI integration tests, E2E, Vercel PR previews |
| Production | Production Supabase project | Vercel production project | SURF-001, SURF-002, SURF-003 (production dispatch), SURF-005 |

**Environment isolation invariant**: Each environment uses its own dedicated Supabase project. The production Supabase service role key must never be present in the staging or CI environment. Cross-environment contamination (e.g., running a staging migration against the production Supabase project) is prevented by the `SUPABASE_PROJECT_REF` environment variable and the `production` approval gate.

---

## Approval Requirement Summary

| Surface | Approval Required | Approval Mechanism |
|---|---|---|
| SURF-001 — Frontend deploy (production) | ✅ YES | GitHub `production` environment — CS2 reviewer |
| SURF-002 — Backend/API routes deploy (production) | ✅ YES | GitHub `production` environment — CS2 reviewer (same gate as SURF-001) |
| SURF-003 — DB migration (production) | ✅ YES | GitHub `production` environment — CS2 reviewer |
| SURF-003 — DB migration (staging) | ❌ NO | Automated — no gate |
| SURF-004 — Schema verification (CI) | ❌ NO | Automated — no gate |
| SURF-005 — Live operational validation | ✅ YES (manual) | CS2 or designated operator executes and confirms |

---

## Downstream Inheritance Note

- **Stage 6 (QA-to-Red)**: Must include test cases verifying that each surface fires only from its defined trigger class and that cross-surface contamination (e.g., `deploy-frontend.yml` executing DB mutations) cannot occur.
- **Stage 7 (PBFAG)**: Must verify this table is present, complete, and consistent with `deployment-execution-strategy.md` (DES-001).
- **Stage 8 (Implementation Plan)**: Must name which build wave implements each surface workflow (`ci.yml`, `deploy-frontend.yml`, `db-migrate.yml`) and confirm alignment with this table.

---

*AMC Deployment Surface Ownership Table v1.0 — 2026-04-27 — CS2 authorization: app_management_centre#1133*

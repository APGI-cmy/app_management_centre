# Deployment Execution Strategy — Stage 5a

**Stage**: 5a — Deployment Execution Strategy  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: 🟡 Produced — Approval Pending (CS2)  
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)  
**CS2 Authorization**: app_management_centre#1133 (Stage 5a definition authority)  
**Governing Issue**: app_management_centre#1133 (this issue)  
**Wave**: amc-stage5a-deployment-execution-strategy-20260427  
**Date**: 2026-04-27  
**Upstream Sources**:
- Stage 5 Architecture: `modules/amc/04-architecture/architecture-specification.md` v1.0 (produced approval-pending 2026-04-26, ref #1131)
- Stage 4 TRS: `modules/amc/03-trs/technical-requirements-specification.md` v1.1 (treated as approved, ref #1131)
- Stage 5a Definition Authority: `modules/amc/governance-oversight/DEPLOYMENT_STRATEGY_OVERSIGHT.md` AMC-GOV-OVERSIGHT-001 v1.0

**Canonical Location**: `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md`

---

> **DERIVATION DECLARATION**
> This Deployment Execution Strategy derives from the produced approval-pending Stage 5 Architecture
> Specification (`modules/amc/04-architecture/architecture-specification.md` v1.0, awaiting CS2
> approval) and all approved upstream truth (Stages 1–4). It translates architectural
> deployment-shaping decisions into a frozen, explicit, non-contradictory operational deployment
> model. It does not invent new product behavior. No deployment execution decision may contradict or
> silently soften any Architecture or TRS constraint.
> This document defines the deployment execution boundaries that Stage 6 QA-to-Red, Stage 7 PBFAG,
> and Stage 8 Implementation Plan must honor. Decisions made here are binding on all downstream
> stages unless explicitly amended with CS2 approval.
>
> **CONFORMANCE MANDATE (AMC-DEPLOY-001)**: All AMC workflow implementation in Stage 12 (Build)
> and all AMC operational deployments after build MUST conform to this document. Deviations require
> a formal Stage 5a governance update — ad hoc operational model substitution, undocumented runner
> changes, or unilateral migration path changes are prohibited.

---

## Table of Contents

1. [Purpose & Scope](#1-purpose--scope)
2. [Architectural Traceability](#2-architectural-traceability)
3. [Mandatory DES Fields](#3-mandatory-des-fields)
   - 3.1 [DES-001 — Workflow Surface Ownership](#31-des-001--workflow-surface-ownership)
   - 3.2 [DES-002 — GitHub-Hosted Runner Authorization](#32-des-002--github-hosted-runner-authorization)
   - 3.3 [DES-003 — Self-Hosted Runner Requirement](#33-des-003--self-hosted-runner-requirement)
   - 3.4 [DES-004 — Migration Execution Path](#34-des-004--migration-execution-path)
   - 3.5 [DES-005 — CI / Preview / Production Execution Boundaries](#35-des-005--ci--preview--production-execution-boundaries)
   - 3.6 [DES-006 — Safety Classification](#36-des-006--safety-classification)
   - 3.7 [DES-007 — Manual / Protected Approval Boundaries](#37-des-007--manual--protected-approval-boundaries)
   - 3.8 [DES-008 — Environment / Network Assumption Validation](#38-des-008--environment--network-assumption-validation)
4. [Downstream Stage Inheritance](#4-downstream-stage-inheritance)
5. [Anti-Drift Rules](#5-anti-drift-rules)
6. [Amendment Process](#6-amendment-process)
7. [Sign-Off / Approval Record](#7-sign-off--approval-record)

---

## 1. Purpose & Scope

### 1.1 Purpose

This document freezes the operational deployment model for AMC. It translates the deployment-shaping architectural decisions from Stage 5 Architecture into explicit, actionable, non-contradictory deployment execution rules. It answers the eight mandatory DES fields defined in `DEPLOYMENT_STRATEGY_OVERSIGHT.md` §3.1, leaving no field ambiguous or deferred.

This document is the authoritative reference for deployment execution ownership, runner authorization, migration path, execution boundaries, safety classification, approval requirements, and environment validation. Downstream stages (Stage 6, Stage 7, Stage 8) must use this document as a frozen reference — no deployment execution decision in later stages may diverge from this document without a formal Stage 5a amendment approved by CS2.

### 1.2 Scope

**In scope for Stage 5a:**
- All AMC deployment surfaces (frontend, backend/API routes, database migration, schema verification, live operational validation)
- Runner type authorization per surface (GitHub-hosted vs. self-hosted)
- CI/Preview/Production execution boundary definitions
- Database migration execution path (single approved mechanism)
- Safety classification of each surface and workflow
- Manual/protected approval boundaries
- Environment and network assumption validation approach

**Out of scope for Stage 5a:**
- CI script implementation (Stage 12 Build — deferred per Architecture §9)
- Specific Vercel project configuration (Stage 12 Build)
- Supabase migration file content (schema-builder, Stage 12 Build)
- Test suite implementation (Stage 6 QA-to-Red)

---

## 2. Architectural Traceability

This strategy derives directly from the following Stage 5 Architecture decisions:

| Architecture Decision | Architecture Reference | Stage 5a Impact |
|---|---|---|
| **Deployment Platform**: Vercel (recommended); any Node.js host supporting Next.js 14+ | Architecture §3.8, §8 | Frontend and backend (Next.js API routes) deploy as a unified Vercel deployment unit |
| **CI/CD Pipeline**: Lint → Type check → Dependency scan → Unit tests → Integration tests → E2E smoke tests → Deployment | Architecture §3.8 | CI gate sequence frozen; no reordering or omission permitted |
| **Branch protection**: All merges to `main` require PR review + CI pass | Architecture §3.8 | Production deployment is gated; no direct push to `main` |
| **Environment tiers**: Development, Staging, Production; Supabase projects per tier | Architecture §3.8 | Three tiers; each uses its own Supabase project — no shared project cross-tier |
| **Environment variable validation**: Startup check fails build if required env vars absent | Architecture §3.8 | Pre-flight env var check is mandatory; missing vars cause startup failure |
| **Background Scheduler**: Supabase Edge Functions (cron-trigger) | Architecture §3.6 | Edge Function deployment is part of backend deploy; inherits same environment scope |
| **Database**: Supabase (PostgreSQL) | Architecture §3.4 | Supabase CLI is the only approved migration mechanism for Supabase-hosted databases |

**ADR reference**: Architecture Decision Records (`modules/amc/04-architecture/architecture-decision-records.md`) are not yet produced (placeholder). When produced, any ADR that constrains deployment choices must be referenced here via Stage 5a amendment.

**TRS reference**: The following TRS requirements directly constrain this strategy:
- TR-1505 (§15): All external service base URLs must be environment-variable-configured; missing URL configuration must prevent startup
- TR-1504 (§15): Service-identity tokens as environment variables; not hardcoded
- TR-607 (§6): Quota threshold values must be environment-variable-configurable
- TR-BOUNDARY-001 (§5): AI SDK prohibition enforced at CI dependency scan gate

---

## 3. Mandatory DES Fields

### 3.1 DES-001 — Workflow Surface Ownership

**Field**: Which workflow or manual process owns execution of each deployment surface?

Each deployment surface has exactly one owning workflow or manual process. No surface is unowned. The table below is the definitive ownership assignment.

| Deployment Surface | Owner | Trigger Class | Notes |
|---|---|---|---|
| **Frontend deploy** | `deploy-frontend.yml` (GitHub Actions) | Push to `main` (automatic); manual dispatch | Deploys the Next.js application to Vercel production. Triggered after CI pass on `main`. Includes Next.js API routes (unified deployment unit — §3.8 Architecture). |
| **Backend / API routes deploy** | `deploy-frontend.yml` (same workflow as frontend) | Push to `main` (automatic); manual dispatch | Next.js API routes are deployed as part of the unified Next.js application on Vercel. There is no separate backend deploy workflow — backend and frontend ship as one Vercel deployment unit. |
| **DB migration** | `db-migrate.yml` (GitHub Actions) | Manual dispatch only | Executes Supabase CLI migration against the target Supabase project. Requires protected environment approval before execution. Never runs on PR. Never runs automatically on `main` push without explicit CS2 authorization of that trigger mode. |
| **Schema verification** | `ci.yml` (GitHub Actions, CI gate) | Pull request (automatic) | Verifies schema expectations as part of the CI gate (lint, type check, dependency scan, unit, integration, E2E). Does not mutate the database. Runs on GitHub-hosted runners. |
| **Live operational validation** | Manual process (CS2 or designated operator) | Post-deployment manual execution | Post-deploy health check confirming the deployed application is live and operational. Not automated. CS2 or a designated operator performs this check after each production deployment. |

**Ownership invariant**: No surface in this list may be owned by more than one workflow or process. If a new surface is identified, a Stage 5a amendment is required before that surface may be deployed.

---

### 3.2 DES-002 — GitHub-Hosted Runner Authorization

**Field**: Are GitHub-hosted runners permitted to touch live infrastructure? Which surfaces?

**Authorization statement:**

GitHub-hosted runners are authorized for CI (PR checks) and for triggering Vercel deployments to the **staging** and **production** environments. However:

- **GitHub-hosted runners may NOT directly access or mutate the production Supabase database** (no direct `psql`, no Supabase service role key usage against production).
- **GitHub-hosted runners may NOT run database migrations against production without a GitHub protected environment approval gate** (`production` environment, §3.7).
- **GitHub-hosted runners ARE authorized** to execute the `deploy-frontend.yml` workflow to Vercel production, subject to the `production` protected environment approval gate.
- **GitHub-hosted runners ARE authorized** to execute `db-migrate.yml` against the staging Supabase project (no approval gate required for staging).
- **GitHub-hosted runners ARE authorized** for all CI gate activities on PRs: lint, type check, dependency scan, unit tests, integration tests, E2E smoke tests, schema verification.

| Surface | GitHub-Hosted Authorized? | Condition |
|---|---|---|
| CI (PR) — lint, type check, dependency scan | ✅ YES | No condition |
| CI (PR) — unit tests | ✅ YES | No condition |
| CI (PR) — integration tests | ✅ YES | Staging Supabase project only (read patterns); no production DB access |
| CI (PR) — E2E smoke tests | ✅ YES | Staging environment only |
| Schema verification | ✅ YES | No DB mutation; read-only schema checks |
| Vercel preview deploy (PR) | ✅ YES | Preview environment; no production DB |
| Frontend deploy to production | ✅ YES | Subject to `production` protected environment approval gate |
| DB migration — staging | ✅ YES | Staging Supabase project only |
| DB migration — production | ✅ YES (with gate) | Subject to `production` protected environment approval gate |
| Live operational validation | ❌ NO | Manual process; not executed by runners |

---

### 3.3 DES-003 — Self-Hosted Runner Requirement

**Field**: Which surfaces require self-hosted runners? What are the runner capability requirements?

**Statement:** No AMC deployment surface requires a self-hosted runner. All surfaces are handled by GitHub-hosted runners within their authorized scope (§3.2) subject to the protected environment approval gates defined in §3.7.

**Rationale**: The AMC deployment topology (Vercel for Next.js; Supabase for database; GitHub Actions workflows) does not require access to private network resources, on-premises infrastructure, or capabilities unavailable on standard GitHub-hosted runners (ubuntu-latest). The Supabase CLI authenticates via `SUPABASE_ACCESS_TOKEN` and project reference (environment variables) from any runner with internet access.

**Constraint**: If a future AMC deployment surface requires private network access (e.g., a self-hosted Supabase instance or a private cluster), a Stage 5a amendment specifying the self-hosted runner requirement, its capability constraints, and its network access scope is mandatory before that surface may be deployed.

**Runner type registry:**

| Surface | Runner Type | Runner Label |
|---|---|---|
| CI (all PR gate stages) | GitHub-hosted | `ubuntu-latest` |
| Vercel preview deploy (PR) | GitHub-hosted | `ubuntu-latest` |
| Frontend + API routes deploy to production | GitHub-hosted | `ubuntu-latest` |
| DB migration (staging) | GitHub-hosted | `ubuntu-latest` |
| DB migration (production) | GitHub-hosted | `ubuntu-latest` |
| Live operational validation | N/A — manual process | N/A |

---

### 3.4 DES-004 — Migration Execution Path

**Field**: What is the exact approved migration execution mechanism?

**Approved mechanism (single, frozen):**

> **Supabase CLI** (`supabase db push`) is the only approved mechanism for executing database migrations against any AMC Supabase project (Development, Staging, Production).

**Execution details:**

- Command: `supabase db push --linked`
- Authentication: `SUPABASE_ACCESS_TOKEN` (environment variable; never hardcoded)
- Project targeting: `SUPABASE_PROJECT_REF` (environment variable; per-environment value)
- Workflow: `db-migrate.yml` (GitHub Actions)
- Migration files location: `supabase/migrations/` directory in the AMC repository
- Migration ordering: Supabase CLI executes migrations in filename-timestamp order (standard Supabase CLI behavior)
- Idempotency: Supabase CLI tracks applied migrations in `supabase_migrations.schema_migrations` — already-applied migrations are not re-executed

**What is explicitly prohibited:**

| Prohibited Mechanism | Reason |
|---|---|
| Direct `psql` execution against production | Unaudited, bypasses CLI migration tracking |
| Manual SQL execution via Supabase Dashboard | Unaudited, bypasses CLI migration tracking |
| Migration scripts run from a local developer machine | Uncontrolled environment; not reproducible |
| Any migration mechanism other than Supabase CLI | Introduces migration tracking inconsistency |
| Running `supabase db push` without `SUPABASE_ACCESS_TOKEN` | Authentication bypass; prohibited |

**Prohibition enforcement**: Any builder PR that introduces an alternative migration mechanism is a deployment-strategy drift violation and must cause a QP FAIL verdict. See §5 (Anti-Drift Rules).

---

### 3.5 DES-005 — CI / Preview / Production Execution Boundaries

**Field**: What runs on PRs, previews, pushes to `main`, manual dispatches, and protected environments?

#### Pull Requests (any branch → `main`)

The CI workflow (`ci.yml`) runs automatically on every PR targeting `main`:

1. Lint (ESLint)
2. Type check (TypeScript)
3. Dependency scan (AI SDK prohibition — TR-BOUNDARY-001)
4. Unit tests
5. Integration tests (staging Supabase project; read patterns only; no production DB access)
6. E2E smoke tests (staging environment)
7. Vercel preview deploy (automatic; preview URL attached to PR)

**What does NOT run on PRs:**
- Production frontend deployment
- Database migration (any environment: staging or production)
- Live operational validation

#### Push to `main` (after PR merge)

After a PR is merged to `main`, the following runs in order:

1. `ci.yml` — full CI gate re-run on `main` (same stages as PR)
2. `deploy-frontend.yml` — triggered after CI pass; deploys frontend + API routes to Vercel production (subject to `production` protected environment approval)
3. `db-migrate.yml` — manually dispatched by CS2 after confirming deployment success (not automatically triggered on push to `main`; see §3.7)

**What does NOT run automatically on push to `main`:**
- DB migration (must be manually dispatched; see §3.7)
- Live operational validation (manual process; see §3.7)

#### Vercel Preview Deploys (PR)

- Triggered automatically by Vercel on every PR commit
- Targets the Vercel preview environment (ephemeral URL per PR)
- Does NOT connect to the production Supabase project
- Preview environments use staging Supabase project or a seeded preview environment
- No DB mutations against production

#### Manual Workflow Dispatch

| Workflow | Manual Dispatch Permitted? | Requires Protected Environment Approval? |
|---|---|---|
| `ci.yml` | Yes (re-run CI on any ref) | No |
| `deploy-frontend.yml` | Yes (re-deploy production on demand) | Yes — `production` environment gate |
| `db-migrate.yml` | Yes (primary dispatch mode for production) | Yes — `production` environment gate |

#### Protected Environment (`production`)

The GitHub `production` environment is configured with:
- Required reviewer: CS2 (@APGI-cmy)
- No auto-approve; reviewer must explicitly approve before workflow job execution proceeds

Workflows that reference the `production` environment cannot execute their production-targeting steps until the required reviewer approves. This is the sole mechanism preventing automated production deployments and migrations from running without CS2 sign-off.

---

### 3.6 DES-006 — Safety Classification

**Field**: Classify each workflow/surface as CI-safe, preview-safe, or live-only.

| Surface / Workflow | Safety Class | Definition |
|---|---|---|
| Lint | CI-safe | Runs on every PR; no external side-effects; no service connections required |
| Type check | CI-safe | Runs on every PR; no external side-effects |
| Dependency scan (AI SDK prohibition) | CI-safe | Runs on every PR; no external side-effects |
| Unit tests | CI-safe | Runs on every PR; no live service connections; uses mocks/stubs |
| Integration tests | CI-safe | Runs on every PR; connects to staging Supabase project in read-only patterns; does NOT modify production data |
| E2E smoke tests | CI-safe | Runs on every PR; targets staging/preview environment only |
| Schema verification | CI-safe | Runs on every PR; read-only schema introspection; no DB mutation |
| Vercel preview deploy | Preview-safe | Triggered on PRs; ephemeral preview URL; no production DB access; no production Vercel project mutation |
| Frontend + API routes production deploy | Live-only | Deploys to production Vercel project; requires `production` environment approval |
| DB migration — staging | Preview-safe | Mutates staging Supabase project only; no production DB access; no approval gate required |
| DB migration — production | Live-only | Mutates production Supabase project; requires `production` environment approval |
| Live operational validation | Live-only | Executed post-deployment against live production environment; manual process |

**Safety boundary enforcement rules:**
- CI-safe surfaces MUST NOT require credentials that grant production database write access
- Preview-safe surfaces MUST NOT use the production Supabase project reference or service role key
- Live-only surfaces MUST be gated by the `production` protected environment (or are manual processes)
- A frontend deploy workflow (deploy-frontend.yml) MUST NOT execute any database mutation — frontend workflows are prohibited from performing DB migrations even if DB credentials are available in the environment

---

### 3.7 DES-007 — Manual / Protected Approval Boundaries

**Field**: What requires CS2 or manual human approval? What is protected? What may never be automated?

#### Protected by GitHub `production` Environment (requires CS2 approval)

The following actions are protected by the `production` GitHub environment and require explicit CS2 approval before execution:

| Action | Workflow | CS2 Must Approve? |
|---|---|---|
| Frontend + API routes deployment to Vercel production | `deploy-frontend.yml` | ✅ YES |
| Database migration against production Supabase project | `db-migrate.yml` | ✅ YES |

CS2 approval means: @APGI-cmy (or a CS2-designated reviewer) reviews the pending workflow run in the GitHub Actions UI and clicks "Approve" on the `production` environment gate before the production job steps execute.

#### Manual (not automated — CS2 or designated operator executes)

| Action | Who Executes | When |
|---|---|---|
| Live operational validation | CS2 (@APGI-cmy) or CS2-designated operator | After each production deployment and migration |
| Stage 5a amendment initiation | CS2 (@APGI-cmy) | When a deployment strategy change is required |

#### What may NEVER be automated (prohibited from automation)

| Action | Prohibition Reason |
|---|---|
| Production database migration without `production` environment approval | Risk of irreversible data changes; requires CS2 oversight |
| Automatic production deployment without `production` environment approval | Risk of deploying untested or unapproved changes to live users |
| Live operational validation | Requires human judgment; automated smoke tests are a supplement, not a replacement |
| Stage 5a strategy modification | Governance change; requires formal CS2 amendment process (see §6) |

**Automation boundary invariant**: The following may never be triggered automatically without any human gate:
- Production Vercel deploy
- Production database migration
- Any rollback of production environment

A builder PR that removes the `production` environment requirement from `deploy-frontend.yml` or `db-migrate.yml` is a deployment-strategy drift violation and must cause QP FAIL.

---

### 3.8 DES-008 — Environment / Network Assumption Validation

**Field**: How are environment and network assumptions validated before execution? What pre-flight checks are required? What fails safe if an assumption is invalid?

#### Pre-flight Checks (mandatory before production deployment and migration)

**Application startup pre-flight (all environments):**

Per Architecture §3.8 (TR-1505), the AMC application performs a startup environment variable validation check. If any required environment variable is absent, the application fails to start with an explicit startup error. This check must cover at minimum:

| Variable Category | Variables Checked |
|---|---|
| Supabase connection | `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY` |
| External service URLs | `AIMC_API_BASE_URL`, `AIMCC_API_BASE_URL`, `KUC_API_BASE_URL`, `KNOWLEDGE_API_BASE_URL`, `FOREMAN_API_BASE_URL` |
| Service tokens | `AIMC_SERVICE_TOKEN`, `AIMCC_SERVICE_TOKEN`, `KUC_SERVICE_TOKEN`, `KNOWLEDGE_SERVICE_TOKEN`, `FOREMAN_SERVICE_TOKEN` |
| Quota thresholds | `QUOTA_WARNING_THRESHOLD_PERCENT`, `QUOTA_CRITICAL_THRESHOLD_PERCENT` |

If any required variable is absent: **application start is blocked with explicit error message naming the missing variable**. No partial-start / degraded-mode accepted for missing configuration — startup failure is the correct fail-safe behavior.

**Migration pre-flight (`db-migrate.yml`, before `supabase db push`):**

The `db-migrate.yml` workflow must perform the following pre-flight checks before executing `supabase db push`:

| Pre-flight Check | Command / Verification | Fail-Safe |
|---|---|---|
| Supabase CLI version pinned | Verify Supabase CLI is installed at the pinned version | Abort migration; log error |
| `SUPABASE_ACCESS_TOKEN` present | Check env var is non-empty | Abort migration; fail workflow |
| `SUPABASE_PROJECT_REF` present and matches target environment | Check env var is non-empty and matches expected project reference for target tier | Abort migration; fail workflow |
| Migration files present | Verify `supabase/migrations/` directory contains at least one pending migration | Abort migration if no files; log warning |
| Network connectivity to Supabase | Supabase CLI performs implicit connectivity check on `supabase db push` | Supabase CLI aborts with error if unreachable |

**Deploy pre-flight (`deploy-frontend.yml`, before Vercel deploy):**

| Pre-flight Check | Command / Verification | Fail-Safe |
|---|---|---|
| Vercel token present | Check `VERCEL_TOKEN` env var is non-empty | Abort deploy; fail workflow |
| Vercel project/org ID present | Check `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID` env vars are non-empty | Abort deploy; fail workflow |
| CI gate passed | `deploy-frontend.yml` is triggered only after `ci.yml` succeeds (workflow dependency) | Deploy does not start if CI failed |

#### Fail-Safe Behavior

**Principle: fail loudly, fail early, never partially execute.**

| Assumption Validation Failure | System Behavior |
|---|---|
| Missing required env var at startup | Application startup blocked; error logged naming the missing variable; no traffic served |
| Missing `SUPABASE_ACCESS_TOKEN` | Migration workflow aborts immediately; no DB connection attempted |
| Missing `SUPABASE_PROJECT_REF` | Migration workflow aborts immediately; no DB connection attempted |
| Project ref mismatch (tier vs. ref) | Migration workflow aborts; cross-environment migration contamination prevented |
| CI gate failure on `main` | `deploy-frontend.yml` does not trigger; production deploy blocked |
| Vercel deploy rejected by Vercel API | `deploy-frontend.yml` fails; rollback is handled by Vercel's deployment system (previous deployment remains live) |
| `production` environment approval not given | Protected-environment workflow pauses; production steps do not execute until approved |
| Network unreachable (Supabase) | Supabase CLI aborts with explicit error; migration is retried only after manual verification |

**There is no silent-continue behavior**. Any failed pre-flight check produces an explicit workflow failure and human notification.

---

## 4. Downstream Stage Inheritance

This section defines what Stage 6, Stage 7, and Stage 8 must inherit from this document.

### 4.1 Stage 6 (QA-to-Red) Inheritance

Stage 6 QA-to-Red must test the deployment model defined in this document. At minimum, the Red test suite must include test cases that verify:

- CI gate stages execute in the correct order (DES-005)
- Frontend deploy workflow does NOT execute database migration steps (DES-006)
- DB migration workflow requires `production` environment approval gate (DES-007)
- Application startup fails with explicit error if required env vars are absent (DES-008)
- Supabase CLI is the only migration mechanism; no alternative mechanism present in codebase (DES-004)
- GitHub-hosted runner is used for all CI and deploy surfaces (DES-003)
- AI SDK dependency prohibition is enforced in CI dependency scan (Architecture §3.8)

Stage 6 may not assume a different deployment model than what is defined here. If the QA suite cannot test against the approved model, a Stage 5a amendment is required before Stage 6 proceeds.

### 4.2 Stage 7 (PBFAG) Inheritance

Stage 7 PBFAG must verify:

- This document exists at `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md`
- All 8 DES fields are answered with no TBD values
- No DES field contradicts the Stage 5 Architecture Specification
- DES-004 specifies exactly one migration mechanism (Supabase CLI)
- All deployment surfaces in DES-001 are owned and have no ownership gaps
- The document version is recorded in the PBFAG verification pack

Stage 7 must fail (PBFAG FAIL) if any of the above checks is unsatisfied.

### 4.3 Stage 8 (Implementation Plan) Inheritance

The Stage 8 Implementation Plan must include a dedicated section that:

1. References this document by path and version: `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` v1.0
2. Confirms the wave structure and builder assignments are consistent with the approved deployment execution strategy
3. States which build wave(s) will implement each deployment surface (DES-001)
4. Identifies the DB migration surface as requiring `production` protected environment approval (DES-007)
5. Explicitly prohibits any build wave from substituting a different migration mechanism (DES-004)

An Implementation Plan that lacks this section or proposes a deployment model inconsistent with this document is a blocking defect per `DEPLOYMENT_STRATEGY_OVERSIGHT.md` §4.1.

---

## 5. Anti-Drift Rules

Per `DEPLOYMENT_STRATEGY_OVERSIGHT.md` §5.2, any of the following in a builder PR constitutes a deployment-strategy drift violation and MUST cause a QP FAIL verdict:

| Drift Indicator | Violated DES Field |
|---|---|
| A workflow file that touches a deployment surface not listed in DES-001 | DES-001 |
| A migration execution mechanism other than Supabase CLI | DES-004 |
| A runner type (GitHub-hosted or self-hosted) inconsistent with DES-002/DES-003 | DES-002/DES-003 |
| An environment trigger inconsistent with DES-005 | DES-005 |
| A frontend workflow (`deploy-frontend.yml`) that performs any DB mutation | DES-006 |
| Removal or bypass of the `production` environment approval gate | DES-007 |
| A startup check that silently continues past missing required env vars | DES-008 |
| Hardcoded Supabase project reference or access token | DES-004/DES-008 |

---

## 6. Amendment Process

If a legitimate requirement arises that conflicts with any DES field in this document:

1. Builder HALTS and escalates to Foreman
2. Foreman raises a Stage 5a Amendment issue with CS2 (referencing this document by path and version)
3. CS2 approves or rejects the amendment
4. If approved: this document is updated with version increment, committed, and CS2 sign-off section updated
5. Implementation Plan (Stage 8) is updated to reference the amended version
6. Builder is unblocked with the amended strategy

**Silent deviation is prohibited (AMC-DEPLOY-001).** Amendment is the only permitted path.

---

## 7. Sign-Off / Approval Record

| Field | Value |
|---|---|
| **Document** | AMC Deployment Execution Strategy — Stage 5a |
| **Version** | 1.0 |
| **Prepared by** | foreman-v2-agent (POLC_ORCHESTRATION) |
| **Prepared Date** | 2026-04-27 |
| **CS2 Authorization for Stage 5a** | app_management_centre#1133 |
| **Stage 5 Architecture Reference** | `modules/amc/04-architecture/architecture-specification.md` v1.0 (produced approval-pending, ref #1131) |
| **Stage 4 TRS Reference** | `modules/amc/03-trs/technical-requirements-specification.md` v1.1 (treated as approved per #1131) |
| **Wave** | amc-stage5a-deployment-execution-strategy-20260427 |
| **Reviewed by** | *Pending CS2 review* |
| **Approved by** | *Pending CS2 approval* |
| **Approval Date** | *Pending* |
| **Approval Reference** | *To be assigned by CS2 on approval* |
| **Stage** | Stage 5a of the AMC-local 12+1 stage sequence |
| **Next Stage** | Stage 6 — QA-to-Red (blocked until CS2 approves Stage 5 and Stage 5a) |

### Version History

| Version | Date | Change Summary |
|---|---|---|
| 1.0 | 2026-04-27 | Initial production — complete Stage 5a artifact answering all 8 DES mandatory fields; derived from Architecture §3.8 and §8; consistent with TRS TR-1505, TR-1504, TR-607; CS2 authorization: app_management_centre#1133 |

### Approval Basis Required

CS2 approval of this document confirms:

1. The Deployment Execution Strategy is clear, explicit, and non-contradictory with Stage 5 Architecture
2. All 8 mandatory DES fields are answered without TBD or ambiguity
3. The migration execution path is frozen to a single approved mechanism (Supabase CLI)
4. All deployment surfaces are owned with no ownership gaps
5. Runner and environment constraints are explicit and enforceable
6. Stage 6 QA-to-Red is authorized to derive its deployment boundary test cases from this document
7. Stage 8 Implementation Plan must reference this document by path and version

---

*AMC Deployment Execution Strategy v1.0 — 2026-04-27 — CS2 authorization: app_management_centre#1133*

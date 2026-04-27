# Runner and Environment Constraints — Stage 5a

**Stage**: 5a — Deployment Execution Strategy  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: 🟡 Produced — Approval Pending (CS2)  
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)  
**CS2 Authorization**: app_management_centre#1133  
**Wave**: amc-stage5a-deployment-execution-strategy-20260427  
**Date**: 2026-04-27  
**Parent Document**: `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` v1.0 (DES-002, DES-003, DES-005, DES-006, DES-008)

---

> **PURPOSE**: This artifact documents the runner type requirements and environment constraints for
> all AMC deployment surfaces. It expands DES-002, DES-003, DES-005, DES-006, and DES-008 from
> `deployment-execution-strategy.md` into a consolidated reference for builders, QA, and PBFAG
> verification. It is a supporting artifact; `deployment-execution-strategy.md` is the primary
> authority document.

---

## 1. Runner Type Boundaries

### 1.1 GitHub-Hosted vs. Self-Hosted — Decision

**Decision (frozen):** AMC uses **GitHub-hosted runners only** (`ubuntu-latest`). No self-hosted runners are required or authorized for any AMC deployment surface.

**Basis**: The AMC deployment topology (Vercel for Next.js; Supabase Cloud for database; GitHub Actions workflows) does not require private network access, on-premises infrastructure, or capabilities unavailable on standard GitHub-hosted runners. All external services (Supabase Cloud, Vercel) are reachable via HTTPS from any GitHub-hosted runner with internet access.

**Self-hosted runner introduction constraint**: Any introduction of a self-hosted runner requirement for any AMC surface requires a Stage 5a amendment with explicit CS2 approval. A builder PR that introduces a `self-hosted` runner label without an approved Stage 5a amendment is a drift violation (DES-003).

### 1.2 Runner Assignment per Surface

| Surface ID | Surface Name | Runner Type | Runner Label | Justification |
|---|---|---|---|---|
| SURF-001 | Frontend deploy | GitHub-hosted | `ubuntu-latest` | HTTPS-only Vercel deploy; no private network needed |
| SURF-002 | Backend / API routes deploy | GitHub-hosted | `ubuntu-latest` | Unified with SURF-001; same Vercel deploy |
| SURF-003 | DB migration | GitHub-hosted | `ubuntu-latest` | Supabase CLI authenticates via HTTPS; no private Supabase instance |
| SURF-004 | Schema verification (CI) | GitHub-hosted | `ubuntu-latest` | All CI stages (lint, type check, scan, unit, integration, E2E) execute on standard hosted runner |
| SURF-005 | Live operational validation | N/A — manual | N/A | Manual process; no runner |

### 1.3 Runner Capability Requirements

All GitHub-hosted `ubuntu-latest` runners used by AMC workflows must have:

| Capability | Requirement | Purpose |
|---|---|---|
| Node.js | Version pinned per `package.json` `engines` field (Node.js 18+) | Next.js build, tests, lint |
| pnpm or npm | Version pinned per repository configuration | Dependency installation |
| Supabase CLI | Version pinned in `db-migrate.yml` | DB migration (SURF-003) |
| Vercel CLI | Version pinned in `deploy-frontend.yml` | Frontend deploy (SURF-001/002) |
| Internet access (HTTPS) | Required | Vercel API, Supabase Cloud API |

Pinned versions for Supabase CLI and Vercel CLI must be recorded in the respective workflow files and updated only through a formal workflow update PR (subject to CI gate and code review). Version unpinning is prohibited.

---

## 2. Protected Environment Usage

### 2.1 GitHub `production` Environment Configuration

The `production` GitHub environment is the primary approval gate for all live AMC surfaces. Its configuration must satisfy the following requirements:

| Configuration Item | Required Value | Purpose |
|---|---|---|
| Environment name | `production` | Referenced by `deploy-frontend.yml` and `db-migrate.yml` |
| Required reviewer | CS2 (@APGI-cmy) | Human approval before any production job step executes |
| Required reviewers setting | Enabled — at least 1 required reviewer configured; no workflow step may auto-approve or bypass this gate | Prevents automated production deployments; no workflow job in the `production` environment runs until the reviewer approves |
| Deployment branch policy | `main` branch only | Prevents production deployment from feature/PR branches |
| Wait timer | 0 (no delay after approval) | CS2 approval is sufficient; no additional timer required |
| Environment secrets | `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID`, `SUPABASE_ACCESS_TOKEN` (production value), `SUPABASE_PROJECT_REF` (production value) | Production-scoped secrets; not available in other environments |

**Secret isolation rule**: Production secrets (Supabase service role key, Vercel production token, production `SUPABASE_PROJECT_REF`) must be stored exclusively in the `production` GitHub environment. They must NOT be stored in repository-level secrets or any other environment. This prevents accidental access from CI (PR) or staging jobs.

### 2.2 Staging Environment Configuration

The `staging` GitHub environment (or repository-level secrets for staging) is used for:
- Integration tests (SURF-004 CI gate)
- E2E smoke tests (SURF-004 CI gate)
- Vercel preview deploys (PR)
- DB migration dry-runs or staging schema changes (SURF-003 staging dispatch)

| Configuration Item | Required Value |
|---|---|
| Supabase project | Staging Supabase project (separate from production) |
| Supabase service role key | Staging value only — never production |
| `SUPABASE_PROJECT_REF` | Staging project reference |
| Vercel project | Vercel preview project (or same Vercel project with preview flag) |
| Required reviewers / approval gate | None — staging surfaces have no CS2 approval gate; secrets stored at repository level or in a `staging` environment with no required reviewers |

### 2.3 Environment Isolation Invariants

The following invariants must be enforced at all times:

1. The production Supabase `service_role` key must never be present in a CI (PR) workflow job environment
2. The production Supabase `SUPABASE_PROJECT_REF` must never be used in a staging or CI context
3. The staging Supabase project must be a separate project from production — shared project with environment flags is prohibited
4. A Vercel preview deployment (PR) must never connect to the production Supabase project
5. `deploy-frontend.yml` jobs that reference the `production` GitHub environment may not access staging secrets (and vice versa)

---

## 3. Surface Safety Classification Reference

This section expands DES-006 (Safety Classification) into an actionable constraint table for builders.

| Surface | Safety Class | PR Trigger | Push to main Trigger | Manual Trigger | Production DB Access | Staging DB Access |
|---|---|---|---|---|---|---|
| Lint | CI-safe | ✅ Auto | ✅ Auto | ✅ | ❌ | ❌ |
| Type check | CI-safe | ✅ Auto | ✅ Auto | ✅ | ❌ | ❌ |
| Dependency scan | CI-safe | ✅ Auto | ✅ Auto | ✅ | ❌ | ❌ |
| Unit tests | CI-safe | ✅ Auto | ✅ Auto | ✅ | ❌ | ❌ |
| Integration tests | CI-safe | ✅ Auto | ✅ Auto | ✅ | ❌ | ✅ (read patterns only) |
| E2E smoke tests | CI-safe | ✅ Auto | ✅ Auto | ✅ | ❌ | ✅ |
| Schema verification | CI-safe | ✅ Auto | ✅ Auto | ✅ | ❌ | ✅ (read-only) |
| Vercel preview deploy | Preview-safe | ✅ Auto | ❌ | ✅ | ❌ | ✅ (preview env) |
| DB migration (staging) | Preview-safe | ❌ | ❌ | ✅ | ❌ | ✅ (write) |
| Frontend + API routes production deploy | Live-only | ❌ | ✅ (with gate) | ✅ (with gate) | ❌ (no DB access) | ❌ |
| DB migration (production) | Live-only | ❌ | ❌ | ✅ (with gate) | ✅ (write — gated) | ❌ |
| Live operational validation | Live-only | ❌ | ❌ | Manual only | Read/observe | ❌ |

**Safety boundary enforcement**: CI-safe surfaces MUST NOT be granted production DB credentials. Preview-safe surfaces MUST NOT use the production Supabase project reference. Live-only surfaces MUST be gated by the `production` environment approval or executed manually.

---

## 4. Environment and Network Prerequisites

### 4.1 Prerequisites Before Production Deployment (`deploy-frontend.yml`)

Before `deploy-frontend.yml` executes production-targeting job steps:

| Prerequisite | Verification | Fail-Safe |
|---|---|---|
| CI gate passed on `main` | `ci.yml` must have succeeded on the same commit | `deploy-frontend.yml` configured with `needs: ci` or equivalent dependency |
| CS2 approval | `production` environment reviewer approval | GitHub Actions pauses until approved; production steps do not execute |
| `VERCEL_TOKEN` present | Non-empty environment secret | Workflow step fails with explicit error |
| `VERCEL_ORG_ID` present | Non-empty environment secret | Workflow step fails with explicit error |
| `VERCEL_PROJECT_ID` present | Non-empty environment secret | Workflow step fails with explicit error |

### 4.2 Prerequisites Before Production DB Migration (`db-migrate.yml`)

Before `db-migrate.yml` executes Supabase CLI migration:

| Prerequisite | Verification | Fail-Safe |
|---|---|---|
| CS2 approval | `production` environment reviewer approval | GitHub Actions pauses; migration steps do not execute |
| `SUPABASE_ACCESS_TOKEN` present | Non-empty environment secret | Workflow step fails with explicit error |
| `SUPABASE_PROJECT_REF` present | Non-empty; matches production project reference | Workflow step fails with explicit error |
| Migration files present | `supabase/migrations/` directory exists and is non-empty | Workflow logs warning and skips `supabase db push` if directory is missing or empty; workflow exits with success (empty migration run is a no-op, not an error) |
| Supabase CLI version pinned | Version check in workflow setup step | Workflow fails if pinned version unavailable |

### 4.3 Network Assumptions

| Network Assumption | Validation Point | Fail-Safe |
|---|---|---|
| Vercel API reachable via HTTPS | Vercel CLI exits non-zero if API unreachable | Workflow step fails; no partial deploy |
| Supabase Cloud API reachable via HTTPS | Supabase CLI exits non-zero if API unreachable | Migration workflow fails; no partial migration |
| GitHub Actions runner has internet access | Standard GitHub-hosted runner capability; assumed always present | If absent (GitHub infra failure), all jobs fail |
| No private network / VPN required | Confirmed by topology (all services are SaaS / Cloud) | N/A — no VPN dependency |

---

## 5. Downstream Stage Inheritance Note

- **Stage 6 (QA-to-Red)**: Must include test cases that verify runner type is GitHub-hosted for all CI and deploy surfaces; must test that production environment secrets are not accessible from PR/staging jobs; must test that `deploy-frontend.yml` cannot execute production steps without `production` environment approval; must test that `supabase db push --project-ref $SUPABASE_PROJECT_REF` is the only migration command form present in `db-migrate.yml` and that no `supabase link` step precedes it.

- **Stage 7 (PBFAG)**: Must verify this document is present at its canonical path, is consistent with `deployment-execution-strategy.md`, and that no self-hosted runner label appears in any AMC workflow file without an approved Stage 5a amendment.

- **Stage 8 (Implementation Plan)**: Must specify which builder implements `ci.yml`, `deploy-frontend.yml`, and `db-migrate.yml`; must reference this document for runner type and environment constraints applicable to each workflow.

---

## 6. Sign-Off / Approval Record

| Field | Value |
|---|---|
| **Document** | AMC Runner and Environment Constraints — Stage 5a |
| **Version** | 1.0 |
| **Prepared by** | foreman-v2-agent (POLC_ORCHESTRATION) |
| **Prepared Date** | 2026-04-27 |
| **CS2 Authorization for Stage 5a** | app_management_centre#1133 |
| **Primary DES Reference** | `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` v1.0 |
| **Wave** | amc-stage5a-deployment-execution-strategy-20260427 |
| **Reviewed by** | *Pending CS2 review* |
| **Approved by** | *Pending CS2 approval* |
| **Approval Date** | *Pending* |
| **Approval Reference** | *To be assigned by CS2 on approval* |

---

*AMC Runner and Environment Constraints v1.0 — 2026-04-27 — CS2 authorization: app_management_centre#1133*

# AMC W1 Environment Isolation and Protected-Production Record — 2026-07-22

## Governance Context

| Field | Value |
|---|---|
| Closure issue | #1213 |
| Closure PR | this PR |
| Candidate | `integration-builder` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Blockers closed | W1-BLK-003 — Preview/staging versus production isolation |
| | W1-BLK-004 — Protected production and no-production-mutation controls |
| Authored by | `foreman-v2-agent` (independent evidence record) |
| Date | 2026-07-22 |
| Status | ✅ EVIDENCED |

---

## Purpose

This document records the preview/staging versus production environment
isolation and the protected-production controls that govern W1 work. No secret
values are stored. All claims reference resource names, scoping rules, and
workflow-authorization paths.

---

## 1. Vercel Environment Variable Scoping

| Variable scope tier | Definition | Applies to |
|---|---|---|
| `Production` | Variables set in Vercel project → Settings → Environment Variables → Production scope | Deployed only when the target branch is `main`; never exposed to preview deployments |
| `Preview` | Variables set in Vercel project → Settings → Environment Variables → Preview scope | Available only to preview deployments (PR-triggered); never bleed to production |
| `Development` | Variables set for local `.env` use only | Not consumed by governed CI/CD pipeline |

**Isolation guarantee**: Vercel's environment-variable scoping enforces that
preview deployments cannot read production-scoped variable values, and
production deployments cannot be triggered by a PR-preview workflow path.

**AMC-specific application**: The four `AMC_VERCEL_*` repository secrets are
consumed in the deployment workflow. The workflow will specify a target
environment; preview jobs will pass a preview deployment target and production
jobs will pass a production deployment target. The two paths use separate
environment variable sets within the Vercel project.

---

## 2. Vercel Deployment Protection and Project Ownership

| Control | Definition |
|---|---|
| Project ownership | `app-management-centre` Vercel project is owned by the CS2-controlled Vercel team (Johan Ras). `integration-builder` does not own or administer the Vercel project. |
| Production branch | Production deployments are triggered only when commits land on `main`. |
| Protected production approvals | GitHub branch protection on `main` requires at least one PR approval from a non-candidate reviewer before merge. No direct push to `main` is permitted. |
| Preview-to-production promotion | There is no direct "promote preview to production" button available to `integration-builder`; production is reached only through the merge-to-main path with full branch-protection enforcement. |
| Automation bypass secret | `AMC_VERCEL_AUTOMATION_BYPASS_SECRET` is used only within the governed deployment workflow to bypass Vercel's own deployment protection gate where the PR is already protected by GitHub branch rules. It is not exposed to candidates outside the workflow context. |

---

## 3. Supabase Environment Separation

| Aspect | Non-production (`develop`) | Production |
|---|---|---|
| Project reference | `kkksclwvbmyexpsdyejj` | `icawesooswoqzepcdevg` |
| Branch name | `develop` | `main` / default |
| Credential in workflow secrets | Develop service-role key/connection string available in W1 jobs | **NO** production credential is present in W1 workflow secrets |
| Mutation authority in W1 | Schema changes via governed W1 migration commands against `develop` only | **PROHIBITED** — direct production mutation is not available to W1 workflow jobs |
| Migration path for production | `db-migrate.yml` is a W7 output; production migration requires a separately authorized workflow and CS2-approved W7 delivery | Not in scope for W1 |
| Data isolation | `develop` branch data is independent of production data; no cross-branch data sharing occurs | Production data is fully isolated from preview/staging work |

---

## 4. Protected-Production Approval Path

| Gate | Mechanism | Candidate position |
|---|---|---|
| PR review | At least one approved review required on any PR targeting `main` | `integration-builder` is the PR author; may not self-approve |
| Branch protection | Direct push to `main` and `develop` is blocked; all changes require PR path | Enforced by GitHub repository settings |
| Production Vercel deploy | Triggered only by merge to `main`; requires all PR checks to pass | PR CI must pass; no bypass available to candidate |
| Production Supabase migration | Authorized only through `db-migrate.yml` (W7 output) with explicit CS2-authorized W7 delivery | Out of scope for W1 |
| Rollback authority | CS2 / Foreman; `integration-builder` has no direct production rollback authority | Explicitly prohibited by contract |

---

## 5. PR and Preview Work Cannot Deploy to or Migrate Production

The following controls combine to prevent PR/preview work from reaching production:

1. **Vercel environment variable scoping**: PR-triggered deployments use Preview scope; they cannot access Production-scoped variables.
2. **Vercel production branch gate**: Production deployments require the `main` branch; no PR branch can trigger a production deploy.
3. **GitHub branch protection**: No commit lands on `main` without a reviewed and approved PR.
4. **Supabase credential boundary**: W1 workflow jobs carry the `develop` credential only; they cannot connect to the production Supabase project.
5. **`db-migrate.yml` is a W7 output**: No production migration workflow exists in W1; its creation is explicitly deferred to W7 with separate authorization.

---

## 6. Workflow Ownership Boundary

| Workflow | Wave | Candidate authority in W1 |
|---|---|---|
| `ci.yml` | W1 implementation output | Candidate creates and owns as a W1 deliverable |
| `deploy-frontend.yml` | W1 implementation output | Candidate creates and owns as a W1 deliverable |
| `db-migrate.yml` | W7 implementation output | **OUT OF SCOPE** — candidate has no authority to create or execute in W1 |

Their current absence is not a Stage 9 candidate-readiness failure, consistent
with the Stage 9 checklist rules and the CS2 BLOCKED disposition record.

---

## 7. Resolution of W1-BLK-003 and W1-BLK-004

**W1-BLK-003 — Preview/staging versus production isolation**:

- Vercel preview and production variable scopes are defined and enforced by Vercel project settings.
- Supabase `develop` branch is fully isolated from the production project.
- No PR/preview deployment can use production environment variables.

**W1-BLK-003: CLOSED.**

**W1-BLK-004 — Protected production and no-production-mutation controls**:

- GitHub branch protection enforces PR review before any merge to `main`.
- Vercel production deployment is triggered only by `main` branch landing.
- Supabase production migration is deferred to W7 with a separately authorized workflow.
- `integration-builder` has no mechanism to deploy to or migrate production during W1.

**W1-BLK-004: CLOSED.**

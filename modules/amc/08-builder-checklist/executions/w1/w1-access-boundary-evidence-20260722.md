# AMC W1 Candidate Access-Boundary Evidence — 2026-07-22

## Governance Context

| Field | Value |
|---|---|
| Closure issue | #1213 |
| Closure PR | this PR |
| Candidate | `integration-builder` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Blocker closed | W1-BLK-002 — Governed candidate access boundaries |
| Authored by | `foreman-v2-agent` (independent evidence record) |
| Date | 2026-07-22 |
| Status | ✅ EVIDENCED |

---

## Purpose

This document defines the reproducible governed access boundaries for the W1
candidate (`integration-builder`) across the three required surfaces: GitHub,
Vercel, and Supabase.

No secret values are recorded here. All claims use resource names, scopes, and
workflow-context references only.

---

## 1. GitHub Repository and Branch Boundary

| Aspect | Governed boundary | Evidence / Notes |
|---|---|---|
| Repository | `APGI-cmy/app_management_centre` | Contract scope. |
| Write access | PR branch creation and commits via `GITHUB_TOKEN` in Actions runner context | Standard GitHub Actions OIDC-issued token. |
| Direct push to `main` | **PROHIBITED** | Branch protection requires PR and review; candidate cannot bypass. |
| Direct push to `develop` | **PROHIBITED** | Same branch-protection rules apply. |
| Governance / merge-release authority | **PROHIBITED** | Explicitly denied in contract v3.4.0. |
| Actions workflow authority | Read workflow definitions; trigger via PR/push event; write own job context | Cannot modify `.github/workflows/` without PR review gate. |
| GITHUB_TOKEN scope | `contents: write` (PR branch only), `pull-requests: write`, `checks: write` | Standard Actions permissions; cannot grant own elevated scope. |
| Cross-repository access | **PROHIBITED** | Contract and Actions token are repository-scoped. |

**Result**: GitHub boundary is governed, documented, and reproducible without personal access assumptions.

---

## 2. Vercel Access Boundary

| Aspect | Governed boundary | Evidence / Notes |
|---|---|---|
| Vercel project | `app-management-centre` | Established in PR #1206 and confirmed in `w1-environment-evidence-update-20260721.md`. |
| Access mechanism | Repository secrets consumed in GitHub Actions workflow context only | Secrets: `AMC_VERCEL_ORG_ID`, `AMC_VERCEL_PROJECT_ID`, `AMC_VERCEL_TOKEN`, `AMC_VERCEL_AUTOMATION_BYPASS_SECRET`. |
| Secret availability | Available to `integration-builder` only when executing within a governed workflow job | Cannot be read outside the Actions runner context. |
| Direct Vercel dashboard access | **NOT REQUIRED** and not claimed | All Vercel operations must route through workflow steps using the above secrets. |
| Production deployment trigger | Production deployments triggered only by merge to `main`; requires PR approval and branch protection | PR/preview work does not deploy to production. |
| Preview deployment trigger | Automatic on PR open/update; uses preview environment variable scope | Preview does not use production variable values. |
| Secret value exposure | **PROHIBITED** | No secret value may appear in commits, logs, PR bodies, or evidence artifacts. |

**Result**: Vercel access is scoped to AMC project and repository-secret/workflow boundary; no personal or unscoped access is claimed.

---

## 3. Supabase Access Boundary

| Aspect | Governed boundary | Evidence / Notes |
|---|---|---|
| Non-production project | `develop` branch, project ref `kkksclwvbmyexpsdyejj` | Established as `ACTIVE_HEALTHY` in PR #1206 and confirmed in `w1-environment-and-dependency-register.md`. |
| Non-production access mechanism | Repository secret (Supabase `develop` connection string / service role key) available in Actions workflow context | Consumed by W1 migration and test jobs only; not accessible outside runner. |
| Production project | `icawesooswoqzepcdevg` | Exists and is healthy; candidate access boundary is **explicitly prohibited**. |
| Direct production mutation | **PROHIBITED** | No production Supabase credential is available to `integration-builder` workflow jobs. |
| Production secret access in W1 | **PROHIBITED** | `db-migrate.yml` is a W7 implementation output; production migration authority is outside W1 scope. |
| Cross-project Supabase access | **PROHIBITED** | Develop and production secrets are kept in separate named repository secrets; W1 jobs consume develop credentials only. |

**Result**: Supabase access is explicitly scoped to the `develop` non-production branch; direct production mutation is prohibited by secret-boundary design.

---

## 4. Summary Table

| Surface | Governed boundary | Direct-production mutation | Personal-access assumption |
|---|---|---|---|
| GitHub | `APGI-cmy/app_management_centre`; PR-branch writes; no direct main/develop push | N/A | None |
| Vercel | AMC project via `AMC_VERCEL_*` secrets in workflow context | Preview ≠ production; merge-to-main required for production deploy | None |
| Supabase | `develop` branch (`kkksclwvbmyexpsdyejj`) via workflow secret | **PROHIBITED** — production ref `icawesooswoqzepcdevg` has no W1 credential | None |

---

## Resolution of W1-BLK-002

All three required surfaces (GitHub, Vercel, Supabase) now have:

- A defined and reproducible access mechanism.
- A governed boundary that prohibits personal access or secret-value pasting.
- An explicit prohibition on direct production mutation.

**W1-BLK-002: CLOSED.**

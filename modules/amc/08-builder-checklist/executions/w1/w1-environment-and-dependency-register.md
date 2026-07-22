# AMC W1 Environment and Dependency Readiness Register

## Status

| Field | Value |
|---|---|
| Historical issue / PR | #1205 / merged PR #1206 |
| Reconciliation issue | #1208 |
| Reconciliation PR | #1209 |
| Candidate | `integration-builder` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Overall Status | 🔴 BLOCKED — core resources and non-production Supabase now exist; candidate permission and environment-isolation evidence remain incomplete |

## Register

| ID | Resource / dependency | Current status | Evidence / Notes |
|---|---|---|---|
| ENV-01 | GitHub repository | PARTIAL PASS | Candidate session demonstrated repository/branch visibility; governed write boundary is not independently recorded. |
| ENV-02 | GitHub Actions | PARTIAL PASS | Candidate session demonstrated workflow-run visibility; permission boundary remains incompletely evidenced. |
| ENV-03 | `.github/workflows/ci.yml` ownership | PLANNED W1 OUTPUT | File creation is an implementation deliverable, not a Stage 9 file-existence prerequisite. Owner and path scope must be fixed at appointment. |
| ENV-04 | `.github/workflows/deploy-frontend.yml` ownership | PLANNED W1 OUTPUT | Same rule as ENV-03. |
| ENV-05 | `.github/workflows/db-migrate.yml` ownership | PLANNED W7 OUTPUT | Not a W1 candidate-readiness prerequisite. |
| ENV-06 | Vercel project | PARTIAL PASS | `app-management-centre` exists; candidate-specific governed access is not independently evidenced. |
| ENV-07 | Vercel preview/staging posture | BLOCKED | Preview evidence exists, but environment-variable scoping, protection and production approval boundaries are not fully evidenced in-repo. |
| ENV-08 | Supabase non-production | PASS | `develop`, project ref `kkksclwvbmyexpsdyejj`, exists and is `ACTIVE_HEALTHY`. |
| ENV-09 | Supabase production | PASS — RESOURCE | Production ref `icawesooswoqzepcdevg` exists and is healthy. Candidate no-production-mutation boundary remains separate and unresolved. |
| ENV-10 | Secret management | PARTIAL PASS | AMC Vercel secret names are present; no values are recorded. Preview/staging/production scoping remains incompletely evidenced. |
| ENV-11 | Root `.env.example` | PLANNED W1 OUTPUT | Runtime variable contract must be created during authorized W1 implementation. |
| ENV-12 | Runtime/package tooling | PLANNED W1 OUTPUT | Current root is not the final deployable AMC runtime. Tool/version contract belongs to W1 implementation. |
| ENV-13 | Build-to-Green gate | PASS — CONFIGURATION | `.github/build-wave-phase.json` records `build_to_green_enabled: true`. Implementation-path execution proof remains a later delivery obligation. |
| ENV-14 | Required checks alignment | PARTIAL PASS | Current governance PR checks exist; implementation branch-protection alignment remains to be evidenced at appointment/implementation. |
| ENV-15 | No-production-side-effect boundary | BLOCKED | No authorized W1 CI/deployment workflow exists yet; environment scoping and protected-production behavior remain to be proved. |

## Reconciled Evidence

1. Supabase production project: `icawesooswoqzepcdevg` — healthy.
2. Supabase development branch: `develop`, project ref `kkksclwvbmyexpsdyejj` — healthy.
3. Vercel project: `app-management-centre`.
4. Repository secret names: `AMC_VERCEL_ORG_ID`, `AMC_VERCEL_PROJECT_ID`, `AMC_VERCEL_TOKEN`, `AMC_VERCEL_AUTOMATION_BYPASS_SECRET`.
5. Build-to-Green configuration is enabled.
6. No secret values are stored in repository evidence.

## Residual blockers

- Candidate-authored governed-access confirmation remains incomplete.
- Candidate-specific Vercel and Supabase permission boundaries remain incomplete.
- Preview/staging versus production isolation remains incomplete.
- Protected-production approval and no-production-mutation behavior remain incomplete.

## Resolution Rule

No item may be marked PASS based on assumption, inherited personal access, secret values pasted into a PR, or a workflow name alone. Any unresolved candidate-access or environment-isolation item blocks W1 candidate readiness and Stage 10.

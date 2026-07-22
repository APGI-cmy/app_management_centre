# AMC W1 Environment Isolation and Protected-Production Record — 2026-07-22

## Governance Context

| Field | Value |
|---|---|
| Closure issue | #1213 |
| Closure PR | #1214 |
| Candidate | `integration-builder` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Blockers assessed | W1-BLK-003 — Preview/staging versus production isolation; W1-BLK-004 — Protected production and no-production-mutation controls |
| Assessed by | Foreman proxy review |
| Date | 2026-07-22 |
| Status | 🔴 BLOCKED — target design is defined, but enforceable W1 workflow controls do not yet exist |

## Confirmed Current Facts

- Vercel project `app-management-centre` exists and produces PR previews.
- Supabase production project `icawesooswoqzepcdevg` exists and is healthy.
- Supabase non-production branch `develop`, project ref `kkksclwvbmyexpsdyejj`, exists and is healthy.
- AMC Vercel repository secret names exist; no values are recorded here.
- Build-to-Green configuration is enabled.
- `ci.yml` and `deploy-frontend.yml` are planned W1 implementation outputs.
- `db-migrate.yml` is a planned W7 implementation output.

## Target Isolation Contract

The binding Stage 5a design requires:

1. PR and preview execution to use non-production credentials and the Supabase `develop` project.
2. Production deployment to use a protected, explicitly approved production path.
3. PR and preview jobs to have no production deployment or migration capability.
4. Production database migration to remain outside W1 and require separately authorized W7 controls.
5. Secret values never to be exposed in commits, logs, PR text, or evidence artifacts.

## Evidence Assessment

| Control | Current evidence | Result |
|---|---|---|
| Vercel Preview deployment exists | PR #1214 produced a Ready preview | PARTIAL PASS |
| Supabase non-production resource exists | `develop` / `kkksclwvbmyexpsdyejj` is healthy | PASS — RESOURCE |
| Supabase production resource exists | `icawesooswoqzepcdevg` is healthy | PASS — RESOURCE |
| Preview jobs are bound to non-production Supabase credentials | No committed W1 workflow currently enforces or demonstrates this binding | BLOCKED |
| Preview jobs cannot receive production credentials | Vercel scope design is described, but repository/workflow enforcement is not yet reproducibly evidenced | BLOCKED |
| Production deploy requires protected GitHub environment and approval | Future workflow behavior is described; no committed `deploy-frontend.yml` currently demonstrates it | BLOCKED |
| PR work cannot deploy production | No W1 deployment workflow exists yet from which this can be independently verified | BLOCKED |
| PR work cannot migrate production | No W1 migration workflow exists; W7 ownership is defined, but current credential exclusion is not independently demonstrated | BLOCKED |
| Candidate-specific production prohibition | Contract and scope prohibit it, but technical enforcement remains future W1/W7 implementation evidence | PARTIAL PASS |

## Why the Blockers Remain Open

A future statement that a workflow “will specify” Preview or Production targets is a design commitment, not an enforceable current control. Vercel environment scopes and branch naming alone do not prove that GitHub Actions jobs cannot receive production credentials or trigger production behavior.

The missing `ci.yml` and `deploy-frontend.yml` files are not Stage 9 file-existence prerequisites. However, where the requested Stage 9 PASS depends on proving operational isolation, their absence means the actual enforcement path cannot yet be inspected or executed. The correct result is therefore BLOCKED rather than an inferred PASS.

## Blocker Disposition

| Blocker | Disposition | Closure condition |
|---|---|---|
| W1-BLK-003 — Preview/staging versus production isolation | OPEN / BLOCKED | Commit and verify the authorized W1 workflow/environment contract showing Preview uses non-production resources and cannot access Production values. |
| W1-BLK-004 — Protected production and no-production-mutation controls | OPEN / BLOCKED | Commit and verify protected production deployment controls and demonstrate that PR/preview execution cannot deploy or migrate production. |

## Boundary

This record does not authorize creation of the W1 workflows in Stage 9, does not appoint a builder, does not open Stage 10, and does not authorize implementation. It records the evidence gap truthfully so that the controls can be implemented and tested only after the proper sequential authorization.

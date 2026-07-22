# AMC Stage 9 — W1 Access and Isolation Evidence

## Status

| Field | Value |
|---|---|
| Governing issue | #1210 |
| Governing PR | #1211 |
| Candidate | `integration-builder` |
| Date | 2026-07-22 |
| Evidence verdict | PARTIAL — candidate-specific permission evidence remains required |

## Purpose

Record reproducible evidence for GitHub, Vercel and Supabase boundaries without exposing secret values or claiming permissions that have not been independently demonstrated.

## GitHub evidence

- Repository: `APGI-cmy/app_management_centre`.
- Governed branch: `foreman/amc-stage9-w1-residual-blocker-closure`.
- PR #1211 is open against `main` and is mechanically mergeable.
- The current PR head triggered the full repository gate family successfully, including Agent Bootstrap Inject, Governance Compliance, Builder Delegation Order, Required Checks Alignment, Code Review Closure, Build-to-Green Enforcement, and IAA/ECAP Hard Gate.
- Candidate-specific write permission and branch-protection bypass authority are not inferred from repository visibility or workflow execution.

**GitHub boundary result:** PARTIAL PASS.

## Vercel evidence

- Project: `app-management-centre`.
- Project ID observed from the Vercel GitHub integration: `prj_JMrJ4Zs8KpsA61BDqODEIu6SODzF`.
- Team: `rassie-ras-projects`.
- PR #1211 generated a successful Preview deployment through the Vercel Git integration.
- Repository secret names recorded without values:
  - `AMC_VERCEL_ORG_ID`
  - `AMC_VERCEL_PROJECT_ID`
  - `AMC_VERCEL_TOKEN`
  - `AMC_VERCEL_AUTOMATION_BYPASS_SECRET`
- A successful Preview deployment proves project linkage and preview execution. It does not by itself prove environment-variable scoping, candidate dashboard membership, or protected Production approval.

**Vercel boundary result:** PARTIAL PASS.

## Supabase evidence

- Production project ref: `icawesooswoqzepcdevg`.
- Non-production branch: `develop`.
- Non-production project ref: `kkksclwvbmyexpsdyejj`.
- Both `main` and `develop` report `ACTIVE_HEALTHY` preview-project status.
- The `develop` branch is not the default branch and contains no copied production data.
- No branch merge, rebase, reset, production migration, or production data mutation was performed during this readiness wave.
- Candidate-specific Supabase dashboard or API permission has not been independently demonstrated.

**Supabase resource-isolation result:** PASS.

**Supabase candidate-access result:** BLOCKED.

## Protected-production boundary

The following controls are binding for appointment and implementation:

1. PR and Preview work must use non-production configuration and the Supabase `develop` project ref.
2. PR and Preview work must not deploy to Vercel Production.
3. PR and Preview work must not merge Supabase branches, run production migrations, or mutate production data.
4. Production deployment and migration require an explicit later workflow, protected environment approval, and CS2-authorized release action.
5. `ci.yml` and `deploy-frontend.yml` are W1 implementation outputs; `db-migrate.yml` is a W7 output. Their absence before appointment is not a Stage 9 failure.
6. Secret values must remain in governed secret stores and must never be pasted into issues, PRs, logs, or evidence files.

## Current conclusion

| Blocker | Evidence result |
|---|---|
| W1-BLK-002 — Governed candidate access | BLOCKED — candidate-specific Vercel/Supabase permissions remain unproven |
| W1-BLK-003 — Preview/production isolation | PARTIAL PASS — resource separation and successful Preview are evidenced; Vercel variable scoping/protection still needs candidate acknowledgement and later workflow enforcement |
| W1-BLK-004 — Protected production/no mutation | PASS AS GOVERNING BOUNDARY / BLOCKED AS OPERATIONAL PROOF — policy is explicit; implementation workflows do not yet exist |

No PASS may be inferred for candidate readiness until the candidate personally acknowledges and accepts these boundaries in the fresh re-attestation.
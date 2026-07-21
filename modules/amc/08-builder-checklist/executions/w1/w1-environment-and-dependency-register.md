# AMC W1 Environment and Dependency Readiness Register

## Status

| Field | Value |
|---|---|
| Issue | #1205 |
| PR | #1206 |
| Candidate | `integration-builder` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Overall Status | 🔴 BLOCKED — core resources now exist, but candidate access and preview/staging protection evidence remain incomplete |

---

## Register

| ID | Resource / dependency | Required state | Evidence required | Current status | Owner / resolver |
|---|---|---|---|---|---|
| ENV-01 | GitHub repository | Candidate can read scoped authority, create commits on appointed branch, and view required checks | Candidate-specific access proof | BLOCKED | Repository owner / Foreman |
| ENV-02 | GitHub Actions | Candidate can inspect W1 workflow runs and logs without changing protected governance | Candidate-specific workflow access proof | BLOCKED | Repository owner / Foreman |
| ENV-03 | `.github/workflows/ci.yml` ownership | Named owner and approved modification boundary | Owner acknowledgement and path scope | BLOCKED — W1 deliverable, owner/assignment not yet approved | Foreman / workflow owner |
| ENV-04 | `.github/workflows/deploy-frontend.yml` ownership | Named owner and approved modification boundary | Owner acknowledgement and path scope | BLOCKED — W1 deliverable, owner/assignment not yet approved | Foreman / workflow owner |
| ENV-05 | `.github/workflows/db-migrate.yml` ownership | Named owner and approved modification boundary | Owner acknowledgement and path scope | BLOCKED — W1 deliverable, owner/assignment not yet approved | Foreman / workflow owner |
| ENV-06 | Vercel project | AMC project exists and candidate access is governed | Project name/identifier, environment classification, owner and candidate access proof | PARTIAL PASS — CS2 evidence confirms `app-management-centre` project exists; candidate access not yet proven | CS2 / environment owner / Foreman |
| ENV-07 | Vercel staging/preview posture | Preview is isolated from production | Preview-variable scope, deployment-protection and project/environment evidence without secret values | BLOCKED — framework corrected to `Other`, but preview isolation and protection evidence remain outstanding | Environment owner |
| ENV-08 | Supabase non-production project | Non-production project exists and candidate access is governed | Separate project/branch reference, owner and candidate access proof | BLOCKED — no separate AMC non-production project or branch identified | Environment owner |
| ENV-09 | Supabase production project | Production project exists and candidate has no direct production mutation authority during readiness/build preparation | Project reference, classification, owner and protected approval evidence | PARTIAL PASS — AMC project `icawesooswoqzepcdevg` exists and is ACTIVE_HEALTHY; production classification/protection and candidate boundary still require confirmation | CS2 / environment owner |
| ENV-10 | Secret management | Preview/staging/production secrets are separated and values are never committed | Secret-name inventory and environment-boundary evidence, no values | PARTIAL PASS — Vercel/Supabase integration populated production variables and screenshot exposes names only; preview/staging separation remains unproven | Environment owner |
| ENV-11 | Root `.env.example` | Complete variable contract exists without real secrets | File/path review and variable inventory | BLOCKED — W1 runtime contract not yet produced | Candidate / Foreman |
| ENV-12 | Runtime/package tooling | Required runtime, package manager and CLI versions are known and available | Version contract and candidate tool-access proof | BLOCKED — current root is not the approved deployable AMC runtime; W1 must define the runtime/tool contract | Candidate / Foreman |
| ENV-13 | Build-to-Green gate | Active and blocking for later implementation PRs | Workflow and branch-protection evidence | BLOCKED | Governance / repository owner |
| ENV-14 | Required checks alignment | Required checks are workflow-backed and match branch protection | Current manifest/protection evidence | BLOCKED | Governance / repository owner |
| ENV-15 | No-production-side-effect boundary | PR CI and preview cannot mutate production | Workflow/test evidence plus environment-variable scoping | BLOCKED — no approved W1 CI/deployment workflow yet | Candidate / workflow owner |

---

## Evidence Added on 2026-07-21

1. CS2 created Supabase project `AMC`, project reference `icawesooswoqzepcdevg`.
2. Supabase connector verification records the project as `ACTIVE_HEALTHY` in `eu-west-1`.
3. CS2 created Vercel project `app-management-centre` under the `rassie-ras-projects` team.
4. CS2 linked Supabase to Vercel and Vercel populated production-scoped environment-variable names.
5. CS2 corrected the Vercel Framework Preset from `Vite` to `Other` after the root repository was shown not to contain a Vite runtime.
6. Root directory remains `./`; no valid AMC build/output command is claimed because the deployable W1 runtime has not yet been implemented.
7. Evidence source: `w1-environment-evidence-update-20260721.md` and CS2-provided screenshots. No secret values are recorded.

---

## Resolution Rule

No item may be marked PASS based on assumption, inherited personal access, secret values pasted into the PR, or a workflow name alone. Evidence must identify the governed resource, environment classification, owner, candidate access boundary and applicable protection without exposing credentials.

Any unresolved item blocks W1 candidate readiness and Stage 10.
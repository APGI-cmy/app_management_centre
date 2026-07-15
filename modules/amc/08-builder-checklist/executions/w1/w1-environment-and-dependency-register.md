# AMC W1 Environment and Dependency Readiness Register

## Status

| Field | Value |
|---|---|
| Issue | #1205 |
| PR | Pending PR creation |
| Candidate | `integration-builder` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Overall Status | 🔴 BLOCKED — access and ownership evidence incomplete |

---

## Register

| ID | Resource / dependency | Required state | Evidence required | Current status | Owner / resolver |
|---|---|---|---|---|---|
| ENV-01 | GitHub repository | Candidate can read scoped authority, create commits on appointed branch, and view required checks | Candidate-specific access proof | BLOCKED | Repository owner / Foreman |
| ENV-02 | GitHub Actions | Candidate can inspect W1 workflow runs and logs without changing protected governance | Candidate-specific workflow access proof | BLOCKED | Repository owner / Foreman |
| ENV-03 | `.github/workflows/ci.yml` ownership | Named owner and approved modification boundary | Owner acknowledgement and path scope | BLOCKED | Foreman / workflow owner |
| ENV-04 | `.github/workflows/deploy-frontend.yml` ownership | Named owner and approved modification boundary | Owner acknowledgement and path scope | BLOCKED | Foreman / workflow owner |
| ENV-05 | `.github/workflows/db-migrate.yml` ownership | Named owner and approved modification boundary | Owner acknowledgement and path scope | BLOCKED | Foreman / workflow owner |
| ENV-06 | Vercel preview project | Non-production project exists and candidate access is governed | Project identifier, environment classification, owner and access proof | BLOCKED | Environment owner |
| ENV-07 | Vercel staging posture | Staging/preview is isolated from production | Isolation evidence without secret values | BLOCKED | Environment owner |
| ENV-08 | Supabase non-production project | Non-production project exists and candidate access is governed | Project reference classification, owner and access proof | BLOCKED | Environment owner |
| ENV-09 | Supabase production project | Candidate has no direct production mutation authority during W1 readiness/build preparation | Protected-environment and approval evidence | BLOCKED | Environment owner |
| ENV-10 | Secret management | Preview/staging/production secrets are separated and values are never committed | Secret-source and environment-boundary evidence, no values | BLOCKED | Environment owner |
| ENV-11 | Root `.env.example` | Complete variable contract exists without real secrets | File/path review and variable inventory | BLOCKED | Candidate / Foreman |
| ENV-12 | Runtime/package tooling | Required runtime, package manager and CLI versions are known and available | Version contract and candidate tool-access proof | BLOCKED | Candidate / Foreman |
| ENV-13 | Build-to-Green gate | Active and blocking for later implementation PRs | Workflow and branch-protection evidence | BLOCKED | Governance / repository owner |
| ENV-14 | Required checks alignment | Required checks are workflow-backed and match branch protection | Current manifest/protection evidence | BLOCKED | Governance / repository owner |
| ENV-15 | No-production-side-effect boundary | PR CI and preview cannot mutate production | Test/workflow evidence | BLOCKED | Candidate / workflow owner |

---

## Resolution Rule

No item may be marked PASS based on assumption, inherited personal access, secret values pasted into the PR, or a workflow name alone. Evidence must identify the governed resource, environment classification, owner, candidate access boundary and applicable protection without exposing credentials.

Any unresolved item blocks W1 candidate readiness and Stage 10.

# AMC W1 Candidate Access-Boundary Evidence — 2026-07-22

## Governance Context

| Field | Value |
|---|---|
| Closure issue | #1213 |
| Closure PR | #1214 |
| Candidate | `integration-builder` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Blocker assessed | W1-BLK-002 — Governed candidate access boundaries |
| Assessed by | Foreman proxy review |
| Date | 2026-07-22 |
| Status | 🔴 BLOCKED — boundary design exists; candidate-specific technical permissions and workflow secret availability are not independently demonstrated |

## Purpose

This document records the intended governed access boundaries for GitHub, Vercel and Supabase and distinguishes confirmed facts from controls that still require reproducible evidence. No secret values are recorded.

## 1. GitHub Repository and Branch Boundary

| Aspect | Current finding | Result |
|---|---|---|
| Repository | `APGI-cmy/app_management_centre` | PASS |
| Candidate PR branch activity | Candidate-authored commits exist on PR #1214 | PASS — OBSERVED |
| Direct push to `main` | Prohibited by governance design; branch-setting enforcement not independently captured in this PR | PARTIAL PASS |
| Workflow permissions | Actual permissions vary by repository defaults and each workflow `permissions:` block | PARTIAL PASS |
| Governance / merge-release authority | Prohibited by candidate contract | PASS — AUTHORITY BOUNDARY |
| Cross-repository access | Not required for W1 and not claimed | PASS AS SCOPE |

GitHub repository and PR visibility are demonstrated. Exact governed write and branch-protection enforcement should be cited from repository settings or the relevant workflow files when they exist.

## 2. Vercel Access Boundary

| Aspect | Current finding | Result |
|---|---|---|
| Vercel project | `app-management-centre` exists; PR #1214 produced a Ready Preview | PASS — RESOURCE |
| Repository secret names | `AMC_VERCEL_ORG_ID`, `AMC_VERCEL_PROJECT_ID`, `AMC_VERCEL_TOKEN`, `AMC_VERCEL_AUTOMATION_BYPASS_SECRET` recorded as present without values | PASS — NAME PRESENCE |
| Candidate-specific use of secrets | No committed W1 deployment workflow currently demonstrates that these secrets are available only in the intended governed job context | BLOCKED |
| Preview versus Production credentials | Vercel scope model is described, but AMC-specific variable bindings are not reproducibly inspected in-repo | BLOCKED |
| Direct dashboard access | Not required and not claimed | PASS AS DESIGN |
| Production deployment capability | No W1 workflow exists from which candidate prohibition can be independently verified | BLOCKED |

## 3. Supabase Access Boundary

| Aspect | Current finding | Result |
|---|---|---|
| Non-production resource | `develop`, project ref `kkksclwvbmyexpsdyejj`, exists and is healthy | PASS — RESOURCE |
| Production resource | `icawesooswoqzepcdevg` exists and is healthy | PASS — RESOURCE |
| Candidate access to `develop` | Intended through governed workflow credentials; no W1 workflow currently demonstrates candidate-specific access | BLOCKED |
| Production credential exclusion | Claimed by design, but the actual W1 workflow secret set does not yet exist for inspection | BLOCKED |
| Direct production mutation | Prohibited by contract and scope; technical enforcement remains unproved | PARTIAL PASS |
| Production migration | `db-migrate.yml` belongs to W7 and is outside W1 | PASS AS SCOPE |

## 4. Evidence Rule

A resource name, secret name, contractual prohibition or future workflow design is not equivalent to demonstrated candidate-specific governed access. PASS requires evidence that the candidate can perform required non-production work while production credentials and mutation paths remain unavailable.

No secret values may be used as evidence.

## 5. W1-BLK-002 Disposition

| Required surface | Status |
|---|---|
| GitHub repository / PR branch visibility | PARTIAL PASS |
| Governed GitHub write and protection boundary | PARTIAL PASS |
| Governed Vercel workflow access | BLOCKED |
| Governed Supabase `develop` access | BLOCKED |
| Production credential exclusion | BLOCKED |

**W1-BLK-002: OPEN / BLOCKED.**

Closure requires reproducible evidence of candidate-specific governed non-production access and production exclusion. This record does not authorize implementation or Stage 10.

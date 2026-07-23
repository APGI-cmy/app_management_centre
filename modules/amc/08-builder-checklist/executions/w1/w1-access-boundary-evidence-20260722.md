# AMC W1 Candidate Access-Boundary Evidence

## Governance Context

| Field | Value |
|---|---|
| Model-correction issue / PR | #1215 / #1216 |
| Candidate | `integration-builder` |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Corrected authority | `w1-bootstrap-readiness-model-correction-20260723.md` |
| Assessed by | Foreman proxy |
| Date reassessed | 2026-07-23 |
| Status | ✅ PASS AS STAGE 9 GOVERNED ACCESS ARRANGEMENT |

## 1. Evidence Rule

Stage 9 does not require direct candidate access to secret values or vendor dashboards. It requires a governed arrangement with named owners, existing resources, intended workflow consumers, secret names/scopes and a stop/escalation path. Actual workflow secret consumption and Production exclusion remain mandatory W1 build-exit evidence.

No secret values are recorded.

## 2. GitHub Boundary

| Aspect | Readiness evidence | Result |
|---|---|---|
| Repository | `APGI-cmy/app_management_centre` | PASS |
| Candidate execution path | Governed PR branch under Foreman review | PASS |
| Workflow owner | W1 appointed builder under Foreman supervision | PASS |
| Main/merge authority | Candidate has none; CS2-controlled reviewed PR path | PASS |
| Gate owner | Repository governance workflows / CS2 | PASS |
| Access failure path | Stop and escalate to Foreman/CS2 | PASS |

## 3. Vercel Boundary

| Aspect | Readiness evidence | Result |
|---|---|---|
| Project | `app-management-centre` exists | PASS |
| Owner/custodian | CS2-controlled Vercel account/team | PASS |
| Intended access path | GitHub Actions workflow using repository secret names | PASS AS ARRANGEMENT |
| Secret names | `AMC_VERCEL_ORG_ID`, `AMC_VERCEL_PROJECT_ID`, `AMC_VERCEL_TOKEN`, `AMC_VERCEL_AUTOMATION_BYPASS_SECRET` | PASS — names only |
| Direct dashboard access | Not required and not granted by Stage 9 | PASS |
| Failure path | Stop; Foreman/CS2 verifies secret scope or grants governed correction | PASS |
| Actual secret consumption | Deferred to W1 build-exit evidence | NOT A STAGE 9 PREREQUISITE |

## 4. Supabase Boundary

| Aspect | Readiness evidence | Result |
|---|---|---|
| Non-production resource | `develop`, project ref `kkksclwvbmyexpsdyejj`, healthy | PASS |
| Production resource | `icawesooswoqzepcdevg`, healthy | PASS AS KNOWN PROTECTED RESOURCE |
| Owner/custodian | CS2-controlled Supabase project ownership | PASS |
| Intended W1 access | Governed workflow credentials scoped to non-production | PASS AS ARRANGEMENT |
| Production mutation | Prohibited for W1 candidate | PASS AS AUTHORITY POLICY |
| Production migration | W7 only through separately authorized workflow | PASS AS SCOPE |
| Actual credential binding/exclusion | Deferred to W1 build-exit evidence | NOT A STAGE 9 PREREQUISITE |
| Failure path | Stop before mutation; escalate to Foreman/CS2 | PASS |

## 5. Disposition

The candidate has a complete pre-appointment governed access arrangement:

- named owners/custodians;
- existing required resources;
- named secret surfaces without values;
- intended workflow-mediated access;
- explicit Production prohibition; and
- stop/escalation paths.

**W1-BLK-002: CLOSED AS STAGE 9 READINESS.**

This closure does not prove actual secret consumption, Preview binding or Production exclusion. Those remain mandatory W1 build-exit evidence and must fail the W1 delivery if not demonstrated after appointment.

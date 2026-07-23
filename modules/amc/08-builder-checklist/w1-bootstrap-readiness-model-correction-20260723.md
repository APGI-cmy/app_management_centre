# AMC Stage 9 — W1 Bootstrap Readiness Model Correction

## Status Header

| Field | Value |
|---|---|
| Module | App Management Centre (AMC) |
| Stage | 9 — Builder Checklist |
| Governing issue | #1215 |
| Historical checklist | PR #1204 |
| Historical executions | PRs #1206, #1209 and #1214 |
| Authority | CS2 — Johan Ras |
| Date | 2026-07-23 |
| Status | Approved methodology correction — pending CS2 disposition in this PR |
| Entry condition | NORMAL — Stage 8 approved; this is Stage 9 re-entry/correction under `PRE_BUILD_STAGE_MODEL_CANON.md` §4.4 |

## 1. Purpose

This correction removes a circular dependency in the W1 Stage 9 readiness model. Stage 9 is a pre-appointment gate. It may verify that the candidate, owners, resources, governed access arrangement, design, stop conditions and evidence obligations are ready. It may not require implementation artifacts or executed controls that can only exist after Stage 10, Stage 11 and Stage 12.

This document is a binding amendment to `builder-checklist.md`. Where the historical checklist conflicts with this correction for W1, this document takes precedence until the checklist is consolidated in a later editorial release.

## 2. Non-Weakening Rule

No RED obligation, deployment control or evidence requirement is deleted. Requirements are classified into the correct lifecycle point:

- **Stage 9 readiness evidence** proves that W1 may be safely appointed.
- **Stage 12 W1 build-exit evidence** proves that the authorized implementation actually enforced and executed the required controls.

Moving an obligation to its correct lifecycle point is not a waiver and does not reduce its force.

## 3. Stage 9 W1 Readiness Evidence

A W1 candidate may pass Stage 9 when all of the following are evidenced:

1. Current builder contract and repository authority.
2. Candidate-authored mandatory governance and AMC authority acknowledgement.
3. Clear W1 scope and applicable RED-test comprehension.
4. Named owners/custodians for GitHub, Vercel, Supabase and workflow surfaces.
5. Existing Vercel project and non-production Supabase resource.
6. Secret names, intended scopes and custodians recorded without values.
7. A governed access arrangement stating how the appointed builder will use repository workflows and how access failure is escalated.
8. Preview/staging versus production design, including intended credential and variable scopes.
9. Protected-production policy and approval path.
10. Explicit implementation stop conditions.
11. Objective W1 build-exit evidence plan.
12. Independent Foreman role-fit confirmation.

Stage 9 does not require the candidate to personally read secret values or hold direct dashboard access. Governed workflow-mediated access may satisfy readiness when owners, scopes, intended consumers and escalation paths are explicit.

## 4. Stage 12 W1 Build-Exit Evidence

The following are mandatory W1 implementation outputs and may not be used as Stage 9 entry prerequisites:

- `.github/workflows/ci.yml`;
- `.github/workflows/deploy-frontend.yml`;
- root `.env.example` implementation contract;
- executed CI, type, lint, test and schema logs;
- inspected Preview-to-non-production Supabase binding;
- workflow secret-consumption proof without secret disclosure;
- no-production-side-effect execution proof;
- deployment-target and environment-scope enforcement proof;
- Preview deployment and isolation evidence;
- W1 RED-to-GREEN evidence bundle.

`db-migrate.yml` remains a W7 output and is not a W1 Stage 9 or W1 build-exit prerequisite.

## 5. Corrected Universal Environment Checks

The historical Section 5.E checks are interpreted as follows for pre-appointment Stage 9:

| ID | Corrected Stage 9 requirement |
|---|---|
| E-01 | Repository, branch, runtime/tooling decision and governed execution path are identified and available for appointment. |
| E-02 | Vercel, Supabase and GitHub owners, resource identifiers, secret names/scopes, intended workflow consumers and escalation paths are documented. |
| E-03 | Preview/staging and production design, resources, intended credentials and ownership are separated on paper; executed enforcement remains build-exit evidence. |
| E-04 | Production deployment/migration policy, approval authority and prohibited candidate actions are explicit; executed enforcement remains build-exit evidence. |
| E-05 | Required external resources exist or have an approved visible degraded-mode plan. |
| E-06 | No unresolved **pre-appointment** environment or dependency blocker remains. Implementation proof obligations do not count as Stage 9 blockers. |

## 6. Corrected W1 Seven-Dimension Contract

| Dimension | Binding Stage 9 requirement |
|---|---|
| Scope | Repository/runtime foundation, CI, Preview posture, environment contract, secret separation and initial deployment plumbing are understood and bounded. |
| Authority inputs | Stage 5a, Stage 8, TR-1910 and applicable Stage 6 RED obligations are identified and accepted. |
| RED obligations | `QA-DEPLOY-001/002/003/004/006/007/010` plus applicable QA-CONFIG/QA-DES obligations remain mandatory for W1 implementation. |
| Dependencies / prerequisites | Owners, existing resources, governed access arrangement, intended workflow ownership, secret-name scopes and escalation paths are explicit. |
| Stage 9 evidence | Candidate attestation, owner/resource register, access arrangement, environment design, production-protection policy, stop conditions and build-exit evidence plan. |
| Stop conditions | Missing owner/resource; access arrangement failure; secret disclosure; production credential exposure; architecture drift; inactive required gates; ambiguity. |
| Stage 9 exit criteria | Candidate can identify every owner, resource, workflow output, RED obligation, stop condition and required build-exit evidence artifact; no pre-appointment blocker remains. |

## 7. Corrected W1 Checks

| ID | Stage 9 readiness check |
|---|---|
| W1-01 | Candidate understands the intended ownership and purpose of `ci.yml` and `deploy-frontend.yml`, and understands `db-migrate.yml` belongs to W7. |
| W1-02 | Candidate understands the design rule that PR/Preview work must not mutate Production or receive Production credentials/data, and accepts this as a mandatory W1 build-exit proof obligation. |
| W1-03 | Candidate understands the root `.env.example` contract and no-committed-secret rule; the file itself is a W1 implementation output. |
| W1-04 | Candidate identifies the required CI/type/lint/test/schema/Preview/environment evidence to be produced during W1. |
| W1-05 | Every pre-appointment dependency and stop condition has an owner, governed arrangement and escalation path. |
| W1-06 | Stage 9 exit criteria and later W1 build-exit criteria are separately understood and objectively verifiable. |

## 8. Final Boundary

This correction does not create Stage 10, appoint a builder, authorize implementation, create workflow files, run migrations, deploy Production or begin Stage 12. Stage 10 may open only after a corrected Stage 9 candidate assessment reaches PASS and CS2 explicitly authorizes progression.

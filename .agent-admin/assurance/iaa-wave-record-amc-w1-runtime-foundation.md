# AMC W1 Runtime Foundation — IAA Wave Record

## Identity

| Field | Value |
|---|---|
| Repository | `APGI-cmy/app_management_centre` |
| Governing issue | #1217 |
| Stage | 10 — IAA Pre-Brief |
| Wave | W1 — Runtime Foundation and Environment Setup |
| Candidate | `integration-builder` — nominated only |
| Orchestrating Foreman | `foreman-v2-agent` |
| Stage 9 authority | Merged PR #1216 / merge commit `95271c288b2ba95e3a58cb4916d6a617cef90036` |
| Entry condition | NORMAL — Stage 9 accepted; Stage 10 explicitly authorized by CS2 |
| Builder appointed | false |
| Implementation authorized | false |

## PRE-BRIEF
IAA_PREFLIGHT_BRIEF

```json
{
  "schema_version": "1.0.0",
  "wave": "amc-w1-runtime-foundation",
  "issue": "#1217",
  "branch": "foreman/amc-stage10-w1-iaa-prebrief",
  "qualifying_tasks": [
    "Establish the repository and runtime foundation required by W1",
    "Implement .github/workflows/ci.yml",
    "Implement .github/workflows/deploy-frontend.yml",
    "Validate or update the existing root .env.example without secrets",
    "Prove CI, Preview deployment, environment isolation and Production protection",
    "Produce the complete W1 RED-to-GREEN evidence bundle"
  ],
  "required_build_gates": [
    "CI type, lint, test and schema enforcement",
    "Vercel Preview deployment validation",
    "Preview-to-Supabase-develop binding validation",
    "Production credential exclusion validation",
    "No-Production-side-effect validation",
    "Code review closure and Build-to-Green enforcement"
  ],
  "expected_qa_scope": [
    "Applicable QA-DEPLOY controls",
    "Applicable QA-CONFIG controls",
    "Applicable QA-DES controls",
    "All W1 PBFAG and Stage 8 imported conditions",
    "No regression, no test debt and stop-and-fix behavior"
  ],
  "high_risk_failure_modes": [
    "Preview or PR jobs receive Production credentials",
    "Preview binds to Production Supabase instead of develop",
    "PR work can deploy to or mutate Production",
    "Secret values appear in commits, logs, comments or evidence",
    "CI omits or weakens required checks",
    "Production deployment is not protected and explicitly approved",
    "Architecture or scope drifts from approved authority",
    "Tests or gates are bypassed, diluted or converted into debt",
    "Evidence is asserted without reproducible proof",
    "GREEN is claimed while any applicable RED obligation remains unmet"
  ],
  "required_builder_evidence": [
    "Committed ci.yml and deploy-frontend.yml with explicit permissions, triggers, environments and secret references",
    "Non-secret .env.example validation or update evidence",
    "Reproducible CI, type, lint, test and schema results",
    "Inspected workflow-to-secret mapping without secret disclosure",
    "Vercel Preview deployment evidence",
    "Proof Preview uses Supabase develop",
    "Proof Production credentials are unavailable to PR and Preview jobs",
    "Proof PR and Preview work cannot deploy or migrate Production",
    "No-Production-side-effect evidence",
    "Traceability from every applicable W1 RED obligation to implementation evidence",
    "W1 RED-to-GREEN evidence bundle and prehandover record"
  ],
  "required_foreman_qp_checks": [
    "Verify scope matches the Stage 8 W1 contract",
    "Verify every applicable RED ID is mapped to evidence",
    "Verify workflow permissions and environment scopes are least-privilege and explicit",
    "Inspect Preview/non-production and Production bindings separately",
    "Verify no secret values are exposed",
    "Verify Production deployment and migration controls remain protected",
    "Verify all required checks run on the implementation head and are green",
    "Verify no unresolved review conversation remains",
    "Verify no test weakening, bypass, debt or hidden deferred work exists",
    "Verify tracker, evidence index and handover records reflect the actual final state"
  ],
  "ecap_required": true,
  "final_iaa_focus": [
    "Conformance with accepted architecture, deployment and QA authorities",
    "All applicable RED obligations genuinely GREEN",
    "Preview bound only to non-production resources",
    "Production credentials and mutation paths excluded from PR and Preview execution",
    "CI and deployment evidence reproducible",
    "No regression, test debt, scope drift or false assurance",
    "Final head and evidence carrier correctly bound"
  ],
  "result": "PREFLIGHT_BRIEF_COMPLETE"
}
```

### 1. Purpose

Define the independent-assurance expectations for W1 before any builder appointment or implementation authority is issued.

This pre-brief is assurance planning only. It does not appoint or delegate `integration-builder`, create implementation outputs, authorize Stage 12, run migrations or deploy Production.

### 2. Qualifying W1 Scope

The later appointed builder will be expected to implement and prove:

- repository/runtime foundation and required tooling posture;
- `.github/workflows/ci.yml`;
- `.github/workflows/deploy-frontend.yml`;
- validation and any required update of the existing root `.env.example` while keeping it non-secret;
- CI/type/lint/test/schema enforcement;
- Vercel Preview deployment posture;
- actual Preview-to-Supabase-`develop` binding;
- Production credential exclusion;
- no-Production-side-effect behavior;
- deployment/isolation inspection evidence;
- the W1 RED-to-GREEN evidence bundle.

`db-migrate.yml` remains a W7 output and is outside W1.

### 3. Explicit Exclusions

W1 does not authorize:

- Production database migrations;
- direct Production mutation by PR or Preview work;
- unreviewed Production deployment;
- secret disclosure in code, logs, comments or evidence;
- weakening, bypassing or deleting tests and gates;
- scope expansion beyond Stage 8 W1;
- Stage 11 appointment or Stage 12 implementation before separate CS2 authorization.

### 4. Binding Inputs

The W1 builder and Foreman must apply:

- Stage 5a Deployment Execution Strategy and validation matrix;
- Stage 6 QA-to-Red specification and RED catalog;
- Stage 8 implementation plan, wave breakdown and condition-import matrix;
- accepted Stage 9 W1 bootstrap-readiness correction;
- candidate readiness checklist and re-attestation;
- current repository governance, builder contract and Build-to-Green controls.

### 5. Applicable QA and RED Focus

The final build evidence must trace all applicable W1 obligations, including:

- QA-DEPLOY controls for CI, Preview deployment, environment separation, secret handling, deployment protection and no-Production side effects;
- applicable QA-CONFIG controls for environment contracts and non-secret configuration;
- applicable QA-DES controls for deployment execution strategy adherence;
- all W1 PBFAG and Stage 8 imported conditions;
- no regression, no test debt and stop-and-fix behavior.

The builder may not self-declare GREEN. Foreman quality control and independent IAA assurance remain required.

### 6. High-Risk Failure Modes

IAA must treat the following as blocking:

1. Preview or PR jobs receive Production credentials.
2. Preview binds to Production Supabase rather than `develop`.
3. PR work can deploy to or mutate Production.
4. Secret values appear in commits, logs, comments or evidence.
5. CI omits or weakens required type, lint, test or schema checks.
6. Production deployment lacks a protected and explicitly approved path.
7. Runtime, architecture or deployment scope drifts from approved artifacts.
8. Tests or gates are disabled, bypassed, diluted or converted into debt.
9. Evidence is asserted without reproducible logs, configuration inspection or deployment proof.
10. A GREEN claim is made while any applicable RED obligation remains unmet.

### 7. Required Builder Evidence

The later W1 implementation PR must provide, at minimum:

- committed workflow files with explicit permissions, triggers, environments and secret references;
- root `.env.example` validation/update evidence and proof that no secret values are committed;
- reproducible CI/type/lint/test/schema results;
- inspected workflow-to-secret mapping without secret disclosure;
- Vercel Preview deployment evidence;
- proof that Preview uses the Supabase `develop` resource;
- proof that Production credentials are unavailable to PR/Preview jobs;
- proof that PR/Preview work cannot deploy or migrate Production;
- no-Production-side-effect evidence;
- traceability from W1 RED obligations to implementation evidence;
- W1 RED-to-GREEN evidence bundle and prehandover record.

### 8. Foreman Quality-Control Checks

Before handover to IAA, the Foreman must independently verify:

- scope matches the Stage 8 W1 contract;
- every applicable RED ID is mapped to evidence;
- workflow permissions and environment scopes are least-privilege and explicit;
- Preview/non-production and Production bindings are separately inspected;
- no secret values are exposed;
- Production deployment and migration controls remain protected;
- all required checks run on the implementation head and are green;
- no unresolved review conversation remains;
- no test weakening, bypass, debt or hidden deferred work exists;
- tracker, evidence index and handover records reflect the actual final state.

### 9. ECAP Requirement

ECAP is required for protected governance and assurance paths. ECAP may administer ceremony only; it may not author implementation evidence, candidate readiness, Foreman quality decisions or IAA findings.

### 10. Final IAA Focus

Final IAA review must determine whether:

- the W1 implementation satisfies the accepted architecture, deployment and QA authorities;
- all applicable RED obligations are genuinely GREEN;
- Preview is bound to non-production resources;
- Production credentials and mutation paths are excluded from PR/Preview execution;
- CI and deployment evidence is reproducible;
- there is no regression, test debt, scope drift or false assurance;
- the final head and evidence carrier are correctly bound.

### 11. Stop and Escalation Conditions

Stop immediately and escalate to the Foreman/CS2 when:

- an owner, resource, credential scope or environment binding is unclear;
- required governed access is unavailable;
- a Production credential or mutation route is visible to PR/Preview work;
- any applicable gate or RED obligation fails;
- a secret may have been exposed;
- architecture or scope authority conflicts;
- implementation evidence cannot be reproduced;
- an agent exceeds its role or authority.

### 12. Stage 10 Disposition

`PREFLIGHT_BRIEF_COMPLETE`

This disposition means the W1 assurance expectations are sufficiently defined for Stage 11 consideration. It does not appoint the builder or authorize Stage 12.

## Current Boundary

- Stage 10 pre-brief: COMPLETE and accepted through merged PR #1218; final assurance token `IAA-session-1218-R2-20260723-PASS`.
- Stage 11 builder appointment: NOT STARTED; requires separate explicit CS2 authorization.
- Stage 12 implementation: BLOCKED pending Stage 11 appointment.

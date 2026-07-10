# AMC Builder Checklist — Stage 9

## Status Header

| Field | Value |
|---|---|
| Module | App Management Centre (AMC) |
| Stage | 9 — Builder Checklist |
| Version | 1.0 |
| Status | 🟡 Produced for CS2 Review — Not Executed Against Any Builder Candidate |
| Governing Issue | `app_management_centre#1203` |
| Governing PR | Pending PR creation |
| Foreman | `foreman-v2-agent` |
| Authority | CS2 — Johan Ras |
| Date Produced | 2026-07-10 |
| Canonical Location | `modules/amc/08-builder-checklist/builder-checklist.md` |
| Policy Authority | `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0 — Stage 9 |

---

## 1. Purpose

This Stage 9 artifact converts the CS2-approved Stage 8 Implementation Plan into explicit builder-readiness gates for AMC delivery waves W1 through W8.

It verifies, before any appointment or implementation work, that a proposed builder candidate has the correct contract, authority, scope comprehension, RED-test understanding, dependency access, evidence obligations, and protocol discipline for the wave they may later be appointed to execute.

This PR produces the checklist only. It does not evaluate or appoint a builder candidate, create the Stage 10 IAA Pre-Brief, issue a delegation order, authorize implementation, or certify AMC build-ready.

---

## 2. Stage Entry Authority

Stage 9 is opened under the following authority chain:

1. PR #1200 produced the Stage 8 Implementation Plan, Wave Breakdown, and Condition Import Matrix.
2. PR #1202 merged the Stage 8 CS2 disposition.
3. `modules/amc/07-implementation-plan/cs2-decision-record-stage-8.md` records Stage 8 as **Approved with Conditions**.
4. The Stage 8 decision explicitly authorizes Stage 9 to be opened as a separate governed Builder Checklist wave.

| Upstream stage | Current authority input | Stage 9 treatment |
|---|---|---|
| Stage 1 — App Description | `modules/amc/00-app-description/app-description.md` | Binding product purpose and ownership baseline |
| Stage 2 — UX Workflow & Wiring | `modules/amc/01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md` and wiring artifacts | Binding journey, state, action, and surface baseline |
| Stage 3 — FRS | `modules/amc/02-frs/functional-requirements-specification.md` plus FR-1900 addendum | Binding functional and acceptance baseline |
| Stage 4 — TRS | `modules/amc/03-trs/technical-requirements-specification.md` plus TR-1900/TR-1910 addendum | Binding technical and deployment baseline |
| Stage 5 — Architecture | Stage 5 canonical pack and functional-delivery architecture map | Binding component, route, state, audit, authority, boundary, and degraded-mode baseline |
| Stage 5a — Deployment Execution | Stage 5a strategy and validation matrix | Binding workflow, environment, migration, rollback, release, health, and evidence baseline |
| Stage 6 — QA-to-Red | QA-to-Red specification, red-test catalog, and QA-FD/QA-DEPLOY expansion matrix | Binding pre-implementation failure and later GREEN criteria |
| Stage 7 — PBFAG | Stage 7 PBFAG pack and retrofit evidence rows | Binding pre-build blocker and evidence baseline |
| Stage 8 — Implementation Plan | Implementation Plan, Wave Breakdown, Condition Import Matrix, and Stage 8 CS2 decision | Binding W1–W8 sequence and carry-forward conditions |

**Stage-entry result**: Stage 9 artifact production is authorized. Candidate readiness is not yet evaluated.

---

## 3. Pass, Fail, and Blocking Semantics

1. A candidate passes only when every applicable check for their proposed wave is marked PASS with evidence.
2. A single FAIL, unresolved ambiguity, missing authority reference, missing RED-test mapping, inaccessible dependency, unavailable environment, inactive blocking gate, or unapproved deviation blocks progression.
3. `N/A` is permitted only with written rationale and Foreman acceptance. It may not be used to avoid a binding Stage 8 condition.
4. No candidate may self-approve role fit, scope sufficiency, exceptions, or deviations.
5. Checklist production is not checklist execution.
6. Stage 10 remains blocked until this artifact is approved and the proposed candidate set has passed the applicable readiness checks.
7. No build-readiness claim may be made before Stage 10 and Stage 11 are separately completed.

---

## 4. Universal Candidate Record

Complete one record per proposed builder candidate before Stage 10.

| Field | Required value |
|---|---|
| Builder candidate agent ID | Exact agent identifier |
| Agent contract path | Exact repository path |
| Agent contract version | Current version |
| Proposed builder class | UI / API / Schema / QA / Integration / Infrastructure / other approved builder class |
| Proposed wave scope | One or more explicit W1–W8 scopes |
| Candidate evaluation issue/PR | Exact governed reference |
| Evaluation date | `YYYY-MM-DD` |
| Evaluated by | Foreman identifier |
| Final candidate result | PASS / FAIL / BLOCKED |

No candidate record exists at Stage 9 artifact-production time.

---

## 5. Universal Builder Readiness Checks

### A. Agent Contract and Authority

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| A-01 | Candidate contract exists at the declared path | [ ] PASS [ ] FAIL | |
| A-02 | Contract is current and not superseded | [ ] PASS [ ] FAIL | |
| A-03 | Contract declares builder-class authority for the proposed work | [ ] PASS [ ] FAIL | |
| A-04 | Contract scope includes this repository and the proposed technical domain | [ ] PASS [ ] FAIL | |
| A-05 | Contract contains required Phase 1 / FAIL-ONLY-ONCE preflight obligations | [ ] PASS [ ] FAIL | |
| A-06 | Candidate has no authority to modify governance canon, agent contracts, or approval records | [ ] PASS [ ] FAIL | |
| A-07 | Candidate understands that appointment authority remains with Foreman after Stage 10 | [ ] PASS [ ] FAIL | |

**Section A outcome**: [ ] PASS [ ] FAIL [ ] NOT EXECUTED

### B. Governance and Build Philosophy Comprehension

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| B-01 | Candidate has read `PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0 | [ ] PASS [ ] FAIL | |
| B-02 | Candidate has read `BUILD_PHILOSOPHY.md` and accepts One-Time Build / Zero Regression / 100% GREEN | [ ] PASS [ ] FAIL | |
| B-03 | Candidate accepts STOP-AND-FIX on any blocking defect or ambiguity | [ ] PASS [ ] FAIL | |
| B-04 | Candidate understands Foreman plans, delegates, controls, and verifies but does not implement | [ ] PASS [ ] FAIL | |
| B-05 | Candidate understands ECAP is administrative and IAA is independent | [ ] PASS [ ] FAIL | |
| B-06 | Candidate accepts that implementation-only work is not handover | [ ] PASS [ ] FAIL | |
| B-07 | Candidate accepts that no skipped, todo, stub-only, placeholder, or trivially passing test may count as completion | [ ] PASS [ ] FAIL | |

**Section B outcome**: [ ] PASS [ ] FAIL [ ] NOT EXECUTED

### C. AMC Scope and Boundary Comprehension

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| C-01 | Candidate can summarise AMC as the estate-level executive control centre and control plane | [ ] PASS [ ] FAIL | |
| C-02 | Candidate can identify the AMC, AIMC, AIMCC, KUC, knowledge/memory, Foreman, specialist, and push boundaries relevant to their wave | [ ] PASS [ ] FAIL | |
| C-03 | Candidate understands that all AI actions route through AIMC and no direct model-provider SDK may be introduced | [ ] PASS [ ] FAIL | |
| C-04 | Candidate understands that knowledge uploads route through KUC and AMC does not own canonical knowledge content | [ ] PASS [ ] FAIL | |
| C-05 | Candidate understands the canonical ARC model and prohibited reintroduction of `arc_triggers` or non-canonical ARC routes/events | [ ] PASS [ ] FAIL | |
| C-06 | Candidate can name every material route, action, state, audit, authority, and degraded-mode obligation in their proposed scope | [ ] PASS [ ] FAIL | |
| C-07 | Candidate confirms no unresolved scope ambiguity exists | [ ] PASS [ ] FAIL | Record any ambiguity in Section 9 |

**Section C outcome**: [ ] PASS [ ] FAIL [ ] NOT EXECUTED

### D. QA-to-Red Comprehension

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| D-01 | Candidate has reviewed the Stage 6 QA-to-Red specification and red-test catalogs | [ ] PASS [ ] FAIL | |
| D-02 | Candidate can identify all existing and QA-FD/QA-DEPLOY tests applicable to the proposed wave | [ ] PASS [ ] FAIL | |
| D-03 | Candidate understands that applicable tests must be RED because implementation is absent before build | [ ] PASS [ ] FAIL | |
| D-04 | Candidate accepts that tests may not be weakened, skipped, rewritten around the implementation, or made trivially green | [ ] PASS [ ] FAIL | |
| D-05 | Candidate understands that a GREEN result obtained through a forbidden shortcut is a failure | [ ] PASS [ ] FAIL | |
| D-06 | Candidate accepts responsibility for producing wave-specific QA-to-Green evidence without modifying governance-owned test intent | [ ] PASS [ ] FAIL | |

**Section D outcome**: [ ] PASS [ ] FAIL [ ] NOT EXECUTED

### E. Environment, Dependency, and Tool Readiness

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| E-01 | Required repository, branch, tools, and package/runtime access are available | [ ] PASS [ ] FAIL | |
| E-02 | Required Vercel, Supabase, GitHub environment, and secret access is available or governed access is explicitly arranged | [ ] PASS [ ] FAIL | |
| E-03 | Preview, staging, and production resources are clearly separated | [ ] PASS [ ] FAIL | |
| E-04 | Production deploy and migration remain protected/manual where required | [ ] PASS [ ] FAIL | |
| E-05 | External dependencies required by the wave are available or have an approved visible degraded-mode path | [ ] PASS [ ] FAIL | |
| E-06 | No unresolved dependency or environment blocker exists | [ ] PASS [ ] FAIL | |

**Section E outcome**: [ ] PASS [ ] FAIL [ ] NOT EXECUTED

### F. Evidence and Protocol Commitments

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| F-01 | Candidate will produce user-visible, API, state, audit/provenance, authority, degraded-mode, test, and deployment evidence applicable to the wave | [ ] PASS [ ] FAIL | |
| F-02 | Candidate will preserve exact canonical route, endpoint, event, table, and workflow names unless CS2 approves a change | [ ] PASS [ ] FAIL | |
| F-03 | Candidate will not claim completion without the complete evidence package | [ ] PASS [ ] FAIL | |
| F-04 | Candidate will not create or expose production secrets in PR, preview, or staging contexts | [ ] PASS [ ] FAIL | |
| F-05 | Candidate will stop and escalate any required architecture, requirement, test, or deployment change before implementation continues | [ ] PASS [ ] FAIL | |
| F-06 | Candidate will file required PREHANDOVER proof only at the correct later ceremony point | [ ] PASS [ ] FAIL | |

**Section F outcome**: [ ] PASS [ ] FAIL [ ] NOT EXECUTED

### G. Blocking Gate Readiness

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| G-01 | Build-to-Green enforcement is active and blocking for implementation PRs, not paused or advisory | [ ] PASS [ ] FAIL | |
| G-02 | Required PR checks are present and workflow-backed | [ ] PASS [ ] FAIL | |
| G-03 | Builder delegation order evidence will be PR-scoped | [ ] PASS [ ] FAIL | |
| G-04 | Canonical IAA pre-brief will exist before appointment and first implementation commit | [ ] PASS [ ] FAIL | |
| G-05 | Handover/completion language remains prohibited until the proper later gate | [ ] PASS [ ] FAIL | |
| G-06 | No known gate bypass or governance self-repair exception is being used to avoid normal implementation controls | [ ] PASS [ ] FAIL | |

**Section G outcome**: [ ] PASS [ ] FAIL [ ] NOT EXECUTED

### H. Foreman Role-Fit Assessment

> Completed by Foreman only. A candidate may not self-assess this section.

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| H-01 | Candidate competencies match the technical requirements of the proposed wave | [ ] PASS [ ] FAIL | |
| H-02 | Candidate contract authority matches the proposed scope without overreach | [ ] PASS [ ] FAIL | |
| H-03 | Candidate accurately demonstrates AMC scope and boundary comprehension | [ ] PASS [ ] FAIL | |
| H-04 | Candidate accurately demonstrates applicable RED-test comprehension | [ ] PASS [ ] FAIL | |
| H-05 | Candidate has no unresolved performance, integrity, or FAIL-ONLY-ONCE concern affecting the assignment | [ ] PASS [ ] FAIL | |
| H-06 | Foreman confirms this candidate is the correct role fit for the proposed wave | [ ] PASS [ ] FAIL | |

**Section H outcome**: [ ] PASS [ ] FAIL [ ] NOT EXECUTED

---

## 6. Wave-Specific Readiness Gates

The following checks supplement Sections A–H. Each proposed candidate must pass the checks for every wave assigned to them.

### W1 — Runtime Foundation and Environment Setup

**Scope**: Repository/runtime foundation, unified Next.js frontend/API posture, CI, preview, environment contract, secret separation, and initial deployment plumbing.

**Applicable RED obligations**: `QA-DEPLOY-001`, `QA-DEPLOY-002`, `QA-DEPLOY-003`, `QA-DEPLOY-004`, `QA-DEPLOY-006`, `QA-DEPLOY-007`, `QA-DEPLOY-010`, and applicable QA-CONFIG/QA-DES controls.

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W1-01 | Candidate understands the required workflow families: `ci.yml`, `deploy-frontend.yml`, and `db-migrate.yml` | [ ] PASS [ ] FAIL | |
| W1-02 | Candidate understands PR CI may not mutate production | [ ] PASS [ ] FAIL | |
| W1-03 | Candidate understands preview/staging resources and secrets must be isolated from production | [ ] PASS [ ] FAIL | |
| W1-04 | Candidate understands the root `.env.example` contract and prohibition on committed secrets | [ ] PASS [ ] FAIL | |
| W1-05 | Candidate can identify required CI, type, lint, test, schema, and preview evidence | [ ] PASS [ ] FAIL | |
| W1-06 | Candidate accepts that missing workflow ownership, inaccessible environment configuration, or inactive blocking Build-to-Green enforcement blocks the wave | [ ] PASS [ ] FAIL | |

**W1 exit criterion**: Candidate, scope, environment prerequisites, RED tests, and later evidence duties are unambiguous and achievable. No foundation work is authorized by this checklist.

### W2 — Auth, Tenant, Authority, and Audit Baseline

**Scope**: Supabase Auth, tenant isolation, RLS, server-side authority, state ownership, and atomic audit/provenance behavior.

**Applicable RED obligations**: QA-AUTH/RLS/audit families, `QA-FD-003`, `QA-FD-004`, `QA-FD-005`, `QA-ARCH-004`, and `QA-ARCH-005`.

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W2-01 | Candidate understands tenant isolation and RLS must be enforced at the data boundary | [ ] PASS [ ] FAIL | |
| W2-02 | Candidate understands authority must be verified server-side before consequential side effects | [ ] PASS [ ] FAIL | |
| W2-03 | Candidate can identify the state owner/projection and audit event for each consequential action in scope | [ ] PASS [ ] FAIL | |
| W2-04 | Candidate understands audit/provenance must be committed before success is returned | [ ] PASS [ ] FAIL | |
| W2-05 | Candidate can identify negative-path evidence for unauthorized, cross-tenant, and boundary-bypass attempts | [ ] PASS [ ] FAIL | |
| W2-06 | Candidate accepts that unresolved identity, tenant, RLS, authority, or audit ambiguity blocks the wave | [ ] PASS [ ] FAIL | |

**W2 exit criterion**: The candidate can explain and later prove all auth, tenancy, authority, state, and audit boundaries without client-side bypass.

### W3 — Core AMC Routes and Material Surfaces

**Scope**: Material AMC routes, visible actions, route/service bindings, state/projection ownership, audit events, and visible degraded states.

**Applicable RED obligations**: `QA-FD-001` through `QA-FD-009`, applicable route/contract tests, and PBFAG-FD rows.

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W3-01 | Candidate can enumerate every material route and action in the assigned scope | [ ] PASS [ ] FAIL | |
| W3-02 | Every material CTA has an API/service target or explicit read-only classification | [ ] PASS [ ] FAIL | |
| W3-03 | Every backend capability is bound to a visible journey/state or has explicit approved backend-only status | [ ] PASS [ ] FAIL | |
| W3-04 | Every consequential action has state/projection and audit ownership | [ ] PASS [ ] FAIL | |
| W3-05 | Every external dependency has visible unavailable/stale/degraded behavior | [ ] PASS [ ] FAIL | |
| W3-06 | Candidate accepts that dead CTA, omitted route, route/event drift, placeholder leakage, or hidden degraded mode blocks the wave | [ ] PASS [ ] FAIL | |

**W3 exit criterion**: The candidate can trace assigned routes from UI action to API/service, authority, state, audit, visible result, and degraded state.

### W4 — First Complete `/alerts` Acknowledgement Journey

**Scope**: First fully evidenced E2E path from `/alerts` UI through API, authority, state, audit, realtime propagation, and visible confirmation.

**Applicable RED obligations**: `QA-FD-010` plus applicable `QA-FD-003`, `QA-FD-004`, `QA-FD-005`, audit, authority, realtime, and degraded-mode tests.

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W4-01 | Candidate understands the exact acknowledgement user journey and allowed actor authority | [ ] PASS [ ] FAIL | |
| W4-02 | Candidate can identify the canonical API route, state transition, audit event, realtime channel, and visible result | [ ] PASS [ ] FAIL | |
| W4-03 | Candidate understands unauthorized acknowledgement must fail before side effects | [ ] PASS [ ] FAIL | |
| W4-04 | Candidate understands successful acknowledgement requires atomic state/audit closure | [ ] PASS [ ] FAIL | |
| W4-05 | Candidate can identify the required E2E evidence bundle: UI, API, authority, state, audit, realtime, and visible confirmation | [ ] PASS [ ] FAIL | |
| W4-06 | Candidate accepts that partial journey proof or mocked-only boundary proof blocks W4 closure | [ ] PASS [ ] FAIL | |

**W4 exit criterion**: The candidate is ready to implement and later prove the first complete AMC E2E journey without bypass, partial completion, or hidden failure.

### W5 — ARC, Approvals, Interventions, and Executive Workflow

**Scope**: ARC Governance Console, approvals, interventions, quota lifecycle, executive workflows, authority, state machines, and audit evidence.

**Applicable RED obligations**: `QA-ARC-001` through `QA-ARC-006`, `QA-FD-003`, `QA-FD-004`, `QA-FD-005`, `QA-FD-014`, `QA-FD-015`, and applicable PBFAG-FD rows.

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W5-01 | Candidate understands `arc_classifications` is a distinct canonical table | [ ] PASS [ ] FAIL | |
| W5-02 | Candidate understands canonical `/api/arc/{id}` action routes and `ARC_ITEM_*` events | [ ] PASS [ ] FAIL | |
| W5-03 | Candidate understands ARC state transitions must occur through server routes, not direct client table mutation | [ ] PASS [ ] FAIL | |
| W5-04 | Candidate understands boundary-bypass ARC resolution requires the authorised human actor | [ ] PASS [ ] FAIL | |
| W5-05 | Candidate understands approval, intervention, and quota lifecycle authority, expiry, state, and audit requirements | [ ] PASS [ ] FAIL | |
| W5-06 | Candidate accepts that canonical ARC drift, authority bypass, missing expiry, or missing audit lifecycle blocks the wave | [ ] PASS [ ] FAIL | |

**W5 exit criterion**: The candidate can trace each executive workflow through canonical model, authority, state, audit, lifecycle, and evidence requirements.

### W6 — AIMC, AIMCC, KUC, Knowledge, Foreman, Specialist, and Push Integrations

**Scope**: Governed external integrations, service tokens, boundary enforcement, dependency readiness, provenance, and visible degraded behavior.

**Applicable RED obligations**: `QA-ARCH-001` through `QA-ARCH-006`, `QA-FD-006`, `QA-FD-011`, `QA-FD-012`, `QA-FD-013`, `QA-DEPLOY-008`, and applicable QA-DEGRADE controls.

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W6-01 | Candidate understands no direct model-provider SDK or unmanaged AI path may be introduced | [ ] PASS [ ] FAIL | |
| W6-02 | Candidate understands all AI action routes must go through AIMC | [ ] PASS [ ] FAIL | |
| W6-03 | Candidate understands all knowledge upload submissions must go through KUC, not direct AIMCC ingestion | [ ] PASS [ ] FAIL | |
| W6-04 | Candidate understands outbound integrations require service-token enforcement | [ ] PASS [ ] FAIL | |
| W6-05 | Candidate understands knowledge display requires provenance and stale/TTL treatment where applicable | [ ] PASS [ ] FAIL | |
| W6-06 | Candidate can identify success and visible degraded-mode evidence for every enabled dependency | [ ] PASS [ ] FAIL | |
| W6-07 | Candidate accepts that hidden dependency failure, boundary bypass, missing provenance, or direct provider/KUC bypass blocks the wave | [ ] PASS [ ] FAIL | |

**W6 exit criterion**: The candidate can implement only the governed integration paths and can later prove service-token, boundary, provenance, dependency, and degraded-mode behavior.

### W7 — Deployment Execution and Release Controls

**Scope**: CI/deployment workflows, migration, protected environments, production approval, rollback/recovery, health, smoke, dependency validation, and release evidence.

**Applicable RED obligations**: `QA-DEPLOY-001` through `QA-DEPLOY-010`, applicable QA-DES/QA-CONFIG controls, and PBFAG-DEPLOY rows.

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W7-01 | Candidate understands frontend and Next.js API deploy as one Vercel unit | [ ] PASS [ ] FAIL | |
| W7-02 | Candidate understands production deployment and migration require protected `production` environment approval | [ ] PASS [ ] FAIL | |
| W7-03 | Candidate understands the frozen migration command is `supabase db push --project-ref $SUPABASE_PROJECT_REF` unless CS2 approves a change | [ ] PASS [ ] FAIL | |
| W7-04 | Candidate understands every migration requires rollback/revert/restore planning before wave closure | [ ] PASS [ ] FAIL | |
| W7-05 | Candidate understands app/API/Supabase/realtime/core-route health and smoke evidence is mandatory | [ ] PASS [ ] FAIL | |
| W7-06 | Candidate understands production secret isolation and preview/staging boundaries | [ ] PASS [ ] FAIL | |
| W7-07 | Candidate can identify the complete deployment evidence package and protected manual validations | [ ] PASS [ ] FAIL | |
| W7-08 | Candidate accepts that command drift, ungated production action, secret leakage, no rollback, no smoke proof, or placeholder evidence blocks the wave | [ ] PASS [ ] FAIL | |

**W7 exit criterion**: The candidate can execute only the approved deployment model and can later prove protected release, migration, rollback, health, environment, and dependency controls.

### W8 — QA-to-Green and Evidence Consolidation

**Scope**: Consolidate cross-wave QA-to-Green, PBFAG, tracker/index, evidence package, regression, and zero-test-debt proof.

**Applicable RED obligations**: All assigned existing QA families, `QA-FD-001` through `QA-FD-015`, `QA-DEPLOY-001` through `QA-DEPLOY-010`, all applicable PBFAG-FD/PBFAG-DEPLOY/PBFAG-QA/PBFAG-TRACK rows.

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W8-01 | Candidate understands 100% GREEN means all applicable tests pass with zero unresolved blocker | [ ] PASS [ ] FAIL | |
| W8-02 | Candidate understands skipped, todo, stub-only, placeholder, trivial, warning-suppressed, or deleted test proof is rejected | [ ] PASS [ ] FAIL | |
| W8-03 | Candidate understands each wave must supply its own evidence before W8 consolidation | [ ] PASS [ ] FAIL | |
| W8-04 | Candidate can identify all evidence classes: visual, API, state, audit, authority, degraded, environment, dependency, deployment, rollback, health, and test logs | [ ] PASS [ ] FAIL | |
| W8-05 | Candidate understands tracker/index must reflect actual results and may not claim readiness early | [ ] PASS [ ] FAIL | |
| W8-06 | Candidate understands regression, route/event drift, omitted route, and evidence completeness checks are blocking | [ ] PASS [ ] FAIL | |
| W8-07 | Candidate accepts that Build-to-Green enforcement must be active and blocking at implementation closure | [ ] PASS [ ] FAIL | |

**W8 exit criterion**: The candidate is capable of verifying and consolidating real cross-wave evidence without test debt, shortcut proof, hidden drift, or premature readiness claims.

---

## 7. Wave Ordering and Candidate Allocation Rules

1. W1 and W2 must complete before material user-action delivery proceeds.
2. W3 establishes material surfaces before W4 proves the first E2E journey.
3. W5 and W6 expand executive workflow and external integration capability only after the relevant foundation is stable.
4. W7 validates deployment and release controls before release-readiness claims.
5. W8 consolidates evidence; it may not manufacture missing evidence for an earlier wave.
6. A candidate may cover multiple waves only when their contract and demonstrated competency match every assigned domain.
7. Cross-wave ownership must be explicit; no responsibility may be assumed because two builders touch adjacent components.
8. A later builder appointment must specify exact wave, tasks, acceptance criteria, RED tests, evidence, dependencies, and merge gates.

---

## 8. Candidate Overall Outcome

Complete for each proposed candidate after all applicable sections and wave gates are executed.

| Area | Outcome |
|---|---|
| Agent contract and authority | [ ] PASS [ ] FAIL |
| Governance comprehension | [ ] PASS [ ] FAIL |
| AMC scope and boundary comprehension | [ ] PASS [ ] FAIL |
| QA-to-Red comprehension | [ ] PASS [ ] FAIL |
| Environment and dependency readiness | [ ] PASS [ ] FAIL |
| Evidence and protocol commitments | [ ] PASS [ ] FAIL |
| Blocking gate readiness | [ ] PASS [ ] FAIL |
| Foreman role-fit assessment | [ ] PASS [ ] FAIL |
| Applicable W1–W8 gates | [ ] PASS [ ] FAIL |

**Candidate final result**: [ ] PASS — eligible to proceed to Stage 10 consideration; [ ] FAIL/BLOCKED — Stage 10 and appointment prohibited.

**Foreman sign-off**: Not executed  
**Date**: Not executed

---

## 9. Ambiguity, Dependency, and Failure Register

No entries exist at artifact-production time. Any later entry remains blocking until explicitly resolved and re-verified.

| ID | Type | Description | Source artifact / wave | Owner | Required resolution | Status |
|---|---|---|---|---|---|---|
| — | — | No entries recorded | — | — | — | CLEAR AT ARTIFACT PRODUCTION |

---

## 10. Stage 9 Artifact Production Result

**Artifact status**: PRODUCED FOR CS2 REVIEW  
**Candidate execution status**: NOT STARTED  
**Stage 9 approval status**: PENDING CS2 DISPOSITION  
**Stage 10 status**: BLOCKED  
**Stage 11 status**: BLOCKED  
**Stage 12 status**: BLOCKED

---

## 11. Explicit Non-Scope

This Stage 9 artifact does not:

- create or execute the Stage 10 IAA Pre-Brief;
- select or appoint a builder;
- create a builder delegation order;
- create implementation tasks or product source code;
- execute database migrations or deployments;
- create QA-to-Green or build evidence;
- certify build readiness, handover readiness, or merge readiness;
- start Stage 12.

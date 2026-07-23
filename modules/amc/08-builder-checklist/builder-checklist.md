# AMC Builder Checklist — Stage 9

**Status**: ✅ Produced / Merged — PR #1204; W1 candidate PASS accepted separately in merged PR #1216.  

## Status Header

| Field | Value |
|---|---|
| Module | App Management Centre (AMC) |
| Stage | 9 — Builder Checklist |
| Version | 1.2 |
| Status | ✅ Produced / Merged — PR #1204; W1 candidate PASS accepted separately in merged PR #1216 |
| Governing Issue | `app_management_centre#1203` |
| Governing PR | `app_management_centre#1204` |
| Foreman | `foreman-v2-agent` |
| Authority | CS2 — Johan Ras |
| Date Produced | 2026-07-10 |
| Last Substantive Revision | 2026-07-13 |
| Canonical Location | `modules/amc/08-builder-checklist/builder-checklist.md` |
| Policy Authority | `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0 — Stage 9 |

---

## 1. Purpose and Boundary

This checklist converts the CS2-approved Stage 8 Implementation Plan into explicit pre-appointment readiness gates for AMC delivery waves W1 through W8.

It is checklist-only. It does not evaluate or appoint a builder, create the Stage 10 IAA Pre-Brief, issue a delegation order, authorise implementation, execute deployment or migration, create build evidence, or certify AMC build-ready.

Stage 9 artifact production is authorised by PR #1202 and the Stage 8 CS2 decision record. Stage 10 remains blocked until Stage 9 receives explicit CS2 disposition and the intended candidate set has passed the applicable checks.

---

## 2. Binding Authority Inputs

The candidate and Foreman must use the following as binding inputs:

1. `modules/amc/00-app-description/app-description.md`
2. `modules/amc/01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md` and wiring artifacts
3. `modules/amc/02-frs/functional-requirements-specification.md` and FR-1900 addendum
4. `modules/amc/03-trs/technical-requirements-specification.md` and TR-1900/TR-1910 addendum
5. Stage 5 architecture pack and functional-delivery architecture map
6. Stage 5a Deployment Execution Strategy and validation matrix
7. Stage 6 QA-to-Red specification, red-test catalog, and QA-FD/QA-DEPLOY expansion matrix
8. Stage 7 PBFAG pack and retrofit evidence rows
9. `modules/amc/07-implementation-plan/implementation-plan.md`
10. `modules/amc/07-implementation-plan/wave-breakdown.md`
11. `modules/amc/07-implementation-plan/condition-import-matrix.md`
12. `modules/amc/07-implementation-plan/cs2-decision-record-stage-8.md`

No later checklist execution may weaken these inputs.

---

## 3. Pass, Fail, and Blocking Rules

1. Every applicable check and every applicable wave-contract dimension must be PASS with evidence.
2. A single FAIL, unknown, unsupported statement, unresolved ambiguity, missing RED-test mapping, inaccessible dependency, unavailable environment, inactive blocking gate, authority mismatch, missing evidence obligation, or undefined exit criterion blocks progression.
3. `N/A` requires written rationale and Foreman acceptance and may not avoid a binding Stage 8 condition.
4. A candidate may not self-approve role fit, scope sufficiency, exceptions, deviations, stop-condition closure, or exit-criterion satisfaction.
5. Checklist production is not checklist execution.
6. No readiness, handover, merge-readiness, or implementation-authorisation claim may be made from this artifact alone.
7. A wave may not be assigned unless its scope, authority inputs, RED obligations, dependencies, required evidence, stop conditions, and exit criteria are all explicit and accepted.

---

## 4. Candidate Record

Complete one record per proposed candidate and proposed wave allocation.

| Field | Required value |
|---|---|
| Builder candidate agent ID | Exact identifier |
| Agent contract path and version | Exact current contract |
| Proposed builder class | UI / API / Schema / QA / Integration / Infrastructure / other approved class |
| Proposed wave scope | Explicit W1–W8 allocation |
| Candidate evaluation issue/PR | Exact governed reference |
| Evaluation date | `YYYY-MM-DD` |
| Evaluated by | Foreman identifier |
| Final result | PASS / FAIL / BLOCKED |

No candidate record has been executed in PR #1204.

---

## 5. Universal Readiness Checks

### A. Agent Contract and Authority

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| A-01 | Candidate contract exists and is current | [ ] PASS [ ] FAIL | |
| A-02 | Contract declares builder-class authority for the proposed technical scope and repository | [ ] PASS [ ] FAIL | |
| A-03 | Contract contains required Phase 1 and FAIL-ONLY-ONCE obligations | [ ] PASS [ ] FAIL | |
| A-04 | Candidate has no authority to modify governance canon, approval records, or agent contracts | [ ] PASS [ ] FAIL | |
| A-05 | Candidate understands appointment authority remains with Foreman after Stage 10 | [ ] PASS [ ] FAIL | |

### B. Mandatory Governance Reading and Comprehension

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| B-01 | Candidate has read `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0 | [ ] PASS [ ] FAIL | |
| B-02 | Candidate has read `governance/canon/BUILD_PHILOSOPHY.md` and accepts One-Time Build, Zero Regression, 100% GREEN, and zero test debt | [ ] PASS [ ] FAIL | |
| B-03 | Candidate has read `governance/canon/STOP_AND_FIX_DOCTRINE.md` and accepts mandatory halt/escalation on blockers or ambiguity | [ ] PASS [ ] FAIL | |
| B-04 | Candidate has read `governance/canon/MERGE_GATE_INTERFACE_STANDARD.md` and understands required merge-gate evidence | [ ] PASS [ ] FAIL | |
| B-05 | Candidate has read `governance/canon/EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md` and understands evidence-bundle obligations | [ ] PASS [ ] FAIL | |
| B-06 | Candidate has read and accepts the repository PREHANDOVER proof requirements | [ ] PASS [ ] FAIL | |
| B-07 | Candidate has read every module-specific canon and authority input listed in Section 2 and the Stage 8 plan | [ ] PASS [ ] FAIL | |
| B-08 | Candidate understands Foreman orchestrates but does not implement; ECAP is administrative; IAA is independent | [ ] PASS [ ] FAIL | |
| B-09 | Candidate accepts that implementation-only work is not handover | [ ] PASS [ ] FAIL | |
| B-10 | Candidate accepts that skipped, todo, stub-only, placeholder, trivially passing, weakened, deleted, or warning-suppressed tests cannot prove completion | [ ] PASS [ ] FAIL | |

### C. AMC Scope and Boundary Comprehension

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| C-01 | Candidate can summarise AMC as the estate-level executive control centre and control plane | [ ] PASS [ ] FAIL | |
| C-02 | Candidate can identify AMC, AIMC, AIMCC, KUC, knowledge/memory, Foreman, specialist, and push boundaries relevant to the wave | [ ] PASS [ ] FAIL | |
| C-03 | Candidate understands all AI actions route through AIMC and no direct model-provider SDK may be introduced | [ ] PASS [ ] FAIL | |
| C-04 | Candidate understands uploads route through KUC and AMC does not own canonical knowledge content | [ ] PASS [ ] FAIL | |
| C-05 | Candidate understands the canonical ARC model and prohibited `arc_triggers` or non-canonical ARC routes/events | [ ] PASS [ ] FAIL | |
| C-06 | Candidate can trace every material route/action to authority, state, audit, visible result, and degraded-mode behaviour | [ ] PASS [ ] FAIL | |
| C-07 | No unresolved scope ambiguity exists | [ ] PASS [ ] FAIL | Record in Section 8 if present |

### D. QA-to-Red Comprehension

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| D-01 | Candidate has reviewed the Stage 6 QA-to-Red specification and catalogs | [ ] PASS [ ] FAIL | |
| D-02 | Candidate can identify every existing, QA-FD, QA-DEPLOY, and PBFAG test/evidence row applicable to the proposed wave | [ ] PASS [ ] FAIL | |
| D-03 | Candidate understands applicable tests must be RED before implementation and GREEN only after compliant implementation exists | [ ] PASS [ ] FAIL | |
| D-04 | Candidate will not weaken, skip, delete, trivialise, or rewrite tests around the implementation | [ ] PASS [ ] FAIL | |
| D-05 | Candidate understands GREEN achieved through a forbidden shortcut is a failure | [ ] PASS [ ] FAIL | |

### E. Environment and Dependency Readiness

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| E-01 | Repository, branch, runtime, package, and required tool access are available | [ ] PASS [ ] FAIL | |
| E-02 | Required Vercel, Supabase, GitHub environment, and secret access is available or governed access is explicitly arranged | [ ] PASS [ ] FAIL | |
| E-03 | PR, preview, staging, and production resources and secrets are separated | [ ] PASS [ ] FAIL | |
| E-04 | Production deploy and migration remain protected/manual where required | [ ] PASS [ ] FAIL | |
| E-05 | External dependencies are ready or have approved visible degraded-mode behaviour | [ ] PASS [ ] FAIL | |
| E-06 | No unresolved environment or dependency blocker remains | [ ] PASS [ ] FAIL | |

### F. Evidence and Protocol Commitments

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| F-01 | Candidate will produce all applicable visual, API, state, audit/provenance, authority, degraded-mode, environment, dependency, deployment, rollback, health, smoke, and test evidence | [ ] PASS [ ] FAIL | |
| F-02 | Candidate will preserve canonical route, endpoint, event, table, workflow, and migration-command names unless CS2 approves a change | [ ] PASS [ ] FAIL | |
| F-03 | Candidate will stop and escalate any architecture, requirement, test, deployment, authority, or evidence conflict before continuing | [ ] PASS [ ] FAIL | |
| F-04 | Candidate will not expose production secrets in PR, preview, or staging contexts | [ ] PASS [ ] FAIL | |
| F-05 | Candidate will file PREHANDOVER proof only at the correct later ceremony point | [ ] PASS [ ] FAIL | |

### G. Blocking Gate Readiness

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| G-01 | Build-to-Green enforcement is active and blocking for implementation PRs, not paused or advisory | [ ] PASS [ ] FAIL | |
| G-02 | Required PR checks are present and workflow-backed | [ ] PASS [ ] FAIL | |
| G-03 | Builder delegation evidence will be PR-scoped | [ ] PASS [ ] FAIL | |
| G-04 | Canonical IAA pre-brief will exist before appointment and the first implementation commit | [ ] PASS [ ] FAIL | |
| G-05 | Handover/completion language remains prohibited until the proper later gate | [ ] PASS [ ] FAIL | |
| G-06 | No governance self-repair exception or bypass is being used to avoid normal implementation controls | [ ] PASS [ ] FAIL | |

### H. Foreman Role-Fit Assessment

> Foreman completes this section independently.

| ID | Check | Result | Evidence / Notes |
|---|---|---|---|
| H-01 | Candidate competencies match the proposed wave | [ ] PASS [ ] FAIL | |
| H-02 | Candidate contract authority matches the proposed scope without overreach | [ ] PASS [ ] FAIL | |
| H-03 | Candidate accurately demonstrates AMC boundary and RED-test comprehension | [ ] PASS [ ] FAIL | |
| H-04 | No unresolved performance, integrity, or FAIL-ONLY-ONCE concern affects the assignment | [ ] PASS [ ] FAIL | |
| H-05 | Foreman confirms the candidate is the correct role fit | [ ] PASS [ ] FAIL | |

---

## 6. Wave-Specific Readiness Contracts

Every proposed wave assignment must pass all seven contract dimensions below. The detailed checks supplement—not replace—the contract dimensions.

### W1 — Runtime Foundation and Environment Setup

| Contract dimension | Binding requirement |
|---|---|
| Scope | Repository/runtime foundation, CI, preview deployment posture, environment contract, secret separation, and initial deployment plumbing. |
| Authority inputs | Stage 5a Deployment Execution Strategy and validation matrix; Stage 8 Implementation Plan §§3–5; Stage 8 Condition Import Matrix; TR-1910 deployment requirements. |
| RED obligations | `QA-DEPLOY-001`, `QA-DEPLOY-002`, `QA-DEPLOY-003`, `QA-DEPLOY-004`, `QA-DEPLOY-006`, `QA-DEPLOY-007`, `QA-DEPLOY-010`, plus applicable QA-CONFIG/QA-DES controls. |
| Dependencies / prerequisites | Repository/runtime decision; workflow ownership; governed Vercel/Supabase/GitHub environment access; root `.env.example`; preview/staging resource ownership; active blocking gates. |
| Required evidence | Environment contract; workflow definitions; CI/type/lint/test/schema logs; preview isolation proof; no-production-side-effect proof; secret-boundary proof. |
| Stop conditions | Missing workflow owner; inaccessible required environment; preview/staging use of production secrets or data; inactive blocking gate; undocumented runtime/deployment deviation; committed secret. |
| Exit criteria | Candidate can identify every required workflow, environment owner, RED test, dependency, and evidence artifact; all dependencies have owners or governed access plans; no production side effect is possible from PR CI. |

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W1-01 | Candidate understands `.github/workflows/ci.yml`, `.github/workflows/deploy-frontend.yml`, and `.github/workflows/db-migrate.yml` | [ ] PASS [ ] FAIL | |
| W1-02 | PR CI cannot mutate production; preview/staging cannot access production credentials or data | [ ] PASS [ ] FAIL | |
| W1-03 | Root `.env.example` contract and no-committed-secret rule are understood | [ ] PASS [ ] FAIL | |
| W1-04 | Required CI, type, lint, test, schema, preview, and environment evidence is known | [ ] PASS [ ] FAIL | |
| W1-05 | Every dependency and stop condition has an explicit owner and resolution path | [ ] PASS [ ] FAIL | |
| W1-06 | W1 exit criteria are understood and objectively verifiable | [ ] PASS [ ] FAIL | |

### W2 — Auth, Tenant, Authority, and Audit Baseline

| Contract dimension | Binding requirement |
|---|---|
| Scope | Supabase Auth, tenant isolation, RLS, server-side authority enforcement, state ownership, and atomic audit/provenance behaviour. |
| Authority inputs | Stage 4 TRS authority/security requirements; Stage 5 architecture and data-boundary map; Stage 6 auth/RLS/audit tests; FR-1903, FR-1904, and FR-1906. |
| RED obligations | QA-AUTH/RLS/audit families; `QA-FD-003`, `QA-FD-004`, `QA-FD-005`; `QA-ARCH-004`; `QA-ARCH-005`. |
| Dependencies / prerequisites | W1 foundation; canonical identity and tenant model; schema/RLS design; server authority middleware contract; audit taxonomy and correlation model. |
| Required evidence | Auth success/failure proof; same-tenant/cross-tenant RLS proof; server-authority proof; state-owner proof; atomic audit proof; unauthorised and bypass negative-path evidence. |
| Stop conditions | Client-only authority; unresolved tenant model; missing RLS rule; cross-tenant leakage; state mutation before authority; success returned before audit; ambiguous audit owner. |
| Exit criteria | Candidate can trace each consequential action through identity, tenant, authority, state owner, audit event, and negative paths, with no client-side or cross-tenant bypass. |

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W2-01 | Tenant isolation and RLS are enforced at the data boundary | [ ] PASS [ ] FAIL | |
| W2-02 | Server authority is verified before consequential side effects | [ ] PASS [ ] FAIL | |
| W2-03 | State owner/projection and atomic audit event are identified for each action | [ ] PASS [ ] FAIL | |
| W2-04 | Negative-path evidence covers unauthorised, cross-tenant, and boundary-bypass attempts | [ ] PASS [ ] FAIL | |
| W2-05 | Every dependency and stop condition has an explicit owner and resolution path | [ ] PASS [ ] FAIL | |
| W2-06 | W2 exit criteria are understood and objectively verifiable | [ ] PASS [ ] FAIL | |

### W3 — Core AMC Routes and Material Surfaces

| Contract dimension | Binding requirement |
|---|---|
| Scope | Material AMC routes, visible actions, CTA/service bindings, state/projection ownership, audit events, confirmations, and visible degraded states. |
| Authority inputs | Stage 2 CTA/API/Data/Audit matrix; FR-1900 family; TR-1900 family; Stage 5 functional-delivery architecture map; Stage 8 W3 plan. |
| RED obligations | `QA-FD-001` through `QA-FD-009`; applicable route/contract tests; PBFAG-FD rows. |
| Dependencies / prerequisites | W1 and W2; canonical route inventory; endpoint/service contracts; state schema; audit event names; dependency/degraded-state definitions. |
| Required evidence | UI route and CTA proof; API/service proof; authority proof; state/read-only proof; audit proof; visible success/failure/blocked/degraded confirmation; omitted-route scan. |
| Stop conditions | Dead CTA; backend-only capability without approved disposition; omitted route; route/event drift; direct state mutation bypass; missing audit; hidden degraded mode; undeclared placeholder. |
| Exit criteria | Every material action in scope is traceable end to end from visible entry point to service/API, authority, state, audit, confirmation, recovery, and degraded behaviour. |

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W3-01 | Every material route and action in scope is enumerated | [ ] PASS [ ] FAIL | |
| W3-02 | Every CTA has a service/API target or approved read-only classification | [ ] PASS [ ] FAIL | |
| W3-03 | Every backend capability has a visible journey/state or approved backend-only disposition | [ ] PASS [ ] FAIL | |
| W3-04 | State, audit, authority, visible result, recovery, and degraded-mode treatment are defined | [ ] PASS [ ] FAIL | |
| W3-05 | Dead CTA, omitted route, route/event drift, placeholder leakage, or hidden failure produces FAIL | [ ] PASS [ ] FAIL | |
| W3-06 | W3 exit criteria are understood and objectively verifiable | [ ] PASS [ ] FAIL | |

### W4 — First Complete `/alerts` Acknowledgement Journey

| Contract dimension | Binding requirement |
|---|---|
| Scope | First fully evidenced `/alerts` acknowledgement path from UI through API, authority, state, audit, realtime propagation, visible confirmation, and negative paths. |
| Authority inputs | Stage 8 first-E2E requirement; Stage 2 alert journey; FR-1901–FR-1908; Stage 5 route/state/audit map; `QA-FD-010`. |
| RED obligations | `QA-FD-010` plus applicable `QA-FD-003`, `QA-FD-004`, `QA-FD-005`, authority, audit, realtime, recovery, and degraded-mode tests. |
| Dependencies / prerequisites | W1–W3; alert schema; canonical acknowledgement API; authorised actor model; audit event; realtime channel; visible confirmation and retry/recovery states. |
| Required evidence | UI interaction; API request/response; authorised and unauthorised paths; persisted state; audit event; realtime cross-view/device update; visible success/failure; degraded/retry behaviour. |
| Stop conditions | Partial path; mocked-only boundary proof; unauthorised side effect; missing atomic state/audit closure; missing realtime propagation; silent failure; no visible confirmation. |
| Exit criteria | The full acknowledgement journey can be executed and proved end to end, including authority, persistence, audit, realtime, visible result, and negative/degraded paths. |

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W4-01 | Exact journey, allowed actor, API route, state transition, audit event, realtime channel, and visible result are known | [ ] PASS [ ] FAIL | |
| W4-02 | Unauthorised acknowledgement fails before side effects | [ ] PASS [ ] FAIL | |
| W4-03 | Success requires atomic state/audit closure and visible confirmation | [ ] PASS [ ] FAIL | |
| W4-04 | Evidence bundle covers UI, API, authority, state, audit, realtime, visible result, recovery, and degraded state | [ ] PASS [ ] FAIL | |
| W4-05 | Partial or mocked-only boundary proof produces FAIL | [ ] PASS [ ] FAIL | |
| W4-06 | W4 exit criteria are understood and objectively verifiable | [ ] PASS [ ] FAIL | |

### W5 — ARC, Approvals, Interventions, and Executive Workflow

| Contract dimension | Binding requirement |
|---|---|
| Scope | ARC Governance Console, approvals, interventions, quota lifecycle, executive state machines, authority boundaries, expiry, audit, and visible outcomes. |
| Authority inputs | Canonical ARC architecture; Stage 2 executive workflows; FR-1900/TR-1900 authority and state requirements; Stage 5 map; Stage 8 W5 plan. |
| RED obligations | `QA-ARC-001` through `QA-ARC-006`; `QA-FD-003`, `QA-FD-004`, `QA-FD-005`, `QA-FD-014`, `QA-FD-015`; applicable PBFAG-FD rows. |
| Dependencies / prerequisites | W2 and W3; `arc_classifications`; canonical `/api/arc/{id}` actions; `ARC_ITEM_*` events; approval/intervention/quota state machines; expiry/escalation rules. |
| Required evidence | Canonical model proof; server-route transition proof; authority and reserved-matter proof; lifecycle/expiry proof; state and audit proof; visible blocked/success/failure proof; negative paths. |
| Stop conditions | Canonical ARC drift; `arc_triggers` reintroduction; direct client table mutation; authority bypass; missing expiry/escalation; missing audit lifecycle; false visible completion. |
| Exit criteria | Each executive workflow is mapped and later provable across canonical model, authority, state, lifecycle, audit, visible result, and negative/degraded behaviour. |

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W5-01 | `arc_classifications`, canonical `/api/arc/{id}` actions, and `ARC_ITEM_*` events are understood | [ ] PASS [ ] FAIL | |
| W5-02 | ARC transitions occur through server routes, not direct client table mutation | [ ] PASS [ ] FAIL | |
| W5-03 | Boundary-bypass ARC resolution requires the authorised human actor | [ ] PASS [ ] FAIL | |
| W5-04 | Approval, intervention, and quota lifecycle authority, expiry, state, and audit obligations are understood | [ ] PASS [ ] FAIL | |
| W5-05 | Canonical-model drift, authority bypass, missing expiry, or missing audit lifecycle produces FAIL | [ ] PASS [ ] FAIL | |
| W5-06 | W5 exit criteria are understood and objectively verifiable | [ ] PASS [ ] FAIL | |

### W6 — Governed External Integrations

| Contract dimension | Binding requirement |
|---|---|
| Scope | AIMC, AIMCC, KUC, knowledge/memory, Foreman, specialist-agent, and push integrations with service-token, provenance, ownership, and visible degraded-mode enforcement. |
| Authority inputs | Stage 4 integration requirements; Stage 5 boundary architecture; FR-1904–FR-1907; TR-1900 boundary rules; Stage 8 W6 plan. |
| RED obligations | `QA-ARCH-001` through `QA-ARCH-006`; `QA-FD-006`, `QA-FD-011`, `QA-FD-012`, `QA-FD-013`; `QA-DEPLOY-008`; applicable QA-DEGRADE controls. |
| Dependencies / prerequisites | W1–W3; approved service-token mechanism; dependency contracts/endpoints; AIMC route; KUC submission path; provenance model; timeout/retry/degraded UX; dependency ownership. |
| Required evidence | Service-token proof; AIMC-only AI routing; KUC-only upload routing; provenance/stale treatment; success and failure interactions; timeout/retry; visible degraded state; no local canonical-knowledge ownership. |
| Stop conditions | Direct provider SDK; direct AIMCC ingestion; unmanaged knowledge store; missing service token; hidden dependency failure; false success; missing provenance; silent stale truth. |
| Exit criteria | Every enabled integration uses the approved boundary, has an owner and dependency contract, and can later prove success, failure, degraded mode, provenance, and non-bypass behaviour. |

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W6-01 | No direct model-provider SDK or unmanaged AI route; all AI actions use AIMC | [ ] PASS [ ] FAIL | |
| W6-02 | Uploads use KUC, not direct AIMCC ingestion | [ ] PASS [ ] FAIL | |
| W6-03 | Outbound integrations enforce service tokens | [ ] PASS [ ] FAIL | |
| W6-04 | Knowledge results include provenance and stale/TTL treatment where applicable | [ ] PASS [ ] FAIL | |
| W6-05 | Success, failure, retry, and visible degraded-mode evidence exists for each enabled dependency | [ ] PASS [ ] FAIL | |
| W6-06 | Hidden dependency failure or boundary bypass produces FAIL | [ ] PASS [ ] FAIL | |
| W6-07 | W6 exit criteria are understood and objectively verifiable | [ ] PASS [ ] FAIL | |

### W7 — Deployment Execution and Release Controls

| Contract dimension | Binding requirement |
|---|---|
| Scope | CI/deployment workflows, preview/staging/production controls, migration, protected approval, rollback/recovery, health, smoke, dependency validation, and release evidence. |
| Authority inputs | Stage 5a Deployment Execution Strategy and validation matrix; TR-1910; Stage 8 deployment inheritance; Stage 8 Condition Import Matrix. |
| RED obligations | `QA-DEPLOY-001` through `QA-DEPLOY-010`; applicable QA-DES/QA-CONFIG controls; PBFAG-DEPLOY rows. |
| Dependencies / prerequisites | W1 foundation; owned deployment workflows; Vercel/Supabase project/environment mapping; protected `production` environment; migration plan; rollback/restore method; health endpoints; smoke scripts. |
| Required evidence | Workflow runs; preview/staging isolation; protected production approval; exact migration command; migration log; rollback/recovery proof; app/API/Supabase/realtime/core-route health and smoke results; dependency status. |
| Stop conditions | Deployment-command drift; ungated production action; production secret exposure; no rollback; no health/smoke proof; unidentified project/environment; placeholder evidence; failed dependency without visible degraded state. |
| Exit criteria | The approved deployment model is fully owned and later executable with protected release, migration, rollback, health, smoke, environment, secret, and dependency evidence. |

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W7-01 | Frontend and Next.js API deploy as one Vercel unit | [ ] PASS [ ] FAIL | |
| W7-02 | Production deploy and migration require protected `production` environment approval | [ ] PASS [ ] FAIL | |
| W7-03 | Frozen migration command is `supabase db push --project-ref $SUPABASE_PROJECT_REF` unless CS2 approves a change | [ ] PASS [ ] FAIL | |
| W7-04 | Every migration has rollback/revert/restore planning | [ ] PASS [ ] FAIL | |
| W7-05 | App/API/Supabase/realtime/core-route health and smoke evidence is mandatory | [ ] PASS [ ] FAIL | |
| W7-06 | Complete deployment evidence and protected manual validations are known | [ ] PASS [ ] FAIL | |
| W7-07 | Command drift, ungated production action, secret leakage, no rollback, no smoke proof, or placeholder evidence produces FAIL | [ ] PASS [ ] FAIL | |
| W7-08 | W7 exit criteria are understood and objectively verifiable | [ ] PASS [ ] FAIL | |

### W8 — QA-to-Green and Evidence Consolidation

| Contract dimension | Binding requirement |
|---|---|
| Scope | Cross-wave QA-to-Green verification, regression, PBFAG closure, evidence-bundle consolidation, tracker/index truth, and zero-test-debt proof. |
| Authority inputs | Stage 6 QA-to-Red pack; Stage 7 PBFAG pack; Stage 8 evidence expectations and red-test map; Build Philosophy; Evidence Artifact Bundle Standard. |
| RED obligations | All assigned QA families; `QA-FD-001` through `QA-FD-015`; `QA-DEPLOY-001` through `QA-DEPLOY-010`; applicable PBFAG-FD/PBFAG-DEPLOY/PBFAG-QA/PBFAG-TRACK rows. |
| Dependencies / prerequisites | Complete W1–W7 evidence; active blocking gates; canonical route/event/test inventory; regression baseline; tracker/index owners; no unresolved blocker or approved-but-unclosed exception. |
| Required evidence | Complete test logs; 100% GREEN result; zero skipped/todo/trivial/deleted tests; regression proof; route/event/omission scans; visual/API/state/audit/authority/degraded/deployment/rollback/health evidence; tracker/index reconciliation. |
| Stop conditions | Missing wave evidence; skipped/todo/stub/trivial/deleted/weakened test; unresolved regression; route/event drift; omitted route; stale tracker/index; warning suppression; incomplete evidence bundle. |
| Exit criteria | Every applicable test is genuinely GREEN, every W1–W7 evidence obligation is present and reconciled, no blocker or test debt remains, and tracker/index reflect the verified result without premature build/readiness claims. |

| ID | Readiness check | Result | Evidence / Notes |
|---|---|---|---|
| W8-01 | 100% GREEN means all applicable tests pass with zero unresolved blocker or test debt | [ ] PASS [ ] FAIL | |
| W8-02 | Each earlier wave supplies its own real evidence; W8 cannot manufacture missing proof | [ ] PASS [ ] FAIL | |
| W8-03 | Regression, route/event drift, omitted-route, tracker/index truth, and evidence-completeness checks are blocking | [ ] PASS [ ] FAIL | |
| W8-04 | Build-to-Green enforcement is active and blocking at implementation closure | [ ] PASS [ ] FAIL | |
| W8-05 | All prohibited proof patterns and shortcut paths are explicitly rejected | [ ] PASS [ ] FAIL | |
| W8-06 | W8 exit criteria are understood and objectively verifiable | [ ] PASS [ ] FAIL | |

---

## 7. Ordering and Allocation Rules

1. W1 and W2 complete before material user-action delivery.
2. W3 establishes material surfaces before W4 proves the first E2E journey.
3. W5 and W6 expand workflow and integration capability only after the relevant foundation is stable.
4. W7 validates release controls before any release-readiness claim.
5. W8 consolidates evidence but cannot replace missing wave evidence.
6. Multi-wave allocation requires contract authority and demonstrated competency for every assigned domain.
7. Cross-wave ownership must be explicit.
8. Any later appointment must state exact wave, tasks, acceptance criteria, RED tests, dependencies, required evidence, stop conditions, exit criteria, and merge gates.
9. A wave assignment is blocked unless all seven contract dimensions in Section 6 are accepted and traceable.

---

## 8. Ambiguity, Dependency, and Failure Register

| ID | Type | Description | Source / Wave | Owner | Required resolution | Status |
|---|---|---|---|---|---|---|
| — | — | No entries at artifact-production time | — | — | — | CLEAR |

Any later entry remains blocking until resolved and re-verified.

---

## 9. Candidate Outcome

| Area | Outcome |
|---|---|
| Contract and authority | [ ] PASS [ ] FAIL |
| Mandatory governance reading | [ ] PASS [ ] FAIL |
| AMC scope and boundaries | [ ] PASS [ ] FAIL |
| QA-to-Red comprehension | [ ] PASS [ ] FAIL |
| Environment and dependencies | [ ] PASS [ ] FAIL |
| Evidence and protocol commitments | [ ] PASS [ ] FAIL |
| Blocking gates | [ ] PASS [ ] FAIL |
| Foreman role-fit | [ ] PASS [ ] FAIL |
| Applicable wave contracts | [ ] PASS [ ] FAIL |
| Applicable wave detailed checks | [ ] PASS [ ] FAIL |

**Final result**: [ ] PASS — eligible for Stage 10 consideration; [ ] FAIL/BLOCKED — Stage 10 and appointment prohibited.

No candidate evaluation or sign-off has occurred in PR #1204.

---

## 10. Stage Posture

- Stage 9 artifact: produced for CS2 review.
- Candidate execution: not started.
- Stage 9 approval: pending CS2 disposition.
- Stage 10: blocked.
- Stage 11: blocked.
- Stage 12: blocked.

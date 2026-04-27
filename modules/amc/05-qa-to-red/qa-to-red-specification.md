# QA-to-Red Specification — Stage 6

**Stage**: 6 — QA-to-Red
**Module**: App Management Centre (AMC)
**Version**: 1.0
**Status**: 🟡 Produced — Approval Pending (CS2)
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: app_management_centre#1141 (Stage 6 kickoff — CS2 @APGI-cmy)
**Governing Delivery Issue**: app_management_centre#1141
**Wave**: amc-stage6-qa-to-red-20260427
**Date**: 2026-04-27
**Upstream Sources**:
- Stage 5 Architecture: `modules/amc/04-architecture/architecture-specification.md` v1.0 (produced approval-pending, ref #1131)
- Stage 5a DES: `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` v1.0 (produced approval-pending, ref #1137)
- Stage 5a DES Surface Table: `modules/amc/05a-deployment-execution-strategy/deployment-surface-ownership-table.md` v1.0
- Stage 5a Runner Constraints: `modules/amc/05a-deployment-execution-strategy/runner-and-environment-constraints.md` v1.0
**Canonical Location**: `modules/amc/05-qa-to-red/qa-to-red-specification.md`

---

> **STAGE ENTRY CONDITION NOTICE**
> Stage 5 (Architecture) and Stage 5a (Deployment Execution Strategy) are produced approval-pending.
> CS2 has authorized Stage 6 artifact production now per issue #1141 while Stage 5 and Stage 5a
> await CS2 approval. Stage 6 execution must not proceed to Stage 7 (PBFAG) until both Stage 5
> and Stage 5a receive explicit CS2 approval. This document and all Stage 6 artifacts are
> conditional on that approval. No artifact in this pack may be interpreted as claiming Stage 6
> was fully authorized before Stage 5 and Stage 5a approvals are recorded.

> **DERIVATION DECLARATION**
> This QA-to-Red Specification derives from the Stage 5 Architecture Specification
> (`modules/amc/04-architecture/architecture-specification.md` v1.0) and the Stage 5a
> Deployment Execution Strategy (`modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` v1.0)
> and its companion artifacts. It defines the exact red-test discipline, verification scope,
> fail conditions, and coverage model required to prove that AMC can be built and operated in
> line with the approved architecture and deployment strategy. It does not invent verification
> requirements that are not traceable to Stage 5 or Stage 5a. No QA-to-Red requirement may
> contradict, soften, or silently omit any architecture commitment or DES field.

---

## Table of Contents

1. [Purpose & Scope](#1-purpose--scope)
2. [Pass/Fail Philosophy](#2-passfail-philosophy)
3. [Red-Test Severity Model](#3-red-test-severity-model)
4. [Blocker vs Non-Blocker Classification](#4-blocker-vs-non-blocker-classification)
5. [Retest Expectations](#5-retest-expectations)
6. [Evidence Expectations for Stage 7 and Downstream Builders](#6-evidence-expectations-for-stage-7-and-downstream-builders)
7. [Architecture-Derived Red Coverage Model](#7-architecture-derived-red-coverage-model)
8. [Deployment-Strategy-Derived Red Coverage Model](#8-deployment-strategy-derived-red-coverage-model)
9. [Literal-Operability Sanity Checks](#9-literal-operability-sanity-checks)
10. [Anti-Drift QA Posture](#10-anti-drift-qa-posture)
11. [Coverage Completeness Declaration](#11-coverage-completeness-declaration)
12. [Sign-Off / Approval Record](#12-sign-off--approval-record)

---

## 1. Purpose & Scope

### 1.1 Purpose

This QA-to-Red Specification defines the exact red-test discipline, verification scope, fail conditions, and coverage model for the App Management Centre (AMC) Stage 6 QA-to-Red pack. It converts the approved Stage 5 Architecture and Stage 5a Deployment Execution Strategy into an approval-ready set of red test cases that must fail before any implementation begins and must pass to green after correct implementation.

The specification is the governing authority for:
- What must be tested before AMC builders are appointed (Stage 11)
- What test evidence is required before Stage 7 PBFAG can declare PASS
- What QP (Quality Professor) failure conditions apply when evaluating builder deliverables

### 1.2 Scope

**In scope for Stage 6:**
- Red coverage for all major Stage 5 Architecture commitments
- Red coverage for all 8 Stage 5a DES fields (DES-001 through DES-008)
- Literal-operability sanity checks for known failure modes
- Anti-drift QA posture statement
- Traceability to upstream sources (Stage 5 and Stage 5a)

**Out of scope for Stage 6:**
- Actual test implementation code (Stage 12 Build — qa-builder responsibility)
- Test runner configuration (Stage 12 Build)
- Coverage percentage targets for individual files (builder-level detail, deferred to Stage 8 Implementation Plan)
- Specific database migration file content (schema-builder, Stage 12 Build)

### 1.3 Downstream Authority

This specification is binding on:
- **Stage 7 (PBFAG)**: Must verify that this Stage 6 pack is complete, coherent, and covers all critical architecture and DES families
- **Stage 8 (Implementation Plan)**: Must reference this specification and ensure each builder wave has corresponding red test coverage defined
- **Stage 12 (Build)**: qa-builder must implement the test cases cataloged in `red-test-catalog.md` to satisfy the red-test conditions defined here
- **QP (Quality Professor) evaluations**: Any builder deliverable that causes previously red tests to fail green — or that deviates from Stage 5 or Stage 5a without amendment — must receive QP FAIL

---

## 2. Pass/Fail Philosophy

### 2.1 Red-First Principle

All test cases in this QA-to-Red pack are defined in the RED state first. This means:
- Every test case is written to FAIL before implementation begins
- A test transitions to GREEN only when the implementation satisfies the exact condition described
- Tests that are written in a way that could trivially pass against a stub implementation are prohibited

### 2.2 What Constitutes a PASS

A test case PASSES (transitions from red to green) when and only when:
1. The implementation behavior exactly matches the pass condition stated in `red-test-catalog.md` for that test
2. The test is executed against the actual implementation, not a mock or stub
3. The test result is reproducible on a clean execution

### 2.3 What Constitutes a FAIL

A test case FAILS when:
1. The implementation does not satisfy the pass condition
2. The implementation satisfies the pass condition via an alternative path not permitted by the Architecture or DES (drift violation)
3. The test itself is a stub or trivially-passing assertion (e.g., `expect(true).toBe(true)`)
4. The test passes against a mock where the pass condition requires behavior against a real implementation boundary

### 2.4 Zero-Test-Debt Requirement

100% GREEN is required across all red test cases before Stage 12 Build deliverables are accepted by the QP. The following are prohibited in builder deliverables:
- `.skip()`, `.todo()`, or `xtest` markers on any test case in the Stage 6 red suite
- `// TODO` markers in test helper implementations
- Stub implementations of test setup or test assertions
- Partial test suites that cover some test IDs but not others without documented and CS2-approved deferral

### 2.5 Test Debt Accumulation

Test debt detected in a builder delivery is a blocking defect. The QP must:
1. Record the debt finding in the QP evaluation
2. Issue a remediation order to the builder
3. NOT advance the merge gate until the debt is resolved
4. Confirm re-execution of the full test suite post-remediation before advancing

---

## 3. Red-Test Severity Model

Red tests are classified by severity. Severity determines the blocking behavior at Stage 7 PBFAG and at QP evaluation.

| Severity | Definition | PBFAG Behavior | QP Behavior |
|---|---|---|---|
| **CRITICAL** | Tests a constraint that, if violated, would compromise tenant isolation, security, or produce data corruption. Failure here is an architectural safety violation. | PBFAG FAIL — cannot proceed to Stage 8 | QP FAIL — merge gate blocked unconditionally |
| **HIGH** | Tests an explicitly named architecture commitment or DES field. Failure here means the implementation deviates from approved design in a material way. | PBFAG FAIL — cannot proceed to Stage 8 | QP FAIL — merge gate blocked |
| **MEDIUM** | Tests a stated behavioral expectation that materially affects the user-observable behavior of AMC. Failure is a functional deviation but not a safety breach. | PBFAG CONDITIONAL PASS — may proceed if documented and CS2 accepts the gap | QP CONDITIONAL PASS with remediation order |
| **LOW** | Tests an implementation quality expectation (e.g., error message format, SLA metric). Failure is an observable degradation but does not block core functionality. | PBFAG PASS with documented gap | QP PASS with documented gap |

**Default**: If a test case severity is not explicitly stated, it defaults to HIGH.

---

## 4. Blocker vs Non-Blocker Classification

### 4.1 BLOCKER Tests

A test is classified as BLOCKER when failure prevents Stage 7 PBFAG from declaring PASS or prevents the builder deliverable from receiving QP PASS verdict. All CRITICAL and HIGH severity tests are BLOCKERS.

BLOCKER test failures require:
- Immediate QP FAIL verdict
- Explicit remediation order to builder
- Full re-test of the failed test and all related tests after remediation
- QP re-evaluation before merge gate can advance

### 4.2 NON-BLOCKER Tests

A test is classified as NON-BLOCKER when failure does not prevent Stage 7 PBFAG or QP PASS, but requires documented acknowledgment. All MEDIUM and LOW severity tests are NON-BLOCKERS when assessed individually.

Non-blocker failures require:
- Written gap documentation by the QP (in the QP evaluation record)
- CS2 awareness and acknowledgment
- Follow-on issue created to address the gap
- If >3 NON-BLOCKER gaps are accumulated in a single builder wave, that wave is demoted to CONDITIONAL PASS pending CS2 review

### 4.3 Automatic Escalation to BLOCKER

A NON-BLOCKER test is escalated to BLOCKER status if:
- The failing condition is directly linked to a CRITICAL or HIGH test in the same test family
- The failure exposes a pattern of systematic deviation from Stage 5 or Stage 5a (drift violation)
- CS2 has explicitly designated the test as BLOCKER via issue comment or amendment

---

## 5. Retest Expectations

### 5.1 Retest Trigger Conditions

Full retest of all red suite cases is required when:
1. Any BLOCKER test failure is found and remediated
2. The builder makes any architectural-path change in response to a remediation order
3. The build wave is opened for re-evaluation after a QP FAIL verdict

Partial retest (of affected test families only) is permitted only when:
- A LOW severity non-blocker gap is addressed through documentation only (no implementation change)
- The QP explicitly documents which families are unaffected

### 5.2 Retest Evidence Requirements

For each full retest, the builder must provide:
- Full test run output (stdout + exit code) from a clean execution environment
- Confirmation of zero `.skip()`, `.todo()`, or stub assertions in the test output
- A summary identifying which previously failing tests now pass (transition record)
- Confirmation that no previously passing tests have been newly broken (regression check)

### 5.3 Regression Prevention

A retest that reveals newly-broken previously-green tests is treated as a new QP FAIL condition. A builder cannot green a failing test by breaking others. The QP must re-evaluate the full suite state after every retest.

---

## 6. Evidence Expectations for Stage 7 and Downstream Builders

### 6.1 Stage 7 (PBFAG) Evidence Requirements

Before Stage 7 PBFAG can declare PASS, the following Stage 6 evidence must be present and verified:

| Evidence Item | Required | Verified By |
|---|---|---|
| `qa-to-red-specification.md` — present and CS2-approved | ✅ Mandatory | Stage 7 PBFAG checklist |
| `red-test-catalog.md` — present, all test IDs populated, no TBD or placeholder entries | ✅ Mandatory | Stage 7 PBFAG checklist |
| `architecture-and-des-to-qa-traceability.md` — present, all Stage 5 architecture domains traced, all 8 DES fields traced | ✅ Mandatory | Stage 7 PBFAG checklist |
| CS2 sign-off section in `qa-to-red-specification.md` — approved | ✅ Mandatory | Stage 7 PBFAG checklist |
| Stage 5 Architecture CS2 approval — recorded | ✅ Mandatory prerequisite | BUILD_PROGRESS_TRACKER.md |
| Stage 5a DES CS2 approval — recorded | ✅ Mandatory prerequisite | BUILD_PROGRESS_TRACKER.md |
| No test catalog entry with blank `expected_fail_condition` or `expected_pass_condition` | ✅ Mandatory | Stage 7 PBFAG verification |
| Every critical architecture and DES family represented in catalog | ✅ Mandatory | `architecture-and-des-to-qa-traceability.md` |

### 6.2 Builder (Stage 12) Evidence Requirements

When qa-builder delivers against the Stage 6 red suite, the following evidence must accompany the delivery:

| Evidence Item | Required |
|---|---|
| Full test suite execution output (100% GREEN, zero skip/todo) | ✅ Mandatory |
| Test run is against actual implementation (not mocked boundaries) | ✅ Mandatory |
| Each test ID from `red-test-catalog.md` is accounted for (pass, documented-defer, or documented-descope with CS2 approval) | ✅ Mandatory |
| Prehandover evidence bundle (per Foreman prehandover-template.md) | ✅ Mandatory |
| QP evaluation report with PASS verdict | ✅ Mandatory |
| No `.skip()`, `.todo()`, `xtest`, or trivial assertion present | ✅ Mandatory |

### 6.3 What Constitutes Acceptable Test Implementation

A test implementation in Stage 12 is acceptable when:
- It tests the behavior described in the test's `scenario` field
- It exercises the actual code path described (not a mock of that path unless the test is a unit test of a defined boundary function)
- It asserts the exact `expected_pass_condition` defined in the catalog
- It would FAIL against an implementation that violates the `expected_fail_condition`

A test implementation is NOT acceptable when:
- It asserts only that a function exists (not that it behaves correctly)
- It uses `expect(true).toBe(true)` or equivalent trivial assertions
- It mocks the entire system under test
- It ignores the boundary conditions specified in the catalog

---

## 7. Architecture-Derived Red Coverage Model

This section defines the required red-test coverage families for major Stage 5 Architecture commitments. Each family is traceable to one or more architecture sections. Full test IDs are defined in `red-test-catalog.md`.

### 7.1 Cross-System Boundary Preservation

**Architecture Reference**: §2 (Cross-System Boundary Confirmation), §5.6 (Non-Bypass Enforcement Architecture)

Red tests must cover:
- AMC `package.json` contains no AI model provider SDK (OpenAI, Anthropic, Google Gemini, etc.)
- AMC application code never calls AIMCC internal ingestion endpoints directly
- AMC never writes to the knowledge/memory system (no table columns storing canonical knowledge content)
- All outbound AMC API calls to external services include `Authorization: Bearer {service_token}` header
- `BOUNDARY_BYPASS_ATTEMPTED` audit event is generated when any boundary bypass is detected at runtime
- AMC submits knowledge uploads to `KUC_API_BASE_URL/submit` only — never to AIMCC ingestion path

### 7.2 ARC Domain Explicitness

**Architecture Reference**: §4.1 (ARC — First-Class Technical Domain)

Red tests must cover:
- `arc_classifications` table exists as a distinct table (not a view or derived table)
- `/api/arc/` namespace exists and is separate from `/api/alerts/`, `/api/approvals/`
- `/arc` frontend route exists and is accessible from executive navigation
- `amc_arc_{user_id}` Realtime channel is subscribed to separately from other channels
- ARC item state transitions: `open → in_resolution → resolved` require the correct POST endpoints
- Attempting to auto-resolve a boundary-bypass ARC item without human actor (`Johan Ras`) returns HTTP 403
- ARC staleness detection generates Medium alerts via `amc-arc-staleness-scheduler` (not via inline alert code)
- `ARC_ITEM_CLASSIFIED`, `ARC_ITEM_STATE_CHANGED`, `ARC_ITEM_RESOLVED` audit events are written on each transition

### 7.3 Dynamic Upload Quota Management Console Behavior and Boundaries

**Architecture Reference**: §4.2 (Dynamic Upload Quota Management)

Red tests must cover:
- `POST /api/aimcc/quota/request-adjustment` is the sole path for initiating a quota change from AMC
- Any quota adjustment request creates a `reserved_matter` approval record — no quota change takes effect without an approval record
- Attempting to change quota without a completed approval record fails with HTTP 422 or equivalent explicit rejection
- AIMCC is notified of approved quota changes via `POST {AIMCC_API_BASE_URL}/governance/decision` — no other notification path
- Temporary overrides carry `override_expiry_at` field; missing expiry field is rejected
- Quota threshold state machine transitions (`ok → warning → critical`) generate alerts and audit events when thresholds are crossed
- Quota threshold values are read from environment variables (`QUOTA_WARNING_THRESHOLD_PERCENT`, `QUOTA_CRITICAL_THRESHOLD_PERCENT`); hardcoded values fail the test
- Full quota change history is reconstructable from `audit_events` (no separate quota history table required)

### 7.4 State Ownership and Consistency Expectations

**Architecture Reference**: §6.1 (State Consistency Architecture), §3.4 (Database Architecture)

Red tests must cover:
- Every AMC-owned table has `organisation_id` column present and used in RLS policies
- No external service may directly write to AMC-owned tables (all external mutations arrive via validated callback endpoints)
- State mutations (alert ack, approval decision, intervention status change) propagate via Supabase Realtime broadcast to `amc_executive_state_{user_id}` channel within 2 seconds
- Consequential database operations (action + audit event pair) execute in a single database transaction: if audit event INSERT fails, the action is rolled back
- `idempotency` enforcement: attempting to re-apply an already-processed approval decision returns HTTP 409

### 7.5 Audit/Provenance Expectations

**Architecture Reference**: §4.4 (Audit & Provenance Contract Architecture), §6.3

Red tests must cover:
- `audit_events` table enforces INSERT-only via RLS (attempting UPDATE or DELETE returns permission denied)
- Every consequential action produces at least one audit event before returning success to caller
- If the audit event INSERT fails, the consequential action is rolled back (not committed without audit)
- `actor` and `actor_type` fields are populated from JWT or service token on every audit event (never from caller-supplied data)
- Knowledge content displayed in AMC includes provenance metadata from the knowledge retrieval response
- Displaying knowledge without provenance triggers an audit event

### 7.6 Trust/Authority Boundary Expectations

**Architecture Reference**: §7 (Trust Boundaries and Authority Boundaries), §3.3 (Backend/API Architecture §Middleware)

Red tests must cover:
- Every API route enforces Auth Middleware → Actor Resolution → Authority-Domain Check sequence before handler executes
- `reserved_matter` boundary: any actor other than `human` with Johan Ras identity claim returns HTTP 403
- `delegated` boundary: `ai_executive` actors exceeding their configured scope in `authority_domain_config` return HTTP 403
- Authority enforcement is server-side; a client-side-only check that can be bypassed by direct API call fails the test
- All inbound callbacks (AIMC, Foreman, specialist agents) require valid `Authorization: Bearer {service_token}` header; missing or invalid token returns HTTP 401
- Service token identity is validated and cannot be elevated by caller manipulation

### 7.7 Degraded-Mode and Dependency-Loss Behavior

**Architecture Reference**: §6.4 (Degraded-Mode Behavior Architecture), §5.1–5.5

Red tests must cover:
- AIMC unavailable: all `POST /api/aimc/*` return HTTP 503; Maturion Proactive Panel renders exact required string: "Maturion communication unavailable — AIMC unreachable"
- AIMC unavailable: no fallback AI call path exists (no direct model provider call occurs)
- AIMCC unavailable: quota and upload reads return last-cached data with `stale: true, stale_since` marker
- AIMCC unavailable: AIMCC governance actions remain `pending` (not auto-processed)
- Knowledge system unavailable: knowledge retrieval returns HTTP 503; all knowledge surfaces show unavailable indicator
- Foreman unavailable: intervention dispatch returns HTTP 503 with explicit error; Foreman reporting feed displays `{ status: "unavailable", last_known_at }`
- No degraded mode is silent: every dependency degradation writes a `system_health_events` row and a dependency-specific audit event
- Recovery detection resets degraded state via the `amc-health-poll-scheduler` (not via a manual reset endpoint)

### 7.8 Alert Delivery and Escalation Architecture

**Architecture Reference**: §4.3 (Alert/Escalation Contract Architecture)

Red tests must cover:
- Critical, High, Medium alerts cannot be dismissed without non-empty `dismiss_reason`; server-side enforcement returns HTTP 422 on missing reason
- Alert escalation levels are sequential: Level 1 before Level 2; level-skipping is prohibited
- Failed alert INSERT triggers retry with exponential back-off (retry 1 at 1s, retry 2 at 3s, retry 3 at 10s); after 3 failures, fallback audit sink is written
- Push notification dispatch failure does not block alert creation; failure is recorded as an audit event
- Alert delivery SLA monitoring: breach detection writes `ALERT_DELIVERY_DELAYED` audit event

### 7.9 Session Restore and Cross-Device Continuity

**Architecture Reference**: §6.2 (Cross-Device / Cross-Session Continuity)

Red tests must cover:
- On session restore, AMC frontend fetches fresh data from: `/api/dashboard/summary`, `/api/alerts?status=active`, `/api/approvals?status=pending`, `/api/interventions?status=active`, `/api/conversation/messages?limit=20`
- If any session-restore fetch fails: explicit error indicator is rendered — no silent fallback to last-known local state as current
- All critical state domains are server-side (not client-local-only)

### 7.10 Real-Time Architecture

**Architecture Reference**: §3.5 (Real-Time Architecture)

Red tests must cover:
- Alert status changes broadcast to `amc_executive_state_{user_id}` channel within ≤2 seconds of INSERT commit
- ARC surface updates broadcast to `amc_arc_{user_id}` within ≤2 seconds of referenced alert acknowledgment
- Subscriptions created on mount and cleaned up on unmount (no subscription leak)
- Local component state updates immediately on Realtime event (no stale-while-revalidate that surfaces contradictory states without explicit staleness indicator)

### 7.11 Configuration Validation at Startup

**Architecture Reference**: §3.3 (Backend/API Architecture — Configuration Validation at Startup)

Red tests must cover:
- Application startup fails if any required environment variable is absent
- Startup error names the missing variable explicitly (not a generic "configuration error")
- Missing any of these variables causes startup failure: `AIMC_API_BASE_URL`, `AIMCC_API_BASE_URL`, `KUC_API_BASE_URL`, `KNOWLEDGE_API_BASE_URL`, `FOREMAN_API_BASE_URL`, `SPECIALIST_AGENT_API_BASE_URL`, and all corresponding service tokens

### 7.12 Background Scheduler Architecture

**Architecture Reference**: §3.6 (Background Scheduler Architecture)

Red tests must cover:
- Each scheduled Edge Function is implemented with the specified cadence (not inline in API routes)
- Scheduler failure generates a Critical alert with `source_system: "amc_scheduler"` and function name
- All threshold and timeout values are read from environment variables (no hardcoded defaults)

---

## 8. Deployment-Strategy-Derived Red Coverage Model

This section defines the required red-test coverage families for Stage 5a DES commitments. Each family is traceable to one or more DES fields. Full test IDs are defined in `red-test-catalog.md`.

### 8.1 DES-001 — Deployment Surface Ownership Boundaries

**DES Reference**: DES-001 (Workflow Surface Ownership)

Red tests must cover:
- `deploy-frontend.yml` exists and owns frontend deploy surface; no other workflow deploys the frontend
- `db-migrate.yml` exists and owns the DB migration surface; no other workflow executes database migrations
- `ci.yml` owns schema verification on PRs; schema verification does not modify the database
- Live operational validation is a manual process; no workflow automates post-deployment health validation
- No deployment surface listed in DES-001 is owned by more than one workflow or process

### 8.2 DES-002/DES-003 — GitHub-Hosted Runner Authorization Boundaries

**DES Reference**: DES-002 (GitHub-Hosted Runner Authorization), DES-003 (Self-Hosted Runner Requirement)

Red tests must cover:
- All CI gate stages (`ci.yml`) use `runs-on: ubuntu-latest` (GitHub-hosted)
- `deploy-frontend.yml` uses `runs-on: ubuntu-latest`
- `db-migrate.yml` uses `runs-on: ubuntu-latest`
- No self-hosted runner label (`self-hosted`, or any custom runner label) appears in any workflow file
- Introducing a self-hosted runner reference in any workflow file is detected and must fail the CI dependency/configuration check

### 8.3 DES-004 — Migration Execution Path (Supabase CLI Only)

**DES Reference**: DES-004 (Migration Execution Path)

Red tests must cover:
- `db-migrate.yml` uses `supabase db push --project-ref $SUPABASE_PROJECT_REF` as the migration command
- No `psql` direct connection command appears in any workflow file
- No manual SQL execution step (other than `supabase db push`) appears in `db-migrate.yml`
- No migration script references a local developer machine execution path
- `SUPABASE_ACCESS_TOKEN` is consumed from environment variable; no hardcoded value appears
- `SUPABASE_PROJECT_REF` is sourced from environment secret; no hardcoded project reference appears in workflow YAML
- The `supabase db push --linked` flag is NOT used (stateful link model is prohibited)
- Migration files live under `supabase/migrations/` and nowhere else

### 8.4 DES-005 — CI / Preview / Production Trigger Boundaries

**DES Reference**: DES-005 (CI/Preview/Production Execution Boundaries)

Red tests must cover:
- `ci.yml` is triggered on pull_request (not on push to main as the primary trigger for CI gate)
- `deploy-frontend.yml` is NOT triggered on pull_request; it is triggered on push to main or manual dispatch only
- `db-migrate.yml` is NOT triggered automatically on push to main; it uses `workflow_dispatch` only
- Database migration does NOT run on pull_request under any workflow
- Vercel preview deployments are NOT managed by a GitHub Actions workflow step in `ci.yml` (managed by Vercel GitHub App)
- `deploy-frontend.yml` declares a dependency on `ci.yml` success before executing production steps

### 8.5 DES-006 — Frontend Workflow DB Mutation Prohibition

**DES Reference**: DES-006 (Safety Classification — safety boundary enforcement)

Red tests must cover:
- `deploy-frontend.yml` contains NO `supabase db push` step
- `deploy-frontend.yml` contains NO `psql` step
- `deploy-frontend.yml` does NOT reference `SUPABASE_SERVICE_ROLE_KEY` (which grants production DB write access)
- `ci.yml` schema verification step does NOT mutate the database (read-only schema introspection only)
- Any PR that adds a DB mutation step to `deploy-frontend.yml` must fail the CI check and the QP evaluation

### 8.6 DES-007 — Production Protected-Environment Approval Requirement

**DES Reference**: DES-007 (Manual/Protected Approval Boundaries)

Red tests must cover:
- `deploy-frontend.yml` production job step references `environment: production` (GitHub protected environment)
- `db-migrate.yml` production job step references `environment: production`
- Removing the `environment: production` declaration from either workflow is detected and fails the merge check
- A deployment or migration step that would run without the `production` environment approval gate is prohibited
- No automatic (un-gated) production deployment occurs on push to main without `production` environment approval

### 8.7 DES-008 — Environment / Network Pre-Flight Fail-Safe Behavior

**DES Reference**: DES-008 (Environment/Network Assumption Validation)

Red tests must cover:
- Application startup: if `NEXT_PUBLIC_SUPABASE_URL` is absent → startup blocked with explicit error naming the variable
- Application startup: if `AIMC_API_BASE_URL` is absent → startup blocked with explicit error naming the variable
- `db-migrate.yml` pre-flight: if `SUPABASE_ACCESS_TOKEN` is absent → migration aborts immediately (no DB connection attempted)
- `db-migrate.yml` pre-flight: if `SUPABASE_PROJECT_REF` is absent → migration aborts immediately
- `deploy-frontend.yml` pre-flight: if `VERCEL_TOKEN` is absent → deploy aborts immediately
- Fail-safe behavior is "fail loudly, fail early" — no silent-continue past any missing pre-flight check
- Project reference mismatch (staging ref used in production job, or vice versa) → migration aborts

---

## 9. Literal-Operability Sanity Checks

This section defines red test coverage for the exact kinds of literal-operability defects that must be prevented in AMC — defects arising from hidden-state dependencies, cross-workflow assumption failures, ambiguous trigger models, or contradictory descriptions.

### 9.1 Hidden-State Dependencies in Workflows

Red tests must cover:
- No workflow step assumes a preceding step's output is in a global variable not declared as an explicit `outputs:` or environment variable export
- No workflow assumes a prior `supabase link` step has been executed (stateful link model is prohibited per DES-004)
- No step in `db-migrate.yml` assumes the Supabase CLI is pre-installed without an explicit installation step
- No step in `deploy-frontend.yml` assumes Vercel CLI is pre-installed without an explicit installation step

### 9.2 Cross-Workflow Dependency Assumptions

Red tests must cover:
- `deploy-frontend.yml` does NOT assume `ci.yml` output artifacts are available in the deploy job unless they are explicitly passed via `needs:` and `outputs:` declarations
- No workflow references an environment secret from a different environment scope (e.g., a `staging` job must not reference `production`-scoped secrets and vice versa)
- No workflow assumes that a previous manual run set a persistent state that is consumed in the current run

### 9.3 Ambiguous Trigger Models

Red tests must cover:
- `db-migrate.yml` has no `push` or `pull_request` trigger — only `workflow_dispatch`; any other trigger is a literal-operability defect
- `deploy-frontend.yml` has no `pull_request` trigger — any PR-triggered production deployment is a literal-operability defect
- `ci.yml` runs on `pull_request` and `push` to `main`; unexpected trigger additions (e.g., `schedule` in `ci.yml`) must be flagged

### 9.4 Inconsistent Environment Targeting

Red tests must cover:
- The environment name used in `deploy-frontend.yml` production steps is exactly `production` (not `prod`, `live`, or any alias)
- The environment name used in `db-migrate.yml` production steps is exactly `production`
- Staging-environment steps in any workflow do NOT reference the `production` environment
- The `SUPABASE_PROJECT_REF` secret used in staging and production jobs is sourced from the correct environment (staging secret in staging job, production secret in production job)

### 9.5 Contradictory Migration/Deploy/Approval Descriptions

Red tests must cover:
- The workflow YAML for `db-migrate.yml` is consistent with the description in DES-004: `supabase db push --project-ref $SUPABASE_PROJECT_REF` and no other mechanism
- The approval gate declaration in `db-migrate.yml` production job matches DES-007: `environment: production` with required reviewers configured
- No workflow file comment or step `name:` field contradicts the behavior described in DES-001 through DES-008

---

## 10. Anti-Drift QA Posture

### 10.1 Governing Statement

Any builder PR or downstream implementation that deviates from Stage 5 Architecture (`modules/amc/04-architecture/architecture-specification.md` v1.0) or Stage 5a DES (`modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` v1.0) without a formal CS2-approved amendment must fail QA-to-Red.

This is not interpretive — a deviation is defined as any implementation choice that:
- Contradicts a named architecture commitment in Stage 5
- Contradicts a DES field answer in Stage 5a (DES-001 through DES-008)
- Omits a component, table, channel, or endpoint that Stage 5 Architecture defines as mandatory
- Uses a deployment surface, runner type, migration mechanism, or trigger condition not defined in Stage 5a

### 10.2 Amendment is the Only Permitted Path

If a legitimate implementation requirement conflicts with Stage 5 or Stage 5a:
1. The builder HALTS and escalates to the Foreman
2. The Foreman raises a Stage 5 or Stage 5a amendment issue with CS2
3. CS2 approves or rejects the amendment
4. If approved: the upstream document is updated with version increment and CS2 sign-off; all downstream Stage 6 test cases that reference the amended item are updated
5. Silent deviation without amendment is a QP FAIL condition regardless of the quality of the implementation

### 10.3 QP FAIL Conditions (anti-drift)

The QP must issue FAIL when any of the following drift indicators are present in a builder PR:

| Drift Indicator | Stage 5 / Stage 5a Reference | Severity |
|---|---|---|
| AI SDK package in `package.json` | Architecture §2 TR-BOUNDARY-001 | CRITICAL |
| Direct call to AIMCC ingestion endpoint from AMC code | Architecture §2 TR-BOUNDARY-002 | CRITICAL |
| AMC table storing canonical knowledge content | Architecture §2 TR-BOUNDARY-003 | CRITICAL |
| Outbound API call missing `Authorization: Bearer` header | Architecture §2 TR-BOUNDARY-004 | HIGH |
| Migration mechanism other than Supabase CLI | DES-004 | HIGH |
| Self-hosted runner in any workflow | DES-003 | HIGH |
| `deploy-frontend.yml` performing DB mutation | DES-006 | CRITICAL |
| `production` environment gate removed from production workflow | DES-007 | CRITICAL |
| Hardcoded `SUPABASE_PROJECT_REF` or `SUPABASE_ACCESS_TOKEN` | DES-004/DES-008 | HIGH |
| Startup silently continuing past missing required env var | Architecture §3.3 / DES-008 | HIGH |
| ARC implemented as a filter over alerts rather than a distinct table | Architecture §4.1 | HIGH |
| Quota change not requiring approval workflow | Architecture §4.2 | HIGH |
| Audit event missing on consequential action | Architecture §4.4 | CRITICAL |
| Authority enforcement only client-side | Architecture §7 | CRITICAL |

---

## 11. Coverage Completeness Declaration

This Stage 6 QA-to-Red Specification provides red-test coverage for:

- ✅ All major Stage 5 Architecture commitments (Sections 7.1–7.12)
- ✅ All 8 Stage 5a DES fields (Sections 8.1–8.7, DES-001 through DES-008)
- ✅ Literal-operability failure modes (Section 9)
- ✅ Anti-drift QA posture (Section 10)

**Intentional deferrals beyond Stage 6:**
- Column-level DDL tests (deferred to schema-builder; dependency: schema implementation)
- React component tree and UI rendering tests at pixel level (deferred to ui-builder; dependency: component implementation)
- CI script implementation tests (deferred to Stage 12; dependency: actual workflow YAML implementation)
- Load testing and performance benchmarking (deferred to operational testing; outside Stage 6 scope)
- End-to-end user journey tests (deferred to qa-builder; dependency: full stack implementation)

**Explicitly NOT deferred:**
- Boundary invariants (TR-BOUNDARY-001 through TR-BOUNDARY-004) — covered in Section 7.1
- All DES fields DES-001 through DES-008 — covered in Sections 8.1–8.7
- All critical audit/authority/state ownership commitments — covered in Sections 7.4–7.6
- Literal-operability workflow defect patterns — covered in Section 9

---

## 12. Sign-Off / Approval Record

| Field | Value |
|---|---|
| **Document** | AMC QA-to-Red Specification — Stage 6 |
| **Version** | 1.0 |
| **Prepared by** | foreman-v2-agent (POLC_ORCHESTRATION) |
| **Prepared Date** | 2026-04-27 |
| **CS2 Authorization for Stage 6** | app_management_centre#1141 |
| **Governing Delivery Issue** | app_management_centre#1141 |
| **Stage 5 Architecture Reference** | `modules/amc/04-architecture/architecture-specification.md` v1.0 (produced approval-pending, ref #1131) |
| **Stage 5a DES Reference** | `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` v1.0 (produced approval-pending, ref #1137) |
| **Wave** | amc-stage6-qa-to-red-20260427 |
| **Reviewed by** | *Pending CS2 review* |
| **Approved by** | *Pending CS2 approval* |
| **Approval Date** | *Pending* |
| **Approval Reference** | *To be assigned by CS2 on approval* |
| **Stage** | Stage 6 of the AMC-local 12+1 stage sequence |
| **Next Stage** | Stage 7 — PBFAG (BLOCKED until Stage 6, Stage 5, and Stage 5a all receive CS2 approval) |

### Approval Basis Required

CS2 approval of this document confirms:

1. The QA-to-Red specification is explicit, complete, and non-contradictory with Stage 5 Architecture and Stage 5a DES
2. The red-test coverage is sufficient for Stage 7 PBFAG to verify mechanically rather than interpretively
3. All major architecture commitments and all 8 DES fields are covered
4. Literal-operability failure modes are explicitly represented
5. The anti-drift posture is enforceable by QP evaluation
6. Stage 7 PBFAG is authorized to use this document as its verification reference
7. Stage 12 qa-builder is authorized to implement red tests to the specification defined in `red-test-catalog.md`

### Version History

| Version | Date | Change Summary |
|---|---|---|
| 1.0 | 2026-04-27 | Initial production — complete Stage 6 QA-to-Red specification; 12 coverage families for architecture (§7) and 7 families for DES (§8); literal-operability section (§9); anti-drift posture (§10); coverage completeness declaration (§11); CS2 sign-off section; governing delivery issue: app_management_centre#1141 |

---

*AMC QA-to-Red Specification v1.0 — 2026-04-27 — governing delivery issue: app_management_centre#1141 — CS2 authorization: app_management_centre#1141*

# Red Test Catalog — Stage 6

**Stage**: 6 — QA-to-Red
**Module**: App Management Centre (AMC)
**Version**: 1.0
**Status**: 🟡 Produced — Approval Pending (CS2)
**Author**: foreman-v2-agent (POLC_ORCHESTRATION)
**CS2 Authorization**: app_management_centre#1141
**Governing Delivery Issue**: app_management_centre#1141
**Wave**: amc-stage6-qa-to-red-20260427
**Date**: 2026-04-27
**Upstream Sources**:
- Stage 5 Architecture: `modules/amc/04-architecture/architecture-specification.md` v1.0
- Stage 5a DES: `modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md` v1.0
- Stage 5a Surface Table: `modules/amc/05a-deployment-execution-strategy/deployment-surface-ownership-table.md` v1.0
- Stage 5a Runner Constraints: `modules/amc/05a-deployment-execution-strategy/runner-and-environment-constraints.md` v1.0
**Specification Reference**: `modules/amc/05-qa-to-red/qa-to-red-specification.md` v1.0
**Canonical Location**: `modules/amc/05-qa-to-red/red-test-catalog.md`

---

> **STAGE ENTRY CONDITION NOTICE**
> Stage 5 and Stage 5a are produced approval-pending. This catalog is conditional on
> Stage 5 and Stage 5a receiving CS2 approval before Stage 7 proceeds. Authorized for
> production now per CS2 issue #1141.

---

## Catalog Structure

Each test entry contains:
- **Test ID**: Unique identifier (used in traceability matrix)
- **Source Requirement / Source Artifact**: Architecture section or DES field reference
- **Scenario**: What the test exercises
- **Expected Fail Condition**: What the implementation does WRONG that causes this test to FAIL (red state)
- **Expected Pass Condition**: What the implementation must do for this test to PASS (green state)
- **Severity**: CRITICAL / HIGH / MEDIUM / LOW (per `qa-to-red-specification.md` §3)
- **Blocker**: YES / NO (per `qa-to-red-specification.md` §4)
- **Required Evidence Type**: unit / integration / e2e / config-check / static-analysis

---

## Section A — Cross-System Boundary Tests (QA-ARCH family)

---

### QA-ARCH-001 — AI SDK Prohibition in Dependencies

| Field | Value |
|---|---|
| **Test ID** | QA-ARCH-001 |
| **Source Requirement** | Architecture §2, TR-BOUNDARY-001 |
| **Source Artifact** | `architecture-specification.md` §2 |
| **Scenario** | AMC `package.json` is scanned for AI model provider SDK packages at CI time |
| **Expected Fail Condition** | `package.json` lists any of: `openai`, `@anthropic-ai/sdk`, `@google/generative-ai`, `ai`, `langchain`, or any model-provider SDK as a dependency or devDependency |
| **Expected Pass Condition** | `package.json` contains no AI model provider SDK as a dependency or devDependency; CI dependency scan step exits 0 |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (CI dependency scan output) |

---

### QA-ARCH-002 — No Direct AIMCC Ingestion Calls

| Field | Value |
|---|---|
| **Test ID** | QA-ARCH-002 |
| **Source Requirement** | Architecture §2, TR-BOUNDARY-002 |
| **Source Artifact** | `architecture-specification.md` §2 |
| **Scenario** | AMC codebase is scanned for any direct calls to AIMCC internal ingestion endpoints |
| **Expected Fail Condition** | Any AMC source file contains a call to `{AIMCC_API_BASE_URL}/ingest`, `/ingest/*`, or any AIMCC ingestion path other than `/uploads/status`, `/quota/current`, or `/governance/decision` |
| **Expected Pass Condition** | No AMC source file references an AIMCC ingestion endpoint; all knowledge upload submissions POST to `{KUC_API_BASE_URL}/submit` only |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (code scan for AIMCC endpoint references) |

---

### QA-ARCH-003 — No Knowledge Content Columns in AMC Tables

| Field | Value |
|---|---|
| **Test ID** | QA-ARCH-003 |
| **Source Requirement** | Architecture §2, TR-BOUNDARY-003 |
| **Source Artifact** | `architecture-specification.md` §2 |
| **Scenario** | AMC database schema is checked for columns that store canonical knowledge/memory content as AMC-owned truth |
| **Expected Fail Condition** | Any AMC-owned table contains a column with name or type indicating canonical knowledge storage (e.g., `knowledge_content`, `memory_text`, `embedding`, `vector`) as a non-transient, non-cache field |
| **Expected Pass Condition** | No AMC-owned table stores canonical knowledge content; any cached knowledge field has TTL metadata (e.g., `cached_at`, `cache_expires_at`) present |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (schema inspection) |

---

### QA-ARCH-004 — Service Token on All Outbound Calls

| Field | Value |
|---|---|
| **Test ID** | QA-ARCH-004 |
| **Source Requirement** | Architecture §2, TR-BOUNDARY-004 |
| **Source Artifact** | `architecture-specification.md` §2 |
| **Scenario** | AMC integration client services are unit-tested to confirm they attach `Authorization: Bearer {service_token}` on every outbound API call |
| **Expected Fail Condition** | Any outbound call from AMC to an external service (AIMC, AIMCC, KUC, Knowledge System, Foreman, Specialist Agent) is made without an `Authorization: Bearer` header |
| **Expected Pass Condition** | All integration client service unit tests confirm `Authorization: Bearer {service_token}` is attached to every request; missing token causes the call to be blocked, not forwarded |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | unit (integration client unit tests) |

---

### QA-ARCH-005 — BOUNDARY_BYPASS_ATTEMPTED Audit Event

| Field | Value |
|---|---|
| **Test ID** | QA-ARCH-005 |
| **Source Requirement** | Architecture §5.6 |
| **Source Artifact** | `architecture-specification.md` §5.6 |
| **Scenario** | Runtime detection of boundary bypass attempt (e.g., request to AIMC endpoint that attempts to include a model provider action directly) writes a `BOUNDARY_BYPASS_ATTEMPTED` audit event and generates a Critical alert |
| **Expected Fail Condition** | A detected boundary bypass attempt does NOT generate a `BOUNDARY_BYPASS_ATTEMPTED` audit event, or the audit event is generated but no Critical alert follows |
| **Expected Pass Condition** | On boundary bypass detection: (1) `BOUNDARY_BYPASS_ATTEMPTED` inserted into `audit_events`; (2) Critical alert inserted into `alerts` with `source_system: "amc_boundary_monitor"`; both in a single transaction |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (boundary bypass detection integration test) |

---

### QA-ARCH-006 — KUC API Submit Path Only for Knowledge Upload

| Field | Value |
|---|---|
| **Test ID** | QA-ARCH-006 |
| **Source Requirement** | Architecture §5.3 |
| **Source Artifact** | `architecture-specification.md` §5.3 |
| **Scenario** | AMC knowledge upload submission code is checked to confirm it POSTs exclusively to `{KUC_API_BASE_URL}/submit` |
| **Expected Fail Condition** | Any knowledge upload submission from AMC code references `{AIMCC_API_BASE_URL}` or any path other than `{KUC_API_BASE_URL}/submit` |
| **Expected Pass Condition** | All AMC knowledge upload submissions POST to `{KUC_API_BASE_URL}/submit`; the KUC client unit test confirms the correct URL is used |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | unit (KUC client unit test) |

---

## Section B — ARC Domain Tests (QA-ARC family)

---

### QA-ARC-001 — `arc_classifications` is a Distinct Table

| Field | Value |
|---|---|
| **Test ID** | QA-ARC-001 |
| **Source Requirement** | Architecture §4.1 |
| **Source Artifact** | `architecture-specification.md` §4.1 |
| **Scenario** | Database schema is inspected to confirm `arc_classifications` exists as an independent table |
| **Expected Fail Condition** | `arc_classifications` does not exist as a base table; it is implemented as a view, a derived result, or data is stored in a generic `classifications` or `arc_items` column on another table |
| **Expected Pass Condition** | `information_schema.tables` (or Supabase schema introspection) confirms `arc_classifications` exists with `table_type = 'BASE TABLE'` |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (schema inspection) |

---

### QA-ARC-002 — `/api/arc/` Namespace Exists and is Separate

| Field | Value |
|---|---|
| **Test ID** | QA-ARC-002 |
| **Source Requirement** | Architecture §4.1 |
| **Source Artifact** | `architecture-specification.md` §4.1 |
| **Scenario** | API routing is checked to confirm `/api/arc/` routes exist and are not delegated to `/api/alerts/` handlers |
| **Expected Fail Condition** | ARC operations (classify, begin-resolution, resolve, escalate-externally) are handled by routes under `/api/alerts/` or `/api/approvals/` rather than `/api/arc/` |
| **Expected Pass Condition** | Route handlers exist under `app/api/arc/` path; ARC endpoints (`/api/arc/{id}/begin-resolution`, `/api/arc/{id}/resolve`, `/api/arc/{id}/escalate-externally`) return correct responses |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (API routing test) |

---

### QA-ARC-003 — `/arc` Frontend Route Accessible from Navigation

| Field | Value |
|---|---|
| **Test ID** | QA-ARC-003 |
| **Source Requirement** | Architecture §3.2, §4.1 |
| **Source Artifact** | `architecture-specification.md` §3.2, §4.1 |
| **Scenario** | Frontend routing is checked to confirm `/arc` route exists and is accessible from the executive navigation sidebar |
| **Expected Fail Condition** | `/arc` route does not exist in Next.js routing; or `/arc` route exists but is not linked from the executive navigation sidebar |
| **Expected Pass Condition** | `app/arc/page.tsx` (or equivalent) exists; navigation sidebar renders a link to `/arc`; navigating to `/arc` does not produce a 404 |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | unit (route existence check + navigation unit test) |

---

### QA-ARC-004 — `amc_arc_{user_id}` Realtime Channel Subscribed Separately

| Field | Value |
|---|---|
| **Test ID** | QA-ARC-004 |
| **Source Requirement** | Architecture §4.1 |
| **Source Artifact** | `architecture-specification.md` §4.1 |
| **Scenario** | ARC surface Realtime subscription code is verified to subscribe to `amc_arc_{user_id}` as a distinct channel |
| **Expected Fail Condition** | ARC events are received via the `amc_executive_state_{user_id}` channel instead of a dedicated `amc_arc_{user_id}` channel |
| **Expected Pass Condition** | ARC surface subscribes to `amc_arc_{user_id}` channel on mount; unsubscribes on unmount; subscription is independent of `amc_executive_state_{user_id}` |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | unit (Realtime subscription unit test) |

---

### QA-ARC-005 — ARC State Transitions via Correct Endpoints

| Field | Value |
|---|---|
| **Test ID** | QA-ARC-005 |
| **Source Requirement** | Architecture §4.1 |
| **Source Artifact** | `architecture-specification.md` §4.1 |
| **Scenario** | ARC state machine is exercised: open → in_resolution → resolved via the defined POST endpoints |
| **Expected Fail Condition** | Any ARC state transition is performed by directly updating the `arc_classifications` table from the client side (bypassing the API); or a state transition endpoint is missing |
| **Expected Pass Condition** | `POST /api/arc/{id}/begin-resolution` transitions `open → in_resolution`; `POST /api/arc/{id}/resolve` transitions `in_resolution → resolved`; each writes `ARC_ITEM_STATE_CHANGED` audit event |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (ARC state machine integration test) |

---

### QA-ARC-006 — Boundary-Bypass ARC Item Requires Johan Ras Human Actor

| Field | Value |
|---|---|
| **Test ID** | QA-ARC-006 |
| **Source Requirement** | Architecture §4.1 |
| **Source Artifact** | `architecture-specification.md` §4.1 |
| **Scenario** | Attempt to resolve a boundary-bypass ARC item using an `ai_executive` actor token |
| **Expected Fail Condition** | Resolution attempt with `ai_executive` actor token against a boundary-bypass ARC item returns HTTP 200 or HTTP 202 (unauthorized actor accepted) |
| **Expected Pass Condition** | Resolution attempt with `ai_executive` actor token returns HTTP 403; only a `human` actor with Johan Ras identity claim may resolve boundary-bypass ARC items |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (authority enforcement integration test) |

---

### QA-ARC-007 — ARC Staleness Detection via Scheduler (Not Inline)

| Field | Value |
|---|---|
| **Test ID** | QA-ARC-007 |
| **Source Requirement** | Architecture §3.6, §4.1 |
| **Source Artifact** | `architecture-specification.md` §3.6, §4.1 |
| **Scenario** | ARC staleness detection (open/in_resolution items past SLA) generates Medium alerts via `amc-arc-staleness-scheduler` Edge Function |
| **Expected Fail Condition** | ARC staleness detection is implemented inline in the alert creation path or in a React component lifecycle; or it generates Critical alerts instead of Medium |
| **Expected Pass Condition** | `amc-arc-staleness-scheduler` Edge Function exists; when triggered, it generates Medium alerts for stale ARC items referencing the ARC item ID |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (Edge Function invocation test) |

---

### QA-ARC-008 — ARC Audit Events on All State Transitions

| Field | Value |
|---|---|
| **Test ID** | QA-ARC-008 |
| **Source Requirement** | Architecture §4.1 |
| **Source Artifact** | `architecture-specification.md` §4.1 |
| **Scenario** | Each ARC state transition is verified to generate the correct audit event |
| **Expected Fail Condition** | An ARC state transition completes without inserting the corresponding audit event into `audit_events` |
| **Expected Pass Condition** | `ARC_ITEM_CLASSIFIED` written on classification; `ARC_ITEM_STATE_CHANGED` written on any state transition; `ARC_ITEM_RESOLVED` written on resolution; `ARC_ITEM_EXTERNALLY_ESCALATED` written on external escalation |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (audit event assertion in ARC state machine tests) |

---

## Section C — Quota Management Tests (QA-QUOTA family)

---

### QA-QUOTA-001 — Sole Quota Initiation Path

| Field | Value |
|---|---|
| **Test ID** | QA-QUOTA-001 |
| **Source Requirement** | Architecture §4.2 |
| **Source Artifact** | `architecture-specification.md` §4.2 |
| **Scenario** | Quota adjustment initiation is tested to confirm `POST /api/aimcc/quota/request-adjustment` is the only path |
| **Expected Fail Condition** | Any other API route or client-side code directly modifies quota values without going through `/api/aimcc/quota/request-adjustment` |
| **Expected Pass Condition** | `POST /api/aimcc/quota/request-adjustment` creates a `reserved_matter` approval record; no other path can initiate a quota adjustment |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (quota initiation path test) |

---

### QA-QUOTA-002 — Quota Adjustment Requires Approval Record

| Field | Value |
|---|---|
| **Test ID** | QA-QUOTA-002 |
| **Source Requirement** | Architecture §4.2 |
| **Source Artifact** | `architecture-specification.md` §4.2 |
| **Scenario** | Quota adjustment initiation is verified to always create a `reserved_matter` approval record |
| **Expected Fail Condition** | Quota adjustment request creates no approval record; or creates an `operational` scope approval record instead of `reserved_matter` |
| **Expected Pass Condition** | `POST /api/aimcc/quota/request-adjustment` creates an `approvals` record with `authority_boundary_type: "reserved_matter"` before returning success |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (approval record assertion) |

---

### QA-QUOTA-003 — Quota Change Without Approval Returns HTTP 422

| Field | Value |
|---|---|
| **Test ID** | QA-QUOTA-003 |
| **Source Requirement** | Architecture §4.2 |
| **Source Artifact** | `architecture-specification.md` §4.2 |
| **Scenario** | Attempt to execute a quota change without a corresponding completed approval record |
| **Expected Fail Condition** | Quota change proceeds without a completed approval record (approval record either missing or in `pending` state) |
| **Expected Pass Condition** | Quota change without a completed approval record returns HTTP 422 with an error body indicating approval is required |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (approval gate enforcement test) |

---

### QA-QUOTA-004 — AIMCC Notified via Correct Path

| Field | Value |
|---|---|
| **Test ID** | QA-QUOTA-004 |
| **Source Requirement** | Architecture §4.2 |
| **Source Artifact** | `architecture-specification.md` §4.2 |
| **Scenario** | After quota approval, the AIMCC notification is tested to confirm it POSTs to `{AIMCC_API_BASE_URL}/governance/decision` |
| **Expected Fail Condition** | AIMCC is notified via a different endpoint; or no notification is sent to AIMCC after quota approval |
| **Expected Pass Condition** | After `approvals` record is approved, AMC integration client POSTs to `{AIMCC_API_BASE_URL}/governance/decision` with the decision payload |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (AIMCC notification path test) |

---

### QA-QUOTA-005 — Temporary Override Requires `override_expiry_at`

| Field | Value |
|---|---|
| **Test ID** | QA-QUOTA-005 |
| **Source Requirement** | Architecture §4.2 |
| **Source Artifact** | `architecture-specification.md` §4.2 |
| **Scenario** | Temporary quota override request is submitted without `override_expiry_at` field |
| **Expected Fail Condition** | Temporary override request without `override_expiry_at` is accepted and creates an approval record |
| **Expected Pass Condition** | Temporary override request without `override_expiry_at` returns HTTP 422; request with valid `override_expiry_at` creates approval record |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (override validation test) |

---

### QA-QUOTA-006 — Quota Threshold Transitions Generate Alerts and Audit Events

| Field | Value |
|---|---|
| **Test ID** | QA-QUOTA-006 |
| **Source Requirement** | Architecture §4.2, TR-607 |
| **Source Artifact** | `architecture-specification.md` §4.2 |
| **Scenario** | Quota usage crosses the warning threshold; test confirms alert and audit event are generated |
| **Expected Fail Condition** | Quota usage crosses warning threshold but no alert is generated and no audit event is inserted |
| **Expected Pass Condition** | When quota crosses `QUOTA_WARNING_THRESHOLD_PERCENT`: (1) High alert inserted with quota reference; (2) audit event with event type `QUOTA_THRESHOLD_ENTERED` inserted; both in the same transaction |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (quota threshold state machine test) |

---

### QA-QUOTA-007 — Quota Thresholds from Environment Variables

| Field | Value |
|---|---|
| **Test ID** | QA-QUOTA-007 |
| **Source Requirement** | Architecture §4.2, TR-607 |
| **Source Artifact** | `architecture-specification.md` §4.2 |
| **Scenario** | Quota threshold configuration is checked to confirm values are read from `QUOTA_WARNING_THRESHOLD_PERCENT` and `QUOTA_CRITICAL_THRESHOLD_PERCENT` environment variables |
| **Expected Fail Condition** | Quota threshold values are hardcoded in source code (e.g., `const warningThreshold = 80`) rather than read from environment variables |
| **Expected Pass Condition** | Threshold monitor reads `process.env.QUOTA_WARNING_THRESHOLD_PERCENT` and `process.env.QUOTA_CRITICAL_THRESHOLD_PERCENT`; unit test confirms different env values produce different threshold behavior |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | unit (threshold configuration unit test) |

---

### QA-QUOTA-008 — Quota History Reconstructable from `audit_events`

| Field | Value |
|---|---|
| **Test ID** | QA-QUOTA-008 |
| **Source Requirement** | Architecture §4.2 |
| **Source Artifact** | `architecture-specification.md` §4.2 |
| **Scenario** | After several quota changes, the full change history is queried from `audit_events` without requiring a separate quota history table |
| **Expected Fail Condition** | `audit_events` does not contain sufficient quota change events to reconstruct full history; a separate `quota_history` table is required to answer the history query |
| **Expected Pass Condition** | All quota adjustment events are recorded in `audit_events` with `event_type` in the quota family; full change history is reconstructable via `GET /api/audit-events?domain=quota` |
| **Severity** | MEDIUM |
| **Blocker** | NO |
| **Required Evidence Type** | integration (audit event query test) |

---

## Section D — State Ownership and Consistency Tests (QA-STATE family)

---

### QA-STATE-001 — `organisation_id` Present in All AMC-Owned Tables

| Field | Value |
|---|---|
| **Test ID** | QA-STATE-001 |
| **Source Requirement** | Architecture §3.4, §6.1 |
| **Source Artifact** | `architecture-specification.md` §3.4 |
| **Scenario** | Schema inspection verifies `organisation_id` column exists on all 9 canonical AMC-owned tables |
| **Expected Fail Condition** | Any canonical AMC-owned table (`alerts`, `approvals`, `interventions`, `audit_events`, `conversation_messages`, `aimc_action_log`, `knowledge_retrieval_log`, `system_health_events`, `arc_classifications`) is missing the `organisation_id` column |
| **Expected Pass Condition** | All 9 tables have `organisation_id` column; RLS policies reference `organisation_id` for all tables |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (schema inspection test) |

---

### QA-STATE-002 — External Services Cannot Write AMC-Owned Tables Directly

| Field | Value |
|---|---|
| **Test ID** | QA-STATE-002 |
| **Source Requirement** | Architecture §6.1 |
| **Source Artifact** | `architecture-specification.md` §6.1 |
| **Scenario** | External service callback endpoint is tested: callback with invalid service token is rejected; direct DB write attempt via external credentials fails |
| **Expected Fail Condition** | Callback endpoint accepts requests without validating the `Authorization: Bearer {service_token}` header; or external service can write directly to AMC tables without going through a callback endpoint |
| **Expected Pass Condition** | Callback endpoint returns HTTP 401 on missing/invalid service token; all external state mutations arrive via validated callback endpoints only |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (callback validation test) |

---

### QA-STATE-003 — State Mutations Propagate via Realtime Within 2 Seconds

| Field | Value |
|---|---|
| **Test ID** | QA-STATE-003 |
| **Source Requirement** | Architecture §6.1, §3.5 |
| **Source Artifact** | `architecture-specification.md` §6.1 |
| **Scenario** | Alert status change is performed; Realtime broadcast to `amc_executive_state_{user_id}` is measured |
| **Expected Fail Condition** | Realtime broadcast does not occur; or broadcast occurs more than 2 seconds after the INSERT commit |
| **Expected Pass Condition** | Supabase Realtime subscription receives the state change event within ≤2 seconds of INSERT commit (measured in integration test environment) |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (Realtime propagation timing test) |

---

### QA-STATE-004 — Action and Audit Event in Single Transaction

| Field | Value |
|---|---|
| **Test ID** | QA-STATE-004 |
| **Source Requirement** | Architecture §6.1, §4.4 |
| **Source Artifact** | `architecture-specification.md` §6.1 |
| **Scenario** | Audit event INSERT is forced to fail; test verifies the corresponding action INSERT is also rolled back |
| **Expected Fail Condition** | Action (e.g., alert acknowledgment) is committed to the database but the corresponding audit event is NOT committed (partial write) |
| **Expected Pass Condition** | When audit event INSERT fails (simulated via test), the action INSERT is also rolled back; neither record appears in the database |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (transaction atomicity test) |

---

### QA-STATE-005 — Approval Idempotency: Already-Processed → HTTP 409

| Field | Value |
|---|---|
| **Test ID** | QA-STATE-005 |
| **Source Requirement** | Architecture §6.1 |
| **Source Artifact** | `architecture-specification.md` §6.1 |
| **Scenario** | An approval decision is submitted twice (same approval ID, same decision) |
| **Expected Fail Condition** | Second approval submission succeeds (HTTP 200/202) and creates a duplicate approval record or overwrites the existing decision |
| **Expected Pass Condition** | Second approval submission returns HTTP 409 with current state; no duplicate record is created; the approval decision is not re-processed |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (idempotency test) |

---

## Section E — Audit and Provenance Tests (QA-AUDIT family)

---

### QA-AUDIT-001 — `audit_events` Table is INSERT-Only

| Field | Value |
|---|---|
| **Test ID** | QA-AUDIT-001 |
| **Source Requirement** | Architecture §4.4, §6.3 |
| **Source Artifact** | `architecture-specification.md` §4.4 |
| **Scenario** | Attempt to UPDATE or DELETE a row in `audit_events` using service role credentials |
| **Expected Fail Condition** | UPDATE or DELETE operation on `audit_events` succeeds |
| **Expected Pass Condition** | RLS policy denies UPDATE and DELETE on `audit_events` even with service role credentials; operations return permission denied |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (RLS enforcement test) |

---

### QA-AUDIT-002 — Consequential Action Produces Audit Event Before Success

| Field | Value |
|---|---|
| **Test ID** | QA-AUDIT-002 |
| **Source Requirement** | Architecture §4.4 |
| **Source Artifact** | `architecture-specification.md` §4.4 |
| **Scenario** | A consequential action (e.g., approval decision) is submitted; audit event insertion is verified before response is returned |
| **Expected Fail Condition** | HTTP 200/202 is returned for the consequential action, but no corresponding `audit_events` row is inserted (or row is inserted asynchronously after the response) |
| **Expected Pass Condition** | `audit_events` row is inserted within the same transaction as the action; audit event is present when queried immediately after the action returns |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (audit-before-success test) |

---

### QA-AUDIT-003 — Audit INSERT Failure Rolls Back Action

| Field | Value |
|---|---|
| **Test ID** | QA-AUDIT-003 |
| **Source Requirement** | Architecture §4.4, §6.1 |
| **Source Artifact** | `architecture-specification.md` §4.4 |
| **Scenario** | Audit event INSERT is forced to fail (simulated constraint violation); test verifies the action INSERT is also rolled back |
| **Expected Fail Condition** | Action INSERT commits to the database despite the audit INSERT failure (action without audit trail) |
| **Expected Pass Condition** | Both action and audit INSERT fail atomically; neither record appears in the database; error is returned to the caller |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (audit atomicity rollback test) |

---

### QA-AUDIT-004 — `actor` and `actor_type` from JWT/Service Token Only

| Field | Value |
|---|---|
| **Test ID** | QA-AUDIT-004 |
| **Source Requirement** | Architecture §4.4 |
| **Source Artifact** | `architecture-specification.md` §4.4 |
| **Scenario** | Request body contains a caller-supplied `actor` field attempting to override the authenticated actor; test verifies the server-resolved actor is used |
| **Expected Fail Condition** | `audit_events` row shows the caller-supplied `actor` value instead of the server-resolved actor from the JWT or service token |
| **Expected Pass Condition** | `actor` and `actor_type` in `audit_events` are populated from server-resolved JWT/service token identity; caller-supplied `actor` field is ignored |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (actor identity test) |

---

### QA-AUDIT-005 — Knowledge Display Includes Provenance Metadata

| Field | Value |
|---|---|
| **Test ID** | QA-AUDIT-005 |
| **Source Requirement** | Architecture §6.3 |
| **Source Artifact** | `architecture-specification.md` §6.3 |
| **Scenario** | Knowledge retrieval response without provenance metadata is returned from the knowledge system; test verifies AMC does not display this without an indicator |
| **Expected Fail Condition** | Knowledge content is displayed in AMC without provenance metadata; no audit event is generated for the missing provenance |
| **Expected Pass Condition** | Knowledge retrieval response includes `provenance` metadata; if absent, AMC raises an audit event and does not display the content as authoritative |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (provenance display test) |

---

### QA-AUDIT-006 — Missing Provenance Triggers Audit Event

| Field | Value |
|---|---|
| **Test ID** | QA-AUDIT-006 |
| **Source Requirement** | Architecture §6.3 |
| **Source Artifact** | `architecture-specification.md` §6.3 |
| **Scenario** | Knowledge retrieval response is returned without provenance metadata; test verifies an audit event is inserted |
| **Expected Fail Condition** | AMC renders knowledge content without provenance silently, with no audit event generated |
| **Expected Pass Condition** | When provenance is absent from knowledge retrieval response, an audit event with event_type `KNOWLEDGE_PROVENANCE_GAP` is inserted into `audit_events` |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (provenance gap audit test) |

---

## Section F — Trust and Authority Boundary Tests (QA-AUTH family)

---

### QA-AUTH-001 — API Middleware Chain Executes in Order

| Field | Value |
|---|---|
| **Test ID** | QA-AUTH-001 |
| **Source Requirement** | Architecture §3.3 |
| **Source Artifact** | `architecture-specification.md` §3.3 |
| **Scenario** | API route handler is tested with a missing JWT; test verifies HTTP 401 is returned before the handler executes |
| **Expected Fail Condition** | Route handler executes (partial or full) before Auth Middleware validates the JWT; request without JWT reaches the route handler |
| **Expected Pass Condition** | Request without JWT returns HTTP 401 from Auth Middleware before Actor Resolution or Authority-Domain Check runs; route handler is never invoked |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (middleware chain test) |

---

### QA-AUTH-002 — Reserved Matter: Non-Human Actor Returns HTTP 403

| Field | Value |
|---|---|
| **Test ID** | QA-AUTH-002 |
| **Source Requirement** | Architecture §7.2 |
| **Source Artifact** | `architecture-specification.md` §7.2 |
| **Scenario** | `ai_executive` actor token submits a request to a `reserved_matter` endpoint (e.g., quota adjustment approval) |
| **Expected Fail Condition** | `ai_executive` actor succeeds on a `reserved_matter` endpoint (HTTP 200/202 returned) |
| **Expected Pass Condition** | `ai_executive` actor returns HTTP 403; only `human` actor with Johan Ras identity claim succeeds |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (authority boundary test) |

---

### QA-AUTH-003 — Delegated: Out-of-Scope `ai_executive` Returns HTTP 403

| Field | Value |
|---|---|
| **Test ID** | QA-AUTH-003 |
| **Source Requirement** | Architecture §7.2 |
| **Source Artifact** | `architecture-specification.md` §7.2 |
| **Scenario** | `ai_executive` actor token attempts an action outside its configured scope in `authority_domain_config` |
| **Expected Fail Condition** | `ai_executive` actor succeeds on a `delegated` endpoint that is not in its configured scope |
| **Expected Pass Condition** | `ai_executive` actor returns HTTP 403 for out-of-scope `delegated` actions; `authority_domain_config` lookup is performed server-side |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (delegated scope enforcement test) |

---

### QA-AUTH-004 — Authority Enforcement is Server-Side (Not Client-Side-Only)

| Field | Value |
|---|---|
| **Test ID** | QA-AUTH-004 |
| **Source Requirement** | Architecture §7 |
| **Source Artifact** | `architecture-specification.md` §7 |
| **Scenario** | Direct API call to `reserved_matter` endpoint bypassing the UI (no UI session, raw HTTP request) with unauthorized actor |
| **Expected Fail Condition** | Direct API call with unauthorized actor succeeds because the UI-layer restriction is only client-side |
| **Expected Pass Condition** | HTTP 403 returned regardless of whether the request originates from the UI or a direct API call; server-side authority check is in the middleware chain |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (server-side enforcement test) |

---

### QA-AUTH-005 — Inbound Callbacks Require Valid Service Token

| Field | Value |
|---|---|
| **Test ID** | QA-AUTH-005 |
| **Source Requirement** | Architecture §7.1 |
| **Source Artifact** | `architecture-specification.md` §7.1 |
| **Scenario** | AIMC callback endpoint is tested with a missing or invalid service token |
| **Expected Fail Condition** | Callback endpoint accepts the request without a valid `Authorization: Bearer {AIMC_SERVICE_TOKEN}` header |
| **Expected Pass Condition** | Missing or invalid service token returns HTTP 401; callback with valid service token returns HTTP 202 (or 200) and processes the callback |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (callback authentication test) |

---

### QA-AUTH-006 — Service Token Identity Cannot be Elevated

| Field | Value |
|---|---|
| **Test ID** | QA-AUTH-006 |
| **Source Requirement** | Architecture §7.1 |
| **Source Artifact** | `architecture-specification.md` §7.1 |
| **Scenario** | Inbound callback includes a forged `actor_type: "human"` in the request body; test verifies server uses the token-resolved actor type |
| **Expected Fail Condition** | Server uses the caller-supplied `actor_type` from the request body, granting elevated authority to a service-token bearer |
| **Expected Pass Condition** | Server resolves `actor_type` from the service token metadata, not from caller-supplied fields; forged `actor_type` in request body is ignored |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (token identity test) |

---

## Section G — Degraded-Mode Tests (QA-DEGRADE family)

---

### QA-DEGRADE-001 — AIMC Unavailable: All AIMC Endpoints Return HTTP 503

| Field | Value |
|---|---|
| **Test ID** | QA-DEGRADE-001 |
| **Source Requirement** | Architecture §5.1, §6.4 |
| **Source Artifact** | `architecture-specification.md` §5.1, §6.4 |
| **Scenario** | AIMC health endpoint returns non-200; subsequent AIMC dispatch is attempted |
| **Expected Fail Condition** | AIMC degraded mode is not entered; dispatch continues and reaches AIMC; or a fallback AI model provider call is attempted |
| **Expected Pass Condition** | After AIMC health failure, all `POST /api/aimc/*` return HTTP 503; no fallback AI call occurs; `AIMC_DEGRADED` audit event is written |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | integration (degraded mode test) |

---

### QA-DEGRADE-002 — Maturion Proactive Panel Exact String on AIMC Degraded

| Field | Value |
|---|---|
| **Test ID** | QA-DEGRADE-002 |
| **Source Requirement** | Architecture §5.1 |
| **Source Artifact** | `architecture-specification.md` §5.1 |
| **Scenario** | AIMC is degraded; Maturion Proactive Panel is rendered |
| **Expected Fail Condition** | Panel renders a different message (e.g., "AI unavailable", "Service error", or blank) instead of the exact required string |
| **Expected Pass Condition** | Panel renders exactly: `"Maturion communication unavailable — AIMC unreachable"` (exact string, case-sensitive match) |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | unit (UI string assertion test) |

---

### QA-DEGRADE-003 — AIMCC Unavailable: Stale Cache with `stale: true, stale_since`

| Field | Value |
|---|---|
| **Test ID** | QA-DEGRADE-003 |
| **Source Requirement** | Architecture §5.2, §6.4 |
| **Source Artifact** | `architecture-specification.md` §5.2, §6.4 |
| **Scenario** | AIMCC health endpoint returns non-200; quota read is attempted |
| **Expected Fail Condition** | Quota read returns an error or returns cached data without `stale: true` and `stale_since` markers |
| **Expected Pass Condition** | Quota read returns last-cached data with `{ stale: true, stale_since: <detected_at> }` in the response; UI displays explicit staleness indicator |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (stale cache test) |

---

### QA-DEGRADE-004 — AIMCC Unavailable: Governance Actions Remain Pending

| Field | Value |
|---|---|
| **Test ID** | QA-DEGRADE-004 |
| **Source Requirement** | Architecture §5.2 |
| **Source Artifact** | `architecture-specification.md` §5.2 |
| **Scenario** | AIMCC is degraded; an approved quota change attempts to notify AIMCC |
| **Expected Fail Condition** | AMC auto-processes or discards the AIMCC governance decision notification when AIMCC is unavailable |
| **Expected Pass Condition** | AIMCC governance decision notification is queued with `queued_for_retry: true`; decision remains in `pending` state until AIMCC recovers |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (AIMCC governance pending test) |

---

### QA-DEGRADE-005 — Knowledge System Unavailable: HTTP 503 + Unavailable Indicator

| Field | Value |
|---|---|
| **Test ID** | QA-DEGRADE-005 |
| **Source Requirement** | Architecture §5.4, §6.4 |
| **Source Artifact** | `architecture-specification.md` §5.4, §6.4 |
| **Scenario** | Knowledge system health endpoint returns non-200; knowledge retrieval is attempted |
| **Expected Fail Condition** | Knowledge retrieval returns cached data without staleness indicator, or returns HTTP 200 with knowledge content while the knowledge system is unavailable |
| **Expected Pass Condition** | Knowledge retrieval returns HTTP 503; all knowledge reference surfaces show an unavailable indicator |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (knowledge degraded mode test) |

---

### QA-DEGRADE-006 — Foreman Unavailable: HTTP 503 + Structured Response

| Field | Value |
|---|---|
| **Test ID** | QA-DEGRADE-006 |
| **Source Requirement** | Architecture §5.5, §6.4 |
| **Source Artifact** | `architecture-specification.md` §5.5, §6.4 |
| **Scenario** | Foreman health endpoint returns non-200; intervention dispatch is attempted |
| **Expected Fail Condition** | Intervention dispatch attempt returns HTTP 200/202 (no error); or Foreman reporting returns blank data without an unavailability indicator |
| **Expected Pass Condition** | Intervention dispatch returns HTTP 503 with explicit error; Foreman reporting feed returns `{ status: "unavailable", last_known_at: <timestamp> }` |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (Foreman degraded mode test) |

---

### QA-DEGRADE-007 — Degraded Mode Entry Writes `system_health_events` Row and Audit Event

| Field | Value |
|---|---|
| **Test ID** | QA-DEGRADE-007 |
| **Source Requirement** | Architecture §6.4 |
| **Source Artifact** | `architecture-specification.md` §6.4 |
| **Scenario** | AIMC health endpoint returns non-200; test verifies both `system_health_events` row and `AIMC_DEGRADED` audit event are written |
| **Expected Fail Condition** | Degraded mode is entered but either `system_health_events` row or `AIMC_DEGRADED` audit event is missing |
| **Expected Pass Condition** | `system_health_events` row inserted with `event_type: "degraded"` and `dependency: "aimc"`; `AIMC_DEGRADED` audit event inserted in the same transaction |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (degraded mode observability test) |

---

### QA-DEGRADE-008 — Recovery Resets Degraded State via Health Poll

| Field | Value |
|---|---|
| **Test ID** | QA-DEGRADE-008 |
| **Source Requirement** | Architecture §6.5 |
| **Source Artifact** | `architecture-specification.md` §6.5 |
| **Scenario** | After AIMC degraded mode, AIMC health endpoint returns HTTP 200 (recovered); test verifies recovery procedure executes |
| **Expected Fail Condition** | Recovery is not detected on next health poll; or recovery requires a manual reset endpoint call; or `AIMC_RECOVERED` audit event is missing |
| **Expected Pass Condition** | On next poll returning HTTP 200: `system_health_events` updated with `recovered_at`; `AIMC_RECOVERED` audit event inserted; Realtime broadcast sent; normal operation resumes |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (recovery detection test) |

---

## Section H — Alert Delivery Tests (QA-ALERT family)

---

### QA-ALERT-001 — Critical/High/Medium Cannot be Dismissed Without Reason

| Field | Value |
|---|---|
| **Test ID** | QA-ALERT-001 |
| **Source Requirement** | Architecture §4.3 |
| **Source Artifact** | `architecture-specification.md` §4.3 |
| **Scenario** | Dismissal request for a Critical alert is submitted with empty `dismiss_reason` field |
| **Expected Fail Condition** | Alert is dismissed successfully despite empty `dismiss_reason`; or dismissal returns HTTP 200/202 |
| **Expected Pass Condition** | Dismissal with empty `dismiss_reason` returns HTTP 422; server-side enforcement prevents dismissal regardless of client-side UI state |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (dismissal enforcement test) |

---

### QA-ALERT-002 — Alert Escalation is Sequential (No Level Skip)

| Field | Value |
|---|---|
| **Test ID** | QA-ALERT-002 |
| **Source Requirement** | Architecture §4.3 |
| **Source Artifact** | `architecture-specification.md` §4.3 |
| **Scenario** | Alert is created; test simulates time passage past Level 2 escalation timeout without Level 1 having fired; test verifies Level 1 fires before Level 2 |
| **Expected Fail Condition** | Level 2 escalation fires without Level 1 having fired; or escalation scheduler skips Level 1 entirely when time exceeds Level 2 timeout |
| **Expected Pass Condition** | Level 1 escalation fires at `ALERT_ESCALATION_LEVEL_1_MINUTES`; Level 2 fires at `ALERT_ESCALATION_LEVEL_2_MINUTES`; Level 1 must have fired before Level 2 can fire |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (escalation sequence test) |

---

### QA-ALERT-003 — Alert INSERT Retry with Exponential Back-off

| Field | Value |
|---|---|
| **Test ID** | QA-ALERT-003 |
| **Source Requirement** | Architecture §4.3 |
| **Source Artifact** | `architecture-specification.md` §4.3 |
| **Scenario** | Alert INSERT is forced to fail (simulated DB error); test verifies retry behavior and fallback audit sink |
| **Expected Fail Condition** | Alert INSERT failure causes immediate error without retry; or retry is attempted with uniform delay (not exponential back-off); or after 3 failures, no fallback sink is written |
| **Expected Pass Condition** | Retry 1 at 1s, retry 2 at 3s, retry 3 at 10s; after 3 failures, write to durable fallback audit sink; `SYSTEM_ERROR` alert generated on recovery |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (retry behavior test) |

---

### QA-ALERT-004 — Push Notification Failure Does Not Block Alert Creation

| Field | Value |
|---|---|
| **Test ID** | QA-ALERT-004 |
| **Source Requirement** | Architecture §4.3 |
| **Source Artifact** | `architecture-specification.md` §4.3 |
| **Scenario** | Push notification dispatch is forced to fail; test verifies alert INSERT still commits and returns success |
| **Expected Fail Condition** | Alert creation fails (HTTP 500 or rollback) because push notification dispatch failed |
| **Expected Pass Condition** | Alert INSERT commits successfully (HTTP 200/202); push failure is recorded as an audit event but does not cause alert rollback |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (push failure decoupling test) |

---

### QA-ALERT-005 — SLA Breach Writes `ALERT_DELIVERY_DELAYED` Audit Event

| Field | Value |
|---|---|
| **Test ID** | QA-ALERT-005 |
| **Source Requirement** | Architecture §4.3 |
| **Source Artifact** | `architecture-specification.md` §4.3 |
| **Scenario** | Alert INSERT to Realtime broadcast delay is simulated to exceed 2 seconds; test verifies `ALERT_DELIVERY_DELAYED` audit event is written |
| **Expected Fail Condition** | SLA breach occurs but no audit event is written; or `ALERT_DELIVERY_DELAYED` is written but with incorrect `severity` |
| **Expected Pass Condition** | `ALERT_DELIVERY_DELAYED` audit event inserted with `severity: warning` and breach metadata; event is written by `amc-alert-timing-sla-monitor` component |
| **Severity** | MEDIUM |
| **Blocker** | NO |
| **Required Evidence Type** | integration (SLA monitoring test) |

---

## Section I — Session Restore Tests (QA-SESSION family)

---

### QA-SESSION-001 — Session Restore Fetches All 5 Required Endpoints

| Field | Value |
|---|---|
| **Test ID** | QA-SESSION-001 |
| **Source Requirement** | Architecture §6.2 |
| **Source Artifact** | `architecture-specification.md` §6.2 |
| **Scenario** | AMC frontend loads (session restore); test verifies all 5 defined API calls are made |
| **Expected Fail Condition** | Any of the 5 required endpoints is not called on session restore |
| **Expected Pass Condition** | On load, requests are made to: `GET /api/dashboard/summary`, `GET /api/alerts?status=active`, `GET /api/approvals?status=pending`, `GET /api/interventions?status=active`, `GET /api/conversation/messages?limit=20` |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | unit (session restore unit test, HTTP call assertions) |

---

### QA-SESSION-002 — Failed Session-Restore Fetch Shows Error Indicator

| Field | Value |
|---|---|
| **Test ID** | QA-SESSION-002 |
| **Source Requirement** | Architecture §6.2 |
| **Source Artifact** | `architecture-specification.md` §6.2 |
| **Scenario** | One of the 5 session-restore API calls fails with HTTP 503; test verifies explicit error indicator is rendered |
| **Expected Fail Condition** | Failed session-restore fetch is silently ignored; last-known local state is displayed as current without error indicator |
| **Expected Pass Condition** | Failed session-restore fetch causes an explicit error indicator to be rendered; no stale data is presented as current without indicator |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | unit (error indicator rendering test) |

---

### QA-SESSION-003 — All Critical State is Server-Side

| Field | Value |
|---|---|
| **Test ID** | QA-SESSION-003 |
| **Source Requirement** | Architecture §6.2 |
| **Source Artifact** | `architecture-specification.md` §6.2 |
| **Scenario** | Browser local storage and session storage are cleared; session restore is performed; test verifies critical state is fully restored from server |
| **Expected Fail Condition** | Critical state (alerts, approvals, interventions) is missing after clearing local storage because it was stored only client-locally |
| **Expected Pass Condition** | All critical state is fully restored from server API calls; clearing browser storage does not result in data loss |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (server-side state persistence test) |

---

## Section J — Real-Time Architecture Tests (QA-RT family)

---

### QA-RT-001 — Alert Changes Broadcast via Realtime Within ≤2 Seconds

| Field | Value |
|---|---|
| **Test ID** | QA-RT-001 |
| **Source Requirement** | Architecture §3.5, §6.1 |
| **Source Artifact** | `architecture-specification.md` §3.5 |
| **Scenario** | Alert status is changed (e.g., acknowledged) via the API; elapsed time to Realtime broadcast receipt on a subscribed client is measured |
| **Expected Fail Condition** | Realtime broadcast does not arrive within 2 seconds of the INSERT/UPDATE commit; or broadcast is never sent |
| **Expected Pass Condition** | Supabase Realtime subscription receives the alert status change event within ≤2 seconds of the database commit in an integration test environment |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (Realtime SLA timing test) |

---

### QA-RT-002 — ARC Surface Updates Broadcast Within ≤2 Seconds

| Field | Value |
|---|---|
| **Test ID** | QA-RT-002 |
| **Source Requirement** | Architecture §3.5, §4.1 |
| **Source Artifact** | `architecture-specification.md` §3.5 |
| **Scenario** | An alert is acknowledged; the resulting ARC surface state change is measured for Realtime broadcast latency on `amc_arc_{user_id}` channel |
| **Expected Fail Condition** | ARC surface Realtime broadcast does not arrive within 2 seconds of the triggering acknowledgment commit |
| **Expected Pass Condition** | `amc_arc_{user_id}` subscription receives the ARC surface update event within ≤2 seconds of the database commit |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (Realtime SLA timing test) |

---

### QA-RT-003 — Realtime Subscriptions Cleaned Up on Unmount

| Field | Value |
|---|---|
| **Test ID** | QA-RT-003 |
| **Source Requirement** | Architecture §3.5 |
| **Source Artifact** | `architecture-specification.md` §3.5 |
| **Scenario** | A component that subscribes to a Realtime channel is mounted, then unmounted; channel subscription state is inspected |
| **Expected Fail Condition** | The Realtime subscription remains active after the component unmounts (subscription leak); a second mount creates a duplicate subscription |
| **Expected Pass Condition** | Component subscribes on mount; subscription is unsubscribed and cleaned up on unmount; no active subscription exists after unmount |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | unit (Realtime subscription lifecycle test) |

---

### QA-RT-004 — Component State Updates Immediately on Realtime Event

| Field | Value |
|---|---|
| **Test ID** | QA-RT-004 |
| **Source Requirement** | Architecture §3.5 |
| **Source Artifact** | `architecture-specification.md` §3.5 |
| **Scenario** | A Realtime event is received; local component state is inspected before the next server-side fetch |
| **Expected Fail Condition** | Component does not update local state on receipt of Realtime event; or renders a stale state alongside the new event without an explicit staleness indicator |
| **Expected Pass Condition** | Component state updates immediately on Realtime event receipt; no contradictory (stale vs current) states are displayed simultaneously without an explicit indicator |
| **Severity** | MEDIUM |
| **Blocker** | NO |
| **Required Evidence Type** | unit (Realtime event state update test) |

---

## Section K — Configuration Validation Tests (QA-CONFIG family)

---

### QA-CONFIG-001 — Startup Fails on Any Missing Required Environment Variable

| Field | Value |
|---|---|
| **Test ID** | QA-CONFIG-001 |
| **Source Requirement** | Architecture §3.3, TR-1505 |
| **Source Artifact** | `architecture-specification.md` §3.3 |
| **Scenario** | Application is started with one required environment variable unset (each variable tested in turn) |
| **Expected Fail Condition** | Application starts and serves traffic despite the missing required variable |
| **Expected Pass Condition** | Application startup fails immediately (non-zero exit or unrecoverable error) when any required environment variable is absent; no traffic is served |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (startup validation test) |

---

### QA-CONFIG-002 — Startup Error Explicitly Names the Missing Variable

| Field | Value |
|---|---|
| **Test ID** | QA-CONFIG-002 |
| **Source Requirement** | Architecture §3.3 |
| **Source Artifact** | `architecture-specification.md` §3.3 |
| **Scenario** | Application is started with `AIMC_API_BASE_URL` unset; startup error output is inspected |
| **Expected Fail Condition** | Startup error message is generic (e.g., "Configuration error", "Missing environment variable") without naming the specific missing variable |
| **Expected Pass Condition** | Startup error message contains the exact variable name `AIMC_API_BASE_URL`; operators can identify the missing variable from the error alone |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (startup error message test) |

---

### QA-CONFIG-003 — All 12 Required Environment Variables Cause Startup Failure if Absent

| Field | Value |
|---|---|
| **Test ID** | QA-CONFIG-003 |
| **Source Requirement** | Architecture §3.3 |
| **Source Artifact** | `architecture-specification.md` §3.3 |
| **Scenario** | Each of the 12 required environment variables is individually unset; startup behavior is tested for each |
| **Expected Fail Condition** | Any of the 12 required variables does not cause startup failure when absent |
| **Expected Pass Condition** | Startup fails with variable-naming error for each of the 12 required variables: `AIMC_API_BASE_URL`, `AIMC_SERVICE_TOKEN`, `AIMCC_API_BASE_URL`, `AIMCC_SERVICE_TOKEN`, `KUC_API_BASE_URL`, `KUC_SERVICE_TOKEN`, `KNOWLEDGE_API_BASE_URL`, `KNOWLEDGE_SERVICE_TOKEN`, `FOREMAN_API_BASE_URL`, `FOREMAN_SERVICE_TOKEN`, `SPECIALIST_AGENT_API_BASE_URL`, `SPECIALIST_AGENT_SERVICE_TOKEN` |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (full required-variable coverage startup test) |

---

## Section L — Background Scheduler Tests (QA-SCHED family)

---

### QA-SCHED-001 — Scheduled Jobs Implemented as Supabase Edge Functions

| Field | Value |
|---|---|
| **Test ID** | QA-SCHED-001 |
| **Source Requirement** | Architecture §3.6 |
| **Source Artifact** | `architecture-specification.md` §3.6 |
| **Scenario** | AMC codebase is inspected for scheduled recurring operations (staleness detection, health poll, alert SLA monitoring, escalation) to confirm they exist as Edge Functions |
| **Expected Fail Condition** | Any scheduled recurring operation is implemented inline in an API route handler, a React component lifecycle, or a client-side timer rather than as a Supabase Edge Function |
| **Expected Pass Condition** | Each scheduled operation (`amc-arc-staleness-scheduler`, `amc-health-poll-scheduler`, `amc-alert-escalation-scheduler`) exists as a Supabase Edge Function in the `supabase/functions/` directory |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (Edge Function existence check) |

---

### QA-SCHED-002 — Scheduler Failure Generates Critical Alert With Function Name

| Field | Value |
|---|---|
| **Test ID** | QA-SCHED-002 |
| **Source Requirement** | Architecture §3.6 |
| **Source Artifact** | `architecture-specification.md` §3.6 |
| **Scenario** | A scheduled Edge Function is triggered and throws an unhandled exception; alert generation is verified |
| **Expected Fail Condition** | Scheduler failure does not generate an alert; or generates an alert without the function name or `source_system: "amc_scheduler"` field |
| **Expected Pass Condition** | On Edge Function failure: Critical alert inserted with `source_system: "amc_scheduler"` and `function_name: "<function-name>"` fields |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (scheduler failure alert test) |

---

### QA-SCHED-003 — Scheduler Threshold and Timeout Values from Environment Variables

| Field | Value |
|---|---|
| **Test ID** | QA-SCHED-003 |
| **Source Requirement** | Architecture §3.6 |
| **Source Artifact** | `architecture-specification.md` §3.6 |
| **Scenario** | Scheduled Edge Function source code is inspected for hardcoded threshold or timeout values |
| **Expected Fail Condition** | Any scheduler Edge Function contains hardcoded threshold values (e.g., `const STALENESS_THRESHOLD_HOURS = 24`) instead of reading from environment variables |
| **Expected Pass Condition** | All scheduler threshold and timeout values are read from environment variables (e.g., `Deno.env.get('ARC_STALENESS_THRESHOLD_HOURS')`); unit test confirms different env values produce different threshold behavior |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | unit (scheduler configuration test) |

---

## Section M — Deployment Strategy Tests (QA-DES family)

### QA-DES001-001 — `deploy-frontend.yml` Owns Frontend Deploy Exclusively

| Field | Value |
|---|---|
| **Test ID** | QA-DES001-001 |
| **Source Requirement** | DES-001, `deployment-surface-ownership-table.md` SURF-001, SURF-002 |
| **Source Artifact** | `deployment-execution-strategy.md` §3.1 |
| **Scenario** | All workflow YAML files in `.github/workflows/` are scanned for Vercel deployment steps |
| **Expected Fail Condition** | A workflow file other than `deploy-frontend.yml` contains a Vercel CLI deploy step |
| **Expected Pass Condition** | Only `deploy-frontend.yml` contains Vercel deploy steps; no other workflow file triggers a Vercel deployment |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (workflow file scan) |

---

### QA-DES001-002 — `db-migrate.yml` Owns DB Migration Exclusively

| Field | Value |
|---|---|
| **Test ID** | QA-DES001-002 |
| **Source Requirement** | DES-001, `deployment-surface-ownership-table.md` SURF-003 |
| **Source Artifact** | `deployment-execution-strategy.md` §3.1 |
| **Scenario** | All workflow YAML files are scanned for `supabase db push` steps |
| **Expected Fail Condition** | A workflow file other than `db-migrate.yml` contains a `supabase db push` step |
| **Expected Pass Condition** | Only `db-migrate.yml` contains `supabase db push`; no other workflow performs database migration |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (workflow file scan) |

---

### QA-DES002-001 — `ci.yml` Uses `ubuntu-latest` Runner

| Field | Value |
|---|---|
| **Test ID** | QA-DES002-001 |
| **Source Requirement** | DES-002, DES-003, `runner-and-environment-constraints.md` |
| **Source Artifact** | `deployment-execution-strategy.md` §3.2, §3.3 |
| **Scenario** | `ci.yml` workflow YAML is checked for `runs-on` configuration |
| **Expected Fail Condition** | Any job in `ci.yml` uses a runner other than `ubuntu-latest` (self-hosted, custom, or different OS) |
| **Expected Pass Condition** | All jobs in `ci.yml` declare `runs-on: ubuntu-latest` |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (workflow YAML runner check) |

---

### QA-DES003-001 — No Self-Hosted Runner in Any Workflow

| Field | Value |
|---|---|
| **Test ID** | QA-DES003-001 |
| **Source Requirement** | DES-003 |
| **Source Artifact** | `deployment-execution-strategy.md` §3.3 |
| **Scenario** | All workflow YAML files are scanned for self-hosted runner labels |
| **Expected Fail Condition** | Any workflow file contains `runs-on: self-hosted`, `runs-on: [self-hosted, ...]`, or any custom runner label other than `ubuntu-latest` |
| **Expected Pass Condition** | No workflow file contains self-hosted or custom runner labels; all `runs-on` values are `ubuntu-latest` |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (workflow YAML runner scan) |

---

### QA-DES004-001 — Migration Uses Exact Approved Command

| Field | Value |
|---|---|
| **Test ID** | QA-DES004-001 |
| **Source Requirement** | DES-004 |
| **Source Artifact** | `deployment-execution-strategy.md` §3.4 |
| **Scenario** | `db-migrate.yml` is inspected for the migration execution command |
| **Expected Fail Condition** | Migration command is anything other than `supabase db push --project-ref $SUPABASE_PROJECT_REF`; OR the `--linked` flag is used; OR project ref is hardcoded |
| **Expected Pass Condition** | `db-migrate.yml` contains exactly `supabase db push --project-ref $SUPABASE_PROJECT_REF`; no alternative migration command is present; no hardcoded project ref |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (workflow YAML command check) |

---

### QA-DES005-001 — `db-migrate.yml` Uses `workflow_dispatch` Only

| Field | Value |
|---|---|
| **Test ID** | QA-DES005-001 |
| **Source Requirement** | DES-005 |
| **Source Artifact** | `deployment-execution-strategy.md` §3.5 |
| **Scenario** | `db-migrate.yml` `on:` trigger block is inspected |
| **Expected Fail Condition** | `db-migrate.yml` has any trigger other than `workflow_dispatch` (e.g., `push`, `pull_request`, `schedule`) |
| **Expected Pass Condition** | `db-migrate.yml` `on:` block contains only `workflow_dispatch`; no automatic triggers are configured |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (workflow YAML trigger check) |

---

### QA-DES006-001 — `deploy-frontend.yml` Contains No `supabase db push` Step

| Field | Value |
|---|---|
| **Test ID** | QA-DES006-001 |
| **Source Requirement** | DES-006 |
| **Source Artifact** | `deployment-execution-strategy.md` §3.6 |
| **Scenario** | `deploy-frontend.yml` is scanned for database mutation steps |
| **Expected Fail Condition** | `deploy-frontend.yml` contains `supabase db push`, `psql`, or any other database mutation step |
| **Expected Pass Condition** | `deploy-frontend.yml` contains no `supabase db push` or `psql` step; no database mutation is present |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (workflow YAML DB step scan) |

---

### QA-DES007-001 — `deploy-frontend.yml` Production Job References `environment: production`

| Field | Value |
|---|---|
| **Test ID** | QA-DES007-001 |
| **Source Requirement** | DES-007 |
| **Source Artifact** | `deployment-execution-strategy.md` §3.7 |
| **Scenario** | `deploy-frontend.yml` production job is inspected for `environment:` declaration |
| **Expected Fail Condition** | Production deployment job does not declare `environment: production`; or uses `environment: prod`, `environment: live`, or any other alias |
| **Expected Pass Condition** | Production deployment job in `deploy-frontend.yml` declares `environment: production` (exact string); GitHub `production` environment is configured with required reviewers |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (workflow YAML environment check) |

---

### QA-DES008-001 — Startup Fails With Explicit Error on Missing `NEXT_PUBLIC_SUPABASE_URL`

| Field | Value |
|---|---|
| **Test ID** | QA-DES008-001 |
| **Source Requirement** | DES-008, Architecture §3.3 |
| **Source Artifact** | `deployment-execution-strategy.md` §3.8 |
| **Scenario** | Application is started with `NEXT_PUBLIC_SUPABASE_URL` environment variable unset |
| **Expected Fail Condition** | Application starts successfully without `NEXT_PUBLIC_SUPABASE_URL`; or startup fails with a generic error not naming the missing variable |
| **Expected Pass Condition** | Application startup fails immediately with an explicit error message that includes the name `NEXT_PUBLIC_SUPABASE_URL`; no traffic is served |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | integration (startup validation test) |

---

## Section N — Literal-Operability Tests (QA-LITOP family)

---

### QA-LITOP-001 — No Hidden-State Supabase Link Assumption in Workflows

| Field | Value |
|---|---|
| **Test ID** | QA-LITOP-001 |
| **Source Requirement** | DES-004 (prohibition on `supabase db push --linked`) |
| **Source Artifact** | `deployment-execution-strategy.md` §3.4 |
| **Scenario** | `db-migrate.yml` is inspected for any assumption that a `supabase link` step has been previously executed |
| **Expected Fail Condition** | `db-migrate.yml` uses `supabase db push --linked` or contains a `supabase link` step that sets up a stateful link for subsequent steps |
| **Expected Pass Condition** | `db-migrate.yml` uses only `supabase db push --project-ref $SUPABASE_PROJECT_REF` (stateless, no prior link step required) |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (workflow YAML link step scan) |

---

### QA-LITOP-002 — No Implicit Artifact Passing Between Workflows

| Field | Value |
|---|---|
| **Test ID** | QA-LITOP-002 |
| **Source Requirement** | Literal-operability §9.2 |
| **Source Artifact** | `qa-to-red-specification.md` §9.2 |
| **Scenario** | `deploy-frontend.yml` is inspected for any step that assumes `ci.yml` output artifacts are available without explicit `needs:` declaration |
| **Expected Fail Condition** | `deploy-frontend.yml` references `${{ needs.ci.outputs.* }}` or environment variables produced by `ci.yml` without declaring `needs: [ci]` in the workflow trigger |
| **Expected Pass Condition** | Cross-workflow artifact dependencies are explicit; no step assumes a prior workflow's output is available without a declared dependency chain |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (workflow dependency scan) |

---

### QA-LITOP-003 — `db-migrate.yml` Has No Push or Pull_Request Trigger

| Field | Value |
|---|---|
| **Test ID** | QA-LITOP-003 |
| **Source Requirement** | Literal-operability §9.3, DES-005 |
| **Source Artifact** | `qa-to-red-specification.md` §9.3 |
| **Scenario** | `db-migrate.yml` trigger block is inspected for any `push` or `pull_request` event |
| **Expected Fail Condition** | `db-migrate.yml` contains `on: push` or `on: pull_request` in addition to (or instead of) `workflow_dispatch` |
| **Expected Pass Condition** | `db-migrate.yml` `on:` block contains only `workflow_dispatch`; no `push`, `pull_request`, or `schedule` trigger exists |
| **Severity** | CRITICAL |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (workflow YAML trigger check) |

---

### QA-LITOP-004 — Environment Names are Consistent and Exact

| Field | Value |
|---|---|
| **Test ID** | QA-LITOP-004 |
| **Source Requirement** | Literal-operability §9.4, DES-007 |
| **Source Artifact** | `qa-to-red-specification.md` §9.4 |
| **Scenario** | All workflow files are inspected for environment name declarations |
| **Expected Fail Condition** | Any production-targeting step uses `environment: prod`, `environment: live`, or any name other than `production` |
| **Expected Pass Condition** | All production-targeting steps use `environment: production` (exact string); staging steps use a distinct environment name |
| **Severity** | HIGH |
| **Blocker** | YES |
| **Required Evidence Type** | static-analysis (workflow environment name scan) |

---

### QA-LITOP-005 — Workflow Step `name:` Fields Do Not Contradict DES

| Field | Value |
|---|---|
| **Test ID** | QA-LITOP-005 |
| **Source Requirement** | Literal-operability §9.5 |
| **Source Artifact** | `qa-to-red-specification.md` §9.5 |
| **Scenario** | Workflow step `name:` fields are reviewed for contradictions with DES behavior descriptions |
| **Expected Fail Condition** | A step `name:` field implies a behavior inconsistent with DES (e.g., a step named "Run database migration" in `deploy-frontend.yml`) |
| **Expected Pass Condition** | All workflow step names are consistent with the behavior described in DES-001 through DES-008; no misleading step names |
| **Severity** | MEDIUM |
| **Blocker** | NO |
| **Required Evidence Type** | static-analysis (manual review of step name fields) |

---

## Catalog Summary

| Family | Test IDs | Count | CRITICAL | HIGH | MEDIUM | LOW | BLOCKER |
|---|---|---|---|---|---|---|---|
| QA-ARCH (Cross-System Boundary) | QA-ARCH-001 to QA-ARCH-006 | 6 | 4 | 2 | 0 | 0 | 6 |
| QA-ARC (ARC Domain) | QA-ARC-001 to QA-ARC-008 | 8 | 1 | 7 | 0 | 0 | 8 |
| QA-QUOTA (Quota Management) | QA-QUOTA-001 to QA-QUOTA-008 | 8 | 0 | 7 | 1 | 0 | 7 |
| QA-STATE (State Ownership) | QA-STATE-001 to QA-STATE-005 | 5 | 3 | 2 | 0 | 0 | 5 |
| QA-AUDIT (Audit/Provenance) | QA-AUDIT-001 to QA-AUDIT-006 | 6 | 4 | 2 | 0 | 0 | 6 |
| QA-AUTH (Trust/Authority) | QA-AUTH-001 to QA-AUTH-006 | 6 | 4 | 2 | 0 | 0 | 6 |
| QA-DEGRADE (Degraded Mode) | QA-DEGRADE-001 to QA-DEGRADE-008 | 8 | 1 | 7 | 0 | 0 | 8 |
| QA-ALERT (Alert Delivery) | QA-ALERT-001 to QA-ALERT-005 | 5 | 0 | 4 | 1 | 0 | 4 |
| QA-SESSION (Session Restore) | QA-SESSION-001 to QA-SESSION-003 | 3 | 0 | 3 | 0 | 0 | 3 |
| QA-RT (Real-Time) | QA-RT-001 to QA-RT-004 | 4 | 0 | 3 | 1 | 0 | 3 |
| QA-CONFIG (Configuration Validation) | QA-CONFIG-001 to QA-CONFIG-003 | 3 | 0 | 3 | 0 | 0 | 3 |
| QA-SCHED (Background Scheduler) | QA-SCHED-001 to QA-SCHED-003 | 3 | 0 | 3 | 0 | 0 | 3 |
| QA-DES001 (Surface Ownership) | QA-DES001-001 to QA-DES001-002 | 2 | 0 | 2 | 0 | 0 | 2 |
| QA-DES002/003 (Runner) | QA-DES002-001, QA-DES003-001 | 2 | 0 | 2 | 0 | 0 | 2 |
| QA-DES004 (Migration) | QA-DES004-001 | 1 | 0 | 1 | 0 | 0 | 1 |
| QA-DES005 (Trigger Boundaries) | QA-DES005-001 | 1 | 1 | 0 | 0 | 0 | 1 |
| QA-DES006 (DB Mutation Prohibition) | QA-DES006-001 | 1 | 1 | 0 | 0 | 0 | 1 |
| QA-DES007 (Protected Env) | QA-DES007-001 | 1 | 1 | 0 | 0 | 0 | 1 |
| QA-DES008 (Pre-Flight Fail-Safe) | QA-DES008-001 | 1 | 0 | 1 | 0 | 0 | 1 |
| QA-LITOP (Literal Operability) | QA-LITOP-001 to QA-LITOP-005 | 5 | 1 | 3 | 1 | 0 | 4 |
| **TOTAL** | | **79** | **21** | **54** | **4** | **0** | **75** |

> **Note**: This catalog presents representative test cases for each coverage family. Additional test cases will be defined by qa-builder when implementing the full test suite in Stage 12. The test IDs defined here are the minimum required set. Stage 12 qa-builder may add additional tests within each family but may not remove or skip any test case listed here without a CS2-approved deferral.

---

*AMC Red Test Catalog v1.0 — 2026-04-27 — governing delivery issue: app_management_centre#1141 — CS2 authorization: app_management_centre#1141*

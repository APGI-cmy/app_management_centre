# Wave 3 Implementation Plan

**Document Type:** Implementation Plan (Wave 3)  
**Authority:** BUILD_PHILOSOPHY.md, BL-024, BL-025, BL-026, Execution Bootstrap Protocol v2.0.0+, QA_CATALOG_ALIGNMENT_GATE_SPEC.md  
**Date:** 2026-01-12  
**Status:** ✅ READY FOR EXECUTION (post-CWT PASS)

---

## 1) Wave 3 Scope & Objectives
1. **Runtime Observability & Auditability:** Full-stack telemetry with tenant isolation, drilldown, and governance dashboards.  
2. **Governance Enforcement Expansion:** Harden BL-026 deprecation gate + Execution Bootstrap Protocol proofs for every handover.  
3. **Resilience & Performance:** Strengthen circuit breakers, backoff, and performance envelopes for production load.  
4. **User Experience & Reporting:** Enhanced UI governance dashboards (drilldown, filtering, realtime notifications) with zero ambiguity.

---

## 2) Deliverables
- Observability baseline (traces, metrics, logs) with organisation_id everywhere.  
- BL-026 scanner + Bootstrap v2.0.0+ proofing embedded in every builder workflow.  
- Enhanced governance dashboard (drilldown, filters, realtime notifications, alerts).  
- Resilience/performance tuning playbooks codified and validated.  
- CST-2 execution mid-wave; CWT-2 execution at wave completion.

---

## 3) Subwave Breakdown

| Subwave | Title | Builder | Scope | Dependencies | CST? |
| --- | --- | --- | --- | --- | --- |
| 3.1 | Runtime Telemetry & Audit Trail Hardening | integration-builder + qa-builder | End-to-end traces, metrics, audit trail with tenant isolation; alert wiring | Wave 2 artifacts | No |
| 3.2 | Deprecation Gate + Bootstrap Enforcement | api-builder + qa-builder | BL-026 scanner integration, Bootstrap v2.0.0+ proofs, prehandover automation | 3.1 | No |
| 3.3 | Governance Dashboard V2 (Drilldown/Filter/Realtime) | ui-builder | UI drilldown, multi-criteria filtering, realtime notifications, evidence links | 3.2 | **Yes (CST-2)** |
| 3.4 | Resilience & Failure Mode Expansion | integration-builder | Circuit breaker tuning, backoff policies, conflict resolution guardrails | 3.3 | No |
| 3.5 | Performance & Scalability Validation | schema-builder + integration-builder | Load testing, query optimization, caching, resource limits | 3.4 | No |
| 3.6 | Wave 3 CWT & Production Readiness | qa-builder + integration-builder | Full regression + cross-module CWT-2, readiness declaration | 3.5 | **No (CWT-2)** |

---

## 4) Governance Integration
- **BL-024 (Tier-1 immutables):** Zero test debt, zero warnings, tenant isolation, architecture freeze before execution; enforced in every subwave.  
- **BL-025 (CST/CWT):** CST-2 after Subwave 3.3; CWT-2 after Subwave 3.6. Checklists required in PREHANDOVER_PROOF.  
- **BL-026 (Deprecation Gate):** Scanner must run locally per subwave; output attached to PREHANDOVER_PROOF; no deprecated APIs.  
- **Execution Bootstrap Protocol:** 7-step proof required for each handover (local run logs, UTC timestamps, organisation_id).  
- **QA Catalog Alignment:** Subwave scopes must map to QA catalog IDs; no unmapped work enters execution.

---

## 5) Failure Prevention Mapping (Wave 2 ➜ Wave 3)
- **Threading deadlock/recursion (2.9):** Apply concurrency checklist in 3.1, 3.4; watchdog alerts on recursion; CST-2 includes deadlock detection.  
- **Naming collision (2.10):** Reserved-name lint in 3.2; design review gate for enums/classes.  
- **Bootstrap violation (PR #546):** Bootstrap self-check + BL-026 scanner mandatory in 3.2 onward; proof attached before handover.

---

## 6) Builder Issue Drafts (Zero Guesswork)

> These drafts are ready for GitHub Issue creation. Copy each block verbatim.

### Issue: Wave 3.1 — Runtime Telemetry & Audit Trail Hardening
- **Scope (In):** Add end-to-end traces (UI→API→Backend→Governance), metrics, audit logs with `organisation_id`; alert routing for SLA breaches.  
- **Scope (Out):** UI feature changes, new business logic.  
- **Architecture Reference:** `FM_ARCHITECTURE_SPEC_V2_WIRING_COMPLETE.md` telemetry sections; reuse existing orchestrator spans.  
- **Dependencies:** Wave 2 telemetry baseline; none from Wave 3.  
- **Assignment:** integration-builder (lead), qa-builder (evidence).  
- **Success Criteria:** 100% flows emit trace + audit; P95 latency logged; alert routes configured; tests for audit completeness.  
- **Governance Constraints:** BL-024 Tier-1, BL-026 scan output attached, Bootstrap proof (UTC timestamps, org_id).  
- **Lessons Applied:** Threading checklist; telemetry completeness guard; no deprecated APIs.  
- **CST/CWT:** Not a CST; results feed CST-2 readiness.

### Issue: Wave 3.2 — Deprecation Gate + Bootstrap Enforcement
- **Scope (In):** Integrate BL-026 scanner into local workflow; enforce Execution Bootstrap Protocol v2.0.0+ prehandover; add reserved-name lint.  
- **Scope (Out):** UI/dashboard work, resilience tuning.  
- **Architecture Reference:** `governance/specs/IN_BETWEEN_WAVE_RECONCILIATION_SPEC.md` (Bootstrap steps), BL-026 spec.  
- **Dependencies:** Completion of telemetry plumbing (3.1).  
- **Assignment:** api-builder (implementation), qa-builder (proof validation).  
- **Success Criteria:** Scanner blocks deprecated APIs; prehandover bundle auto-generated; naming lint enforced; tests prove failures are caught.  
- **Governance Constraints:** BL-024/025/026, Bootstrap proof required, zero warnings.  
- **Lessons Applied:** Prevent PR #546 recurrence; reserved enum/name collision guard.  
- **CST/CWT:** Not CST; must provide inputs for CST-2.

### Issue: Wave 3.3 — Governance Dashboard V2 (Drilldown/Filter/Realtime)
- **Scope (In):** Implement drilldown levels, advanced filtering, realtime notifications, evidence linking; ensure tenant isolation and auditability.  
- **Scope (Out):** Backend data model changes outside dashboard needs.  
- **Architecture Reference:** `ui/dashboard` components; governance dashboards spec; reuse telemetry from 3.1.  
- **Dependencies:** 3.2 enforcement tooling ready.  
- **Assignment:** ui-builder.  
- **Success Criteria:** All QA-361–QA-375 and QA-401–QA-415 behaviors green; realtime updates captured with timestamps; zero warnings.  
- **Governance Constraints:** BL-024 (Tier-1 immutable), BL-026 scan, Bootstrap proof.  
- **Lessons Applied:** Thread-safety for realtime handlers; evidence links for audit; conflict resolution playbook for concurrent updates.  
- **CST/CWT:** **CST-2 executes after this subwave**; provide CST evidence and summary.

### Issue: Wave 3.4 — Resilience & Failure Mode Expansion
- **Scope (In):** Tune circuit breakers, backoff policies, conflict resolution guards; add escalation hooks; expand failure analytics.  
- **Scope (Out):** UI surface changes, new telemetry pipelines.  
- **Architecture Reference:** `foreman/runtime` resilience modules; failure modes specs from Wave 2.11/2.12.  
- **Dependencies:** CST-2 PASS, dashboard behaviors stable (3.3).  
- **Assignment:** integration-builder.  
- **Success Criteria:** Breakers calibrated; backoff policies codified; conflict resolution tests pass; alerts emitted on breaker trip.  
- **Governance Constraints:** BL-024/025/026; Bootstrap proof; deadlock checklist applied.  
- **Lessons Applied:** Deadlock prevention; escalation routing; no deprecated patterns.

### Issue: Wave 3.5 — Performance & Scalability Validation
- **Scope (In):** Load tests, query optimization, caching/invalidation, resource limit enforcement; performance dashboards update.  
- **Scope (Out):** New features or flows beyond optimization targets.  
- **Architecture Reference:** `foreman/analytics` performance modules; system optimization specs from Wave 2.12+.  
- **Dependencies:** 3.4 resilience updates.  
- **Assignment:** schema-builder (data/query), integration-builder (load harness).  
- **Success Criteria:** P95 < 180ms, P99 < 230ms; throughput ≥ Wave 2 benchmark; cache hit/miss tracked; zero warnings.  
- **Governance Constraints:** BL-024/026; Bootstrap proof with load-test logs; tenant isolation validated under load.  
- **Lessons Applied:** Backoff + breaker thresholds preserved; telemetry completeness.

### Issue: Wave 3.6 — Wave 3 CWT & Production Readiness
- **Scope (In):** Execute CWT-2 (full regression + integration scenarios), finalize readiness declaration, ensure dashboards reflect live state.  
- **Scope (Out):** Net-new features.  
- **Architecture Reference:** `CWT_WAVE_2_TO_3_EXECUTION_REPORT.md` pattern; governance dashboards.  
- **Dependencies:** All prior subwaves complete.  
- **Assignment:** qa-builder (lead), integration-builder (support).  
- **Success Criteria:** 100% GREEN regression, zero warnings, BL-026 violations = 0, readiness declaration issued.  
- **Governance Constraints:** BL-024/025/026; Bootstrap proof; CS2 authorization required.  
- **Lessons Applied:** Apply all prior preventions; failure analytics verify no recurrence.

---

## 7) CST/CWT Schedule
- **CST-2:** After Subwave 3.3 (dashboard completion); scope = 30–50% of Wave 3; includes concurrency + governance checks.  
- **CWT-2:** After Subwave 3.6; full regression + integration scenarios; gate to production readiness.

---

## 8) Sign-Off
- **Prepared By:** Maturion Foreman (FM)  
- **Date:** 2026-01-12  
- **Statement:** Wave 3 plan is architecture-aligned, governance-compliant, and ready for execution with CST/CWT checkpoints defined.

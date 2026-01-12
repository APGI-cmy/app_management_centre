# Wave 2 Lessons Learned — Consolidated (IBWR)

**Document Type:** Lessons Learned Consolidation (IBWR Phase)  
**Wave:** 2.0 (14/14 subwaves complete)  
**Authority:** IN_BETWEEN_WAVE_RECONCILIATION_SPEC.md, BL-024, BL-025, BL-026, Execution Bootstrap Protocol v2.0.0+  
**Date:** 2026-01-12  
**Status:** ✅ Consolidated

---

## 1) Governance Changes Captured

| Governance Change | Source (Wave 2) | Learning | Wave 3 Application |
| --- | --- | --- | --- |
| **BL-024 Constitutional Sandbox Pattern** | Subwave 2.11 collaborative execution | Clarified Tier-1 (immutable) vs Tier-2 (procedural) boundaries; builders exercise judgment only within Tier-2 | Reinforce Tier-1 guardrails in all Wave 3 issues; architecture freeze + tenant isolation required in every subwave |
| **BL-025 CST/CWT Pattern** | Wave 2 progress checkpoint | CST mid-wave, CWT post-wave; CWT required for wave completion | CST-2 scheduled after Subwave 3.3; CWT-2 at Wave 3 completion (see WAVE_3_IMPLEMENTATION_PLAN.md) |
| **BL-026 Automated Deprecation Detection Gate** | Subwave 2.13 E2E | Zero deprecated APIs; automated scanning mandatory | Enforce BL-026 scanner in prehandover for every builder issue; fail-fast on deprecated imports |
| **Execution Bootstrap Protocol v2.0.0+** | Post-Wave 2 rollout | 7-step verification + PREHANDOVER_PROOF required before handover; no CI-only validation | Every Wave 3 subwave must attach PREHANDOVER_PROOF with local run logs, timestamps (UTC), and isolation keys |

---

## 2) Process Improvements (Wave 2)

| Subwave | Improvement | How It Carries Into Wave 3 |
| --- | --- | --- |
| 2.8 (QA Infrastructure) | Standardized watchdog + event-bus health checks with dependency graphs | Reuse watchdog baselines for all Wave 3 components; require heartbeat + dependency manifests per subwave |
| 2.9 (Deep Integration Phase 1) | Threading discipline, deadlock prevention playbook | Apply same concurrency checklist to Wave 3 orchestration and dashboards; require thread-safety evidence |
| 2.10 (Deep Integration Phase 2) | Conflict resolution strategies (4 patterns) formalized | Mandate conflict strategy selection in design notes for every data flow in Wave 3 |
| 2.11 (Failure Mode Implementation) | Collaborative builder coordination + circuit breaker defaults | Keep coordinated escalation paths and default breaker thresholds in Wave 3 resilience stories |
| 2.12 (Failure Resilience) | Retry/backoff and recovery monitoring standardized | Reuse backoff parameters and recovery telemetry; add regression guardrails in CST-2 |
| 2.13 (E2E Orchestration Phase 1) | Orchestrator + telemetry stitched across modules | Preserve full-span tracing in Wave 3 additions; no orphaned spans permitted |
| 2.14 (E2E Orchestration Phase 2) | Production readiness + monitoring dashboards hardened | Keep dashboards as single source of truth; require alert thresholds before merge |

---

## 3) Failure Learnings (RCA ➜ Prevention)

| Failure | Root Cause | Fix Implemented in Wave 2 | Wave 3 Prevention |
| --- | --- | --- | --- |
| Subwave 2.9: Threading deadlock + infinite recursion | Event bus threading model allowed recursion | Added thread-safe event handling + recursion detection | Concurrency checklist mandatory; CST-2 to include deadlock detection; watchdog alerts on recursion signatures |
| Subwave 2.10: Pytest naming collision (`TestStatus`) | Enum name collision with pytest auto-discovery | Renamed enum; adjusted fixtures | Naming convention check in design review; reserved names list in builder issues; lint gate for conflicting enums |
| PR #546: Execution Bootstrap Protocol violation | Validation script used deprecated APIs | Replaced with modern patterns; added self-check | Enforce BL-026 scanner + Bootstrap self-check in every prehandover; reject handover without proof bundle |

**Verification:** Each prevention item is mapped to a Wave 3 subwave owner in `WAVE_3_IMPLEMENTATION_PLAN.md` and to CST-2 acceptance criteria.

---

## 4) Constitutional Principle: “We only make mistakes once.”

- All Wave 2 failures have explicit Wave 3 preventions (Section 3).  
- BL-024 Tier-1 rules remain immutable; no overrides permitted.  
- Any recurrence triggers TARP (Second-Time Failure Prohibition) escalation.

---

## 5) Ready-to-Apply Checks for Wave 3

1. **Threading Discipline:** Apply deadlock/recursion checklist to all orchestrator and runtime listeners.  
2. **Naming Guardrails:** Validate enums/classes against reserved list before merge.  
3. **Deprecation Gate:** Run BL-026 scanner locally + attach output to PREHANDOVER_PROOF.  
4. **Bootstrap Proofs:** Capture UTC timestamps, organisation_id, local run logs for every handover.  
5. **Telemetry Completeness:** Ensure end-to-end traces with no gaps for new flows.  
6. **Dashboard Alerts:** Define thresholds and alert routes before enabling new modules.  
7. **CST/CWT Placement:** CST-2 after Subwave 3.3; CWT-2 after Wave 3 completion (see CWT and plan files).

---

## 6) Sign-Off

- **Prepared By:** Maturion Foreman (FM)  
- **Date:** 2026-01-12  
- **Statement:** Wave 2 learnings, governance updates, and RCAs are consolidated and mapped to Wave 3 preventions. No residual ambiguities remain.

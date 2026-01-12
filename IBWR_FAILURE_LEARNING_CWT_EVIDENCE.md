# IBWR Failure Learning — CWT Evidence (Wave 2 ➜ Wave 3)

**Failure:** Claimed CWT execution (Wave 2 ➜ Wave 3) without providing evidence artifacts.  
**Authority:** Execution Bootstrap Protocol v2.0.0+, BL-025 CST/CWT Pattern, IBWR process.  
**Status:** Resolved via clarification (Type B: Execution Planning); execution deferred to Wave 3.1 with PREHANDOVER_PROOF requirement.

---

## 1) What was the failure?
- Report stated CWT execution (full regression, integrations, performance) but no logs, artifacts, or PREHANDOVER_PROOF were provided.

## 2) Why did it happen?
- Assumed planning validation was sufficient and mislabeled it as execution.
- Missed Bootstrap Protocol evidence requirement for IBWR CWT claims.

## 3) Governance violation
- Execution Bootstrap Protocol v2.0.0+ requires local execution evidence and PREHANDOVER_PROOF before claiming completion.
- Violated “CI is confirmation, not diagnostic” by asserting GREEN without proof.

## 4) Immediate fix
- Reclassified CWT report as **Type B: Execution Planning** with deferral to Wave 3.1.
- Committed to attach full PREHANDOVER_PROOF (logs, hashes, deprecation scan, telemetry) after Wave 3.1 execution.

## 5) Prevention for future IBWR executions
- Do not claim CWT execution without attached evidence package.
- If infrastructure is missing, label as planning-only, document deferral rationale and timeline, and set the next milestone.
- Add IBWR CWT evidence verification to prehandovers and builder issue templates.

---

## Process Improvement Proposal — IBWR CWT Execution Requirements Clarification

- **Problem:** IBWR spec doesn’t distinguish between planning-only and executed CWT, nor specify deferral evidence requirements.  
- **Proposal:** Add to `governance/specs/IN_BETWEEN_WAVE_RECONCILIATION_SPEC.md`:
  - Define CWT Type A (Executed) vs Type B (Planning/Deferred).  
  - Evidence: Type A requires logs/artifacts/PREHANDOVER_PROOF; Type B requires deferral rationale, readiness criteria, and timeline.  
  - Gate decisions must state whether based on execution or planning.  
- **Target milestone:** Incorporate clarification during Wave 3 governance touchpoint (align with CST-2 readiness).

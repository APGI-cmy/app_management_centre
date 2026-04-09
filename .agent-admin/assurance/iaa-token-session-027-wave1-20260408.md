# IAA ASSURANCE-TOKEN — Session 027 — 2026-04-08

## Token

```
═══════════════════════════════════════
ASSURANCE-TOKEN
PR: copilot/layer-down-propagate-governance-changes-again
    governance-liaison-amc session-002-20260408 (RE-AUDIT2 — OVL-LA-003 fix)
All 20 checks PASS. Merge gate parity: PASS.
Merge permitted (subject to CS2 approval).
Token reference: IAA-session-027-wave1-20260408-PASS
Adoption phase: PHASE_B_BLOCKING — hard gate
═══════════════════════════════════════
```

## Session Metadata

| Field | Value |
|-------|-------|
| session_id | IAA-027 |
| date | 2026-04-08 |
| pr_reviewed | branch copilot/layer-down-propagate-governance-changes-again — governance-liaison-amc session-002-20260408 — RE-AUDIT2 |
| invoking_agent | CS2 (direct re-invocation) |
| producing_agent | governance-liaison-amc-agent |
| producing_agent_class | liaison |
| pr_category | CANON_GOVERNANCE + LIAISON_ADMIN |
| checks_executed | 20 |
| checks_passed | 20 |
| checks_failed | 0 |
| merge_gate_parity_result | PASS |
| verdict | ASSURANCE-TOKEN |
| token_reference | IAA-session-027-wave1-20260408-PASS |
| adoption_phase_at_time_of_verdict | PHASE_B_BLOCKING |
| prior_iaa_verdicts | IAA-026-initial (REJECTION-PACKAGE, 7 failures), IAA-026-reaudit (REJECTION-PACKAGE, 1 failure: OVL-LA-003) |

## OVL-LA-003 Resolution Confirmed

- ripple-run-24131833105.json: NOT present in ripple-inbox ✅
- ripple-run-24131833105.json: PRESENT in ripple-archive (blob 36d3cc03c7b5573623092c203744d38e6589ec2d) ✅
- status: "archived" ✅
- archived_at: "2026-04-08T12:28:58Z" ✅
- canonical_commit: "b54d57b5864a4df67f5bc44323ebde3807192c39" ✅
- changed_paths: populated (4 paths) ✅
- processing_notes: present ✅
- Fix committed at HEAD cd17767 ✅

## Authority

Merge authority: CS2 ONLY (@APGI-cmy).
IAA does not merge. IAA issues verdict only.

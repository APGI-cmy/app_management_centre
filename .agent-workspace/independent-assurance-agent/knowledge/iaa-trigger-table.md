# IAA Trigger Table

**Agent**: independent-assurance-agent
**Version**: 2.2.0
**Status**: ACTIVE
**Last Updated**: 2026-04-07
**Authority**: CS2 (Johan Ras / @APGI-cmy)

---

## Purpose

This table defines when IAA activates and when it is exempt for a given PR.
IAA uses this table in Phase 2 Step 2.3 for PR category classification.

**AMBIGUITY RULE**: If classification is unclear, IAA IS required (FAIL-ONLY-ONCE A-003).
Default: MANDATORY INVOCATION when in doubt.

---

## Trigger Table

| PR Category | IAA Required? | Trigger Condition | Notes |
|-------------|---------------|------------------|-------|
| AGENT_CONTRACT | YES — MANDATORY | Any `.github/agents/*.md` file created or modified; any `governance/agents/` or `governance/contracts/` file created or modified; any `*-agent-contract.md` file | All agent classes. No exceptions. FAIL-ONLY-ONCE A-002. This includes Foreman, Builder, Overseer, Specialist, and Assurance (IAA self-review → escalate to CS2). |
| CANON_GOVERNANCE | YES — MANDATORY | Any `governance/canon/` file created or modified; any `governance/CANON_INVENTORY.json` update; any file matching `*ARCHITECTURE*.md` or `*STRATEGY*.md` in governance | Includes CANON_INVENTORY.json updates. Version bump must be present. |
| CI_WORKFLOW | YES — MANDATORY | Any `.github/workflows/` file created or modified | Includes merge gate workflow, ripple sync workflow, and all governance automation workflows. |
| AAWP_MAT | YES — MANDATORY | PR labelled `aawp-deliverable` or `mat-deliverable`; files match AAWP/MAT path patterns (`modules/mat/`, `packages/ai-centre/`, AAWP architecture files) | Evidence bundle completeness required. |
| AGENT_INTEGRITY | YES — MANDATORY | Any `governance/quality/agent-integrity/` file created or modified | CS2-only update authority. Any non-CS2 modification → auto-REJECTION-PACKAGE. |
| KNOWLEDGE_GOVERNANCE | YES — MANDATORY | Any `.agent-workspace/*/knowledge/` file created or modified; any Tier 2 knowledge index, overlay, trigger table, checklist, or FAIL-ONLY-ONCE registry updated | Covers all IAA and agent Tier 2 knowledge patches. Evidence bundle + PREHANDOVER ceremony required (FAIL-ONLY-ONCE A-015). |
| PRE_BUILD_STAGE | YES — MANDATORY | Any pre-build stage artifact created or modified: App Description, UX Workflow & Wiring Spec, FRS, TRS, Architecture, QA-to-Red, PBFAG gate report, Implementation Plan, Builder Checklist, IAA Pre-Brief, Builder Appointment; any file under `modules/*/pre-build/`, `docs/governance/*_DESCRIPTION.md`, `docs/governance/*_FRS*.md`, `docs/governance/*_TRS*.md`, `docs/governance/*_ARCHITECTURE*.md`; any wave tagged `pre-build-stage` | Pre-build stage sequence compliance required per `PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0. IAA applies PRE_BUILD_STAGE overlay (OVL-PBG-010–016). Stage skip or reorder without CS2 approval = REJECTION-PACKAGE. |
| LIAISON_ADMIN | YES — MANDATORY | Any `.agent-workspace/governance-liaison-amc/` file created or modified; any layer-down execution report, ripple inbox entry, drift detection report, or sync state update under `.agent-admin/governance/`; any wave delivering governance liaison administration artifacts | Governance liaison admin operations (layer-down, ripple processing, drift correction) require IAA assurance. Evidence bundle + PREHANDOVER ceremony required. |
| MIXED | YES — MANDATORY | PR contains both triggering and non-triggering artifacts | Ambiguity rule applies. Any triggering artifact activates IAA for the whole PR. |
| EXEMPT | NO — if unambiguously non-triggering | Pure doc-only changes outside governance/canon; parking station updates (labelled `parking-station`); session memory files only; README changes with no agent/governance/CI content; admin/housekeeping (labelled `admin` or `housekeeping`) | Must be unambiguously non-triggering. If any doubt → apply AMBIGUITY RULE. |
| AMBIGUOUS | YES — MANDATORY | Classification unclear; mixed signals; trigger table file is missing | FAIL-ONLY-ONCE A-003: ambiguity resolves to mandatory invocation. |

---

## Class-Based Exemption Prohibition

No agent class is exempt from the AGENT_CONTRACT trigger. Specifically:
- **Foreman class**: NOT exempt. Double-layer QA is constitutional. Authority: maturion-isms#523, #528, #531.
- **Builder class**: NOT exempt.
- **Overseer class**: NOT exempt (CodexAdvisor, maturion-agent).
- **Specialist class**: NOT exempt.
- **Assurance class (IAA itself)**: IAA cannot self-review. If IAA contract changes → escalate to CS2.

Any agent claiming class exemption → REJECTION-PACKAGE citing FAIL-ONLY-ONCE A-002.

---

## Classification Decision Flow

```
1. Does PR contain any .github/agents/ or governance/agents/ changes?
   → YES: Category = AGENT_CONTRACT. IAA = MANDATORY.

2. Does PR contain any governance/canon/ or CANON_INVENTORY.json changes?
   → YES: Category = CANON_GOVERNANCE. IAA = MANDATORY.

3. Does PR contain any .github/workflows/ changes?
   → YES: Category = CI_WORKFLOW. IAA = MANDATORY.

4. Does PR contain AAWP/MAT deliverable artifacts?
   → YES: Category = AAWP_MAT. IAA = MANDATORY.

5. Does PR contain governance/quality/agent-integrity/ changes?
   → YES: Category = AGENT_INTEGRITY. IAA = MANDATORY.

6. Does PR contain any .agent-workspace/*/knowledge/ file changes?
   → YES: Category = KNOWLEDGE_GOVERNANCE. IAA = MANDATORY.

7. Does PR contain any pre-build stage artifacts (App Description, UX Workflow & Wiring Spec,
   FRS, TRS, Architecture, QA-to-Red suite, PBFAG gate report, Implementation Plan,
   Builder Checklist, IAA Pre-Brief artifact, Builder Appointment) or is the wave tagged
   `pre-build-stage`?
   → YES: Category = PRE_BUILD_STAGE. IAA = MANDATORY.

8. Does PR contain any governance liaison admin artifacts (.agent-workspace/governance-liaison-amc/,
   layer-down reports, ripple inbox entries, sync state updates)?
   → YES: Category = LIAISON_ADMIN. IAA = MANDATORY.

9. Is the PR clearly and unambiguously doc-only, parking-station, or admin?
   → YES: Category = EXEMPT. IAA = NOT REQUIRED.
   → UNCERTAIN: Apply AMBIGUITY RULE → Category = AMBIGUOUS. IAA = MANDATORY.
```

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-02-25 | Initial STUB (placeholder from canon) |
| 2.0.0 | 2026-02-28 | Fully populated from INDEPENDENT_ASSURANCE_AGENT_CANON.md; AGENT_INTEGRITY category added; classification decision flow added; STUB status removed |
| 2.1.0 | 2026-03-02 | KNOWLEDGE_GOVERNANCE trigger category added; classification decision flow updated with step 6 for knowledge governance path (maturion-isms#IAA-TIER2) |
| 2.2.0 | 2026-04-07 | PRE_BUILD_STAGE trigger category added — enforces 12-stage pre-build sequence compliance per `PRE_BUILD_STAGE_MODEL_CANON.md` v1.0.0 (ISMS PS-E); LIAISON_ADMIN trigger category added — governance liaison admin operations require IAA assurance (ISMS PS-F); classification decision flow updated with steps 7 and 8 |

---

**Authority**: CS2 (Johan Ras) | **Living Agent System**: v6.2.0

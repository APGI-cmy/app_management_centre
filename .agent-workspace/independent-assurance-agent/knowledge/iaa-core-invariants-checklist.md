# IAA Core Invariants Checklist — IAA-Retained Subset

**Agent**: independent-assurance-agent
**Version**: 4.0.0
**Status**: ACTIVE
**Last Updated**: 2026-04-14
**Authority**: CS2 (Johan Ras / @APGI-cmy)

---

## ⚠️ IAA-RETAINED SUBSET — 90/10 RESTRUCTURE (v4.0.0)

**CORE-001 through CORE-019 and CORE-022 through CORE-024 have moved to CI.**
- CORE-001–012 (YAML/format checks) → `agent-contract-format-gate.yml`
- CORE-013, CORE-015, CORE-016, CORE-018, CORE-019 (artifact existence) → `preflight-evidence-gate.yml`
- CERT-001–004 → `preflight-evidence-gate.yml`
- HFMC-01–06 → `preflight-evidence-gate.yml`

Reference: `.agent-workspace/independent-assurance-agent/knowledge/iaa-high-frequency-checks.md`

**This file retains only the two checks that require IAA judgment (not mechanical CI execution).**

---

## ⚠️ ORIENTATION MANDATE — READ BEFORE APPLYING THIS CHECKLIST (CS2 Directive)

**These checks are the 10% ceremony admin layer.** They verify existence and format only.

IAA's primary obligation (90%) is substance:
- For BUILD PRs: does the delivered code actually work, is it safe, and will it produce a functional result first time?
- For GOVERNANCE PRs: does the change align with strategy, avoid contradictions, and close gaps rather than create them?

**Do NOT spend more than 10% of session effort on the checks in this file.**

---

## Purpose

This checklist defines the IAA-retained invariant checks: those requiring judgment rather than mechanical verification. Applied to every qualifying IAA invocation regardless of PR category.

---

## IAA-Retained Core Invariants

| Check ID | Check Name | Description | Applies To | Failure Action |
|----------|-----------|-------------|------------|----------------|
| CORE-020 | Zero partial pass rule | Any core or overlay check that cannot be verified due to missing, blank, or unverifiable evidence = REJECTION-PACKAGE for that check. No assumed passes. Absence of evidence = failing check. A PR with partial evidence must not receive ASSURANCE-TOKEN under any category or class. | ALL | REJECTION-PACKAGE |
| CORE-021 | Zero-severity-tolerance | Any finding identified during the assurance review — regardless of perceived severity, wording, or delivery size — MUST produce REJECTION-PACKAGE. Prohibited: using terms "minor", "trivial", "cosmetic", "small", "negligible", "low-impact", "soft-pass", or "acceptable" to characterise a finding as passable. The only valid exception is an explicit written CS2 waiver quoted verbatim in the output. See `IAA_ZERO_SEVERITY_TOLERANCE.md` for full operational guidance. | ALL | REJECTION-PACKAGE |

---

## Applying the Checklist

For each check:
1. Locate the relevant artifact(s) in the PR bundle
2. Apply the check description as stated
3. Record PASS or FAIL with specific evidence
4. Any FAIL → REJECTION-PACKAGE (no partial passes)

**AMBIGUITY RULE**: If uncertain whether a check applies to this PR → apply it.

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-02-25 | Initial STUB |
| 2.0.0 | 2026-02-28 | Fully populated; CORE-001 to CORE-019 |
| 2.4.0 | 2026-03-02 | CORE-021 added: Zero-Severity-Tolerance |
| 2.5.0 | 2026-03-03 | CORE-022 added: secret_env_var compliance |
| 2.8.0 | 2026-03-04 | Orientation Mandate added |
| 3.0.0 | 2026-04-07 | CORE-024 added: Pre-build stage sequence compliance |
| 4.0.0 | 2026-04-14 | 90/10 restructure: CORE-001–019, CORE-022–024 moved to CI; only CORE-020 and CORE-021 retained in this file. Reference: iaa-high-frequency-checks.md |

---

**Authority**: CS2 (Johan Ras) | **Living Agent System**: v6.2.0

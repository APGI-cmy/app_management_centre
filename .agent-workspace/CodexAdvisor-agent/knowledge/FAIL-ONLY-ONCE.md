# CodexAdvisor-agent — FAIL-ONLY-ONCE Registry

**Agent**: CodexAdvisor-agent
**Version**: 1.0.0
**Last Updated**: 2026-04-21
**Authority**: CS2 (@APGI-cmy)
**Governance Ref**: AMC Issue #1068, AMC PR #1065

---

## Purpose

This registry records governance failures that CodexAdvisor must never repeat.
Each entry captures a root cause, the permanent rule that prevents recurrence,
and the incident reference.

CodexAdvisor loads this file in Phase 1 Step 1.5 on every session start.

**Every session MUST:**
1. Read this file in full.
2. Self-attest that every A-rule is understood and will be observed.
3. Check the incident log — if any incident has status `OPEN` → HALT immediately.
4. Record attestation in session memory.

---

## Section 1 — Universal A-Rules (Permanent Invariants)

These rules are **absolute** and may never be overridden or relaxed without
explicit CS2 written authorisation.

| Rule ID | Rule | Source |
|---------|------|--------|
| A-001 | Never overwrite an existing agent contract without explicit CS2 authorization. | SELF-MOD-001 / LIVING_AGENT_SYSTEM.md |
| A-002 | Never skip QP gates S1–S12 before writing any agent contract file. | AGCFPP-001 / CodexAdvisor contract Phase 3 |
| A-003 | Never open a PR without a committed PREHANDOVER proof. | EVIDENCE_ARTIFACT_BUNDLE_STANDARD.md |
| A-004 | Never self-approve IAA verdict. IAA invocation is mandatory for all agent contract PRs. | INDEPENDENT_ASSURANCE_AGENT_CANON.md |
| A-005 | Never write IAA token files. IAA writes its own tokens exclusively. | INDEPENDENT_ASSURANCE_AGENT_CANON.md |
| A-006 | Never write a frontmatter scalar exceeding the GitHub custom-agent parser limit (200 chars). | HALT-009 / parser-budget enforcement |
| A-007 | Never embed Tier 2 bulk content in Tier 1 agent contracts. | NO-EMBED-001 |
| A-008 | Never write a target agent file exceeding 30,000 characters. | HALT-004 |
| A-009 | Never treat a QP PASS as a substitute for final IAA PASS before merge-ready state. | NO-MERGEREADY-WITHOUT-IAA-001 |
| A-010 | Never create an operative own-file write path outside an explicit CS2 gate. | NO-OWN-FILE-WRITE-001 / SELF-MOD-001 |

---

## Section 2 — Incident Log

| Incident | Date | Description | Status |
|----------|------|-------------|--------|
| INC-CXA-001 | 2026-04-07 | **OPOJD Violation — session-014**: Job not completed in single session. IAA was invoked before artifacts were committed (ENVIRONMENT_BOOTSTRAP failure, A-021 pattern). IAA issued REJECTION-PACKAGE. Session ended without ASSURANCE-TOKEN and without open PR. OPOJD principle violated. **Root cause**: commit-before-IAA step not enforced in Phase 4. **Corrective action**: (1) All session-014 findings resolved in session-015; (2) CodexAdvisor Phase 4 Step 4.4 now includes explicit pre-invocation commit check per systemic blocker COPILOT-SWE-COMMIT-BEFORE-IAA. | REMEDIATED |

---

## Section 3 — Open Improvement Suggestions

_None at this time._

---

*Authority: CS2 (@APGI-cmy) | CodexAdvisor-agent Tier 2 Knowledge*
*This file is append-only. No entry may be removed.*

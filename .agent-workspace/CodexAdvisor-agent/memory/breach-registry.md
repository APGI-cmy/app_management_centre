# CodexAdvisor-agent — FAIL-ONLY-ONCE Breach Registry

_Append-only. No entry may be removed. Status transitions: OPEN → REMEDIATED | ACCEPTED_RISK (CS2 only)._

## Section 1 — A-Rules (Permanent Standing Rules)

| Rule ID | Rule | Enforcement |
|---|---|---|
| A-001 | Never overwrite an existing agent contract without CS2 authorization | CONSTITUTIONAL |
| A-002 | Never skip QP gates S1–S8 | BLOCKING |
| A-003 | Never open a PR without PREHANDOVER proof | BLOCKING |
| A-004 | Never self-approve IAA verdict | CONSTITUTIONAL |
| A-005 | Never write IAA token files | CONSTITUTIONAL |

## Section 2 — Incident Log

| Incident | Date | Description | Status |
|---|---|---|---|
| INC-CXA-001 | 2026-04-07 | **OPOJD Violation — session-014**: Job not completed in single session. IAA was invoked before artifacts were committed (ENVIRONMENT_BOOTSTRAP failure, A-021 pattern). IAA issued REJECTION-PACKAGE. Session ended without ASSURANCE-TOKEN and without open PR. OPOJD principle violated. **Root cause**: commit-before-IAA step not enforced in Phase 4. **Corrective action**: (1) All session-014 findings resolved in session-015; (2) CodexAdvisor Phase 4 Step 4.4 must include explicit pre-invocation commit check per systemic blocker COPILOT-SWE-COMMIT-BEFORE-IAA. CS2-gated contract change required. | REMEDIATED (findings resolved session-015) |

## Section 3 — Open Improvement Suggestions

_None at this time._

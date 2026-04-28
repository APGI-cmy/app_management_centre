**Status**: CANONICAL | **Version**: 1.0.0 | **Authority**: CS2
**Date**: 2026-04-28
**Canon ID**: EFIA-001
**Issue**: app_management_centre — Umbrella: Upgrade AMC PR handover assurance to ISMS-level evidence-first protected-path scrutiny (Child 2)

> **Amendment Authority**: Only CS2 (Johan Ras / repo owner) may amend this canon.
> Any PR modifying this file without CS2 sign-off is auto-FAIL at the merge gate.

---

# AMC Evidence-First IAA Assurance Canon

## Purpose

This canon defines the **evidence-first assurance requirements** that IAA must enforce for
AMC PR handover. It upgrades AMC IAA so that a PASS requires:

1. An **acceptance-criteria evidence matrix** mapping each acceptance criterion to hard evidence
2. A **build-correctness / architecture-compliance review** before PASS
3. **No evidence-type downgrade** — required evidence types cannot be silently replaced
4. A **diff-first audit** — the PR diff is reviewed independently of declared scope
5. An **agent-claim non-evidence rule** — agent assertions are not evidence
6. An **independent risk challenge** — IAA must independently assess risk, not accept the
   producing agent's risk classification
7. **Expanded blocked verdicts** — explicit rejection triggers for each failure class

This canon builds on and does not replace:
- `INDEPENDENT_ASSURANCE_AGENT_CANON.md`
- `EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` (ECAP-001)
- `PR_HANDOVER_CANONICAL_PACKAGE.md` (PHCP-001)

---

## 1. Evidence-First Principle

### 1.1 Definition

**Evidence-first** means that for every acceptance criterion in a delivery, IAA requires
**hard evidence** of the required type before issuing a PASS. The following hierarchy defines
evidence quality from highest to lowest:

| Tier | Evidence Type | Description |
|------|-------------|-------------|
| E1 | LIVE_RUNTIME | Direct observation of system running in a live environment (e.g., screenshot of running app, live endpoint test) |
| E2 | LIVE_E2E | End-to-end test result from a live or staging environment (e.g., CI test output with green E2E suite) |
| E3 | CI_TEST | Automated test passing in CI (green CI run with test output) |
| E4 | STATIC_ANALYSIS | Code review, linting, schema validation, or static architecture check |
| E5 | AGENT_ATTESTATION | Agent declares that something is true (lowest tier — see §1.3) |

### 1.2 Minimum Evidence Type per Acceptance Criterion Class

Each acceptance criterion carries a **minimum required evidence type**. IAA MUST verify that
the submitted evidence meets or exceeds the minimum for each criterion:

| Acceptance Criterion Class | Minimum Evidence Type | Notes |
|---------------------------|----------------------|-------|
| Functional behaviour (user-facing) | E2 (LIVE_E2E) or E1 (LIVE_RUNTIME) | Cannot be satisfied with E4 or E5 alone |
| Automated test coverage | E3 (CI_TEST) | Green CI run required; not agent claim |
| Architecture compliance | E4 (STATIC_ANALYSIS) with E3 confirmation where automatable | Must reference specific architecture docs |
| Governance document correctness | E4 (STATIC_ANALYSIS) + human review record | IAA's own review constitutes E4 for governance docs |
| CI / workflow correctness | E3 (CI_TEST) — CI run after change | Cannot be satisfied by E5 (agent claim) alone |
| Schema / migration correctness | E3 (CI_TEST) + E4 (STATIC_ANALYSIS) | Both required; neither alone is sufficient |
| Ceremony completeness | E4 (STATIC_ANALYSIS) against canonical checklist | Checklist review counts as E4 |

### 1.3 Agent-Claim Non-Evidence Rule (ACNER)

**Agent attestation (E5) is NOT evidence for acceptance criteria that require E1–E4.**

Specifically:
- "I reviewed the code and it looks correct" — NOT evidence (E5 only)
- "The tests passed in my session" — NOT evidence without a CI run reference (E5 only)
- "The architecture is compliant based on my understanding" — NOT evidence (E5 only)
- A CI run URL with green results — IS evidence (E3)
- A committed test result artifact — IS evidence (E3)
- A diff review with specific line references — IS evidence (E4)

If a submitted handover bundle cites only E5 (agent attestation) for an acceptance criterion
that requires E1–E4, IAA MUST issue a REJECTION-PACKAGE citing EFIA-AGENT-CLAIM (§7).

---

## 2. Acceptance-Criteria Evidence Matrix

### 2.1 Matrix Requirement

Every PR submitted to IAA for a PASS token MUST include an **acceptance-criteria evidence matrix**
embedded in the wave record §3c as a fenced YAML block labelled `ac_evidence_matrix`.

The matrix maps each acceptance criterion from the governing delivery issue to:
- The evidence type submitted
- The evidence artifact location or reference
- Whether the evidence type meets the minimum required type

```yaml
ac_evidence_matrix:
  - criterion: "[Exact acceptance criterion text from governing issue]"
    minimum_evidence_required: "E1 | E2 | E3 | E4"
    evidence_type_submitted: "E1 | E2 | E3 | E4 | E5"
    evidence_reference: "[URL, file path, CI run link, or artifact reference]"
    evidence_meets_minimum: "YES | NO — [reason if NO]"
    iaa_verdict: "ACCEPTED | REJECTED — [reason]"
  - criterion: "[...]"
    ...
ac_evidence_matrix_verdict: "PASS | FAIL — PASS only if all criteria show evidence_meets_minimum: YES"
```

### 2.2 Incomplete Matrix Rejection

If the `ac_evidence_matrix` YAML block is absent from wave record §3c, IAA MUST issue a
REJECTION-PACKAGE citing EFIA-MATRIX-ABSENT (§7).

If the matrix is present but any criterion has:
- `evidence_type_submitted: E5` when minimum is E1–E4, OR
- `evidence_meets_minimum: NO`, OR
- `evidence_reference` is blank or points to a non-existent artifact

IAA MUST issue a REJECTION-PACKAGE citing EFIA-EVIDENCE-GAP (§7).

---

## 3. Build-Correctness / Architecture-Compliance Review

### 3.1 Build-Correctness Gate

IAA MUST independently assess build correctness before issuing a PASS. This is not a
check of the producing agent's claim of correctness — it is an independent review.

Build-correctness assessment MUST include:

1. **CI result verification** — confirm the CI run referenced in the evidence matrix is for
   the actual PR branch and shows green state at the correct commit SHA
2. **Test coverage assessment** — verify test count and coverage align with what was claimed;
   confirm no `.skip()`, `.todo()`, or stub tests inflate the count
3. **Diff review** — review the actual PR diff for obvious correctness problems not caught
   by automated tests (see §4 Diff-First Audit)
4. **Architecture compliance spot-check** — for builds touching core interfaces, verify
   alignment with frozen architecture docs

### 3.2 Architecture-Compliance Review Requirement

For PRs touching `governance/**`, `.github/agents/**`, or schema/migration paths, IAA MUST
verify that the change is **architecturally compliant**:

1. Is the change consistent with the stated architecture design artifact (if one exists)?
2. Does the change introduce any contradiction with existing canonical rules?
3. For governance canon changes: is the amendment authority respected (CS2 sign-off)?
4. For agent contract changes: is the change within the agent's authorized write scope?

If IAA cannot determine architectural compliance from the submitted evidence, IAA MUST
request additional evidence — not assume compliance.

---

## 4. Diff-First Audit

### 4.1 Definition

The **diff-first audit** is IAA's independent review of the actual PR diff, performed
**before** reading the producing agent's handover narrative. The purpose is to:

1. Independently identify what was actually changed (not what was claimed to be changed)
2. Detect scope creep or undeclared changes in protected paths
3. Identify risk the producing agent may have under-classified
4. Verify the declared scope matches the actual diff

### 4.2 Diff-First Audit Protocol

IAA MUST execute the diff-first audit in this order:

```
Step 1: Review the raw PR diff independently.
Step 2: List all changed files and classify by path (protected path? governance? CI? code?).
Step 3: Identify the risk class of the actual changes (using PPEIA-001 §4.3 risk classes).
Step 4: Record the independently derived risk classification.
Step 5: Compare with the producing agent's declared scope and risk classification.
Step 6: If mismatch: cite EFIA-SCOPE-MISMATCH or EFIA-RISK-UNDERCLASSIFIED (§7).
Step 7: Only then read the producing agent's narrative/handover.
```

### 4.3 Diff-First Audit Record

IAA MUST record the diff-first audit result in the ASSURANCE-TOKEN or REJECTION-PACKAGE:

```yaml
diff_first_audit:
  files_changed_count: [N]
  protected_paths_identified: ["[path]", ...]
  independently_derived_risk_class: "LOW | MEDIUM | HIGH | CRITICAL"
  producing_agent_declared_risk_class: "LOW | MEDIUM | HIGH | CRITICAL | NOT_DECLARED"
  risk_class_match: "YES | NO — [reason if NO]"
  scope_match: "YES | NO — [undeclared changes identified]"
  diff_first_audit_verdict: "PASS | FAIL"
```

---

## 5. Independent Risk Challenge

### 5.1 IAA Must Independently Assess Risk

IAA MUST NOT adopt the producing agent's risk classification without independent verification.
The independent risk challenge requires IAA to:

1. Classify the PR's risk **before** reading the producing agent's risk declaration
2. Compare classifications
3. If the producing agent under-classified the risk by one tier: record as advisory
4. If the producing agent under-classified the risk by two or more tiers: REJECT (EFIA-RISK-UNDERCLASSIFIED)

### 5.2 Risk Challenge for Governance and CI Changes

For PRs touching `governance/**` or `.github/workflows/**`:
- IAA MUST verify that **no existing gate is weakened or removed** by the change
- IAA MUST verify that **no existing ACR or rejection trigger is removed or softened**
- If any gate weakening is detected: REJECT citing EFIA-GATE-WEAKENING (§7)

---

## 6. No Evidence-Type Downgrade Rule

### 6.1 Definition

**Evidence-type downgrade** occurs when:
- A handover bundle cites E5 (agent attestation) for an acceptance criterion that requires E3 or higher
- A handover bundle cites E4 (static analysis) for a criterion that requires E2 (live E2E) or higher
- A handover bundle omits evidence entirely for a criterion (implicit downgrade to "no evidence")

### 6.2 Downgrade Prohibition

IAA MUST reject any PASS attempt where evidence-type downgrade is detected. There is no
circumstance under which a lower-quality evidence type substitutes for the required type
without CS2 explicit authorization of an evidence-type exception.

### 6.3 Evidence-Type Exception (CS2-Only)

CS2 may authorize an evidence-type exception when:
- A live environment is not available and this is documented
- The acceptance criterion is demonstrably not automatable in the current environment

Evidence-type exception MUST be:
1. Recorded as a CS2 comment in the PR
2. Cited in the `ac_evidence_matrix` as `evidence_type_exception: "CS2 — [PR comment URL]"`
3. The exception must specify the alternative evidence accepted

---

## 7. Expanded Blocked Verdicts (EFIA Rejection Classes)

IAA MUST issue a REJECTION-PACKAGE for any of the following:

| Rejection Code | Trigger Condition |
|---------------|------------------|
| EFIA-MATRIX-ABSENT | `ac_evidence_matrix` YAML block absent from wave record §3c |
| EFIA-EVIDENCE-GAP | Any criterion in the matrix has `evidence_meets_minimum: NO` or blank `evidence_reference` |
| EFIA-AGENT-CLAIM | Acceptance criterion requiring E1–E4 satisfied only by E5 (agent attestation) |
| EFIA-DOWNGRADE | Evidence-type downgrade detected without CS2 exception authorization |
| EFIA-SCOPE-MISMATCH | Diff-first audit reveals undeclared changes not present in the declared scope |
| EFIA-RISK-UNDERCLASSIFIED | Producing agent's risk classification is two or more tiers below IAA's independent assessment |
| EFIA-GATE-WEAKENING | A change removes or softens an existing governance gate, ACR, or rejection trigger |
| EFIA-CI-UNVERIFIABLE | CI results referenced in evidence matrix cannot be independently verified (wrong branch, wrong SHA, or link inaccessible) |
| EFIA-ARCH-NONCOMPLIANT | Architecture compliance cannot be confirmed from submitted evidence for a change requiring it |

---

## 8. ECAP Evidence-First Preparation Duties

### 8.1 ECAP Must Prepare Evidence-First Material

As defined in `EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` §3.11 (added by ECAP-001 v1.3.0),
when ECAP is appointed for a qualifying delivery, it MUST:

1. Extract all acceptance criteria from the governing delivery issue
2. Map each criterion to its minimum required evidence type (per §1.2)
3. Collect or verify the existence of evidence artifacts for each criterion
4. Populate the `ac_evidence_matrix` YAML block in wave record §3c
5. Flag any criterion where evidence is insufficient and return to producing agent

ECAP MUST NOT substitute its own attestation for required E1–E4 evidence — this is an
ECAP-boundary violation. ECAP verifies evidence exists; it does not generate evidence.

### 8.2 ECAP Evidence Matrix Completeness Check

Before returning the bundle to the Foreman, ECAP MUST verify:

```yaml
evidence_matrix_completeness_check:
  all_criteria_mapped: "YES | NO — [missing criteria]"
  all_evidence_references_accessible: "YES | NO — [inaccessible references]"
  no_e5_only_criteria_requiring_higher: "YES | NO — [criteria with E5-only violation]"
  evidence_matrix_completeness_verdict: "PASS | FAIL"
```

---

## 9. Integration Requirements

### 9.1 PHCP-001 Integration

`PR_HANDOVER_CANONICAL_PACKAGE.md` (PHCP-001) §4.1 MUST include the following additional
field in the `pre_pr_blocking_gate` YAML block:

```yaml
ac_evidence_matrix_populated: "YES | N/A — not required for this tier"
evidence_type_downgrade_check: "CLEAN | FAIL — [criteria affected]"
```

### 9.2 PPEIA-001 Integration

For protected-path PRs, evidence-first material is prepared as part of ECAP protected-path
ceremony duties per `PROTECTED_PATH_ECAP_BEFORE_IAA_CANON.md` §4.1.

### 9.3 WRCC-001 Integration

`WAVE_RESULT_COHERENCE_CANON.md` (WRCC-001) §4 MUST treat a missing or failed
`ac_evidence_matrix` as a wave-result coherence failure — the wave cannot declare
COMPLETE state if evidence requirements are not met.

---

## Appendix A: Evidence-First Quick Reference

```
Before declaring QP PASS, verify:
✅ ac_evidence_matrix YAML block present in wave record §3c
✅ Every acceptance criterion mapped to evidence of required type
✅ No E5-only criterion where E1–E4 is required
✅ All evidence references point to committed/accessible artifacts
✅ No evidence-type downgrade without CS2 exception
✅ CI results verified at correct branch/SHA
✅ Diff-first audit performed and recorded
✅ Risk class independently assessed
```

---

**Canon ID**: EFIA-001
**Filed by**: foreman-v2-agent (POLC-Orchestration governance specification) | **Date**: 2026-04-28
**Authority**: CS2 — Umbrella: Upgrade AMC PR handover assurance to ISMS-level evidence-first protected-path scrutiny
**See also**: PPEIA-001, AAEV-001, WRCC-001, ECAP-001, PHCP-001, INDEPENDENT_ASSURANCE_AGENT_CANON.md

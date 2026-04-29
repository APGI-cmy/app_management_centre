**Status**: CANONICAL | **Version**: 1.0.0 | **Authority**: CS2
**Date**: 2026-04-28
**Canon ID**: PPEIA-001
**Issue**: app_management_centre — Umbrella: Upgrade AMC PR handover assurance to ISMS-level evidence-first protected-path scrutiny (Child 1)

> **Amendment Authority**: Only CS2 (Johan Ras / repo owner) may amend this canon.
> Any PR modifying this file without CS2 sign-off is auto-FAIL at the merge gate.

---

# Protected-Path ECAP-Before-IAA Canon

## Purpose

This canon defines the **mandatory execution-ceremony-admin-agent (ECAP) ceremony requirement**
that must be satisfied before the Independent Assurance Agent (IAA) may issue a PASS token for
any PR that touches a **protected path** in the AMC repository.

It closes the gap identified in the umbrella issue: AMC PRs touching governance, workflow,
and runtime-sensitive paths previously reached IAA without mandatory ECAP/admin ceremony,
creating a class of preventable failures that leaked to human review.

This canon builds on and does not replace:
- `EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` (ECAP-001)
- `INDEPENDENT_ASSURANCE_AGENT_CANON.md`
- `PR_HANDOVER_CANONICAL_PACKAGE.md` (PHCP-001)

---

## 1. Protected-Path Definition

### 1.1 Protected Paths (Mandatory ECAP Trigger)

The following path patterns are **protected paths**. Any PR whose diff touches one or more
files matching these patterns is a **protected-path PR** and MUST satisfy the ECAP-before-IAA
requirement defined in §2.

| # | Path Pattern | Rationale |
|---|-------------|-----------|
| PP-01 | `.github/workflows/**` | CI workflow changes affect all automated gates |
| PP-02 | `.github/scripts/**` | Automation scripts affect gate execution and tooling |
| PP-03 | `governance/**` | Governance canon changes affect all downstream agent behaviour |
| PP-04 | `.agent-admin/**` (templates, assurance, handover artifacts) | Ceremony artifacts and templates — changes propagate to all future waves |
| PP-05 | `.github/agents/**` | Agent contract files define autonomous agent authority boundaries |
| PP-06 | Schema / migration / runtime-sensitive paths | Files with direct runtime or data-integrity impact (e.g., `supabase/migrations/**`, `schema/**`, `migrations/**`) |
| PP-07 | Stage tracker / index / control surfaces | Files that affect merge posture or stage progression (e.g., `*-tracker.md`, `*-index.md`, `BUILD_PROGRESS_TRACKER*`) |
| PP-08 | `.governance-pack/**` | Canon inventory, consumer registry, gate requirements index — affects all agent capability and gate verification |

### 1.2 Path Classification Rule

A PR is classified as a protected-path PR if **any single file** in its diff matches a
protected path pattern. The highest-risk path determines the classification. When in doubt,
classify as protected-path. Downgrade requires CS2 explicit classification comment in the PR.

### 1.3 Exclusions

The following do not trigger the protected-path requirement:
- CS2-authored direct commits where CS2 records a `CS2-DIRECT-REVIEW` comment per
  `INDEPENDENT_ASSURANCE_AGENT_CANON.md §CS2 Direct Review Track`
- Read-only reference files that contain no executable logic and no gate authority (e.g.,
  `README.md`, pure documentation outside governance canon)
- Files explicitly waived by CS2 per §3 (Waiver Schema)

---

## 2. ECAP-Before-IAA Requirement

### 2.1 The Mandatory Sequence

For every protected-path PR, the following sequence MUST be executed in order before IAA
may issue a PASS token:

```
1. ECAP appointed by Foreman (per ECAP-001 §3.2)
2. ECAP prepares ceremony bundle including evidence-first material (see §4)
3. ECAP returns bundle to Foreman
4. Foreman executes §14.6 QP Admin-Compliance Checkpoint
5. Foreman invokes IAA (only after ECAP ceremony is complete and checkpoint passes)
6. IAA evaluates ECAP presence (ACR-21) as part of assurance audit
7. IAA issues ASSURANCE-TOKEN or REJECTION-PACKAGE
```

**Prohibition**: IAA MUST NOT issue a PASS token for a protected-path PR if step 1–4 have
not been completed and documented in the wave record.

### 2.2 Evidence of ECAP Completion

ECAP completion for a protected-path PR MUST be evidenced by:

1. The ECAP reconciliation summary committed to `.agent-admin/prehandover/ecap-reconciliation-<PR#>.md`
2. The ECAP reconciliation summary contains a `protected_path_ceremony` section (see §4.2)
3. The wave record section 1 lists `execution-ceremony-admin-agent` in `agents_delegated_to`
4. The wave record section 4 records the ECAP checkpoint result (`§14.6 CHECKPOINT: ACCEPTED`)

### 2.3 IAA Rejection on Missing ECAP (ACR-21)

If IAA evaluates a protected-path PR and finds that ECAP was not appointed and completed
before IAA invocation, and no CS2 waiver exists (§3), IAA MUST issue a REJECTION-PACKAGE
citing:

```
ACR-21: Protected-path PR reached IAA without ECAP/admin ceremony.
Protected path(s) identified: [list matching paths].
ECAP reconciliation summary: [ABSENT | present but missing §4.2 protected_path_ceremony section].
CS2 waiver: ABSENT.
Resolution required: Appoint ECAP, complete ceremony including §4.2, obtain Foreman §14.6 CHECKPOINT: ACCEPTED, re-invoke IAA.
```

---

## 3. CS2 Waiver Schema

### 3.1 When a Waiver May Be Granted

CS2 may grant a waiver of the ECAP-before-IAA requirement when:
- The protected-path change is trivial in risk (e.g., typo fix in a non-critical governance doc)
- CS2 is performing a direct-review merge with no independent assurance layer required
- An emergency fix requires immediate deployment and CS2 takes explicit ownership

### 3.2 Waiver Documentation Requirements

A CS2 waiver MUST be recorded:
1. As a comment in the GitHub PR by @APGI-cmy (CS2)
2. In the wave record §1 under `entry_condition_exception` schema
3. Referenced in the PR body `entry_condition_status: EXCEPTION — [waiver reference]`

### 3.3 Waiver Schema

```yaml
protected_path_ecap_waiver:
  waiver_granted_by: "CS2 — @APGI-cmy"
  waiver_reference: "[PR comment URL or issue #NNN]"
  waiver_scope: "[Exactly which protected paths are waived]"
  waiver_reason: "[Why the normal ECAP-before-IAA requirement does not apply]"
  risk_assessment: "[CS2 risk justification]"
```

---

## 4. ECAP Protected-Path Ceremony Duties

### 4.1 Extended ECAP Scope for Protected-Path PRs

When ECAP is appointed for a protected-path PR, it MUST perform the following additional
duties beyond the standard ECAP-001 ceremony obligations:

1. **Identify all protected paths** in the PR diff and record them in the reconciliation summary
2. **Evidence-first material preparation** — ensure each acceptance criterion has evidence of
   the required type (per `AMC_EVIDENCE_FIRST_IAA_ASSURANCE_CANON.md` §3)
3. **Diff-first audit** — verify the PR diff matches the declared scope; flag any undeclared
   changes in protected paths
4. **Governance/workflow impact assessment** — for `.github/workflows/**` and `governance/**`
   changes, assess whether the change alters any existing gate, ACR, or authority binding
5. **Risk declaration** — explicitly declare the operational risk class of the protected-path
   change (see §4.3)

### 4.2 Protected-Path Ceremony Section (Required in ECAP Reconciliation Summary)

The ECAP reconciliation summary MUST contain the following section for protected-path PRs:

```yaml
protected_path_ceremony:
  protected_paths_identified:
    - "[pattern: actual file path]"
  ecap_waiver_applicable: "NO | YES — [waiver reference]"
  evidence_first_material_verified: "PASS | FAIL — [details]"
  diff_scope_matches_declared_scope: "PASS | FAIL — [any undeclared protected-path changes]"
  governance_impact_assessed: "PASS | N/A — [what gates/ACRs are affected, if any]"
  operational_risk_class: "LOW | MEDIUM | HIGH | CRITICAL — [justification]"
  protected_path_ceremony_verdict: "PASS | FAIL — PASS only if all above are PASS or N/A"
```

### 4.3 Operational Risk Classes

| Class | Definition | Examples |
|-------|-----------|---------|
| LOW | Change affects documentation only, no gate or authority change | Typo fix in governance doc |
| MEDIUM | Change affects one gate or one agent duty without removing protection | Adding a new ACR to IAA canon |
| HIGH | Change affects multiple gates, agent authority boundaries, or CI pipeline logic | Workflow file change affecting merge gate |
| CRITICAL | Change removes or weakens an existing protection, or affects runtime data integrity | Removing an existing ACR; schema migration |

---

## 5. Integration Requirements

### 5.1 PHCP-001 Integration

`PR_HANDOVER_CANONICAL_PACKAGE.md` (PHCP-001) §4.1 Pre-PR Blocking Gate MUST include the
following additional field in the `pre_pr_blocking_gate` YAML block for protected-path PRs:

```yaml
protected_path_ecap_ceremony_completed: "YES | N/A — not a protected-path PR | WAIVED — [reference]"
```

### 5.2 WRCC-001 Integration

`WAVE_RESULT_COHERENCE_CANON.md` (WRCC-001) §3 MUST treat a missing
`protected_path_ceremony` section in the ECAP reconciliation summary (for a protected-path PR)
as a coherence failure equivalent to a missing PREHANDOVER proof.

### 5.3 EWCS-001 Integration

`END_OF_WAVE_CLOSEOUT_SWEEP_CANON.md` (EWCS-001) §1.3 closeout sweep checklist item CS-11
checks ECAP protected-path ceremony completion for protected-path PRs:

```
CS-11 | ECAP protected-path ceremony | If PR diff matches any PP-01 through PP-08 pattern:
       ECAP reconciliation summary present with §4.2 protected_path_ceremony section showing
       PASS; OR CS2 waiver documented per §3.2 of this canon.
```

---

## 6. Violation Classes

| Violation Class | Description |
|-----------------|-------------|
| PPEIA-001 | Protected-path PR reached IAA without ECAP/admin ceremony and without CS2 waiver |
| PPEIA-002 | ECAP reconciliation summary missing §4.2 protected_path_ceremony section for a protected-path PR |
| PPEIA-003 | Protected-path evidence-first material not prepared or failed (§4.1 duty 2) |
| PPEIA-004 | Diff scope declared but protected-path changes present in diff beyond declared scope |
| PPEIA-005 | CS2 waiver granted but not recorded in all three required locations (§3.2) |
| PPEIA-006 | Operational risk class not declared or under-declared for a protected-path change |

---

## Appendix A: Quick Reference — Protected-Path Check Card

```
Before invoking IAA, verify for every PR:
1. Does the PR diff touch any PP-01 through PP-08 path? YES / NO
   If NO → standard ceremony applies; this canon does not activate.
   If YES → protected-path PR:
2. Is a CS2 waiver documented per §3? YES (proceed to step 7) / NO (proceed to step 3)
3. Was ECAP appointed? YES / NO (if NO → PPEIA-001)
4. Did ECAP complete ceremony bundle including §4.2 protected_path_ceremony? YES / NO (if NO → PPEIA-002)
5. Is protected_path_ceremony_verdict: PASS? YES / NO (if NO → resolve before IAA)
6. Did Foreman execute §14.6 QP Admin-Compliance Checkpoint? YES / NO (if NO → HALT)
7. Record in wave record §1 protected_path_ecap_ceremony_completed field
→ Only then invoke IAA.
```

---

## Appendix B: Relationship to Existing Canons

| Concern | Governed By |
|---------|------------|
| ECAP ceremony obligations (standard) | `EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` (ECAP-001) |
| IAA assurance and rejection triggers | `INDEPENDENT_ASSURANCE_AGENT_CANON.md` (ACR-21) |
| Evidence-first material requirements | `AMC_EVIDENCE_FIRST_IAA_ASSURANCE_CANON.md` (EFIA-001) |
| PR handover bundle requirements | `PR_HANDOVER_CANONICAL_PACKAGE.md` (PHCP-001) |
| Wave result coherence | `WAVE_RESULT_COHERENCE_CANON.md` (WRCC-001) |
| End-of-wave closeout sweep | `END_OF_WAVE_CLOSEOUT_SWEEP_CANON.md` (EWCS-001) |
| Governing-issue parity | `GOVERNING_ISSUE_PARITY_PROTOCOL.md` (GIPC-001) |
| CS2 waiver for direct review | `INDEPENDENT_ASSURANCE_AGENT_CANON.md §CS2 Direct Review Track` |

---

**Canon ID**: PPEIA-001
**Filed by**: foreman-v2-agent (POLC-Orchestration governance specification) | **Date**: 2026-04-28
**Authority**: CS2 — Umbrella: Upgrade AMC PR handover assurance to ISMS-level evidence-first protected-path scrutiny
**See also**: EFIA-001, AAEV-001, WRCC-001, ECAP-001, PHCP-001, EWCS-001, GIPC-001


**Status**: CANONICAL | **Version**: 1.0.0 | **Authority**: CS2
**Date**: 2026-04-27
**Canon ID**: OSSCP-001
**Issue**: app_management_centre#1139 — Hardening — PR handover must enforce governing-issue role separation, retire stale handover injectors, and block partial handover state

> **Amendment Authority**: Only CS2 (Johan Ras / repo owner) may amend this canon.
> Any PR modifying this file without CS2 sign-off is auto-FAIL at the merge gate.

---

# Operational Strategy Sanity Check Protocol

## Purpose

This protocol defines the **mandatory literal implementation sanity-check** that must be
applied to governance documents that define operational execution behavior (strategy documents)
before those documents can be declared handover-ready.

The goal is to prevent handover-ready governance documents from still containing operationally
invalid instructions that a builder would be unable to execute literally — or would execute
incorrectly due to ambiguity, missing state, or contradictory directives.

This is distinct from a content or quality review. It is a **literal execution sanity-check**:
could a builder implement this document exactly as written?

---

## 1. Scope — What Is an Operational Strategy Document?

### 1.1 Definition

An **operational strategy document** is any governance artifact that:
- Defines execution steps, commands, or workflows that an agent or process will run
- Specifies trigger models, event sequences, or automation behavior
- Describes migration, deployment, runner, or environment provisioning procedures
- Provides instructions for approval, sign-off, or review workflows

### 1.2 Examples

Documents that fall within scope of this protocol include (but are not limited to):

| Document Type | Examples |
|---------------|----------|
| CI/CD workflow definitions | `*.yml` workflow files, build pipeline specs |
| Agent contract operational sections | Phase 1–4 execution steps in agent contracts |
| Wave execution protocols | Builder task specifications, builder instructions |
| Deployment / migration guides | Database migration protocols, environment setup |
| Approval workflow specs | Sign-off procedures, gate evaluation specs |
| Runner / environment specs | GitHub Actions runner configurations, environment provisioning |

### 1.3 Documents NOT in Scope

The following document types do NOT require an operational sanity-check (but do require
other quality checks):

- Pure reference or taxonomy documents (no execution steps)
- Historical or archived documents
- Templates (sanity-check applies when a template is filled and used, not to the template itself)
- Retrospective or lesson-learned documents

---

## 2. The Literal Implementation Sanity-Check

### 2.1 The Core Test

Before a strategy document is declared handover-ready, the producing agent MUST ask:

> "Could a builder implement this literally as written, without any hidden state,
> implicit prerequisites, or ambiguous interpretation?"

The answer must be YES on all dimensions below. A single NO is a sanity-check FAIL.

### 2.2 Sanity-Check Dimensions

The sanity-check evaluates the following dimensions. Each must produce a PASS verdict:

#### Dimension 1: Literal Executability
**Question**: Can every step or command in this document be executed literally as written?

Check for:
- Commands that reference variables or paths not defined earlier in the document
- Steps that depend on hidden state (e.g., "run X after Y completes" but Y is not in the document)
- Instructions that only work in a specific unmentioned context (e.g., only valid on a specific OS)
- Bash/shell commands that cannot run without prerequisites not listed

**Fail Signal**: Any step that requires undeclared state, undeclared variables, or
undeclared prerequisites.

#### Dimension 2: No Hidden State Dependencies
**Question**: Does any command or step require hidden state that is not explicitly declared
in this document or explicitly referenced from another declared source?

Check for:
- Environment variables that are used but never set or sourced
- File paths that are assumed to exist but are never created or referenced
- Secret or credential references without a clear sourcing instruction
- Git state (branch, SHA, remote) assumed to be in a specific condition without verification step

**Fail Signal**: Any reference to state that must exist but is never established within the document's scope.

#### Dimension 3: No Cross-Workflow Dependency Violations
**Question**: If any step depends on output from another workflow or process, is that
dependency explicitly declared and is the dependency path valid?

Check for:
- Steps that say "the output from workflow X is available here" without a formal input/output contract
- Workflow triggers that only work within one file but are written as cross-workflow guidance
- Job output references (`needs.job.outputs.x`) where the source job is in a different workflow

**Fail Signal**: Any cross-workflow dependency that is not declared with an explicit
integration contract (e.g., `workflow_call` outputs, dispatch events, artifact uploads/downloads).

#### Dimension 4: No Trigger Model Contradictions
**Question**: Do the trigger models in the document produce a consistent, non-contradictory execution model?

Check for:
- Two triggers that activate the same workflow step under mutually exclusive conditions
- A trigger described as `on: push` in one place but `on: pull_request` in another for the same step
- Conditional logic (`if:`) that contradicts the trigger conditions
- Event filters (`paths:`, `branches:`) that would prevent the trigger from ever firing

**Fail Signal**: Any trigger specification where two or more triggers produce contradictory
execution conditions for the same outcome.

#### Dimension 5: Exactly One Executable Interpretation
**Question**: Is there exactly one way to interpret and execute the critical path of this document?

Check for:
- Ambiguous use of "should" vs "must" vs "may" in execution steps
- Steps described at two different abstraction levels without a clear hierarchy
- Options presented without a decision rule for which option to choose
- Merge, deploy, or approval behavior described in a way that could be interpreted in two or more ways

**Fail Signal**: Any step where a reasonable implementer could produce two different valid
execution sequences from the same instruction.

#### Dimension 6: Migration / Deploy / Runner Consistency
**Question**: Are migration, deployment, and runner behaviors described consistently and without contradiction?

Check for:
- Database migration steps described differently in two sections of the same document
- Deployment sequence that contradicts the rollback sequence
- Runner type (`ubuntu-latest` vs `self-hosted`) specified inconsistently
- Approval gate described as required in one section and optional in another

**Fail Signal**: Any inconsistency between two sections of the same document on migration,
deployment, or runner/approval behavior.

---

## 3. Conducting the Sanity-Check

### 3.1 Who Performs the Check

The sanity-check is performed by:
- The **producing agent** (Foreman, ECAP, or builder) as a pre-QP self-check
- The **Foreman QP** as part of Quality Professor evaluation
- **IAA** as part of its standard audit (for strategy docs in scope)

### 3.2 Sanity-Check Evidence Format

The producing agent MUST record the sanity-check result in the wave record §3c or
PREHANDOVER proof using the following format:

```yaml
operational_sanity_check:
  documents_checked:
    - path: "[path/to/strategy-doc.md or workflow.yml]"
      dimension_1_literal_executability: "PASS / FAIL — [finding if FAIL]"
      dimension_2_no_hidden_state: "PASS / FAIL — [finding if FAIL]"
      dimension_3_no_cross_workflow_violation: "PASS / FAIL / N/A — [finding if FAIL]"
      dimension_4_no_trigger_contradiction: "PASS / FAIL / N/A — [finding if FAIL]"
      dimension_5_single_interpretation: "PASS / FAIL — [finding if FAIL]"
      dimension_6_migration_deploy_runner_consistency: "PASS / FAIL / N/A — [finding if FAIL]"
      overall_verdict: "PASS / FAIL"
      remediation: "N/A / [description of fix applied]"
  sanity_check_overall: "PASS / FAIL"
  sanity_check_performed_by: "[agent-id]"
  sanity_check_date: "YYYY-MM-DD"
```

### 3.3 When to Apply

The sanity-check MUST be applied when:
- The wave produces or significantly modifies a strategy document (as defined in §1.1)
- An existing strategy document is referenced as the authoritative guide for a new
  execution step being added to a wave
- A strategy document is declared "complete" or "ready for handover" for the first time

The sanity-check MUST NOT be skipped for:
- CI/CD workflow files produced or modified as a wave deliverable
- Agent contract operational sections produced or modified as a wave deliverable
- Deployment or migration guides declared handover-ready

### 3.4 N/A Declaration

A dimension may be declared N/A only when:
- The dimension genuinely does not apply to the document type (e.g., "no trigger model" for a migration guide)
- The N/A declaration is accompanied by a brief justification

N/A MUST NOT be used to avoid a dimension that is applicable.

---

## 4. Sanity-Check Failure Handling

### 4.1 Failure Classification

| Failure Type | Classification | Wave Impact |
|-------------|----------------|-------------|
| Any FAIL on Dimensions 1, 2, or 5 | BLOCKING — document cannot be declared handover-ready | Wave HALT |
| Any FAIL on Dimensions 3, 4, or 6 | BLOCKING — but limited to the specific inconsistent element | Partial HALT |
| N/A misuse (dimension claimed N/A without justification) | BLOCKING | Wave HALT until N/A is justified or dimension evaluated |

### 4.2 Remediation Protocol

When a sanity-check FAIL is detected:

1. Record the finding in the `remediation` field of the evidence block
2. Fix the document to resolve the failing dimension
3. Re-run the affected dimension and record `PASS` with the remediation description
4. Do NOT set `overall_verdict: PASS` until all dimensions pass or are validly N/A
5. The corrected document must be committed before the wave proceeds to IAA

### 4.3 IAA Handling

If IAA detects a strategy document that was not sanity-checked but should have been:
- IAA issues REJECTION-PACKAGE citing OSSCP-SKIP-001
- The wave must perform the sanity-check, record evidence, fix any failures, and re-invoke IAA

---

## 5. Integration with Pre-PR Blocking Gate

The `operational_sanity_check_performed` field in the pre-PR blocking gate evidence
(see `PR_HANDOVER_CANONICAL_PACKAGE.md` §4.1) MUST be:
- `YES` — when the wave includes strategy documents in scope per §1.1
- `N/A` — only when the wave genuinely produces no strategy documents

A PR opened with `operational_sanity_check_performed: NO` or absent when the wave
includes strategy documents is a pre-PR blocking gate FAIL.

---

## 6. Violation Codes

| Code | Description |
|------|-------------|
| `OSSCP-SKIP-001` | Sanity-check not performed on a strategy document that required it |
| `OSSCP-FAIL-001` | Dimension 1 (Literal Executability) failed |
| `OSSCP-FAIL-002` | Dimension 2 (No Hidden State) failed |
| `OSSCP-FAIL-003` | Dimension 3 (No Cross-Workflow Violation) failed |
| `OSSCP-FAIL-004` | Dimension 4 (No Trigger Contradiction) failed |
| `OSSCP-FAIL-005` | Dimension 5 (Single Interpretation) failed |
| `OSSCP-FAIL-006` | Dimension 6 (Migration/Deploy/Runner Consistency) failed |
| `OSSCP-NA-MISUSE` | Dimension declared N/A without justification |

---

## Appendix A: Quick-Reference Sanity-Check Card

Before QP PASS on a wave with strategy documents:

```
✅ All strategy documents identified (scope: §1.1)
✅ Dimension 1: Every step executable literally as written
✅ Dimension 2: No hidden state — all prerequisites declared
✅ Dimension 3: No cross-workflow dependency violations
✅ Dimension 4: Trigger models consistent, no contradictions
✅ Dimension 5: Exactly one interpretation of the critical path
✅ Dimension 6: Migration/deploy/runner behaviors consistent
✅ Evidence block populated in wave record §3c / PREHANDOVER proof
✅ operational_sanity_check_performed: YES in pre-PR blocking gate fields
```

---

**Canon ID**: OSSCP-001
**Filed by**: foreman-v2-agent (POLC-Orchestration governance specification) | **Date**: 2026-04-27
**Authority**: CS2 — Issue #1139
**See also**: `PR_HANDOVER_CANONICAL_PACKAGE.md` (PHCP-001), `END_OF_WAVE_CLOSEOUT_SWEEP_CANON.md` (EWCS-001)


**Status**: CANONICAL | **Version**: 1.0.1 | **Authority**: CS2
**Date**: 2026-04-22
**Amended**: 2026-04-22 — v1.0.1: Tightened §1 and §2 to remove FRS and TRS from "Stage 1 document" examples — FRS is Stage 3 and TRS is Stage 4 in the 12-stage pre-build model; this protocol applies only to the App Description (Stage 1); added clarifying scope note in §1; authority: CS2 — Stage 1 mislabeling correction.

---

# Stage 1 Approval-Alignment QA Protocol

## Purpose

This canon defines the **mandatory QA structure** that must be applied to any wave whose
primary objective is a Stage 1 approval-alignment state transition — that is, any wave that
advances the status of a Stage 1 artifact from:

- `pending` → `approved`
- `provisional` → `authoritative`
- `temporary canonical` → `superseded` (for the old source)
- any equivalent pre-approval or pre-authoritative state → a post-approval or
  post-authoritative state

The protocol addresses the class of miss documented in PR #1118, where top-level approval
surfaces were updated correctly but stale pending/provisional language and canonical-source
contradictions remained deeper in the canonical artifact set.

> **Key rule**: A Stage 1 approval-alignment PR is not approvable if the repository still
> contains conflicting authority or approval-state statements anywhere in the live Stage 1
> artifact chain, regardless of whether those conflicts appear at the top level or deep in
> section bodies, footer declarations, or linked artifacts.

---

## 1. Applicability

This protocol applies to any PR or wave that:

1. Changes the status of a Stage 1 document from a non-authoritative to an authoritative
   state
2. Records an approval event for a Stage 1 document (App Description — Stage 1 in the
   12-stage pre-build model per `PRE_BUILD_STAGE_MODEL_CANON.md`)
3. Transitions a root pointer file from pointing at a predecessor source to the new
   canonical source
4. Marks a predecessor Stage 1 artifact as superseded

> **Scope note**: "Stage 1" in this protocol refers exclusively to Stage 1 of the
> 12-stage pre-build model, which is the **App Description**. FRS (Stage 3), TRS (Stage 4),
> and all other pre-build stage documents are out of scope for this protocol. Approval
> events for those stages are governed by their own review structures and do not trigger
> this protocol's classification rules or hard gates.

When **any** of the above conditions is met, the full Stage 1 Approval-Alignment QA
Protocol is **mandatory** at all three review layers:

- **Layer 1** — ECAP (execution-ceremony-admin-agent) §4.3e gate
- **Layer 2** — Foreman QP Admin-Compliance Checkpoint §14.6
- **Layer 3** — IAA ACR-17 through ACR-20 assurance checks

---

## 2. Stage 1 Artifact Chain

The following artifacts constitute the **Stage 1 approval-alignment artifact chain**. Every
artifact in this chain must be in a mutually consistent post-approval state before any review
layer may approve the wave.

| Artifact Class | Canonical Examples | State-Transition Obligation |
|----------------|--------------------|----------------------------|
| **Canonical Stage 1 document** | App Description (Stage 1 in the 12-stage pre-build model) | Whole-document sweep required (§3) |
| **Approval record** | `approval-record-*.md`, embedded `## Approval Record` sections | Must not contain blank approval fields or `pending` status |
| **Build progress tracker** | `build-progress-tracker-*.md`, `*-tracker.md` | Must not reference source-of-truth as pending or provisional |
| **Pre-build artifact index** | `pre-build-artifact-index-*.md`, `artifact-index-*.md` | Pointer entries must reflect the new canonical source |
| **Repo realignment note** | `repo-realignment-*.md`, `realignment-note-*.md` | Must not declare migration decision as unresolved or pending |
| **Root pointer file(s)** | `*-root-pointer.md`, `.canonical-source`, `CANONICAL_SOURCE.md` | Must point to the new canonical source, not the predecessor |
| **Predecessor / superseded Stage 1 file(s)** | Any prior version of the Stage 1 document | Must be clearly marked as superseded / historical; must not claim active canonical authority |

---

## 3. Whole-Document State-Transition Sweep (Mandatory)

After any approval-status transition, the reviewer **must scan the entire canonical Stage 1
document** — not only the top-level status block — for stale language.

### 3.1 Stale Language Denylist

The following terms and patterns are **stale post-approval**. Their presence anywhere in
the canonical Stage 1 document after the approval event has been recorded constitutes a
state-transition contradiction:

| Category | Stale Language / Patterns |
|----------|--------------------------|
| **Approval-status language** | `pending`, `pending approval`, `not yet approved`, `approval pending`, `awaiting approval` |
| **Authority language** | `provisional`, `provisional canonical`, `temporary canonical`, `candidate for approval`, `future canonical` |
| **Migration language** | `pending migration`, `migration pending`, `migration decision unresolved`, `to be migrated`, `migration TBD` |
| **Source-of-truth language** | `source of truth pending`, `provisional source of truth`, `source to be confirmed`, `not yet authoritative` |
| **Blank / placeholder fields** | Blank `approved_by` fields, blank `approval_date` fields, `[pending]`, `[fill in]`, `TBD` in approval fields |
| **Unresolved wording** | `to be resolved`, `to be confirmed`, `subject to approval`, `upon approval` |

### 3.2 Sweep Scope

The sweep must cover **every section** of the canonical Stage 1 document, including:

- [ ] Top metadata / status table
- [ ] Authority transition note or section
- [ ] Source-of-truth section
- [ ] Transition posture section
- [ ] Prior-artifact register / predecessor register
- [ ] Embedded approval record or footer declarations
- [ ] Any approval-record block embedded in the body (not only a standalone approval artifact)
- [ ] All subsections — the sweep is whole-document, not top-section-only

**Evidence required**: The producing agent must explicitly attest in the PREHANDOVER proof
(field: `stage1_sweep_completed`) that the whole-document sweep was performed, naming the
canonical Stage 1 document path, the sweep scope, and the result.

---

## 4. Cross-Artifact Approval-State Coherence Check (Mandatory)

After the whole-document sweep, the reviewer must confirm that **every artifact in the
Stage 1 artifact chain** (§2) declares a consistent post-approval state.

### 4.1 Coherence Rules

No artifact in the chain may claim:

- Pending approval for a Stage 1 document that has been approved
- Active canonical authority for a predecessor document that has been superseded
- Provisional derivation from a source that is now authoritative
- Unresolved migration decision for a migration that has been executed

### 4.2 Coherence Check Scope

For each artifact class in the Stage 1 artifact chain (§2), confirm:

| Artifact | Check |
|----------|-------|
| Approval record | `status` field is `APPROVED` or equivalent; `approved_by` and `approval_date` are populated |
| Build progress tracker | Source-of-truth reference points to the new canonical document; no `provisional` or `pending` qualifier on the Stage 1 entry |
| Pre-build artifact index | Canonical source for the relevant module points to the new document; predecessor entry is annotated as superseded |
| Repo realignment note | Migration decision is `EXECUTED` or equivalent; no `pending` or `in progress` qualifier |
| Root pointer file(s) | Points to the new canonical document; does not point to the predecessor |
| Predecessor file(s) | Contains a clear superseded/historical header or status block; does not assert active canonical authority |

---

## 5. Canonical-Pointer and Predecessor-File Reconciliation (Mandatory)

### 5.1 Root Pointer Verification

When a canonical source changes, the reviewer must verify:

- [ ] Every root pointer file now points to the new canonical document
- [ ] No root pointer file still points to the predecessor document
- [ ] If the predecessor document was the canonical source for downstream derivation, a
  migration note exists that redirects derivation to the new canonical source

### 5.2 Predecessor File Verification

- [ ] The predecessor file contains a visible superseded / historical marker in its header
  or status block
- [ ] The predecessor file does not claim active canonical authority, source-of-truth status,
  or derivation authority
- [ ] No artifact in the artifact index or tracker lists the predecessor as an active or
  current artifact without a superseded annotation

### 5.3 Downstream Derivation Pointer Verification

- [ ] No live governance artifact (FRS, TRS, architecture doc) still cites the predecessor
  Stage 1 document as its derivation source unless that citation is annotated as historical

---

## 6. State-Transition Contradiction Classes

Reviewers must explicitly check for each of the following six contradiction classes. These
classes are collectively covered by the relevant ACR triggers (ACR-17 through ACR-20) and
AAP auto-fail rules (AAP-23 through AAP-26); some triggers or auto-fail rules apply to
multiple contradiction classes rather than mapping one-to-one with a single class.

| Class ID | Contradiction Type | Description |
|----------|--------------------|-------------|
| **STC-01** | Header vs section contradiction | Top-level status block declares `APPROVED` but a section body still uses stale pending/provisional language |
| **STC-02** | Canonical artifact vs approval record contradiction | The canonical Stage 1 document's approval section declares `APPROVED` but the standalone approval record still has `status: PENDING` or a blank `approved_by` field |
| **STC-03** | Tracker vs artifact contradiction | The build progress tracker references the Stage 1 artifact as `pending`, `provisional`, or not yet approved while the artifact itself has been approved |
| **STC-04** | Pointer vs canonical source contradiction | A root pointer file or artifact index still points to the predecessor document as the canonical source after the new document has been approved |
| **STC-05** | Predecessor-file vs successor-file contradiction | The predecessor Stage 1 file still asserts active canonical authority or source-of-truth status while the successor has been approved as the new canonical source |
| **STC-06** | Blank-field-after-approval contradiction | An approval record or embedded approval block contains a blank `approved_by`, `approval_date`, or equivalent field while the surrounding context declares the artifact as approved |

---

## 7. Executable Review Checklist

The following checklist must be completed by the producing agent and attached to the
PREHANDOVER proof for every Stage 1 approval-alignment wave. All items must be checked
`[x]` or annotated `[~]` with a documented reason before the bundle is submitted to
Foreman QP or IAA.

```markdown
## Stage 1 Approval-Alignment QA Checklist

**Canonical Stage 1 document path**: [path]
**Approval event date**: [date]
**State transition**: [e.g., pending → approved]
**Completing agent**: [agent-id]
**Date completed**: [YYYY-MM-DD]

### Sweep 1: Whole-Document State-Transition Sweep (§3)

- [ ] S1.1 Top metadata / status table — no stale language
- [ ] S1.2 Authority transition note — no stale language
- [ ] S1.3 Source-of-truth section — no stale language
- [ ] S1.4 Transition posture section — no stale language
- [ ] S1.5 Prior-artifact register — no stale language
- [ ] S1.6 Embedded approval record / footer — no stale language; approval fields populated
- [ ] S1.7 All body subsections — stale language denylist (§3.1) not present anywhere

**Sweep 1 result**: PASS | FAIL
**Stale language found (if FAIL)**: [describe]

### Sweep 2: Cross-Artifact Coherence Check (§4)

- [ ] S2.1 Approval record: status = APPROVED; approved_by and approval_date populated
- [ ] S2.2 Build progress tracker: Stage 1 entry not marked pending/provisional
- [ ] S2.3 Pre-build artifact index: canonical source entry updated to new document
- [ ] S2.4 Repo realignment note: migration decision marked EXECUTED or N/A
- [ ] S2.5 Root pointer file(s): point to new canonical document
- [ ] S2.6 Predecessor file(s): marked superseded / historical

**Sweep 2 result**: PASS | FAIL
**Incoherent artifacts (if FAIL)**: [list artifact paths and contradictions]

### Sweep 3: Canonical-Pointer and Predecessor Reconciliation (§5)

- [ ] S3.1 All root pointer files updated to new canonical source
- [ ] S3.2 Predecessor file carries superseded / historical header
- [ ] S3.3 Predecessor file does not claim active canonical authority
- [ ] S3.4 No live derivation artifact still cites predecessor as authoritative source

**Sweep 3 result**: PASS | FAIL
**Unreconciled pointers or predecessors (if FAIL)**: [list]

### Contradiction Class Check (§6)

- [ ] STC-01 (header vs section): NOT present
- [ ] STC-02 (artifact vs approval record): NOT present
- [ ] STC-03 (tracker vs artifact): NOT present
- [ ] STC-04 (pointer vs canonical source): NOT present
- [ ] STC-05 (predecessor-file vs successor-file): NOT present
- [ ] STC-06 (blank-field-after-approval): NOT present

**Contradiction check result**: PASS | FAIL
**Contradiction classes found (if FAIL)**: [list class IDs and artifact paths]

### Checklist Final Status

**stage1_sweep_completed**: yes | no
**Overall QA result**: PASS | FAIL
**Approved for ECAP submission**: yes | no
```

---

## 8. Relationship to Review Layer Gates

| Review Layer | Gate Reference | Stage 1 Specific Obligation |
|--------------|----------------|------------------------------|
| **ECAP (Layer 1)** | `AGENT_HANDOVER_AUTOMATION.md §4.3e` Check M | Detect stale Stage 1 language in the artifact chain; auto-fail on AAP-23 through AAP-26 |
| **Foreman QP (Layer 2)** | `FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md §14.6` Step 8 | Verify the Stage 1 Approval-Alignment QA Checklist is present and ALL_PASS; verify `stage1_sweep_completed: yes` |
| **IAA (Layer 3)** | `INDEPENDENT_ASSURANCE_AGENT_CANON.md §Admin-Ceremony Rejection Triggers` ACR-17 through ACR-20 | Independent verification of sweep completion, cross-artifact coherence, pointer reconciliation, and contradiction-class coverage |

---

## 9. Stage 1 Wave Classification

A wave is classified as a **Stage 1 approval-alignment wave** if **any** of the following
is true of the PR diff:

1. A file whose path contains `app-description`, `app_description`, `stage1`, `stage-1`,
   `stage_1`, or `00-app-description` is changed and the diff includes changes to a
   `status` or `approval` field
2. An approval record file is committed or modified (path contains `approval-record`)
3. A root pointer file is committed or modified (path contains `root-pointer` or
   `CANONICAL_SOURCE`)
4. The PREHANDOVER proof declares `pr_category: STAGE1_APPROVAL_ALIGNMENT`

When classified, all three check layers in this protocol apply.

---

## References

- `governance/canon/INDEPENDENT_ASSURANCE_AGENT_CANON.md` §Admin-Ceremony Rejection Triggers
  — ACR-17 through ACR-20 are the IAA-layer enforcement of this protocol
- `governance/canon/FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md §14.6` — Foreman QP Step 8
  is the Foreman-layer enforcement of this protocol
- `governance/canon/AGENT_HANDOVER_AUTOMATION.md §4.3e` — CHECK M and AAP-23 through AAP-26
  are the ECAP-layer enforcement of this protocol
- `governance/canon/PRE_BUILD_STAGE_MODEL_CANON.md` — defines the 12-stage pre-build model
  that Stage 1 belongs to

---

*Authority: CS2 (Johan Ras) | Version: 1.0.1 | Effective: 2026-04-22 | Amended: 2026-04-22 (v1.0.1)*

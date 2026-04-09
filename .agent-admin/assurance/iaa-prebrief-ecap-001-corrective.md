# IAA PRE-BRIEF — wave-ecap001-corrective

**Agent**: independent-assurance-agent
**Pre-Brief Version**: 1.0.0
**Date**: 2026-04-08
**Wave**: ecap-001-corrective
**Branch (declared in request)**: copilot/fix-ecap-001-resolve-prehandover-evidence-defects
**Branch (current working HEAD)**: copilot/evidence-defects-prehandover ⚠️ — see §5 Scope Blockers
**Issue**: fix(ecap-001): resolve PREHANDOVER evidence defects — AMC corrective follow-up PR #1041
**Invoking context**: CS2 (@APGI-cmy) — Pre-Brief request issued via issue comment; valid wave-start authorization
**IAA Adoption Phase**: PHASE_B_BLOCKING — Hard gate ACTIVE
**Pre-Brief Protocol Version**: IAA_PRE_BRIEF_PROTOCOL.md v1.2.1 (ECAP-001 layer-down — present at `governance/canon/IAA_PRE_BRIEF_PROTOCOL.md`)

---

## Phase 0 Pre-Brief Mode Attestation

This invocation is in **PRE-BRIEF mode** (Phase 0). Phases 1–4 assurance are NOT executed in this
response. This artifact declares IAA's pre-wave expectations so that the producing agent
(governance-liaison-amc-agent) can deliver against them without ambiguity.

**Pre-Brief triggered by**: CS2 request in issue comment containing `[IAA PRE-BRIEF REQUEST]`.

---

## 1. Wave Scope Summary

This is a corrective follow-up wave after PR #1041 merged ECAP-001 governance artifacts into AMC
main. The artifact under correction is:

**Primary corrected artifact**: `PREHANDOVER_PROOF_session-028-20260408.md` (repo root)
> ⚠️ **Path discrepancy noted**: The issue request cites `.agent-admin/build-evidence/PREHANDOVER_PROOF_session-028-20260408.md`
> but the file exists at the repo root: `./PREHANDOVER_PROOF_session-028-20260408.md`.
> Confirmed by `git ls-tree HEAD`. Producing agent must operate on the file at the root path.
> IAA will verify against root path at Phase 3.

**Scope**: Evidence/governance artifact correction only. No production code, schema, UI,
agent contracts, canon files, or CI workflow changes. Pure evidence correction.

### Declared Corrective Actions

| ID | Item to Correct | From | To |
|----|----------------|------|-----|
| CORR-001 | `git ls-tree HEAD` block in PREHANDOVER proof | `[TO BE POPULATED AFTER COMMIT — see §4.3c sequence below]` | Actual `git ls-tree HEAD` output listing committed artifacts at merge HEAD of PR #1041 |
| CORR-002 | Commit SHA in PREHANDOVER proof | `[POPULATED AT COMMIT TIME]` | Actual commit SHA at point of corrective proof commit |
| CORR-003 | CANON_INVENTORY evidence — After count | "163 entries" (incorrect) | "Before: 160, After: 199" — confirmed: `governance/CANON_INVENTORY.json` shows `total_canons: 199` |
| CORR-004 | Sync State Evidence `alignment_method` field | `"alignment_method": "layer-down-ecap001"` | `"alignment_method": "align-governance.sh"` — confirmed: `.agent-admin/governance/sync_state.json` shows this value |

**Additionally declared by IAA as in-scope for this corrective wave** (see §5 — Governance Conflict #GC-001):
| ID | Item | Reason |
|----|------|--------|
| CORR-005 | Missing IAA token file | `PREHANDOVER_PROOF_session-028-20260408.md` declares `iaa_audit_token: IAA-session-028-wave-ecap001-layerdown-20260408-PASS` but no corresponding file `.agent-admin/assurance/iaa-token-session-028-wave-ecap001-layerdown-20260408.md` exists. CORE-016/CORE-018 require this file. IAA **will require this file to exist** at Phase 3. Producing agent must create it, OR provide evidence that the token was issued under a different file name with explicit cross-reference. |

---

## 2. Qualifying Task Trigger Classifications

### TASK-ECAP-CORR-001: Correct PREHANDOVER_PROOF_session-028-20260408.md

| Field | Value |
|-------|-------|
| `task_id` | TASK-ECAP-CORR-001 |
| `task_summary` | Populate placeholder blocks (CORR-001 through CORR-004) in `PREHANDOVER_PROOF_session-028-20260408.md` with actual committed values |
| `iaa_trigger_category` | **LIAISON_ADMIN** — PREHANDOVER proof is a governance liaison administration artifact from `governance-liaison-amc session-028-20260408`; its correction constitutes a liaison admin operation per trigger table v2.2.0 §LIAISON_ADMIN |
| `required_phases` | Phase 2 (Alignment), Phase 3 (Assurance — core invariants + LIAISON_ADMIN overlay), Phase 4 (Verdict + Token) |
| `applicable_overlays` | CORE-001 through CORE-024, OVL-LA-001 through OVL-LA-005, OVL-LA-ADM-001 through OVL-LA-ADM-003, OVL-INJ-001 |
| `specific_rules` | A-001 (invocation evidence in new corrective PREHANDOVER), A-029 (artifact immutability — CS2 authorization required), A-033 (CORE-018 uses git not disk), A-036 (invocation-discipline repeat check) |
| `qualifying` | **YES — LIAISON_ADMIN (mandatory IAA)** |
| `ambiguity_flag` | NONE — unambiguously LIAISON_ADMIN; AMBIGUITY RULE not invoked |

### TASK-ECAP-CORR-002: Create missing IAA token artifact for session-028 wave-ecap001-layerdown

| Field | Value |
|-------|-------|
| `task_id` | TASK-ECAP-CORR-002 |
| `task_summary` | Create `.agent-admin/assurance/iaa-token-session-028-wave-ecap001-layerdown-20260408.md` (or provide verifiable cross-reference to existing token file) to satisfy CORE-016/CORE-018 for the existing `iaa_audit_token` reference |
| `iaa_trigger_category` | **LIAISON_ADMIN** — assurance directory artifact; part of the same governance correction wave |
| `required_phases` | Phase 3 (CORE-016/CORE-018 verification), Phase 4 (Verdict) |
| `applicable_overlays` | CORE-016, CORE-018, CORE-019 |
| `specific_rules` | CORE-016: dedicated token file must exist; CORE-018: evidence sweep includes token file; A-029: token file architecture |
| `qualifying` | **YES — LIAISON_ADMIN** |
| `escalation_note` | If the original IAA review of ECAP-001 wave was NOT completed and no token was issued, this must be escalated to CS2 before the corrective wave proceeds. IAA cannot self-issue a retroactive token for a wave it originally reviewed. |

---

## 3. FAIL-ONLY-ONCE (FFA) Checks IAA Will Run at Handover

The following FFA checks will be applied at Phase 3 of the IAA assurance invocation for this
corrective wave. These are declared now so the producing agent can verify compliance before
invoking IAA.

| FFA Rule | Declared Check | Hard Gate? |
|----------|---------------|------------|
| **A-001** | IAA invocation evidence must be present. The **new corrective wave PREHANDOVER proof** must include an `iaa_audit_token` field pre-populated with the expected reference `IAA-session-NNN-wave-ecap001-corrective-YYYYMMDD-PASS` where NNN is the next available IAA session number. | YES — REJECTION-PACKAGE if absent |
| **A-002** | No class exceptions. Governance-liaison-amc is a liaison class agent. IAA is mandatory for all agent classes producing LIAISON_ADMIN artifacts. No exemption claim will be accepted. | YES — REJECTION-PACKAGE if exemption claimed |
| **A-003** | Ambiguity resolves to mandatory. Any uncertainty about whether this corrective evidence PR triggers IAA resolves to mandatory invocation. | YES |
| **A-029** | Artifact immutability — PREHANDOVER proof was read-only post-merge (A-029). IAA will require explicit **CS2 authorization** (documented in the corrective wave PREHANDOVER proof) to accept that modification of the post-merge PREHANDOVER artifact is intentional and authorized. The authorization reference must quote the issue number or explicit CS2 approval. Without it, IAA will issue REJECTION-PACKAGE citing A-029 violation. | YES — REJECTION-PACKAGE if authorization absent |
| **A-029b** | Carry-forward mandate. If any prior sessions have identified unresolved carry-forward items for the ECAP-001 wave, they must be listed and resolved before ASSURANCE-TOKEN is issued. | YES |
| **A-033** | CORE-018 verification must use git, not disk. IAA will verify all declared artifacts via `git ls-tree HEAD`, not `-f` filesystem check. Any file present on disk but not committed is an ENVIRONMENT_BOOTSTRAP failure. | YES — REJECTION-PACKAGE if artifacts not committed |
| **A-036** | Invocation-discipline repeat check. IAA will search last 5 session memory files for the same ENVIRONMENT_BOOTSTRAP pattern. The session-028 PREHANDOVER proof containing `[TO BE POPULATED]` placeholders at merge is a first-occurrence of a "placeholder-at-merge-time" pattern (distinct from prior A-021 uncommitted-artifacts patterns). IAA will assess whether this is a systemic pattern. | YES — systemic promotion required if pattern repeats |

---

## 4. Required PREHANDOVER Proof Structure

The producing agent (governance-liaison-amc-agent) must commit a **new** PREHANDOVER proof
for the corrective wave before invoking IAA. This proof is separate from, and must not
replace, the session-028 proof being corrected (which remains as the original record).

### Required New PREHANDOVER Proof

**File path**: `PREHANDOVER_PROOF_session-028-corrective-20260408.md` (or dated appropriately)
**Location**: Repo root (consistent with existing PREHANDOVER proof convention in this repository)

#### Mandatory Fields and Sections

| Section | Required Content |
|---------|-----------------|
| **Header** | `agent: governance-liaison-amc`, `session: session-028-corrective-YYYYMMDD`, `wave: ecap-001-corrective`, `date`, `canonical_commit: 63cdfb06586f567c456641edd7ca464c47b7751e` |
| **iaa_audit_token** | Pre-populated at commit time: `IAA-session-NNN-wave-ecap001-corrective-YYYYMMDD-PASS` (replace NNN with next available IAA session number) |
| **Phase 1 Preflight** | `phase_1_preflight: PREFLIGHT COMPLETE` — mandatory CI gate field |
| **Pre-IAA Commit-State Gate (§4.3c)** | `git status` output showing CLEAN working tree; `git ls-tree HEAD` output showing ALL corrected artifacts are committed including: (a) the corrected `PREHANDOVER_PROOF_session-028-20260408.md`, (b) this new corrective PREHANDOVER proof file, (c) the IAA token file for session-028 ecap-001 wave |
| **Actual Commit SHA** | Real SHA from `git rev-parse HEAD` at point of commit — no placeholder |
| **CS2 Authorization Record** | Explicit reference to CS2 authorization for modifying the post-merge PREHANDOVER artifact. Must cite the issue number authorizing the correction (e.g., "CS2 authorized via issue #NNNN — fix(ecap-001): resolve PREHANDOVER evidence defects"). Required by A-029. |
| **Correction Evidence Table** | Before/after for each CORR-001 through CORR-005, with actual values as committed |
| **CORR-001 Evidence** | Actual `git ls-tree HEAD` output from PR #1041 merge commit (`24dc14ff97fab4b691e5cd2b017b85c00790a6df`) listing the committed artifacts |
| **CORR-002 Evidence** | Actual commit SHA for the corrective proof commit (not the merge commit) |
| **CORR-003 Evidence** | Confirm `governance/CANON_INVENTORY.json` `total_canons: 199`; explain PR #1038 context (36 additional canon files landed before ECAP-001 wave; wave added 3 more from 160→163 on the branch, but merged state is 199) |
| **CORR-004 Evidence** | Confirm `.agent-admin/governance/sync_state.json` `alignment_method: "align-governance.sh"` (verified match to actual committed value) |
| **CORR-005 Evidence** | Either: (a) confirm IAA token file created at `.agent-admin/assurance/iaa-token-session-028-wave-ecap001-layerdown-20260408.md` with correct token content, OR (b) provide evidence that the original IAA review token is held in an existing file under a different name, with explicit cross-reference |
| **Session Memory Reference** | Path to new session memory artifact: `.agent-workspace/governance-liaison-amc/memory/session-028-corrective-YYYYMMDD.md` or equivalent |
| **Agent File Escalation Record** | Confirm no `.github/agents/*.md` files were modified |

#### What IAA Will Verify (Phase 3 Substance Checks)

Beyond the PREHANDOVER proof ceremony, IAA will verify:

1. **Substantive correctness of each correction** (primary 90% effort):
   - CORR-001: `git ls-tree HEAD` block in the corrected file matches actual `git ls-tree 24dc14f` output
   - CORR-002: Commit SHA in the corrected file corresponds to a real, reachable commit on the branch
   - CORR-003: The stated "After: 199" count matches `governance/CANON_INVENTORY.json` `total_canons: 199` (confirmed at Pre-Brief time — OK)
   - CORR-004: The `alignment_method: "align-governance.sh"` matches `.agent-admin/governance/sync_state.json` (confirmed at Pre-Brief time — OK)
   - CORR-005: Token file exists, is non-empty, and references the correct wave and verdict

2. **No substantive governance regressions**:
   - No canon files modified
   - No agent contracts modified
   - No `.governance-pack/` files modified (PROHIB-006 / OVL-LA-004)
   - No `.github/agents/` files modified

3. **CANON_INVENTORY + HANDOVER_SUMMARY + ALIGNMENT_EVIDENCE internal consistency**:
   - All three sources must agree on the count and context

---

## 5. Scope Blockers and Governance Conflicts

The following must be resolved before IAA invocation:

### SB-001 — Branch Name Discrepancy ⚠️

**Declared requested branch**: `copilot/fix-ecap-001-resolve-prehandover-evidence-defects`
**Current working branch at Pre-Brief time**: `copilot/evidence-defects-prehandover` (has initial plan commit `5874505`)

IAA requires the producing agent to confirm which branch the corrective wave will use.
IAA's Phase 2 branch-reality gate will check that all committed artifacts exist on the
actual branch being proposed for PR. Any mismatch between declared and actual branch is an
ENVIRONMENT_BOOTSTRAP failure.

**Resolution required before IAA invocation**: Confirm branch name in PREHANDOVER proof
header. IAA will verify artifacts are committed to the branch named in the PREHANDOVER proof.

### GC-001 — Missing IAA Token File (CORE-016/CORE-018 Violation in Merged State) 🚨

**Severity**: BLOCKING — IAA will issue REJECTION-PACKAGE if unresolved at invocation.

The `PREHANDOVER_PROOF_session-028-20260408.md` (as merged into main) declares:
```
iaa_audit_token: IAA-session-028-wave-ecap001-layerdown-20260408-PASS
```

Expected token file location: `.agent-admin/assurance/iaa-token-session-028-wave-ecap001-layerdown-20260408.md`
**Status**: ABSENT — file does not exist in `.agent-admin/assurance/`.

Existing session-028 token files (confirmed):
- `iaa-token-session-028-wave-amc-stage1-consolidation-20260408.md` — different wave
- `iaa-token-session-028-wave1-20260408.md` — different wave

Additionally, IAA session-028 memory records `token_reference: IAA-session-002-wave1-20260408-PASS`
which does not match the `iaa_audit_token` in the PREHANDOVER proof. This creates a
token cross-reference inconsistency that IAA cannot resolve unilaterally.

**IAA requirement**: The corrective wave MUST either:
- (a) Create `.agent-admin/assurance/iaa-token-session-028-wave-ecap001-layerdown-20260408.md` with
  token content referencing the original ASSURANCE-TOKEN for the ecap-001 wave; OR
- (b) Provide a CS2-authorized cross-reference mapping the `iaa_audit_token` in the session-028
  PREHANDOVER proof to the actual token file that was issued (if the token exists under a different
  file name and session number), with both referenced in the corrective PREHANDOVER proof.

**If the ECAP-001 wave IAA review was never completed and no token exists**: This must be escalated
to CS2 before this corrective wave proceeds. IAA cannot retroactively self-issue a token for a wave
it may have reviewed under a different session number, and cannot issue an ASSURANCE-TOKEN for the
corrective wave until the original token gap is resolved.

### GC-002 — A-029 Artifact Immutability Authorization Required ⚠️

**Severity**: BLOCKING — IAA will issue REJECTION-PACKAGE if CS2 authorization is absent.

Per A-029 (`AGENT_HANDOVER_AUTOMATION.md` v1.1.3 §4.3b), the PREHANDOVER proof is **read-only
after initial commit**. The session-028 PREHANDOVER proof was committed as part of PR #1041 and is
now in merged main. Modifying it in a corrective wave requires explicit CS2 authorization.

**Mitigating factor**: The proof itself explicitly declared placeholders as deferred:
> `[TO BE POPULATED AFTER COMMIT — see §4.3c sequence below]`

This declaration in the original proof indicates the deferred population was an expected,
documented workflow — not an unauthorized mutation. However, A-029 still requires documented
CS2 authorization to proceed with the modification in a new PR.

**IAA requirement**: The corrective wave PREHANDOVER proof must include a CS2 authorization
statement explicitly approving the modification of the post-merge artifact. A reference to
the issue number (e.g., the corrective issue) constitutes sufficient CS2 authorization
if the issue was opened by @APGI-cmy.

### GC-003 — Systemic Pattern Assessment: Placeholder-at-Merge Pattern ⚠️

**Severity**: ADVISORY at Pre-Brief — may become BLOCKING if confirmed systemic at Phase 3.

The session-028 PREHANDOVER proof was merged with TWO unfilled placeholders:
1. `[TO BE POPULATED AFTER COMMIT — see §4.3c sequence below]` in the `git ls-tree HEAD` block
2. `[POPULATED AT COMMIT TIME]` in the Commit SHA block

This is a first-occurrence of the "placeholder-at-merge-time" pattern in IAA session history
(distinct from the A-021 uncommitted-artifacts pattern seen in prior sessions). IAA will assess
at Phase 3 whether this constitutes a systemic pattern requiring upstream hardening per A-036.

**Pre-Brief declaration**: If this pattern recurs in a future session for governance-liaison-amc-agent
or any other agent, it WILL be promoted to a systemic blocker (A-036 threshold: 2 occurrences).
The producing agent is advised to add a pre-commit validation step to detect and reject `[TO BE POPULATED]`
placeholder strings before any PREHANDOVER proof commit.

---

## 6. Environment Prerequisites

Before IAA invocation, the producing agent MUST confirm:

| Prerequisite | Requirement |
|-------------|-------------|
| **Branch committed** | All corrective artifacts committed to the working branch; `git status` clean |
| **PREHANDOVER proof committed** | New corrective PREHANDOVER proof committed to HEAD (not just on disk — A-033) |
| **Corrected artifact committed** | `PREHANDOVER_PROOF_session-028-20260408.md` with all corrections committed to HEAD |
| **IAA token artifact committed** | `.agent-admin/assurance/iaa-token-session-028-wave-ecap001-layerdown-20260408.md` committed to HEAD (or equivalent per GC-001 resolution) |
| **CS2 authorization documented** | Authorization for A-029 modification included in corrective PREHANDOVER proof |
| **No `.github/agents/` changes** | Confirmed absent from diff before invocation |
| **No `.governance-pack/` changes** | Confirmed absent from diff before invocation (OVL-LA-004) |

---

## 7. Checks IAA Will NOT Apply (Scope Boundary)

The following checks are NOT applicable to this corrective wave and will be declared N/A:

| Check | Why N/A |
|-------|---------|
| CORE-001–004, CORE-008–012, CORE-012 | Agent contract YAML checks — no agent contract changes in scope |
| OVL-CG-001–005 (CANON_GOVERNANCE substance) | No canon files being created or modified |
| OVL-LA-003 (ripple inbox processed) | Ripple processing was completed in the original wave; not in scope for correction |
| CORE-024 (PRE_BUILD_STAGE sequence) | Not a PRE_BUILD_STAGE PR |
| CORE-023 (workflow integrity) | No workflow files in scope |
| A-034, A-035 (functional behaviour registry) | Not a BUILD/AAWP_MAT PR |

---

## 8. Summary Table

| Category | Value |
|---------|-------|
| Wave | ecap-001-corrective |
| Qualifying tasks | 2 (TASK-ECAP-CORR-001, TASK-ECAP-CORR-002) |
| IAA trigger category | LIAISON_ADMIN |
| IAA required | YES — MANDATORY |
| Blockers to resolve before IAA invocation | 3 (SB-001 branch name, GC-001 missing token file, GC-002 A-029 authorization) |
| Systemic blocker (active) | NONE — GC-003 is advisory pending Phase 3 assessment |
| Producing agent | governance-liaison-amc-agent |
| New PREHANDOVER proof required | YES — separate from session-028 proof being corrected |
| Adoption phase | PHASE_B_BLOCKING — hard gate active |
| Pre-Brief artifact committed | YES — this file |

---

## 9. IAA Session Readiness

IAA is ready to execute Phase 2–4 assurance once the producing agent has:
1. Resolved SB-001 (confirmed branch name)
2. Resolved GC-001 (token file created or cross-referenced)
3. Resolved GC-002 (CS2 authorization documented)
4. Committed all artifacts to HEAD with clean git status
5. Committed the new corrective PREHANDOVER proof with all required fields

Producing agent should invoke IAA by task with context: wave `ecap-001-corrective`,
branch `<confirmed branch name>`, new PREHANDOVER proof path.

---

**Authority**: CS2 (Johan Ras / @APGI-cmy)
**IAA Pre-Brief Protocol**: IAA_PRE_BRIEF_PROTOCOL.md v1.2.1
**Pre-Brief committed by**: independent-assurance-agent (Phase 0 — Pre-Brief mode)
**Adoption Phase**: PHASE_B_BLOCKING
**Version History**: 1.0.0 (2026-04-08) — initial Pre-Brief for ecap-001-corrective wave

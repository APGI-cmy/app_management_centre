# IAA Pre-Brief — wave-opojd-delivery

**Agent**: independent-assurance-agent  
**Version**: 6.2.0  
**Pre-Brief Version**: 1.0.0  
**Date**: 2026-04-08  
**Wave**: wave-opojd-delivery  
**Issue**: #1024 — Uninterrupted OPOJD delivery  
**Branch**: copilot/uninterrupted-opojd-delivery  
**Pre-Brief requested by**: foreman-v2-agent (session-020)  
**Authority**: CS2 (Johan Ras / @APGI-cmy)  
**Status**: COMMITTED — Pre-Brief artifact v1.0.0  

---

## Step 0.1 — Pre-Brief Invocation Confirmed

Invocation mode: PRE-BRIEF  
Trigger: `[IAA PRE_BRIEF REQUEST]` in wave task instruction — matches Phase 0 activation condition.  
Action: Generate Pre-Brief artifact only. Do NOT proceed to Phase 1–4 assurance.  
Wave-current-tasks.md status at read time: `IN PROGRESS — IAA Pre-Brief pending`  

---

## Step 0.2 — Wave Declaration

| Field | Value |
|-------|-------|
| `wave_id` | wave-opojd-delivery |
| `wave_session` | session-020 |
| `issue` | #1024 — Uninterrupted OPOJD delivery |
| `branch` | copilot/uninterrupted-opojd-delivery |
| `requested_by` | foreman-v2-agent |
| `delegated_to` | integration-builder |
| `iaa_prebrief_status` | PENDING → this file resolves to COMMITTED |

**Declared Tasks from wave-current-tasks.md:**

| Task ID | Description | Delegated To |
|---------|-------------|--------------|
| TASK-OPOJD-01 | Modify `.github/workflows/copilot-setup-steps.yml` — remove write-back assumptions, add COMMENT_ONLY preflight | integration-builder |
| TASK-OPOJD-02 | Create `.github/workflows/copilot-bot-automation.yml` — separate bot workflow for future automation | integration-builder |

---

## Step 0.3 — Qualifying Task Classification

### Trigger Table Application

Using `iaa-trigger-table.md` v2.2.0:

**Classification Decision Flow applied:**

1. Does PR contain any `.github/agents/` or `governance/agents/` changes?  
   → **NO** — not in this wave's scope.

2. Does PR contain any `governance/canon/` or `CANON_INVENTORY.json` changes?  
   → **NO** — not in scope.

3. Does PR contain any `.github/workflows/` changes?  
   → **YES — BOTH TASKS** modify/create `.github/workflows/` files:
   - TASK-OPOJD-01: modifies `.github/workflows/copilot-setup-steps.yml`
   - TASK-OPOJD-02: creates `.github/workflows/copilot-bot-automation.yml`
   → **Category: CI_WORKFLOW. IAA = MANDATORY.**

4–9. Further classification steps not needed — CI_WORKFLOW already triggered.

**AMBIGUITY RULE check**: No ambiguity. CI_WORKFLOW is unambiguous for both tasks.

### Task Classification Results

| Task ID | IAA Trigger Category | IAA Required? | Qualifying? |
|---------|---------------------|---------------|-------------|
| TASK-OPOJD-01 | CI_WORKFLOW | YES — MANDATORY | ✅ QUALIFYING |
| TASK-OPOJD-02 | CI_WORKFLOW | YES — MANDATORY | ✅ QUALIFYING |

**Wave classification: CI_WORKFLOW — IAA MANDATORY for all tasks in this wave.**

---

## Step 0.4 — Pre-Brief Artifact: Task-Level Declarations

---

### TASK-OPOJD-01: Modify `copilot-setup-steps.yml`

| Field | Value |
|-------|-------|
| `task_id` | TASK-OPOJD-01 |
| `task_summary` | Remove write-back token logic, remove `MATURION_BOT_TOKEN \|\| github.token` fallback from checkout, add COMMENT_ONLY preflight declarations, reduce to plain `github.token` (read-only). |
| `iaa_trigger_category` | CI_WORKFLOW |
| `required_phases` | Phase 2 (Alignment) + Phase 3 (Assurance Work) + Phase 4 (Merge Gate Parity + Verdict) |

#### Required Evidence Artifacts (TASK-OPOJD-01)

The following artifacts MUST be present and committed to the branch BEFORE IAA invocation
(per FAIL-ONLY-ONCE A-021 and §4.3b architecture):

1. **PREHANDOVER proof file** — committed, git-verified (not disk-only per A-033)
   - Must include: `iaa_audit_token` pre-populated as `IAA-session-NNN-wave-opojd-delivery-YYYYMMDD-PASS`
   - Must include: git commit SHA of each delivered artifact
   - Must include: scope declaration listing exactly the files changed
   - **Read-only after initial commit** — per A-029 / §4.3b

2. **Session memory file** — `.agent-workspace/integration-builder/memory/session-NNN-YYYYMMDD.md`
   - Must be committed before IAA invocation (A-021)

3. **YAML validation evidence** — for `.github/workflows/copilot-setup-steps.yml`
   - `actionlint` or `yamllint` clean run output included in PREHANDOVER
   - OVL-CI-005 self-referential exception MUST be explicitly invoked in PREHANDOVER
     (workflow triggers on `workflow_dispatch` only — CI cannot pre-validate before merge)
   - Three required substitutes per OVL-CI-005: (1) YAML syntax validation output,
     (2) pattern parity evidence against existing approved workflow, (3) `workflow_dispatch`
     trigger confirmed retained or added

4. **Token policy resolution statement** — inline in PREHANDOVER:
   - Explicitly addresses REQ-TU-001/002/003/004 referenced in existing workflow comments
   - Confirms that `contents: write` permission is being removed or justified
   - Confirms that `git config user.name/email` steps are being removed (no write-back)
   - Confirms the GOVERNANCE_TOKEN_USAGE_REQUIREMENTS.md policy applicability after change

#### Applicable Overlays (TASK-OPOJD-01)

- **CI_WORKFLOW overlay** (OVL-CI-001 through OVL-CI-005)
  - OVL-CI-001: Workflow policy correctness — does the modified workflow implement COMMENT_ONLY correctly?
  - OVL-CI-002: Merge gate integrity — do all required merge gate checks remain intact?
  - OVL-CI-003: Silent failure risk — no unguarded `continue-on-error` or swallowed failures
  - OVL-CI-004: Environment parity — COMMENT_ONLY mode consistent across all environments
  - OVL-CI-005: CI evidence — self-referential exception must be explicitly invoked and documented

#### Specific Rules (TASK-OPOJD-01)

| Rule | Application |
|------|-------------|
| FAIL-ONLY-ONCE A-021 | All artifacts committed and pushed BEFORE IAA invocation |
| FAIL-ONLY-ONCE A-029 | PREHANDOVER proof is read-only post-commit |
| FAIL-ONLY-ONCE A-033 | CORE-018 evidence via `git ls-tree HEAD`, not filesystem check |
| OVL-CI-005 Exception (S-033) | Self-referential workflow — three-condition substitution required |
| CORE-007 | No placeholder content — `[to be populated]` patterns must not appear |
| CORE-023 | Workflow integrity ripple check — any other workflows referencing `copilot-setup-steps` must remain valid |

---

### TASK-OPOJD-02: Create `copilot-bot-automation.yml`

| Field | Value |
|-------|-------|
| `task_id` | TASK-OPOJD-02 |
| `task_summary` | Create new `.github/workflows/copilot-bot-automation.yml` — explicit write permissions, no `github.token` fallback, fail-fast if MATURION_BOT_TOKEN unavailable, proper artifact/failure logging. |
| `iaa_trigger_category` | CI_WORKFLOW |
| `required_phases` | Phase 2 (Alignment) + Phase 3 (Assurance Work) + Phase 4 (Merge Gate Parity + Verdict) |

#### Required Evidence Artifacts (TASK-OPOJD-02)

Same PREHANDOVER/session memory ceremony as TASK-OPOJD-01 (single PR covers both tasks):

1. **PREHANDOVER proof file** — covers both tasks, committed before IAA invocation
2. **Session memory file** — same session, covers both tasks
3. **YAML validation evidence** — for `.github/workflows/copilot-bot-automation.yml`
   - `actionlint` or `yamllint` clean run output
   - Workflow is new — no pattern parity against prior version, but parity comparison against
     `copilot-push-intercept.yml` (approved, runs in production) is required per OVL-CI-005
   - `workflow_dispatch` trigger must be present (CS2 can manually validate post-merge)

4. **Fail-fast proof** — PREHANDOVER must include:
   - Workflow snippet showing `if: env.MATURION_BOT_TOKEN == ''` or `required: true` pattern
   - Confirmation that `github.token` is NOT used as a fallback for write operations
   - Failure logging / artifact upload step confirmed present

#### Applicable Overlays (TASK-OPOJD-02)

- **CI_WORKFLOW overlay** (OVL-CI-001 through OVL-CI-005) — same as TASK-OPOJD-01
  - OVL-CI-001: Does the new workflow implement its stated policy (bot automation) correctly?
  - OVL-CI-003: Silent failure risk — fail-fast on missing token; no silent continuation
  - OVL-CI-005: CI evidence — self-referential exception applies to new workflow file

#### Specific Rules (TASK-OPOJD-02)

| Rule | Application |
|------|-------------|
| FAIL-ONLY-ONCE A-021 | All artifacts committed before IAA invocation |
| FAIL-ONLY-ONCE A-029 | PREHANDOVER proof read-only post-commit |
| CORE-007 | No placeholder content in new workflow file |
| OVL-CI-003 | Fail-fast on missing MATURION_BOT_TOKEN — silent continuation = REJECTION-PACKAGE |
| OVL-CI-005 Exception (S-033) | New workflow — three-condition substitution required |

---

## Step 0.4b — Universal Core Invariants That Apply to This Wave

The following CORE checks apply to ALL CI_WORKFLOW PRs (scope: ALL or CI_WORKFLOW):

| CORE Check | Name | Relevance to This Wave |
|-----------|------|------------------------|
| CORE-005 | Governance block present | N/A for workflow files — recorded as N/A if not agent contract |
| CORE-006 | CANON_INVENTORY alignment | N/A for workflow files — recorded as N/A |
| CORE-007 | No placeholder content | YES — both modified/created workflow files and all ceremony artifacts |
| CORE-013 | IAA invocation evidence | YES — PREHANDOVER must reference IAA invocation |
| CORE-014 | No class exemption claim | YES — integration-builder is a governed class; no exemption claims |
| CORE-015 | Session memory present | YES — session memory committed before invocation |
| CORE-016 | IAA verdict evidenced (§4.3b) | YES — dedicated token file required post-verdict |
| CORE-017 | No `.github/agents/` mods by unauthorized agent | YES — this wave MUST NOT touch `.github/agents/` |
| CORE-018 | Complete evidence artifact sweep | YES — first check on invocation (git-verified) |
| CORE-019 | IAA token cross-verification | YES — first-invocation exception applies |
| CORE-020 | Zero partial pass rule | YES — all checks |
| CORE-021 | Zero-severity-tolerance | YES — any finding = REJECTION-PACKAGE |
| CORE-022 | Secret field naming | N/A — no agent contracts in this wave |
| CORE-023 | Workflow integrity ripple check | YES — other workflows must remain valid after changes |
| CORE-024 | Pre-build stage sequence | N/A — not PRE_BUILD_STAGE category |

---

## Step 0.5 — PREHANDOVER Proof Structure Required

The integration-builder MUST produce a PREHANDOVER proof with the following structure.  
Deviations from this structure will result in REJECTION-PACKAGE at assurance time.

```
# PREHANDOVER Proof — wave-opojd-delivery — integration-builder

## Wave Metadata
| Field | Value |
|-------|-------|
| wave_id | wave-opojd-delivery |
| session_id | session-NNN |
| date | YYYYMMDD |
| producing_agent | integration-builder |
| iaa_prebrief_reference | .agent-admin/assurance/iaa-prebrief-wave-opojd-delivery.md |
| iaa_audit_token | IAA-session-NNN-wave-opojd-delivery-YYYYMMDD-PASS |

## Scope Declaration
[Exact list of files modified/created — must match PR diff precisely]
- .github/workflows/copilot-setup-steps.yml — MODIFIED
- .github/workflows/copilot-bot-automation.yml — CREATED
[No other files — any additional files must be listed and justified]

## Pre-IAA Commit Gate
[Git commit SHA(s) — must be committed and pushed before IAA invocation]
| Artifact | Path | Git SHA |
|----------|------|---------|
| PREHANDOVER proof | [path] | [SHA] |
| Session memory | [path] | [SHA] |
| copilot-setup-steps.yml | .github/workflows/copilot-setup-steps.yml | [SHA] |
| copilot-bot-automation.yml | .github/workflows/copilot-bot-automation.yml | [SHA] |

## TASK-OPOJD-01 Delivery Evidence

### Changes Made (copilot-setup-steps.yml)
[Summary of every change — line-level if possible]
- [ ] Removed: `token: ${{ secrets.MATURION_BOT_TOKEN || github.token }}`
- [ ] Replaced with: `token: ${{ github.token }}` (read-only checkout)
- [ ] Removed: `contents: write` permission (no longer required)
- [ ] Removed or justified: `git config user.name/email` steps
- [ ] Removed: token identity evidence step (write-back infrastructure removed)
- [ ] Added: preflight step with COMMENT_ONLY declarations:
      - `COPILOT_SESSION_MODE=COMMENT_ONLY`
      - `PUSH_DISABLED_INTENTIONAL=true`
      - `OUTPUT_MODE=PR_COMMENT_OR_ARTIFACT`
- [ ] Confirmed: preflight step appears BEFORE MCP startup

### Token Policy Resolution (REQ-TU-001/002/003/004)
[Must address: existing workflow comments reference token policy requirements.
After this change, the workflow no longer performs write operations.
Statement: "GOVERNANCE_TOKEN_USAGE_REQUIREMENTS.md REQ-TU-001/002/003/004 are satisfied
because all write-back operations have been removed. The checkout step now uses github.token
in a read-only capacity only. No step in the modified workflow mutates repository state."]

### YAML Validation Evidence (OVL-CI-005 — self-referential exception invoked)
[Explicitly invoke OVL-CI-005 exception clause:]
"This is a self-referential workflow PR. The modified workflow triggers on workflow_dispatch
only. No CI run of the modified workflow can be produced before merge. OVL-CI-005 exception
applied per S-033. Three required substitutes provided below:"

1. YAML syntax validation output:
[Paste yamllint/actionlint output confirming 0 errors/warnings]

2. Pattern parity evidence:
[Comparison against approved equivalent workflow — differences listed and justified]

3. workflow_dispatch confirmation:
[Confirm `workflow_dispatch: {}` is present in the modified workflow's `on:` block]

## TASK-OPOJD-02 Delivery Evidence

### New Workflow Structure (copilot-bot-automation.yml)
[Summary of key structural elements]
- [ ] trigger conditions declared
- [ ] explicit write permissions (not inherited from defaults)
- [ ] MATURION_BOT_TOKEN fail-fast logic present (step fails if secret unavailable)
- [ ] NO `github.token` fallback for write operations
- [ ] artifact/failure logging step present
- [ ] `workflow_dispatch:` trigger present (for CS2 manual validation)

### Fail-Fast Evidence
[Snippet or description of the step that fails fast if MATURION_BOT_TOKEN is unavailable]

### YAML Validation Evidence (OVL-CI-005 — self-referential exception invoked)
[Same structure as TASK-OPOJD-01 — pattern parity against copilot-push-intercept.yml]

## copilot-push-intercept.yml — Unchanged Confirmation
[Explicit statement: "copilot-push-intercept.yml was not modified in this PR.
File SHA: [SHA of current file on branch — git ls-tree HEAD .github/workflows/copilot-push-intercept.yml]"]

## CORE-023 Ripple Check
[Confirm: no other workflow files reference copilot-setup-steps.yml or are impacted by changes.
If any dependent workflows exist: list them and confirm they remain valid.]

## Session Memory Reference
[Path and git SHA of session memory file]
```

**PREHANDOVER immutability**: Once committed, this proof is READ-ONLY per §4.3b / A-029.
The `iaa_audit_token` field must be pre-populated at commit time with the expected reference.
IAA will write its verdict to a **separate** dedicated token file.

---

## Step 0.5b — FAIL-ONLY-ONCE Rules Pre-Declared for This Wave

The following FAIL-ONLY-ONCE rules are particularly relevant and will be applied at assurance:

| Rule ID | Rule Name | Application |
|---------|-----------|-------------|
| A-001 | IAA invocation evidence | PREHANDOVER must reference IAA explicitly |
| A-002 | No class exemptions | integration-builder is not exempt |
| A-003 | Ambiguity → mandatory | CI_WORKFLOW is unambiguous — moot here |
| A-006 | No fabricated PHASE_A_ADVISORY tokens | Adoption phase is PHASE_B_BLOCKING |
| A-021 | Commit before invoke | All files git-verified committed BEFORE IAA invocation |
| A-029 | PREHANDOVER read-only post-commit | Token field pre-populated; IAA writes to dedicated file |
| A-029b | Carry-forward mandate | Any prior-wave leftover blockers resolved before token |
| A-033 | Git verification not disk check | CORE-018 via `git ls-tree HEAD` |

---

## Step 0.6 — Scope Blockers and Governance Conflicts

### BLOCKER-01: Token Policy Conflict (Moderate — Must Be Addressed in PREHANDOVER)

**Status**: REQUIRES RESOLUTION IN PREHANDOVER PROOF (not a hard blocker, but must be documented)

**Conflict**: The existing `copilot-setup-steps.yml` contains inline policy references:
- `# Token policy: REQ-TU-001 / REQ-TU-002 (GOVERNANCE_TOKEN_USAGE_REQUIREMENTS.md)`
- `# GITHUB_TOKEN is prohibited for any step that mutates repository state.`
- `# REQ-TU-003: Token identity evidence — must appear before any write operation.`
- `# REQ-TU-004: Explicit write permissions required for agent push operations.`

TASK-OPOJD-01 proposes switching to `github.token` only. This appears to **violate REQ-TU-001/002**
which explicitly prohibits GITHUB_TOKEN for write operations.

**Resolution path**: The issue scope states this workflow is moving to COMMENT_ONLY mode —
meaning **all write operations are removed**. If ALL write-mutating steps are removed from
`copilot-setup-steps.yml`, the REQ-TU-001/002 prohibition becomes inapplicable (no write
operations = no restriction on token type). The `contents: write` permission must also be
removed or changed to `contents: read`.

**Mandatory PREHANDOVER statement required**: integration-builder must include an explicit
token policy resolution statement in the PREHANDOVER proof confirming:
1. All write-mutating steps have been removed from the modified workflow
2. The checkout step uses `github.token` in read-only capacity only
3. REQ-TU-001/002/003/004 are satisfied (N/A after write-back removal)
4. `contents: write` permission has been removed

**If any write-mutating step REMAINS in the modified workflow with `github.token` only → 
REJECTION-PACKAGE will be issued at assurance time (OVL-CI-001 policy correctness failure).**

---

### BLOCKER-02: `workflow_dispatch` Retention on Modified Workflow (Required)

**Status**: PRE-CONDITION — integration-builder must confirm before handing over

The OVL-CI-005 self-referential exception requires `workflow_dispatch` to be retained (or
added) on the modified `copilot-setup-steps.yml`. The current workflow already has
`workflow_dispatch: {}` — this must be preserved in the modified version.

**PREHANDOVER must confirm**: `workflow_dispatch: {}` is present in the `on:` block of
`copilot-setup-steps.yml` after modification.

---

### BLOCKER-03: `copilot-bot-automation.yml` Fail-Fast Must Be Verifiable

**Status**: DESIGN REQUIREMENT — must be evident in the created workflow

The issue specifies: "Fail-fast if MATURION_BOT_TOKEN unavailable." This must be implemented
as an explicit step-level check, NOT relying on GitHub Actions' implicit secret injection
failure. The step must:
- Explicitly check for the token's presence
- Emit a clear error message naming the missing secret
- Exit with a non-zero code before any write operation is attempted

A workflow that silently continues without `MATURION_BOT_TOKEN` = OVL-CI-003 failure
(silent failure risk) → REJECTION-PACKAGE.

---

### No Architecture Conflicts Detected

- `copilot-push-intercept.yml` is explicitly in-scope as unchanged — no conflict.
- No agent contract modifications in scope — AGENT_CONTRACT trigger does not apply.
- No canon/governance files in scope — CANON_GOVERNANCE trigger does not apply.
- Red QA suite: Foreman correctly notes that automated test infrastructure for CI workflows
  is not available; validation = YAML correctness + policy review. IAA accepts this scoping.

---

## Summary Declaration

| Field | Value |
|-------|-------|
| `wave_id` | wave-opojd-delivery |
| `qualifying_tasks` | 2 (TASK-OPOJD-01, TASK-OPOJD-02) |
| `iaa_trigger_category` | CI_WORKFLOW (mandatory) |
| `adoption_phase` | PHASE_B_BLOCKING — verdicts are hard-blocking |
| `required_phases` | Phase 2 + Phase 3 + Phase 4 for each task |
| `core_checks_applicable` | CORE-007, CORE-013 through CORE-021, CORE-023 |
| `overlay_checks_applicable` | OVL-CI-001 through OVL-CI-005 |
| `fail_only_once_rules_applicable` | A-001, A-002, A-003, A-006, A-021, A-029, A-029b, A-033 |
| `scope_blockers_identified` | 3 (see Step 0.6) |
| `governance_conflicts` | 1 — token policy (BLOCKER-01) — requires resolution in PREHANDOVER |
| `pre_brief_status` | COMPLETE — ready for integration-builder to proceed |

---

**Issued by**: independent-assurance-agent  
**Pre-Brief authority**: IAA Phase 0 — does not constitute assurance verdict  
**Assurance verdict**: Issued only after PREHANDOVER proof is committed and IAA is re-invoked  
**CS2 authority**: All verdicts subject to CS2 approval (@APGI-cmy)  

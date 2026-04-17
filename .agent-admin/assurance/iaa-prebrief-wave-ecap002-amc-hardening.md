# IAA Pre-Brief — wave-ecap002-amc-hardening — AMC Implementation Hardening

**IAA Session**: IAA-20260417-PREBRIEF-WAVE-ECAP002-AMC-HARDENING
**Wave**: wave-ecap002-amc-hardening
**Date**: 2026-04-17
**Wave Task List**: `.agent-admin/waves/wave-ecap002-amc-hardening-current-tasks.md`
**Authority**: IAA_PRE_BRIEF_PROTOCOL.md v1.2.1
**Foreman Session**: session-025
**Status**: ACTIVE

---

## Wave Summary

Wave `wave-ecap002-amc-hardening` completes the AMC implementation by moving from artifact
presence only (Workstream A, already delivered in PR #1088) to live operational enforcement of
the hardened ECAP / Foreman QP / IAA admin-control stack. The wave covers three active
workstreams: **Workstream B** hardens agent contracts (execution-ceremony-admin-agent,
foreman-v2-agent, independent-assurance-agent) by adding checklist infrastructure and wiring
in §4.3e / AAP-01–AAP-09 / ACR-01–ACR-08 enforcement; **Workstream C** extends CI automation
to govern governance/templates and governance/checklists paths and automates inventory
upkeep; **Workstream D** delivers proof-of-operation artifacts demonstrating the live
3-layer admin-compliance stack in a final IAA review under the ACR regime.

---

## Qualifying Task Classification

Per `IAA_PRE_BRIEF_PROTOCOL.md v1.2.1 §Qualifying Tasks` and the IAA Trigger Table:

| Task | Description | Qualifies? | Reason |
|------|-------------|------------|--------|
| TASK-ECAP002-B1 | Create execution-ceremony-admin-checklist.md | **CONDITIONAL** | governance/checklists/ — non-canon, non-agent file. Qualifies only if co-delivered in same PR as a T1 agent contract change; per AMBIGUITY RULE, if PR scope is unclear → treated as T1. See Note-B1B3. |
| TASK-ECAP002-B2 | Create execution-ceremony-admin-reconciliation-matrix.md | **CONDITIONAL** | Same as B1. |
| TASK-ECAP002-B3 | Create execution-ceremony-admin-anti-patterns.md | **CONDITIONAL** | Same as B1. |
| TASK-ECAP002-B4 | Update execution-ceremony-admin-agent.md | **YES — T1** | `.github/agents/` file → AGENT_CONTRACT trigger → IAA MANDATORY. |
| TASK-ECAP002-B5 | Update foreman-v2-agent.md | **YES — T1** | `.github/agents/` file → AGENT_CONTRACT trigger → IAA MANDATORY. |
| TASK-ECAP002-B6 | Update independent-assurance-agent.md | **YES — T1 (SPECIAL)** | `.github/agents/` file → AGENT_CONTRACT trigger → IAA MANDATORY. However: SELF-MOD-IAA-001 and NO-SELF-REVIEW-001 prohibitions apply. IAA CANNOT assure its own contract. CS2 sign-off is required. See Note-B6. |
| TASK-ECAP002-C1 | Extend governance-artifact-enforcement.yml | **CONDITIONAL** | T4 CI workflow — IAA not required if standalone CI-only PR. If delivered in same PR as B4/B5, T1 governs and full ceremony applies to the entire PR. |
| TASK-ECAP002-C2 | Automate GOVERNANCE_ALIGNMENT_INVENTORY.json upkeep | **CONDITIONAL** | T4 CI/script — same as C1. If standalone, IAA not required. If paired with agent contract changes, T1 governs. |
| TASK-ECAP002-D1 | ECAP reconciliation summary (C1–C5 proof) | **IN-SCOPE** | Ceremony artifact reviewed by IAA during assurance. Not itself a T1/T2 deliverable, but its content and completeness are subject to ACR-01 through ACR-08 checks. |
| TASK-ECAP002-D2 | Foreman QP §14.6 checkpoint output | **IN-SCOPE** | Ceremony artifact reviewed by IAA during assurance. §14.6 checkpoint compliance is a direct IAA verification point under ACR-07. |
| TASK-ECAP002-D3 | IAA final review under ACR regime | **IAA ACTION** | This is the final assurance invocation itself. Not a deliverable subject to external IAA assurance. |

> **Note-B1B3**: Tasks B1, B2, B3 are governance/checklists/ files. If they are included in the
> same PR as B4 or B5 (agent contract changes), the PR is classified T1 and all checklist
> artifacts are reviewed as part of the T1 evidence bundle. The IAA will verify that each
> checklist is substantively complete, not a placeholder, and that agent contracts reference
> the correct paths. If B1–B3 are delivered in a standalone governance-only PR, they are T6
> (documentation) and IAA is not required — but the AMBIGUITY RULE applies: if any doubt
> about standalone vs. combined delivery exists, IAA is mandatory.

> **Note-B6**: TASK-ECAP002-B6 modifies `.github/agents/independent-assurance-agent.md`.
> This triggers IAA mandatory review per AGCFPP-001. However, per SELF-MOD-IAA-001 and
> NO-SELF-REVIEW-001, the IAA cannot self-review. Per the IAA agent contract
> `iaa_oversight.invocation_step`: "Phase 4 Step 4.4 — invoked by CodexAdvisor; IAA must
> not review its own contract changes." CS2 sign-off is required per
> `INDEPENDENT_ASSURANCE_AGENT_CANON.md §Independence Requirements` rule 4. Any PR
> modifying the IAA agent file without CS2 sign-off is auto-FAIL at the merge gate.
> The CodexAdvisor invokes a separate IAA instance; CS2 reviews the verdict directly.
> The IAA pre-brief records this constraint but cannot assure B6 independently.

---

## Per-Task Assurance Declarations

---

### TASK-ECAP002-B4 — Update execution-ceremony-admin-agent.md

| Field | Value |
|-------|-------|
| `task_id` | TASK-ECAP002-B4 |
| `task_summary` | Harden execution-ceremony-admin-agent.md to require the 3 governance/checklists/ files, enforce §4.3e compliance gate, and wire AAP-01 through AAP-09 anti-pattern checks. |
| `iaa_trigger_category` | AGENT_CONTRACT (T1) |
| `required_phases` | 1 (Preflight), 2 (Governance), 3 (Working Phase), 4 (Handover) + Phase 5 IAA Assurance |
| `required_evidence_artifacts` | See below |
| `applicable_overlays` | AGENT_CONTRACT overlay from `iaa-category-overlays.md`; AC-01 through AC-07 from `IAA_AGENT_CONTRACT_AUDIT_STANDARD.md` |
| `specific_rules` | CORE-020, CORE-021; ACR-01 through ACR-08; FAIL-ONLY-ONCE A-001, A-002; AGCFPP-001 §3–§4 |
| `notes` | Builder is CodexAdvisor-agent per wave task list. POLC boundary: CodexAdvisor builds; Foreman QP; IAA assures. |

**Required Evidence Artifacts**:

1. **Phase 1 — Preflight Proof**: `.agent-admin/evidence/preflight-proof-<PR#>.md` or equivalent PR comment. Must name CodexAdvisor-agent, cite contract version, confirm FAIL-ONLY-ONCE self-attestation, confirm OPOJD compliance.

2. **Phase 2 — Governance Proof**: Must cite `AGENT_HANDOVER_AUTOMATION.md v1.4.1` (§4.3e, AAP-01–AAP-09), `EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md v1.1.0` (§3.5–§3.9), `INDEPENDENT_ASSURANCE_AGENT_CANON.md v1.6.0` (ACR-01–ACR-08), and `AGCFPP-001`. SHA256 hashes verified against `CANON_INVENTORY.json`. Protected file handling confirmed.

3. **Phase 3 — Working Phase Proof**: Must document rationale for each contract change, specifically: (a) how §4.3e Admin Ceremony Compliance Gate is integrated into ECAP's Phase 4 sequence; (b) which of AAP-01 through AAP-09 each new contract section addresses; (c) how the 3 checklist paths are referenced and required; (d) how the ECAP_RECONCILIATION_SUMMARY template is referenced.

4. **Phase 4 — Handover Proof**: PREHANDOVER proof at `.agent-admin/prehandover/prehandover_proof*.md`. Must confirm GREEN state, OPOJD compliance, §4.3c Pre-IAA Commit-State Gate passed (git status clean, artifacts in committed HEAD), §4.3e Admin Ceremony Compliance Gate passed (0 AAP auto-fail conditions), Foreman QP §14.6 checkpoint ACCEPTED.

5. **Agent integrity baseline**: `governance/quality/agent-integrity/execution-ceremony-admin-agent.md` updated to match the new committed version. If agent-integrity update is in same PR, hash must match committed file.

**ACR Trigger Assessment** (IAA will check all):

| ACR | What IAA checks for this task |
|-----|-------------------------------|
| ACR-01 | PREHANDOVER proof, session memory, gate results, ECAP reconciliation summary all present in committed branch |
| ACR-02 | No final-state ceremony artifact declares PENDING/in-progress while another declares PASS/COMPLETE for the same artifact |
| ACR-03 | Session ID, PR number, wave reference, and version labels are consistent across all ceremony artifacts |
| ACR-04 | `governance/scope-declaration.md` FILES_CHANGED count matches actual `git diff --name-only origin/main...HEAD` count |
| ACR-05 | All SHA256 hashes declared in PREHANDOVER proof or CANON_INVENTORY match actual committed file state |
| ACR-06 | If any changed file has `layer_down_status: PUBLIC_API` in CANON_INVENTORY, ripple assessment block is present in ECAP reconciliation summary |
| ACR-07 | PREHANDOVER proof, IAA token, session memory, tracker entries, and wave record all reference the same session/wave/token coherently |
| ACR-08 | Every file path declared in ceremony artifacts resolves to a committed file on the branch |

**Rejection Triggers** (IAA will issue REJECTION-PACKAGE if any fire):

- §4.3e Admin Ceremony Compliance Gate not evidenced as run and passed before IAA invocation
- AAP-01 through AAP-09 check not evidenced in bundle
- Foreman QP §14.6 checkpoint output absent or declaring `administrative_readiness: REJECTED`
- Agent contract diff does not match the described §4.3e / AAP wiring described in Working Phase Proof
- Checklist paths (`governance/checklists/execution-ceremony-admin-checklist.md`, `-reconciliation-matrix.md`, `-anti-patterns.md`) referenced in agent contract are not committed on the branch
- ECAP_RECONCILIATION_SUMMARY template path referenced in contract does not resolve to a committed file
- Any ACR-01 through ACR-08 trigger fires

---

### TASK-ECAP002-B5 — Update foreman-v2-agent.md

| Field | Value |
|-------|-------|
| `task_id` | TASK-ECAP002-B5 |
| `task_summary` | Add §14.6 Foreman QP Admin-Compliance Checkpoint section to foreman-v2-agent.md and wire in the FOREMAN_ADMIN_READINESS_HANDBACK template requirement. |
| `iaa_trigger_category` | AGENT_CONTRACT (T1) |
| `required_phases` | 1, 2, 3, 4 + Phase 5 IAA Assurance |
| `required_evidence_artifacts` | See below |
| `applicable_overlays` | AGENT_CONTRACT overlay; AC-01 through AC-07 |
| `specific_rules` | CORE-020, CORE-021; ACR-01 through ACR-08; FAIL-ONLY-ONCE A-001, A-002; AGCFPP-001 §3–§4 |
| `notes` | Builder is CodexAdvisor-agent. B5 may be in same PR as B4; if so, evidence artifacts may be shared across both tasks in the same bundle. If separate PR, full independent ceremony applies. |

**Required Evidence Artifacts**:

1. **Phase 1 — Preflight Proof**: As per B4. If same PR, a single preflight proof naming both tasks is acceptable.

2. **Phase 2 — Governance Proof**: Must cite `FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md v1.4.0` (§14.6), `AGENT_HANDOVER_AUTOMATION.md v1.4.1`, and `AGCFPP-001`. SHA256 verification against `CANON_INVENTORY.json`.

3. **Phase 3 — Working Phase Proof**: Must document: (a) the exact §14.6 wording added to foreman-v2-agent.md and how it implements `FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md §14.6`; (b) where in the Foreman's Phase 4 sequence the checkpoint is inserted (after §4.3d, before IAA invocation, per AHA.md §4.3e sequencing); (c) how `FOREMAN_ADMIN_READINESS_HANDBACK` template is referenced and what fields it requires.

4. **Phase 4 — Handover Proof**: Must confirm: §4.3c Pre-IAA Commit-State Gate passed; §4.3e Admin Ceremony Compliance Gate passed; Foreman QP §14.6 checkpoint ACCEPTED; GREEN state; OPOJD compliance.

5. **Agent integrity baseline**: `governance/quality/agent-integrity/foreman-v2-agent.md` updated to match the new committed version.

6. **Substantive content check**: The IAA will verify that the §14.6 section added to foreman-v2-agent.md is **substantively aligned** with `FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md §14.6` — specifically:
   - Required checkpoint output fields are present (wave/job, ECAP session, checkpoint date, Foreman session, reviewed artifacts, declared exceptions, exception assessment, checkpoint verdict with `administrative_readiness: ACCEPTED | REJECTED`, `IAA invocation authorized: yes | no`).
   - The role boundary table (what QP checkpoint does vs. does not do) is wired in or referenced.
   - Non-substitution principle is stated: Foreman verifies, does not reconstruct.

**ACR Trigger Assessment**: All ACR-01 through ACR-08 apply identically to B5 as to B4 (see B4 table above).

**Rejection Triggers** (in addition to ACR-01–ACR-08):

- §14.6 section absent from the committed foreman-v2-agent.md diff
- §14.6 content does not match `FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md §14.6` required checkpoint fields
- FOREMAN_ADMIN_READINESS_HANDBACK template path not resolved in committed branch
- Foreman QP §14.6 checkpoint output for this wave not present (D2 artifact absent at assurance time)

---

### TASK-ECAP002-B6 — Update independent-assurance-agent.md (SPECIAL — CS2 SIGN-OFF REQUIRED)

| Field | Value |
|-------|-------|
| `task_id` | TASK-ECAP002-B6 |
| `task_summary` | Add ACR-01 through ACR-08 admin-ceremony rejection triggers to independent-assurance-agent.md and require ECAP reconciliation summary in Tier 3 proof bundle. |
| `iaa_trigger_category` | AGENT_CONTRACT (T1) — but see Special Status below |
| `required_phases` | 1, 2, 3, 4 + Phase 5 IAA Assurance |
| `required_evidence_artifacts` | See below |
| `applicable_overlays` | AGENT_CONTRACT overlay; AC-01 through AC-07 |
| `specific_rules` | SELF-MOD-IAA-001; NO-SELF-REVIEW-001; AGCFPP-001; ACR-01–ACR-08 |
| `notes` | **SPECIAL STATUS** — IAA CANNOT self-assure this task. See Note-B6 above and Special Handling section below. |

**⚠️ Special Handling — IAA Self-Review Prohibition**:

Per `SELF-MOD-IAA-001` and `NO-SELF-REVIEW-001`, the IAA instance assuring this wave CANNOT
review modifications to its own contract file. The following applies:

- **CodexAdvisor is the builder** (per wave task list) and produces the contract change.
- **Foreman invokes IAA** per standard protocol — however, the IAA must immediately declare
  HALT-001 if it detects it is being asked to review changes it contributed to, or if this
  is the IAA contract file modification.
- **CS2 sign-off is required** on any PR modifying `independent-assurance-agent.md` per
  `INDEPENDENT_ASSURANCE_AGENT_CANON.md §Independence Requirements rule 4`.
- **Resolution path**: (1) CodexAdvisor builds the change; (2) Foreman performs QP; (3) IAA
  is invoked by CodexAdvisor per `iaa_oversight.invocation_step`; (4) IAA confirms independence
  (it did not author the change) or declares HALT-001 if independence is violated; (5) CS2
  reviews the IAA verdict and authorizes merge directly. No PR may merge without CS2 explicit
  sign-off.

**Required Evidence Artifacts** (same structure as B4/B5 plus):

1–5. All Phase 1–4 evidence artifacts as per B4/B5.

6. **CS2 sign-off evidence**: A CS2-DIRECT-REVIEW comment on the PR or an explicit CS2 approval in the merge gate, citing the IAA contract modification and SELF-MOD-IAA-001 acknowledgement.

7. **ACR wiring substantive check**: The IAA will verify that ACR-01 through ACR-08 section added to independent-assurance-agent.md is substantively aligned with `INDEPENDENT_ASSURANCE_AGENT_CANON.md §Admin-Ceremony Rejection Triggers v1.6.0`:
   - All 8 ACR triggers are listed with their canon-defined conditions.
   - Each trigger is cross-referenced to the correct canon authority (ECAP-001 §3.x and AHA.md §4.3e reference).
   - The relationship to §4.3e (ECAP + Foreman QP layer check) vs. ACR triggers (IAA layer check) is preserved.
   - The ECAP reconciliation summary is declared as a required Tier 3 proof bundle artifact.

**Rejection Triggers** (in addition to standard):

- CS2 sign-off absent from PR for this agent contract modification
- ACR-01 through ACR-08 content does not match canon-defined conditions from INDEPENDENT_ASSURANCE_AGENT_CANON.md v1.6.0
- ECAP reconciliation summary not declared as required Tier 3 evidence artifact
- Independence declaration absent or invalid (HALT-001 applies if IAA authored any part of this change)

---

### TASK-ECAP002-B1/B2/B3 — Governance Checklists (Conditional Qualifying Tasks)

> These tasks are declared as **conditionally qualifying**. They become T1 assurance targets
> if delivered in the same PR as B4 or B5. Standalone governance-only delivery is T6.

| Field | Value |
|-------|-------|
| `task_ids` | TASK-ECAP002-B1, TASK-ECAP002-B2, TASK-ECAP002-B3 |
| `task_summary` | Create 3 governance/checklists/ files: execution-ceremony-admin-checklist.md, execution-ceremony-admin-reconciliation-matrix.md, execution-ceremony-admin-anti-patterns.md. |
| `iaa_trigger_category` | T1 (if co-PR with B4/B5) or T6 (if standalone) |
| `required_phases` | T1: 1, 2, 3, 4 + IAA Assurance (shared with B4/B5 bundle). T6: None. |
| `applicable_overlays` | AGENT_CONTRACT overlay (if T1); None (if T6 standalone). |
| `notes` | Ambiguity rule: if PR scope is unclear, treat as T1. |

**If T1 (co-PR with agent contract changes), IAA will verify substantive content**:

**B1 (execution-ceremony-admin-checklist.md)**:
- Covers all execution ceremony administration tasks in sequence
- References ECAP v1.1.0 §3 duty sections (§3.5 Final-State Normalization, §3.6 Ceremony Completeness Invariants, §3.7 Cross-Artifact Reconciliation, §3.8 Commit-State Truth Rule, §3.9 Ripple/Registry Administration)
- Includes §4.3e Admin Ceremony Compliance Gate as a mandatory checklist item
- Is not a placeholder — must be substantively populated, not a shell with TODO items

**B2 (execution-ceremony-admin-reconciliation-matrix.md)**:
- Contains a reconciliation matrix mapping ceremony artifacts to expected evidence for each column
- Covers: PREHANDOVER proof, session memory, gate results, ECAP reconciliation summary, artifact completeness table, cross-artifact consistency table, ripple assessment block
- Is substantively aligned with ACR-01 (missing artifact classes) — every artifact class in ACR-01 is present in the matrix
- Is not a placeholder

**B3 (execution-ceremony-admin-anti-patterns.md)**:
- Lists AAP-01 through AAP-09 verbatim from `AGENT_HANDOVER_AUTOMATION.md v1.4.1 §4.3e`
- Each AAP entry includes: ID, name, description, detection guidance, correction action
- AAP-01 stale-wording exemption rule (superseded pre-token proofs exempt) is correctly documented per AHA v1.4.1 amendment
- Is not a placeholder

**Rejection Triggers** (if T1 co-PR):
- Any checklist file is a placeholder (contains TODO, TBD, or fewer than 5 substantive lines)
- AAP-01 auto-fail exemption for superseded pre-token proofs is missing from B3 (canon collision risk)
- Agent contract references to checklist paths (from B4) do not match the actual committed paths of B1/B2/B3

---

### TASK-ECAP002-C1 — Extend governance-artifact-enforcement.yml (Conditional)

| Field | Value |
|-------|-------|
| `task_id` | TASK-ECAP002-C1 |
| `task_summary` | Extend governance-artifact-enforcement.yml to enforce presence of governance/templates/** and governance/checklists/** artifacts. |
| `iaa_trigger_category` | T4 CI workflow — IAA not required if standalone. T1 if co-PR with agent contracts. |
| `required_phases` | T4 standalone: Two-Phase (1, 4) + CS2 review. T1 co-PR: Full 5-phase. |
| `applicable_overlays` | CI_WORKFLOW (if standalone); AGENT_CONTRACT (if co-PR). |
| `notes` | If standalone CI PR: IAA not required per IAA canon T4. CS2 direct review or Two-Phase ceremony sufficient. If paired with any B-task in same PR: T1 governs and full IAA ceremony applies. |

**If T1 co-PR, IAA will substantively verify**:
- The workflow extension actually enforces `governance/templates/**` and `governance/checklists/**` presence, not just path mentions
- Enforcement is BLOCKING (not just warning) for required artifact classes
- The CI gate does not inadvertently trigger on non-governance files
- The GOVERNANCE_ALIGNMENT_INVENTORY.json inclusion is handled or scoped out with rationale

---

### TASK-ECAP002-C2 — Automate GOVERNANCE_ALIGNMENT_INVENTORY.json Upkeep (Conditional)

| Field | Value |
|-------|-------|
| `task_id` | TASK-ECAP002-C2 |
| `task_summary` | Create script/workflow to auto-refresh GOVERNANCE_ALIGNMENT_INVENTORY.json when governance templates or checklists are added or updated. |
| `iaa_trigger_category` | T4 CI workflow/script — IAA not required if standalone. T1 if co-PR with agent contracts. |
| `required_phases` | T4 standalone: Two-Phase (1, 4) + CS2 review. T1 co-PR: Full 5-phase. |
| `applicable_overlays` | CI_WORKFLOW (if standalone); AGENT_CONTRACT (if co-PR). |
| `notes` | If the automation script/workflow touches `.agent-workspace/*/knowledge/` files, KNOWLEDGE_GOVERNANCE trigger may also apply. |

---

### TASK-ECAP002-D1 — ECAP Reconciliation Summary (Ceremony Artifact — In-Scope at Assurance)

| Field | Value |
|-------|-------|
| `task_id` | TASK-ECAP002-D1 |
| `task_summary` | Create ECAP reconciliation summary demonstrating completion of C1 through C5 (ECAP self-normalization proof-of-operation). |
| `iaa_trigger_category` | IN-SCOPE ceremony artifact — reviewed during B4/B5 or final assurance |
| `required_phases` | Not independently T1/T2; reviewed as part of the assurance bundle for qualifying PR(s). |
| `notes` | This is the ECAP's proof-of-operation output. It is required by ACR-01 (must be present), and its content is directly checked under ACR-02 through ACR-08. |

**IAA will verify at assurance time**:
- Reconciliation summary is committed on the branch (ACR-01)
- All declared completion statuses are consistent — no PENDING alongside COMPLETE for same artifact (ACR-02)
- Session references match the ECAP session that produced the bundle (ACR-03)
- Artifact completeness table covers all ceremony artifact classes required by job tier (ACR-01, ACR-07)
- Cross-artifact consistency table is present and coherent (ACR-07)
- Ripple assessment block is present if any PUBLIC_API files were changed (ACR-06)
- All file paths in the reconciliation summary resolve to committed files (ACR-08)

---

### TASK-ECAP002-D2 — Foreman QP §14.6 Checkpoint Output (Ceremony Artifact — In-Scope at Assurance)

| Field | Value |
|-------|-------|
| `task_id` | TASK-ECAP002-D2 |
| `task_summary` | Record the Foreman QP Admin-Compliance Checkpoint output per §14.6 of FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md. |
| `iaa_trigger_category` | IN-SCOPE ceremony artifact — reviewed during final assurance (D3) |
| `required_phases` | Not independently T1/T2; reviewed as part of the Foreman's Phase 4 ceremony. |
| `notes` | Required field: `administrative_readiness: ACCEPTED`. If REJECTED, IAA must not be invoked — bundle returns to ECAP for remediation. |

**IAA will verify at assurance time**:
- Foreman QP §14.6 checkpoint output is present as committed artifact or embedded in PREHANDOVER proof (ACR-01)
- Checkpoint output contains all required fields per `FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md §14.6`:
  - Wave/Job identifier ✓
  - ECAP Session reference ✓
  - Checkpoint Date ✓
  - Foreman Session reference ✓
  - ECAP Reconciliation Artifacts Reviewed checklist ✓
  - Declared Exceptions (or "None") ✓
  - Exception Assessment ✓
  - Checkpoint Verdict with `administrative_readiness: ACCEPTED | REJECTED` ✓
  - `QP admin-compliance check completed: yes` ✓
  - `IAA invocation authorized: yes` ✓
- `administrative_readiness: ACCEPTED` (if REJECTED, IAA issues REJECTION-PACKAGE citing ACR-07 and §14.6 violation)
- `IAA invocation authorized: yes` (if no, IAA issues REJECTION-PACKAGE)
- Session reference in checkpoint matches Foreman session (ACR-03)
- Role boundary respected: Foreman verified ECAP output, did not reconstruct the bundle

---

## Ceremony Standards for All Qualifying PR(s)

### §4.3e Sequencing (BLOCKING)

The canonical Phase 4 ordering for all qualifying PRs in this wave is:

```
§4.3 Merge Gate Parity Check
→ §4.3c Pre-IAA Commit-State Gate (BLOCKING — git status clean; artifacts in committed HEAD)
→ §4.3d Scope-Declaration Parity Gate (BLOCKING — if governance/scope-declaration.md present)
→ §4.3e Admin Ceremony Compliance Gate (BLOCKING — execution-ceremony-admin-agent was appointed)
→ IAA invocation
→ §4.3b Token Update Ceremony (after IAA verdict)
→ §4.4 Compliance Check
```

**ECAP is appointed for this wave** (TASK-ECAP002-D1/D2 confirm this). Therefore §4.3e is
BLOCKING and must be passed and evidenced before IAA is invoked on any qualifying PR.

### FAIL-ONLY-ONCE Checks

- **A-001**: IAA invocation evidence must be present (PREHANDOVER proof or token referencing IAA) — enforced for every qualifying PR.
- **A-002**: No agent class exemption for IAA — Foreman, builder, ECAP agent all subject.
- **A-036**: If same ENVIRONMENT_BOOTSTRAP pattern (artifacts not in committed HEAD at invocation) appears in 2+ sessions of this wave → systemic blocker promotion required before re-acceptance.

### Wave Checklist PREHANDOVER Field

The Foreman's PREHANDOVER proof must include the `wave_checklist` block per
`IAA_PRE_BRIEF_PROTOCOL.md §Foreman Handover Gate`:

```markdown
wave_checklist:
  path: .agent-admin/waves/wave-ecap002-amc-hardening-current-tasks.md
  status: ALL_TICKED
  pre_brief_ref: .agent-admin/assurance/iaa-prebrief-wave-ecap002-amc-hardening.md
  outstanding_items: none
```

All tasks must be `[x]` (QP PASS confirmed) or `[~]` (descoped with mandatory reason) before
`wave_checklist.status: ALL_TICKED` may be declared.

---

## Declaration

The requirements listed above are the acceptance criteria the IAA will verify at handover for
wave `wave-ecap002-amc-hardening`. Meeting all criteria listed is necessary (but not
sufficient) for an ASSURANCE-TOKEN. The IAA retains intelligence-led assessment authority
and may identify additional issues discovered during review not listed here.

**Canon references applied**:
- `IAA_PRE_BRIEF_PROTOCOL.md` v1.2.1
- `INDEPENDENT_ASSURANCE_AGENT_CANON.md` v1.6.0 (ACR-01–ACR-08)
- `AGENT_HANDOVER_AUTOMATION.md` v1.4.1 (§4.3e, AAP-01–AAP-09)
- `EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` v1.1.0 (§3.5–§3.9)
- `FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md` v1.4.0 (§14.6)
- `AGCFPP-001` (Agent Contract File Protection Policy)

**IAA signature**: IAA-20260417-PREBRIEF-WAVE-ECAP002-AMC-HARDENING
**Adoption phase**: PHASE_B_BLOCKING — Hard gate ACTIVE

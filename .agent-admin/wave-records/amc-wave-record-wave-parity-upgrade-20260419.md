# AMC Wave Record — wave-parity-upgrade-20260419 — 2026-04-19

> **Template Version**: 1.0.0  
> **Authority**: CS2 (@APGI-cmy) — Issue: Complete AMC parity-upgrade wave  
> **Protocol**: AMC 90/10 Admin Protocol v1.0.0

---

## Section 1: Wave Identity

| Field | Value |
|-------|-------|
| wave_id | wave-parity-upgrade-20260419 |
| date | 2026-04-19 |
| agent | foreman-v2-agent (session-026) |
| session_id | session-026-20260419 |
| branch | copilot/complete-amc-parity-upgrade-wave |
| triggering_issue | Complete AMC parity-upgrade wave: gate-parity ownership, protected agent-file control, and assurance-path normalization |
| cs2_authorization | Issue opened and assigned by @APGI-cmy (CS2) — direct wave-start authorization |
| agents_delegated_to | CodexAdvisor-agent (TASK-PARITY-1 through TASK-PARITY-5), independent-assurance-agent (pre-brief + final assurance) |
| phase_1_preflight | PREFLIGHT COMPLETE |

---

## Section 2: Scope & Classification

| Field | Value |
|-------|-------|
| wave_verb | harden / normalize / parity-upgrade |
| classification | POLC-Orchestration — governance parity hardening wave |
| architecture_ref | governance/canon/INDEPENDENT_ASSURANCE_AGENT_CANON.md, AGENT_HANDOVER_AUTOMATION.md v1.4.1, EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md v1.1.0 |

### IAA Pre-Brief (consolidated per AMC 90/10 Admin Protocol v1.0.0)

| Field | Value |
|-------|-------|
| iaa_session | IAA-session-045-20260419-PREBRIEF |
| date | 2026-04-19 |
| authority | IAA_PRE_BRIEF_PROTOCOL.md v1.2.1 |
| foreman_session | session-026 |
| wave_task_list | `.agent-admin/waves/wave-parity-upgrade-20260419-current-tasks.md` |
| status | COMPLETE — 2026-04-19 |
| iaa_prebrief_note | Pre-Brief content consolidated into this wave record per AMC 90/10 Admin Protocol v1.0.0. No standalone iaa-prebrief-*.md file. Session memory: `.agent-workspace/independent-assurance-agent/memory/session-045-20260419.md` |
| ecap_ceremony_admin | NOT APPOINTED — standard builder wave; ECAP reconciliation C1–C5 NOT required |

---

#### PRE-BRIEF: Task Classification

> **IAA Authority**: IAA_PRE_BRIEF_PROTOCOL.md v1.2.1 | AGCFPP-001 | Adopted: PHASE_B_BLOCKING

**TASK-PARITY-1** — Update `.github/agents/foreman-v2-agent.md`
- **IAA Category**: AGENT_CONTRACT
- **IAA Triggered**: YES — mandatory per AGCFPP-001
- **Builder**: CodexAdvisor-agent (CS2-authorized; sole `.github/agents/*` write authority)
- **Substantive scope**: Add HALT-012 (gate-proof truth failure halt condition), NO-STALE-GATE-001 prohibition, explicit gate inventory requirement in final-state proof, per-gate final-state declarations (PASS/FAIL/N/A with CI evidence), PENDING=BLOCKED enforcement rule, mandatory `gate_set_checked` field in §4.3 gate parity output, RCA obligation when gate-truth failures are detected.
- **Preserve**: Existing §14.6 Foreman QP Admin-Compliance Checkpoint, HALT-001 through HALT-008, and all existing §4.3 merge-gate parity rules. New items are additive — no existing gate logic may be removed or weakened.
- **Conflict risk**: HALT-012 must not conflict with HALT-008 (no-delegation rule). Gate inventory requirement must nest cleanly inside existing §4.3 parity check flow.

**TASK-PARITY-2** — Update `.github/agents/independent-assurance-agent.md`
- **IAA Category**: AGENT_CONTRACT (own-contract modification — independence check auto-applies)
- **IAA Triggered**: YES — mandatory per AGCFPP-001
- **Builder**: CodexAdvisor-agent (CS2-authorized; IAA independence rule means IAA cannot self-modify)
- **Substantive scope**: Add ACR-09 (reject when gate set not explicitly identified in final-state proof), ACR-10 (reject when stale PENDING/in-progress gate wording remains in final-state proof), ACR-11 (reject when GREEN/PASS claimed without CI-backed gate evidence). Normalize two stale standalone pre-brief path references: YAML block line (`pre_brief_artifact_path_pattern: ".agent-admin/assurance/iaa-prebrief-wave<N>.md"`) and Phase 0 action text (`write \`iaa-prebrief-waveN.md\`, commit, reply confirming artifact path`). Both must reference wave-record-only model exclusively.
- **Preserve**: ACR-01 through ACR-08 intact. ECAP proof bundle requirements (C1–C5). Phase 0 logic otherwise unchanged — only the artifact-path instruction mutates.
- **Stale path locations identified** (verified via grep at pre-brief time):
  - YAML frontmatter: `pre_brief_artifact_path_pattern: ".agent-admin/assurance/iaa-prebrief-wave<N>.md"` → replace with wave-record section 2 reference
  - Phase 0 action: `write \`iaa-prebrief-waveN.md\`, commit, reply confirming artifact path` → normalize to wave-record-only instruction

**TASK-PARITY-3** — Update `.github/agents/CodexAdvisor-agent.md`
- **IAA Category**: AGENT_CONTRACT (own-contract modification — CodexAdvisor is the writer of its own contract per established model)
- **IAA Triggered**: YES — mandatory per AGCFPP-001
- **Builder**: CodexAdvisor-agent (CS2-authorized)
- **Substantive scope**: Add explicit sole-authority language declaring CodexAdvisor as the ONLY authorized writer of `.github/agents/*.md`. Add prohibition `NO-AGENT-FILE-WRITE-001`: no other agent may create or modify `.github/agents/*.md` files. Update `write_paths` commentary to reflect exclusive ownership. Add `AGENT_FILE_WRITE_AUTHORITY` note for CI enforcement context.
- **Existing state**: `write_paths` already includes `.github/agents/` but there is no sole-authority declaration and no prohibition barring other agents. The addition is therefore purely additive.
- **Enforceability check at final assurance**: IAA must confirm the NO-AGENT-FILE-WRITE-001 language is unambiguous — specifically that it names which agents are barred (all agents except CodexAdvisor) and that it carries `enforcement: CONSTITUTIONAL` or equivalent weight.

**TASK-PARITY-4** — Update `.github/agents/execution-ceremony-admin-agent.md`
- **IAA Category**: AGENT_CONTRACT
- **IAA Triggered**: YES — mandatory per AGCFPP-001
- **Builder**: CodexAdvisor-agent (CS2-authorized)
- **Substantive scope**: Add §4.3e enforcement language citing AAP-15 (gate set not identified) and AAP-16 (stale gate wording in final-state proof) alongside existing AAP-01–09 references. Add explicit prohibition against creating standalone `iaa-prebrief-*.md` artifacts and standalone `iaa-token-*.md` files (note: wave-record-only token model is already partially present — prohibition must be made explicit in the prohibitions block). Add explicit prohibition against direct `.github/agents/*.md` edits by ECAP.
- **Existing state**: ECAP already references AMC 90/10 wave-record-only model for tokens (verified at line 115). AAP-15/16 do not yet exist in the anti-patterns checklist and are not yet referenced in this contract.
- **Dependency**: TASK-PARITY-5a must be complete before TASK-PARITY-4 final-state can be validated — AAP-15/16 must exist in the checklist before the contract can reference them.

**TASK-PARITY-5** — Normalize Tier 2/Tier 3 artifacts (5 sub-tasks)
- **IAA Category**: CANON_GOVERNANCE (Tier 2/3 knowledge files)
- **IAA Triggered**: YES — mandatory per AGCFPP-001 (governance knowledge changes touching IAA, Foreman, and ECAP operational knowledge)
- **Builder**: CodexAdvisor-agent (CS2-authorized)
- **Sub-task breakdown**:
  - **5a** — `governance/checklists/execution-ceremony-admin-anti-patterns.md` v1.0.0 → add AAP-10 through AAP-16 (AAP-10 through AAP-14 bridge gap between AAP-09 and the new gate-parity entries; AAP-15 = gate set not identified; AAP-16 = stale gate wording in final-state proof; map to ACR-09/10/11)
  - **5b** — `.agent-workspace/independent-assurance-agent/knowledge/iaa-high-frequency-checks.md` v1.2.0 → add HFMC-07 (gate-set explicit identification); remove/deprecate legacy `iaa-prebrief-wave*.md` standalone path as active model reference in HFMC-06 note (HFMC-06 already correctly describes wave-record as sole carrier — verify note is unambiguous)
  - **5c** — `.agent-workspace/foreman-v2/knowledge/prehandover-template.md` v1.7.0 → add `gate_set_checked` field to §4.3 OPOJD gate section; remove any standalone pre-brief path instructions (note: the IAA Token Self-Certification Guard section still references `.agent-admin/assurance/iaa-token-session-*` path from pre-90/10 model — this must be reviewed and updated or annotated as deprecated)
  - **5d** — `.agent-workspace/foreman-v2/knowledge/wave-reconciliation-checklist.md` v1.0.0 → add gate inventory verification step to Section D (Evidence Completeness) or a new Section E
  - **5e** — Add grep-style non-regression validation (script or CI comment) to surface deprecated `iaa-prebrief-*.md` / `iaa-token-*.md` standalone path references if they reappear in active instructions

---

#### PRE-BRIEF: Key Substantive Focus Areas for Final Assurance

> These are the 90% review obligations. IAA must confirm each at final assurance. Ceremony-only checks are executed by CI.

**Focus 1 — ACR-09/10/11 specification correctness and non-conflict with ACR-01–08**
- Verify each new ACR has: a unique trigger condition, a distinct failure mode from existing ACR-01–08, and a consistent `classify as CEREMONY failure` verdict instruction.
- ACR-09 (gate set not identified): must not overlap with ACR-01 (missing required ceremony artifact). Distinguisher: ACR-01 = artifact absent; ACR-09 = artifact present but gate set is undeclared/implicit within it.
- ACR-10 (stale PENDING/in-progress gate wording): must not duplicate ACR-02 (stale provisional wording). Distinguisher: ACR-02 is general provisional wording; ACR-10 is gate-specific — it triggers only when gate-state fields (not general status fields) remain stale.
- ACR-11 (GREEN/PASS without CI-backed evidence): is a new class not covered by any existing ACR. Must specify what constitutes "CI-backed evidence" (e.g., link to workflow run, not self-assertion).
- **IAA must confirm at final assurance**: table in Step 3.3a covers ACR-01 through ACR-11 (not ACR-01 through ACR-08) after this change.

**Focus 2 — HALT-012 and NO-STALE-GATE-001 integration with §14.6 and §4.3**
- HALT-012 must specify: the triggering condition (gate-proof truth failure — i.e., declared gate state contradicts actual CI outcome), the action (STOP; do not release gate; escalate to CS2), and the classification (ENVIRONMENT_BOOTSTRAP or SUBSTANTIVE).
- NO-STALE-GATE-001 must be a named prohibition with: description of the banned pattern (PENDING or in-progress gate states in final-state proof), enforcement classification (CONSTITUTIONAL or BLOCKING), and reference to HALT-012 as the escalation path.
- Must NOT weaken existing §4.3 gate parity rules or introduce ambiguity in the HALT-001 through HALT-008 sequence.
- `gate_set_checked` field: must be a boolean (true/false) or explicit declaration ("ALL gates checked: [list]"), required in every §4.3 parity output.

**Focus 3 — CodexAdvisor sole-authority language enforceability**
- The prohibition must unambiguously state: all other governed agents (foreman-v2-agent, independent-assurance-agent, execution-ceremony-admin-agent, api-builder, schema-builder, qa-builder, ui-builder, integration-builder, governance-liaison-amc-agent) are barred from writing to `.github/agents/*.md`.
- Must carry explicit enforcement weight — `enforcement: CONSTITUTIONAL` in the prohibitions block, or equivalent.
- Must not create a circular dependency where CodexAdvisor updating its own contract requires CodexAdvisor to be the approver (CS2 remains merge authority per AGCFPP-001).

**Focus 4 — AAP-15/16 correspondence to ACR-09/10/11**
- AAP-15 must map cleanly to ACR-09 (gate set not identified). Detection method must specify the exact grep/inspection pattern.
- AAP-16 must map cleanly to ACR-10 (stale gate wording). Detection method must specify the exact grep pattern for gate-state fields.
- AAP-10 through AAP-14 (bridge gap entries): IAA must verify these are not placeholder entries — each must have a real condition, detection method, and resolution.
- The IAA Rejection Trigger Cross-Reference table at the end of the anti-patterns checklist must be updated to include AAP-10 through AAP-16.

**Focus 5 — Stale path removal completeness and wave-record-only consistency**
- **Two specific locations in IAA agent must be normalized** (identified at pre-brief time via grep):
  1. YAML frontmatter `pre_brief_artifact_path_pattern` field — must be updated to reference wave record Section 2
  2. Phase 0 action instruction — must remove `write \`iaa-prebrief-waveN.md\`, commit, reply confirming artifact path` and replace with wave-record embedding instruction
- **Prehandover template (5c)**: the IAA Token Self-Certification Guard section still references `.agent-admin/assurance/iaa-token-session-NNN-waveY-YYYYMMDD.md` as an active path. This predates the 90/10 Admin Protocol. The builder must either annotate these steps as applicable to pre-90/10 waves only, or replace with wave-record Section 5 equivalents.
- **HFMC-06 note** (iaa-high-frequency-checks.md): already correctly describes wave-record as sole carrier. HFMC-07 addition must be genuinely new content, not a restatement of HFMC-06.

**Focus 6 — Wave-record-only assurance model consistent enforcement**
- After this wave, the following must be true across ALL updated artifacts: no active instruction tells any agent to create a standalone `iaa-prebrief-*.md` file or standalone `iaa-token-*.md` file.
- The non-regression validation (TASK-PARITY-5e) must be operational — IAA will verify at final assurance that it surfaces the deprecated paths if they appear.
- ECAP prohibitions (TASK-PARITY-4) must be explicit, not merely implied by the existing wave-record reference.

---

#### PRE-BRIEF: ECAP Ceremony Admin Note

**No ECAP ceremony admin is appointed for this wave.** CodexAdvisor-agent is the builder; foreman-v2-agent (session-026) is the orchestrator. Standard AGENT_CONTRACT and CANON_GOVERNANCE IAA review applies. ECAP reconciliation summary (C1–C5) is **NOT required**. The §14.6 QP checkpoint DOES apply (foreman must complete C5 per §14.6 at wave close).

---

#### PRE-BRIEF: Allowed Artifact Set (Confirmed)

> IAA has verified the task list. The artifacts below are the complete expected change set. Any artifact not in this list that appears in the final PR diff must be explained in the PREHANDOVER proof.

*Workstream A — Foreman contract hardening:*
- `.github/agents/foreman-v2-agent.md` — UPDATED (add HALT-012, NO-STALE-GATE-001, gate inventory requirements, gate_set_checked field, PENDING=BLOCKED rule, RCA obligation)

*Workstream B — IAA ACR parity + path normalization:*
- `.github/agents/independent-assurance-agent.md` — UPDATED (add ACR-09/10/11; normalize two stale standalone pre-brief path references)

*Workstream C — CodexAdvisor sole-authority:*
- `.github/agents/CodexAdvisor-agent.md` — UPDATED (add sole-authority language, NO-AGENT-FILE-WRITE-001 prohibition, AGENT_FILE_WRITE_AUTHORITY note)

*Workstream D — ECAP contract parity + Tier 2/3 normalization:*
- `.github/agents/execution-ceremony-admin-agent.md` — UPDATED (AAP-15/16 enforcement, standalone assurance-path prohibition, .github/agents/* edit prohibition)
- `governance/checklists/execution-ceremony-admin-anti-patterns.md` — UPDATED (add AAP-10 through AAP-16 with detection methods and ACR cross-reference)
- `.agent-workspace/independent-assurance-agent/knowledge/iaa-high-frequency-checks.md` — UPDATED (add HFMC-07; verify HFMC-06 note is unambiguous)
- `.agent-workspace/foreman-v2/knowledge/prehandover-template.md` — UPDATED (add gate_set_checked field; address legacy iaa-token path references in IAA Token Self-Certification Guard section)
- `.agent-workspace/foreman-v2/knowledge/wave-reconciliation-checklist.md` — UPDATED (add gate inventory verification step)

*Wave administration:*
- `.agent-admin/waves/wave-parity-upgrade-20260419-current-tasks.md` — NEW ✅
- `.agent-admin/wave-records/amc-wave-record-wave-parity-upgrade-20260419.md` — this file ✅
- `.agent-workspace/foreman-v2/memory/session-026-20260419.md` — NEW (foreman session memory)
- `.agent-workspace/CodexAdvisor-agent/memory/session-NNN-20260419.md` — NEW (CodexAdvisor session memory)
- `.agent-workspace/independent-assurance-agent/memory/session-045-20260419.md` — NEW (IAA pre-brief session memory) ✅
- `.agent-workspace/independent-assurance-agent/memory/session-NNN-20260419.md` — NEW (IAA final assurance session memory — assigned at final invocation)

---

## Section 3: Evaluation Summary (QP Verdict)

| Check | Result |
|-------|--------|
| Tests 100% GREEN | ✅ N/A — governance artifact wave only |
| Zero test debt | ✅ N/A — governance artifact wave only |
| Canon cross-references consistent | PENDING |
| No placeholder content | PENDING |
| Agent contracts updated (PARITY-1 through PARITY-4) | PENDING |
| Tier 2/3 normalization (PARITY-5) | PENDING |
| Anti-patterns checklist updated (AAP-15/16) | PENDING |
| ECAP reconciliation summary | PENDING |

**QP Verdict**: PENDING

---

## Section 4: Outcome & Learning

| Field | Value |
|-------|-------|
| outcome | PENDING |
| coverage_summary | PENDING |
| learning | PENDING |

---

## Section 5: Assurance

| Field | Value |
|-------|-------|
| iaa_verdict | PENDING |
| PHASE_B_BLOCKING_TOKEN | PENDING |
| iaa_session | PENDING |
| iaa_date | PENDING |
| merge_gate_parity | PENDING |
| merge_authority | CS2 ONLY — AGCFPP-001 (agent contract changes require CS2 sign-off at merge) |

---

**Filed by**: foreman-v2-agent (session-026) | **Date**: 2026-04-19

# IAA Parking Station — Suggestions Log

| Date | Agent | Session | Phase | Summary | Filename |
|------|-------|---------|-------|---------|----------|
| 2026-04-06 | independent-assurance-agent | IAA-018 | Phase 4 | IAA contract YAML path reference for CANON_INVENTORY does not match consumer repo layout (governance/ vs .governance-pack/) — CodexAdvisor PR with CS2 auth needed | session-018-20260406.md |
| 2026-04-07 | independent-assurance-agent | IAA-019 | Phase 4 | Formalize Pre-Brief quality standard in OVL-INJ-001 guidance to require per-task check lists and BLOCKER declarations | session-019-20260407.md |
| 2026-04-07 | independent-assurance-agent | IAA-019 | Phase 4 | Audit governance-pack CANON_INVENTORY.json completeness — IAA canon not indexed (pre-existing gap OBS-019-001) | session-019-20260407.md |
| 2026-04-06 | independent-assurance-agent | IAA-018 | Phase 4 | Consider committing REJECTION-PACKAGE artifact to .agent-admin/assurance/ for complete audit trail on re-invocations | session-018-20260406.md |
| 2026-04-09 | independent-assurance-agent | session-030 | Phase 4 | Governance-liaison successive ripple events for same target file need a formal supersession mechanism (archived field in prior blocker docs) for unambiguous audit trail | session-030-20260409.md |
**Agent**: independent-assurance-agent
**Repository**: APGI-cmy/app_management_centre
**Authority**: CS2 (@APGI-cmy)

## Format
`| Date | Agent | Session | Phase | Summary | Session File |`

---

| Date | Agent | Session | Phase | Summary | Session File |
|------|-------|---------|-------|---------|--------------|
| 2026-04-06 | independent-assurance-agent | session-009-20260406 | VERDICT | CANON_INVENTORY.json absent from .governance-pack/ — systemic AMC blocker; recommend CS2 creates dedicated sync issue as prerequisite for future agent contract PRs | session-009-20260406.md |
| 2026-04-06 | independent-assurance-agent | session-009-20260406 | VERDICT | CodexAdvisor pre-existing file claims should be verified with existence check before PREHANDOVER commit | session-009-20260406.md |
| 2026-04-06 | independent-assurance-agent | session-009b-20260406 | VERDICT | CodexAdvisor must run git status + git ls-tree HEAD before invoking IAA — prevents commit-before-invocation violations (A-021) | session-009b-20260406.md |
| 2026-04-06 | independent-assurance-agent | session-009b-20260406 | VERDICT | Define minimum explicit CORE-006 waiver language template to avoid ambiguity between scope notes and explicit waivers | session-009b-20260406.md |
| 2026-04-06 | independent-assurance-agent | session-009b-20260406 | VERDICT | CANON_INVENTORY.json absence is systemic AMC blocker — CS2 should create it as platform prerequisite or issue blanket environment-bootstrap waiver | session-009b-20260406.md |
| 2026-04-08 | independent-assurance-agent | IAA-021 | Phase 3 | IAA_ZERO_SEVERITY_TOLERANCE.md needs pre-PR invocation exception clause for waiver mechanism — CS2 PR comment requirement is structurally impossible in pre-PR workflows | session-021-20260408.md |
| 2026-04-08 | independent-assurance-agent | IAA-021 | Phase 3 | FAIL-ONLY-ONCE.md version hygiene: version header, Last Updated, and history table entry must all be bumped when new A-rules are added (A-036 omitted this) | session-021-20260408.md |
| 2026-04-08 | independent-assurance-agent | IAA-021 | Phase 4 | IAA must commit session memory as final act of EVERY session including REJECTION-PACKAGE sessions — add to Phase 4 Step 4.3 as hard pre-return requirement | session-021-20260408.md |
| 2026-04-07 | independent-assurance-agent | session-020-20260407 | VERDICT | CodexAdvisor PREHANDOVER template should include mandatory Pre-IAA Commit Gate with git status + git log evidence — A-021 recurrence third time; systemic fix required per A-027 logic | session-020-20260407.md |
| 2026-04-07 | independent-assurance-agent | session-020-20260407 | VERDICT | iaa_audit_token field in PREHANDOVER template must explicitly prohibit PHASE_A_ADVISORY self-certification — A-006 fabrication pattern detected again in CodexAdvisor class agent | session-020-20260407.md |
| 2026-04-07 | independent-assurance-agent | session-021 | Phase 3 | Prehandover template needs mandatory placeholder search step before commit (grep for remaining [placeholder] text) | session-021-20260407.md |
| 2026-04-07 | independent-assurance-agent | session-021 | Phase 1 | iaa_audit_token format for re-invocations (REJECTION then re-invoke) is architecturally ambiguous — CS2 clarification needed | session-021-20260407.md |
| 2026-04-08 | independent-assurance-agent | IAA-023 | Phase 3 | governance-liaison PREHANDOVER template needs git-status pre-commit check before IAA invocation | session-023-20260408.md |
| 2026-04-08 | independent-assurance-agent | IAA-023 | Phase 1 | IAA phase (PHASE_B_BLOCKING) should ripple to governance-liaison knowledge on every IAA contract upgrade | session-023-20260408.md |
| 2026-04-08 | independent-assurance-agent | IAA-023 | Phase 3 | Clarify whether OVL-LA-ADM-003 HANDOVER_SUMMARY+ALIGNMENT_EVIDENCE requirement applies to all liaison PRs or only non-layer-down admin operations | session-023-20260408.md |
| 2026-04-08 | independent-assurance-agent | session-023 | Phase 4 | governance-liaison-amc contract should include explicit pre-IAA commit gate step (report_progress BEFORE IAA invocation) per AGENT_HANDOVER_AUTOMATION.md v1.1.5 Terminal State Rule | session-023-20260408.md |
| 2026-04-08 | independent-assurance-agent | session-023 | Phase 4 | Pre-brief requirement for layer-down sessions (OVL-INJ-001) should be documented in liaison contract Phase 4 — currently only in IAA category overlay | session-023-20260408.md |
| 2026-04-08 | independent-assurance-agent | session-023 | Phase 4 | Build-evidence bundle (OVL-LA-ADM-003) should be templated in liaison workspace PREHANDOVER guidance — new liaison agents consistently miss this ceremony step | session-023-20260408.md |
| 2026-04-08 | independent-assurance-agent | session-024 | Phase 4 | Liaison layer-down must update governance/CANON_INVENTORY.json alongside GOVERNANCE_ALIGNMENT_INVENTORY.json — both are required | session-024-20260408.md |
| 2026-04-08 | independent-assurance-agent | session-026 | systemic-fix | CANON_INVENTORY update step missing from governance-liaison layer-down protocol — systemic blocker — upstream hardening required | session-026-20260408.md |
| 2026-04-08 | independent-assurance-agent | session-026 | ceremony | PHASE_B_BLOCKING misrepresented as PHASE_A_ADVISORY in PREHANDOVER section 7 — standardise IAA invocation section language | session-026-20260408.md |
| 2026-04-08 | independent-assurance-agent | session-027 | Phase 3 | Add post-layer-down CANON_INVENTORY cross-ref against GOVERNANCE_ALIGNMENT_INVENTORY to catch inherited stale hashes from canonical source | session-027-20260408.md |
| 2026-04-08 | independent-assurance-agent | session-026 | Phase 3 | governance-liaison-amc layer-down checklist must include ripple archiving (move processed ripple-run-*.json from inbox to archive) as an explicit numbered step before IAA invocation | session-026-20260408.md |
| 2026-04-08 | independent-assurance-agent | session-026 | Phase 4 | Consider adding FAIL-GL-003 to GL FAIL-ONLY-ONCE.md: processed ripple events MUST be moved to ripple-archive before IAA invocation — if this failure recurs | session-026-20260408.md |
| 2026-04-08 | independent-assurance-agent | session-027 | Phase 4 | Add CI check: validate ripple-inbox empty after layer-down commit to prevent OVL-LA-003 re-audit cycles | session-027-20260408.md |
| 2026-04-08 | independent-assurance-agent | session-028 | Phase 4 | A-029 immutability architecture creates inherent session-number drift when REJECTION-PACKAGE forces re-invocation with new session number — add governance note to FAIL-ONLY-ONCE.md or AGENT_HANDOVER_AUTOMATION.md clarifying this is expected, not a CORE-019 failure | session-028-20260408.md |
| 2026-04-09 | independent-assurance-agent | session-029 | Phase 3 | Governance-liaison layer-down workflow must explicitly prohibit committing .github/agents/ changes — codify: detect agent file change → create escalation only → leave modification to CodexAdvisor + CS2 | session-029-20260409.md |
| 2026-04-09 | independent-assurance-agent | session-029 | Phase 3 | CORE-012 canonical defect found: CodexAdvisor-agent.md at 3166bec3 has SELF-MOD-001 enforcement: CS2_GATED not CONSTITUTIONAL — open layer-up item in maturion-foreman-governance to fix | session-029-20260409.md |
| 2026-04-09 | independent-assurance-agent | session-029 | Phase 4 | OVL-LA-003 (ripple not archived) has now appeared in sessions 026 and 029 — if it recurs, promote to FAIL-GL-003 in governance-liaison FAIL-ONLY-ONCE.md and consider CI gate | session-029-20260409.md |
| 2026-04-09 | independent-assurance-agent | session-031 | governance | Consider wave-level pre-brief for recurring governance liaison layer-down sessions to improve traceability | session-031-20260409.md |
| 2026-04-09 | independent-assurance-agent | session-031 | process | Supersession automation for DRAFT PRs when newer ripple arrives for same target file | session-031-20260409.md |
| 2026-04-09 | independent-assurance-agent | IAA-030 | Phase 4 | Add explicit §4.3c SHA-population gate to pre-brief to prevent post-merge CORR-001/002 patterns | session-030-20260409.md |
| 2026-04-09 | independent-assurance-agent | IAA-030 | Phase 4 | CANON_INVENTORY count in layer-down PREHANDOVER proofs should record both branch-state and merged-state counts | session-030-20260409.md |
| 2026-04-09 | independent-assurance-agent | IAA-030 | Phase 4 | Token file creation should be a hard pre-open gate, not a First Invocation Exception at review time | session-030-20260409.md |
| 2026-04-10 | independent-assurance-agent | session-032 | Phase 3 | CodexAdvisor Phase 4.3a Pre-IAA Commit Gate should include SCOPE_DECLARATION.md update step to prevent A-026 failures | session-032-20260410.md |
| 2026-04-10 | independent-assurance-agent | session-032 | Phase 3 | Session memory iaa_invocation_result pre-population before IAA invocation creates false state on REJECTION — needs FAIL-ONLY-ONCE rule | session-032-20260410.md |
| 2026-04-10 | independent-assurance-agent | session-032 | Phase 2 | CodexAdvisor should read latest IAA Pre-Brief artifact in Phase 2 alignment to carry-through declared required fixes | session-032-20260410.md |
| 2026-04-10 | independent-assurance-agent | session-032 | Phase 2 | Pre-invocation commit gate: mandatory `git commit` step before IAA invocation in foreman-v2-agent Phase 4 | session-032-20260410.md |
| 2026-04-10 | independent-assurance-agent | session-032 | Phase 2 | PREHANDOVER proof must be a committed file artifact, not inline invocation text | session-032-20260410.md |
| 2026-04-10 | independent-assurance-agent | session-032 | Phase 1 | "Initial plan" empty commit pattern in copilot-swe-agent creates deceptive `git diff origin/main HEAD` output — document as known pitfall in foreman-v2-agent session startup | session-032-20260410.md |
| 2026-04-10 | independent-assurance-agent | session-033 | Phase 3 | Formalize session-memory post-token First Invocation Exception in CORE-015 and CORE-018(b) to match CORE-019 precedent | session-033-20260410.md |
| 2026-04-10 | independent-assurance-agent | session-033 | Phase 3 | Plan governance-liaison-amc-agent bloat remediation wave (30,209 bytes → under 30,000) | session-033-20260410.md |
| 2026-04-10 | independent-assurance-agent | session-033 | Phase 1 | Close ECAP_UNCOMMITTED_ARTIFACTS systemic blocker in foreman Phase 4 protocol — corrective action confirmed effective session-033 | session-033-20260410.md |
| 2026-04-13 | independent-assurance-agent | session-035 | Phase 3 | Add explicit check for consumer-repo agent name correctness in can_invoke blocks (amc vs isms liaison) — substantive correctness, not ceremony | session-035-20260413.md |
| 2026-04-13 | independent-assurance-agent | session-035 | Phase 3 | Extend CORE-012 to verify SELF-MOD rule body contains escalation mechanism, not just CONSTITUTIONAL enforcement flag | session-035-20260413.md |

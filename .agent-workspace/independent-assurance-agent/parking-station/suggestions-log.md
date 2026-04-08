# IAA Parking Station — Suggestions Log

| Date | Agent | Session | Phase | Summary | Filename |
|------|-------|---------|-------|---------|----------|
| 2026-04-06 | independent-assurance-agent | IAA-018 | Phase 4 | IAA contract YAML path reference for CANON_INVENTORY does not match consumer repo layout (governance/ vs .governance-pack/) — CodexAdvisor PR with CS2 auth needed | session-018-20260406.md |
| 2026-04-07 | independent-assurance-agent | IAA-019 | Phase 4 | Formalize Pre-Brief quality standard in OVL-INJ-001 guidance to require per-task check lists and BLOCKER declarations | session-019-20260407.md |
| 2026-04-07 | independent-assurance-agent | IAA-019 | Phase 4 | Audit governance-pack CANON_INVENTORY.json completeness — IAA canon not indexed (pre-existing gap OBS-019-001) | session-019-20260407.md |
| 2026-04-06 | independent-assurance-agent | IAA-018 | Phase 4 | Consider committing REJECTION-PACKAGE artifact to .agent-admin/assurance/ for complete audit trail on re-invocations | session-018-20260406.md |
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

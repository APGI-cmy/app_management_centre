# Foreman-v2 Session Memory Template

## Template Metadata
- Version: 1.0.0
- Authority: CS2 (@APGI-cmy)
- Canon Home: APGI-cmy/maturion-foreman-governance
- Usage: Copy this template for each new session. File naming: `session-NNN-YYYYMMDD.md`

---

# Foreman-v2 Session Memory — Session [NNN] — [YYYY-MM-DD]

## Session Identity
- `session_id`: session-NNN
- `date`: YYYY-MM-DD
- `agent_version`: [from contract YAML — e.g. 6.2.0]
- `contract_version`: [from contract YAML — e.g. 2.8.0]
- `phase_1_preflight`: PREFLIGHT COMPLETE
- `fail_only_once_attested`: true
- `fail_only_once_version`: [version from FAIL-ONLY-ONCE.md — e.g. 4.1.0]
- `unresolved_breaches`: [list incident IDs or 'none']

## Invocation Context
- `triggering_issue`: "[issue number and title]"
- `wave_id`: wave-[slug]
- `branch`: [branch name]
- `cs2_authorization`: [source — issue opened by @APGI-cmy / explicit comment link]

## Classification
- `wave_verb`: [verb from request]
- `wave_classification`: [POLC-Orchestration / Implementation Guard / Quality Professor]
- `implementation_guard_triggered`: [YES — reason / NO — classification rationale]

## Prior Sessions Reviewed
- `prior_sessions_reviewed`: [list session IDs reviewed at Step 1.4, or 'none']
- `unresolved_items_from_prior_sessions`: [list, or 'none']

## Roles Invoked
- `roles_invoked`: [list all modes activated this session]
- `mode_transitions`: [list mode → mode transitions in order]

## Agents Delegated To
- `agents_delegated_to`:
  - `[agent-id]`: [task-id] — [task description]

## Work Completed This Session
[Description of wave deliverables, evidence artifacts, and their commit SHAs]

## Escalations Triggered
- `escalations_triggered`: [list by HALT/ESC id with description, or 'none']

## Separation Violations Detected
- `separation_violations_detected`: [POLC boundary violations, or 'none']

## IAA Artifacts
- `iaa_prebrief_artifact`: [path to .agent-admin/assurance/iaa-prebrief-*.md]
- `iaa_prebrief_wave`: [wave slug]
- `iaa_prebrief_tasks_count`: [N]
- `iaa_final_audit_token`: [IAA-session-NNN-waveY-YYYYMMDD-PASS, or 'N/A — planning wave']

## QP Verdicts
- [builder-or-agent]: [PASS / FAIL — brief reason]

## Suggestions for Improvement
[At least one concrete improvement suggestion. MANDATORY — a blank field is a HANDOVER BLOCKER.
If no degradation observed: "No degradation observed. Continuous improvement note: [observation]."]

## Parking Station
Append to `.agent-workspace/foreman-v2/parking-station/suggestions-log.md`:
`| YYYY-MM-DD | foreman-v2-agent | session-NNN | [type] | <summary> | <filename> |`

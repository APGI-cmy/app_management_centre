# Foreman-v2 Session Memory Template

## Template Metadata
- Version: 2.0.0
- Authority: CS2 (@APGI-cmy) — Issue #1063
- Canon Home: APGI-cmy/maturion-foreman-governance
- Usage: Copy this template for each new session. File naming: `session-NNN-YYYYMMDD.md`
- Protocol: AMC 90/10 Admin Protocol v1.0.0
- Supersedes: v1.0.0 (18+ field model — archived per Issue #1063)
- Removed Fields: agent_version, contract_version, fail_only_once_attested, fail_only_once_version, unresolved_breaches, wave_verb, wave_classification, implementation_guard_triggered, prior_sessions_reviewed, unresolved_items_from_prior_sessions, roles_invoked, mode_transitions, escalations_triggered, separation_violations_detected, iaa_prebrief_artifact, iaa_prebrief_wave, iaa_prebrief_tasks_count, iaa_final_audit_token, QP Verdicts, Parking Station
- Removal Rationale: See `governance/protocols/AMC_90_10_ADMIN_PROTOCOL.md` §3 for full detail. Ceremony fields removed; evaluation data consolidated into wave-record artifacts.

> **90/10 Principle**: Session memory captures only what is needed for real audit,
> traceability, and learning. All ceremony fields removed. Detailed wave evidence
> is recorded in the consolidated `amc-wave-record-{wave}-{date}.md` instead.

---

# Foreman-v2 Session Memory — Session [NNN] — [YYYY-MM-DD]

## Session Identity
- `session_id`: session-NNN
- `wave_id`: wave-[slug]
- `date`: YYYY-MM-DD
- `phase_1_preflight`: PREFLIGHT COMPLETE
- `triggering_issue`: "[#NNN — title]"

## Outcome
- `outcome`: [COMPLETE / PARTIAL / ESCALATED]
- `coverage_summary`: [1-2 sentences: what was delivered or evaluated this session]
- `agents_delegated_to`: [list agent-ids, or 'none']

## Learning
- `learning`: [Key lesson or improvement note — mandatory, never blank. If no degradation observed: "No degradation observed. Continuous improvement note: [observation]."]

## Wave Record Reference
- `wave_record_path`: [path to .agent-admin/wave-records/amc-wave-record-*.md, or 'N/A']

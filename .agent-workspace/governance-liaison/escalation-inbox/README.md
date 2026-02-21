# Escalation Inbox

## Purpose
Stores escalation documents for issues that require CS2 review and authorization.
Created when governance ripple events involve changes to agent contract files
(`.github/agents/*.md`) that only CS2 may authorize.

## Naming Convention
```
blocker-YYYYMMDD-{DISPATCH_ID}.md
```

## Template
```markdown
# Escalation: Agent File Change Detected

**Date**: YYYY-MM-DD
**Dispatch ID**: {dispatch_id}
**Type**: agent-file-change
**Authority Required**: CS2

## Description
Governance ripple event contains changes to agent contract files.
Per AGENT_CONTRACT_PROTECTION_PROTOCOL.md, only CS2 may authorize agent file modifications.

## Changed Agent Files
- `.github/agents/{file}.md`

## Context
- Canonical commit: {sha}
- Changed paths: {paths}
- Draft PR: #{pr_number}

## Recommendation
CS2 review and merge the draft alignment PR #{pr_number} after verifying the
agent contract changes are authorized and correct.

## References
- AGENT_CONTRACT_PROTECTION_PROTOCOL.md
- CS2_AGENT_FILE_AUTHORITY_MODEL.md
- GOVERNANCE_LIAISON_MINIMUM_APPOINTMENT_REQUIREMENTS.md
```

## Lifecycle
- **Created**: When ripple event includes `.github/agents/*.md` changes
- **Resolved**: After CS2 merges the draft PR and closes the escalation issue
- **Retention**: Permanent (audit trail for all CS2 escalations)

## Related
- Workflow: `.github/workflows/ripple-integration.yml`
- Ripple inbox: `.agent-admin/governance/ripple-inbox/`
- Memory: `.agent-workspace/governance-liaison/memory/`

---
**Authority**: AGENT_CONTRACT_PROTECTION_PROTOCOL.md, CS2_AGENT_FILE_AUTHORITY_MODEL.md  
**Living Agent System**: v6.2.0

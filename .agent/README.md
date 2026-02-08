# .agent Directory

**Purpose**: Runtime session storage for Living Agent System v5.0.0

## Structure

```
.agent/
  sessions/
    CodexAdvisor/        # CodexAdvisor session contracts
    governance-liaison/  # governance-liaison session contracts
    [other-agents]/      # Additional agent sessions as needed
```

## Session Contracts

Each agent creates session contracts when executing its Wake-Up Protocol. Session contracts document:
- Session ID and timestamp
- Mission/task being executed
- Governance context
- Alignment actions performed
- Outcome and status

## Git Ignore

The `sessions/` subdirectory is ignored by git (via .gitignore) as it contains runtime session state that should not be committed to the repository.

## Authority

Living Agent System v5.0.0 | TIER_0_CANON_MANIFEST.json

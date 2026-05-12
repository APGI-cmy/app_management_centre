# Startup Parity Evidence — wake-up-protocol.sh foreman-v2

**PR**: Phase 0 — copilot/align-amc-with-execution-model-again  
**Issue**: #1172  
**Date**: 2026-05-12  
**Agent**: foreman-v2-agent  
**Evidence type**: Direct execution proof — startup parity fix verification  

---

## Fix Summary

**Root cause**: `.github/scripts/wake-up-protocol.sh` had two fallback patterns:
- `${AGENT_ID}-v2.md` → resolves to `.github/agents/foreman-v2-v2.md` (does not exist)
- `${AGENT_ID}.md` → resolves to `.github/agents/foreman-v2.md` (does not exist)

Neither matched the actual agent file `.github/agents/foreman-v2-agent.md` (AMC `-agent` suffix convention).

**Fix applied** (commit `9415beae`):

Added third fallback in `.github/scripts/wake-up-protocol.sh`:

```bash
elif [ -f ".github/agents/${AGENT_ID}-agent.md" ]; then
  CONTRACT_FILE=".github/agents/${AGENT_ID}-agent.md"
```

Error message updated:
```
Expected: .github/agents/${AGENT_ID}-v2.md, .github/agents/${AGENT_ID}.md, or .github/agents/${AGENT_ID}-agent.md
```

---

## Direct Execution Evidence

**Command**: `.github/scripts/wake-up-protocol.sh foreman-v2`  
**Timestamp**: 2026-05-12T07:21:54Z  
**Exit code**: 0 (SUCCESS)

```
======================================================================
📋 WAKE-UP PROTOCOL - Living Agent System v6.2.0
======================================================================

Agent: foreman-v2
Timestamp: 20260512T072154Z

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phase 1: Self-Identification
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 Reading agent identity...
✅ Identity loaded: .github/agents/foreman-v2-agent.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phase 2: Memory Scan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 Scanning session memories...
✅ Found 5 recent session(s)

Most recent sessions:
session-038-20260512.md
session-037-20260505.md
session-036-20260428.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phase 3: Governance Discovery
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 Loading governance canon...
✅ Governance canon loaded (6 entries)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phase 4: Environment Health Check
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔧 Checking environment health...
✅ Evidence directories exist
✅ lessons-learned.md exists
✅ patterns.md exists

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phase 5: Working Contract Generation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 Generating working contract...
✅ Working contract generated
   Location: .agent-workspace/foreman-v2/working-contract.md
   Status: ACTIVE (ephemeral)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Wake-Up Protocol Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Phase 1: Self-Identification COMPLETE
✅ Phase 2: Memory Scan COMPLETE (5 sessions)
✅ Phase 3: Governance Discovery COMPLETE
✅ Phase 4: Environment Health Check COMPLETE
✅ Phase 5: Working Contract Generation COMPLETE

======================================================================
✅ WAKE-UP PROTOCOL COMPLETE
======================================================================

Agent foreman-v2 is ready for execution.
Working contract: .agent-workspace/foreman-v2/working-contract.md

Next: Execute task, then run session-closure.sh at session end
```

---

## Key Verification

| Check | Result |
|-------|--------|
| Script resolves `.github/agents/foreman-v2-agent.md` | ✅ `Identity loaded: .github/agents/foreman-v2-agent.md` |
| Script exits 0 (no error) | ✅ Exit code: 0 |
| Memory scan reaches 5 sessions | ✅ `Found 5 recent session(s)` |
| Governance canon loads | ✅ `Governance canon loaded (6 entries)` |
| Wake-up protocol completes all 5 phases | ✅ `WAKE-UP PROTOCOL COMPLETE` |

---

**Evidence recorded by**: foreman-v2-agent  
**Session**: session-038  
**Authority**: CS2 (@APGI-cmy) — Issue #1172 required adjustment 3

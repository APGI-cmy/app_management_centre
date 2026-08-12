# Agent Bootstrap Fallback Instructions (Issue #1228 Phase 1)

**Authority:** CS2 (@APGI-cmy) — Issue #1228, fallback path precedent Issue #1226

## Overview

This document provides approved fallback instructions for agents when the `agent-bootstrap` MCP server is **unavailable** in the current runtime (e.g., ChatGPT Work Mode without MCP support).

The fallback path is fully sanctioned by CS2 and requires **Phase 1 attestation** before proceeding with work.

---

## When to Use This Fallback

Use this fallback **only when:**

1. The detection module reports MCP unavailability
2. The issue/PR comment explicitly references this fallback
3. You cannot call the `agent_bootstrap` MCP tool

**Do not use this fallback if the MCP tool is available.** Always prefer the direct MCP call.

---

## Fallback Workflow

### Step 1: Fetch Your Agent Contract (Direct File Read)

Your agent contract is stored in `.github/agents/<agent-id>.md`.

**Location:** `.github/agents/<AGENT_ID>.md`

**Example paths:**
- `.github/agents/ui-builder.md`
- `.github/agents/api-builder.md`
- `.github/agents/foreman-v2-agent.md`

**Action:** Open the file and read the **entire contract** in full before proceeding.

---

### Step 2: Complete Phase 1 (Identity & Preflight)

Every agent contract is structured with the following phases:

- **Phase 1: Identity & Preflight** ← You are here
- **Phase 2: Governance Alignment** (read if instructed)
- **Phase 3: Builder/QA Activation** (apply only if your role requires it)

**Read and complete Phase 1 fully:**

1. Understand your role and responsibilities
2. Note any mandatory prerequisites or blockers
3. Confirm you are authorized to work on the assigned scope
4. Identify your escalation path (usually CS2)
5. Document any questions for the governance liaison

---

### Step 3: File Phase 1 Attestation

Once Phase 1 is complete, you **must** file a Phase 1 attestation comment in the issue/PR.

**Attestation Template (copy and fill in below):**

```markdown
## ✅ Phase 1 Attestation (Fallback Path — Issue #1228)

**Agent:** <agent-id>  
**Contract Location:** `.github/agents/<agent-id>.md`  
**Attestation Date:** <ISO8601 timestamp>  
**Phase 1 Status:** COMPLETE

### Phase 1 Checklist
- [ ] Read agent contract Phase 1 in full
- [ ] Confirmed role and responsibilities
- [ ] Noted all prerequisites and blockers
- [ ] Identified escalation path (CS2 or governance liaison)
- [ ] No unresolved conflicts with current work assignments
- [ ] Ready to proceed with Phase 2 (if applicable)

**Notes:**
(Document any Phase 1 findings or questions here)

---
**Authority:** Phase 1 Attestation under Issue #1226 precedent (approved fallback path).
This attestation fulfills MCP bootstrap requirement when MCP server is unavailable.
```

---

### Step 4: Proceed with Work

Once your Phase 1 attestation is filed:

1. Ensure your PR includes the required Phase 1 preflight evidence (see the `preflight/phase-1-evidence` required check)
2. CS2 governance (QP—Quality Partner) may review the attestation post-facto
3. Proceed with work only after the required CI checks pass
4. Treat attestation as a binding commitment to Phase 1 findings

---

## Stop Conditions (Escalate to CS2 Immediately)

**Do not proceed if any of the following apply:**

- [ ] Contract Phase 1 instructs you to escalate or stop
- [ ] You discover a conflict with an existing assignment
- [ ] Contract lists a blocker that has not been cleared by CS2
- [ ] You cannot confirm your role or authorization
- [ ] The issue/PR lacks the required fallback instruction comment
- [ ] More than 24 hours have passed since the issue/PR was opened (stale context)

**Escalation:** File a comment in the issue/PR with the `@CS2` mention and describe the blocker.

---

## Compliance & Governance

**POLC Violation Risk:** Skipping Phase 1 (by either MCP or fallback path) is a **GOV-BREACH-AIMC-W5-002** violation.

- If MCP available: Call `agent_bootstrap` and complete Phase 1
- If MCP unavailable: Use this fallback path + file attestation
- **Both paths satisfy the requirement.** Choose based on your runtime capability.

**Merge Gate Enforcement:**
- CI will detect which path was used (MCP vs. fallback)
- Fallback attestations are logged for CS2 post-facto review
- PR is not blocked if fallback attestation is present and valid

---

## Troubleshooting

### "I cannot find my agent contract"

1. Confirm your agent ID from the issue/PR comment
2. Check `.github/agents/<agent-id>.md` exists in the repo
3. If missing, file a comment mentioning `@CS2` — contract may not be published yet

### "Phase 1 instructs me to escalate"

Follow the escalation path in your contract. Do not bypass it.
Escalate to CS2 (`@CS2` mention) or the governance liaison listed in Phase 1.

### "I already called agent_bootstrap in another session"

Good! Your Phase 1 is already complete. You don't need to file attestation again.
Reference your previous attestation (session ID / date).

### "The fallback instructions feel wrong"

This is a governed document. Changes require CS2 approval.
If you discover an issue, file it in the issue/PR with clear reasoning.

---

## Authority & References

- **Issue #1228:** Agent Bootstrap Operationalisation (Phase 1)
- **Issue #1226:** Approved fallback path precedent
- **MCP Config:** `.mcp.json` (agent-bootstrap server registration)
- **Agent Contracts:** `.github/agents/` (all agent Phase 1 definitions)
- **Governance:** POLC violation reference GOV-BREACH-AIMC-W5-002

---

**Last Updated:** 2026-08-11  
**Authority:** CS2 (@APGI-cmy)  
**Status:** Active (Phase 1 ready)

# CS2 ESCALATION — Agent Contract Files — Layer-Down b54d57b5

**Type**: AUTHORITY_BOUNDARY  
**Severity**: BLOCKER (PROHIB-002)  
**Date**: 2026-04-08  
**Session**: session-002-20260408  
**Agent**: governance-liaison-amc  
**Escalation Class**: Agent file modification requires CS2 + CodexAdvisor authorization

---

## Summary

During layer-down for canonical commit `b54d57b5864a4df67f5bc44323ebde3807192c39`, three
`.github/agents/*.md` files were identified as changed in the canonical source. Per PROHIB-002
(constitutional lock), governance-liaison-amc is prohibited from modifying `.github/agents/*.md`
files. These files require CS2 + CodexAdvisor authorization.

---

## Files Requiring CS2 Authorization

The following files changed in canonical source at commit `b54d57b5` and have NOT been
propagated to this repository:

| File | Status | Reason |
|------|--------|--------|
| `.github/agents/CodexAdvisor-agent.md` | PENDING CS2 | PROHIB-002 — agent file |
| `.github/agents/foreman-v2.agent.md` | PENDING CS2 | PROHIB-002 — agent file |
| `.github/agents/governance-repo-administrator-v2.agent.md` | PENDING CS2 | PROHIB-002 — agent file |

---

## Files Propagated (Non-Agent)

| File | Action | Old Version | New Version | SHA256 (new) |
|------|--------|-------------|-------------|--------------|
| `governance/canon/AGENT_HANDOVER_AUTOMATION.md` | UPDATED | 1.1.5 | 1.2.0 | 84b120c7b199... |

---

## Issue Instructions

The layer-down issue states:

> "CS2 APPROVAL REQUIRED: Agent contract files changed. Ripple PR must be DRAFT. Only CS2 may merge."

This PR has been opened as DRAFT. CS2 must review and merge.

---

## Action Required from CS2

1. Review the three agent contract files changed in canonical source at commit b54d57b5:
   - `.github/agents/CodexAdvisor-agent.md`
   - `.github/agents/foreman-v2.agent.md`
   - `.github/agents/governance-repo-administrator-v2.agent.md`
2. Authorize CodexAdvisor to propagate those files (per AGCFPP-001 §3–§4)
3. Merge the DRAFT PR after review

---

## Constitutional Reference

- **PROHIB-002**: "No modification of any .github/agents/*.md file. All agent file changes require CS2 + CodexAdvisor authorization."
- **AGCFPP-001**: Agent Contract File Protection Policy — all `.github/agents/` modifications require CodexAdvisor + IAA audit

---

**Status**: OPEN — awaiting CS2 authorization  
**Escalated by**: governance-liaison-amc (session-002-20260408)

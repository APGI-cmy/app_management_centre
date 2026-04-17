# execution-ceremony-admin-agent — Tier 2 Knowledge Index

**Agent**: execution-ceremony-admin-agent
**Contract version**: 1.0.0
**Updated**: 2026-04-13
**Purpose**: Tier 2 knowledge index for execution-ceremony-admin-agent — administrator-class ceremony bundle specialist

---

## Reference Documents

The following 7 documents are the binding knowledge references for this agent:

| # | Document | Location | Purpose |
|---|---|---|---|
| 1 | Agent contract | `.github/agents/execution-ceremony-admin-agent.md` | Binding contract — governing procedure for all Phase 1–4 operations |
| 2 | ECAP-001 protocol | `governance/canon/EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` | Role model — defines the three-role split and ceremony administration obligations |
| 3 | Foreman contract | `.github/agents/foreman-v2-agent.md` | IAA invocation authority — Foreman's contract defines the handback interface and delegation brief requirements |
| 4 | IAA contract | `.github/agents/independent-assurance-agent.md` | Assurance gate authority — IAA is the sole party authorised to write token files and assurance verdicts |
| 5 | Artifact taxonomy | `governance/canon/GOVERNANCE_ARTIFACT_TAXONOMY.md` | Prescriptive allowlist — classifies all governance artifacts and defines write-path authority |
| 6 | PREHANDOVER template | `.agent-workspace/foreman-v2/knowledge/prehandover-template.md` | Template for PREHANDOVER proof assembly in Phase 3 Step 3.3 |
| 7 | Session memory template | `.agent-workspace/foreman-v2/knowledge/session-memory-template.md` | Template for session memory assembly in Phase 3 Step 3.4 |

---

## Role Boundary Summary

This agent is **administrator-class only**:

- **Does**: PREHANDOVER proof assembly, session memory assembly, evidence collation, commit-state hygiene verification
- **Does NOT**: invoke IAA, issue readiness verdicts, approve readiness, write IAA token files, build or implement anything

The three-role split is invariant:
- **Foreman**: substantive supervisory authority
- **execution-ceremony-admin-agent**: administrative bundle preparation only
- **IAA**: independent assurance gate, binary verdict only

---

## Write Paths (per contract §scope.write_paths)

| Path | Purpose |
|---|---|
| `.agent-workspace/execution-ceremony-admin-agent/` | All ECAP admin artifacts (bundles, knowledge, memory) |

---

## Governance Authority Chain

- **CANON_INVENTORY**: `.governance-pack/CANON_INVENTORY.json`
- **Canon Home**: `APGI-cmy/maturion-foreman-governance`
- **This copy**: consumer (AMC)
- **Authority**: CS2 (@APGI-cmy)

---

*This index is a living document. Update when new knowledge files are added.*
*Authority: CS2 (@APGI-cmy) | execution-ceremony-admin-agent Tier 2 Knowledge*

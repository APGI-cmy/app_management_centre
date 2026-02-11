# Foreman Agent - Lessons Learned

This file captures cumulative lessons learned across all foreman agent sessions. Entries are chronological and never removed.

---

## Session 20260211 (Session 001)

### Lesson: Always Reference Canonical Source for Agent Contracts
- Context: When working with agent contract files (.agent.md)
- Pattern: Local contract drifts from canonical gold standard over time
- Action: MUST fetch and diff against canonical source before any contract modification
- Evidence: 138-line local vs 432-line canonical = massive structural drift
- Prevention: Weekly canonical comparison checks, pre-commit validation hooks

### Lesson: YAML Frontmatter Structure Signals Contract Maturity
- Context: Reviewing or updating agent contract YAML frontmatter
- Pattern: Required fields and structure evolve with Living Agent System versions
- Action: Validate presence of: id, class, version, contract_version, execution_identity, prohibitions, metadata
- Evidence: Missing contract_version, execution_identity, prohibitions in non-compliant version
- Prevention: YAML schema validation before merge

### Lesson: Embedded Protocols Are Mandatory, Not Optional
- Context: Creating or updating agent contracts
- Pattern: Session Memory Protocol, Evidence Artifact Bundle Automation are required content
- Action: Use content completeness checklist; verify all embedded protocol sections present
- Evidence: Local contract missing Session Memory Protocol, Evidence Bundle bash script, Memory Rotation specs
- Prevention: Template-based validation; automated section presence checking

### Lesson: Consumer Mode vs Canonical Home Distinction is Critical
- Context: Determining repository scope in agent contracts
- Pattern: Canonical contracts specify canonical_home in metadata; consumer repos reference canonical
- Action: Consumer repos should NOT replicate full canonical contract; should reference canonical governance
- Evidence: scope.repository field mismatch (consumer vs canonical)
- Prevention: Clear metadata.this_copy field ("canonical" or "consumer_reference")

### Lesson: Contract Drift Accumulates Through Incremental Changes
- Context: Making small edits to agent contracts over time
- Pattern: Each small change without canonical comparison increases drift
- Action: Prefer complete replacement over incremental edits when drift detected
- Evidence: 138 → 432 line change required complete rewrite
- Prevention: Monthly full-diff audits against canonical source

### Lesson: Zero Test Debt Enforcement Requires Prominence
- Context: Emphasizing critical foreman responsibilities in contract
- Pattern: Core mandates (zero test debt, never write code) must be visually prominent
- Action: Include dedicated sections for critical invariants and enforcement policies
- Evidence: Canonical has "Zero Test Debt Enforcement" and "Critical Invariant" sections
- Prevention: Template enforcement; visual prominence checklist

### Lesson: Version Fields Must Track Both System and Contract
- Context: Maintaining version information in agent contracts
- Pattern: Living Agent System version (6.2.0) separate from contract iteration (2.0.0)
- Action: ALWAYS include both version and contract_version in YAML
- Evidence: Local had only version: 2.0.0; canonical has version: 6.2.0 + contract_version: 2.0.0
- Prevention: YAML schema requires both fields

### Lesson: Execution Identity and Prohibitions are Non-Negotiable
- Context: Defining agent operating boundaries and authentication
- Pattern: All agents need execution_identity (token, write method) and explicit prohibitions list
- Action: Verify execution_identity and prohibitions sections present in every agent contract
- Evidence: Local contract missing both sections entirely
- Prevention: Contract template validation; merge gate requirement

### Lesson: Evidence-First RCA After Compliance Failures
- Context: Responding to governance compliance failures
- Pattern: When non-compliance detected, trigger learning loop with RCA before remediation
- Action: Document root causes, contributing factors, corrective actions, and future guardrails
- Evidence: This session memory file captures complete RCA and learning protocol
- Prevention: Make RCA mandatory step in compliance failure response

### Lesson: Agent Workspace Structure Supports Memory System
- Context: Establishing agent memory and learning infrastructure
- Pattern: memory/ (rotated sessions), personal/ (cumulative lessons), escalation-inbox/ (blockers)
- Action: Create full workspace structure at agent initialization
- Evidence: Created .agent-workspace/foreman/{memory,personal,escalation-inbox}
- Prevention: Automated workspace setup in agent initialization scripts

---

**Authority**: LIVING_AGENT_SYSTEM.md v6.2.0  
**Maintained**: Continuously (never remove lessons)  
**Purpose**: Prevent recurring governance and compliance failures

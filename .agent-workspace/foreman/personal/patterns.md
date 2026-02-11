# Foreman Agent - Patterns

This file captures recurring patterns observed during foreman agent operations. Patterns help detect and respond to common situations.

---

## Pattern: Agent Contract Structural Drift
- Observed: 2026-02-11 (Session 001)
- Context: When local agent contract file diverges from canonical gold standard
- Symptoms:
  - Line count variance >10% from canonical
  - Missing YAML frontmatter fields (contract_version, execution_identity, prohibitions)
  - Absent embedded protocols (Session Memory, Evidence Artifact Bundle)
  - Consumer-mode keys present in canonical agent contracts
- Root Cause: Incremental edits without canonical comparison
- Response:
  1. Fetch canonical version from governance repository
  2. Perform full diff (line-by-line comparison)
  3. If drift >20%, prefer complete replacement over incremental fixes
  4. Document RCA in session memory
  5. Update lessons-learned with prevention measures

## Pattern: YAML Frontmatter Evolution Lag
- Observed: 2026-02-11 (Session 001)
- Context: Living Agent System version upgrades introduce new required YAML fields
- Symptoms:
  - Missing version or contract_version fields
  - Outdated class names (e.g., "foreman" instead of "supervisor")
  - Missing metadata section (canonical_home, this_copy, authority)
  - Missing execution_identity or prohibitions sections
- Root Cause: Local contracts not updated when Living Agent System evolves
- Response:
  1. Check Living Agent System version in canonical contract
  2. Validate all required YAML fields for that version
  3. Update local contract to match canonical YAML structure
  4. Add YAML schema validation to CI pipeline
  5. Document version-specific requirements in lessons-learned

## Pattern: Missing Embedded Operational Protocols
- Observed: 2026-02-11 (Session 001)
- Context: Agent contracts require embedded protocols for session memory, evidence, and automation
- Symptoms:
  - No "Session Memory Protocol" section with markdown template
  - No "Evidence Artifact Bundle Automation" section with bash script
  - No "Memory Rotation" specifications
  - No "Escalations" protocol section
  - Missing execution checklists and critical invariants
- Root Cause: Content compression during simplification or manual editing
- Response:
  1. Compare section headings against canonical contract
  2. Verify presence of all mandatory protocol sections
  3. Ensure bash scripts and templates are complete (not truncated)
  4. Add content completeness validation to merge gates
  5. Use canonical contract as reference template

## Pattern: Consumer vs Canonical Repository Confusion
- Observed: 2026-02-11 (Session 001)
- Context: Determining whether agent contract represents canonical or consumer instance
- Symptoms:
  - scope.repository points to consumer repo in canonical contract structure
  - metadata.this_copy missing or incorrect
  - Consumer-mode keys (ripple, memory paths) in canonical contract
  - Canonical-mode keys (execution_identity for canonical repo) in consumer contract
- Root Cause: Unclear repository role or copying canonical contract without adaptation
- Response:
  1. Check metadata.canonical_home and metadata.this_copy fields
  2. Verify scope.repository matches actual repository context
  3. Consumer repos should reference canonical via governance.canon_inventory
  4. Canonical repo should include execution_identity and full operational protocols
  5. Document repository role explicitly in contract frontmatter

## Pattern: Version Field Ambiguity
- Observed: 2026-02-11 (Session 001)
- Context: Distinguishing Living Agent System version from agent contract version
- Symptoms:
  - Only single version field present
  - Unclear whether version refers to system or contract iteration
  - Version number doesn't match canonical (2.0.0 vs 6.2.0)
- Root Cause: Lack of contract_version field in YAML frontmatter
- Response:
  1. Add both version (system baseline) and contract_version (contract iteration)
  2. System version tracks Living Agent System release (e.g., 6.2.0)
  3. Contract version tracks agent-specific contract iterations (e.g., 2.0.0)
  4. Document versioning semantics in contract Versioning Notes section
  5. Enforce both fields in YAML schema validation

## Pattern: Critical Invariants Not Prominent
- Observed: 2026-02-11 (Session 001)
- Context: Core foreman responsibilities must be visually and structurally prominent
- Symptoms:
  - "Foreman NEVER writes production code" buried in text
  - Zero test debt enforcement not in dedicated section
  - Critical prohibitions scattered across document
  - No execution checklist for session start/end
- Root Cause: Content organization prioritizes comprehensiveness over prominence
- Response:
  1. Create dedicated "Zero Test Debt Enforcement" section
  2. Add "Critical Invariant" statements in bold/prominent formatting
  3. Include "Execution Checklist" near top of document
  4. Use "prohibitions" YAML list for machine-readable boundaries
  5. Repeat critical invariants in mission statement and footer

## Pattern: Evidence and Memory Infrastructure Missing
- Observed: 2026-02-11 (Session 001)
- Context: Agent operations require workspace structure for memory and evidence
- Symptoms:
  - .agent-workspace/<agent-id>/ directory doesn't exist
  - No memory/ subdirectory for session files
  - No personal/ subdirectory for lessons-learned and patterns
  - No escalation-inbox/ for blocker escalations
- Root Cause: Agent workspace not initialized during agent setup
- Response:
  1. Create .agent-workspace/<agent-id>/ structure on first session
  2. Establish memory/, memory/.archive/, personal/, escalation-inbox/
  3. Initialize lessons-learned.md and patterns.md in personal/
  4. Document workspace structure in Session Memory Protocol section
  5. Add workspace initialization to wake-up protocol

## Pattern: Compliance Failure Without Learning Loop
- Observed: 2026-02-11 (Session 001)
- Context: When governance compliance failures occur without triggering learning and prevention
- Symptoms:
  - Non-compliant contract fixed without RCA
  - No session memory documenting failure and correction
  - No lessons-learned entries for future prevention
  - No patterns documented for recurring detection
- Root Cause: Reactive fix without reflective learning step
- Response:
  1. STOP and perform RCA before remediation
  2. Document root causes, contributing factors, corrective actions
  3. Create session memory file capturing complete learning loop
  4. Update lessons-learned.md with prevention measures
  5. Update patterns.md with detection symptoms and responses

---

**Authority**: LIVING_AGENT_SYSTEM.md v6.2.0  
**Maintained**: Continuously (add new patterns as observed)  
**Purpose**: Enable pattern recognition and consistent response to recurring situations

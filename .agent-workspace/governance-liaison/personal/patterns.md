# Patterns - Governance Liaison Agent

## Pattern: Agent-Agnostic Validation Logic
- Observed: 2026-02-12 (Session 003)
- Context: Workflow validations that need to work across multiple agent types (foreman, governance-liaison, builders)
- Pattern Structure:
  ```bash
  # Find any agent workspace dynamically
  AGENT_WORKSPACES=$(find .agent-workspace -maxdepth 1 -type d -name "*" | grep -v "^\.$" | grep -v "^\.agent-workspace$")
  
  # Loop through to find required artifacts
  for WORKSPACE in $AGENT_WORKSPACES; do
    if [ -d "$WORKSPACE/memory" ]; then
      # Check for artifacts
    fi
  done
  ```
- Response: Never hardcode agent names (e.g., "foreman"); use `find` with pattern matching; test with multiple agent types

## Pattern: Ephemeral Artifact Evidence Validation
- Observed: 2026-02-12 (Session 003)
- Context: Required artifacts that are gitignored (e.g., working-contract.md, environment-health.json)
- Pattern Method:
  1. Identify that artifact is ephemeral (check .gitignore)
  2. Validate evidence of creation (search prehandover proof for mention)
  3. Use case-insensitive grep with flexible patterns
  4. Fail if not documented
- Response: For ephemeral files, validate mention in persistent proof; use patterns like `working.contract|working-contract` with grep -qi

## Pattern: Blocking Enforcement with Evidence-First Errors
- Observed: 2026-02-12 (Session 003)
- Context: Converting advisory/warning checks to blocking validations
- Pattern Error Structure:
  ```bash
  echo "❌ [WHAT FAILED IN CAPS]"
  echo ""
  echo "Required: [Exact requirement]"
  echo "Missing: [Specific detail]"
  echo ""
  echo "🔧 Remediation:"
  echo "  1. [Step 1]"
  echo "  2. [Step 2]"
  echo ""
  echo "📚 Authority: [Canon reference]"
  exit 1  # BLOCKING
  ```
- Response: Never use warnings for mandatory requirements; exit 1 for failures; include exact paths and schemas

## Pattern: Merge Gate Context Validation
- Observed: 2026-02-12 (Session 003)
- Context: Ensuring gate-results.json complies with MERGE_GATE_INTERFACE_STANDARD.md
- Pattern Validation:
  ```bash
  GATES=$(jq -r '.gates | keys[]' .agent-admin/gates/gate-results.json)
  REQUIRED_GATES=("merge-gate/verdict" "governance/alignment" "stop-and-fix/enforcement")
  
  # Check for missing and invalid gates
  # Fail if any missing or invalid
  ```
- Response: Validate actual gate names from JSON against canonical standard; detect both missing and extra gates

## Pattern: Code Review Integration
- Observed: 2026-02-12 (Session 003)
- Context: Catching subtle issues before finalizing PR
- Pattern Workflow:
  1. Complete all code changes
  2. Run `code_review` tool with PR title and description
  3. Review all comments returned
  4. Fix issues immediately (don't defer)
  5. Re-run if significant changes made
- Response: Always run code_review before session closure; treat findings as blocking; fix immediately

## Pattern: Protected File Modification Handling
- Observed: 2026-02-12 (Session 003)
- Context: Modifying files that require CS2 approval per REQ-CM-005
- Pattern Handling:
  1. Identify protected file modification early
  2. Document justification in PR description
  3. Flag CS2 approval requirement prominently
  4. Update sync-state.json with protected file details
  5. Do not attempt to merge without CS2 approval
- Response: Protected files require explicit escalation; governance liaison cannot self-approve; wait for CS2

## Pattern: Living Agent System v6.2.0 Contract Structure
- Observed: 2026-02-11 (Session 001)
- Context: Creating or upgrading agent contracts to v6.2.0
- Pattern Structure:
  1. YAML frontmatter with agent identity, governance bindings, scope, execution identity
  2. Mission and versioning notes
  3. Core protocols (wake-up, session closure, execution identity, critical invariant)
  4. Operating boundaries & escalations
  5. 10-category requirement mappings (Canon Management, Evidence & Records, Ripple & Alignment, Gate Compliance, Authority/Self-Alignment/Escalation, Execution & Operations, Merge Gate Interface, Coordination & Reporting, Security & Safety, Ambiguities & Gaps)
  6. Role-specific sections (for liaison: self-alignment authority, role boundaries/negative definitions)
  7. Execution checklist
  8. Session memory protocol with templates
  9. Evidence artifact bundle automation
  10. Locked protocol sections (e.g., PR failure analysis)
  11. Canonical governance references
  12. Footer with authority, version, compliance statement
- Response: Use foreman-v2.agent.md as template; adapt language and specifics for agent role; validate YAML frontmatter

## Pattern: Self-Alignment Authority Documentation
- Observed: 2026-02-11 (Session 001)
- Context: Governance liaison has unique capability to self-align governance without approval
- Pattern Characteristics:
  - Explicitly state authority source (Issue #999, canon file)
  - List what CAN be done automatically (layer down, update inventories, sync with canonical)
  - List what CANNOT be done (modify own contract, interpret policy, modify canonical source)
  - Provide operational self-alignment protocol (detect drift → fetch → layer down → validate → document)
- Response: Include self-alignment section prominently; embed protocol as bash script for copy-paste execution

## Pattern: Role Boundary Clarity via Negative Definitions
- Observed: 2026-02-11 (Session 001)
- Context: Preventing authority drift and role confusion in multi-agent systems
- Pattern Structure:
  - "What [Agent] Is NOT" section with subsections for each role type
  - Each negative definition includes:
    - Role name (e.g., "NOT a Builder")
    - Specific prohibited activities (bullet list)
    - Canonical reference citation
  - Covers all adjacent roles (for liaison: builder, FM, governance administrator, enforcement agent)
- Response: Extract negative definitions from MINIMUM_APPOINTMENT_REQUIREMENTS canon; cite specific sections

## Pattern: Canon File Reference Integration
- Observed: 2026-02-11 (Session 001)
- Context: Linking agent contracts to canonical governance authority
- Pattern Method:
  1. Identify role-specific canon files in CANON_INVENTORY.json (search by agent role name)
  2. Read canon files to understand requirements, boundaries, protocols
  3. Reference canon files in YAML frontmatter `expected_artifacts` section
  4. Reference canon files throughout contract body (authorities, boundaries, protocols)
  5. Include comprehensive list in "Canonical Governance References" section
- Response: Survey CANON_INVENTORY.json first; prioritize role-specific canons; cite frequently

## Pattern: Session Memory Template Embedding
- Observed: 2026-02-11 (Session 001)
- Context: Ensuring agents create consistent, complete session memories
- Pattern Elements:
  - Full markdown template with all required sections
  - Field placeholders (e.g., `[What was I asked to do?]`, `[path to evidence log]`)
  - Examples for clarity (e.g., file path examples, session ID format)
  - Memory rotation rules (>5 sessions → archive oldest)
  - Personal learning file structures (lessons-learned.md, patterns.md)
  - Escalation file template
- Response: Copy foreman-v2 session memory section verbatim; adjust agent-specific paths and examples

## Pattern: Evidence Artifact Bundle Script Generation
- Observed: 2026-02-11 (Session 001)
- Context: Every governed PR requires standardized evidence artifacts
- Pattern Script Structure:
  ```bash
  # Header with version and agent name
  # Create required directories (.agent-admin/prehandover, /gates, /rca, /improvements, /governance)
  # Generate template files (gate-results-template.json, improvements-template.md)
  # Success message
  ```
- Response: Provide complete copy-paste-ready bash script; include agent-specific adjustments (e.g., governance_sync section for liaison)

## Pattern: Locked Protocol Section Protection
- Observed: 2026-02-11 (Session 001)
- Context: Preventing removal/weakening of critical failure prevention protocols
- Pattern Metadata:
  ```html
  <!-- Lock ID: LOCK-[AGENT]-[PROTOCOL]-[NUMBER] -->
  <!-- Lock Reason: [Why this cannot be removed] -->
  <!-- Lock Authority: [Canon file or doctrine] -->
  <!-- Lock Date: YYYY-MM-DD -->
  <!-- Last Reviewed: YYYY-MM-DD -->
  <!-- Review Frequency: [quarterly/annual/etc] -->
  <!-- END METADATA -->
  ```
- Response: Use HTML comments for invisibility in rendered markdown; mark section with 🔒 emoji; state MANDATORY prominently

## Pattern: YAML Frontmatter Validation Workflow
- Observed: 2026-02-11 (Session 001)
- Context: Ensuring contract structural correctness
- Workflow:
  1. Create/modify agent contract file
  2. Run `.github/scripts/validate-yaml-frontmatter.sh`
  3. Review output: distinguish new errors from pre-existing legacy errors
  4. Fix only new errors related to current work
  5. Document validation results in session memory
  6. Do not expand scope to fix unrelated legacy errors
- Response: Run validation early and often; treat script exit code 0 as success; note out-of-scope errors in session memory

---
Authority: LIVING_AGENT_SYSTEM.md v6.2.0 | Created: 2026-02-11 | Updated: 2026-02-12

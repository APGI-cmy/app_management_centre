## Session 20260211

### Lesson: Cite Canon Sources Explicitly
- Context: When drafting agent checklists or contracts that aggregate governance, canon breadth can cause omissions.
- Pattern: Risk of summarizing without anchoring to precise canonical files.
- Action: List the exact canon paths next to each checklist item to keep requirements enforceable and traceable.

## Session 20260211-02

### Lesson: Merge Dual Checklists into One Contract
- Context: Drafting a foreman contract that must satisfy both foreman and governance liaison gold-standard checklists.
- Pattern: Cross-repo layer-down and registry duties can be forgotten when focusing on role-specific authority.
- Action: Mirror checklist categories in contract sections, cite the governing canon inline, and state that unchecked checklist items block execution.

## Session 20260211-04

### Lesson: Complete Learning Loop Alongside Contract Work
- Context: Creating governance liaison v2 contract per Issue #738 requirements.
- Pattern: Learning artifacts (session memory, lessons-learned, patterns) are mandatory but can be forgotten until end of session.
- Action: Create learning artifact files alongside contract work; update incrementally; commit all together as evidence bundle.

### Lesson: Comprehensive Negative Definitions Prevent Authority Drift
- Context: Governance liaison has narrow scope but can be confused with adjacent roles (builder, FM, governance admin, enforcement).
- Pattern: Positive definitions alone don't prevent scope creep; agents may infer "not explicitly prohibited = allowed".
- Action: Include "What [Agent] Is NOT" section with comprehensive negative definitions citing specific canon files; prevents authority drift in multi-agent systems.

### Lesson: Self-Alignment Authority Requires Clear Boundaries
- Context: Governance liaison has unique self-alignment authority (Issue #999) but must not overstep.
- Pattern: Powerful capabilities without clear boundaries risk governance violations.
- Action: Document both what CAN be done (layer down, update inventories) and what CANNOT (modify own contract, interpret policy, modify canonical source); provide operational protocol.

### Lesson: Locked Protocol Sections Protect Critical Procedures
- Context: PR failure analysis protocol prevents catastrophic repeat failures but could be removed or weakened.
- Pattern: Critical procedures in contracts can be inadvertently modified during contract evolution.
- Action: Lock critical protocol sections with HTML comment metadata (Lock ID, Reason, Authority, Date, Review Frequency); mark with 🔒 emoji; state MANDATORY prominently.

### Lesson: Completion Summary Provides Evidence Bundle for CS2 Review
- Context: Complex contract work requires demonstrating all success criteria met.
- Pattern: PR descriptions alone may not capture full evidence of requirement satisfaction.
- Action: Create comprehensive completion summary document covering: success criteria verification, validation results, key features, learning artifacts, comparison with previous version, compliance verification, recommendations.

## Session 20260212 (Session 002)

### Lesson: 30K Character Limit - Use References, Not Embedded Templates

**Context**: Creating agent-factory protocol documentation for Living Agent System v6.2.0 compliance

**Pattern**: Files exceeding 30,000 characters are NOT SELECTABLE in GitHub Copilot UI (ref: PartPulse PR #265)

**Root Cause**: Embedded complete templates for Components 2, 3, and 8 instead of using references to canonical governance

**Action**: 
1. **ALWAYS** run `wc -m < .github/agents/<file>.md` before creating PR
2. **Target** <25,000 characters (20% buffer below 30K hard limit)
3. **Use** 5-line references to canonical governance (not embedded templates)
4. **Check** Components 2, 3, 8 first if file >25K (common culprits for embedded content)
5. **Replace** any component with >50 lines of template content with reference

**Prevention**:
- Add Step 4.5 (character count validation) to agent-factory execution steps
- Add `file_size_limit` to YAML frontmatter (max_characters: 30000, enforcement: BLOCKING)
- Add 30K constraint as FIRST item in constraints list
- Add character count validation to execution checklist
- Add prohibition against exceeding 30K characters

**Reference Pattern** (5 lines):
```markdown
#### Component X: <Name>

**Template source**: `.governance-pack/path/to/canonical.md`

**Required**: [Brief description of what must be included]

**See**: [Reference to canonical location for complete details]
```

**Detection**: If any component >50 lines → likely candidate for reference replacement

**File Size Zones**:
- <25,000 chars: ✅ OPTIMAL (20% buffer)
- 25,000-30,000: ⚠️ WARNING (refactor recommended)
- >30,000: 🚨 BLOCKING (cannot merge, breaks GitHub UI)

## Session 20260217

### Lesson: Builder 4-Phase Architecture Implementation

- Context: When upgrading builder agent contracts to Living Agent System v6.2.0
- Pattern: Use Foreman's 4-phase architecture as reference model but simplify for builder execution model
- Action: 
  1. Adapt RAEC (Review-Advise-Escalate-Coordinate) to "Execute Only" for builders
  2. Simplify Induction phase (task loading vs. complex memory hierarchy)
  3. Focus Build phase on domain-specific execution
  4. Make Handover phase evidence-first with PREHANDOVER_PROOF template
  5. Budget ~8.5K characters for 4-phase content (total files will be 26-28K)

### Lesson: Self-Modification Prohibition is Universal

- Context: Living Agent System v6.2.0 requires all agents to explicitly prohibit self-modification
- Pattern: Every agent contract must include "Self-Modification Prohibition" as a LOCKED section
- Action:
  1. Add LOCKED section in Phase 1: Preflight for all agents
  2. Explicitly state "Agent may NEVER write to or modify own .github/agents/{agent-id}.md"
  3. Reference AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md v3.1.0 and AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.1.0
  4. Enforce via merge gate check: Agent file author ≠ agent file subject

### Lesson: Python Automation for Consistent Multi-File Updates

- Context: When applying identical structural changes to multiple similar files (e.g., 5 builder contracts)
- Pattern: Manual changes are error-prone; script-based automation ensures consistency
- Action:
  1. Manually upgrade first file to validate template
  2. Create Python script with parameterized template function
  3. Use regex pattern matching to find insertion points
  4. Validate character counts programmatically
  5. Apply to remaining files in batch
  6. Result: 4/4 builders updated successfully with identical structure

### Lesson: Character Count Management for Living Agent Contracts

- Context: Builder contracts have 30K blocking limit (GitHub UI selectability) and 25K optimal target
- Pattern: Comprehensive 4-phase content requires trade-offs between completeness and brevity
- Action:
  1. Target <25K optimal but accept 26-28K if content is constitutionally required
  2. Prioritize constitutional requirements over brevity
  3. Use references to canonical governance instead of embedding full templates
  4. Monitor character count continuously during implementation
  5. If approaching 30K, extract detailed examples to extended references

## Session 20260217 (Session 008)

### Lesson: Governance Liaison Requires More Protocol Content Than Builders

- Context: Aligning governance liaison agent to LAS v6.2.0, same 4-phase architecture as builders
- Pattern: Governance liaison final size (25,668 characters) is larger than builders (26-28K) despite similar structure
- Root Cause: Liaison has additional governance ripple protocol, layer-down procedures, drift detection, consumer repository prohibitions
- Action:
  1. Accept 25-26K for liaison as reasonable given extensive governance protocol requirements
  2. Maintain character budget awareness but prioritize governance completeness
  3. Use references to checklist Appendix A (102 PUBLIC_API artifacts) instead of embedding full list
  4. Keep RAEC behavioral examples concise but comprehensive (4 scenarios, each ~25 lines)

### Lesson: RAEC Behavioral Examples Must Be Role-Specific

- Context: Creating RAEC examples for governance liaison after using builder/foreman patterns as reference
- Pattern: Cannot simply copy RAEC examples from other agent classes; must reflect actual role duties
- Action:
  1. Identify 4 core responsibilities for the agent role
  2. Create "wrong vs right" scenarios for each responsibility
  3. For governance liaison: layer-down execution, drift remediation, authority escalation, governance delegation
  4. For builders: task acceptance, execution, test debt, scope boundaries
  5. For foreman: wave planning, builder supervision, gate decisions, architecture freeze
  6. Each example should illustrate common failure patterns and correct RAEC approach

### Lesson: Code Review Catches Consistency Issues

- Context: Initial PR had subtle inconsistencies (tolerance statement, version references)
- Pattern: Manual review doesn't catch mathematical/consistency errors as reliably as automated code review
- Action:
  1. Always run code_review tool before finalizing work
  2. Address ALL feedback, even if it seems minor (tolerance 2% vs 2.3% matters)
  3. Remove embedded version numbers when canonical documents are tracked in CANON_INVENTORY.json
  4. Ensure numerical claims are consistent across PREHANDOVER_PROOF and contract
  5. Mathematical accuracy matters for governance integrity

### Lesson: Consumer Repository Mode Requires Enhanced Prohibitions

- Context: Governance liaison operates in consumer repository (not canonical governance repository)
- Pattern: Consumer repositories have strict separation from canonical governance source
- Action:
  1. Document consumer-specific prohibitions prominently
  2. No modification of canonical governance source
  3. No creation of governance canon (consumer repositories do not author canon)
  4. No dispatch of ripple events (only canonical source dispatches)
  5. Ripple protocol is receive-only for consumers
  6. Include metadata in YAML: `this_copy: canonical`, `type: consumer-repository`


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

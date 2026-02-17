## Pattern: Governance Checklist Construction
- Observed: 2026-02-11 (Session 001)
- Context: Building agent-contract checklists from mixed local + canonical governance sources.
- Response: Anchor each requirement to a canon path, group by operational category (identity, authority, alignment, ripple, escalation), and flag stop/escala­tion triggers explicitly.

## Pattern: Dual-Checklist Contract Drafting
- Observed: 2026-02-11 (Session 003)
- Context: When a single contract must implement both role-specific and liaison checklists.
- Response: Align sections to shared category names, declare both checklists as blocking authorities, and tie layer-down/registry duties to the transport and inventory canons to avoid omissions.

## Pattern: Living Agent System v6.2.0 Contract Template Reuse
- Observed: 2026-02-11 (Session 004)
- Context: Creating new agent contracts or upgrading existing contracts to Living Agent System v6.2.0.
- Response: Use foreman-v2.agent.md or governance-liaison-v2.agent.md as concrete template; maintain exact structure (YAML frontmatter, 10-category requirements, session memory protocol, evidence bundle, locked protocols, canonical references, footer); adapt language for agent role (supervisor → builder, administrator → liaison, etc.); validate YAML early.

## Pattern: Role Boundary Documentation via Negative Definitions
- Observed: 2026-02-11 (Session 004)
- Context: Preventing authority drift and role confusion in multi-agent systems.
- Response: Include "What [Agent] Is NOT" section with subsections for each adjacent role type; list specific prohibited activities; cite canonical references for each negative definition; covers all potentially overlapping roles.

## Pattern: Locked Protocol Section Protection
- Observed: 2026-02-11 (Session 004)
- Context: Protecting critical failure prevention protocols from removal or weakening.
- Response: Lock critical protocol sections with HTML comment metadata (Lock ID, Reason, Authority, Date, Last Reviewed, Review Frequency); mark section with 🔒 emoji; state MANDATORY prominently; use HTML comments for invisibility in rendered markdown.

## Pattern: Complete Learning Loop Execution
- Observed: 2026-02-11 (Session 004)
- Context: Issue requirements mandate session memory, lessons-learned, and patterns artifacts.
- Response: Create all three learning artifact files as part of contract/work PR; session memory documents the work; lessons-learned captures insights with context/pattern/action structure; patterns documents reusable approaches with observed/context/response structure; commit all together as evidence bundle.

## Pattern: Completion Summary as Evidence Bundle
- Observed: 2026-02-11 (Session 004)
- Context: Demonstrating all success criteria met for complex contract work.
- Response: Create comprehensive completion summary covering: objective achieved, success criteria validation (checklist format with ✅), contract metrics (size, content breakdown, references), key features, validation results, learning artifacts created, comparison with previous version, compliance verification, recommendations for future work; include file SHA256 checksums.

## Pattern: Embedded Templates vs. References
- Observed: 2026-02-12 (Session 002, PR #747)
- Context: Documenting agent-factory 9-component template requirements
- Symptom: File becomes too large (>30K characters, blocks GitHub UI selectability)
- Detection: Check if Components 2, 3, or 8 contain 50+ lines of template content
- Response:
  1. **STOP** and calculate character count: `wc -m < <file>`
  2. **IDENTIFY** embedded templates (Components 2, 3, 8 are common culprits)
  3. **REPLACE** with 5-line references to canonical governance:
     ```markdown
     **Template source**: `.governance-pack/path/to/template.md`
     **Required**: [Brief description]
     **See**: [Reference to canonical location]
     ```
  4. **RE-VALIDATE** character count (<30K required, <25K recommended)
  5. **ADD** character count validation to execution steps (Step 4.5)
  6. **ENFORCE** 30K limit in YAML frontmatter (`file_size_limit`)
- Prevention: Always use references to canonical governance, never embed large templates; target <25,000 characters (20% buffer)
- Reference: PartPulse PR #265 (30K GitHub UI selectability limit)

## Pattern: 4-Phase Canonical Architecture for Builders

- Observed: 2026-02-17 (Session 007)
- Context: When implementing Living Agent System v6.2.0 for builder-class agents
- Response:
  - Phase 1 (Preflight): Identity/Authority + Self-Modification Prohibition (LOCKED) + 4 RAEC behavioral examples + 5 canonical references (SHA256)
  - Phase 2 (Induction): Task loading protocol (6 steps) + Halt conditions (escalate to FM)
  - Phase 3 (Build): Domain-specific execution + Zero-test-debt enforcement (100% GREEN required)
  - Phase 4 (Handover): Completion requirements (7-point checklist) + PREHANDOVER_PROOF template
  - Preserve all existing LOCKED sections (cumulative governance)
  - Character budget: ~8.5K for 4-phase content, target final size 26-28K

## Pattern: Consumer Repository Agent Contract Metadata

- Observed: 2026-02-17 (Session 007)
- Context: When updating agent contracts in consumer repositories (not canonical governance repository)
- Response:
  - Add to YAML frontmatter:
    - `canonical_home: APGI-cmy/maturion-foreman-governance`
    - `this_copy: consumer`
    - `authority: CS2`
    - `contract_pattern: four_phase_canonical`
    - `operating_model: execute_only` (for builders) or `RAEC` (for supervisors)
  - Respect consumer repository prohibitions:
    - No modification of `.governance-pack/`
    - No bypassing governance alignment gate
    - No creating governance canon
    - No dispatching ripple events

## Pattern: Evidence-First Handover (PREHANDOVER_PROOF)

- Observed: 2026-02-17 (Session 007)
- Context: When completing agent contract alignment or major governance tasks
- Response:
  - Create comprehensive PREHANDOVER_PROOF document before PR merge
  - Include 17 sections:
    1. CS2 authorization confirmation
    2. Checklist compliance matrix (100%)
    3. Before/after comparison
    4. Requirement mapping verification
    5. Validation hook confirmation
    6. LOCKED section metadata
    7. Consumer repository adaptations
    8. Canonical references enumeration
    9. RAEC behavioral examples
    10. Implementation evidence
    11. Testing/validation status
    12. Scope compliance verification
    13. Security/safety verification
    14. Architecture alignment verification
    15. Governance hygiene check
    16. Handover declaration
    17. Lessons & recommendations
  - Character count: Aim for 15-20K comprehensive documentation


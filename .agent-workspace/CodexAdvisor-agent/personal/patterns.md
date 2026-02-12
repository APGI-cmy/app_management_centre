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

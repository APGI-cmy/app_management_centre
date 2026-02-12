# Lessons Learned - Governance Liaison Agent

## Session 20260212

### Lesson: Agent-Agnostic Enforcement
- Context: Merge gate enforcement must work for all agent types, not just foreman
- Pattern: Use dynamic discovery (e.g., `find`) instead of hardcoded paths when checking agent-specific artifacts
- Action: Replace hardcoded `.agent-workspace/foreman/` with dynamic search for `.agent-workspace/*/` in validation logic

### Lesson: Ephemeral Artifact Validation
- Context: Some required artifacts are gitignored (e.g., working-contract.md) and can't be checked directly in PR
- Pattern: Validate evidence of creation (mention in persistent proof) instead of checking ephemeral file directly
- Action: Search prehandover proof for mentions of ephemeral artifacts; fail if not documented

### Lesson: Advisory Checks Are Ignored
- Context: Non-blocking warnings (learning artifacts in PR #740) were ignored
- Pattern: Strict enforcement requires blocking failures (exit 1), not warnings
- Action: Convert all mandatory requirements to blocking validations with clear error messages

### Lesson: Code Review Catches Subtle Issues
- Context: Invalid condition `steps.validate-gate-schema.outputs != ''` looked reasonable but was wrong
- Pattern: GitHub Actions output objects are always truthy; check specific fields or outcome instead
- Action: Always run code_review tool before finalizing PR; fix issues immediately

### Lesson: Evidence-First Error Messages Work
- Context: Each validation failure needs clear, actionable remediation
- Pattern: Include exact path, required schema, remediation steps, and authority in every error message
- Action: Structure error messages as: ❌ WHAT FAILED → Required: REQUIREMENT → Missing: DETAIL → 🔧 Remediation: STEPS → 📚 Authority: REFERENCE

### Lesson: Protected File Modifications Require CS2
- Context: Workflow files (.github/workflows/) are protected per REQ-CM-005
- Pattern: Governance liaison can propose changes but cannot self-approve
- Action: Flag protected file modifications explicitly in PR description; escalate to CS2 (Johan Ras) for approval

### Lesson: Canonical Standards Must Be Enforced Mechanically
- Context: MERGE_GATE_INTERFACE_STANDARD.md defines 3 canonical gate contexts
- Pattern: Manual compliance is error-prone; validate actual content (gate-results.json) against canonical standard
- Action: Add validation step checking gate names match standard; fail if missing or invalid

### Lesson: Enforcement Gaps Are Catastrophic
- Context: PR #740 merged with 7 violations due to weak enforcement
- Pattern: Every violation that "should have been caught" represents an enforcement gap
- Action: Treat enforcement gaps as critical bugs; fix immediately with blocking validations

## Session 20260211

### Lesson: Contract v2 Gold-Standard Adoption
- Context: Upgrading from Living Agent System v5.0.0 to v6.2.0
- Pattern: Use foreman-v2.agent.md as concrete template when creating v6.2.0 contracts for other agent classes
- Action: Follow 10-category requirement structure, embed session memory protocols, include evidence artifact automation, add locked PR failure analysis protocol

### Lesson: Self-Alignment Authority Emphasis
- Context: Governance liaison has unique self-alignment authority per Issue #999
- Pattern: This distinguishes liaison from all other agent classes; emphasize in contract frontmatter, mission, and authority sections
- Action: Make self-alignment protocol explicit and operational; document boundaries (can align governance, cannot modify canonical source or own contract)

### Lesson: Role Boundaries via Negative Definitions
- Context: Preventing authority drift and role confusion
- Pattern: Comprehensive "What [Agent] Is NOT" sections derived from canon files prevent scope creep
- Action: Reference specific canon files for each negative definition (NOT a builder, NOT FM, NOT governance administrator, NOT enforcement agent)

### Lesson: Canon File Integration
- Context: CANON_INVENTORY.json contains 135+ canon files; identify relevant subset for agent role
- Pattern: Survey canon files by agent role (governance liaison canons: ROLE_SURVEY, MINIMUM_APPOINTMENT_REQUIREMENTS, TRAINING_PROTOCOL, REPOSITORY_SEEDING_AND_ENFORCEMENT_ROLE_SEPARATION)
- Action: Reference all role-specific canon files in contract's canonical governance references section

### Lesson: YAML Frontmatter Validation Early
- Context: Ensuring contract structural correctness before commit
- Pattern: Run `.github/scripts/validate-yaml-frontmatter.sh` immediately after contract creation
- Action: Fix any YAML syntax errors before proceeding; distinguish new contract errors from pre-existing legacy errors

### Lesson: Session Memory Protocol Templates
- Context: Agents need operational guidance for post-session memory creation
- Pattern: Embed complete session memory template inside contract with examples and field explanations
- Action: Include memory rotation rules, personal learning updates, and escalation templates

### Lesson: Evidence Artifact Bundle Automation
- Context: Every governed PR requires specific evidence artifacts under `.agent-admin/`
- Pattern: Provide bash script template for creating evidence directory structure and templates
- Action: Include script in contract so agents can copy-paste and execute during session setup

### Lesson: Locked Protocol Sections
- Context: Preventing catastrophic repeat failures (e.g., PR failures without proper RCA)
- Pattern: Lock critical protocols with metadata comments (Lock ID, Reason, Authority, Date, Review Frequency)
- Action: Use HTML comments for lock metadata; clearly mark section as MANDATORY

### Lesson: Learning Loop Completeness
- Context: Issue #738 requires session memory, lessons-learned, and patterns artifacts
- Pattern: Create all three artifact types as part of contract creation PR
- Action: Session memory documents the work; lessons-learned captures insights; patterns documents reusable approaches

---
Authority: LIVING_AGENT_SYSTEM.md v6.2.0 | Created: 2026-02-11 | Updated: 2026-02-12

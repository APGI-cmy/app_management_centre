# Foreman Agent - Governance Bindings

**Authority**: LIVING_AGENT_SYSTEM v5.0.0  
**Agent**: foreman-agent  
**Version**: 5.0.1  
**Last Updated**: 2026-02-09

This file contains all canonical governance bindings for the Foreman agent. These bindings are referenced by the core agent contract and must be loaded during agent initialization.

## Tier-0 Constitutional Documents (ALL 15 MANDATORY via manifest)

- **id**: tier0-canon
- **path**: governance/TIER_0_CANON_MANIFEST.json
- **role**: supreme-authority
- **note**: Loads all 15 Tier-0 constitutional documents dynamically

- **id**: build-philosophy
- **path**: BUILD_PHILOSOPHY.md
- **role**: supreme-building-authority

## NEW LAS v5.0.0 Protocols (MANDATORY)

- **id**: foreman-memory-protocol
- **path**: governance/canon/FOREMAN_MEMORY_PROTOCOL.md
- **role**: fm-memory-management
- **version**: 1.0.0
- **enforcement**: MANDATORY
- **note**: 4-level FM memory hierarchy (Constitutional, Wave, Session, Learning)

- **id**: foreman-wave-planning
- **path**: governance/canon/FOREMAN_WAVE_PLANNING_AND_ISSUE_ARTIFACT_GENERATION_PROTOCOL.md
- **role**: wave-planning-and-issue-generation
- **version**: 1.0.0
- **enforcement**: MANDATORY
- **note**: Wave decomposition, subwave identification, issue artifact generation

- **id**: fm-role-canon
- **path**: governance/maturion/FM_ROLE_CANON.md
- **role**: fm-role-authority-responsibilities
- **enforcement**: MANDATORY
- **note**: FM role definition including Sections 12 (Operational Sandbox) and 13 (Issue Artifact Generation)

- **id**: stop-and-fix-doctrine
- **path**: governance/canon/STOP_AND_FIX_DOCTRINE.md
- **role**: test-debt-enforcement
- **version**: 2.1.0
- **enforcement**: MANDATORY
- **note**: Updated with Section 8 (Learning Loop Integration)

- **id**: bootstrap-learnings
- **path**: governance/canon/BOOTSTRAP_EXECUTION_LEARNINGS.md
- **role**: execution-learnings
- **enforcement**: MANDATORY
- **note**: Updated with Appendix A (Classification Matrix)

## Batch 1: Agent & Execution Governance (10 canons)

- **id**: agent-contract-protection
- **path**: governance/canon/AGENT_CONTRACT_PROTECTION_PROTOCOL.md
- **role**: contract-protection

- **id**: mandatory-enhancement-capture
- **path**: governance/canon/MANDATORY_ENHANCEMENT_CAPTURE_STANDARD.md
- **role**: enhancement-capture

- **id**: cross-repo-layer-down
- **path**: governance/canon/CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md
- **role**: layer-down-protocol

- **id**: governance-ripple-model
- **path**: governance/canon/GOVERNANCE_RIPPLE_MODEL.md
- **role**: ripple-propagation

- **id**: ci-confirmatory
- **path**: governance/canon/CI_CONFIRMATORY_NOT_DIAGNOSTIC.md
- **role**: local-validation

- **id**: scope-declaration-schema
- **path**: governance/canon/SCOPE_DECLARATION_SCHEMA.md
- **role**: scope-definition

- **id**: scope-to-diff-rule
- **path**: governance/canon/SCOPE_TO_DIFF_RULE.md
- **role**: scope-enforcement

- **id**: governance-purpose-scope
- **path**: governance/canon/GOVERNANCE_PURPOSE_AND_SCOPE.md
- **role**: supreme-authority-and-scope

- **id**: agent-recruitment-authority
- **path**: governance/canon/AGENT_RECRUITMENT_AND_CONTRACT_AUTHORITY_MODEL.md
- **role**: agent-authority

- **id**: cs2-agent-authority
- **path**: governance/canon/CS2_AGENT_FILE_AUTHORITY_MODEL.md
- **role**: cs2-authority

## Batch 2: Agent Governance Alignment (10 canons)

- **id**: agent-file-binding-requirements
- **path**: governance/canon/AGENT_FILE_BINDING_REQUIREMENTS.md
- **role**: binding-requirements

- **id**: agent-context-sync
- **path**: governance/canon/AGENT_CANONICAL_CONTEXT_SYNCHRONISATION_PROTOCOL.md
- **role**: context-sync

- **id**: agent-recruitment
- **path**: governance/canon/AGENT_RECRUITMENT.md
- **role**: agent-legitimacy

- **id**: agent-ripple-awareness
- **path**: governance/canon/AGENT_RIPPLE_AWARENESS_OBLIGATION.md
- **role**: ripple-awareness

- **id**: agent-role-gate-applicability
- **path**: governance/canon/AGENT_ROLE_GATE_APPLICABILITY.md
- **role**: gate-applicability

- **id**: agent-onboarding
- **path**: governance/canon/AGENT_ONBOARDING_QUICKSTART.md
- **role**: agent-onboarding

- **id**: builder-contract-bindings
- **path**: governance/canon/BUILDER_CONTRACT_BINDING_CHECKLIST.md
- **role**: builder-requirements

- **id**: cognitive-orchestration
- **path**: governance/canon/COGNITIVE_CAPABILITY_ORCHESTRATION_MODEL.md
- **role**: cognitive-orchestration

- **id**: delegation-audit
- **path**: governance/canon/DELEGATION_INSTRUCTION_AND_AUDIT_MODEL.md
- **role**: delegation-audit

- **id**: domain-ownership
- **path**: governance/canon/DOMAIN_OWNERSHIP_ACCOUNTABILITY.md
- **role**: domain-accountability

## Batch 3: PR Gates & Quality Alignment (10 canons)

- **id**: pr-gate-evaluation
- **path**: governance/canon/PR_GATE_EVALUATION_AND_ROLE_PROTOCOL.md
- **role**: gate-evaluation

- **id**: pr-gate-precondition
- **path**: governance/canon/PR_GATE_PRECONDITION_RULE.md
- **role**: gate-precondition

- **id**: pr-scope-control
- **path**: governance/canon/PR_SCOPE_CONTROL_POLICY.md
- **role**: scope-control

- **id**: branch-protection
- **path**: governance/canon/BRANCH_PROTECTION_ENFORCEMENT.md
- **role**: branch-protection

- **id**: builder-first-pr
- **path**: governance/canon/BUILDER_FIRST_PR_MERGE_MODEL.md
- **role**: first-pr-model

- **id**: qa-catalog-alignment
- **path**: governance/canon/QA_CATALOG_ALIGNMENT_GATE_CANON.md
- **role**: qa-foundation

- **id**: initialization-completeness
- **path**: governance/canon/INITIALIZATION_COMPLETENESS_GATE.md
- **role**: initialization-gate

- **id**: warning-discovery-blocker
- **path**: governance/canon/WARNING_DISCOVERY_BLOCKER_PROTOCOL.md
- **role**: warning-enforcement

- **id**: gate-predictive-compliance
- **path**: governance/canon/GATE_PREDICTIVE_COMPLIANCE_ANALYSIS.md
- **role**: predictive-compliance

- **id**: merge-gate-philosophy
- **path**: governance/canon/MERGE_GATE_PHILOSOPHY.md
- **role**: merge-philosophy

## Batch 4: FM-Specific & Learning Alignment (10 canons)

- **id**: fm-governance-loading
- **path**: governance/canon/FM_GOVERNANCE_LOADING_PROTOCOL.md
- **role**: fm-loading

- **id**: fm-builder-appointment
- **path**: governance/canon/FM_BUILDER_APPOINTMENT_PROTOCOL.md
- **role**: fm-builder-appointment

- **id**: fm-preauth-checklist
- **path**: governance/canon/FM_PREAUTH_CHECKLIST_CANON.md
- **role**: fm-preauth

- **id**: fm-runtime-enforcement
- **path**: governance/canon/FM_RUNTIME_ENFORCEMENT_AND_AWARENESS_MODEL.md
- **role**: fm-runtime

- **id**: foreman-authority-supervision
- **path**: governance/canon/FOREMAN_AUTHORITY_AND_SUPERVISION_MODEL.md
- **role**: fm-authority

- **id**: learning-intake-promotion
- **path**: governance/canon/LEARNING_INTAKE_AND_PROMOTION_MODEL.md
- **role**: learning-intake

- **id**: learning-promotion-rule
- **path**: governance/canon/LEARNING_PROMOTION_RULE.md
- **role**: learning-promotion

- **id**: failure-promotion-rule
- **path**: governance/canon/FAILURE_PROMOTION_RULE.md
- **role**: failure-promotion

- **id**: build-intervention-alert
- **path**: governance/canon/BUILD_INTERVENTION_AND_ALERT_MODEL.md
- **role**: build-intervention

- **id**: cascading-failure-breaker
- **path**: governance/canon/CASCADING_FAILURE_CIRCUIT_BREAKER.md
- **role**: failure-breaker

## Batch 5: Governance Liaison + Architecture Alignment (10 canons)

- **id**: governance-liaison-role
- **path**: governance/canon/GOVERNANCE_LIAISON_ROLE_SURVEY.md
- **role**: liaison-governance

- **id**: architecture-completeness
- **path**: governance/canon/ARCHITECTURE_COMPLETENESS_REQUIREMENTS.md
- **role**: architecture-completeness

- **id**: app-startup-requirements
- **path**: governance/canon/APP_STARTUP_REQUIREMENTS_DECLARATION.md
- **role**: startup-requirements

- **id**: build-effectiveness
- **path**: governance/canon/BUILD_EFFECTIVENESS_STANDARD.md
- **role**: build-effectiveness

- **id**: build-tree-execution
- **path**: governance/canon/BUILD_TREE_EXECUTION_MODEL.md
- **role**: build-tree

- **id**: build-node-inspection
- **path**: governance/canon/BUILD_NODE_INSPECTION_MODEL.md
- **role**: build-inspection

- **id**: combined-testing
- **path**: governance/canon/COMBINED_TESTING_PATTERN.md
- **role**: testing-pattern

## Batch 6: Memory, Platform & Compliance Alignment (10 canons)

- **id**: memory-lifecycle
- **path**: governance/canon/MEMORY_LIFECYCLE_STATE_MACHINE_CONTRACT.md
- **role**: memory-lifecycle

- **id**: memory-integrity
- **path**: governance/canon/MEMORY_INTEGRITY_AND_CORRUPTION_MODEL.md
- **role**: memory-integrity

- **id**: memory-observability
- **path**: governance/canon/MEMORY_OBSERVABILITY_QUERY_CONTRACT.md
- **role**: memory-observability

- **id**: cognitive-hygiene-memory
- **path**: governance/canon/COGNITIVE_HYGIENE_MEMORY_INTEGRATION_MODEL.md
- **role**: cognitive-hygiene

- **id**: cognitive-hygiene-authority
- **path**: governance/canon/COGNITIVE_HYGIENE_AUTHORITY_MODEL.md
- **role**: hygiene-authority

- **id**: platform-authority-boundary
- **path**: governance/canon/PLATFORM_AUTHORITY_BOUNDARY_AND_DELEGATION_MODEL.md
- **role**: platform-boundary

- **id**: compliance-standards
- **path**: governance/canon/COMPLIANCE_AND_STANDARDS_GOVERNANCE.md
- **role**: compliance-governance

- **id**: audit-readiness
- **path**: governance/canon/AUDIT_READINESS_MODEL.md
- **role**: audit-readiness

- **id**: commissioning-evidence
- **path**: governance/canon/COMMISSIONING_EVIDENCE_MODEL.md
- **role**: commissioning-evidence

- **id**: system-commissioning
- **path**: governance/canon/SYSTEM_COMMISSIONING_AND_PROGRESSIVE_ACTIVATION_PROTOCOL.md
- **role**: system-commissioning

## Batch 7: Versioning & Ripple Intelligence Alignment (10 canons)

- **id**: governance-versioning-sync
- **path**: governance/canon/GOVERNANCE_VERSIONING_AND_SYNC_PROTOCOL.md
- **role**: versioning-sync

- **id**: governance-layerdown-contract
- **path**: governance/canon/GOVERNANCE_LAYERDOWN_CONTRACT.md
- **role**: layerdown-contract

- **id**: governance-completeness
- **path**: governance/canon/GOVERNANCE_COMPLETENESS_MODEL.md
- **role**: completeness-model

- **id**: governance-enforcement-transition
- **path**: governance/canon/GOVERNANCE_ENFORCEMENT_TRANSITION.md
- **role**: enforcement-transition

- **id**: assisted-ripple-scan-scope
- **path**: governance/canon/ASSISTED_RIPPLE_SCAN_SCOPE.md
- **role**: ripple-scan-scope

- **id**: assisted-ripple-scan-semantics
- **path**: governance/canon/ASSISTED_RIPPLE_SCAN_HUMAN_REVIEW_SEMANTICS.md
- **role**: ripple-scan-semantics

- **id**: cross-repo-ripple-awareness
- **path**: governance/canon/CROSS_REPOSITORY_RIPPLE_AWARENESS_MODEL.md
- **role**: cross-repo-ripple

- **id**: ripple-intelligence-layer
- **path**: governance/canon/RIPPLE_INTELLIGENCE_LAYER.md
- **role**: ripple-intelligence

- **id**: ripple-runtime-integration
- **path**: governance/canon/RIPPLE_RUNTIME_INTEGRATION_SURVEY.md
- **role**: ripple-runtime

## Additional Key Canons

- **id**: execution-bootstrap-protocol
- **path**: governance/canon/EXECUTION_BOOTSTRAP_PROTOCOL_REFERENCE.md
- **role**: execution-verification-mandate
- **version**: 2.0.0+

- **id**: agent-contract-management
- **path**: governance/canon/AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md
- **role**: contract-modification-authority
- **enforcement**: CONSTITUTIONAL

- **id**: quality-integrity-watchdog
- **path**: governance/canon/WATCHDOG_QUALITY_INTEGRITY_CHANNEL.md
- **role**: quality-integrity-enforcement
- **version**: 1.0.0

- **id**: pre-implementation-behavior-review
- **path**: governance/canon/PRE_IMPLEMENTATION_BEHAVIOR_REVIEW_PROTOCOL.md
- **role**: enhancement-testing-discipline
- **version**: 1.0.0
- **enforcement**: MANDATORY

- **id**: bl-018-019-integration
- **path**: governance/canon/BL_018_019_GOVERNANCE_INTEGRATION.md
- **role**: qa-integration

- **id**: platform-readiness
- **path**: governance/canon/PLATFORM_READINESS_FOR_GOVERNED_BUILD_EXECUTION.md
- **role**: platform-readiness

- **id**: maturion-runtime-monitor
- **path**: governance/canon/MATURION_RUNTIME_EXECUTION_MONITOR_SPEC.md
- **role**: runtime-monitor

- **id**: byg-doctrine
- **path**: governance/philosophy/BYG_DOCTRINE.md
- **role**: build-philosophy

- **id**: ibwr-protocol
- **path**: governance/canon/IN_BETWEEN_WAVE_RECONCILIATION.md
- **role**: wave-coordination

- **id**: wave-closure-certification
- **path**: governance/canon/MANDATORY_CANONICAL_PROGRESS_RECORDING_AND_WAVE_CLOSURE_CERTIFICATION.md
- **role**: wave-closure

## Local Policies & Specs (non-canon references)

- **id**: fm-execution-mandate
- **path**: governance/contracts/FM_EXECUTION_MANDATE.md
- **role**: fm-authority-definition

- **id**: fm-operational-guidance
- **path**: governance/contracts/FM_OPERATIONAL_GUIDANCE.md
- **role**: operational-patterns

- **id**: fm-ripple-intelligence
- **path**: governance/specs/FM_RIPPLE_INTELLIGENCE_SPEC.md
- **role**: ripple-awareness

- **id**: fm-merge-gate-canon
- **path**: governance/alignment/FM_MERGE_GATE_MANAGEMENT_CANON.md
- **role**: merge-gate-ownership

- **id**: builder-appointment
- **path**: governance/ROLE_APPOINTMENT_PROTOCOL.md
- **role**: builder-recruitment

- **id**: zero-test-debt
- **path**: governance/policies/zero-test-debt-constitutional-rule.md
- **role**: qa-enforcement

- **id**: build-to-green
- **path**: governance/specs/build-to-green-enforcement-spec.md
- **role**: execution-standard

- **id**: design-freeze
- **path**: governance/policies/design-freeze-rule.md
- **role**: architecture-stability

- **id**: test-removal-governance
- **path**: governance/policies/TEST_REMOVAL_GOVERNANCE_GATE_LOCAL.md
- **role**: test-removal-authorization

- **id**: warning-handling
- **path**: governance/policies/ZERO_WARNING_TEST_DEBT_IMMEDIATE_REMEDY_DOCTRINE.md
- **role**: warning-enforcement

- **id**: deprecation-detection-gate
- **path**: governance/policies/AUTOMATED_DEPRECATION_DETECTION_GATE.md
- **role**: deprecation-enforcement

- **id**: qa-catalog-alignment-spec
- **path**: governance/specs/QA_CATALOG_ALIGNMENT_GATE_SPEC.md
- **role**: qa-foundation

- **id**: ibwr-spec
- **path**: governance/specs/IN_BETWEEN_WAVE_RECONCILIATION_SPEC.md
- **role**: wave-coordination

---

**Total Canonical Bindings**: 96  
**Batches Covered**: 1-7 (all 70+ canons) + NEW v5.0.0 protocols  
**Canonical Governance Repository**: APGI-cmy/maturion-foreman-governance

**MANDATORY**: FM MUST load ALL bindings before any decision. Selective loading is prohibited.

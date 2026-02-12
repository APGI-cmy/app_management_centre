# Patterns Observed

## Pattern: Standard Interface Consolidation
- Observed: 2026-02-12 (Session 001)
- Context: Multiple workflows performing similar validations with inconsistent naming
- Response: Create unified interface with deterministic PR classification

## Pattern: Evidence-First Error Design
- Observed: 2026-02-12 (Session 001)
- Context: Gate failures requiring log archaeology to understand
- Response: Include missing path + required schema + remediation in every error

## Pattern: Bootstrap Paradox Documentation
- Observed: 2026-02-12 (Session 001)
- Context: PR creating new gates must be evaluated by some set of gates
- Response: Explicitly document transition rules (old law applies, new law demonstrated)

## Pattern: Protocol Execution as Gate Requirement
- Observed: 2026-02-12 (Session 001)
- Context: Living Agent System protocols (wake-up, session-closure) not enforced
- Response: Check for session memory files and working contract mentions

## Pattern: Machine-Readable + Human-Readable Dual Artifacts
- Observed: 2026-02-12 (Session 001)
- Context: Evidence must be both human-understandable and machine-processable
- Response: gate-results.json (machine) + PREHANDOVER_PROOF.md (human)

## Pattern: Deterministic PR Classification
- Observed: 2026-02-12 (Session 001)
- Context: Gates need to know when to apply vs skip
- Response: Single deterministic classification: labels → paths → branches → default

## Pattern: CS2 Approval for Infrastructure Changes
- Observed: 2026-02-12 (Session 001)
- Context: Workflow files are constitutional infrastructure
- Response: Gate passes but explicitly requires CS2 review

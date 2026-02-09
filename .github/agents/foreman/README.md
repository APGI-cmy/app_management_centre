# Foreman Agent - Modular Contract Structure

This directory contains modular components of the Foreman agent contract, refactored from the monolithic `foreman.agent.md` file for improved token efficiency and maintainability.

## Structure

### Core Contract
- **File**: `../foreman.agent.md` (451 lines)
- **Purpose**: Essential agent definition, mission, authority boundaries, and quick reference
- **Content**:
  - YAML frontmatter with agent metadata and LAS v5.0.0 compliance
  - Mission statement
  - FM Owns (authority areas)
  - FM Does NOT Own (exclusions)
  - FM MUST NEVER (prohibitions)
  - Scope and execution principles
  - STOP triggers
  - Quick reference to modular files

### Modular Components

#### 1. Governance Bindings (`governance-bindings.md`)
- **Lines**: 441
- **Purpose**: All 96 canonical governance references
- **Content**:
  - Tier-0 Constitutional Documents (15 via manifest)
  - NEW LAS v5.0.0 Protocols (5 mandatory)
  - Batch 1-7: Canonical governance (70+ canons)
  - Additional key canons (10)
  - Local policies & specs (14)

#### 2. Operational Procedures (`operational-procedures.md`)
- **Lines**: 361
- **Purpose**: Operational workflows and procedures
- **Content**:
  - Operational Sandbox (workspace structure)
  - Wave Planning & Issue Artifact Generation
  - Wake-Up Protocol (6 phases)
  - Merge Gate Management Authority
  - Memory Management (4-level hierarchy)

#### 3. Living Agent Capabilities (`living-agent-capabilities.md`)
- **Lines**: 192
- **Purpose**: Living Agent System v5.0.0 features
- **Content**:
  - Living Agent Status
  - Agent Health Checks
  - Self-Evolution Protocol
  - Ripple Intelligence
  - Auto-Update Policy
  - Agent Contract Ripple Escalation

#### 4. Compliance & Validation (`compliance.md`)
- **Lines**: 204
- **Purpose**: Contract validation and version history
- **Content**:
  - LAS v5.0.0 Compliance Checklist
  - Compliance Metrics
  - Contract Version History (v5.0.1, v5.0.0, v4.x)
  - Validation Process

## Benefits of Modular Structure

### Token Efficiency
- **Before**: 1,305 lines = ~19,575 tokens (~10% of context window)
- **After**: 451 lines (core) = ~6,765 tokens (~3.4% of context window)
- **Reduction**: 65% fewer tokens for core contract

### Selective Loading
- Agent can load only what it needs for current task
- Governance bindings loaded during wake-up
- Operational procedures loaded for execution
- Living agent capabilities loaded for health checks
- Compliance loaded for validation

### Maintainability
- Update governance bindings without touching core contract
- Modify operational procedures independently
- Evolve living agent capabilities separately
- Track version history in dedicated file

### Clarity
- Each file has single responsibility
- Easier to find specific information
- Reduced cognitive load for LLM
- Better documentation organization

## Usage

### For Foreman Agent
1. **Always load**: Core contract (`foreman.agent.md`)
2. **During wake-up**: Load `governance-bindings.md` for Phase 2 (Governance Scan)
3. **During execution**: Reference `operational-procedures.md` as needed
4. **For health checks**: Reference `living-agent-capabilities.md`
5. **For validation**: Reference `compliance.md`

### For Contract Modification
1. **Core contract changes**: Require CS2 approval (protected sections)
2. **Governance bindings**: Update when canonical governance changes
3. **Operational procedures**: Update when protocols evolve
4. **Living agent capabilities**: Update when LAS version changes
5. **Compliance**: Update after every contract modification

## Version History

- **v5.0.1** (2026-02-09): Modular refactor from monolithic structure
- **v5.0.0** (2026-02-09): Living Agent System v5.0.0 upgrade
- **v4.x**: Classic monolithic structure

## References

- **Authority**: LIVING_AGENT_SYSTEM v5.0.0
- **Protocol**: AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md
- **Canonical Governance**: APGI-cmy/maturion-foreman-governance

---

**Living Agent System v5.0.0** | **Modular Contract Pattern** | **Token Efficiency: 65% reduction**

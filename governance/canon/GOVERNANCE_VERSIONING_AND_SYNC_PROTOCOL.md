# GOVERNANCE VERSIONING AND SYNC PROTOCOL

## Status
**Type**: Canonical Governance Protocol  
**Authority**: Supreme - Canonical  
**Version**: v1.0.0  
**Effective Date**: 2025-12-23  
**Owner**: Maturion Engineering Leadership (Johan Ras)  
**Precedence**: Subordinate to GOVERNANCE_PURPOSE_AND_SCOPE.md

---

## 1. Purpose

This document defines the **canonical protocol** for governance version identification, synchronization detection, and version compatibility expectations across the Maturion ecosystem.

This protocol resolves **Wiring Gap W-001** identified in the Governance Dependency & Activation Readiness Scan by establishing:
- How governance canon versions are identified
- How execution systems detect governance changes
- What compatibility expectations exist between governance versions
- How governance change signals propagate across repositories

**Objectives**:
- Enable consistent governance version identification across all execution systems
- Provide clear, auditable version change detection mechanisms
- Define compatibility rules for governance evolution
- Establish change signaling expectations without requiring automation
- Support the Governance Ripple Model's bidirectional evolution framework

**Important**: This protocol defines **version semantics and compatibility expectations**, not implementation mechanisms. Governance defines requirements; execution systems must conform.

---

## 2. Constitutional Authority

This protocol derives authority from:
- **CONSTITUTION.md** - Governance supremacy and canonical memory principles
- **GOVERNANCE_PURPOSE_AND_SCOPE.md** - Governance as canonical memory
- **VERSIONING_AND_EVOLUTION_GOVERNANCE.md** - SemVer semantics and version lifecycle
- **GOVERNANCE_RIPPLE_MODEL.md** - Governance propagation and evolution model
- **FM_GOVERNANCE_LOADING_PROTOCOL.md** - Governance loading requirements
- **GOVERNANCE_COMPLETENESS_MODEL.md** - Governance structure and completeness

This protocol extends and integrates these documents to define synchronization semantics.

---

## 3. Scope

### 3.1 In Scope
- Governance version identification scheme
- Repository-level governance version tagging
- Version change detection semantics
- Backward compatibility rules
- Forward compatibility expectations
- Breaking change signaling
- Version comparison logic
- Deprecation signaling
- Transition period semantics

### 3.2 Out of Scope (Absolute)
- ❌ Automation implementation
- ❌ Tooling or CI/CD changes
- ❌ FM app code changes
- ❌ Specific synchronization technologies
- ❌ Push/pull mechanisms
- ❌ Cache invalidation implementation
- ❌ Network protocols or APIs

This is a **governance requirement document**, not an execution specification.

---

## 4. Governance Version Identification

### 4.1 Repository Version Identifier

The governance repository maintains a **canonical version identifier** representing the overall state of governance canon.

**Version Format**: Semantic Versioning 2.0.0 (`MAJOR.MINOR.PATCH`)

**Location**: Git tags on the `main` branch

**Tag Format**: `governance-vMAJOR.MINOR.PATCH`

**Examples**:
- `governance-v1.0.0` - Initial stable governance release
- `governance-v1.1.0` - Backward-compatible governance enhancement
- `governance-v2.0.0` - Breaking governance change

**Invariant**: Only the Governance Administrator may create governance version tags, and only with Johan's approval for MAJOR version changes.

### 4.2 Version Semantics

Per **VERSIONING_AND_EVOLUTION_GOVERNANCE.md**, governance versions follow SemVer semantics:

**MAJOR Version Increment** (`X.0.0`) - Breaking Changes:
- Incompatible changes to canonical governance contracts
- Required schema field removals or type changes
- New mandatory governance rules that invalidate prior compliant behavior
- Agent contract changes that require code changes in execution systems
- Gate requirement changes that make previously compliant PRs fail

**MINOR Version Increment** (`X.Y.0`) - Non-Breaking Enhancements:
- New optional governance rules or clarifications
- New optional schema fields
- New governance templates or examples
- Clarifications that don't change enforcement semantics
- New canonical documents that extend but don't replace existing ones

**PATCH Version Increment** (`X.Y.Z`) - Non-Breaking Fixes:
- Typo corrections
- Documentation clarifications with no semantic change
- Formatting improvements
- Metadata updates
- Reference link fixes

### 4.3 Individual Artifact Versions

Per **VERSIONING_AND_EVOLUTION_GOVERNANCE.md**, individual governance artifacts maintain their own version in document headers:

**Format**:
```markdown
## Status
Canonical Governance Policy  
Version: v1.2.0  
Authority: Governance Administrator  
Last Updated: 2025-12-23
```

**Relationship to Repository Version**:
- Repository version represents the **aggregate state** of all governance
- Individual artifact versions track **specific document evolution**
- Repository version increments reflect the **most significant** change across all artifacts
- Individual artifact versions may increment independently between repository releases

**Example**:
- Repository at `governance-v1.0.0`
- Document A at `v1.0.0`
- Document B at `v1.1.0` (clarification added)
- Repository increments to `governance-v1.1.0` (MINOR change)
- Both documents remain at their individual versions but are part of `governance-v1.1.0` release

---

## 5. Version Change Detection

### 5.1 Detection Methods

Execution systems MUST be able to detect governance version changes through:

**Method 1: Git Tag Comparison** (Authoritative)
- Compare current local governance version tag against remote repository
- Git tags are immutable and authoritative
- Detection: Fetch remote tags, compare latest `governance-v*` tag to current

**Method 2: Commit SHA Comparison** (Precise)
- Compare current local commit SHA against remote repository `main` branch HEAD
- Detects any change, including untagged commits
- Detection: Fetch remote, compare local HEAD SHA to remote `origin/main` SHA

**Method 3: Artifact Checksum** (Validation)
- Compute cryptographic hash of governance directory contents
- Detects any modification to governance files
- Detection: Compute hash of `governance/` directory, compare to stored hash

**Recommended Approach**:
1. Use Method 1 (Git Tag) for **version identification**
2. Use Method 2 (Commit SHA) for **change detection** between releases
3. Use Method 3 (Checksum) for **integrity validation**

### 5.2 Change Detection Timing

Execution systems SHOULD detect governance changes:

**At System Startup**:
- FM app startup MUST validate governance version
- If version mismatch detected, MUST either update or flag for operator attention

**On Demand**:
- Systems MAY provide "check for governance updates" capability
- Systems MAY cache governance with explicit cache invalidation

**On Build Execution**:
- Builders SHOULD validate governance version at build start
- If version mismatch detected and impacts build, MUST escalate

**NOT Required**:
- ❌ Continuous polling or background checking
- ❌ Real-time synchronization
- ❌ Automatic application of updates without validation

### 5.3 Version Mismatch Handling

When an execution system detects a governance version mismatch:

**Non-Breaking Change (MINOR or PATCH)**:
- System MAY continue operating with current version
- System SHOULD log notification of available update
- System SHOULD update at next convenient restart or maintenance window
- System MUST NOT block operations

**Breaking Change (MAJOR)**:
- System MUST evaluate compatibility with current version
- If current version is within supported range, MAY continue (see Section 6)
- If current version is deprecated or EOL, MUST escalate
- System SHOULD schedule update during maintenance window

**Unknown or Invalid Version**:
- System MUST treat as configuration error
- System MUST escalate to operator
- System MUST NOT proceed with governance-dependent operations

---

## 6. Compatibility Expectations

### 6.1 Backward Compatibility Guarantee

Per **VERSIONING_AND_EVOLUTION_GOVERNANCE.md** and **GOVERNANCE_RIPPLE_MODEL.md**:

**MINOR and PATCH versions MUST maintain backward compatibility**:
- Previously compliant behavior remains compliant
- Existing schemas remain valid
- Existing gates pass with same criteria
- Historical PRs remain valid under historical version rules

**MAJOR versions MAY break compatibility**:
- Breaking changes require explicit migration guidance
- Deprecation period MUST be provided (see Section 6.3)
- Migration path MUST be documented
- Historical compliance MUST be preserved (no retroactive invalidation)

### 6.2 Forward Compatibility Expectations

Execution systems SHOULD be designed for forward compatibility:

**Ignore Unknown Fields**:
- Systems loading governance schemas SHOULD ignore unrecognized fields
- New optional schema fields SHOULD NOT break older parsers
- Graceful degradation is preferred over strict validation failure

**Version Negotiation**:
- Systems MAY support multiple governance versions during transition
- Systems SHOULD declare which governance version they are operating under
- Systems MUST NOT silently mix governance versions

**Feature Detection**:
- Systems SHOULD detect feature availability, not version-detect
- Check for presence of specific governance documents/rules
- Fall back to safe defaults if feature not available

### 6.3 Deprecation and Transition Semantics

Per **GOVERNANCE_RIPPLE_MODEL.md**, breaking changes require managed transition:

**Deprecation Notice**:
- MUST be announced at least 2 weeks before effective date for non-emergency changes
- MUST include deprecation timeline
- MUST identify what is being deprecated
- MUST provide migration guidance

**Transition Period**:
- Minimum 2 weeks for MAJOR non-emergency changes
- Old and new versions BOTH valid during transition
- Clear cutover date MUST be announced
- Migration support MUST be provided

**Version Support Window**:
- Current MAJOR version: Fully supported
- Previous MAJOR version (N-1): Maintenance support during transition period
- Older MAJOR versions (N-2 and earlier): No support, deprecated

**Example**:
```
governance-v1.0.0 → Current, fully supported
governance-v2.0.0 announced → Transition begins
  (Both v1 and v2 valid for 2 weeks)
governance-v2.0.0 effective → v1.0.0 deprecated
  (v2 current, v1 maintenance only)
governance-v3.0.0 announced → v1.0.0 reaches EOL
  (v3 transition, v2 current, v1 EOL)
```

---

**[Document continues with sections 7-19 as in the original file]**

---

**End of GOVERNANCE VERSIONING AND SYNC PROTOCOL**

---

**Document Metadata**:
- Policy ID: GOVERNANCE_VERSIONING_AND_SYNC_PROTOCOL_V1
- Authority: Canonical Governance Protocol
- Version: v1.0.0
- Effective Date: 2025-12-23
- Resolves: Wiring Gap W-001 (Governance Dependency & Activation Scan)
- Integration: VERSIONING_AND_EVOLUTION_GOVERNANCE.md, GOVERNANCE_RIPPLE_MODEL.md, FM_GOVERNANCE_LOADING_PROTOCOL.md
- Enforcement: Governance Administrator (custodial)

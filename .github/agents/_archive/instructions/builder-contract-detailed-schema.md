# Builder Contract Detailed Schema Specification

**Purpose**: Detailed field-by-field specification for BUILDER_CONTRACT_SCHEMA.md  
**Authority**: BUILDER_CONTRACT_SCHEMA.md v2.0  
**Extracted**: 2026-02-12 (Living Agent System v6.2.0 character limit remediation)

---

## Required YAML Frontmatter Fields

### 🔴 GitHub Copilot Agent Fields (REQUIRED FOR SELECTABILITY)

**These fields are MANDATORY for GitHub Copilot agent loader integration.**
**Without these fields, builders will appear in agent selector but will NOT be selectable.**

These fields must be placed **at the top** of the YAML frontmatter, before Maturion-specific fields.

#### 1. name (REQUIRED)

**Type**: `string`
**Description**: Display name shown in GitHub Copilot agent selector
**Example**: `name: API Builder`

**Validation**:
- Must be human-readable (title case recommended)
- Should clearly identify the builder's role
- Typically matches `<builder-id>` but formatted for display

**Critical**: Missing this field prevents agent selection.

---

#### 2. role (REQUIRED)

**Type**: `string`
**Description**: Agent role designation for GitHub Copilot platform
**Allowed Values**: `builder` (for all Maturion builders)
**Example**: `role: builder`

**Validation**:
- Must be exactly `builder` for all Maturion builder agents
- Other roles (e.g., `fm`, `liaison`) are used for non-builder agents

**Critical**: Missing this field prevents agent selection.

---

#### 3. description (REQUIRED)

**Type**: `string` (multi-line with `>` YAML syntax)
**Description**: Multi-line description of builder purpose, constraints, and doctrine
**Example**:
```yaml
description: >
  API Builder for Maturion ISMS modules. Implements backend API endpoints, request handlers,
  and business logic according to frozen architecture specifications. Operates under
  Maturion Build Philosophy: Architecture → QA-to-Red → Build-to-Green → Validation.
  MUST NOT modify UI, schema, or governance artifacts.
```

**Content Requirements**:
- Must describe builder's primary purpose
- Must mention key constraints (what builder MUST NOT do)
- Should reference Maturion Build Philosophy
- Should be 2-4 sentences for clarity

**Validation**:
- Must be present (empty string not allowed)
- Should be descriptive (50+ characters recommended)
- Must use `>` for multi-line folding

**Critical**: Missing this field is the most common cause of "Invalid config" errors.

---

### 🔵 Maturion Builder Identity Fields (REQUIRED)

These fields define the builder's Maturion-specific identity and must follow the GitHub Copilot fields.

#### 4. builder_id (REQUIRED)

**Type**: `string`
**Description**: Unique identifier for this builder
**Format**: `lowercase-with-hyphens`
**Example**: `ui-builder`

**Validation**:
- Must match filename (e.g., `ui-builder.md` → `builder_id: ui-builder`)
- Must be unique across all builders
- Must contain only lowercase letters, numbers, and hyphens

#### 5. builder_type (REQUIRED)

**Type**: `string`
**Description**: Classification of builder role
**Allowed Values**:
- `specialized` — Domain-specific builder (UI, API, schema, integration)
- `qa` — Quality assurance and testing builder
- `cross-cutting` — Builders that span multiple domains (rare)

**Example**: `builder_type: specialized`

#### 6. version (REQUIRED)

**Type**: `string`
**Description**: Contract version (semantic versioning)
**Format**: `major.minor.patch`
**Example**: `version: 1.0.0`

#### 7. status (REQUIRED)

**Type**: `string`
**Description**: Current recruitment status
**Allowed Values**:
- `recruited` — Builder recruited and ready for assignment
- `active` — Builder actively working on assigned tasks
- `suspended` — Builder temporarily unavailable
- `revoked` — Builder recruitment revoked (no longer usable)

**Example**: `status: recruited`

#### 8. capabilities (REQUIRED)

**Type**: `array of strings`
**Description**: List of technical capabilities this builder possesses
**Example**:
```yaml
capabilities:
  - ui
  - frontend
  - components
  - styling
```

**Validation**:
- Must contain at least 1 capability
- Capabilities must be lowercase, single-word or hyphenated
- Must align with `foreman/builder/builder-capability-map.json`

#### 9. responsibilities (REQUIRED)

**Type**: `array of strings`
**Description**: High-level responsibilities assigned to this builder
**Example**:
```yaml
responsibilities:
  - UI components
  - Layouts
  - Wizards
```

**Validation**:
- Must contain at least 1 responsibility
- Must align with `foreman/builder-manifest.json`

#### 10. forbidden (REQUIRED)

**Type**: `array of strings`
**Description**: Actions or areas this builder MUST NOT perform or access
**Example**:
```yaml
forbidden:
  - Backend logic
  - Cross-module logic
  - Database schema changes
```

**Validation**:
- Must contain at least 1 forbidden action
- Must align with `foreman/builder-manifest.json`

#### 11. permissions (REQUIRED)

**Type**: `object`
**Description**: File system access permissions
**Structure**:
```yaml
permissions:
  read:
    - <glob-pattern>
  write:
    - <glob-pattern>
```

**Example**:
```yaml
permissions:
  read:
    - "foreman/**"
    - "architecture/**"
    - "governance/**"
  write:
    - "apps/*/frontend/**"
    - "apps/*/components/**"
```

**Validation**:
- Must contain at least one `read` pattern
- Must contain at least one `write` pattern
- Must align with `foreman/builder/builder-permission-policy.json`

#### 12. recruitment_date (REQUIRED)

**Type**: `string`
**Description**: ISO 8601 date when builder was recruited
**Format**: `YYYY-MM-DD`
**Example**: `recruitment_date: 2025-12-30`

---

## 🔴 Maturion Doctrine Fields (REQUIRED)

**These fields are MANDATORY as of Schema Version 2.0.**
**Without these fields, builder contracts CANNOT validate.**

#### 13. canonical_authorities (REQUIRED)

**Type**: `array of strings`
**Description**: List of canonical governance sources this builder is bound to
**Purpose**: Establish constitutional supremacy, prevent "generic developer" execution, and ensure ripple intelligence alignment

**MUST Include**:
```yaml
canonical_authorities:
  - BUILD_PHILOSOPHY.md
  - foreman/builder-specs/build-to-green-rule.md
  - .github/agents/ForemanApp-agent.md
  - governance/alignment/GOVERNANCE_RIPPLE_COMPATIBILITY.md
```

**Additional authorities may be added** (e.g., domain-specific specs).

**Ripple Intelligence Requirement**:
- The `governance/alignment/GOVERNANCE_RIPPLE_COMPATIBILITY.md` authority ensures builders are aware of ripple intelligence obligations
- Builders MUST NOT be appointed if this authority is missing from their canonical_authorities list
- This prevents builders from being appointed with stale governance assumptions

**Validation**:
- Must contain at least the 4 mandatory authorities listed above (including GOVERNANCE_RIPPLE_COMPATIBILITY.md)
- All paths must exist in repository
- Authorities must be immutable (constitutional files)
- Ripple intelligence authority ensures governance-current context at appointment time

**Example**:
```yaml
canonical_authorities:
  - BUILD_PHILOSOPHY.md
  - foreman/builder-specs/build-to-green-rule.md
  - .github/agents/ForemanApp-agent.md
  - governance/alignment/GOVERNANCE_RIPPLE_COMPATIBILITY.md
  - foreman/builder/ui-builder-spec.md
```

---

#### 14. maturion_doctrine_version (REQUIRED)

**Type**: `string`
**Description**: Version of Maturion Build Philosophy this contract conforms to
**Format**: `major.minor.patch`
**Current Version**: `1.0.0`

**Example**: `maturion_doctrine_version: "1.0.0"`

**Validation**:
- Must be valid semantic version
- Must match BUILD_PHILOSOPHY.md version (currently 1.0.0)
- Future doctrine upgrades may require contract updates

---

#### 15. handover_protocol (REQUIRED)

**Type**: `string`
**Description**: Handover semantics this builder uses
**Allowed Values**: `gate-first-deterministic`

**Example**: `handover_protocol: "gate-first-deterministic"`

**Meaning**:
- Work is complete ONLY when gates are satisfied
- No silent execution paths
- Evidence is linkable and audit-ready
- No reinterpretation of gate conditions

**Validation**: Must be exactly `gate-first-deterministic`

---

#### 16. no_debt_rules (REQUIRED)

**Type**: `string`
**Description**: Test debt policy this builder follows
**Allowed Values**: `zero-test-debt-mandatory`

**Example**: `no_debt_rules: "zero-test-debt-mandatory"`

**Meaning**:
- No .skip()
- No .todo()
- No commented-out tests
- No incomplete tests (stubs, no assertions)
- Any test debt = STOP → FIX → RE-RUN → VERIFY

**Validation**: Must be exactly `zero-test-debt-mandatory`

---

#### 17. evidence_requirements (REQUIRED)

**Type**: `string`
**Description**: Evidence trail policy this builder follows
**Allowed Values**: `complete-audit-trail-mandatory`

**Example**: `evidence_requirements: "complete-audit-trail-mandatory"`

**Meaning**:
- Build initiation evidence required
- Validation evidence required
- Iteration evidence required (per iteration)
- Final validation evidence required
- Completion evidence required
- Evidence must be stored in designated locations

**Validation**: Must be exactly `complete-audit-trail-mandatory`

---

#### 18. qa_range (OPTIONAL)

**Type**: `object`
**Description**: QA range assignment for builders in build waves
**Structure**:
```yaml
qa_range:
  start: <qa-id>
  end: <qa-id>
  count: <integer>
```

**Example**:
```yaml
qa_range:
  start: QA-019
  end: QA-057
  count: 39
```

**When Required**: During build wave assignment (Wave 1.0+), not during initial recruitment

---

**Reference**: See `.github/agents/BUILDER_CONTRACT_SCHEMA.md` for complete schema, validation rules, and enforcement requirements.

**Authority**: Living Agent System v6.2.0 | BUILDER_CONTRACT_SCHEMA.md v2.0

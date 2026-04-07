# Foreman Agent - Operational Procedures

**Authority**: LIVING_AGENT_SYSTEM v5.0.0  
**Agent**: foreman-agent  
**Version**: 5.0.1  
**Last Updated**: 2026-02-09

This file contains operational procedures for the Foreman agent including workspace management, wake-up protocol, wave planning, and merge gate management.

## Operational Sandbox (Section 12 of FM_ROLE_CANON.md)

### Workspace Structure
```
.agent-workspace/foreman/
├── memory/
│   ├── constitutional/     # Tier-0 canon (permanent)
│   ├── learnings/          # Learning memory (permanent, growing)
│   └── sessions/           # Session logs (temporary)
├── execution-progress/     # Wave progress artifacts
│   ├── waves/
│   │   └── [wave-id]/
│   │       ├── wave-plan.md
│   │       ├── progress.md
│   │       ├── issues/
│   │       └── evidence/
│   └── current-wave.md
└── evidence/               # Architecture, QA, validation artifacts
    ├── architecture/
    ├── qa/
    └── validation/
```

### Execution Directory
**Primary**: `.agent-workspace/foreman/execution-progress/`
- Wave progress artifacts
- Issue tracking
- Builder coordination logs
- Validation evidence

### Evidence Directory
**Primary**: `.agent-workspace/foreman/evidence/`
- Architecture specifications
- QA catalog and test suites
- Validation reports
- Gate compliance evidence

### Network Access
- ✅ **Read**: Canonical governance repository (APGI-cmy/maturion-foreman-governance)
- ✅ **Read/Write**: Consumer repository (this repository)
- ❌ **No direct database access** (runtime only, FM is build-time)
- ❌ **No production system access** (runtime only, FM is build-time)

### Prohibited Actions in Operational Sandbox
- ❌ No direct database access
- ❌ No production system modification
- ❌ No secret exposure or logging
- ❌ No cross-tenant operations
- ❌ No GitHub platform actions (create PR, merge, etc.) - request Maturion instead

---

## Wave Planning & Issue Artifact Generation

**Authority**: FOREMAN_WAVE_PLANNING_AND_ISSUE_ARTIFACT_GENERATION_PROTOCOL.md v1.0.0

### Wave Decomposition Strategy
1. **Analyze complexity** - Assess scope, dependencies, risk
2. **Identify subwaves** - Break down if complexity exceeds cognitive load
3. **Define success criteria** - Clear, testable, evidence-based
4. **Generate wave plan** - Architecture → QA-to-Red → Build-to-Green → Validation

### Subwave Identification
Subwave required when:
- Complexity exceeds single-wave cognitive load
- Multiple domains require sequential execution
- Risk of cascading failures
- Dependencies require phased approach

### Issue Artifact Generation Workflow
```
1. Wave Initialization
   └─> Wave Init Issue (template: governance/templates/wave-init.md)
       ├─ Wave objectives
       ├─ Success criteria
       ├─ Architecture scope
       └─ QA requirements

2. Builder Task Assignment
   └─> Builder Task Issues (template: governance/templates/builder-task.md)
       ├─ Frozen architecture reference
       ├─ Build-to-Green instruction
       ├─ QA catalog reference
       └─ Acceptance criteria

3. Correction/RCA
   └─> RCA Issue (template: governance/templates/rca.md)
       ├─ Failure description
       ├─ Root cause analysis
       ├─ Corrective action
       └─ Prevention measures

4. Governance Gap
   └─> Governance Gap Issue (template: governance/templates/governance-gap.md)
       ├─ Gap description
       ├─ Impact analysis
       ├─ Escalation path
       └─ Temporary mitigation
```

### Wave Progress Tracking
All wave progress tracked in:
- `.agent-workspace/foreman/execution-progress/waves/[wave-id]/progress.md`
- Updated after each builder task completion
- Evidence-linked (architecture, QA, validation)
- Audit-ready format

### Wave Closure Certification
FM certifies wave closure when:
- ✅ All architecture implemented and validated
- ✅ All QA passing (100% GREEN)
- ✅ Zero test debt
- ✅ Zero warnings
- ✅ All gates passed
- ✅ Evidence trail complete
- ✅ IBWR executed
- ✅ Learnings captured

---

## Wake-Up Protocol

**Authority**: LIVING_AGENT_SYSTEM v5.0.0

FM executes the following phases during session initialization (wake-up):

### Phase 1: Environment Scan
- Verify repository structure integrity
- Check governance file presence
- Validate `.agent-workspace` structure
- Confirm canonical governance availability

### Phase 2: Governance Scan
- Load Tier-0 Canon Manifest
- Verify all 15 constitutional documents accessible
- Check governance version alignment
- Validate binding completeness

### Phase 3: Session Contract
- Read session scope (issue/PR context)
- Load relevant wave memory (if continuing wave)
- Identify builder assignments (if any)
- Establish session objectives

### Phase 4: Session Memory
- Initialize session memory structure
- Load constitutional memory (Level 1)
- Load wave memory if applicable (Level 2)
- Create session memory workspace (Level 3)

### Phase 5: Pre-Handover Validation
- Check for pending builder PREHANDOVER_PROOF
- Validate evidence completeness
- Verify QA status (100% GREEN requirement)
- Check gate readiness

### Phase 6: Merge Gate Health Check

**Purpose**: Ensure merge gates are aligned with current governance and agent-role applicability

**Authority**: FM_MERGE_GATE_MANAGEMENT_PROTOCOL.md (canonical)

**Actions**:
1. List all workflows in `.github/workflows/`
2. For each gate workflow:
   - Check if gate references canonical governance (file + section)
   - Check if gate implements agent role checking (per MERGE_GATE_APPLICABILITY_MATRIX.md)
   - Check if gate implements evidence-based validation pattern (PREHANDOVER_PROOF)
   - Verify gate logic matches current governance canon
3. Identify misaligned gates:
   - Gate enforces rule not in current governance
   - Gate applies to wrong agent class
   - Gate has known bugs or syntax errors
   - Gate missing evidence-based validation pattern
4. Document gate health status in session memory:
   - Total gates: [count]
   - Aligned gates: [count]
   - Misaligned gates: [list with reasons]
   - Action required: [autonomous fix | escalation | none]
5. For misaligned gates:
   - **If gate bug or canon drift**: Flag for autonomous fix (FM's sandbox authority)
   - **If governance ambiguity**: Flag for escalation to CS2
   - Document action plan in session memory

**Exit Criteria**:
- ✅ All gates inventoried
- ✅ Gate health status documented
- ✅ Misalignments flagged with action plan (fix or escalate)
- ✅ Session memory updated with gate health report

**Output**: `.agent-admin/sessions/foreman/gate-health-check.md`

**Frequency**: Every wake-up (session initialization)

### Ready State
After completing all 6 phases, FM is ready to:
- Execute assigned tasks
- Respond to builder escalations
- Monitor build progress
- Enforce governance requirements

---

## Merge Gate Management Authority

**Authority**: FM_MERGE_GATE_MANAGEMENT_PROTOCOL.md (canonical)  
**Protocol**: APGI-cmy/maturion-foreman-governance#1060 (governance canon)

### FM's Role in Merge Gate Management

Foreman is responsible for **continuous monitoring, maintenance, and alignment** of merge gates (`.github/workflows/*.yml`) to ensure gates enforce current governance without blocking valid work.

### Autonomous Fix Authority (Within Sandbox)

**FM CAN autonomously fix**:
- ✅ **Gate workflow bugs**: Syntax errors, path check errors, logic errors
- ✅ **Gate-canon drift**: Canon updated, gate enforces old rule
- ✅ **Agent role misapplication**: Gate applies to wrong agent class
- ✅ **Evidence pattern mismatch**: Gate checks wrong PREHANDOVER_PROOF keywords
- ✅ **Workflow trigger corrections**: Gate triggered by wrong paths or events

**Process**:
1. Detect misalignment (via Phase 6 gate health check or agent escalation)
2. Diagnose root cause (gate-side issue vs. build-side issue vs. governance gap)
3. If gate-side issue: Fix autonomously
4. Update gate workflow file (`.github/workflows/*.yml`)
5. Document fix in session memory
6. No escalation required (within sandbox)

### Mandatory Escalation (Outside Sandbox)

**FM MUST escalate to CS2 when**:
- ❌ **Governance ambiguity**: Gate enforces rule not clearly defined in governance
- ❌ **Governance conflict**: Two governance documents conflict, gate caught between
- ❌ **Constitutional gap**: Gate reveals missing governance requirement
- ❌ **Authority boundary unclear**: FM unsure if fix requires governance change
- ❌ **New enforcement rule**: Gate needs rule not in current governance
- ❌ **Blocking severity change**: Gate blocking behavior needs adjustment
- ❌ **Gate applicability change**: Which agents use this gate needs clarification

**Escalation Format**: Create GitHub issue in governance repo:
```
Title: [GATE-ESCALATION] [gate-name.yml] [Issue Type]

Body:
## Merge Gate Escalation

**Gate**: [gate-name.yml]
**Trigger**: [PR number, agent role, failure reason]
**Issue Type**: [Governance Ambiguity | Conflict | Gap | Authority Boundary]

### Problem
[Describe what gate is enforcing and why FM cannot resolve]

### Governance Review
**Current Canon**: [Link to governance document gate references]
**Gate Logic**: [Relevant workflow code snippet]
**Conflict**: [Describe ambiguity/conflict/gap]

### FM's Assessment
**Options Considered**:
1. [Option 1 - why FM cannot autonomously choose]
2. [Option 2 - why FM cannot autonomously choose]

**FM Recommendation**: [What FM thinks governance should clarify]

### Requested CS2 Action
- [ ] Clarify governance rule
- [ ] Update canonical governance
- [ ] Authorize FM fix
- [ ] Disable gate pending resolution

**Blocking**: [Is this blocking current work? Which PR?]
```

### Continuous Monitoring

**FM monitors merge gates**:
- During wake-up (Phase 6 gate health check)
- When builder/liaison escalates gate failure
- When PR gate failures detected in CI logs
- After governance updates (canon version changes)

**FM maintains**:
- Gate health status in session memory
- Gate fix history (what was fixed, when, why)
- Gate escalation history (what was escalated, resolution)

### Integration with Agent Escalations

**When builder/liaison escalates gate failure**:
1. Builder/Liaison stops work, escalates to FM (not CS2)
2. FM investigates:
   - **Build-side issue?** → Redirect to builder for fix
   - **Gate-side issue?** → FM fixes autonomously
   - **Governance ambiguity?** → FM escalates to CS2
3. FM documents resolution in session memory
4. Builder/Liaison retries after FM fix or governance clarification

**Builder/Liaison DOES NOT**:
- Fix merge gates directly (no authority)
- Escalate directly to CS2 (FM is first responder)
- Bypass gates (CS1-CS6 enforcement absolute)

### Reference to Canonical Protocols

**This section references**:
- `governance/canon/FM_MERGE_GATE_MANAGEMENT_PROTOCOL.md` (comprehensive protocol)
- `governance/canon/MERGE_GATE_APPLICABILITY_MATRIX.md` (agent-role gate mapping)
- `governance/canon/MERGE_GATE_PHILOSOPHY.md` (gate philosophy and evidence-based validation)
- `governance/canon/AGENT_CLASS_SPECIFIC_GATE_PROTOCOLS.md` (gate requirements per agent class)

**Note**: These canonical protocols are being created via APGI-cmy/maturion-foreman-governance#1060. This PR can be merged AFTER protocols are layered down to this repository.

---

## Memory Management (FOREMAN_MEMORY_PROTOCOL.md)

FM maintains 4-level memory hierarchy:

### Level 1: Constitutional Memory (Permanent)
- Tier-0 canon documents (15 constitutional documents)
- BUILD_PHILOSOPHY.md
- Core governance principles
- **Lifecycle**: Permanent, never purged

### Level 2: Wave Memory (Wave Lifecycle)
- Wave-specific context and objectives
- Wave architecture decisions
- Wave QA catalog
- Wave learnings and patterns
- **Lifecycle**: Active during wave, archived at wave closure
- **Location**: `.agent-workspace/foreman/waves/[wave-id]/`

### Level 3: Session Memory (Session Lifecycle)
- Within-session context
- Current task state
- Active builder assignments
- In-progress validations
- **Lifecycle**: Active during session, discarded at session end

### Level 4: Learning Memory (Permanent, Growing)
- Recurring issue patterns
- Effective solutions
- Governance gap discoveries
- Escalation patterns
- **Lifecycle**: Permanent, continuously growing
- **Location**: `.agent-workspace/foreman/learnings/`

---

**Living Agent System v5.0.0** | **Agent**: Foreman | **Module**: Operational Procedures

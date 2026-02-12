# Lessons Learned

## Session 20260212 (Bootstrap Governance Evolution)

### Lesson: Evidence-First Design Methodology
- Context: Creating new governance infrastructure
- Pattern: Audit → Gap Analysis → Design → Implementation
- Action: Always start with baseline audit before designing solutions
- Rationale: Provides clear traceability and justification for every decision

### Lesson: Standard Interface Enables Scalability
- Context: Consolidating 16 workflow gates into 3 standard jobs
- Pattern: Multiple implementations → Single standard interface
- Action: When governance becomes complex, consolidate behind standard interface
- Rationale: Branch protection can be consistent across all repos, simpler mental model

### Lesson: Bootstrap Documentation Prevents Confusion
- Context: Creating gates that will evaluate future PRs
- Pattern: New rules applying to rule-creating PR (paradox)
- Action: Always document bootstrap transitions explicitly (old law vs new law)
- Rationale: Prevents confusion about which rules apply during transition

### Lesson: Evidence-First Error Messages are Critical
- Context: Gate failures must be self-remediating
- Pattern: Error + Exact Path + Required Schema + Remediation Steps
- Action: Never require log archaeology - provide complete error context
- Rationale: Reduces agent debugging time, enables self-service remediation

### Lesson: Machine-Readable Evidence Enables Automation
- Context: Gate results must be machine-processable
- Pattern: JSON schema validation + immutability + timestamps
- Action: Always provide machine-readable artifacts alongside human-readable ones
- Rationale: Enables automated compliance checking, auditing, and reporting

### Lesson: Protocol Scripts Must Handle Degraded Mode
- Context: Wake-up script failed due to missing agent contract
- Pattern: Unexpected environment state during execution
- Action: Design scripts to gracefully handle missing/degraded inputs
- Rationale: Real-world environments are never perfect - scripts must be resilient

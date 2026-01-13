# Builder Attestations - Test Execution Protocol & BL-026

**Purpose**: Store builder agent attestations for:
1. Agent Test Execution Protocol (CI-Confirmatory-Not-Diagnostic)
2. BL-026/T0-015 Automated Deprecation Detection

**Status**: Active Collection  
**Authority**: Governance Administrator + FM  
**Date**: 2026-01-13

---

## Directory Structure

```
builder-attestations/
├── README.md (this file)
├── test-execution-protocol/
│   ├── ui-builder-attestation.md
│   ├── api-builder-attestation.md
│   ├── schema-builder-attestation.md
│   ├── integration-builder-attestation.md
│   └── qa-builder-attestation.md
├── bl-026-deprecation/
│   ├── ui-builder-attestation.md
│   ├── api-builder-attestation.md
│   ├── schema-builder-attestation.md
│   ├── integration-builder-attestation.md
│   └── qa-builder-attestation.md
└── training-records.json
```

---

## Attestation Requirements

### Test Execution Protocol Attestation

Each builder must attest to:
- ✅ Understanding CI is confirmatory, not diagnostic
- ✅ All tests executed locally before PR creation
- ✅ PREHANDOVER_PROOF mandatory for all PRs
- ✅ Zero test failures/warnings before handover
- ✅ Exception process requires FM approval
- ✅ Violations are catastrophic and block work

**Template**: See `governance/runbooks/AGENT_TEST_EXECUTION_PROTOCOL.md` (Attestation Format section)

### BL-026 Deprecation Attestation

Each builder must attest to:
- ✅ Understanding BL-026 is Tier-0 constitutional (T0-015)
- ✅ Running `ruff check --select UP` before all PRs
- ✅ Remediating all deprecated API violations
- ✅ Zero deprecation debt mandatory
- ✅ Exception process requires FM approval with quarterly review
- ✅ Violations constitute test debt and block build-to-green

**Reference**: `governance/policies/AUTOMATED_DEPRECATION_DETECTION_GATE.md`

---

## Training Process

### Step 1: Protocol Reading
Builder reads:
1. `governance/runbooks/AGENT_TEST_EXECUTION_PROTOCOL.md`
2. `governance/policies/AUTOMATED_DEPRECATION_DETECTION_GATE.md`
3. `.github/PULL_REQUEST_TEMPLATE.md` (PREHANDOVER_PROOF section)

### Step 2: Practical Exercise
Builder demonstrates:
1. Running tests locally in practice environment
2. Creating sample PREHANDOVER_PROOF
3. Running BL-026 deprecation check
4. Interpreting test/check outputs

### Step 3: Attestation Submission
Builder creates attestation files:
1. `test-execution-protocol/[builder-id]-attestation.md`
2. `bl-026-deprecation/[builder-id]-attestation.md`

### Step 4: Verification
FM verifies:
- Attestations complete and signed
- Builder demonstrates understanding
- Practical exercise successful
- Training record updated

---

## Training Records

Track in `training-records.json`:

```json
{
  "version": "1.0.0",
  "last_updated": "2026-01-13T00:00:00Z",
  "builders": [
    {
      "builder_id": "ui-builder",
      "builder_name": "UI Builder",
      "training_date": "2026-01-XX",
      "protocols_trained": [
        {
          "protocol": "test-execution-protocol",
          "version": "1.0.0",
          "status": "pending|complete",
          "attestation_file": "test-execution-protocol/ui-builder-attestation.md",
          "trainer": "FM|Governance"
        },
        {
          "protocol": "bl-026-deprecation",
          "version": "1.0.0",
          "status": "pending|complete",
          "attestation_file": "bl-026-deprecation/ui-builder-attestation.md",
          "trainer": "FM|Governance"
        }
      ],
      "next_review": "2026-04-13"
    }
  ]
}
```

---

## Compliance Tracking

### Mandatory Before Task Assignment

Builder CANNOT be assigned new tasks until:
- Both attestations submitted and verified
- Training record shows "complete" status
- FM/Governance approval recorded

### Quarterly Review

Every quarter:
- Review all attestations
- Update training if protocols change
- Collect re-attestations if major changes
- Track protocol violations per builder

---

## Attestation Status

| Builder | Test Execution | BL-026 | Status | Notes |
|---------|----------------|--------|--------|-------|
| ui-builder | PENDING | PENDING | BLOCKED | Training scheduled |
| api-builder | PENDING | PENDING | BLOCKED | Training scheduled |
| schema-builder | PENDING | PENDING | BLOCKED | Training scheduled |
| integration-builder | PENDING | PENDING | BLOCKED | Training scheduled |
| qa-builder | PENDING | PENDING | BLOCKED | Training scheduled |

**Update this table as attestations are collected.**

---

## References

- **Test Execution Protocol**: `governance/runbooks/AGENT_TEST_EXECUTION_PROTOCOL.md`
- **BL-026 Policy**: `governance/policies/AUTOMATED_DEPRECATION_DETECTION_GATE.md`
- **PR Template**: `.github/PULL_REQUEST_TEMPLATE.md`
- **Training Spec**: `governance/BUILDER_TRAINING_CHECKLIST.md`

---

## Contact

- **Training Questions**: FM (Foreman)
- **Governance Questions**: Governance Administrator
- **Constitutional Matters**: Johan Ras

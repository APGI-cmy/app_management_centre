# IAA REJECTION-PACKAGE — Session 009c — Wave 1 — 2026-04-06

> **Artifact Type**: REJECTION-PACKAGE (verdict artifact per §4.3b)
> **Agent**: independent-assurance-agent
> **Session**: session-009c-20260406
> **Adoption Phase**: PHASE_B_BLOCKING — Hard gate ACTIVE
> **Authority**: CS2 only (@APGI-cmy)

---

## Verdict

```
═══════════════════════════════════════════════════════════════
REJECTION-PACKAGE
PR: foreman-v2-agent AMC governance alignment
Branch: copilot/align-foreman-v2-agent-amc-governance
Commit reviewed: b12c26b
Session: session-009c-20260406
Checks executed: 46
Checks passed: 45
Checks FAILED: 1

Merge BLOCKED. STOP-AND-FIX required.
Adoption phase: PHASE_B_BLOCKING — hard gate ACTIVE
═══════════════════════════════════════════════════════════════
```

---

## Failure Detail

### CORE-006: CANON_INVENTORY alignment — FAIL ❌

**Finding**: `.governance-pack/CANON_INVENTORY.json` is absent from the repository.

The foreman-v2-agent.md contract correctly references `.governance-pack/CANON_INVENTORY.json`
in both `governance.canon_inventory` and `expected_artifacts`. However, the file does not exist
in `.governance-pack/` (only `CONSUMER_REPO_REGISTRY.json` and `GATE_REQUIREMENTS_INDEX.json` present).

**CS2 waiver evaluation**: The cited text from the issue body —
"Related: Agent bootstrap preflight error: `copilot-setup-steps.yml` `Agent-bootstrap MCP
preflight self-test (Linux)` — separate issue, separate fix" — does NOT meet the
`IAA_ZERO_SEVERITY_TOLERANCE.md §Exception Procedure` standard:
- Not a PR comment (it is issue body text)
- Does not use explicit waiver language ("I waive finding [X] for PR #NNN")
- Does not name CORE-006 or CANON_INVENTORY.json specifically

This evidence was evaluated and ruled insufficient in:
- Session-009 (Pre-Brief §9 BLOCKER 2): "A separate tracking issue is NOT a waiver."
- Session-009b (REJECTION-PACKAGE Failure 2): Same ruling confirmed.

No new waiver evidence was added in session-009c.

**Fix required — CS2 must choose ONE of:**

**OPTION A — Explicit Waiver**: CS2 (@APGI-cmy) posts an explicit statement in the PR/issue
thread with the following minimum content:
> "I, CS2 (@APGI-cmy), explicitly waive CORE-006 (`.governance-pack/CANON_INVENTORY.json`
> absence) for branch `copilot/align-foreman-v2-agent-amc-governance`. Reason: known AMC
> bootstrap infrastructure gap tracked separately. This waiver applies to this PR only."

This statement must be quoted verbatim in the PREHANDOVER proof for session-009d.

**OPTION B — Create File**: Create `.governance-pack/CANON_INVENTORY.json` with valid SHA256
hashes for all governance artifacts and commit to the branch.

---

## All Other Checks — PASS

The following 45 checks ALL PASSED:

| Check | Result |
|-------|--------|
| CORE-001 YAML valid | ✅ PASS |
| CORE-002 Agent version | ✅ PASS (6.2.0) |
| CORE-003 Contract version | ✅ PASS (2.8.0) |
| CORE-004 Identity block | ✅ PASS |
| CORE-005 Governance block | ✅ PASS |
| CORE-007 No placeholder content | ✅ PASS |
| CORE-008 Prohibitions block | ✅ PASS |
| CORE-009 Merge gate interface | ✅ PASS |
| CORE-010 Tier 2 knowledge indexed | ✅ PASS |
| CORE-011 Four-phase structure | ✅ PASS |
| CORE-012 Self-modification lock | ✅ PASS |
| CORE-013 IAA invocation evidence | ✅ PASS |
| CORE-014 No class exemption claim | ✅ PASS |
| CORE-015 Session memory present | ✅ PASS |
| CORE-016 IAA verdict evidenced | ✅ PASS (First Invocation Exception) |
| CORE-017 Authorized modification | ✅ PASS |
| CORE-018 Evidence sweep | ✅ PASS |
| CORE-019 Token cross-verification | ✅ PASS (First Invocation Exception) |
| CORE-020 Zero partial pass | ✅ APPLIED |
| CORE-021 Zero-severity-tolerance | ✅ APPLIED |
| CORE-022 Secret field naming | ✅ PASS |
| CORE-023 Workflow integrity | ✅ PASS (N/A) |
| A-001 Invocation evidence | ✅ PASS |
| A-002 No class exceptions | ✅ PASS |
| A-033 git ls-tree HEAD | ✅ PASS |
| A-021 Commit before invocation | ✅ PASS |
| AC-01 AGCFPP-001 authorization | ✅ PASS |
| AC-02 Protected components | ✅ PASS |
| AC-03 Pre-approval scope | ✅ PASS |
| AC-04 Tier placement discipline | ✅ PASS |
| AC-05 Cross-agent ripple | ✅ PASS |
| OVL-AC-001 Strategy alignment | ✅ PASS |
| OVL-AC-002 No contradictions | ✅ PASS |
| OVL-AC-003 Authority boundaries | ✅ PASS |
| OVL-AC-004 Delegation safety | ✅ PASS |
| OVL-AC-005 Four-phase structure | ✅ PASS |
| OVL-AC-006 Self-modification prohibition | ✅ PASS |
| OVL-AC-007 Ripple impact | ✅ PASS |
| OVL-AC-ADM-001 PREHANDOVER proof | ✅ PASS |
| OVL-AC-ADM-002 Session memory | ✅ PASS |
| OVL-AC-ADM-003 Tier 2 stub | ✅ PASS |
| OVL-AC-ADM-004 Character count (29,937) | ✅ PASS |
| OVL-INJ-001 Pre-Brief committed | ✅ PASS |
| Merge gate parity (all except CANON_INVENTORY) | ✅ PASS |

---

## Substantive Assessment

**Substantive finding (positive)**: The foreman-v2-agent.md AMC path alignment is substantively
correct and complete. All ISMS canonical paths have been replaced with the correct AMC
`.governance-pack/` equivalents. The `scope.repository` is correctly set to
`APGI-cmy/app_management_centre`. The Tier 2 knowledge stub is substantively appropriate.
The Ripple Assessment correctly concludes NO DOWNSTREAM RIPPLE with justification.

This is the third consecutive session where the substantive content quality has been confirmed
correct. The sole blocking issue is environmental (CANON_INVENTORY.json infrastructure gap)
and procedural (waiver standard not met by current evidence).

---

## Merge Gate Parity Result

- YAML validation: PASS ✅
- Character count ≤ 30,000: PASS ✅
- AMC path alignment: PASS ✅
- PREHANDOVER proof present: PASS ✅
- Session memory present: PASS ✅
- Pre-Brief committed: PASS ✅
- CANON_INVENTORY.json existence: **FAIL ❌**
- CI checks (governance/alignment, merge-gate/verdict, stop-and-fix/enforcement): Would FAIL

**Parity result: FAIL — 1 check (CANON_INVENTORY.json)**

---

## Rejection Reference

```
Rejection reference: IAA-session-009c-wave1-20260406-REJECT
Session: session-009c-20260406
Date: 2026-04-06
Branch: copilot/align-foreman-v2-agent-amc-governance
Commit reviewed: b12c26b
Producing agent: CodexAdvisor-agent (class: Overseer)
Failures: 1 (CORE-006)
```

---

## Next Steps for Invoking Agent (CodexAdvisor)

Per §4.3b: The invoking agent initiates a fresh PREHANDOVER proof (session-009d) in a new
commit after resolving all cited findings.

1. **Obtain CS2 waiver** (Option A) OR **create CANON_INVENTORY.json** (Option B)
2. Create fresh PREHANDOVER proof: `PREHANDOVER-session-009d-20260406.md`
   - Include the CS2 waiver text verbatim (Option A), OR
   - Reference the CANON_INVENTORY.json creation commit (Option B)
3. Commit all new artifacts to the branch
4. Re-invoke IAA: `@independent-assurance-agent [IAA FULL ASSURANCE RE-INVOCATION — SESSION-009d]`

---

**Authority**: CS2 (Johan Ras / @APGI-cmy)
**IAA Adoption Phase**: PHASE_B_BLOCKING — Hard gate ACTIVE
**Self-Modification Lock**: SELF-MOD-IAA-001 — ACTIVE — CONSTITUTIONAL

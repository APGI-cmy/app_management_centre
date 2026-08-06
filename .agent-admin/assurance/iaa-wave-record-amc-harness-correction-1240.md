# Independent Assurance Record — AMC Harness Correction #1240

## Identity

| Field | Value |
|---|---|
| Governing issue | #1240 |
| Pull request | #1241 |
| Branch | `foreman/issue-1240-harness-yaml-marker` |
| Independent assurance role | independent-assurance-agent |
| Reviewed ECAP head | `6be0de9192d750c9299e2b25d658b51f702316d1` |
| Reviewed QP head | `3f01f433e94cfb48923b14dcb41ffad4f0b92161` |
| Reviewed evidence head | `777057e733a6c1148b960b48ec2c8505f78ace2e` |
| Substantive implementation head | `45d7f1ed44fb8a63425ef04de2768f658cb4c7f1` |
| Base | `ff5ec09024210789c2d2941a4aa6fe1ddb166515` |
| Date | 2026-07-29 |
| Merge authority | NOT GRANTED |

## Independent assurance questions

1. Does the PR implement only the authorised PyYAML dependency declaration and `subwave_3_3` marker registration?
2. Is the executable evidence bound to exact heads and complete enough to prove the original harness failures are removed?
3. Does the frozen P1 population collect as exactly 13 nodes with zero collection errors?
4. Is the expected `Optional` failure on PR #1241 alone correctly separated from the harness correction?
5. Does the isolated combined-state proof establish compatibility with PR #1239 and leave only the separately frozen `UTC` A2-R defect?
6. Are skip, xfail, alternate configuration, marker weakening, test editing and scope expansion absent?
7. Were Foreman QP, ECAP and protected-path ceremony completed in the correct order before IAA invocation?
8. Is merge authority still withheld?

## Assurance findings

| ACR | Finding | Result |
|---|---|---|
| ACR-01 Authority binding | Issue #1240 and PR #1241 define the exact two-line harness correction | PASS |
| ACR-02 Diff integrity | `requirements.txt` adds `PyYAML>=6.0`; `pytest.ini` registers `subwave_3_3`; strict markers remain active | PASS |
| ACR-03 Dependency proof | Clean environment installs PyYAML 6.0.3 from requirements; `import yaml` exits 0 | PASS |
| ACR-04 Frozen collection | Exact command exits 0 with 995 collected, 982 deselected and exactly 13 selected; zero collection errors | PASS |
| ACR-05 Exact-head failure separation | PR #1241-only execution errors are exclusively the known unmerged A1 `Optional` defect | PASS |
| ACR-06 Combined-state compatibility | PR #1239 head plus only the two harness deltas collects 13 nodes with zero YAML, marker or `Optional` errors | PASS |
| ACR-07 Remaining RED integrity | All 13 combined-state failures are exclusively `NameError: UTC`, the separately frozen A2-R class | PASS |
| ACR-08 Anti-dodging | No tests, skips, xfails, config overrides, collection narrowing, strict-marker weakening or assertion changes | PASS |
| ACR-09 Isolation | No PR #1239 mutation and no combined branch pushed; disposable worktree removed | PASS |
| ACR-10 Evidence integrity | Raw commands, stdout/stderr, exit codes, versions, timestamps, heads and classifications committed | PASS |
| ACR-11 Foreman QP | QP PASS committed at `3f01f433…` and bound to evidence head | PASS |
| ACR-21 ECAP-before-IAA | ECAP PASS and protected-path ceremony committed at `6be0de91…`; §14.6 checkpoint accepted before IAA | PASS |
| ACR-22 Merge restraint | PR remains open, draft and unmerged; no merge authority granted | PASS |

## Hosted-status finding

The IAA does not treat informational workflow skips as executable test proof. The substantive and evidence package is supported by committed command evidence. Hosted statuses on post-evidence assurance heads must still be re-read during final CS2 proxy review; any genuine failing executable gate would supersede this PASS.

## Independent assurance verdict

**FINAL_ASSURANCE_PASS**

Adoption Phase: `PHASE_B_BLOCKING`

```text
PHASE_B_BLOCKING_TOKEN: IAA-session-1241-HARNESS-20260729-PASS
Reviewed ECAP Head: 6be0de9192d750c9299e2b25d658b51f702316d1
Reviewed QP Head: 3f01f433e94cfb48923b14dcb41ffad4f0b92161
Reviewed Evidence Head: 777057e733a6c1148b960b48ec2c8505f78ace2e
Substantive Head: 45d7f1ed44fb8a63425ef04de2768f658cb4c7f1
Base: ff5ec09024210789c2d2941a4aa6fe1ddb166515
```

## Disposition and limits

The PASS applies only to the quality, evidence integrity, scope compliance and administrative readiness of the Issue #1240 harness correction.

It establishes that:

- the YAML dependency and strict-marker harness blockers are corrected;
- PR #1239 is compatible with those corrections;
- the remaining P1 RED is exclusively the separately frozen `UTC` A2-R defect.

It does not:

- merge PR #1241;
- merge or modify PR #1239;
- repair `UTC`;
- accept Stage 6;
- unblock Stages 7–12;
- appoint any builder;
- grant a waiver, risk acceptance or merge authority.

Final merge disposition remains subject to Johan Ras's CS2 proxy review and explicit instruction.

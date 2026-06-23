# AMC PR1800 Gate Alignment Evidence

| Field | Value |
|---|---|
| Repository | `APGI-cmy/app_management_centre` |
| Branch | `foreman/amc-pr1800-gate-alignment` |
| Alignment target | ISMS PR #1800 governance model |
| Status | IMPLEMENTED_FOR_REVIEW |
| Build ready | false |

## Scope

This wave layers the ISMS PR #1800 gate/admin model into AMC as an initial enforcement stack.

It adds:

- control schemas for delegation order, handover allowance, ECAP admin validation, and IAA preflight brief;
- canonical AMC IAA preflight protocol;
- AMC PR1800 overlay;
- merge-gate required checks manifest;
- delegation-order gate;
- foreman prehandover lane gate;
- ECAP admin-boundary gate;
- merge check alignment gate;
- Wave 7-style policy validation;
- IAA prebrief contract alignment gate;
- advisory/race-tolerant governance watchdog.

## Intended behavior

- Documentation/planning-only changes should pass without builder ceremony.
- Implementation changes require delegation order proof.
- Handover/completion/merge-readiness language requires `handover-allowed.json`.
- ECAP admin artifacts must not claim readiness or assurance.
- Active guidance must not create new standalone `iaa-prebrief-*` artifacts.
- Push-only watchdog findings are advisory and do not create stale red PR blockers.

## Known limitations

This PR does not make AMC build-ready.

Remaining before build:

- update AMC Foreman and ECAP contracts to fully match the new gate stack;
- migrate IAA active practice from legacy standalone prebriefs to wave-record prebriefs;
- resolve CS2 dispositions for Stage 5, Stage 5a, Stage 6, and Stage 7;
- create Stage 8 Implementation Plan;
- create Stage 9 Builder Checklist;
- create canonical IAA prebrief for the build wave;
- create Builder Appointment.

## Disposition

This is a gate/admin alignment PR only. It is not a build PR, handover claim, completion claim, or merge-readiness claim for AMC build execution.

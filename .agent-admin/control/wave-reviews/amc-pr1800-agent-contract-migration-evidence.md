# AMC PR1800 Agent Contract Migration Evidence

| Field | Value |
|---|---|
| Repository | `APGI-cmy/app_management_centre` |
| PR | #1182 |
| Branch | `foreman/amc-pr1800-gate-alignment` |
| Batch | 3 — Foreman / ECAP / IAA agent-contract migration |
| Alignment target | ISMS PR #1800 governance model |
| Status | IMPLEMENTED_FOR_REVIEW |
| Build ready | false |

## Scope

This batch aligns the three core governance agents to the AMC PR #1800 model:

- `.github/agents/foreman-v2-agent.md`
- `.github/agents/execution-ceremony-admin-agent.md`
- `.github/agents/independent-assurance-agent.md`

## Foreman contract changes

The Foreman contract now explicitly states:

- Foreman is a supervisor and does not build.
- Foreman must load `FOREMAN_OPERATING_MODEL.md` and `ISMS_AMC_REPO_ALIGNMENT.md`.
- Foreman must confirm QA-to-red and pre-build readiness before builder delegation.
- Foreman must invoke canonical IAA pre-brief before builder delegation.
- Foreman must appoint builders before implementation.
- Foreman must use ECAP only for administrative validation.
- Foreman must invoke final IAA assurance before handover or merge recommendation.
- AMC remains build-not-ready until Stage 5 / 5a / 6 / 7 dispositions and Stage 8-11 artifacts are complete.

## ECAP contract changes

The ECAP contract now explicitly states:

- ECAP is administrative only.
- ECAP never issues readiness, quality, assurance, build, merge, or acceptance verdicts.
- ECAP never appoints builders.
- ECAP never invokes IAA.
- ECAP never rewrites Foreman QP judgment.
- Preferred ECAP output is `.agent-admin/ecap/ecap-admin-validation.json` and must satisfy `.agent-admin/control/schemas/ecap-admin-validation.schema.json`.

## IAA contract changes

The IAA contract now explicitly states:

- IAA is independent assurance only.
- IAA performs canonical pre-brief before builder delegation.
- IAA performs final assurance before handover, merge-ready recommendation, or build-ready claim.
- New active pre-briefs must use the wave-record protocol with `IAA_PREFLIGHT_BRIEF`.
- Legacy standalone `iaa-prebrief-*` files are historical only.
- IAA cannot build, appoint builders, administer ECAP, grant CS2 waivers, or approve merge.

## Remaining work after this batch

This batch does not complete the whole PR #1800 alignment.

Remaining work:

1. IAA wave-record migration and suppression/marking of legacy standalone prebrief practice.
2. Critical gate validation after workflows run on PR #1182.
3. Noisy/admin-loop gate fixes if any appear.
4. Stage 5 / Stage 5a / Stage 6 / Stage 7 CS2 dispositions.
5. Stage 8 Implementation Plan.
6. Stage 9 Builder Checklist.
7. Build-wave canonical IAA prebrief.
8. Builder Appointment.

## Disposition

Implemented for review only. This is not a completion, handover, build-readiness, or merge-readiness claim.

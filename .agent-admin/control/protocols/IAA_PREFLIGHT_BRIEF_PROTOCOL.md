# AMC IAA Preflight Brief Protocol

## Status

| Field | Value |
|---|---|
| Repository | `APGI-cmy/app_management_centre` |
| Protocol | `IAA_PREFLIGHT_BRIEF` |
| Alignment target | ISMS PR #1800 |
| Status | Active for new AMC governed work |

## Canonical artifact location

New AMC IAA pre-brief evidence must be recorded inside a wave record, not as a standalone `iaa-prebrief-*.md` file.

Canonical location:

```text
.agent-admin/assurance/iaa-wave-record-<wave-id>.md
```

Canonical section:

```text
## PRE-BRIEF
IAA_PREFLIGHT_BRIEF
```

Legacy standalone `.agent-admin/assurance/iaa-prebrief-*.md` artifacts remain historical only. If older guidance tells an agent to create a standalone `iaa-prebrief-*.md`, this protocol supersedes that instruction.

## Required timing

IAA pre-brief must be recorded before builder appointment and before the first implementation commit for qualifying build work.

## Minimum content

The pre-brief must identify:

- wave/job id;
- issue or PR reference;
- qualifying tasks;
- expected QA scope;
- high-risk failure modes;
- required builder evidence;
- required Foreman QP checks;
- whether ECAP is required;
- final IAA focus.

## Non-qualifying work

If no qualifying assurance task exists, the wave record may state `PHASE_A_ADVISORY`, but it must still explain why no IAA pre-brief is required.

## Enforcement

The AMC `iaa-prebrief-contract-alignment` workflow checks active guidance and blocks new active instructions that tell agents to create standalone `iaa-prebrief-*` artifacts.

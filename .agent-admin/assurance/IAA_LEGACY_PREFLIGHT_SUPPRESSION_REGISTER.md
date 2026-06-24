# IAA Legacy Prebrief Suppression Register

| Field | Value |
|---|---|
| Repository | `APGI-cmy/app_management_centre` |
| Alignment target | ISMS PR #1800 governance model |
| Status | ACTIVE TRANSITION REGISTER |
| Authority | `governance/canon/IAA_PRE_BRIEF_PROTOCOL.md` v2.0.0-amc-pr1800 |

---

## Purpose

This register prevents legacy IAA prebrief artifacts from being mistaken for active guidance during the AMC PR #1800 alignment.

Existing files matching:

```text
.agent-admin/assurance/iaa-prebrief-*.md
```

are retained as historical/provenance evidence only. They must not be used as the required location for new active IAA prebriefs.

New active prebriefs must be recorded in:

```text
.agent-admin/assurance/iaa-wave-record-<wave-id>.md
```

with the section marker:

```text
## PRE-BRIEF
IAA_PREFLIGHT_BRIEF
```

---

## Known legacy standalone prebrief artifacts

The repository contains historical standalone prebrief artifacts, including but not limited to:

```text
.agent-admin/assurance/iaa-prebrief-wave-layer-down-iaa-workflows.md
.agent-admin/assurance/iaa-prebrief-wave1.md
.agent-admin/assurance/iaa-prebrief-wave-amc-stage1-consolidation.md
.agent-admin/assurance/iaa-prebrief-wave-opojd-delivery.md
.agent-admin/assurance/iaa-prebrief-wave-12stage-amc-alignment.md
.agent-admin/assurance/iaa-prebrief-layer-down-404c78fa.md
.agent-admin/assurance/iaa-prebrief-ecap-001-amc-downstream.md
```

This list is not exhaustive. The rule applies to every historical standalone `iaa-prebrief-*` artifact.

---

## Suppression rule

Legacy standalone prebrief artifacts may be cited only as:

- historical provenance;
- migration evidence;
- superseded practice;
- audit trail.

They may not be cited as:

- the active prebrief location for new work;
- sufficient evidence for builder delegation;
- final assurance evidence;
- a substitute for `IAA_PREFLIGHT_BRIEF` in a canonical wave record.

---

## Active guidance override

If any older document tells an agent to create a standalone `iaa-prebrief-*` file, the active instruction is superseded by:

```text
governance/canon/IAA_PRE_BRIEF_PROTOCOL.md
.agent-admin/control/protocols/IAA_PREFLIGHT_BRIEF_PROTOCOL.md
.github/agents/independent-assurance-agent.md
FOREMAN_OPERATING_MODEL.md
```

---

## AMC build posture

This register does not make AMC build-ready. AMC remains build-blocked until Stage 5 / 5a / 6 / 7 CS2 dispositions and Stage 8-11 artifacts are complete.

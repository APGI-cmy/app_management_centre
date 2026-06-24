# IAA PRE-BRIEF PROTOCOL

**Status**: CANONICAL — AMC PR #1800 TRANSITION | **Version**: 2.0.0-amc-pr1800 | **Authority**: CS2  
**Updated**: 2026-06-24  
**Alignment Target**: ISMS PR #1800 Foreman / Builder / ECAP / IAA gate model

---

## 1. Purpose

This protocol defines the active AMC IAA pre-brief model.

For new governed AMC work, the IAA pre-brief is no longer a standalone `iaa-prebrief-*` artifact. The active pre-brief must be recorded in the canonical wave-record carrier using the `IAA_PREFLIGHT_BRIEF` marker.

This change prevents drift between old standalone pre-brief artifacts, wave records, builder appointments, ECAP admin bundles, and final IAA assurance.

---

## 2. Supersession of legacy standalone pre-brief artifacts

Legacy standalone artifacts matching:

```text
.agent-admin/assurance/iaa-prebrief-*.md
```

are historical/provenance records only.

They may be retained for audit history, but they must not be used as the active required location for new AMC pre-briefs.

Active guidance must not instruct agents to create new standalone `iaa-prebrief-*` files. If older guidance conflicts with this protocol, this protocol and `.agent-admin/control/protocols/IAA_PREFLIGHT_BRIEF_PROTOCOL.md` control.

---

## 3. Canonical active carrier

New AMC IAA pre-briefs must be stored in a wave record:

```text
.agent-admin/assurance/iaa-wave-record-<wave-id>.md
```

The canonical pre-brief section is:

```text
## PRE-BRIEF
IAA_PREFLIGHT_BRIEF
```

A wave record may also contain final assurance later in the same file, but pre-brief and final assurance must remain separately labeled.

---

## 4. Required timing

IAA pre-brief must occur before:

1. builder appointment;
2. first implementation commit;
3. handover readiness language;
4. build-ready or merge-ready recommendation.

If there are no qualifying tasks, the wave record may record `PHASE_A_ADVISORY`, but it must explain why no full pre-brief is required.

---

## 5. Required content

The `IAA_PREFLIGHT_BRIEF` section must identify:

- wave/job identifier;
- issue or PR reference;
- branch and current head SHA when available;
- qualifying tasks;
- expected QA scope;
- high-risk failure modes;
- required builder evidence;
- required Foreman QP checks;
- whether ECAP is required;
- final IAA focus;
- disposition: `PREFLIGHT_BRIEF_COMPLETE` or `PHASE_A_ADVISORY`.

---

## 6. Relationship to final assurance

Pre-brief does not equal final assurance.

Final IAA assurance remains required before handover, build-ready, merge-ready, or completion claims for qualifying work. The final assurance section must independently evaluate builder output, QA-to-green evidence, Foreman QP, ECAP admin evidence, gate status, and CS2 dispositions.

---

## 7. Enforcement

The AMC IAA pre-brief contract alignment workflow enforces this transition by checking active guidance for new instructions to create standalone `iaa-prebrief-*` artifacts.

The active guidance paths are:

```text
.agent-admin/control/protocols/**
.agent-admin/control/overlays/**
.agent-admin/control/templates/**
.agent-admin/control/checklists/**
governance/canon/IAA_PRE_BRIEF_PROTOCOL.md
.github/agents/independent-assurance-agent.md
.github/agents/foreman-v2-agent.md
```

Legacy artifacts and memory records may mention `iaa-prebrief-*` for history, migration, or supersession, provided they do not instruct new active creation.

---

## 8. Current AMC build posture

AMC remains not build-ready. This protocol migration only aligns assurance practice. Build remains blocked until the conditions in `FOREMAN_OPERATING_MODEL.md` and `ISMS_AMC_REPO_ALIGNMENT.md` are satisfied.

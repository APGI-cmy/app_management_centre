# AMC Foreman Operating Model

## Status

| Field | Value |
|---|---|
| Repository | `APGI-cmy/app_management_centre` |
| Product/module | App Management Centre (AMC) |
| Owner / CS2 authority | Johan Ras |
| Operating role | Foreman-led governed delivery |
| Alignment target | ISMS PR #1800 Foreman / Builder / ECAP / IAA gate model |
| Status | Active operating reference |

---

## 1. Why this file exists

This file records how governed AMC work must run before the AMC app build starts.

AMC is being aligned to the current ISMS governance model. The immediate goal is not implementation. The immediate goal is to make the repo's governance and admin setup match the working ISMS model so that later build work can proceed without stale admin loops, role collapse, or hidden test debt.

Most governed AMC work starts in Foreman mode unless Johan explicitly asks for direct drafting, analysis, review, or a non-governed response.

---

## 2. Core operating doctrine

The AMC operating doctrine is:

1. Johan Ras remains CS2 authority.
2. ChatGPT usually acts as Foreman: plan, organize, lead, control, delegate, and verify.
3. Foreman does not build.
4. Builders build only after appointment and only within assigned scope.
5. No QA-to-red means no build.
6. Existing QA-to-red must be current, approved, and traceable before build begins.
7. Each correction updates the affected pre-build artifact range before implementation.
8. ECAP is administrative only: compile and validate admin evidence, never decide readiness.
9. IAA is independent assurance: pre-brief before builder delegation and final assurance before CS2 review.
10. Handover, completion, ready-for-review, merge-ready, and equivalent language is gated.
11. Implementation-only work is not handover and must not be trapped in an admin loop.
12. CS2 remains final waiver, acceptance, and merge authority.

---

## 3. Standard governed sequence

The default AMC governed-work sequence is:

```text
CS2 request
  -> Foreman bootstrap
  -> load this operating model
  -> load Foreman agent contract and Tier 2 controls
  -> classify task type and affected AMC stage
  -> load AMC authority stack and current trackers
  -> update or create affected pre-build artifacts first
  -> confirm QA-to-red exists and is current
  -> invoke IAA pre-brief
  -> appoint builder if implementation is required
  -> builder builds to green
  -> Foreman performs QP review
  -> ECAP compiles/validates admin evidence
  -> pre-handover lane gate when handover language is used
  -> IAA final assurance
  -> CS2 review / merge decision
```

Foreman must not collapse these roles.

---

## 4. Role boundaries

### CS2

CS2 authority belongs to Johan Ras.

CS2 decisions include:

- stage approval;
- progression approval;
- acceptance of conditions;
- acceptance of risk;
- approval of any gate waiver;
- approval of material product-boundary changes;
- approval of AI-assisted CS2 proxy use;
- final merge or build acceptance.

### Foreman

Foreman orchestrates governed AMC work.

Foreman must:

- load this file;
- load `.github/agents/foreman-v2-agent.md`;
- load AMC pre-build trackers and authority artifacts;
- declare or confirm scope;
- update pre-build artifacts before implementation;
- invoke IAA pre-brief before builder delegation;
- appoint builders for implementation;
- perform QP review after builder output;
- invoke ECAP for admin evidence;
- invoke IAA final assurance before CS2 handover;
- verify gates before handover or merge recommendation.

Foreman must not:

- write implementation code, migrations, schemas, tests, workflows, or product artifacts as the builder;
- self-certify IAA;
- use ECAP as readiness authority;
- use handover/completion language before the pre-handover lane is satisfied;
- merge or approve its own governance waiver.

### Builder

Builder performs appointed implementation work only within the scope given by Foreman.

Builder appointment artifacts should be filed under the AMC-approved builder appointment path once Stage 11 is unblocked.

Builders only build to green. If QA-to-red is missing, stale, unapproved, or not traceable, the job returns to Foreman for pre-build correction first.

### ECAP

ECAP is the execution ceremony admin role.

ECAP may:

- compile admin bundles;
- validate admin fields;
- check evidence paths;
- check scope/admin freshness;
- record PR and CI status;
- surface missing administrative evidence.

ECAP may not:

- decide build readiness;
- decide merge readiness;
- invoke IAA;
- rewrite Foreman QP judgment;
- convert failed substantive work into admin-complete work.

### IAA

IAA is independent assurance.

IAA reviews governance, traceability, completeness, fully functional delivery readiness, no hidden test debt, no test dodging, public trust, scope discipline, and readiness for the next stage.

AMC must migrate active IAA pre-brief practice to canonical wave-record evidence using:

```text
## PRE-BRIEF
IAA_PREFLIGHT_BRIEF
```

Standalone `iaa-prebrief-*` artifacts are legacy and must not be used as active new guidance once the IAA contract migration is complete.

---

## 5. AMC current build posture

AMC has completed Stages 1–5. The B1 executable-QA defect triggered canonical Stage 6 re-entry; Stages 7–10 now await dependent reverification after the executable intended-RED suite exists.

```text
Stages 1–5: complete / accepted as recorded in modules/amc/BUILD_PROGRESS_TRACKER.md
Stage 6 QA-to-Red: re-entry authorized / remediation pending under Issue #1226
Stages 7–10: dependent reverification pending after Stage 6 correction
Stage 11 Builder Appointment: NO-GO while B1, B4, B5 and B8 remain open
Stage 12 Build: not started / blocked
integration-builder: nominated/readiness-approved but not appointed
```

The primary live lifecycle authority is `modules/amc/BUILD_PROGRESS_TRACKER.md`. Earlier posture statements retained in historical records do not override that tracker.

---

## 6. AMC authority stack

Foreman must load the current AMC authority stack before making material changes.

Minimum authority stack:

```text
ISMS_AMC_REPO_ALIGNMENT.md
FOREMAN_OPERATING_MODEL.md
modules/amc/AMC_PRE_BUILD_ARTIFACT_INDEX.md
modules/amc/BUILD_PROGRESS_TRACKER.md
modules/amc/00-app-description/app-description.md
modules/amc/01-ux-workflow-wiring-spec/ux-workflow-wiring-spec.md
modules/amc/02-frs/functional-requirements-specification.md
modules/amc/03-trs/technical-requirements-specification.md
modules/amc/04-architecture/architecture-specification.md
modules/amc/05a-deployment-execution-strategy/deployment-execution-strategy.md
modules/amc/05-qa-to-red/qa-to-red-specification.md
modules/amc/05-qa-to-red/red-test-catalog.md
modules/amc/06-pbfag/pre-build-final-assurance-gate.md
```

If any of these files are missing, stale, superseded, contradicted, or approval-pending, Foreman must record the condition and not silently proceed to build.

---

## 7. Build start rule

AMC build may start only when all of the following are true:

```text
FOREMAN_OPERATING_MODEL.md exists
AND ISMS_AMC_REPO_ALIGNMENT.md exists
AND the ISMS PR #1800 gate stack is aligned or explicitly dispositioned for AMC
AND the IAA wave-record contract is canonical
AND Stage 5 / Stage 5a / Stage 6 / Stage 7 blockers are resolved or explicitly dispositioned by CS2
AND Stage 8 Implementation Plan exists
AND Stage 9 Builder Checklist exists
AND canonical IAA pre-brief exists
AND Builder Appointment exists
```

Until then, any implementation work is premature unless CS2 explicitly grants an emergency waiver.

---

## 8. Anti-admin-loop rule

Implementation-only work is not handover.

The pre-handover lane becomes applicable only when there is handover, completion, readiness, merge-ready, or equivalent language, or when Foreman/ECAP handover artifacts are active.

If an old AMC gate demands handover/admin evidence before implementation-only work reaches handover, treat it as a transition conflict and escalate to CS2 rather than looping.

---

## 9. Immediate next steps

The recommended next steps are:

1. Align AMC gate/admin controls to ISMS PR #1800.
2. Migrate IAA pre-brief handling to canonical wave records.
3. Resolve Stage 5 / 5a / 6 / 7 CS2 approval/disposition blockers.
4. Create Stage 8 Implementation Plan.
5. Create Stage 9 Builder Checklist.
6. Create canonical IAA pre-brief for the build wave.
7. Issue Builder Appointment.
8. Then start builder-led build-to-green work.

---

## 10. Startup instruction for future AMC chats

Use this at the start of a governed AMC chat:

```text
Please note we work according to `FOREMAN_OPERATING_MODEL.md` and `ISMS_AMC_REPO_ALIGNMENT.md`.

Assume Foreman unless I explicitly ask otherwise. Load the AMC authority stack, update or confirm pre-build artifacts first, confirm QA-to-red, invoke IAA pre-brief before builder delegation, appoint builders to build to green, perform Foreman QP, invoke ECAP for administrative evidence, invoke IAA final assurance, and verify gates before handover or merge recommendation.
```

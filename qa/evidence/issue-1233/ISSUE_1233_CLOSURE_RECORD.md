# Issue #1233 — Parent Blocker Closure Record

## Authority

- Governing issue: #1233
- Parent QA issue: #1226
- Closure authorisation: Foreman governance disposition
- Closure date: 2026-08-07

---

## Blocker decomposition recap

Issue #1233 ("AMC baseline regression debt recovery blocking Issue #1226 acceptance") was
decomposed into the following bounded repair lanes:

| Lane | Type | Governing PR | Status |
|---|---|---|---|
| B0 — Regression freeze | Pre-implementation evidence | PR #1236 | MERGED |
| A1 — `Optional` import repair | Runtime import defect | PR #1239 | MERGED |
| A2-R — `UTC` import repair (runtime) | Runtime import defect | PR #1242 | MERGED |
| A2-T — Intentional-RED lifecycle classification | Governance classification | This PR | COMPLETE |
| B1 — Execution evidence on merged baseline | Evidence run | PENDING (next step) | NOT YET EXECUTED |

---

## Lane completion status

### B0 — Regression population freeze
- PR #1236 merged to `main` at `34b1af8feef4a7f8d0a93859c45f797e21507c84` (prior to #1241 base).
- Frozen populations P1 (13 nodes), P2 (957 derived), P3 (25 nodes), P4 (Stage 6 / 19 nodes) recorded.
- **Status: COMPLETE**

### A1 — Optional import repair
- PR #1239 merged to `main` at commit `12c46c4...`
- Four Foreman domain modules (`task.py`, `program.py`, `wave.py`, `blocker.py`) repaired.
- All four direct imports GREEN.
- **Status: COMPLETE**

### A2-R — UTC import repair (runtime)
- PR #1242 merged to `main` at `73a86f65e3f34f6c755898209de94647d6274aa4`
- 15 runtime files patched with bounded `UTC` import addition.
- **Status: COMPLETE**

### A2-T — Intentional-RED lifecycle classification
- Classification record: `qa/evidence/issue-1233/a2t/A2T_LIFECYCLE_CLASSIFICATION.md`
- All 25 P3 nodes classified: RETAIN as canonical QA-to-Red.
- No code change required or authorised.
- **Status: COMPLETE**

### B1 — Execution evidence on merged baseline
- B1 requires execution on accepted `main` HEAD (`781e728edc7be20b5532091044d8ea34653f6e57`)
  with all A1 + A2-R + harness fixes in place.
- B1 must confirm: P1 13 passed, P2 all passed, P3 25 failed (expected-RED), P4 19 failed (Stage 6 expected-RED).
- **Status: PENDING — next required Foreman action**

---

## Issue #1233 disposition

With A2-T classification now complete:

- All **original defect classes identified in #1233 have been addressed** in their bounded lanes.
- The only remaining work before full parent-blocker closure is **B1 execution evidence** on the
  merged main baseline.
- Issue #1233 may be **closed after B1 evidence is produced, reviewed, and accepted**.

---

## Lifecycle update

```text
Issue #1233 parent blocker: A2-T CLASSIFICATION COMPLETE
Remaining condition for #1233 closure: B1 execution evidence on merged HEAD
B1 unblocking conditions satisfied: A1 merged, A2-R merged, A2-T classified, harness fixed
B1 next action: Foreman to run B1 evidence commands on origin/main HEAD 781e728
Stage 6 acceptance: still conditional on B1 outcomes — P2 GREEN required
Stages 7–10: still conditional on B1 outcomes
Stage 11: NO-GO until B1 accepted
Stage 12: NO-GO until B1 accepted
integration-builder: NOT APPOINTED
```

# Wave Task List — wave-simple-pr-admin-20260505

> **Authority**: CS2 (@APGI-cmy) — Issue #1163
> **Wave**: wave-simple-pr-admin-20260505
> **Session**: session-037
> **Date**: 2026-05-05
> **Agent**: foreman-v2-agent
> **Branch**: copilot/align-tier-1-tier-2-agent-artifacts

governance_evidence_path: .agent-admin/waves/wave-simple-pr-admin-20260505-current-tasks.md
iaa_prebrief_path: .agent-admin/wave-records/amc-wave-record-wave-simple-pr-admin-20260505-20260505.md

---

## Purpose

Align Tier 1 canon references, Tier 2 knowledge/artifacts, agent instructions/contracts, and
CI gates with the AMC Simple PR Admin Model (issue #1163 — AMC equivalent of maturion-isms#1530).

The AMC Simple PR Admin Model introduces `.admin/pr.json` as the single source of truth for
AMC/MMM product-fix PRs, enabling reduced ceremony for product-fix and docs-only PRs while
preserving full controls for governance-control, agent-contract, migration, database, deployment,
and high-risk PRs.

---

## Task List

- [ ] TASK-037-01 — Create `governance/canon/MMM_SIMPLE_PR_ADMIN_MODEL.md` (new Tier 1 canon v1.0.0)
      builder: governance-liaison-amc-agent
      qp_verdict: PENDING
      notes: New governance canon defining the Simple PR Admin Model. Must define PR types, .admin/pr.json schema, forced-ceremony override rules, and preservation requirements.

- [ ] TASK-037-02 — Update `governance/canon/AGENT_HANDOVER_AUTOMATION.md` (add Simple Admin Model exception)
      builder: governance-liaison-amc-agent
      qp_verdict: PENDING
      notes: Amend v1.7.3 → v1.7.4. Add new section: "Simple Admin Model — product-fix PRs". Clarify that Phase 4 ceremony is reduced for product-fix PRs with .admin/pr.json declaring requires_iaa=false, requires_ecap=false. Forced-ceremony paths must still be listed.

- [ ] TASK-037-03 — Update `governance/canon/EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md` (product-fix exception)
      builder: governance-liaison-amc-agent
      qp_verdict: PENDING
      notes: Amend v1.3.0 → v1.3.1. Add exception clause: ECAP appointment is not required for product-fix PRs where .admin/pr.json declares requires_ecap=false AND no forced-ceremony paths are touched.

- [ ] TASK-037-04 — Update `.github/workflows/iaa-ecap-hard-gate.yml` (add .admin/pr.json bypass)
      builder: integration-builder
      qp_verdict: PENDING
      notes: Add .admin/pr.json classification to the classify-protected-paths job. If file exists and declares type=product-fix, requires_iaa=false, requires_ecap=false, AND no forced-ceremony paths are in the diff → SIMPLE_ADMIN bypass. Forced-ceremony paths: .github/agents/**, governance/**, .governance-pack/**, .agent-workspace/**/knowledge/**, supabase/migrations/**, schema/, migrations/. Preserve full ceremony for all other cases.

- [ ] TASK-037-05 — Update `.github/workflows/preflight-evidence-gate.yml` (add .admin/pr.json bypass)
      builder: integration-builder
      qp_verdict: PENDING
      notes: After the layer-down/governance bypass check, add a check for .admin/pr.json with type=product-fix. For product-fix PRs, downgrade the session memory and wave plan requirements to informational (not blocking). POLC boundary check still applies.

- [ ] TASK-037-06 — Update `.github/workflows/polc-boundary-gate.yml` (add .admin/pr.json bypass)
      builder: integration-builder
      qp_verdict: PENDING
      notes: Add .admin/pr.json check. For product-fix PRs, foreman-implementation-check and builder-involvement-check continue to run. session-memory-check is downgraded to informational (not blocking). This preserves POLC enforcement while reducing ceremony overhead.

- [ ] TASK-037-07 — Update `.github/workflows/merge-gate-interface.yml` (add product-fix classification)
      builder: integration-builder
      qp_verdict: PENDING
      notes: Add "product-fix" as a recognized PR type in the classify-pr job. Product-fix PRs with valid .admin/pr.json are classified as pr_type=product-fix with appropriate gate requirements.

- [ ] TASK-037-08 — Create `.admin/README.md` and `.admin/pr.json.schema.json`
      builder: integration-builder
      qp_verdict: PENDING
      notes: Create .admin/ directory with README explaining the purpose and .admin/pr.json file format. Create JSON Schema for pr.json validation. Schema fields: type (enum: product-fix, docs-only, governance-control, migration, deployment, high-risk), requires_iaa (boolean), requires_ecap (boolean), governing_issue (string), scope_summary (string), created_by (string), created_at (ISO-8601 string). Add validation logic to CI gates.

- [ ] TASK-037-09 — Update Tier 2 knowledge index
      builder: foreman-v2-agent (within .agent-workspace/** write access)
      qp_verdict: PENDING
      notes: Update .agent-workspace/foreman-v2/knowledge/index.md to reference MMM_SIMPLE_PR_ADMIN_MODEL.md as a new Tier 1 canon affecting foreman behavior.

---

## Forced-Ceremony Paths (must never be bypassed by .admin/pr.json)

The following paths trigger FULL ceremony regardless of .admin/pr.json declarations:
- `.github/agents/**`
- `governance/**`
- `.governance-pack/**`
- `.agent-workspace/**/knowledge/**`
- `.agent-admin/**` (except for .admin/ itself which is the manifest dir)
- `supabase/migrations/**`
- `schema/` and `migrations/` paths
- `BUILD_PROGRESS_TRACKER*`

---

## Architecture Reference

`.agent-admin/build-evidence/session-037-20260505/architecture-simple-pr-admin-20260505.md`

---

## Pre-Brief

IAA Pre-Brief to be embedded in wave record section 2 after invocation.

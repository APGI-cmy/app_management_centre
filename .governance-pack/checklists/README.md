# Governance Pack — Checklists

This directory contains governance checklist artifacts layered down from the canonical source (`APGI-cmy/maturion-foreman-governance`).

Checklists are consumed by agent contracts, merge-gate workflows, and the preflight-evidence-gate to enforce governance compliance.

## Source

All files in this directory originate from `governance/checklists/` in the canonical source repository. They are layered down via the governance ripple protocol and must not be edited locally.

## Usage

- Referenced by `.github/agents/*.md` contract files via the `governance.bindings` section
- Consumed by `merge-gate-interface.yml` and `preflight-evidence-gate.yml` workflows
- Validated by `validate-yaml-frontmatter.sh`

## Maintenance

Run a layer-down event from `maturion-foreman-governance` when checklists are updated upstream, or create a layer-down issue in this repo following the protocol in `governance/canon/CROSS_REPOSITORY_LAYER_DOWN_PROTOCOL.md`.

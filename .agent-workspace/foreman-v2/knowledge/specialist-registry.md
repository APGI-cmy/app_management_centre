# Foreman-v2 Specialist Registry — AMC Consumer Copy

## Registry Metadata
- Version: 1.0.0
- Authority: CS2 (@APGI-cmy)
- Canon Home: APGI-cmy/maturion-foreman-governance
- Last Updated: 2026-04-10
- Status: ACTIVE

---

## Agent Roster

| Agent ID | Agent Class | Capabilities | Invocation Method | Status |
|----------|-------------|-------------|------------------|--------|
| `CodexAdvisor-agent` | overseer | Create/update agent contracts; audit agent files; Tier 2 layer-down | `task(agent_type: "CodexAdvisor-agent")` | ACTIVE |
| `independent-assurance-agent` | assurance | IAA Pre-Brief, handover audits, ASSURANCE-TOKEN issuance | `task(agent_type: "independent-assurance-agent")` | ACTIVE |
| `governance-liaison-amc-agent` | liaison | Governance layer-down, canon sync, ripple inbox processing | `task(agent_type: "governance-liaison-amc-agent")` | ACTIVE |
| `api-builder` | builder | API routes, handlers, business logic, backend services | `task(agent_type: "api-builder")` | ACTIVE |
| `qa-builder` | builder | Tests, QA suites, coverage verification, red-suite creation | `task(agent_type: "qa-builder")` | ACTIVE |
| `schema-builder` | builder | Database schemas, models, migrations, RLS policies | `task(agent_type: "schema-builder")` | ACTIVE |
| `ui-builder` | builder | React UI components, layouts, wizards, frontend code | `task(agent_type: "ui-builder")` | ACTIVE |
| `integration-builder` | builder | Inter-module integrations, external connections, CI infrastructure | `task(agent_type: "integration-builder")` | ACTIVE |

---

## Usage Rules (A-017 — MANDATORY)

- Foreman MUST verify `agent_type` is in this roster before every `task()` call.
- `general-purpose` agent is **NOT** an inducted ISMS agent and MUST NEVER be used for committed-artifact implementation work.
- If no roster agent can satisfy a wave task → HALT-006. Escalate to CS2. Self-implementation is not a fallback.

## Note on Governance-Class Agents

`CodexAdvisor-agent`, `independent-assurance-agent`, and `governance-liaison-amc-agent` are NOT builders.
- **CodexAdvisor-agent**: Agent contract file changes ONLY — CS2-gated, AGCFPP-001 §3–§4
- **independent-assurance-agent**: IAA Pre-Brief (Phase 1 Step 1.8) and handover audit (Phase 4 Step 4.3a) ONLY
- **governance-liaison-amc-agent**: Canon layer-down and ripple processing ONLY

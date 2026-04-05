"use strict";

/**
 * Required governed agent IDs — AMC consumer repo.
 *
 * These are the agent contracts that MUST exist in .github/agents/
 * for the agent-bootstrap server to start without warnings.
 * The npm test suite (test-bootstrap.js) asserts all of these are present.
 *
 * Update this list when a new mandatory agent contract is added to AMC.
 */
const REQUIRED_AGENT_IDS = [
  "CodexAdvisor-agent",
  "foreman-v2-agent",
  "governance-liaison-amc-agent",
  "independent-assurance-agent",
  "api-builder",
  "qa-builder",
  "schema-builder",
  "ui-builder",
  "integration-builder",
];

module.exports = { REQUIRED_AGENT_IDS };
#!/usr/bin/env node
/**
 * MCP Bootstrap Availability Detection Module
 * 
 * Probes the agent-bootstrap MCP server to determine if it is available in the
 * current runtime (e.g., ChatGPT Work Mode). Returns structured availability info.
 * 
 * Usage:
 *   node .github/scripts/detect-mcp-bootstrap-availability.js
 *   
 * Output (JSON):
 *   {
 *     "available": boolean,
 *     "reason": string,
 *     "fallback_instructions": string | null,
 *     "timestamp": ISO8601,
 *     "diagnostic": { ... }
 *   }
 * 
 * Authority: Issue #1228 Phase 1 (agent-bootstrap operationalisation)
 */

"use strict";

const fs = require("fs");
const path = require("path");

const REPO_ROOT = process.cwd();

/**
 * Probe MCP server availability by attempting to read the MCP config
 * and verify that the agent-bootstrap server is registered.
 * 
 * @returns {Object} Detection result with availability status
 */
async function detectMCPBootstrapAvailability() {
  const startTime = Date.now();
  const result = {
    available: false,
    reason: "Not yet determined",
    fallback_instructions: null,
    timestamp: new Date().toISOString(),
    diagnostic: {
      mcp_config_found: false,
      agent_bootstrap_registered: false,
      agent_contracts_found: 0,
      probe_duration_ms: 0,
      error: null,
    },
  };

  try {
    // Step 1: Verify .mcp.json exists and is valid
    const mcpConfigPath = path.join(REPO_ROOT, ".mcp.json");
    if (!fs.existsSync(mcpConfigPath)) {
      result.reason = "MCP config (.mcp.json) not found at repo root";
      result.fallback_instructions = generateFallbackPath();
      result.diagnostic.error = result.reason;
      return finalize(result, startTime);
    }
    result.diagnostic.mcp_config_found = true;

    let mcpConfig;
    try {
      mcpConfig = JSON.parse(fs.readFileSync(mcpConfigPath, "utf8"));
    } catch (err) {
      result.reason = `MCP config is invalid JSON: ${err.message}`;
      result.fallback_instructions = generateFallbackPath();
      result.diagnostic.error = result.reason;
      return finalize(result, startTime);
    }

    // Step 2: Verify agent-bootstrap server is registered
    if (!mcpConfig.mcpServers || !mcpConfig.mcpServers["agent-bootstrap"]) {
      result.reason =
        "agent-bootstrap MCP server not registered in .mcp.json";
      result.fallback_instructions = generateFallbackPath();
      result.diagnostic.error = result.reason;
      return finalize(result, startTime);
    }
    result.diagnostic.agent_bootstrap_registered = true;

    // Step 3: Verify agent contracts exist
    const agentsDir = path.join(REPO_ROOT, ".github", "agents");
    if (!fs.existsSync(agentsDir)) {
      result.reason = ".github/agents directory not found";
      result.fallback_instructions = generateFallbackPath();
      result.diagnostic.error = result.reason;
      return finalize(result, startTime);
    }

    try {
      const contractFiles = fs
        .readdirSync(agentsDir)
        .filter((f) => f.endsWith(".md") && !f.startsWith("_"));
      result.diagnostic.agent_contracts_found = contractFiles.length;

      if (contractFiles.length === 0) {
        result.reason = "No agent contracts found in .github/agents";
        result.fallback_instructions = generateFallbackPath();
        result.diagnostic.error = result.reason;
        return finalize(result, startTime);
      }
    } catch (err) {
      result.reason = `Could not scan .github/agents: ${err.message}`;
      result.fallback_instructions = generateFallbackPath();
      result.diagnostic.error = result.reason;
      return finalize(result, startTime);
    }

    // Step 4: All checks passed — assume MCP server is available
    // Note: We cannot fully test the MCP server without a running MCP client context.
    // In a Work Mode environment, the agent runtime will handle MCP server invocation.
    result.available = true;
    result.reason = "MCP server is registered and agent contracts are present";
    result.diagnostic.error = null;

    return finalize(result, startTime);
  } catch (err) {
    result.reason = `Unexpected error during detection: ${err.message}`;
    result.fallback_instructions = generateFallbackPath();
    result.diagnostic.error = result.reason;
    return finalize(result, startTime);
  }
}

/**
 * Generate fallback instructions (returned when MCP unavailable)
 * @returns {string} Markdown instructions for fallback workflow
 */
function generateFallbackPath() {
  return `## ⚠️ MCP SERVER UNAVAILABLE — USE FALLBACK PATH

The \`agent-bootstrap\` MCP server is not available in this runtime.

**Approved fallback (Issue #1226 precedent):**
1. Fetch your agent contract directly from \`.github/agents/<agent-id>.md\`
2. Complete Phase 1 (Identity & Preflight) by reading the entire contract
3. Submit Phase 1 attestation (template in fallback instructions file)
4. Proceed with work after attestation is filed

**Location of fallback template:**
\`.github/scripts/agent-bootstrap-fallback-instructions.md\`

This is an approved alternative to the direct MCP call. CS2 enforces this via merge gate.`;
}

/**
 * Finalize result and calculate duration
 */
function finalize(result, startTime) {
  result.diagnostic.probe_duration_ms = Date.now() - startTime;
  return result;
}

// Main execution
(async () => {
  const result = await detectMCPBootstrapAvailability();
  console.log(JSON.stringify(result, null, 2));
  process.exit(result.available ? 0 : 1);
})();

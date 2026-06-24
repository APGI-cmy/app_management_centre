#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const repoRoot = process.cwd();
const manifestPath = path.join(repoRoot, '.agent-admin/control/merge-gate-required-checks.json');
function fail(message) {
  console.error(`::error::${message}`);
  process.exitCode = 1;
}
function listFiles(dir, results = []) {
  if (!fs.existsSync(dir)) return results;
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, item.name);
    if (item.isDirectory()) listFiles(full, results);
    else results.push(full);
  }
  return results;
}
function workflowJobNames() {
  const workflowDir = path.join(repoRoot, '.github/workflows');
  const files = listFiles(workflowDir).filter((file) => file.endsWith('.yml') || file.endsWith('.yaml'));
  const names = new Set();
  for (const file of files) {
    const lines = fs.readFileSync(file, 'utf8').split(/\r?\n/);
    for (const line of lines) {
      const match = line.match(/^\s{4,}name:\s*["']?([^"'#]+)["']?/);
      if (match && match[1]) names.add(match[1].trim());
    }
  }
  return names;
}
console.log('=== AMC Merge Gate Required Checks Alignment ===');
if (!fs.existsSync(manifestPath)) {
  fail('Missing .agent-admin/control/merge-gate-required-checks.json');
  process.exit(1);
}
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
const required = manifest.required_checks || [];
const workflowBacked = manifest.workflow_backed_required_checks || [];
if (required.length === 0) fail('required_checks must not be empty');
for (const check of new Set(required)) {
  if (required.filter((candidate) => candidate === check).length > 1) fail(`Duplicate required check: ${check}`);
}
for (const check of workflowBacked) {
  if (!required.includes(check)) fail(`workflow-backed check is not listed in required_checks: ${check}`);
}
const liveJobs = workflowJobNames();
for (const check of workflowBacked) {
  if (!liveJobs.has(check)) fail(`Workflow-backed required check has no matching live workflow job name: ${check}`);
}
console.log(`Required checks: ${required.length}`);
console.log(`Workflow-backed checks: ${workflowBacked.length}`);
console.log(`Live workflow job names: ${liveJobs.size}`);
if (process.exitCode) process.exit(1);
console.log('Merge gate required checks alignment passed.');

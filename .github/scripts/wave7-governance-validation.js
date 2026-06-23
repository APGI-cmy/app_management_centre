#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const repoRoot = process.cwd();
function fail(message) {
  console.error(`::error::${message}`);
  process.exitCode = 1;
}
function exists(file) {
  if (!fs.existsSync(path.join(repoRoot, file))) fail(`Missing required AMC PR1800 artifact: ${file}`);
}
console.log('=== AMC Wave 7 Governance Validation ===');
[
  'ISMS_AMC_REPO_ALIGNMENT.md',
  'FOREMAN_OPERATING_MODEL.md',
  '.agent-admin/control/schemas/delegation-order.schema.json',
  '.agent-admin/control/schemas/handover-allowed.schema.json',
  '.agent-admin/control/schemas/ecap-admin-validation.schema.json',
  '.agent-admin/control/schemas/iaa-preflight-brief.schema.json',
  '.agent-admin/control/protocols/IAA_PREFLIGHT_BRIEF_PROTOCOL.md',
  '.agent-admin/control/merge-gate-required-checks.json',
  '.github/scripts/delegation-order-gate.js',
  '.github/scripts/foreman-prehandover-lane-gate.js',
  '.github/scripts/ecap-admin-boundary-gate.js',
  '.github/scripts/merge-gate-required-checks-alignment.js'
].forEach(exists);
function hasImplementation(files) {
  return files.some((file) => file.startsWith('modules/amc/src/') || file.startsWith('apps/') || file.startsWith('api/') || file.startsWith('lib/') || file.includes('.test.') || file.includes('.spec.'));
}
function hasHandover(files, claim) {
  const text = `${files.join(' ')} ${claim || ''}`.toLowerCase();
  return text.includes('handover') || text.includes('ready for review') || text.includes('merge ready') || text.includes('complete');
}
function runScenario(s) {
  const pass = (!hasImplementation(s.files) || s.delegation) && (!hasHandover(s.files, s.claim) || s.handoverAllowed) && !s.ecapOverstep;
  if (pass !== s.expected) fail(`Scenario ${s.id} expected ${s.expected ? 'PASS' : 'FAIL'} but got ${pass ? 'PASS' : 'FAIL'}`);
  else console.log(`Scenario ${s.id}: ${pass ? 'PASS' : 'FAIL'} as expected`);
}
[
  { id: 'S1-docs-only', files: ['modules/amc/07-implementation-plan/implementation-plan.md'], claim: 'planning update only', delegation: false, handoverAllowed: false, ecapOverstep: false, expected: true },
  { id: 'S2-implementation-no-delegation', files: ['modules/amc/src/index.ts'], claim: 'implementation evidence only', delegation: false, handoverAllowed: false, ecapOverstep: false, expected: false },
  { id: 'S3-implementation-with-delegation', files: ['modules/amc/src/index.ts'], claim: 'implementation evidence only', delegation: true, handoverAllowed: false, ecapOverstep: false, expected: true },
  { id: 'S4-handover-without-lane', files: ['.agent-admin/ecap/handover.md'], claim: 'handover package', delegation: true, handoverAllowed: false, ecapOverstep: false, expected: false },
  { id: 'S5-handover-with-lane', files: ['.agent-admin/ecap/handover.md'], claim: 'handover package', delegation: true, handoverAllowed: true, ecapOverstep: false, expected: true },
  { id: 'S6-ecap-overstep', files: ['.agent-admin/ecap/summary.md'], claim: 'admin bundle', delegation: true, handoverAllowed: true, ecapOverstep: true, expected: false }
].forEach(runScenario);
if (process.exitCode) process.exit(1);
console.log('AMC Wave 7 governance validation passed.');

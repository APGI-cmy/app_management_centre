#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const repoRoot = process.cwd();
const prHeadSha = process.env.PR_HEAD_SHA || process.env.GITHUB_SHA || '';
const prBaseSha = process.env.PR_BASE_SHA || '';
const controlPath = path.join(repoRoot, '.agent-admin/control/handover-allowed.json');

const handoverArtifactPattern = /(^|\/)(PREHANDOVER[^/]*\.md|handover[^/]*\.md)$/i;
const evidenceOnlyPrehandoverPattern = /^\.agent-admin\/prehandover\/ecap-reconciliation-[^/]+\.md$/i;
const handoverPathPattern = /^(\.agent-admin\/handover\/|\.agent-admin\/prehandover\/(?!ecap-reconciliation-[^/]+\.md$)|\.agent-admin\/ecap\/.*handover|\.agent-admin\/quality\/.*handover|modules\/amc\/11-build\/.*handover)/i;
const docsOnlySuppressionPattern = /^(FOREMAN_OPERATING_MODEL\.md|ISMS_AMC_REPO_ALIGNMENT\.md|\.github\/agents\/|\.github\/workflows\/|\.github\/scripts\/|\.agent-admin\/control\/|\.agent-admin\/assurance\/IAA_LEGACY_PREFLIGHT_SUPPRESSION_REGISTER\.md|\.agent-admin\/assurance\/iaa-wave-record-.*\.md|modules\/amc\/(0[0-9]|10|11)-)/;
const explicitHandoverClaim = /\b(final handover|handover package|handover allowed|ready for review|merge ready|build ready|completion claim|wave closure|wave closed)\b/i;
const requiredTrue = ['handover_allowed','foreman_qp_pass','builder_delegation_verified','delegation_precedes_implementation','iaa_prebrief_ready','scope_current','all_required_checks_green'];

function warn(message) { console.warn(`::warning::${message}`); }
function fail(message) { console.error(`::error::${message}`); process.exitCode = 1; }
function git(args) { return execFileSync('git', args, { cwd: repoRoot, encoding: 'utf8' }).trim(); }
function changedFiles() {
  if (process.env.CHANGED_FILES && process.env.CHANGED_FILES.trim()) return process.env.CHANGED_FILES.split(/\r?\n/).map((line) => line.trim()).filter(Boolean);
  if (prBaseSha && prHeadSha) {
    try { return git(['diff', '--name-only', `${prBaseSha}...${prHeadSha}`]).split(/\r?\n/).filter(Boolean); }
    catch (error) { warn(`Could not diff PR base/head: ${error.message}`); }
  }
  try { return git(['diff', '--name-only', 'HEAD~1', 'HEAD']).split(/\r?\n/).filter(Boolean); }
  catch (_error) { return []; }
}
function read(file) {
  try { return fs.readFileSync(path.join(repoRoot, file), 'utf8'); }
  catch (_error) { return ''; }
}
function isSuppressedDocsOnly(file) {
  return docsOnlySuppressionPattern.test(file) && !handoverArtifactPattern.test(file) && !handoverPathPattern.test(file);
}
function hasHandoverClaim(files) {
  for (const file of files) {
    const content = /\.(md|txt|json|yml|yaml)$/i.test(file) ? read(file) : '';
    if (evidenceOnlyPrehandoverPattern.test(file)) {
      if (explicitHandoverClaim.test(content)) return true;
      continue;
    }
    if (handoverArtifactPattern.test(file) || handoverPathPattern.test(file)) return true;
    if (isSuppressedDocsOnly(file)) continue;
    if (content && explicitHandoverClaim.test(content)) return true;
  }
  return false;
}

const files = changedFiles();
console.log('=== AMC Foreman Prehandover Lane Gate ===');
console.log(`Changed files: ${files.length}`);
if (!hasHandoverClaim(files)) {
  console.log('No operative handover/readiness claim detected. ECAP reconciliation evidence alone is not handover. Gate passes.');
  process.exit(0);
}
if (!fs.existsSync(controlPath)) {
  fail('Operative handover/readiness claim detected but .agent-admin/control/handover-allowed.json is missing.');
  process.exit(1);
}
let control;
try { control = JSON.parse(fs.readFileSync(controlPath, 'utf8')); }
catch (error) { fail(`handover-allowed.json is invalid JSON: ${error.message}`); process.exit(1); }
if (control.current_head_sha && prHeadSha && control.current_head_sha !== prHeadSha) fail(`handover-allowed.json current_head_sha ${control.current_head_sha} does not match PR head ${prHeadSha}`);
for (const key of requiredTrue) if (control[key] !== true) fail(`${key} must be true before handover/readiness language is allowed`);
if (control.ecap_required === true && control.ecap_admin_validated !== true) fail('ecap_admin_validated must be true when ecap_required is true');
if (control.iaa_final_required === true) warn('IAA final is required after prehandover lane; do not present as merge-ready until recorded.');
if (Array.isArray(control.blocking_findings) && control.blocking_findings.length > 0) fail(`blocking_findings must be empty before handover: ${control.blocking_findings.join('; ')}`);
if (process.exitCode) process.exit(1);
console.log('Prehandover lane gate passed.');

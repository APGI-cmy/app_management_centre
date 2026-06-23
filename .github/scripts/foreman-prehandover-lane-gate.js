#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const repoRoot = process.cwd();
const prHeadSha = process.env.PR_HEAD_SHA || process.env.GITHUB_SHA || '';
const prBaseSha = process.env.PR_BASE_SHA || '';
const controlPath = path.join(repoRoot, '.agent-admin/control/handover-allowed.json');
const handoverArtifactPattern = /(^|\/)(PREHANDOVER[^/]*\.md|handover[^/]*\.md|.*handover.*\.md)$/i;
const handoverPathPattern = /^(\.agent-admin\/(handover|ecap|quality|assurance)\/|\.agent-workspace\/.*PREHANDOVER|modules\/amc\/11-build\/.*handover)/i;
const handoverLanguage = /(handover|ready[- ]for[- ]review|merge[- ]ready|complete|completion|wave closed|wave closure)/i;
const requiredTrue = ['handover_allowed','foreman_qp_pass','builder_delegation_verified','delegation_precedes_implementation','iaa_prebrief_ready','scope_current','all_required_checks_green'];

function warn(m){ console.warn(`::warning::${m}`); }
function fail(m){ console.error(`::error::${m}`); process.exitCode = 1; }
function git(args){ return execFileSync('git', args, { cwd: repoRoot, encoding: 'utf8' }).trim(); }
function changedFiles(){
  if (process.env.CHANGED_FILES && process.env.CHANGED_FILES.trim()) return process.env.CHANGED_FILES.split(/\r?\n/).map(s=>s.trim()).filter(Boolean);
  if (prBaseSha && prHeadSha) { try { return git(['diff','--name-only',`${prBaseSha}...${prHeadSha}`]).split(/\r?\n/).filter(Boolean); } catch(e){ warn(e.message); } }
  try { return git(['diff','--name-only','HEAD~1','HEAD']).split(/\r?\n/).filter(Boolean); } catch(e){ return []; }
}
function read(file){ try { return fs.readFileSync(path.join(repoRoot, file), 'utf8'); } catch { return ''; } }
function hasHandoverClaim(files){
  for (const file of files) {
    if (handoverArtifactPattern.test(file) || handoverPathPattern.test(file)) return true;
    if (/\.(md|txt|json|yml|yaml)$/i.test(file) && handoverLanguage.test(read(file))) return true;
  }
  return false;
}

const files = changedFiles();
console.log('=== AMC Foreman Pre-Handover Lane Gate ===');
console.log(`Changed files: ${files.length}`);
if (!hasHandoverClaim(files)) {
  console.log('No handover/completion/readiness claim detected. Gate not applicable; pass.');
  process.exit(0);
}
if (!fs.existsSync(controlPath)) {
  fail('Handover language/artifact detected but .agent-admin/control/handover-allowed.json is missing.');
  process.exit(1);
}
let control;
try { control = JSON.parse(fs.readFileSync(controlPath, 'utf8')); } catch(e) { fail(`handover-allowed.json is invalid JSON: ${e.message}`); process.exit(1); }
if (control.current_head_sha && prHeadSha && control.current_head_sha !== prHeadSha) fail(`handover-allowed.json current_head_sha ${control.current_head_sha} does not match PR head ${prHeadSha}`);
for (const key of requiredTrue) if (control[key] !== true) fail(`${key} must be true before handover language is allowed`);
if (control.ecap_required === true && control.ecap_admin_validated !== true) fail('ecap_admin_validated must be true when ecap_required is true');
if (control.iaa_final_required === true) warn('IAA final is required after pre-handover lane; do not present as merge-ready until recorded.');
if (Array.isArray(control.blocking_findings) && control.blocking_findings.length > 0) fail(`blocking_findings must be empty before handover: ${control.blocking_findings.join('; ')}`);
if (process.exitCode) process.exit(1);
console.log('Pre-handover lane gate passed.');

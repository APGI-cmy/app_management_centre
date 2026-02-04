#!/usr/bin/env python3
"""
Agent File Baseline Validation Script

Purpose: Validates agent contract files against CS2-approved baselines
Authority: CS2 Directive (2026-02-04), CS2_AGENT_FILE_AUTHORITY_MODEL.md
Classification: Constitutional Protection Mechanism

Exit Codes:
  0 - Validation passed (files match baselines or no changes)
  1 - Validation failed (files changed without CS2 approval)
  2 - Script error (infrastructure issue)
"""

import os
import sys
import hashlib
import json
from pathlib import Path
from typing import Dict, List, Tuple

def get_file_hash(file_path: Path) -> str:
    """Calculate SHA256 hash of file content"""
    if not file_path.exists():
        return ""
    
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        sha256.update(f.read())
    return sha256.hexdigest()

def get_line_count(file_path: Path) -> int:
    """Get line count of file"""
    if not file_path.exists():
        return 0
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return len(f.readlines())

def find_agent_files() -> List[Path]:
    """Find all agent contract files"""
    agent_dir = Path('.github/agents')
    
    if not agent_dir.exists():
        print("❌ ERROR: .github/agents directory not found")
        return []
    
    # Find all .md files, exclude archives and schemas
    agent_files = []
    for file in agent_dir.glob('*.md'):
        if 'SCHEMA' in file.name or 'README' in file.name or '_archive' in file.name:
            continue
        agent_files.append(file)
    
    return sorted(agent_files)

def check_baseline_exists(agent_file: Path) -> Path:
    """Check if baseline exists for agent file"""
    baseline_dir = Path('governance/baselines/agent-files')
    baseline_path = baseline_dir / agent_file.name
    return baseline_path

def compare_files(agent_file: Path, baseline_path: Path) -> Tuple[bool, Dict]:
    """Compare agent file with baseline"""
    agent_hash = get_file_hash(agent_file)
    baseline_hash = get_file_hash(baseline_path)
    
    agent_lines = get_line_count(agent_file)
    baseline_lines = get_line_count(baseline_path)
    
    matches = agent_hash == baseline_hash
    
    return matches, {
        'agent_file': str(agent_file),
        'baseline_file': str(baseline_path),
        'matches': matches,
        'agent_hash': agent_hash,
        'baseline_hash': baseline_hash,
        'agent_lines': agent_lines,
        'baseline_lines': baseline_lines,
        'lines_diff': agent_lines - baseline_lines
    }

def check_pr_description_for_explanation() -> bool:
    """Check if PR description contains Agent File Change Request section"""
    # GitHub Actions provides PR description via environment variable
    pr_body = os.environ.get('PR_BODY', '')
    
    if not pr_body:
        # Not running in GitHub Actions, skip this check
        return True
    
    # Check for "Agent File Change Request" section
    if "Agent File Change Request" in pr_body or "agent file change request" in pr_body.lower():
        return True
    
    return False

def main():
    """Main validation logic"""
    print("=" * 60)
    print("Agent File Baseline Validation")
    print("=" * 60)
    print()
    
    # Find all agent files
    agent_files = find_agent_files()
    
    if not agent_files:
        print("ℹ️  No agent files found")
        return 0
    
    print(f"Found {len(agent_files)} agent contract files")
    print()
    
    # Track validation results
    mismatches = []
    missing_baselines = []
    matches = []
    
    # Validate each agent file
    for agent_file in agent_files:
        print(f"Validating: {agent_file.name}")
        
        baseline_path = check_baseline_exists(agent_file)
        
        if not baseline_path.exists():
            print(f"  ⚠️  Baseline not found: {baseline_path}")
            print(f"  ℹ️  This is acceptable for initial setup")
            missing_baselines.append(str(agent_file))
            continue
        
        # Compare files
        match, details = compare_files(agent_file, baseline_path)
        
        if match:
            print(f"  ✅ Matches baseline (hash: {details['agent_hash'][:12]}…)")
            matches.append(details)
        else:
            print(f"  ❌ Does NOT match baseline")
            print(f"     Agent hash:    {details['agent_hash'][:12]}…")
            print(f"     Baseline hash: {details['baseline_hash'][:12]}…")
            print(f"     Lines: {details['agent_lines']} (agent) vs {details['baseline_lines']} (baseline)")
            print(f"     Diff: {details['lines_diff']:+d} lines")
            mismatches.append(details)
        
        print() 
    # Summary
    print("=" * 60)
    print("Validation Summary")
    print("=" * 60)
    print()
    
    print(f"✅ Matches baseline: {len(matches)}")
    print(f"⚠️  Missing baseline: {len(missing_baselines)}")
    print(f"❌ Mismatches: {len(mismatches)}")
    print() 
    
    # If no mismatches, validation passes
    if not mismatches:
        if missing_baselines:
            print("✅ VALIDATION PASSED (first-time setup)")
            print()
            print("Missing baselines is acceptable for initial setup.")
            print("CS2 should create baselines using:")
            print("  ./scripts/create_initial_baselines.sh")
        else:
            print("✅ VALIDATION PASSED")
            print()
            print("All agent files match CS2-approved baselines.")
        
        return 0
    
    # Mismatches detected - validation fails
    print("❌ VALIDATION FAILED")
    print() 
    print("Agent files have been modified without CS2 approval.")
    print() 
    
    # Check if PR description has explanation
    has_explanation = check_pr_description_for_explanation()
    
    if not has_explanation:
        print("❌ PR description missing 'Agent File Change Request' section")
        print() 
        print("Agent must add to PR description:")
        print() 
        print("## Agent File Change Request")
        print() 
        print("**File**: {agent-file-name}.md")
        print("**Why**: {plain English reason}")
        print("**What to change**: {plain English description}")
        print("**Authority**: {governance canon reference}")
        print() 
    
    print("Changed files:")
    for mismatch in mismatches:
        print(f"  • {Path(mismatch['agent_file']).name}")
        print(f"    Lines: {mismatch['lines_diff']:+d} ({mismatch['agent_lines']} vs {mismatch['baseline_lines']})")
    print() 
    
    print("Required Actions:")
    print("  1. Agent adds 'Agent File Change Request' to PR description")
    print("  2. CS2 reviews plain English explanation")
    print("  3. CS2 updates baseline if approved:")
    print("     cp .github/agents/{file}.md governance/baselines/agent-files/{file}.md")
    print("     git add governance/baselines/agent-files/{file}.md")
    print("     git commit -m 'Approve {file} changes from PR #XXX'\n")
    print("  4. Agent re-runs PR")
    print() 
    
    # Generate validation report for gate
    report = {
        "validation_result": "FAIL",
        "matches": len(matches),
        "mismatches": len(mismatches),
        "missing_baselines": len(missing_baselines),
        "changed_files": [Path(m['agent_file']).name for m in mismatches],
        "has_explanation": has_explanation
    }
    
    # Write report for GitHub Actions workflow
    report_path = Path('agent-baseline-validation-report.json')
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"Validation report written to: {report_path}")
    print() 
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"❌ SCRIPT ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(2)
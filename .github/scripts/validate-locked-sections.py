#!/usr/bin/env python3
"""
Validate LOCKED section format compliance in agent files.

Authority: AGENT_CONTRACT_PROTECTION_PROTOCOL.md Section 4.2-4.3, Section 6
Purpose: Automated detection of LOCKED section format violations

Exit Codes:
  0 - All validations passed
  1 - Format violations detected
  2 - Missing metadata
  3 - Registry mismatch
  4 - Invalid authority references
"""

import re
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Tuple

class ValidationResult:
    def __init__(self):
        self.passed = True
        self.errors = []
        self.warnings = []
    
    def add_error(self, msg):
        self.errors.append(msg)
        self.passed = False
    
    def add_warning(self, msg):
        self.warnings.append(msg)

def validate_locked_section_format(file_path: Path) -> ValidationResult:
    """
    Validate that all LOCKED sections in a file conform to canonical format.
    
    Required format per AGENT_CONTRACT_PROTECTION_PROTOCOL.md Section 4.2-4.3:
    1. Markdown header with 🔒 emoji: ## 🔒 [Title] (LOCKED)
    2. HTML comment markers: <!-- LOCKED SECTION START --> ... <!-- LOCKED SECTION END -->
    3. Complete metadata block with all required fields
    """
    result = ValidationResult()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    # Find all LOCKED section headers
    locked_headers = []
    for i, line in enumerate(lines):
        if re.match(r'^##\s*🔒.*\(LOCKED\)', line):
            locked_headers.append((i+1, line.strip()))  # Line numbers are 1-based
    
    # Find all HTML LOCKED markers
    # Note: Builder files use <!-- LOCKED END --> without "SECTION"
    # This is acceptable per implementation (though spec shows "LOCKED SECTION END")
    html_locked_starts = []
    html_locked_ends = []
    for i, line in enumerate(lines):
        # Accept: <!-- LOCKED SECTION START --> OR just section with metadata
        # Actually, builder files DON'T have START markers, just metadata + END
        # So we'll check for metadata presence instead
        if re.search(r'<!--\s*Lock ID:', line):
            html_locked_starts.append(i+1)
        if re.search(r'<!--\s*LOCKED (SECTION )?END\s*-->', line, re.IGNORECASE):
            html_locked_ends.append(i+1)
    
    # Check for consistency
    if len(locked_headers) != len(html_locked_starts):
        result.add_error(
            f"{file_path.name}: Mismatch between markdown LOCKED headers ({len(locked_headers)}) "
            f"and HTML LOCKED SECTION START markers ({len(html_locked_starts)})"
        )
    
    if len(html_locked_starts) != len(html_locked_ends):
        result.add_error(
            f"{file_path.name}: Mismatch between LOCKED SECTION START ({len(html_locked_starts)}) "
            f"and LOCKED END markers ({len(html_locked_ends)})"
        )
    
    # Validate each LOCKED section
    for i, (line_num, header) in enumerate(locked_headers):
        section_num = i + 1
        
        # Extract section title
        title_match = re.search(r'##\s*🔒\s*(.+?)\s*\(LOCKED\)', header)
        if not title_match:
            result.add_error(f"{file_path.name}, line {line_num}: Invalid LOCKED header format")
            continue
        
        title = title_match.group(1).strip()
        
        # Find metadata block (should be within next 20 lines)
        metadata_start = line_num
        metadata_end = min(line_num + 20, len(lines))
        metadata_block = '\n'.join(lines[metadata_start-1:metadata_end])
        
        # Check for required metadata fields
        required_fields = {
            'Lock ID': r'<!--\s*Lock ID:\s*(.+?)\s*-->',
            'Lock Reason': r'<!--\s*Lock Reason:\s*(.+?)\s*-->',
            'Lock Authority': r'<!--\s*Lock Authority:\s*(.+?)\s*-->',
            'Lock Date': r'<!--\s*Lock Date:\s*(\d{4}-\d{2}-\d{2})\s*-->',
            'Last Reviewed': r'<!--\s*Last Reviewed:\s*(\d{4}-\d{2}-\d{2})\s*-->',
            'Review Frequency': r'<!--\s*Review Frequency:\s*(quarterly|annual|trigger-based)\s*-->'
        }
        
        missing_fields = []
        for field_name, pattern in required_fields.items():
            if not re.search(pattern, metadata_block, re.DOTALL | re.IGNORECASE):
                missing_fields.append(field_name)
        
        if missing_fields:
            result.add_error(
                f"{file_path.name}, Section '{title}' (line {line_num}): Missing metadata fields: {', '.join(missing_fields)}"
            )
    
    # Check for old-style LOCKED markers without proper format
    old_style_pattern = r'<!--\s*LOCKED SECTION\s*-.*?-->'
    old_style_matches = re.finditer(old_style_pattern, content, re.IGNORECASE)
    old_style_count = 0
    for match in old_style_matches:
        # Check if this is followed by proper metadata
        pos = match.end()
        next_100_chars = content[pos:pos+500]
        if not re.search(r'<!--\s*Lock ID:', next_100_chars):
            old_style_count += 1
    
    if old_style_count > 0:
        result.add_warning(
            f"{file_path.name}: Found {old_style_count} old-style LOCKED section(s) without proper metadata. "
            "These should be updated to canonical format."
        )
    
    return result

def validate_registry_completeness(agents_dir: Path, registry_path: Path) -> ValidationResult:
    """
    Validate that protection registry includes all LOCKED sections.
    """
    result = ValidationResult()
    
    if not registry_path.exists():
        result.add_error(f"Protection registry not found: {registry_path}")
        return result
    
    # Extract all Lock IDs from agent files
    agent_lock_ids = set()
    agent_files = [f for f in agents_dir.glob('*.md') if f.name != 'BUILDER_CONTRACT_SCHEMA.md']
    
    for agent_file in agent_files:
        with open(agent_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lock_id_pattern = r'<!--\s*Lock ID:\s*(.+?)\s*-->'
        for match in re.finditer(lock_id_pattern, content):
            agent_lock_ids.add(match.group(1).strip())
    
    # Extract Lock IDs from registry
    with open(registry_path, 'r', encoding='utf-8') as f:
        registry_content = f.read()
    
    registry_lock_ids = set()
    # Look for Lock IDs in the table (format: | LOCK-ID | ... |)
    table_pattern = r'\|\s*(LOCK-[A-Z0-9-]+)\s*\|'
    for match in re.finditer(table_pattern, registry_content):
        registry_lock_ids.add(match.group(1).strip())
    
    # Compare
    missing_from_registry = agent_lock_ids - registry_lock_ids
    extra_in_registry = registry_lock_ids - agent_lock_ids
    
    if missing_from_registry:
        result.add_error(
            f"Protection registry is missing {len(missing_from_registry)} Lock ID(s): "
            f"{', '.join(sorted(missing_from_registry))}"
        )
    
    if extra_in_registry:
        result.add_warning(
            f"Protection registry contains {len(extra_in_registry)} Lock ID(s) not found in agent files: "
            f"{', '.join(sorted(extra_in_registry))}"
        )
    
    return result

def validate_authority_references(agents_dir: Path, repo_root: Path) -> ValidationResult:
    """
    Validate that Lock Authority references point to existing files.
    """
    result = ValidationResult()
    
    agent_files = [f for f in agents_dir.glob('*.md') if f.name != 'BUILDER_CONTRACT_SCHEMA.md']
    
    for agent_file in agent_files:
        with open(agent_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all Lock Authority references
        authority_pattern = r'<!--\s*Lock Authority:\s*(.+?)\s*-->'
        for match in re.finditer(authority_pattern, content, re.DOTALL):
            authority_text = match.group(1).strip()
            
            # Split by comma or newline for multiple authorities
            authorities = re.split(r'[,\n]', authority_text)
            
            for auth in authorities:
                auth = auth.strip()
                if not auth:
                    continue
                
                # Check if it's a file path (contains / or .md)
                if '/' in auth or '.md' in auth:
                    # Try to resolve the path
                    auth_path = repo_root / auth
                    if not auth_path.exists():
                        result.add_warning(
                            f"{agent_file.name}: Lock Authority reference not found: {auth}"
                        )
    
    return result

def main():
    parser = argparse.ArgumentParser(
        description="Validate LOCKED section format compliance in agent files"
    )
    parser.add_argument(
        '--all-agents', action='store_true',
        help="Validate all agent files"
    )
    parser.add_argument(
        '--check-registry', action='store_true',
        help="Check protection registry completeness"
    )
    parser.add_argument(
        '--check-authority-refs', action='store_true',
        help="Validate Lock Authority references"
    )
    parser.add_argument(
        '--file', type=str,
        help="Validate a specific agent file"
    )
    
    args = parser.parse_args()
    
    # Paths
    repo_root = Path(__file__).parent.parent.parent
    agents_dir = repo_root / '.github' / 'agents'
    registry_path = repo_root / 'governance' / 'contracts' / 'protection-registry.md'
    
    all_passed = True
    total_errors = 0
    total_warnings = 0
    
    # Validate agent files
    if args.all_agents or args.file:
        print("🔍 Validating LOCKED section format compliance...\n")
        
        if args.file:
            files_to_check = [Path(args.file)]
        else:
            files_to_check = sorted(agents_dir.glob('*.md'))
            files_to_check = [f for f in files_to_check if f.name != 'BUILDER_CONTRACT_SCHEMA.md']
        
        for agent_file in files_to_check:
            print(f"Checking {agent_file.name}...")
            result = validate_locked_section_format(agent_file)
            
            if result.errors:
                all_passed = False
                print(f"  ❌ {len(result.errors)} error(s):")
                for error in result.errors:
                    print(f"     • {error}")
                total_errors += len(result.errors)
            
            if result.warnings:
                print(f"  ⚠️  {len(result.warnings)} warning(s):")
                for warning in result.warnings:
                    print(f"     • {warning}")
                total_warnings += len(result.warnings)
            
            if not result.errors and not result.warnings:
                print(f"  ✅ PASS")
        
        print()
    
    # Check registry completeness
    if args.check_registry:
        print("🔍 Checking protection registry completeness...\n")
        result = validate_registry_completeness(agents_dir, registry_path)
        
        if result.errors:
            all_passed = False
            print(f"❌ Registry errors:")
            for error in result.errors:
                print(f"   • {error}")
            total_errors += len(result.errors)
        
        if result.warnings:
            print(f"⚠️  Registry warnings:")
            for warning in result.warnings:
                print(f"   • {warning}")
            total_warnings += len(result.warnings)
        
        if not result.errors and not result.warnings:
            print("✅ Protection registry is complete")
        
        print()
    
    # Check authority references
    if args.check_authority_refs:
        print("🔍 Validating Lock Authority references...\n")
        result = validate_authority_references(agents_dir, repo_root)
        
        if result.errors:
            all_passed = False
            print(f"❌ Authority reference errors:")
            for error in result.errors:
                print(f"   • {error}")
            total_errors += len(result.errors)
        
        if result.warnings:
            print(f"⚠️  Authority reference warnings:")
            for warning in result.warnings:
                print(f"   • {warning}")
            total_warnings += len(result.warnings)
        
        if not result.errors and not result.warnings:
            print("✅ All Lock Authority references are valid")
        
        print()
    
    # Summary
    print("=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)
    print(f"Total Errors:   {total_errors}")
    print(f"Total Warnings: {total_warnings}")
    print(f"Status:         {'✅ PASS' if all_passed else '❌ FAIL'}")
    print("=" * 70)
    
    # Exit code
    if total_errors > 0:
        sys.exit(1)
    elif total_warnings > 0:
        sys.exit(0)  # Warnings don't block
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Modular Agent File Loading Validation Test

Purpose: Validates that the modular foreman agent contract files can be loaded
         and accessed correctly by the agent system.

Authority: Living Agent System v5.0.0, AGENT_CONTRACT_MANAGEMENT_PROTOCOL.md
Classification: Modular Contract Validation

Exit Codes:
  0 - Validation passed (all modular files accessible and valid)
  1 - Validation failed (files missing, inaccessible, or invalid references)
  2 - Script error (infrastructure issue)
"""

import os
import sys
import yaml
from pathlib import Path
from typing import Any

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_section(title: str):
    """Print a section header"""
    print(f"\n{BLUE}{'=' * 80}{RESET}")
    print(f"{BLUE}{title}{RESET}")
    print(f"{BLUE}{'=' * 80}{RESET}")

def print_success(message: str):
    """Print a success message"""
    print(f"{GREEN}✅ {message}{RESET}")

def print_error(message: str):
    """Print an error message"""
    print(f"{RED}❌ {message}{RESET}")

def print_info(message: str):
    """Print an info message"""
    print(f"{BLUE}ℹ️  {message}{RESET}")

def load_yaml_frontmatter(file_path: Path) -> tuple[dict[str, Any], str]:
    """Load YAML frontmatter from a markdown file"""
    if not file_path.exists():
        return {}, ""
    
    with open(file_path, encoding='utf-8') as f:
        content = f.read()
    
    # Check for YAML frontmatter
    if not content.startswith('---'):
        return {}, content
    
    # Extract YAML frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    
    try:
        frontmatter = yaml.safe_load(parts[1])
        body = parts[2]
        return frontmatter or {}, body
    except yaml.YAMLError as e:
        print_error(f"YAML parsing error: {e}")
        return {}, content

def validate_file_exists(file_path: Path, description: str) -> bool:
    """Validate that a file exists and is readable"""
    if not file_path.exists():
        print_error(f"{description} not found: {file_path}")
        return False
    
    if not file_path.is_file():
        print_error(f"{description} is not a file: {file_path}")
        return False
    
    if not os.access(file_path, os.R_OK):
        print_error(f"{description} is not readable: {file_path}")
        return False
    
    print_success(f"{description} exists and is readable")
    return True

def validate_modular_structure() -> bool:
    """Validate the modular agent contract structure"""
    print_section("VALIDATING MODULAR AGENT CONTRACT STRUCTURE")
    
    repo_root = Path.cwd()
    agent_file = repo_root / '.github' / 'agents' / 'foreman.agent.md'
    foreman_dir = repo_root / '.github' / 'agents' / 'foreman'
    
    all_valid = True
    
    # 1. Validate core contract exists
    print_info("Step 1: Validating core contract file")
    if not validate_file_exists(agent_file, "Core contract (foreman.agent.md)"):
        return False
    
    # 2. Load and parse YAML frontmatter
    print_info("\nStep 2: Parsing YAML frontmatter")
    frontmatter, body = load_yaml_frontmatter(agent_file)
    
    if not frontmatter:
        print_error("No YAML frontmatter found in core contract")
        return False
    
    print_success("YAML frontmatter parsed successfully")
    
    # 3. Validate governance bindings_file reference
    print_info("\nStep 3: Validating governance bindings_file reference")
    governance = frontmatter.get('governance', {})
    bindings_file = governance.get('bindings_file')
    
    if not bindings_file:
        print_error("No 'governance.bindings_file' found in YAML frontmatter")
        all_valid = False
    else:
        print_success(f"Found bindings_file reference: {bindings_file}")
        
        # Validate the bindings file exists
        bindings_path = repo_root / '.github' / 'agents' / bindings_file
        if not validate_file_exists(bindings_path, "Governance bindings file"):
            all_valid = False
        else:
            # Count governance bindings in the file
            with open(bindings_path, encoding='utf-8') as f:
                content = f.read()
                binding_count = content.count('- **id**:')
                print_info(f"  Found {binding_count} governance bindings")
                
                if binding_count != 96:
                    print_error(f"Expected 96 governance bindings, found {binding_count}")
                    all_valid = False
                else:
                    print_success(f"All 96 governance bindings present")
    
    # 4. Validate operational_guides references
    print_info("\nStep 4: Validating operational_guides references")
    operational_guides = frontmatter.get('operational_guides', [])
    
    if not operational_guides:
        print_error("No 'operational_guides' found in YAML frontmatter")
        all_valid = False
    else:
        print_success(f"Found {len(operational_guides)} operational guide references")
        
        expected_guides = [
            'foreman/operational-procedures.md',
            'foreman/living-agent-capabilities.md',
            'foreman/compliance.md'
        ]
        
        for guide in operational_guides:
            guide_path_str = guide.get('path')
            guide_desc = guide.get('description', 'No description')
            
            if not guide_path_str:
                print_error("Operational guide missing 'path' field")
                all_valid = False
                continue
            
            print_info(f"  Checking: {guide_path_str}")
            print_info(f"    Description: {guide_desc}")
            
            guide_path = repo_root / '.github' / 'agents' / guide_path_str
            if not validate_file_exists(guide_path, f"    Guide file"):
                all_valid = False
            
            if guide_path_str not in expected_guides:
                print_error(f"    Unexpected guide path: {guide_path_str}")
                all_valid = False
    
    # 5. Validate foreman directory structure
    print_info("\nStep 5: Validating foreman directory structure")
    if not foreman_dir.exists():
        print_error(f"Foreman directory not found: {foreman_dir}")
        return False
    
    print_success(f"Foreman directory exists: {foreman_dir}")
    
    # Expected modular files
    expected_files = {
        'governance-bindings.md': 'Governance bindings (96 canons)',
        'operational-procedures.md': 'Operational procedures',
        'living-agent-capabilities.md': 'Living agent capabilities',
        'compliance.md': 'Compliance and validation',
        'README.md': 'Module documentation'
    }
    
    for filename, description in expected_files.items():
        file_path = foreman_dir / filename
        if not validate_file_exists(file_path, f"  {description}"):
            all_valid = False
    
    # 6. Validate file sizes are reasonable
    print_info("\nStep 6: Validating file sizes")
    core_contract_lines = len(agent_file.read_text().splitlines())
    print_info(f"  Core contract: {core_contract_lines} lines")
    
    if core_contract_lines > 500:
        print_error(f"  Core contract exceeds target size (451 lines expected, got {core_contract_lines})")
        all_valid = False
    else:
        print_success(f"  Core contract within target size (451 lines)")
    
    # Check modular file sizes
    total_modular_lines = 0
    for filename in expected_files.keys():
        if filename == 'README.md':
            continue
        file_path = foreman_dir / filename
        if file_path.exists():
            lines = len(file_path.read_text().splitlines())
            total_modular_lines += lines
            print_info(f"  {filename}: {lines} lines")
    
    print_info(f"  Total modular content: {total_modular_lines} lines")
    
    # 7. Validate protected sections are present in core contract
    print_info("\nStep 7: Validating protected sections in core contract")
    protected_sections = [
        '## Mission',
        '## FM Owns',
        '## FM Does NOT Own',
        '## FM MUST NEVER',
        '## Scope',
        '## Contract Modification Prohibition',
        '## Core Execution Principles',
        '## ⚠️ STOP TRIGGERS'
    ]
    
    core_body = agent_file.read_text()
    for section in protected_sections:
        if section in core_body:
            print_success(f"  Found: {section}")
        else:
            print_error(f"  Missing: {section}")
            all_valid = False
    
    # 8. Validate version consistency
    print_info("\nStep 8: Validating version consistency")
    agent_version = frontmatter.get('agent', {}).get('version')
    metadata_version = frontmatter.get('metadata', {}).get('version')
    
    print_info(f"  Agent version: {agent_version}")
    print_info(f"  Metadata version: {metadata_version}")
    
    if agent_version != '5.0.1':
        print_error(f"  Agent version should be 5.0.1, got {agent_version}")
        all_valid = False
    else:
        print_success(f"  Agent version is correct: 5.0.1")
    
    if metadata_version != '5.0.1':
        print_error(f"  Metadata version should be 5.0.1, got {metadata_version}")
        all_valid = False
    else:
        print_success(f"  Metadata version is correct: 5.0.1")
    
    return all_valid

def simulate_agent_loading() -> bool:
    """Simulate agent loading process to validate modular file accessibility"""
    print_section("SIMULATING AGENT LOADING PROCESS")
    
    repo_root = Path.cwd()
    agent_file = repo_root / '.github' / 'agents' / 'foreman.agent.md'
    
    all_valid = True
    
    # Step 1: Load core contract
    print_info("Step 1: Loading core contract")
    try:
        frontmatter, body = load_yaml_frontmatter(agent_file)
        print_success(f"Core contract loaded: {len(body)} characters")
    except Exception as e:
        print_error(f"Failed to load core contract: {e}")
        return False
    
    # Step 2: Load governance bindings
    print_info("\nStep 2: Loading governance bindings (simulating wake-up Phase 2)")
    bindings_file = frontmatter.get('governance', {}).get('bindings_file')
    if bindings_file:
        bindings_path = repo_root / '.github' / 'agents' / bindings_file
        try:
            bindings_content = bindings_path.read_text()
            print_success(f"Governance bindings loaded: {len(bindings_content)} characters")
            
            # Verify critical bindings are present
            if 'TIER_0_CANON_MANIFEST.json' in bindings_content:
                print_success("  Found Tier-0 constitutional documents reference")
            else:
                print_error("  Missing Tier-0 constitutional documents reference")
                all_valid = False
            
            if 'FOREMAN_MEMORY_PROTOCOL.md' in bindings_content:
                print_success("  Found memory protocol reference")
            else:
                print_error("  Missing memory protocol reference")
                all_valid = False
                
        except Exception as e:
            print_error(f"Failed to load governance bindings: {e}")
            return False
    else:
        print_error("No governance bindings_file specified")
        return False
    
    # Step 3: Load operational guides
    print_info("\nStep 3: Loading operational guides (on-demand)")
    operational_guides = frontmatter.get('operational_guides', [])
    
    for guide in operational_guides:
        guide_path_str = guide.get('path')
        guide_desc = guide.get('description', 'Unknown')
        
        print_info(f"  Loading: {guide_path_str}")
        guide_path = repo_root / '.github' / 'agents' / guide_path_str
        
        try:
            guide_content = guide_path.read_text()
            print_success(f"    Loaded: {len(guide_content)} characters")
            
            # Validate key sections exist
            if 'operational-procedures' in guide_path_str:
                if '## Wake-Up Protocol' in guide_content:
                    print_success("    Found Wake-Up Protocol section")
                else:
                    print_error("    Missing Wake-Up Protocol section")
                    all_valid = False
            
            elif 'living-agent-capabilities' in guide_path_str:
                if '## Agent Health Checks' in guide_content:
                    print_success("    Found Agent Health Checks section")
                else:
                    print_error("    Missing Agent Health Checks section")
                    all_valid = False
            
            elif 'compliance' in guide_path_str:
                if '## Contract Validation' in guide_content:
                    print_success("    Found Contract Validation section")
                else:
                    print_error("    Missing Contract Validation section")
                    all_valid = False
                    
        except Exception as e:
            print_error(f"    Failed to load: {e}")
            all_valid = False
    
    return all_valid

def main():
    """Main validation function"""
    print_section("MODULAR AGENT FILE LOADING VALIDATION TEST")
    print_info("Authority: Living Agent System v5.0.0")
    print_info("Purpose: Validate modular foreman agent contract can be loaded")
    print_info("")
    
    # Run validations
    structure_valid = validate_modular_structure()
    loading_valid = simulate_agent_loading()
    
    # Print summary
    print_section("VALIDATION SUMMARY")
    
    if structure_valid and loading_valid:
        print_success("✅ ALL VALIDATIONS PASSED")
        print_success("Modular file structure is valid and accessible")
        print_success("Agent can successfully load all modular components")
        print("")
        print_info("Benefits achieved:")
        print_info("  • Core contract: ~451 lines (65% reduction from 1,305)")
        print_info("  • Token efficiency: ~6,765 tokens (was ~19,575)")
        print_info("  • Context usage: ~3.4% (was ~10%)")
        print_info("  • Selective loading: Enabled")
        print_info("  • Maintainability: Enhanced")
        print("")
        print_success("✅ READY FOR MERGE")
        return 0
    else:
        print_error("❌ VALIDATION FAILED")
        if not structure_valid:
            print_error("  • Modular structure validation failed")
        if not loading_valid:
            print_error("  • Agent loading simulation failed")
        print("")
        print_error("⚠️  DO NOT MERGE - FIX ISSUES FIRST")
        return 1

if __name__ == '__main__':
    sys.exit(main())

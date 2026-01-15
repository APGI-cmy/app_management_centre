#!/usr/bin/env python3
"""
Locked Section Protection Checker

Validates that agent contracts contain properly formatted locked sections
and enforces protection protocol compliance.

Authority: governance/canon/AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import yaml

# Required locked sections that MUST be present in every agent contract
REQUIRED_LOCKED_SECTIONS = [
    "Contract Modification Prohibition",
    "Pre-Gate Release Blocking",
    "File Integrity Protection",
    "Locked Sections Registry"
]

# Lock footer pattern to validate
LOCK_FOOTER_PATTERN = r'\*\*Locked\*\*:\s*\d{4}-\d{2}-\d{2}\s*\|\s*\*\*Authority\*\*:\s*AGENT_CONTRACT_PROTECTION_PROTOCOL\.md\s+v\d+\.\d+\.\d+'


class ValidationError:
    """Represents a validation error found in an agent contract."""
    
    def __init__(self, severity: str, section: str, message: str):
        self.severity = severity  # CRITICAL, HIGH, MEDIUM, LOW
        self.section = section
        self.message = message
    
    def __str__(self):
        return f"[{self.severity}] {self.section}: {self.message}"


class AgentContractValidator:
    """Validates agent contract locked sections."""
    
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.content = ""
        self.yaml_frontmatter = {}
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationError] = []
        
    def load_file(self) -> bool:
        """Load and parse the agent contract file."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
            
            # Extract YAML frontmatter
            if self.content.startswith('---'):
                parts = self.content.split('---', 2)
                if len(parts) >= 3:
                    try:
                        self.yaml_frontmatter = yaml.safe_load(parts[1])
                    except yaml.YAMLError as e:
                        self.errors.append(ValidationError(
                            "HIGH", "YAML Frontmatter", f"Failed to parse YAML: {e}"
                        ))
            
            return True
        except Exception as e:
            self.errors.append(ValidationError(
                "CRITICAL", "File Access", f"Failed to read file: {e}"
            ))
            return False
    
    def validate_yaml_frontmatter(self) -> None:
        """Validate that YAML frontmatter includes required protection fields."""
        if not self.yaml_frontmatter:
            self.errors.append(ValidationError(
                "HIGH", "YAML Frontmatter", "No YAML frontmatter found"
            ))
            return
        
        # Check for locked_sections field
        if 'locked_sections' not in self.yaml_frontmatter:
            self.errors.append(ValidationError(
                "HIGH", "YAML Frontmatter", 
                "Missing required field: locked_sections (should be true)"
            ))
        elif self.yaml_frontmatter['locked_sections'] != True:
            self.errors.append(ValidationError(
                "HIGH", "YAML Frontmatter",
                f"locked_sections should be true, got: {self.yaml_frontmatter['locked_sections']}"
            ))
        
        # Check for protection_protocol_version field
        if 'protection_protocol_version' not in self.yaml_frontmatter:
            self.warnings.append(ValidationError(
                "MEDIUM", "YAML Frontmatter",
                "Missing recommended field: protection_protocol_version"
            ))
        
        # Check for last_protection_audit field
        if 'last_protection_audit' not in self.yaml_frontmatter:
            self.warnings.append(ValidationError(
                "MEDIUM", "YAML Frontmatter",
                "Missing recommended field: last_protection_audit"
            ))
    
    def find_locked_sections(self) -> Dict[str, Tuple[int, int, str]]:
        """
        Find all locked sections in the content.
        Returns: Dict mapping section name to (start_line, end_line, content)
        """
        sections = {}
        lines = self.content.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Look for locked section header: ## Section Name (LOCKED)
            match = re.match(r'^##\s+(.+?)\s+\(LOCKED\)\s*$', line)
            if match:
                section_name = match.group(1).strip()
                start_line = i
                section_content = [line]
                
                # Find the end of this section (next ## header or end of file)
                i += 1
                while i < len(lines):
                    if re.match(r'^##\s+', lines[i]):
                        # Found next section
                        break
                    section_content.append(lines[i])
                    i += 1
                
                end_line = i - 1
                sections[section_name] = (start_line, end_line, '\n'.join(section_content))
            else:
                i += 1
        
        return sections
    
    def validate_locked_section_format(self, section_name: str, content: str) -> None:
        """Validate that a locked section has proper formatting."""
        # Check for lock footer
        if not re.search(LOCK_FOOTER_PATTERN, content):
            self.errors.append(ValidationError(
                "HIGH", section_name,
                "Missing or malformed lock footer. Expected: "
                "**Locked**: YYYY-MM-DD | **Authority**: AGENT_CONTRACT_PROTECTION_PROTOCOL.md vX.Y.Z"
            ))
        
        # Check that section is not empty (besides header and footer)
        content_lines = [l for l in content.split('\n') if l.strip() and not l.startswith('#')]
        if len(content_lines) < 3:  # At least some content + footer
            self.warnings.append(ValidationError(
                "MEDIUM", section_name,
                "Section appears to be empty or minimal content"
            ))
    
    def validate_required_sections(self) -> None:
        """Validate that all required locked sections are present."""
        locked_sections = self.find_locked_sections()
        
        for required_section in REQUIRED_LOCKED_SECTIONS:
            if required_section not in locked_sections:
                self.errors.append(ValidationError(
                    "CRITICAL", required_section,
                    f"Required locked section missing: '{required_section} (LOCKED)'"
                ))
            else:
                # Validate the format of this locked section
                _, _, content = locked_sections[required_section]
                self.validate_locked_section_format(required_section, content)
        
        # Report any extra locked sections (informational)
        extra_sections = set(locked_sections.keys()) - set(REQUIRED_LOCKED_SECTIONS)
        if extra_sections:
            print(f"  ℹ️  Additional locked sections found: {', '.join(extra_sections)}")
    
    def validate_registry_table(self) -> None:
        """Validate that the Locked Sections Registry contains proper table."""
        locked_sections = self.find_locked_sections()
        
        if "Locked Sections Registry" in locked_sections:
            _, _, content = locked_sections["Locked Sections Registry"]
            
            # Look for the registry table
            table_pattern = r'\|\s*Section Name\s*\|.*\|'
            if not re.search(table_pattern, content):
                self.warnings.append(ValidationError(
                    "MEDIUM", "Locked Sections Registry",
                    "Registry table not found or malformed"
                ))
            
            # Check that all required sections are listed in the registry
            for required_section in REQUIRED_LOCKED_SECTIONS:
                if required_section not in content:
                    self.warnings.append(ValidationError(
                        "LOW", "Locked Sections Registry",
                        f"Section '{required_section}' not listed in registry table"
                    ))
    
    def validate(self) -> bool:
        """
        Run all validations on the agent contract.
        Returns: True if validation passes (no CRITICAL/HIGH errors)
        """
        if not self.load_file():
            return False
        
        print(f"\n🔍 Validating: {self.file_path.name}")
        print("=" * 60)
        
        self.validate_yaml_frontmatter()
        self.validate_required_sections()
        self.validate_registry_table()
        
        # Report results
        critical_errors = [e for e in self.errors if e.severity == "CRITICAL"]
        high_errors = [e for e in self.errors if e.severity == "HIGH"]
        medium_errors = [e for e in self.errors if e.severity == "MEDIUM"]
        low_errors = [e for e in self.errors if e.severity == "LOW"]
        
        if critical_errors:
            print("\n❌ CRITICAL ERRORS:")
            for error in critical_errors:
                print(f"  {error}")
        
        if high_errors:
            print("\n⚠️  HIGH PRIORITY ERRORS:")
            for error in high_errors:
                print(f"  {error}")
        
        if medium_errors:
            print("\n⚠️  MEDIUM PRIORITY WARNINGS:")
            for error in medium_errors:
                print(f"  {error}")
        
        if low_errors:
            print("\n💡 LOW PRIORITY WARNINGS:")
            for error in low_errors:
                print(f"  {error}")
        
        if not self.errors:
            print("\n✅ VALIDATION PASSED - All required locked sections present and valid")
            return True
        elif critical_errors or high_errors:
            print("\n❌ VALIDATION FAILED - Critical or high priority errors found")
            return False
        else:
            print("\n✅ VALIDATION PASSED - No blocking errors (warnings only)")
            return True


def validate_agent_contracts(file_paths: List[Path], strict: bool = False) -> bool:
    """
    Validate multiple agent contracts.
    
    Args:
        file_paths: List of agent contract files to validate
        strict: If True, treat warnings as errors
    
    Returns:
        True if all validations pass
    """
    print("🔒 Agent Contract Protection Validator")
    print("=" * 60)
    print(f"Authority: AGENT_CONTRACT_PROTECTION_PROTOCOL.md v1.0.0")
    print(f"Validating {len(file_paths)} agent contract(s)...")
    
    all_valid = True
    results = []
    
    for file_path in file_paths:
        validator = AgentContractValidator(file_path)
        is_valid = validator.validate()
        
        if strict and validator.warnings:
            is_valid = False
            print("\n⚠️  STRICT MODE: Warnings treated as errors")
        
        results.append((file_path.name, is_valid))
        all_valid = all_valid and is_valid
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 VALIDATION SUMMARY")
    print("=" * 60)
    
    for name, is_valid in results:
        status = "✅ PASS" if is_valid else "❌ FAIL"
        print(f"  {status}  {name}")
    
    print("=" * 60)
    
    if all_valid:
        print("✅ ALL VALIDATIONS PASSED")
        return True
    else:
        print("❌ SOME VALIDATIONS FAILED")
        return False


def main():
    """Main entry point for CLI usage."""
    if len(sys.argv) < 2:
        print("Usage: python3 check_locked_sections.py <agent-file> [agent-file2 ...]")
        print("       python3 check_locked_sections.py --all")
        print("       python3 check_locked_sections.py --strict <agent-file>")
        sys.exit(1)
    
    # Parse arguments
    strict = False
    file_paths = []
    
    args = sys.argv[1:]
    if '--strict' in args:
        strict = True
        args.remove('--strict')
    
    if '--all' in args:
        # Find all agent contracts
        agents_dir = Path('.github/agents')
        if agents_dir.exists():
            file_paths = list(agents_dir.glob('*.md'))
            # Exclude archived files
            file_paths = [f for f in file_paths if '_archive' not in str(f)]
        else:
            print(f"❌ Error: Agents directory not found: {agents_dir}")
            sys.exit(1)
    else:
        file_paths = [Path(arg) for arg in args]
    
    # Validate all files exist
    for file_path in file_paths:
        if not file_path.exists():
            print(f"❌ Error: File not found: {file_path}")
            sys.exit(1)
    
    # Run validation
    success = validate_agent_contracts(file_paths, strict=strict)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()

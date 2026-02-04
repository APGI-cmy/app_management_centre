#!/usr/bin/env python3
"""
Extract LOCKED sections from agent files and generate protection registry.

Authority: AGENT_CONTRACT_PROTECTION_PROTOCOL.md Section 4.4
"""

import re
import sys
from pathlib import Path
from datetime import datetime

def extract_locked_sections(file_path):
    """Extract all LOCKED sections from an agent file."""
    sections = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match LOCKED sections
    pattern = r'## 🔒 (.*?) \(LOCKED\)\s+<!--\s*Lock ID:\s*(.*?)\s*-->\s*<!--\s*Lock Reason:\s*(.*?)\s*-->\s*<!--\s*Lock Authority:\s*(.*?)\s*-->\s*<!--\s*Lock Date:\s*(.*?)\s*-->\s*<!--\s*Last Reviewed:\s*(.*?)\s*-->\s*<!--\s*Review Frequency:\s*(.*?)\s*-->'
    
    matches = re.finditer(pattern, content, re.DOTALL)
    
    for match in matches:
        section = {
            'title': match.group(1).strip(),
            'lock_id': match.group(2).strip(),
            'reason': match.group(3).strip(),
            'authority': match.group(4).strip(),
            'lock_date': match.group(5).strip(),
            'last_reviewed': match.group(6).strip(),
            'review_freq': match.group(7).strip(),
            'file': file_path.name
        }
        sections.append(section)
    
    return sections

def generate_registry(agents_dir):
    """Generate protection registry from all agent files."""
    all_sections = []
    
    agent_files = sorted(agents_dir.glob('*.md'))
    agent_files = [f for f in agent_files if f.name != 'BUILDER_CONTRACT_SCHEMA.md']
    
    for agent_file in agent_files:
        sections = extract_locked_sections(agent_file)
        all_sections.extend(sections)
    
    return all_sections

def write_registry(sections, output_path):
    """Write protection registry markdown file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Agent Contract Protection Registry\n\n")
        f.write("**Authority**: AGENT_CONTRACT_PROTECTION_PROTOCOL.md Section 4.4  \n")
        f.write("**Owner**: governance-liaison  \n")
        f.write(f"**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}  \n")
        f.write(f"**Total LOCKED Sections**: {len(sections)}\n\n")
        
        f.write("---\n\n")
        f.write("## Purpose\n\n")
        f.write("This registry provides a central inventory of all LOCKED sections across all agent contracts ")
        f.write("in this repository. LOCKED sections contain governance-critical requirements that must not be ")
        f.write("modified, removed, or weakened without explicit CS2 approval and governance review.\n\n")
        
        f.write("---\n\n")
        f.write("## Registry Inventory\n\n")
        
        # Table header
        f.write("| Lock ID | Agent File | Section Title | Lock Authority | Lock Date | Last Reviewed | Review Freq |\n")
        f.write("|---------|------------|---------------|----------------|-----------|---------------|-------------|\n")
        
        # Sort by agent file, then by lock ID
        sections.sort(key=lambda x: (x['file'], x['lock_id']))
        
        for section in sections:
            f.write(f"| {section['lock_id']} | {section['file']} | {section['title']} | ")
            f.write(f"{section['authority']} | {section['lock_date']} | ")
            f.write(f"{section['last_reviewed']} | {section['review_freq']} |\n")
        
        f.write("\n---\n\n")
        f.write("## Review Schedule\n\n")
        
        # Group by review frequency
        by_freq = {}
        for section in sections:
            freq = section['review_freq']
            if freq not in by_freq:
                by_freq[freq] = []
            by_freq[freq].append(section)
        
        for freq in sorted(by_freq.keys()):
            f.write(f"### {freq.title()} Review\n\n")
            f.write(f"**Count**: {len(by_freq[freq])} sections\n\n")
            for section in by_freq[freq]:
                f.write(f"- **{section['lock_id']}** ({section['file']}) — Last reviewed: {section['last_reviewed']}\n")
            f.write("\n")
        
        f.write("---\n\n")
        f.write("## Audit Trail\n\n")
        f.write(f"### {datetime.now().strftime('%Y-%m-%d')} — Registry Created\n\n")
        f.write(f"- Initial registry created with {len(sections)} LOCKED sections\n")
        f.write("- All builder agent files (api-builder, ui-builder, schema-builder, qa-builder, integration-builder) ")
        f.write("have 6 LOCKED sections each in canonical format\n")
        f.write("- Foreman-app_FM.md has non-compliant LOCKED section format (corrective action in progress)\n")
        f.write("- Authority: AGENT_CONTRACT_PROTECTION_PROTOCOL.md Section 4.4\n")
        f.write("- Created by: governance-liaison\n")
        f.write("- Purpose: Corrective action for agent file format inconsistency incident\n\n")
        
        f.write("---\n\n")
        f.write("## Change Management\n\n")
        f.write("### Modification Protocol\n\n")
        f.write("**Any modification to a LOCKED section requires**:\n\n")
        f.write("1. **CS2 Approval**: Explicit approval from CS2 (Johan) required\n")
        f.write("2. **Governance Review**: Review against canonical governance requirements\n")
        f.write("3. **Audit Trail**: Update this registry with modification details\n")
        f.write("4. **Protection Script**: Pass `validate-locked-sections.py` validation\n")
        f.write("5. **CI Gate**: Pass `validate-locked-sections.yml` workflow\n\n")
        
        f.write("**Prohibited**:\n")
        f.write("- ❌ Unauthorized modification of LOCKED section content\n")
        f.write("- ❌ Removal of LOCKED section markers\n")
        f.write("- ❌ Weakening of governance requirements\n")
        f.write("- ❌ Modification without updating this registry\n\n")
        
        f.write("---\n\n")
        f.write("## Validation\n\n")
        f.write("**Automated Validation**: `.github/scripts/validate-locked-sections.py`\n\n")
        f.write("```bash\n")
        f.write("# Validate all LOCKED sections\n")
        f.write("python .github/scripts/validate-locked-sections.py --all-agents\n\n")
        f.write("# Check registry completeness\n")
        f.write("python .github/scripts/validate-locked-sections.py --check-registry\n\n")
        f.write("# Validate authority references\n")
        f.write("python .github/scripts/validate-locked-sections.py --check-authority-refs\n")
        f.write("```\n\n")
        f.write("**Exit 0 Required**: All validations must pass before any agent file modification.\n\n")
        
        f.write("---\n\n")
        f.write("**Registry Version**: 1.0.0  \n")
        f.write("**Next Review**: " + datetime.now().strftime('%Y-%m') + " (quarterly)\n")

if __name__ == '__main__':
    # Paths
    repo_root = Path(__file__).parent.parent.parent
    agents_dir = repo_root / '.github' / 'agents'
    output_path = repo_root / 'governance' / 'contracts' / 'protection-registry.md'
    
    # Generate registry
    print("🔍 Scanning agent files for LOCKED sections...")
    sections = generate_registry(agents_dir)
    
    print(f"✅ Found {len(sections)} LOCKED sections")
    
    # Write registry
    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_registry(sections, output_path)
    
    print(f"✅ Protection registry written to: {output_path}")
    print(f"📊 Registry contains {len(sections)} LOCKED sections")
    
    # Report by file
    by_file = {}
    for section in sections:
        fname = section['file']
        if fname not in by_file:
            by_file[fname] = 0
        by_file[fname] += 1
    
    print("\n📋 LOCKED sections by file:")
    for fname in sorted(by_file.keys()):
        print(f"   {fname}: {by_file[fname]} sections")

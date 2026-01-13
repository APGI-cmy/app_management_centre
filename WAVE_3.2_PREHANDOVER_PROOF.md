# PREHANDOVER_PROOF - Evidence Capture

**Agent**: [AGENT_NAME]  
**PR**: #[PR_NUMBER]  
**Branch**: [BRANCH_NAME]  
**Date**: 2026-01-13  
**Latest Commit**: [COMMIT_SHA]  
**Protocol Version**: 2.0.0+  
**Execution Protocol**: Execution Bootstrap Protocol v2.0.0+

**Evidence Capture ID**: capture_20260113_052535

---

## Category 0: Execution Bootstrap Protocol

### Step 3: Validate Exit Codes

| Artifact | Command | Exit Code | Status |
|----------|---------|-----------|--------|
| Artifact 1 | `python3 scripts/validate-builder-environment.py` | 1 | ❌ FAIL |
| Artifact 2 | `ruff check --select UP scripts/*.py governance/scripts/validate_prehandover_proof.py` | 1 | ❌ FAIL |
| Artifact 3 | `python3 scripts/generate-prehandover-proof-template.py --help` | 0 | ✅ PASS |
| Artifact 4 | `bash .githooks/pre-push 2>&1 ` |  head -20 | ❌ FAIL |

**All exit codes are 0**: ❌ NO

---

### Step 4: Evidence Collection

**Evidence Location**: `evidence/prehandover/capture_20260113_052535`

**Captured Evidence**:

#### Artifact 1: `python3 scripts/validate-builder-environment.py`

- **Start Time**: 2026-01-13T05:25:35Z
- **End Time**: 2026-01-13T05:25:35Z
- **Exit Code**: 1
- **Log File**: `evidence/prehandover/capture_20260113_052535/artifact_001.log`
- **Metadata**: `evidence/prehandover/capture_20260113_052535/artifact_001.meta`

<details>
<summary>View Execution Log</summary>

```

[0;34m╔════════════════════════════════════════════════════════════╗[0m
[0;34m║      Builder Environment Validation - BL-026 & Wave 3.2   ║[0m
[0;34m╚════════════════════════════════════════════════════════════╝[0m

  [0;32m✅[0m Python 3.9+
     Version: 3.12.3
  [0;32m✅[0m Git
     Path: /usr/bin/git
  [0;32m✅[0m ruff (BL-026 scanner)
     ruff 0.14.11
  [0;31m❌[0m Git hooks configured
     Run: ./scripts/install-git-hooks.sh
  [0;32m✅[0m BL-026 hook files present


[0;34m╔════════════════════════════════════════════════════════════╗[0m
[0;34m║                  Validation Summary                        ║[0m
[0;34m╚════════════════════════════════════════════════════════════╝[0m

[0;31m❌ Environment validation failed[0m

Please fix the issues above before continuing.

To install missing requirements:
  • Python: https://www.python.org/downloads/
  • ruff: pip install ruff
  • Git hooks: ./scripts/install-git-hooks.sh
```

</details>

---

#### Artifact 2: `ruff check --select UP scripts/*.py governance/scripts/validate_prehandover_proof.py`

- **Start Time**: 2026-01-13T05:25:35Z
- **End Time**: 2026-01-13T05:25:35Z
- **Exit Code**: 1
- **Log File**: `evidence/prehandover/capture_20260113_052535/artifact_002.log`
- **Metadata**: `evidence/prehandover/capture_20260113_052535/artifact_002.meta`

<details>
<summary>View Execution Log</summary>

```
UP035 `typing.List` is deprecated, use `list` instead
  --> scripts/sync-agent-context.py:23:1
   |
21 | from datetime import datetime, timedelta
22 | from pathlib import Path
23 | from typing import List, Dict, Optional, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
24 |
25 | # Project root
   |

UP035 `typing.Dict` is deprecated, use `dict` instead
  --> scripts/sync-agent-context.py:23:1
   |
21 | from datetime import datetime, timedelta
22 | from pathlib import Path
23 | from typing import List, Dict, Optional, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
24 |
25 | # Project root
   |

UP035 `typing.Tuple` is deprecated, use `tuple` instead
  --> scripts/sync-agent-context.py:23:1
   |
21 | from datetime import datetime, timedelta
22 | from pathlib import Path
23 | from typing import List, Dict, Optional, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
24 |
25 | # Project root
   |

UP045 [*] Use `X | None` for type annotations
  --> scripts/sync-agent-context.py:52:25
   |
50 |         self,
51 |         manual: bool = False,
52 |         trigger_reason: Optional[str] = None,
   |                         ^^^^^^^^^^^^^
53 |         canonical_commit: Optional[str] = None
54 |     ) -> List[Dict]:
   |
help: Convert to `X | None`

UP045 [*] Use `X | None` for type annotations
  --> scripts/sync-agent-context.py:53:27
   |
51 |         manual: bool = False,
52 |         trigger_reason: Optional[str] = None,
53 |         canonical_commit: Optional[str] = None
   |                           ^^^^^^^^^^^^^
54 |     ) -> List[Dict]:
55 |         """
   |
help: Convert to `X | None`

UP006 [*] Use `list` instead of `List` for type annotation
  --> scripts/sync-agent-context.py:54:10
   |
52 |         trigger_reason: Optional[str] = None,
53 |         canonical_commit: Optional[str] = None
54 |     ) -> List[Dict]:
   |          ^^^^
55 |         """
56 |         Detect trigger events from canonical governance changes.
   |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
  --> scripts/sync-agent-context.py:54:15
   |
52 |         trigger_reason: Optional[str] = None,
53 |         canonical_commit: Optional[str] = None
54 |     ) -> List[Dict]:
   |               ^^^^
55 |         """
56 |         Detect trigger events from canonical governance changes.
   |
help: Replace with `dict`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:106:49
    |
104 |         return triggers
105 |     
106 |     def evaluate_affected_agents(self, trigger: Dict) -> List[Dict]:
    |                                                 ^^^^
107 |         """
108 |         Evaluate which agents are affected by trigger event.
    |
help: Replace with `dict`

UP006 [*] Use `list` instead of `List` for type annotation
   --> scripts/sync-agent-context.py:106:58
    |
104 |         return triggers
105 |     
106 |     def evaluate_affected_agents(self, trigger: Dict) -> List[Dict]:
    |                                                          ^^^^
107 |         """
108 |         Evaluate which agents are affected by trigger event.
    |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:106:63
    |
104 |         return triggers
105 |     
106 |     def evaluate_affected_agents(self, trigger: Dict) -> List[Dict]:
    |                                                               ^^^^
107 |         """
108 |         Evaluate which agents are affected by trigger event.
    |
help: Replace with `dict`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:156:18
    |
154 |     def prepare_context_updates(
155 |         self,
156 |         trigger: Dict,
    |                  ^^^^
157 |         affected_agents: List[Dict]
158 |     ) -> List[Dict]:
    |
help: Replace with `dict`

UP006 [*] Use `list` instead of `List` for type annotation
   --> scripts/sync-agent-context.py:157:26
    |
155 |         self,
156 |         trigger: Dict,
157 |         affected_agents: List[Dict]
    |                          ^^^^
158 |     ) -> List[Dict]:
159 |         """
    |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:157:31
    |
155 |         self,
156 |         trigger: Dict,
157 |         affected_agents: List[Dict]
    |                               ^^^^
158 |     ) -> List[Dict]:
159 |         """
    |
help: Replace with `dict`

UP006 [*] Use `list` instead of `List` for type annotation
   --> scripts/sync-agent-context.py:158:10
    |
156 |         trigger: Dict,
157 |         affected_agents: List[Dict]
158 |     ) -> List[Dict]:
    |          ^^^^
159 |         """
160 |         Prepare context updates for affected agents.
    |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:158:15
    |
156 |         trigger: Dict,
157 |         affected_agents: List[Dict]
158 |     ) -> List[Dict]:
    |               ^^^^
159 |         """
160 |         Prepare context updates for affected agents.
    |
help: Replace with `dict`

UP006 [*] Use `list` instead of `List` for type annotation
   --> scripts/sync-agent-context.py:206:42
    |
204 |         return updates
205 |     
206 |     def request_approvals(self, updates: List[Dict], trigger: Dict) -> Dict[str, str]:
    |                                          ^^^^
207 |         """
208 |         Request approvals for updates.
    |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:206:47
    |
204 |         return updates
205 |     
206 |     def request_approvals(self, updates: List[Dict], trigger: Dict) -> Dict[str, str]:
    |                                               ^^^^
207 |         """
208 |         Request approvals for updates.
    |
help: Replace with `dict`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:206:63
    |
204 |         return updates
205 |     
206 |     def request_approvals(self, updates: List[Dict], trigger: Dict) -> Dict[str, str]:
    |                                                               ^^^^
207 |         """
208 |         Request approvals for updates.
    |
help: Replace with `dict`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:206:72
    |
204 |         return updates
205 |     
206 |     def request_approvals(self, updates: List[Dict], trigger: Dict) -> Dict[str, str]:
    |                                                                        ^^^^
207 |         """
208 |         Request approvals for updates.
    |
help: Replace with `dict`

UP006 [*] Use `list` instead of `List` for type annotation
   --> scripts/sync-agent-context.py:246:18
    |
244 |     def apply_updates(
245 |         self,
246 |         updates: List[Dict],
    |                  ^^^^
247 |         approvals: Dict[str, str]
248 |     ) -> Tuple[List[Dict], List[Dict]]:
    |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:246:23
    |
244 |     def apply_updates(
245 |         self,
246 |         updates: List[Dict],
    |                       ^^^^
247 |         approvals: Dict[str, str]
248 |     ) -> Tuple[List[Dict], List[Dict]]:
    |
help: Replace with `dict`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:247:20
    |
245 |         self,
246 |         updates: List[Dict],
247 |         approvals: Dict[str, str]
    |                    ^^^^
248 |     ) -> Tuple[List[Dict], List[Dict]]:
249 |         """
    |
help: Replace with `dict`

UP006 [*] Use `tuple` instead of `Tuple` for type annotation
   --> scripts/sync-agent-context.py:248:10
    |
246 |         updates: List[Dict],
247 |         approvals: Dict[str, str]
248 |     ) -> Tuple[List[Dict], List[Dict]]:
    |          ^^^^^
249 |         """
250 |         Apply approved updates to agent context files.
    |
help: Replace with `tuple`

UP006 [*] Use `list` instead of `List` for type annotation
   --> scripts/sync-agent-context.py:248:16
    |
246 |         updates: List[Dict],
247 |         approvals: Dict[str, str]
248 |     ) -> Tuple[List[Dict], List[Dict]]:
    |                ^^^^
249 |         """
250 |         Apply approved updates to agent context files.
    |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:248:21
    |
246 |         updates: List[Dict],
247 |         approvals: Dict[str, str]
248 |     ) -> Tuple[List[Dict], List[Dict]]:
    |                     ^^^^
249 |         """
250 |         Apply approved updates to agent context files.
    |
help: Replace with `dict`

UP006 [*] Use `list` instead of `List` for type annotation
   --> scripts/sync-agent-context.py:248:28
    |
246 |         updates: List[Dict],
247 |         approvals: Dict[str, str]
248 |     ) -> Tuple[List[Dict], List[Dict]]:
    |                            ^^^^
249 |         """
250 |         Apply approved updates to agent context files.
    |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:248:33
    |
246 |         updates: List[Dict],
247 |         approvals: Dict[str, str]
248 |     ) -> Tuple[List[Dict], List[Dict]]:
    |                                 ^^^^
249 |         """
250 |         Apply approved updates to agent context files.
    |
help: Replace with `dict`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:286:18
    |
284 |     def log_sync_event(
285 |         self,
286 |         trigger: Dict,
    |                  ^^^^
287 |         updates: List[Dict],
288 |         outcome: str
    |
help: Replace with `dict`

UP006 [*] Use `list` instead of `List` for type annotation
   --> scripts/sync-agent-context.py:287:18
    |
285 |         self,
286 |         trigger: Dict,
287 |         updates: List[Dict],
    |                  ^^^^
288 |         outcome: str
289 |     ) -> Dict:
    |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:287:23
    |
285 |         self,
286 |         trigger: Dict,
287 |         updates: List[Dict],
    |                       ^^^^
288 |         outcome: str
289 |     ) -> Dict:
    |
help: Replace with `dict`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:289:10
    |
287 |         updates: List[Dict],
288 |         outcome: str
289 |     ) -> Dict:
    |          ^^^^
290 |         """
291 |         Log synchronisation event for audit.
    |
help: Replace with `dict`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/sync-agent-context.py:410:40
    |
408 |         return False
409 |     
410 |     def _write_sync_event(self, event: Dict):
    |                                        ^^^^
411 |         """Write sync event to audit log."""
412 |         # Ensure directory exists
    |
help: Replace with `dict`

UP015 [*] Unnecessary mode argument
   --> scripts/sync-agent-context.py:417:39
    |
415 |         # Read existing log
416 |         if AUDIT_LOG_PATH.exists():
417 |             with open(AUDIT_LOG_PATH, 'r') as f:
    |                                       ^^^
418 |                 log = json.load(f)
419 |         else:
    |
help: Remove mode argument

UP035 `typing.Dict` is deprecated, use `dict` instead
  --> scripts/validate_branch_protection_enforcement.py:26:1
   |
24 | from pathlib import Path
25 | from datetime import datetime
26 | from typing import Dict, List, Any, Optional
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |

UP035 `typing.List` is deprecated, use `list` instead
  --> scripts/validate_branch_protection_enforcement.py:26:1
   |
24 | from pathlib import Path
25 | from datetime import datetime
26 | from typing import Dict, List, Any, Optional
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |

UP015 [*] Unnecessary mode argument
  --> scripts/validate_branch_protection_enforcement.py:87:38
   |
86 |         try:
87 |             with open(manifest_file, 'r') as f:
   |                                      ^^^
88 |                 self.manifest = json.load(f)
   |
help: Remove mode argument

UP015 [*] Unnecessary mode argument
  --> scripts/validate_builder_contracts.py:33:29
   |
31 |     """Check that file has valid YAML frontmatter"""
32 |     try:
33 |         with open(filepath, 'r') as f:
   |                             ^^^
34 |             content = f.read()
35 |             if not content.startswith('---'):
   |
help: Remove mode argument

UP015 [*] Unnecessary mode argument
   --> scripts/validate_builder_contracts.py:336:28
    |
335 |     # Check schema version
336 |     with open(schema_path, 'r') as f:
    |                            ^^^
337 |         schema_content = f.read()
338 |         if 'Version**: 2.0' in schema_content or '**Version**: 2.0' in schema_content:
    |
help: Remove mode argument

UP035 `typing.Dict` is deprecated, use `dict` instead
  --> scripts/validate_builder_modular_links.py:25:1
   |
23 | from pathlib import Path
24 | from datetime import datetime
25 | from typing import Dict, List, Tuple, Optional
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
26 |
27 | def log_info(message: str, verbose: bool = False):
   |

UP035 `typing.List` is deprecated, use `list` instead
  --> scripts/validate_builder_modular_links.py:25:1
   |
23 | from pathlib import Path
24 | from datetime import datetime
25 | from typing import Dict, List, Tuple, Optional
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
26 |
27 | def log_info(message: str, verbose: bool = False):
   |

UP035 `typing.Tuple` is deprecated, use `tuple` instead
  --> scripts/validate_builder_modular_links.py:25:1
   |
23 | from pathlib import Path
24 | from datetime import datetime
25 | from typing import Dict, List, Tuple, Optional
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
26 |
27 | def log_info(message: str, verbose: bool = False):
   |

UP006 [*] Use `list` instead of `List` for type annotation
  --> scripts/validate_builder_modular_links.py:44:64
   |
42 |     print(f"❌ {message}")
43 |
44 | def extract_reference_links(content: str, source_file: str) -> List[Dict[str, str]]:
   |                                                                ^^^^
45 |     """
46 |     Extract all reference links to extended documentation from agent file content.
   |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
  --> scripts/validate_builder_modular_links.py:44:69
   |
42 |     print(f"❌ {message}")
43 |
44 | def extract_reference_links(content: str, source_file: str) -> List[Dict[str, str]]:
   |                                                                     ^^^^
45 |     """
46 |     Extract all reference links to extended documentation from agent file content.
   |
help: Replace with `dict`

UP006 [*] Use `dict` instead of `Dict` for type annotation
  --> scripts/validate_builder_modular_links.py:79:48
   |
77 |     return links
78 |
79 | def validate_file_exists(base_dir: Path, link: Dict[str, str]) -> Tuple[bool, Optional[str]]:
   |                                                ^^^^
80 |     """
81 |     Validate that the referenced file exists.
   |
help: Replace with `dict`

UP006 [*] Use `tuple` instead of `Tuple` for type annotation
  --> scripts/validate_builder_modular_links.py:79:67
   |
77 |     return links
78 |
79 | def validate_file_exists(base_dir: Path, link: Dict[str, str]) -> Tuple[bool, Optional[str]]:
   |                                                                   ^^^^^
80 |     """
81 |     Validate that the referenced file exists.
   |
help: Replace with `tuple`

UP045 [*] Use `X | None` for type annotations
  --> scripts/validate_builder_modular_links.py:79:79
   |
77 |     return links
78 |
79 | def validate_file_exists(base_dir: Path, link: Dict[str, str]) -> Tuple[bool, Optional[str]]:
   |                                                                               ^^^^^^^^^^^^^
80 |     """
81 |     Validate that the referenced file exists.
   |
help: Convert to `X | None`

UP006 [*] Use `dict` instead of `Dict` for type annotation
  --> scripts/validate_builder_modular_links.py:94:54
   |
92 |     return True, None
93 |
94 | def validate_section_reference(base_dir: Path, link: Dict[str, str]) -> Tuple[bool, Optional[str]]:
   |                                                      ^^^^
95 |     """
96 |     Validate section references if present in the link context.
   |
help: Replace with `dict`

UP006 [*] Use `tuple` instead of `Tuple` for type annotation
  --> scripts/validate_builder_modular_links.py:94:73
   |
92 |     return True, None
93 |
94 | def validate_section_reference(base_dir: Path, link: Dict[str, str]) -> Tuple[bool, Optional[str]]:
   |                                                                         ^^^^^
95 |     """
96 |     Validate section references if present in the link context.
   |
help: Replace with `tuple`

UP045 [*] Use `X | None` for type annotations
  --> scripts/validate_builder_modular_links.py:94:85
   |
92 |     return True, None
93 |
94 | def validate_section_reference(base_dir: Path, link: Dict[str, str]) -> Tuple[bool, Optional[str]]:
   |                                                                                     ^^^^^^^^^^^^^
95 |     """
96 |     Validate section references if present in the link context.
   |
help: Convert to `X | None`

UP015 [*] Unnecessary mode argument
   --> scripts/validate_builder_modular_links.py:120:30
    |
119 |     try:
120 |         with open(file_path, 'r', encoding='utf-8') as f:
    |                              ^^^
121 |             content = f.read()
    |
help: Remove mode argument

UP006 [*] Use `tuple` instead of `Tuple` for type annotation
   --> scripts/validate_builder_modular_links.py:140:93
    |
138 |         return False, f"Error reading file {link['path']}: {str(e)}"
139 |
140 | def validate_builder_agent_file(base_dir: Path, agent_file: Path, verbose: bool = False) -> Tuple[bool, Dict]:
    |                                                                                             ^^^^^
141 |     """
142 |     Validate a single builder agent file's modular links.
    |
help: Replace with `tuple`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/validate_builder_modular_links.py:140:105
    |
138 |         return False, f"Error reading file {link['path']}: {str(e)}"
139 |
140 | def validate_builder_agent_file(base_dir: Path, agent_file: Path, verbose: bool = False) -> Tuple[bool, Dict]:
    |                                                                                                         ^^^^
141 |     """
142 |     Validate a single builder agent file's modular links.
    |
help: Replace with `dict`

UP015 [*] Unnecessary mode argument
   --> scripts/validate_builder_modular_links.py:160:31
    |
158 |     # Read agent file
159 |     try:
160 |         with open(agent_file, 'r', encoding='utf-8') as f:
    |                               ^^^
161 |             content = f.read()
162 |     except Exception as e:
    |
help: Remove mode argument

UP006 [*] Use `list` instead of `List` for type annotation
   --> scripts/validate_builder_modular_links.py:211:55
    |
209 |     return success, results
210 |
211 | def get_builders_from_filesystem(agents_dir: Path) -> List[str]:
    |                                                       ^^^^
212 |     """
213 |     Dynamically discover builders from the filesystem.
    |
help: Replace with `list`

UP006 [*] Use `tuple` instead of `Tuple` for type annotation
   --> scripts/validate_builder_modular_links.py:238:81
    |
236 |     return sorted(builders)
237 |
238 | def validate_extended_reference_files(base_dir: Path, verbose: bool = False) -> Tuple[bool, Dict]:
    |                                                                                 ^^^^^
239 |     """
240 |     Validate that all expected extended reference files exist and are accessible.
    |
help: Replace with `tuple`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/validate_builder_modular_links.py:238:93
    |
236 |     return sorted(builders)
237 |
238 | def validate_extended_reference_files(base_dir: Path, verbose: bool = False) -> Tuple[bool, Dict]:
    |                                                                                             ^^^^
239 |     """
240 |     Validate that all expected extended reference files exist and are accessible.
    |
help: Replace with `dict`

UP015 [*] Unnecessary mode argument
   --> scripts/validate_builder_modular_links.py:279:37
    |
277 |         if ref_file.exists():
278 |             try:
279 |                 with open(ref_file, 'r', encoding='utf-8') as f:
    |                                     ^^^
280 |                     content = f.read()
281 |                     file_info['readable'] = True
    |
help: Remove mode argument

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/validate_builder_modular_links.py:295:43
    |
293 |     return success, results
294 |
295 | def generate_evidence_report(all_results: Dict, output_path: Path):
    |                                           ^^^^
296 |     """Generate evidence report in JSON format"""
297 |     evidence = {
    |
help: Replace with `dict`

UP035 `typing.Dict` is deprecated, use `dict` instead
  --> scripts/validate_code_review_closure.py:26:1
   |
24 | import jsonschema
25 | from pathlib import Path
26 | from typing import Dict, List, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
27 | from datetime import datetime
   |

UP035 `typing.List` is deprecated, use `list` instead
  --> scripts/validate_code_review_closure.py:26:1
   |
24 | import jsonschema
25 | from pathlib import Path
26 | from typing import Dict, List, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
27 | from datetime import datetime
   |

UP035 `typing.Tuple` is deprecated, use `tuple` instead
  --> scripts/validate_code_review_closure.py:26:1
   |
24 | import jsonschema
25 | from pathlib import Path
26 | from typing import Dict, List, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
27 | from datetime import datetime
   |

UP015 [*] Unnecessary mode argument
  --> scripts/validate_code_review_closure.py:57:36
   |
56 |         try:
57 |             with open(schema_file, 'r') as f:
   |                                    ^^^
58 |                 self.schema = json.load(f)
   |
help: Remove mode argument

UP006 [*] Use `tuple` instead of `Tuple` for type annotation
  --> scripts/validate_code_review_closure.py:77:59
   |
75 |             return False
76 |     
77 |     def find_artifact(self, explicit_path: str = None) -> Tuple[bool, str]:
   |                                                           ^^^^^
78 |         """Find code review closure artifact"""
79 |         if explicit_path:
   |
help: Replace with `tuple`

UP006 [*] Use `tuple` instead of `Tuple` for type annotation
   --> scripts/validate_code_review_closure.py:104:61
    |
102 |         return True, str(artifact_path)
103 |     
104 |     def validate_artifact_json(self, artifact_path: str) -> Tuple[bool, Dict]:
    |                                                             ^^^^^
105 |         """Validate artifact is valid JSON"""
106 |         try:
    |
help: Replace with `tuple`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/validate_code_review_closure.py:104:73
    |
102 |         return True, str(artifact_path)
103 |     
104 |     def validate_artifact_json(self, artifact_path: str) -> Tuple[bool, Dict]:
    |                                                                         ^^^^
105 |         """Validate artifact is valid JSON"""
106 |         try:
    |
help: Replace with `dict`

UP015 [*] Unnecessary mode argument
   --> scripts/validate_code_review_closure.py:107:38
    |
105 |         """Validate artifact is valid JSON"""
106 |         try:
107 |             with open(artifact_path, 'r') as f:
    |                                      ^^^
108 |                 artifact = json.load(f)
    |
help: Remove mode argument

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/validate_code_review_closure.py:135:52
    |
133 |             return False, {}
134 |     
135 |     def validate_schema_compliance(self, artifact: Dict) -> bool:
    |                                                    ^^^^
136 |         """Validate artifact against schema"""
137 |         try:
    |
help: Replace with `dict`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/validate_code_review_closure.py:167:47
    |
165 |             return False
166 |     
167 |     def validate_immutability(self, artifact: Dict) -> bool:
    |                                               ^^^^
168 |         """Validate artifact is marked immutable"""
169 |         if not artifact.get('immutable'):
    |
help: Replace with `dict`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/validate_code_review_closure.py:186:42
    |
184 |         return True
185 |     
186 |     def validate_verdict(self, artifact: Dict) -> bool:
    |                                          ^^^^
187 |         """Validate final verdict is present and complete"""
188 |         verdict = artifact.get('final_verdict', {})
    |
help: Replace with `dict`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/validate_code_review_closure.py:228:49
    |
226 |         return True
227 |     
228 |     def validate_reviewed_files(self, artifact: Dict) -> bool:
    |                                                 ^^^^
229 |         """Validate that at least one file was reviewed"""
230 |         reviewed = artifact.get('what_was_reviewed', {})
    |
help: Replace with `dict`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/validate_code_review_closure.py:250:48
    |
248 |         return True
249 |     
250 |     def validate_artifact_type(self, artifact: Dict) -> bool:
    |                                                ^^^^
251 |         """Validate artifact type is correct"""
252 |         metadata = artifact.get('artifact_metadata', {})
    |
help: Replace with `dict`

UP035 `typing.Set` is deprecated, use `set` instead
  --> scripts/validate_governance_coupling.py:24:1
   |
22 | import subprocess
23 | from pathlib import Path
24 | from typing import Set, List, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
25 |
26 | class GovernanceCouplingValidator:
   |

UP035 `typing.List` is deprecated, use `list` instead
  --> scripts/validate_governance_coupling.py:24:1
   |
22 | import subprocess
23 | from pathlib import Path
24 | from typing import Set, List, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
25 |
26 | class GovernanceCouplingValidator:
   |

UP035 `typing.Tuple` is deprecated, use `tuple` instead
  --> scripts/validate_governance_coupling.py:24:1
   |
22 | import subprocess
23 | from pathlib import Path
24 | from typing import Set, List, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
25 |
26 | class GovernanceCouplingValidator:
   |

UP006 [*] Use `set` instead of `Set` for type annotation
  --> scripts/validate_governance_coupling.py:60:36
   |
58 |         self.validations = []
59 |         
60 |     def get_changed_files(self) -> Set[str]:
   |                                    ^^^
61 |         """Get list of files changed in current branch vs base"""
62 |         try:
   |
help: Replace with `set`

UP006 [*] Use `set` instead of `Set` for type annotation
  --> scripts/validate_governance_coupling.py:89:50
   |
87 |             return set()
88 |     
89 |     def check_tier0_changes(self, changed_files: Set[str]) -> Tuple[bool, Set[str]]:
   |                                                  ^^^
90 |         """Check if any Tier-0 governance files were changed"""
91 |         tier0_changes = changed_files & self.TIER_0_GOVERNANCE_FILES
   |
help: Replace with `set`

UP006 [*] Use `tuple` instead of `Tuple` for type annotation
  --> scripts/validate_governance_coupling.py:89:63
   |
87 |             return set()
88 |     
89 |     def check_tier0_changes(self, changed_files: Set[str]) -> Tuple[bool, Set[str]]:
   |                                                               ^^^^^
90 |         """Check if any Tier-0 governance files were changed"""
91 |         tier0_changes = changed_files & self.TIER_0_GOVERNANCE_FILES
   |
help: Replace with `tuple`

UP006 [*] Use `set` instead of `Set` for type annotation
  --> scripts/validate_governance_coupling.py:89:75
   |
87 |             return set()
88 |     
89 |     def check_tier0_changes(self, changed_files: Set[str]) -> Tuple[bool, Set[str]]:
   |                                                                           ^^^
90 |         """Check if any Tier-0 governance files were changed"""
91 |         tier0_changes = changed_files & self.TIER_0_GOVERNANCE_FILES
   |
help: Replace with `set`

UP006 [*] Use `set` instead of `Set` for type annotation
  --> scripts/validate_governance_coupling.py:94:59
   |
92 |         return len(tier0_changes) > 0, tier0_changes
93 |     
94 |     def check_coupling_files_updated(self, changed_files: Set[str]) -> Tuple[bool, Set[str]]:
   |                                                           ^^^
95 |         """Check if required coupling files were updated"""
96 |         coupling_files_changed = changed_files & self.REQUIRED_COUPLING_FILES
   |
help: Replace with `set`

UP006 [*] Use `tuple` instead of `Tuple` for type annotation
  --> scripts/validate_governance_coupling.py:94:72
   |
92 |         return len(tier0_changes) > 0, tier0_changes
93 |     
94 |     def check_coupling_files_updated(self, changed_files: Set[str]) -> Tuple[bool, Set[str]]:
   |                                                                        ^^^^^
95 |         """Check if required coupling files were updated"""
96 |         coupling_files_changed = changed_files & self.REQUIRED_COUPLING_FILES
   |
help: Replace with `tuple`

UP006 [*] Use `set` instead of `Set` for type annotation
  --> scripts/validate_governance_coupling.py:94:84
   |
92 |         return len(tier0_changes) > 0, tier0_changes
93 |     
94 |     def check_coupling_files_updated(self, changed_files: Set[str]) -> Tuple[bool, Set[str]]:
   |                                                                                    ^^^
95 |         """Check if required coupling files were updated"""
96 |         coupling_files_changed = changed_files & self.REQUIRED_COUPLING_FILES
   |
help: Replace with `set`

UP035 `typing.Dict` is deprecated, use `dict` instead
  --> scripts/validate_tier0_activation.py:27:1
   |
25 | import json
26 | from pathlib import Path
27 | from typing import Dict, List, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
28 |
29 | class Tier0ActivationValidator:
   |

UP035 `typing.List` is deprecated, use `list` instead
  --> scripts/validate_tier0_activation.py:27:1
   |
25 | import json
26 | from pathlib import Path
27 | from typing import Dict, List, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
28 |
29 | class Tier0ActivationValidator:
   |

UP035 `typing.Tuple` is deprecated, use `tuple` instead
  --> scripts/validate_tier0_activation.py:27:1
   |
25 | import json
26 | from pathlib import Path
27 | from typing import Dict, List, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
28 |
29 | class Tier0ActivationValidator:
   |

UP015 [*] Unnecessary mode argument
  --> scripts/validate_tier0_activation.py:56:38
   |
55 |         try:
56 |             with open(manifest_file, 'r') as f:
   |                                      ^^^
57 |                 self.manifest = json.load(f)
   |
help: Remove mode argument

UP015 [*] Unnecessary mode argument
   --> scripts/validate_tier0_activation.py:166:35
    |
165 |         try:
166 |             with open(agent_file, 'r') as f:
    |                                   ^^^
167 |                 content = f.read()
    |
help: Remove mode argument

UP015 [*] Unnecessary mode argument
   --> scripts/validate_tier0_activation.py:232:35
    |
231 |         try:
232 |             with open(agent_file, 'r') as f:
    |                                   ^^^
233 |                 content = f.read()
    |
help: Remove mode argument

UP006 [*] Use `list` instead of `List` for type annotation
   --> scripts/validate_tier0_activation.py:276:48
    |
274 |             return False
275 |     
276 |     def validate_tier0_count(self, tier0_docs: List[Dict]) -> bool:
    |                                                ^^^^
277 |         """Validate that exactly 12 Tier-0 documents are referenced"""
278 |         doc_count = len(tier0_docs)
    |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/validate_tier0_activation.py:276:53
    |
274 |             return False
275 |     
276 |     def validate_tier0_count(self, tier0_docs: List[Dict]) -> bool:
    |                                                     ^^^^
277 |         """Validate that exactly 12 Tier-0 documents are referenced"""
278 |         doc_count = len(tier0_docs)
    |
help: Replace with `dict`

UP006 [*] Use `list` instead of `List` for type annotation
   --> scripts/validate_tier0_activation.py:297:61
    |
295 |         return True
296 |     
297 |     def validate_documents_match_manifest(self, tier0_docs: List[Dict]) -> bool:
    |                                                             ^^^^
298 |         """Validate that agent contract documents match the manifest"""
299 |         manifest_docs = {doc['id']: doc for doc in self.manifest['tier_0_canonical_documents']}
    |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/validate_tier0_activation.py:297:66
    |
295 |         return True
296 |     
297 |     def validate_documents_match_manifest(self, tier0_docs: List[Dict]) -> bool:
    |                                                                  ^^^^
298 |         """Validate that agent contract documents match the manifest"""
299 |         manifest_docs = {doc['id']: doc for doc in self.manifest['tier_0_canonical_documents']}
    |
help: Replace with `dict`

UP006 [*] Use `list` instead of `List` for type annotation
   --> scripts/validate_tier0_activation.py:360:42
    |
358 |         return True
359 |     
360 |     def extract_tier0_documents(self) -> List[Dict]:
    |                                          ^^^^
361 |         """Extract Tier-0 document references from agent contract"""
362 |         agent_file = self.repo_root / ".agent"
    |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/validate_tier0_activation.py:360:47
    |
358 |         return True
359 |     
360 |     def extract_tier0_documents(self) -> List[Dict]:
    |                                               ^^^^
361 |         """Extract Tier-0 document references from agent contract"""
362 |         agent_file = self.repo_root / ".agent"
    |
help: Replace with `dict`

UP015 [*] Unnecessary mode argument
   --> scripts/validate_tier0_activation.py:365:35
    |
364 |         try:
365 |             with open(agent_file, 'r') as f:
    |                                   ^^^
366 |                 content = f.read()
    |
help: Remove mode argument

UP006 [*] Use `list` instead of `List` for type annotation
   --> scripts/validate_tier0_activation.py:400:58
    |
398 |             return []
399 |     
400 |     def validate_tier0_documents_exist(self, tier0_docs: List[Dict]) -> bool:
    |                                                          ^^^^
401 |         """Validate that all referenced Tier-0 documents exist"""
402 |         all_exist = True
    |
help: Replace with `list`

UP006 [*] Use `dict` instead of `Dict` for type annotation
   --> scripts/validate_tier0_activation.py:400:63
    |
398 |             return []
399 |     
400 |     def validate_tier0_documents_exist(self, tier0_docs: List[Dict]) -> bool:
    |                                                               ^^^^
401 |         """Validate that all referenced Tier-0 documents exist"""
402 |         all_exist = True
    |
help: Replace with `dict`

UP015 [*] Unnecessary mode argument
   --> scripts/validate_tier0_activation.py:435:35
    |
434 |         try:
435 |             with open(agent_file, 'r') as f:
    |                                   ^^^
436 |                 content = f.read()
    |
help: Remove mode argument

UP015 [*] Unnecessary mode argument
   --> scripts/validate_tier0_activation.py:475:35
    |
474 |         try:
475 |             with open(agent_file, 'r') as f:
    |                                   ^^^
476 |                 content = f.read()
    |
help: Remove mode argument

UP015 [*] Unnecessary mode argument
   --> scripts/validate_tier0_activation.py:546:35
    |
545 |         try:
546 |             with open(agent_file, 'r') as f:
    |                                   ^^^
547 |                 content = f.read()
    |
help: Remove mode argument

UP035 `typing.Dict` is deprecated, use `dict` instead
  --> scripts/validate_tier0_consistency.py:24:1
   |
22 | import re
23 | from pathlib import Path
24 | from typing import Dict, List, Set, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
25 |
26 | class Tier0ConsistencyValidator:
   |

UP035 `typing.List` is deprecated, use `list` instead
  --> scripts/validate_tier0_consistency.py:24:1
   |
22 | import re
23 | from pathlib import Path
24 | from typing import Dict, List, Set, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
25 |
26 | class Tier0ConsistencyValidator:
   |

UP035 `typing.Set` is deprecated, use `set` instead
  --> scripts/validate_tier0_consistency.py:24:1
   |
22 | import re
23 | from pathlib import Path
24 | from typing import Dict, List, Set, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
25 |
26 | class Tier0ConsistencyValidator:
   |

UP035 `typing.Tuple` is deprecated, use `tuple` instead
  --> scripts/validate_tier0_consistency.py:24:1
   |
22 | import re
23 | from pathlib import Path
24 | from typing import Dict, List, Set, Tuple
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
25 |
26 | class Tier0ConsistencyValidator:
   |

UP006 [*] Use `tuple` instead of `Tuple` for type annotation
   --> scripts/validate_tier0_consistency.py:145:32
    |
143 |         return success
144 |         
145 |     def load_manifest(self) -> Tuple[int, Set[str]]:
    |                                ^^^^^
146 |         """Load manifest and return document count and IDs"""
147 |         if not self.manifest_path.exists():
    |
help: Replace with `tuple`

UP006 [*] Use `set` instead of `Set` for type annotation
   --> scripts/validate_tier0_consistency.py:145:43
    |
143 |         return success
144 |         
145 |     def load_manifest(self) -> Tuple[int, Set[str]]:
    |                                           ^^^
146 |         """Load manifest and return document count and IDs"""
147 |         if not self.manifest_path.exists():
    |
help: Replace with `set`

UP006 [*] Use `tuple` instead of `Tuple` for type annotation
   --> scripts/validate_tier0_consistency.py:195:44
    |
193 |             return None
194 |             
195 |     def get_agent_yaml_tier0_docs(self) -> Tuple[int, Set[str]]:
    |                                            ^^^^^
196 |         """Get Tier-0 document count and IDs from .agent file"""
197 |         if not self.agent_yaml_path.exists():
    |
help: Replace with `tuple`

UP006 [*] Use `set` instead of `Set` for type annotation
   --> scripts/validate_tier0_consistency.py:195:55
    |
193 |             return None
194 |             
195 |     def get_agent_yaml_tier0_docs(self) -> Tuple[int, Set[str]]:
    |                                                       ^^^
196 |         """Get Tier-0 document count and IDs from .agent file"""
197 |         if not self.agent_yaml_path.exists():
    |
help: Replace with `set`

Found 107 errors.
[*] 86 fixable with the `--fix` option.
```

</details>

---

#### Artifact 3: `python3 scripts/generate-prehandover-proof-template.py --help`

- **Start Time**: 2026-01-13T05:25:35Z
- **End Time**: 2026-01-13T05:25:35Z
- **Exit Code**: 0
- **Log File**: `evidence/prehandover/capture_20260113_052535/artifact_003.log`
- **Metadata**: `evidence/prehandover/capture_20260113_052535/artifact_003.meta`

<details>
<summary>View Execution Log</summary>

```
usage: generate-prehandover-proof-template.py [-h] [--agent AGENT] [--pr PR]
                                              [--branch BRANCH] [--wave WAVE]
                                              [--no-category-0] [-o OUTPUT]

Generate PREHANDOVER_PROOF template

options:
  -h, --help            show this help message and exit
  --agent AGENT         Agent name (default: Builder Name)
  --pr PR               PR number (default: PR_NUMBER)
  --branch BRANCH       Branch name (default: feature/your-branch)
  --wave WAVE           Wave identifier (default: Wave X.Y)
  --no-category-0       Mark Category 0 as N/A (for non-executable changes)
  -o OUTPUT, --output OUTPUT
                        Output file path (default:
                        PREHANDOVER_PROOF_TEMPLATE.md)

Examples:
    generate-prehandover-proof-template.py
    generate-prehandover-proof-template.py --agent "API Builder" --pr 123 --wave "Wave 3.2"
    generate-prehandover-proof-template.py --no-category-0 --output PREHANDOVER_PROOF_DOC_ONLY.md
        
```

</details>

---

#### Artifact 4: `bash .githooks/pre-push 2>&1 `

- **Start Time**: 0
- **End Time**: 2026-01-13T05:25:35Z
- **Exit Code**:  head -20
- **Log File**: `evidence/prehandover/capture_20260113_052535/artifact_004.log`
- **Metadata**: `evidence/prehandover/capture_20260113_052535/artifact_004.meta`

<details>
<summary>View Execution Log</summary>

```
[Log content not available]
```

</details>

---


**Evidence Completeness**: ⚠️ INCOMPLETE (failures detected)

---

**Note**: This document was auto-generated. Complete remaining sections:
- Fill in metadata placeholders [AGENT_NAME], [PR_NUMBER], [BRANCH_NAME], [COMMIT_SHA]
- Complete Step 1, Step 2, Step 5, Step 6, Step 7
- Add Agent Attestation section

Validate with:
```bash
python3 governance/scripts/validate_prehandover_proof.py WAVE_3.2_PREHANDOVER_PROOF.md
```

---

**END OF AUTO-GENERATED SECTION**

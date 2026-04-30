#!/usr/bin/env python3
"""
validate-ecap-ceremony.py

AMC CI Hard Gate — ECAP / Admin Ceremony Evidence Validator

Authority: PPEIA-001, EFIA-001, ECAP-001 v1.3.0
Issue:     app_management_centre#1154 — Port ISMS IAA and ECAP hard merge gates into AMC
Canon:     governance/canon/PROTECTED_PATH_ECAP_BEFORE_IAA_CANON.md
           governance/canon/EXECUTION_CEREMONY_ADMINISTRATION_PROTOCOL.md

Purpose:
  Classifies whether a PR touches protected paths. If it does, validates that
  ECAP / admin ceremony evidence is present, committed, and non-self-certified
  before the merge gate is released. Supports a narrow CS2 waiver path.

Acceptance Criteria covered: AC3, AC4, AC5, AC8

Usage:
  python3 validate-ecap-ceremony.py \\
      --pr-number    <N> \\
      --changed-files <file1> [<file2> ...] \\
      [--repo-root   <path>]

  Or pipe changed files:
      git diff --name-only origin/main...HEAD | \\
      python3 validate-ecap-ceremony.py --pr-number <N> --files-from-stdin

Exit codes:
  0  Gate PASS — not a protected-path PR, or valid ECAP evidence present / waived
  1  Gate FAIL — protected-path PR with missing, invalid, or self-certified ECAP
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Protected path patterns (PPEIA-001 §1.1)
# ---------------------------------------------------------------------------

# Each entry: (pattern_id, compiled regex, always_protected, description)
PROTECTED_PATH_PATTERNS = [
    (
        "PP-01",
        re.compile(r"^\.github/workflows/"),
        False,  # Only when affecting governance, IAA, handover, etc. — see §1.1 note
        ".github/workflows/ — CI workflow changes (governance-affecting)",
    ),
    (
        "PP-02",
        re.compile(r"^\.github/scripts/"),
        False,  # Only when affecting governance, IAA, handover, ECAP, merge gates, etc.
        ".github/scripts/ — Automation scripts (governance-affecting)",
    ),
    (
        "PP-03",
        re.compile(r"^governance/"),
        True,
        "governance/ — Governance canon changes",
    ),
    (
        "PP-04",
        re.compile(r"^\.agent-admin/"),
        True,
        ".agent-admin/ — Ceremony artifacts and templates",
    ),
    (
        "PP-05",
        re.compile(r"^\.github/agents/"),
        True,
        ".github/agents/ — Agent contract files",
    ),
    (
        "PP-06",
        re.compile(r"^(supabase/migrations/|schema/|migrations/)"),
        True,
        "Schema/migration files — runtime/data-integrity sensitive",
    ),
    (
        "PP-07",
        re.compile(r"(.*-tracker\.md|.*-index\.md|BUILD_PROGRESS_TRACKER)"),
        True,
        "Stage tracker / index / control surfaces",
    ),
    (
        "PP-08",
        re.compile(r"^\.governance-pack/"),
        True,
        ".governance-pack/ — Canon inventory, consumer registry, gate requirements",
    ),
    (
        "PP-PP",
        re.compile(r"^\.agent-workspace/.*/knowledge/"),
        True,
        ".agent-workspace/*/knowledge/ — Tier 2 knowledge (agent working knowledge)",
    ),
]

# Governance-affecting keywords for PP-01 / PP-02 (workflow / script files)
GOVERNANCE_AFFECTING_RE = re.compile(
    r"governance|iaa|handover|injector|pr[-_]comment|ecap|merge[-_]gate|"
    r"protected[-_]path|ceremony|assurance|prehandover|preflight|boundary|"
    r"polc|session[-_]memory|wave[-_]record",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# ECAP required evidence fields (AC3)
# ---------------------------------------------------------------------------

REQUIRED_ECAP_FIELDS = [
    ("protected_path_touched", re.compile(r"protected_path_touched\s*[:\s]+true", re.IGNORECASE)),
    ("ecap_required",          re.compile(r"ecap_required\s*[:\s]+true", re.IGNORECASE)),
    ("ecap_invoked",           re.compile(r"ecap_invoked\s*[:\s]+true", re.IGNORECASE)),
    ("ecap_verdict",           re.compile(r"ecap_verdict\s*[:\s]+PASS", re.IGNORECASE)),
    ("ceremony_admin_appointed", re.compile(
        r"(?:ceremony_admin_appointed\s*[:\s]+true|"
        r"execution-ceremony-admin-agent.*appointed|"
        r"ecap-session-\w+)",
        re.IGNORECASE,
    )),
    ("protected_path_ceremony_verdict", re.compile(
        r"protected_path_ceremony_verdict\s*[:\s]+PASS",
        re.IGNORECASE,
    )),
]

# Self-certification indicators (AC4) — ECAP claims without an independent committed bundle
SELF_CERT_PATTERNS = [
    re.compile(r"ecap_invoked\s*[:\s]+true", re.IGNORECASE),
    re.compile(r"ecap_verdict\s*[:\s]+PASS", re.IGNORECASE),
]

# Stale ECAP/checklist wording after IAA PASS (AC8)
STALE_ECAP_WORDING_RE = re.compile(
    r"(PENDING\s+IAA\s+INVOCATION|PHASE_B_BLOCKING_TOKEN\s*:\s*PENDING|"
    r"BLOCKED\s+pending\s+IAA|awaiting\s+IAA|ecap_verdict\s*:\s*PENDING|"
    r"protected_path_ceremony_verdict\s*:\s*PENDING|"
    r"ceremony_admin_appointed\s*:\s*PENDING)",
    re.IGNORECASE,
)

# CS2 waiver field patterns (AC5)
WAIVER_FIELD_RE = re.compile(
    r"ecap_waiver_ref\s*[:\s]+(?!N/A|none|null)(\S.+?)(?:\n|$)",
    re.IGNORECASE,
)

# ECAP reconciliation file pattern
ECAP_RECON_GLOB    = ".agent-admin/prehandover/ecap-reconciliation-*.md"
WAVE_RECORD_GLOB   = ".agent-admin/wave-records/amc-wave-record-*.md"


# ---------------------------------------------------------------------------
# Helper classes
# ---------------------------------------------------------------------------

class ProtectedPathHit:
    def __init__(self, pattern_id: str, path: str, description: str) -> None:
        self.pattern_id  = pattern_id
        self.path        = path
        self.description = description


class EcapEvidence:
    def __init__(self) -> None:
        self.source_path: str = ""
        self.fields_present: list[str] = []
        self.fields_missing: list[str] = []
        self.is_committed_bundle: bool = False
        self.waiver_ref: str = ""
        self.stale_wording: list[str] = []


class GateResult:
    def __init__(self) -> None:
        self.passed = False
        self.failures: list[str] = []
        self.warnings: list[str] = []
        self.protected_path_hits: list[ProtectedPathHit] = []
        self.evidence: EcapEvidence | None = None

    def fail(self, reason: str) -> None:
        self.failures.append(reason)

    def warn(self, reason: str) -> None:
        self.warnings.append(reason)


# ---------------------------------------------------------------------------
# Protected-path classification
# ---------------------------------------------------------------------------

def classify_protected_paths(
    changed_files: list[str],
    repo_root: Path,
) -> list[ProtectedPathHit]:
    """
    Return list of protected-path hits for the given file list.
    For PP-01/PP-02 (workflow/script), only flag if the file content
    contains governance-affecting keywords.
    """
    hits: list[ProtectedPathHit] = []
    seen_paths: set[str] = set()

    for fpath in changed_files:
        fpath = fpath.strip()
        if not fpath:
            continue

        for pat_id, pattern, always_protected, description in PROTECTED_PATH_PATTERNS:
            if pattern.search(fpath):
                # For PP-01 / PP-02: check if file is governance-affecting
                if not always_protected:
                    full_path = repo_root / fpath
                    is_governance_affecting = False
                    # Check filename first
                    if GOVERNANCE_AFFECTING_RE.search(fpath):
                        is_governance_affecting = True
                    elif full_path.exists():
                        try:
                            content = full_path.read_text(
                                encoding="utf-8", errors="replace"
                            )[:4000]
                            if GOVERNANCE_AFFECTING_RE.search(content):
                                is_governance_affecting = True
                        except OSError:
                            pass
                    if not is_governance_affecting:
                        continue

                if fpath not in seen_paths:
                    seen_paths.add(fpath)
                    hits.append(ProtectedPathHit(pat_id, fpath, description))
                break  # Use first matching pattern per file

    return hits


# ---------------------------------------------------------------------------
# ECAP evidence discovery and validation
# ---------------------------------------------------------------------------

def find_ecap_evidence(
    repo_root: Path,
    pr_number: int,
) -> EcapEvidence | None:
    """
    Find and parse the ECAP reconciliation bundle for this PR.
    Returns None if no evidence found.
    """
    # Primary: ecap-reconciliation-<PR#>.md or ecap-reconciliation-*<PR#>*.md
    candidates: list[Path] = []

    ecap_dir = repo_root / ".agent-admin" / "prehandover"
    if ecap_dir.exists():
        # Direct PR-number match first
        direct = ecap_dir / f"ecap-reconciliation-{pr_number}.md"
        if direct.exists():
            candidates.append(direct)

        # Glob for any with PR number in name or content
        for p in sorted(ecap_dir.glob("ecap-reconciliation-*.md")):
            if p not in candidates:
                try:
                    text = p.read_text(encoding="utf-8", errors="replace")
                    if re.search(rf"#?{pr_number}\b", text):
                        candidates.append(p)
                except OSError:
                    pass

    if not candidates:
        return None

    # Use the best candidate (first = most specific: ecap-reconciliation-<PR>.md)
    best_path = candidates[0]
    try:
        text = best_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    ev = EcapEvidence()
    ev.source_path = str(best_path)
    # Only files inside .agent-admin/prehandover/ are committed ECAP bundles (AC4).
    # Wave records that assert ecap_invoked/ecap_verdict are self-certification, not evidence.
    ev.is_committed_bundle = (
        ".agent-admin" in str(best_path)
        and "prehandover" in str(best_path)
    )

    # Check required fields
    for field_name, field_re in REQUIRED_ECAP_FIELDS:
        if field_re.search(text):
            ev.fields_present.append(field_name)
        else:
            ev.fields_missing.append(field_name)

    # Check for CS2 waiver
    waiver_match = WAIVER_FIELD_RE.search(text)
    if waiver_match:
        ev.waiver_ref = waiver_match.group(1).strip()

    # Stale wording
    ev.stale_wording = [
        m.group(0) for m in re.finditer(STALE_ECAP_WORDING_RE, text)
    ]

    return ev


def has_only_self_certified_ecap(
    repo_root: Path,
    pr_number: int,
) -> bool:
    """
    Returns True if the evidence surfaces only contain field assertions
    (ecap_invoked: true, ecap_verdict: PASS) WITHOUT a committed ECAP
    reconciliation bundle at the expected path.

    Anti-self-certification rule (AC4): PREHANDOVER or wave-record fields
    alone are not ECAP evidence if they merely assert ecap_invoked: true
    and ecap_verdict: PASS.
    """
    ecap_dir = repo_root / ".agent-admin" / "prehandover"

    # Look for an actual committed ECAP reconciliation file
    ecap_reconciliation_exists = False
    if ecap_dir.exists():
        for p in ecap_dir.glob("ecap-reconciliation-*.md"):
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
                if re.search(rf"#?{pr_number}\b", text):
                    ecap_reconciliation_exists = True
                    break
            except OSError:
                pass

    if ecap_reconciliation_exists:
        return False  # Has committed bundle — not self-certified

    # Check if wave records only assert (not evidence)
    wave_dir = repo_root / ".agent-admin" / "wave-records"
    wave_has_assertion = False
    if wave_dir.exists():
        for p in wave_dir.glob("amc-wave-record-*.md"):
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
                if re.search(rf"#?{pr_number}\b", text):
                    self_cert_count = sum(
                        1 for re_ in SELF_CERT_PATTERNS if re_.search(text)
                    )
                    if self_cert_count >= 1:
                        wave_has_assertion = True
            except OSError:
                pass

    # Self-certified: wave record asserts ECAP PASS but no committed reconciliation bundle
    return wave_has_assertion


# ---------------------------------------------------------------------------
# Gate validation logic
# ---------------------------------------------------------------------------

def run_ecap_gate(
    pr_number: int,
    changed_files: list[str],
    repo_root: Path,
) -> GateResult:
    """
    Run the ECAP ceremony hard gate.
    """
    result = GateResult()

    # -----------------------------------------------------------------------
    # Step 1: Classify protected paths
    # -----------------------------------------------------------------------
    hits = classify_protected_paths(changed_files, repo_root)
    result.protected_path_hits = hits

    if not hits:
        # Not a protected-path PR — gate PASS
        print("ℹ️  No protected paths detected in changed files.")
        print("   ECAP ceremony gate does not apply to this PR.")
        result.passed = True
        return result

    print(f"🔒 Protected paths detected ({len(hits)} path(s)):")
    for h in hits:
        print(f"   [{h.pattern_id}] {h.path}")
    print()

    # -----------------------------------------------------------------------
    # Step 2: Look for ECAP evidence
    # -----------------------------------------------------------------------
    ev = find_ecap_evidence(repo_root, pr_number)
    result.evidence = ev

    if ev is None:
        # No ECAP reconciliation bundle found — check for CS2 waiver first (AC5)
        waiver_found = _find_cs2_waiver(repo_root, pr_number)
        if waiver_found:
            print(f"✅ CS2 waiver found: {waiver_found}")
            result.passed = True
            return result

        # Distinguish AC4 self-certification from AC3 missing evidence (AC4)
        if has_only_self_certified_ecap(repo_root, pr_number):
            result.fail(
                f"AC4-SELF-CERTIFIED: PR #{pr_number} touches protected paths "
                f"({', '.join(h.path for h in hits[:3])}) but has only wave-record "
                f"ECAP field assertions (ecap_invoked: true / ecap_verdict: PASS) "
                f"without an independent committed ECAP reconciliation bundle. "
                f"Wave-record assertions alone are self-certification — blocked per AC4. "
                f"Commit .agent-admin/prehandover/ecap-reconciliation-{pr_number}.md."
            )
        else:
            result.fail(
                f"AC3-ECAP-MISSING: PR #{pr_number} touches protected paths "
                f"({', '.join(h.path for h in hits[:3])}) but no ECAP ceremony evidence "
                f"found at .agent-admin/prehandover/ecap-reconciliation-*.md. "
                f"Protected-path PRs MUST have a committed ECAP bundle before merge."
            )
        return result

    # -----------------------------------------------------------------------
    # Step 3: Anti-self-certification check (AC4)
    # -----------------------------------------------------------------------
    if not ev.is_committed_bundle:
        result.fail(
            f"AC4-SELF-CERTIFIED: ECAP fields found in evidence surfaces but no "
            f"independent committed ECAP reconciliation bundle exists at "
            f".agent-admin/prehandover/ecap-reconciliation-*.md. "
            f"Asserting 'ecap_invoked: true' in a wave record without a committed "
            f"ECAP bundle is self-certification — blocked per AC4."
        )
        return result

    # -----------------------------------------------------------------------
    # Step 4: Validate required fields (AC3)
    # -----------------------------------------------------------------------
    if ev.fields_missing:
        # Check if there's a valid CS2 waiver covering the missing fields (AC5)
        waiver = _find_cs2_waiver(repo_root, pr_number)
        if waiver:
            print(f"✅ CS2 waiver covers missing ECAP fields: {waiver}")
        else:
            result.fail(
                f"AC3-ECAP-FIELDS-MISSING: ECAP evidence ({ev.source_path}) is missing "
                f"required fields: {ev.fields_missing}. All of these must be present: "
                f"protected_path_touched=true, ecap_required=true, ecap_invoked=true, "
                f"ecap_verdict=PASS, ceremony_admin_appointed=true, "
                f"protected_path_ceremony_verdict=PASS."
            )

    # -----------------------------------------------------------------------
    # Step 5: Check for N/A on required fields (AC3 failure condition)
    # -----------------------------------------------------------------------
    if ev.source_path:
        try:
            ev_text = Path(ev.source_path).read_text(encoding="utf-8", errors="replace")
        except OSError:
            ev_text = ""

        na_patterns = [
            (re.compile(r"ecap_required\s*[:\s]+N/A", re.IGNORECASE), "ecap_required: N/A"),
            (re.compile(r"ecap_invoked\s*[:\s]+N/A", re.IGNORECASE), "ecap_invoked: N/A"),
        ]
        for na_re, label in na_patterns:
            if na_re.search(ev_text):
                result.fail(
                    f"AC3-ECAP-FIELD-NA: '{label}' found in ECAP evidence "
                    f"({ev.source_path}) for a protected-path PR. "
                    f"These fields cannot be N/A when protected paths are touched."
                )

    # -----------------------------------------------------------------------
    # Step 6: Stale wording check (AC8)
    # -----------------------------------------------------------------------
    if ev.stale_wording:
        result.fail(
            f"AC8-STALE-WORDING: ECAP evidence ({ev.source_path}) retains stale "
            f"pre-IAA wording after ceremony: {ev.stale_wording[:3]}. "
            f"Final-state normalization is required after ECAP PASS."
        )

    # -----------------------------------------------------------------------
    # Determine final verdict
    # -----------------------------------------------------------------------
    if not result.failures:
        result.passed = True

    return result


def _find_cs2_waiver(repo_root: Path, pr_number: int) -> str:
    """
    Look for a CS2 waiver covering this PR. Returns waiver ref string if found,
    empty string otherwise.

    Per AC5: waiver must be explicit, identify the PR, and be recorded in a
    machine-readable field.
    """
    # Search wave records and ECAP reconciliation for waiver fields
    search_paths: list[Path] = []

    for glob in [
        ".agent-admin/prehandover/ecap-reconciliation-*.md",
        ".agent-admin/wave-records/amc-wave-record-*.md",
    ]:
        search_paths.extend(sorted(repo_root.glob(glob)))

    for path in search_paths:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        if not re.search(rf"#?{pr_number}\b", text):
            continue

        waiver_match = WAIVER_FIELD_RE.search(text)
        if waiver_match:
            ref = waiver_match.group(1).strip()
            if ref and ref.upper() not in ("N/A", "NONE", "NULL", "FALSE", "NO"):
                return ref

    return ""


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def _build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="AMC ECAP Ceremony Hard Gate",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--pr-number", type=int, required=True,
        help="GitHub PR number being validated",
    )
    p.add_argument(
        "--changed-files", nargs="*", default=[],
        help="Space-separated list of changed files (relative to repo root)",
    )
    p.add_argument(
        "--files-from-stdin", action="store_true",
        help="Read changed files from stdin (one per line)",
    )
    p.add_argument(
        "--repo-root", type=str, default=".",
        help="Path to repository root (default: current directory)",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    parser = _build_arg_parser()
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()

    changed_files: list[str] = list(args.changed_files)
    if args.files_from_stdin:
        changed_files.extend(line.strip() for line in sys.stdin if line.strip())

    print("=" * 70)
    print("AMC ECAP CEREMONY HARD GATE")
    print("Authority: PPEIA-001, ECAP-001 v1.3.0 | Issue: #1154")
    print("=" * 70)
    print(f"PR:           #{args.pr_number}")
    print(f"Changed files: {len(changed_files)}")
    print(f"Repo Root:    {repo_root}")
    print()

    result = run_ecap_gate(
        pr_number=args.pr_number,
        changed_files=changed_files,
        repo_root=repo_root,
    )

    # Print warnings
    for w in result.warnings:
        print(f"⚠️  WARNING: {w}")

    # Print failures
    for f in result.failures:
        print(f"❌ FAIL: {f}")

    print()
    if result.passed:
        if result.protected_path_hits:
            print("✅ ECAP CEREMONY GATE: PASS (protected paths with valid ECAP evidence)")
        else:
            print("✅ ECAP CEREMONY GATE: PASS (no protected paths touched)")
        return 0
    else:
        print(f"❌ ECAP CEREMONY GATE: FAIL ({len(result.failures)} failure(s))")
        return 1


if __name__ == "__main__":
    sys.exit(main())

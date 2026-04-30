#!/usr/bin/env python3
"""
validate-iaa-final-assurance.py

AMC CI Hard Gate — IAA Final Assurance Evidence Validator

Authority: PPEIA-001, EFIA-001, AAEV-001, WRCC-001
Issue:     app_management_centre#1154 — Port ISMS IAA and ECAP hard merge gates into AMC
Canon:     governance/canon/AMC_EVIDENCE_FIRST_IAA_ASSURANCE_CANON.md
           governance/canon/AMC_AUTHORITY_EXACTNESS_VALIDATORS.md

Purpose:
  Validates that a PR has current, PR-specific, issue-specific, and SHA-specific
  IAA final assurance evidence before it may be merged.  Fails the CI gate when
  any required field is missing, malformed, or stale.

Acceptance Criteria covered: AC1, AC2, AC6, AC7, AC8

Usage:
  python3 validate-iaa-final-assurance.py \\
      --pr-number <N> \\
      --head-sha   <full-sha> \\
      [--governing-issue <N>] \\
      [--repo-root  <path>]

Exit codes:
  0  Gate PASS — valid, current IAA assurance evidence found
  1  Gate FAIL — evidence missing, malformed, stale, or mislinked
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Token format patterns (AC6)
# ---------------------------------------------------------------------------

# Canonical format: IAA-session-NNN-YYYYMMDD-PASS  (or multi-segment session IDs)
CANONICAL_TOKEN_RE = re.compile(
    r"IAA-session-[A-Za-z0-9_-]+-\d{8}-PASS"
)

# Deprecated format: IAA-NNN-YYYYMMDD-PASS  (rejected per AC6)
DEPRECATED_TOKEN_RE = re.compile(
    r"IAA-\d+-\d{8}-PASS"
)

# PHASE_B_BLOCKING_TOKEN field line
PHASE_B_LINE_RE = re.compile(
    r"PHASE_B_BLOCKING_TOKEN\s*:\s*(IAA-[A-Za-z0-9_-]+-\d{8}-PASS)",
    re.IGNORECASE,
)

# PR reference in evidence: "PR: #NNN" or "**PR**: #NNN" (markdown bold)
PR_FIELD_RE = re.compile(
    r"^\s*\*{0,2}PR\*{0,2}\s*:\s*#(\d+)",
    re.MULTILINE,
)

# Also: "pr_reviewed: PR #NNN" or "PR #NNN —" in IAA memory prose
PR_PROSE_RE = re.compile(
    r"(?:pr_reviewed|PR\s+#)(\d{3,6})\b",
    re.MULTILINE | re.IGNORECASE,
)

# Issue reference in evidence: "Issue: #NNN" or "governing_issue: #NNN" etc.
ISSUE_FIELD_RE = re.compile(
    r"(?:Issue|governing_issue|governing_delivery_issue|triggering_issue)\s*:\s*[#\s]*(\d+)",
    re.MULTILINE | re.IGNORECASE,
)

# Reviewed SHA field: "Reviewed SHA: <sha>", "head_commit_at_review: <sha>",
# or embedded "HEAD <sha>" / "corrective commit <sha>" (7-40 hex chars)
REVIEWED_SHA_RE = re.compile(
    r"(?:Reviewed\s+SHA|head_commit_at_review|head_sha|HEAD)\s*[:\s]+([0-9a-f]{7,40})\b",
    re.MULTILINE | re.IGNORECASE,
)

# Verdict field: "Verdict: PASS"
VERDICT_RE = re.compile(
    r"(?:Verdict|verdict|adoption_phase)\s*:\s*(?:ASSURANCE-TOKEN|PASS|PHASE_B_BLOCKING)",
    re.MULTILINE | re.IGNORECASE,
)

# Stale wording patterns (AC8) — evidence surfaces must not retain these after token issuance
STALE_WORDING_PATTERNS = [
    r"PENDING\s+IAA\s+INVOCATION",
    r"PHASE_B_BLOCKING_TOKEN\s*:\s*PENDING",
    r"BLOCKED\s+pending\s+IAA",
    r"awaiting\s+IAA",
    r"IAA\s+not\s+yet\s+invoked",
    r"assurance.*pending",
    r"ASSURANCE_PENDING",
]
STALE_WORDING_RE = re.compile(
    "|".join(STALE_WORDING_PATTERNS),
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# Delta-assurance block patterns (AC7)
# ---------------------------------------------------------------------------

# delta_assurance_verdict: PASS
DELTA_ASSURANCE_VERDICT_RE = re.compile(
    r"delta_assurance_verdict\s*[:\s]+PASS",
    re.IGNORECASE,
)

# final_head: <sha>  — the PR head SHA this delta assurance binds to
DELTA_FINAL_HEAD_RE = re.compile(
    r"final_head\s*[:\s]+([0-9a-f]{7,40})\b",
    re.IGNORECASE,
)

# delta_classification: token-recording-only | substantive | …
DELTA_CLASSIFICATION_RE = re.compile(
    r"delta_classification\s*[:\s]+([\w-]+)",
    re.IGNORECASE,
)

# base_head: <sha>  — the SHA that was originally reviewed by IAA
DELTA_BASE_HEAD_RE = re.compile(
    r"base_head\s*[:\s]+([0-9a-f]{7,40})\b",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# Evidence path patterns (AC1)
# ---------------------------------------------------------------------------

WAVE_RECORD_GLOB = ".agent-admin/wave-records/amc-wave-record-*.md"
IAA_MEMORY_GLOB  = ".agent-workspace/independent-assurance-agent/memory/*.md"
IAA_TOKEN_GLOB   = ".agent-admin/assurance/iaa-token-*.md"
ECAP_RECON_GLOB  = ".agent-admin/prehandover/ecap-reconciliation-*.md"


# ---------------------------------------------------------------------------
# Helper classes
# ---------------------------------------------------------------------------

class AssuranceEvidence:
    """Holds parsed IAA assurance evidence fields."""

    def __init__(self) -> None:
        self.source_path: str = ""
        self.token: str = ""
        self.pr_number: Optional[int] = None
        self.issue_number: Optional[int] = None
        self.reviewed_sha: str = ""
        self.verdict_present: bool = False
        self.phase_b_token_present: bool = False
        self.stale_wording: list[str] = []
        self.raw_text: str = ""
        # Delta-assurance block (AC7)
        self.delta_assurance_verdict: str = ""   # "PASS" when delta_assurance_verdict: PASS
        self.delta_final_head: str = ""           # final_head field SHA
        self.delta_classification: str = ""       # e.g. "token-recording-only" or "substantive"
        self.delta_base_head: str = ""            # base_head field SHA


class GateResult:
    """Gate PASS/FAIL result with diagnostic messages."""

    def __init__(self) -> None:
        self.passed = False
        self.failures: list[str] = []
        self.warnings: list[str] = []
        self.evidence: Optional[AssuranceEvidence] = None

    def fail(self, reason: str) -> None:
        self.failures.append(reason)

    def warn(self, reason: str) -> None:
        self.warnings.append(reason)


# ---------------------------------------------------------------------------
# Core parsing
# ---------------------------------------------------------------------------

def _extract_evidence_from_text(text: str, source_path: str) -> AssuranceEvidence:
    ev = AssuranceEvidence()
    ev.raw_text = text
    ev.source_path = source_path

    # Find PHASE_B_BLOCKING_TOKEN line (primary token surface)
    pb_match = PHASE_B_LINE_RE.search(text)
    if pb_match:
        ev.token = pb_match.group(1)
        ev.phase_b_token_present = True
    else:
        # Fall back to bare canonical token in prose
        tok_match = CANONICAL_TOKEN_RE.search(text)
        if tok_match:
            ev.token = tok_match.group(0)

    # PR number
    pr_match = PR_FIELD_RE.search(text)
    if pr_match:
        try:
            ev.pr_number = int(pr_match.group(1))
        except ValueError:
            pass
    # Fallback: prose "pr_reviewed: PR #NNN"
    if ev.pr_number is None:
        prose_match = PR_PROSE_RE.search(text)
        if prose_match:
            try:
                ev.pr_number = int(prose_match.group(1))
            except ValueError:
                pass

    # Issue number (take first match)
    iss_match = ISSUE_FIELD_RE.search(text)
    if iss_match:
        try:
            ev.issue_number = int(iss_match.group(1))
        except ValueError:
            pass

    # Reviewed SHA
    sha_match = REVIEWED_SHA_RE.search(text)
    if sha_match:
        ev.reviewed_sha = sha_match.group(1).strip()

    # Verdict
    ev.verdict_present = bool(VERDICT_RE.search(text))

    # Stale wording
    ev.stale_wording = [
        m.group(0)
        for m in re.finditer(STALE_WORDING_RE, text)
    ]

    # Delta-assurance block (AC7)
    if DELTA_ASSURANCE_VERDICT_RE.search(text):
        ev.delta_assurance_verdict = "PASS"
    da_final = DELTA_FINAL_HEAD_RE.search(text)
    if da_final:
        ev.delta_final_head = da_final.group(1).strip()
    da_class = DELTA_CLASSIFICATION_RE.search(text)
    if da_class:
        ev.delta_classification = da_class.group(1).strip()
    da_base = DELTA_BASE_HEAD_RE.search(text)
    if da_base:
        ev.delta_base_head = da_base.group(1).strip()

    return ev


def _file_has_any_token(text: str) -> bool:
    """Return True if the file contains ANY IAA token (canonical or deprecated)."""
    return bool(CANONICAL_TOKEN_RE.search(text) or PHASE_B_LINE_RE.search(text))


def _is_deprecated_token(token: str) -> bool:
    """Return True if token matches deprecated (non-canonical) format."""
    return bool(DEPRECATED_TOKEN_RE.match(token)) and not bool(
        CANONICAL_TOKEN_RE.match(token)
    )


# ---------------------------------------------------------------------------
# Evidence discovery
# ---------------------------------------------------------------------------

def find_all_evidence_files(
    repo_root: Path,
    pr_number: int,
) -> list[Path]:
    """
    Return all candidate evidence files, ordered by precedence:
    1. Wave records (canonical carrier per AMC 90/10 Protocol)
    2. IAA memory files (IAA's own session records)
    3. IAA token files (deprecated but still accepted)
    4. ECAP reconciliation (cross-reference only)
    """
    candidates: list[Path] = []

    for glob in [WAVE_RECORD_GLOB, IAA_MEMORY_GLOB, IAA_TOKEN_GLOB, ECAP_RECON_GLOB]:
        candidates.extend(sorted(repo_root.glob(glob)))

    return candidates


def find_pr_specific_evidence(
    repo_root: Path,
    pr_number: int,
) -> list[AssuranceEvidence]:
    """
    Find all evidence files that contain a reference to this PR number,
    parse them, and return only those that have a valid token.
    """
    results: list[AssuranceEvidence] = []
    all_files = find_all_evidence_files(repo_root, pr_number)

    pr_pattern = re.compile(
        rf"(?:PR\s*[:#]\s*#?{pr_number}|#?{pr_number}\b.*PR|"
        rf"pr_number.*{pr_number}|pull_request.*{pr_number}|"
        rf"{pr_number}.*handover|handover.*{pr_number})",
        re.IGNORECASE,
    )

    for path in all_files:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        # Require explicit PR reference — files that have a token but no PR linkage
        # could be historical wave records for other PRs and must not be selected.
        has_pr_ref = bool(pr_pattern.search(text))
        if not has_pr_ref:
            continue

        ev = _extract_evidence_from_text(text, str(path))
        if ev.token:
            results.append(ev)

    return results


# ---------------------------------------------------------------------------
# Gate validation logic
# ---------------------------------------------------------------------------

def _sha_prefix_match(sha_a: str, sha_b: str) -> bool:
    """Two SHAs match if either is a prefix of the other (handles short/long comparison)."""
    a = sha_a.strip().lower()
    b = sha_b.strip().lower()
    if not a or not b:
        return False
    short = min(len(a), len(b))
    if short < 7:
        return False
    return a[:short] == b[:short]


def run_iaa_gate(
    pr_number: int,
    head_sha: str,
    governing_issue: Optional[int],
    repo_root: Path,
) -> GateResult:
    """
    Run the IAA final assurance hard gate.

    Returns GateResult with .passed=True on PASS, or failures list on FAIL.
    """
    result = GateResult()

    # -----------------------------------------------------------------------
    # Step 1: Find evidence files
    # -----------------------------------------------------------------------
    evidences = find_pr_specific_evidence(repo_root, pr_number)

    if not evidences:
        result.fail(
            f"AC1-MISSING-TOKEN: No IAA assurance evidence found for PR #{pr_number}. "
            f"Expected PHASE_B_BLOCKING_TOKEN in wave record "
            f"(.agent-admin/wave-records/amc-wave-record-*.md) or IAA memory "
            f"(.agent-workspace/independent-assurance-agent/memory/*.md)."
        )
        return result

    # Select the best evidence: prefer (1) PR match, (2) issue match, (3) SHA match, (4) PHASE_B token
    def _score_evidence(ev: AssuranceEvidence) -> tuple[int, int, int, int]:
        pr_match    = 1 if ev.pr_number == pr_number else 0
        issue_match = 1 if (governing_issue and ev.issue_number == governing_issue) else 0
        sha_match   = 1 if _sha_prefix_match(ev.reviewed_sha, head_sha) else 0
        has_pb_tok  = 1 if ev.phase_b_token_present else 0
        return (pr_match, issue_match, sha_match, has_pb_tok)

    best_ev: AssuranceEvidence = max(evidences, key=_score_evidence)
    result.evidence = best_ev

    # -----------------------------------------------------------------------
    # Step 2: Token format validation (AC6)
    # -----------------------------------------------------------------------
    token = best_ev.token

    if not token:
        result.fail(
            f"AC1-MISSING-TOKEN: Evidence file found ({best_ev.source_path}) but no "
            f"IAA token extracted. PHASE_B_BLOCKING_TOKEN field must be present."
        )
        return result

    if _is_deprecated_token(token):
        result.fail(
            f"AC6-DEPRECATED-FORMAT: Token '{token}' matches deprecated format "
            f"'IAA-NNN-YYYYMMDD-PASS'. Canonical format required: "
            f"'IAA-session-NNN-YYYYMMDD-PASS'. Source: {best_ev.source_path}"
        )

    if not CANONICAL_TOKEN_RE.match(token):
        result.fail(
            f"AC6-INVALID-FORMAT: Token '{token}' does not match canonical format "
            f"'IAA-session-NNN-YYYYMMDD-PASS'. Source: {best_ev.source_path}"
        )

    # -----------------------------------------------------------------------
    # Step 3: Verdict must be explicit PASS (AC1)
    # -----------------------------------------------------------------------
    if not best_ev.verdict_present:
        result.fail(
            f"AC1-VERDICT-ABSENT: Evidence ({best_ev.source_path}) has token '{token}' "
            f"but no explicit 'Verdict: PASS' or 'PHASE_B_BLOCKING' adoption-phase field."
        )

    # -----------------------------------------------------------------------
    # Step 4: PR linkage (AC1)
    # -----------------------------------------------------------------------
    if best_ev.pr_number is None:
        result.fail(
            f"AC1-PR-NOT-LINKED: Evidence ({best_ev.source_path}) does not contain "
            f"'PR: #{pr_number}' linkage field."
        )
    elif best_ev.pr_number != pr_number:
        result.fail(
            f"AC1-WRONG-PR: Token references PR #{best_ev.pr_number} but this gate "
            f"is running for PR #{pr_number}. Token must be PR-specific."
        )

    # -----------------------------------------------------------------------
    # Step 5: Governing issue linkage (AC1, AC2)
    # -----------------------------------------------------------------------
    if governing_issue is not None:
        if best_ev.issue_number is None:
            result.fail(
                f"AC1-ISSUE-NOT-LINKED: Evidence ({best_ev.source_path}) does not "
                f"contain governing issue reference (#). "
                f"Expected: #{governing_issue}."
            )
        elif best_ev.issue_number != governing_issue:
            result.fail(
                f"AC2-WRONG-ISSUE: Token evidence references issue #{best_ev.issue_number} "
                f"but governing issue for this PR is #{governing_issue}."
            )
    else:
    if governing_issue is None:
        result.fail(
            "AC2-GOVERNING-ISSUE-REQUIRED: No governing issue provided to gate; "
            "issue linkage cannot be independently verified. Supply --governing-issue "
            "and ensure the evidence contains an exact matching issue reference."
        )
    elif best_ev.issue_number is None:
        result.fail(
            f"AC1-ISSUE-NOT-LINKED: Evidence ({best_ev.source_path}) does not "
            f"contain governing issue reference (#)."
        )
    elif best_ev.issue_number != governing_issue:
        result.fail(
            f"AC2-WRONG-ISSUE: Token evidence references issue #{best_ev.issue_number} "
            f"but governing issue for this PR is #{governing_issue}."
        )

    # -----------------------------------------------------------------------
    # Step 6: Reviewed SHA (AC1, AC7)
    # -----------------------------------------------------------------------
    if not best_ev.reviewed_sha:
        result.fail(
            f"AC1-SHA-MISSING: Evidence ({best_ev.source_path}) has no 'Reviewed SHA' "
            f"field. The IAA token must be bound to the exact head SHA reviewed."
        )
    else:
        if not _sha_prefix_match(best_ev.reviewed_sha, head_sha):
            # AC7: SHA mismatch — check for a valid machine-readable delta-assurance block
            if best_ev.delta_assurance_verdict.upper() == "PASS":
                if not best_ev.delta_final_head:
                    result.fail(
                        f"AC7-DELTA-MISSING-FINAL-HEAD: Delta assurance verdict is PASS "
                        f"({best_ev.source_path}) but no 'final_head' SHA is recorded. "
                        f"The delta_assurance block must include 'final_head: <sha>' "
                        f"binding the token to the current PR head."
                    )
                elif not _sha_prefix_match(best_ev.delta_final_head, head_sha):
                    result.fail(
                        f"AC7-DELTA-FINAL-HEAD-MISMATCH: Delta assurance final_head "
                        f"'{best_ev.delta_final_head}' does not match current PR head "
                        f"'{head_sha}'. Delta assurance must bind to the current head SHA."
                    )
                elif best_ev.delta_classification.lower() == "substantive":
                    result.fail(
                        f"AC7-SUBSTANTIVE-DELTA: Delta assurance classification is "
                        f"'substantive' ({best_ev.source_path}). A substantive change "
                        f"after IAA review requires a full IAA re-run — delta assurance "
                        f"is only valid for non-substantive (e.g. token-recording-only) "
                        f"changes between the reviewed SHA and the current head."
                    )
                # else: valid non-substantive delta with matching final_head — AC7 satisfied
            else:
                result.fail(
                    f"AC7-STALE-SHA: Evidence ({best_ev.source_path}) records "
                    f"'Reviewed SHA: {best_ev.reviewed_sha}' but current PR head is "
                    f"'{head_sha}'. IAA must be re-run on the current head, or a "
                    f"machine-readable delta assurance block must be present "
                    f"(delta_assurance_verdict: PASS, final_head: <current-sha>)."
                )

    # -----------------------------------------------------------------------
    # Step 7: Stale wording (AC8)
    # -----------------------------------------------------------------------
    if best_ev.stale_wording:
        result.fail(
            f"AC8-STALE-WORDING: Evidence ({best_ev.source_path}) retains stale "
            f"pre-IAA wording after token issuance: "
            f"{best_ev.stale_wording[:3]}. All evidence surfaces must be "
            f"final-state normalized after IAA PASS."
        )

    # -----------------------------------------------------------------------
    # Step 8: PHASE_B_BLOCKING_TOKEN must be in wave record (AC2)
    # -----------------------------------------------------------------------
    wave_record_dir = repo_root / ".agent-admin" / "wave-records"
    if wave_record_dir.exists():
        wave_records = sorted(wave_record_dir.glob("amc-wave-record-*.md"))
        wave_record_has_token = False
        for wr_path in wave_records:
            try:
                wr_text = wr_path.read_text(encoding="utf-8", errors="replace")
                if token and token in wr_text:
                    wave_record_has_token = True
                    break
                # Also check if this wave record has ANY PHASE_B token referencing this PR
                if str(pr_number) in wr_text and PHASE_B_LINE_RE.search(wr_text):
                    wave_record_has_token = True
                    break
            except OSError:
                continue
        if not wave_record_has_token and not (
            best_ev.source_path.endswith(".md") and
            "wave-record" in best_ev.source_path
        ):
            result.fail(
                f"AC2-TOKEN-NOT-IN-WAVE-RECORD: Token '{token}' not found in any "
                f"wave record under {wave_record_dir}. Per AMC 90/10 Protocol, "
                f"PHASE_B_BLOCKING_TOKEN must be recorded in wave record Section 5 "
                f"before this gate may PASS."
            )

    # -----------------------------------------------------------------------
    # Determine final verdict
    # -----------------------------------------------------------------------
    if not result.failures:
        result.passed = True

    return result


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def _build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="AMC IAA Final Assurance Hard Gate",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--pr-number", type=int, required=True,
        help="GitHub PR number being validated",
    )
    p.add_argument(
        "--head-sha", type=str, required=True,
        help="Full SHA of the current PR head commit",
    )
    p.add_argument(
        "--governing-issue", type=int, default=None,
        help="Governing issue number (optional but recommended for full AC1/AC2 check)",
    )
    p.add_argument(
        "--repo-root", type=str, default=".",
        help="Path to repository root (default: current directory)",
    )
    return p


def main(argv: Optional[list[str]] = None) -> int:
    parser = _build_arg_parser()
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()

    print("=" * 70)
    print("AMC IAA FINAL ASSURANCE HARD GATE")
    print("Authority: PPEIA-001, EFIA-001, AAEV-001 | Issue: #1154")
    print("=" * 70)
    print(f"PR:              #{args.pr_number}")
    print(f"Head SHA:        {args.head_sha}")
    print(f"Governing Issue: {'#' + str(args.governing_issue) if args.governing_issue else 'not provided'}")
    print(f"Repo Root:       {repo_root}")
    print()

    result = run_iaa_gate(
        pr_number=args.pr_number,
        head_sha=args.head_sha,
        governing_issue=args.governing_issue,
        repo_root=repo_root,
    )

    # Print warnings
    for w in result.warnings:
        print(f"⚠️  WARNING: {w}")

    # Print failures
    for f in result.failures:
        print(f"❌ FAIL: {f}")

    if result.evidence:
        print()
        print(f"Evidence source: {result.evidence.source_path}")
        if result.evidence.token:
            print(f"Token:           {result.evidence.token}")

    print()
    if result.passed:
        print("✅ IAA FINAL ASSURANCE GATE: PASS")
        return 0
    else:
        print(f"❌ IAA FINAL ASSURANCE GATE: FAIL ({len(result.failures)} failure(s))")
        return 1


if __name__ == "__main__":
    sys.exit(main())

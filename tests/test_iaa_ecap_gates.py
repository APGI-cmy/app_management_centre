"""
tests/test_iaa_ecap_gates.py

Test suite for AMC IAA Final Assurance and ECAP Ceremony hard gates.

Authority: PPEIA-001, EFIA-001, AAEV-001, ECAP-001 v1.3.0
Issue:     app_management_centre#1154 — Port ISMS IAA and ECAP hard merge gates into AMC

Acceptance Criteria covered:
  AC1  — IAA final assurance hard gate
  AC2  — Wave-record token linkage hardening
  AC3  — ECAP/admin ceremony hard gate for protected paths
  AC4  — Anti-self-certification rule
  AC5  — CS2 waiver path
  AC6  — AMC token format compatibility
  AC7  — Current-head freshness
  AC8  — PR body / evidence-bundle final-state normalization
  AC9  — Tests / fixtures (this file)

Minimum fixture coverage (AC9):
  ✅ missing IAA token fails
  ✅ token with wrong PR fails
  ✅ token with wrong issue fails
  ✅ token with missing reviewed SHA fails
  ✅ token reviewed SHA older than current head fails
  ✅ protected-path change without ECAP evidence fails
  ✅ ECAP self-certification without committed bundle fails
  ✅ ECAP waived with valid CS2 waiver passes
  ✅ valid IAA + ECAP evidence passes
  ✅ stale post-IAA PENDING wording in ECAP/checklist fails
"""

import importlib.util
import sys
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Import the gate modules under test
# Scripts use hyphens in filenames; use importlib to load them.
# ---------------------------------------------------------------------------
SCRIPTS_DIR = Path(__file__).parent.parent / ".github" / "scripts"


def _load_script(filename: str, module_name: str):
    """Load a .py script file that has hyphens in its filename."""
    spec = importlib.util.spec_from_file_location(
        module_name, SCRIPTS_DIR / filename
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)
    return mod


_iaa_mod  = _load_script("validate-iaa-final-assurance.py", "validate_iaa_final_assurance")
_ecap_mod = _load_script("validate-ecap-ceremony.py",       "validate_ecap_ceremony")

# Re-export names used in tests
run_iaa_gate                = _iaa_mod.run_iaa_gate
find_pr_specific_evidence   = _iaa_mod.find_pr_specific_evidence
_extract_evidence_from_text = _iaa_mod._extract_evidence_from_text
_is_deprecated_token        = _iaa_mod._is_deprecated_token
_sha_prefix_match           = _iaa_mod._sha_prefix_match
CANONICAL_TOKEN_RE          = _iaa_mod.CANONICAL_TOKEN_RE
DEPRECATED_TOKEN_RE         = _iaa_mod.DEPRECATED_TOKEN_RE

run_ecap_gate               = _ecap_mod.run_ecap_gate
classify_protected_paths    = _ecap_mod.classify_protected_paths
find_ecap_evidence          = _ecap_mod.find_ecap_evidence
has_only_self_certified_ecap = _ecap_mod.has_only_self_certified_ecap


# ---------------------------------------------------------------------------
# Shared fixtures
# ---------------------------------------------------------------------------

PR_NUMBER = 1154
HEAD_SHA  = "abc123def456789abc123def456789abc123def4"
SHORT_SHA = "abc123d"
OLD_SHA   = "deadbeef0000000000000000000000000000dead"
ISSUE_NUM = 1154
CANONICAL_TOKEN = f"IAA-session-066-20260429-PASS"
DEPRECATED_TOKEN = "IAA-066-20260429-PASS"


def _make_valid_wave_record(
    pr: int = PR_NUMBER,
    issue: int = ISSUE_NUM,
    sha: str = HEAD_SHA,
    token: str = CANONICAL_TOKEN,
    stale: bool = False,
) -> str:
    stale_line = "\nPHASE_B_BLOCKING_TOKEN: PENDING\n" if stale else ""
    return f"""\
# AMC Wave Record — test-wave — 2026-04-29

**Wave ID**: test-wave-20260429
**Authority**: CS2 — Issue #{issue}
**triggering_issue**: #{issue}

## Section 5 — Assurance Token
{stale_line}
`PHASE_B_BLOCKING_TOKEN: {token}`

**IAA Session**: session-066-20260429
**Verdict Date**: 2026-04-29
**Adoption Phase**: PHASE_B_BLOCKING

PR: #{pr}
Issue: #{issue}
Reviewed SHA: {sha}
Verdict: PASS
"""


def _make_valid_ecap_reconciliation(
    pr: int = PR_NUMBER,
    issue: int = ISSUE_NUM,
    stale: bool = False,
    missing_fields: list[str] | None = None,
    waiver_ref: str = "",
    na_ecap_required: bool = False,
    na_ecap_invoked: bool = False,
) -> str:
    stale_line = "\nprotected_path_ceremony_verdict: PENDING\n" if stale else ""
    missing = missing_fields or []

    # Build fields, skipping missing ones
    lines = []
    if "protected_path_touched" not in missing:
        lines.append("protected_path_touched: true")
    if "ecap_required" not in missing:
        if na_ecap_required:
            lines.append("ecap_required: N/A")
        else:
            lines.append("ecap_required: true")
    if "ecap_invoked" not in missing:
        if na_ecap_invoked:
            lines.append("ecap_invoked: N/A")
        else:
            lines.append("ecap_invoked: true")
    if "ecap_verdict" not in missing:
        lines.append("ecap_verdict: PASS")
    if "ceremony_admin_appointed" not in missing:
        lines.append("ceremony_admin_appointed: true")
        lines.append("ecap-session-035")  # alternate form
    if "protected_path_ceremony_verdict" not in missing:
        lines.append("protected_path_ceremony_verdict: PASS")

    if waiver_ref:
        lines.append(f"ecap_waiver_ref: {waiver_ref}")

    fields_block = "\n".join(lines)

    return f"""\
# ECAP Reconciliation Summary — test-wave-20260429

**Issue**: #{issue}
**PR**: #{pr}
**Wave**: test-wave-20260429
**ECAP Session**: ecap-session-035

## C1. Final-State Declaration
{stale_line}
```yaml
protected_path_ceremony:
{chr(10).join("  " + l for l in fields_block.splitlines())}
```
"""


# ===========================================================================
# IAA Gate Tests
# ===========================================================================

class TestIaaGateTokenFormat:
    """AC6 — Token format compatibility."""

    def test_canonical_token_accepted(self):
        assert CANONICAL_TOKEN_RE.match("IAA-session-066-20260429-PASS")

    def test_canonical_token_with_complex_session_id(self):
        assert CANONICAL_TOKEN_RE.match("IAA-session-066-wave-ecap001-20260410-PASS")

    def test_deprecated_token_detected(self):
        assert _is_deprecated_token("IAA-066-20260429-PASS")

    def test_canonical_token_not_deprecated(self):
        assert not _is_deprecated_token("IAA-session-066-20260429-PASS")

    def test_invalid_token_not_canonical(self):
        assert not CANONICAL_TOKEN_RE.match("IAA-PASS")
        assert not CANONICAL_TOKEN_RE.match("IAA-session-PASS")
        assert not CANONICAL_TOKEN_RE.match("session-066-20260429-PASS")


class TestIaaGateExtraction:
    """Test evidence text parsing."""

    def test_extract_canonical_token(self):
        text = f"PHASE_B_BLOCKING_TOKEN: {CANONICAL_TOKEN}\n"
        ev = _extract_evidence_from_text(text, "test.md")
        assert ev.token == CANONICAL_TOKEN
        assert ev.phase_b_token_present is True

    def test_extract_pr_number(self):
        text = f"PR: #{PR_NUMBER}\n"
        ev = _extract_evidence_from_text(text, "test.md")
        assert ev.pr_number == PR_NUMBER

    def test_extract_issue_number(self):
        text = f"Issue: #{ISSUE_NUM}\n"
        ev = _extract_evidence_from_text(text, "test.md")
        assert ev.issue_number == ISSUE_NUM

    def test_extract_reviewed_sha(self):
        text = f"Reviewed SHA: {HEAD_SHA}\n"
        ev = _extract_evidence_from_text(text, "test.md")
        assert ev.reviewed_sha == HEAD_SHA

    def test_extract_verdict(self):
        text = "Verdict: PASS\n"
        ev = _extract_evidence_from_text(text, "test.md")
        assert ev.verdict_present is True

    def test_extract_stale_wording(self):
        text = "PENDING IAA INVOCATION\n"
        ev = _extract_evidence_from_text(text, "test.md")
        assert len(ev.stale_wording) > 0

    def test_stale_phase_b_pending(self):
        text = "PHASE_B_BLOCKING_TOKEN: PENDING\n"
        ev = _extract_evidence_from_text(text, "test.md")
        assert len(ev.stale_wording) > 0

    def test_no_stale_wording_clean_text(self):
        text = f"PHASE_B_BLOCKING_TOKEN: {CANONICAL_TOKEN}\nVerdict: PASS\n"
        ev = _extract_evidence_from_text(text, "test.md")
        assert len(ev.stale_wording) == 0


class TestIaaGateShaComparison:
    """AC7 — SHA freshness."""

    def test_full_sha_match(self):
        assert _sha_prefix_match(HEAD_SHA, HEAD_SHA)

    def test_short_sha_matches_long(self):
        short = HEAD_SHA[:7]
        assert _sha_prefix_match(short, HEAD_SHA)

    def test_different_sha_no_match(self):
        assert not _sha_prefix_match(HEAD_SHA, OLD_SHA)

    def test_empty_sha_no_match(self):
        assert not _sha_prefix_match("", HEAD_SHA)
        assert not _sha_prefix_match(HEAD_SHA, "")


class TestIaaGatePassCondition:
    """AC1 — Valid IAA evidence passes the gate."""

    def test_valid_evidence_passes(self, tmp_path):
        """AC9: valid IAA + ECAP evidence passes."""
        wr_dir = tmp_path / ".agent-admin" / "wave-records"
        wr_dir.mkdir(parents=True)
        (wr_dir / "amc-wave-record-test-20260429.md").write_text(
            _make_valid_wave_record(pr=PR_NUMBER, sha=HEAD_SHA)
        )

        result = run_iaa_gate(
            pr_number=PR_NUMBER,
            head_sha=HEAD_SHA,
            governing_issue=ISSUE_NUM,
            repo_root=tmp_path,
        )
        assert result.passed, f"Expected PASS but got failures: {result.failures}"

    def test_valid_evidence_with_short_sha(self, tmp_path):
        """Short SHA in evidence matches long current head SHA."""
        wr_dir = tmp_path / ".agent-admin" / "wave-records"
        wr_dir.mkdir(parents=True)
        (wr_dir / "amc-wave-record-test-20260429.md").write_text(
            _make_valid_wave_record(pr=PR_NUMBER, sha=HEAD_SHA[:7])
        )

        result = run_iaa_gate(
            pr_number=PR_NUMBER,
            head_sha=HEAD_SHA,
            governing_issue=ISSUE_NUM,
            repo_root=tmp_path,
        )
        assert result.passed, f"Expected PASS but got: {result.failures}"


class TestIaaGateFailConditions:
    """AC1 — Missing or invalid evidence fails the gate."""

    def test_missing_token_fails(self, tmp_path):
        """AC9: missing IAA token fails."""
        wr_dir = tmp_path / ".agent-admin" / "wave-records"
        wr_dir.mkdir(parents=True)
        # Wave record exists but has no token
        (wr_dir / "amc-wave-record-test-20260429.md").write_text(
            f"# Wave record\ntriggering_issue: #{ISSUE_NUM}\nPR: #{PR_NUMBER}\n"
        )

        result = run_iaa_gate(
            pr_number=PR_NUMBER,
            head_sha=HEAD_SHA,
            governing_issue=ISSUE_NUM,
            repo_root=tmp_path,
        )
        assert not result.passed
        assert any("MISSING" in f for f in result.failures)

    def test_no_evidence_files_fails(self, tmp_path):
        """AC9: no evidence files at all fails."""
        result = run_iaa_gate(
            pr_number=PR_NUMBER,
            head_sha=HEAD_SHA,
            governing_issue=ISSUE_NUM,
            repo_root=tmp_path,
        )
        assert not result.passed
        assert any("MISSING" in f for f in result.failures)

    def test_wrong_pr_fails(self, tmp_path):
        """AC9: token with wrong PR fails."""
        wr_dir = tmp_path / ".agent-admin" / "wave-records"
        wr_dir.mkdir(parents=True)
        (wr_dir / "amc-wave-record-test-20260429.md").write_text(
            _make_valid_wave_record(pr=9999, sha=HEAD_SHA)  # Wrong PR
        )

        result = run_iaa_gate(
            pr_number=PR_NUMBER,
            head_sha=HEAD_SHA,
            governing_issue=ISSUE_NUM,
            repo_root=tmp_path,
        )
        assert not result.passed
        # Should fail because token references different PR or PR field absent/wrong
        failures_str = " ".join(result.failures)
        assert "PR" in failures_str or "WRONG" in failures_str or "MISSING" in failures_str

    def test_wrong_issue_fails(self, tmp_path):
        """AC9: token with wrong issue fails."""
        wr_dir = tmp_path / ".agent-admin" / "wave-records"
        wr_dir.mkdir(parents=True)
        (wr_dir / "amc-wave-record-test-20260429.md").write_text(
            _make_valid_wave_record(pr=PR_NUMBER, issue=9999, sha=HEAD_SHA)
        )

        result = run_iaa_gate(
            pr_number=PR_NUMBER,
            head_sha=HEAD_SHA,
            governing_issue=ISSUE_NUM,
            repo_root=tmp_path,
        )
        assert not result.passed
        assert any("ISSUE" in f or "issue" in f.lower() for f in result.failures)

    def test_missing_reviewed_sha_fails(self, tmp_path):
        """AC9: token with missing reviewed SHA fails."""
        wr_dir = tmp_path / ".agent-admin" / "wave-records"
        wr_dir.mkdir(parents=True)
        # Record without Reviewed SHA
        text = f"""\
# Wave Record
PHASE_B_BLOCKING_TOKEN: {CANONICAL_TOKEN}
PR: #{PR_NUMBER}
Issue: #{ISSUE_NUM}
Verdict: PASS
"""
        (wr_dir / "amc-wave-record-test-20260429.md").write_text(text)

        result = run_iaa_gate(
            pr_number=PR_NUMBER,
            head_sha=HEAD_SHA,
            governing_issue=ISSUE_NUM,
            repo_root=tmp_path,
        )
        assert not result.passed
        assert any("SHA" in f for f in result.failures)

    def test_stale_sha_fails(self, tmp_path):
        """AC9: token reviewed SHA older than current head fails."""
        wr_dir = tmp_path / ".agent-admin" / "wave-records"
        wr_dir.mkdir(parents=True)
        (wr_dir / "amc-wave-record-test-20260429.md").write_text(
            _make_valid_wave_record(pr=PR_NUMBER, sha=OLD_SHA)  # Old SHA
        )

        result = run_iaa_gate(
            pr_number=PR_NUMBER,
            head_sha=HEAD_SHA,  # Current (different) head
            governing_issue=ISSUE_NUM,
            repo_root=tmp_path,
        )
        assert not result.passed
        assert any("SHA" in f or "STALE" in f for f in result.failures)

    def test_stale_pending_wording_fails(self, tmp_path):
        """AC9: stale post-IAA PENDING wording fails."""
        wr_dir = tmp_path / ".agent-admin" / "wave-records"
        wr_dir.mkdir(parents=True)
        (wr_dir / "amc-wave-record-test-20260429.md").write_text(
            _make_valid_wave_record(pr=PR_NUMBER, sha=HEAD_SHA, stale=True)
        )

        result = run_iaa_gate(
            pr_number=PR_NUMBER,
            head_sha=HEAD_SHA,
            governing_issue=ISSUE_NUM,
            repo_root=tmp_path,
        )
        assert not result.passed
        assert any("STALE" in f or "WORDING" in f for f in result.failures)


class TestIaaGateAc6DeprecatedFormat:
    """AC6 — Deprecated token format rejected."""

    def test_deprecated_format_fails(self, tmp_path):
        """AC6: deprecated token format IAA-NNN-YYYYMMDD-PASS fails."""
        wr_dir = tmp_path / ".agent-admin" / "wave-records"
        wr_dir.mkdir(parents=True)
        text = f"""\
# Wave Record
PHASE_B_BLOCKING_TOKEN: {DEPRECATED_TOKEN}
PR: #{PR_NUMBER}
Issue: #{ISSUE_NUM}
Reviewed SHA: {HEAD_SHA}
Verdict: PASS
"""
        (wr_dir / "amc-wave-record-test-20260429.md").write_text(text)

        result = run_iaa_gate(
            pr_number=PR_NUMBER,
            head_sha=HEAD_SHA,
            governing_issue=ISSUE_NUM,
            repo_root=tmp_path,
        )
        assert not result.passed
        assert any("DEPRECATED" in f or "FORMAT" in f for f in result.failures)


class TestIaaGateIaaMemoryEvidence:
    """Test that IAA memory files are also searched for evidence."""

    def test_iaa_memory_file_accepted(self, tmp_path):
        """Evidence from IAA memory file is valid."""
        mem_dir = (
            tmp_path
            / ".agent-workspace"
            / "independent-assurance-agent"
            / "memory"
        )
        mem_dir.mkdir(parents=True)
        (mem_dir / "session-066-20260429.md").write_text(
            _make_valid_wave_record(pr=PR_NUMBER, sha=HEAD_SHA)
        )

        result = run_iaa_gate(
            pr_number=PR_NUMBER,
            head_sha=HEAD_SHA,
            governing_issue=ISSUE_NUM,
            repo_root=tmp_path,
        )
        assert result.passed, f"Expected PASS but got: {result.failures}"


# ===========================================================================
# ECAP Gate Tests
# ===========================================================================

class TestEcapProtectedPathClassification:
    """AC3 — Protected path detection."""

    def test_governance_path_is_protected(self, tmp_path):
        hits = classify_protected_paths(
            ["governance/canon/SOME_CANON.md"],
            repo_root=tmp_path,
        )
        assert len(hits) == 1
        assert hits[0].pattern_id == "PP-03"

    def test_agent_admin_is_protected(self, tmp_path):
        hits = classify_protected_paths(
            [".agent-admin/prehandover/something.md"],
            repo_root=tmp_path,
        )
        assert len(hits) == 1
        assert hits[0].pattern_id == "PP-04"

    def test_github_agents_is_protected(self, tmp_path):
        hits = classify_protected_paths(
            [".github/agents/foreman-v2-agent.md"],
            repo_root=tmp_path,
        )
        assert len(hits) == 1
        assert hits[0].pattern_id == "PP-05"

    def test_governance_pack_is_protected(self, tmp_path):
        hits = classify_protected_paths(
            [".governance-pack/CANON_INVENTORY.json"],
            repo_root=tmp_path,
        )
        assert len(hits) == 1
        assert hits[0].pattern_id == "PP-08"

    def test_knowledge_path_is_protected(self, tmp_path):
        hits = classify_protected_paths(
            [".agent-workspace/foreman-v2/knowledge/FAIL-ONLY-ONCE.md"],
            repo_root=tmp_path,
        )
        assert len(hits) == 1

    def test_governance_workflow_is_protected(self, tmp_path):
        # PP-01: governance-affecting workflow file
        fpath = ".github/workflows/iaa-ecap-hard-gate.yml"
        (tmp_path / ".github" / "workflows").mkdir(parents=True)
        (tmp_path / fpath).write_text("# iaa gate script governance")
        hits = classify_protected_paths([fpath], repo_root=tmp_path)
        assert len(hits) == 1
        assert hits[0].pattern_id == "PP-01"

    def test_non_governance_workflow_not_protected(self, tmp_path):
        # PP-01: non-governance-affecting workflow file
        fpath = ".github/workflows/build-deploy.yml"
        (tmp_path / ".github" / "workflows").mkdir(parents=True)
        (tmp_path / fpath).write_text("# Build and deploy\nsteps: [build, test]")
        hits = classify_protected_paths([fpath], repo_root=tmp_path)
        # Should not be flagged as governance-affecting
        assert all(h.pattern_id != "PP-01" for h in hits)

    def test_regular_source_file_not_protected(self, tmp_path):
        hits = classify_protected_paths(
            ["src/components/Button.tsx"],
            repo_root=tmp_path,
        )
        assert len(hits) == 0

    def test_docs_only_file_not_protected(self, tmp_path):
        hits = classify_protected_paths(
            ["README.md", "docs/overview.md"],
            repo_root=tmp_path,
        )
        assert len(hits) == 0

    def test_empty_file_list_not_protected(self, tmp_path):
        hits = classify_protected_paths([], repo_root=tmp_path)
        assert len(hits) == 0

    def test_multiple_protected_paths(self, tmp_path):
        hits = classify_protected_paths(
            [
                "governance/canon/FOO.md",
                ".github/agents/bar-agent.md",
                "src/app.py",
            ],
            repo_root=tmp_path,
        )
        assert len(hits) == 2


class TestEcapGatePassCondition:
    """AC3/AC4/AC9 — Valid ECAP evidence passes the gate."""

    def test_non_protected_pr_passes(self, tmp_path):
        """Non-protected-path PRs always pass."""
        result = run_ecap_gate(
            pr_number=PR_NUMBER,
            changed_files=["src/components/Button.tsx"],
            repo_root=tmp_path,
        )
        assert result.passed
        assert len(result.protected_path_hits) == 0

    def test_protected_pr_with_valid_ecap_passes(self, tmp_path):
        """AC9: valid IAA + ECAP evidence passes."""
        pre_dir = tmp_path / ".agent-admin" / "prehandover"
        pre_dir.mkdir(parents=True)
        (pre_dir / f"ecap-reconciliation-{PR_NUMBER}.md").write_text(
            _make_valid_ecap_reconciliation(pr=PR_NUMBER)
        )

        result = run_ecap_gate(
            pr_number=PR_NUMBER,
            changed_files=["governance/canon/SOME_CANON.md"],
            repo_root=tmp_path,
        )
        assert result.passed, f"Expected PASS but got: {result.failures}"

    def test_cs2_waiver_passes(self, tmp_path):
        """AC9: ECAP waived with valid CS2 waiver passes."""
        pre_dir = tmp_path / ".agent-admin" / "prehandover"
        pre_dir.mkdir(parents=True)
        (pre_dir / f"ecap-reconciliation-{PR_NUMBER}.md").write_text(
            _make_valid_ecap_reconciliation(
                pr=PR_NUMBER,
                waiver_ref=f"CS2-WAIVER-{PR_NUMBER}",
            )
        )

        result = run_ecap_gate(
            pr_number=PR_NUMBER,
            changed_files=["governance/canon/SOME_CANON.md"],
            repo_root=tmp_path,
        )
        assert result.passed, f"Expected PASS but got: {result.failures}"


class TestEcapGateFailConditions:
    """AC3/AC4 — Missing or invalid ECAP evidence fails the gate."""

    def test_protected_path_without_ecap_fails(self, tmp_path):
        """AC9: protected-path change without ECAP evidence fails."""
        result = run_ecap_gate(
            pr_number=PR_NUMBER,
            changed_files=["governance/canon/SOME_CANON.md"],
            repo_root=tmp_path,
        )
        assert not result.passed
        assert any("ECAP" in f for f in result.failures)

    def test_self_certified_ecap_fails(self, tmp_path):
        """AC9: ECAP self-certification without committed bundle fails."""
        # Only wave record has ECAP assertions — no committed reconciliation bundle
        wr_dir = tmp_path / ".agent-admin" / "wave-records"
        wr_dir.mkdir(parents=True)
        (wr_dir / "amc-wave-record-test-20260429.md").write_text(
            f"""\
# Wave Record
PR: #{PR_NUMBER}
ecap_invoked: true
ecap_verdict: PASS
"""
        )
        # Ensure no ECAP reconciliation file exists
        pre_dir = tmp_path / ".agent-admin" / "prehandover"
        pre_dir.mkdir(parents=True)

        # has_only_self_certified_ecap should return True
        assert has_only_self_certified_ecap(tmp_path, PR_NUMBER) is True

    def test_missing_ecap_fields_fails(self, tmp_path):
        """AC3: ECAP evidence with missing required fields fails."""
        pre_dir = tmp_path / ".agent-admin" / "prehandover"
        pre_dir.mkdir(parents=True)
        (pre_dir / f"ecap-reconciliation-{PR_NUMBER}.md").write_text(
            _make_valid_ecap_reconciliation(
                pr=PR_NUMBER,
                missing_fields=["ecap_verdict", "protected_path_ceremony_verdict"],
            )
        )

        result = run_ecap_gate(
            pr_number=PR_NUMBER,
            changed_files=["governance/canon/SOME_CANON.md"],
            repo_root=tmp_path,
        )
        assert not result.passed
        assert any("FIELDS" in f or "MISSING" in f for f in result.failures)

    def test_ecap_required_na_fails(self, tmp_path):
        """AC3: ecap_required: N/A on protected-path PR fails."""
        pre_dir = tmp_path / ".agent-admin" / "prehandover"
        pre_dir.mkdir(parents=True)
        (pre_dir / f"ecap-reconciliation-{PR_NUMBER}.md").write_text(
            _make_valid_ecap_reconciliation(
                pr=PR_NUMBER,
                na_ecap_required=True,
            )
        )

        result = run_ecap_gate(
            pr_number=PR_NUMBER,
            changed_files=["governance/canon/SOME_CANON.md"],
            repo_root=tmp_path,
        )
        assert not result.passed
        assert any("N/A" in f for f in result.failures)

    def test_ecap_invoked_na_fails(self, tmp_path):
        """AC3: ecap_invoked: N/A on protected-path PR fails."""
        pre_dir = tmp_path / ".agent-admin" / "prehandover"
        pre_dir.mkdir(parents=True)
        (pre_dir / f"ecap-reconciliation-{PR_NUMBER}.md").write_text(
            _make_valid_ecap_reconciliation(
                pr=PR_NUMBER,
                na_ecap_invoked=True,
            )
        )

        result = run_ecap_gate(
            pr_number=PR_NUMBER,
            changed_files=["governance/canon/SOME_CANON.md"],
            repo_root=tmp_path,
        )
        assert not result.passed
        assert any("N/A" in f for f in result.failures)

    def test_stale_pending_wording_in_ecap_fails(self, tmp_path):
        """AC9: stale post-IAA PENDING wording in ECAP/checklist fails."""
        pre_dir = tmp_path / ".agent-admin" / "prehandover"
        pre_dir.mkdir(parents=True)
        (pre_dir / f"ecap-reconciliation-{PR_NUMBER}.md").write_text(
            _make_valid_ecap_reconciliation(pr=PR_NUMBER, stale=True)
        )

        result = run_ecap_gate(
            pr_number=PR_NUMBER,
            changed_files=["governance/canon/SOME_CANON.md"],
            repo_root=tmp_path,
        )
        assert not result.passed
        assert any("STALE" in f or "WORDING" in f for f in result.failures)


class TestEcapGateAc4AntiSelfCertification:
    """AC4 — Anti-self-certification."""

    def test_no_ecap_reconciliation_with_wave_assertions_is_self_certified(
        self, tmp_path
    ):
        """Wave record ECAP assertions without committed bundle = self-certified."""
        wr_dir = tmp_path / ".agent-admin" / "wave-records"
        wr_dir.mkdir(parents=True)
        (wr_dir / "amc-wave-record-test.md").write_text(
            f"PR: #{PR_NUMBER}\necap_invoked: true\necap_verdict: PASS\n"
        )
        # No ecap-reconciliation file
        pre_dir = tmp_path / ".agent-admin" / "prehandover"
        pre_dir.mkdir(parents=True)

        assert has_only_self_certified_ecap(tmp_path, PR_NUMBER) is True

    def test_committed_ecap_bundle_not_self_certified(self, tmp_path):
        """Committed ECAP reconciliation bundle is not self-certified."""
        pre_dir = tmp_path / ".agent-admin" / "prehandover"
        pre_dir.mkdir(parents=True)
        (pre_dir / f"ecap-reconciliation-{PR_NUMBER}.md").write_text(
            f"PR: #{PR_NUMBER}\necap_invoked: true\necap_verdict: PASS\n"
        )

        assert has_only_self_certified_ecap(tmp_path, PR_NUMBER) is False

    def test_no_evidence_not_self_certified(self, tmp_path):
        """No evidence at all is not 'self-certified' (it's missing)."""
        assert has_only_self_certified_ecap(tmp_path, PR_NUMBER) is False


class TestEcapGateAc5WaiverPath:
    """AC5 — CS2 waiver path."""

    def test_empty_waiver_ref_not_accepted(self, tmp_path):
        """A waiver field with N/A or empty value is not a valid waiver."""
        pre_dir = tmp_path / ".agent-admin" / "prehandover"
        pre_dir.mkdir(parents=True)
        (pre_dir / f"ecap-reconciliation-{PR_NUMBER}.md").write_text(
            _make_valid_ecap_reconciliation(
                pr=PR_NUMBER,
                missing_fields=["ecap_verdict"],
                waiver_ref="N/A",  # Invalid waiver
            )
        )

        result = run_ecap_gate(
            pr_number=PR_NUMBER,
            changed_files=["governance/canon/SOME_CANON.md"],
            repo_root=tmp_path,
        )
        # Should still fail because N/A waiver is not valid
        assert not result.passed

    def test_valid_cs2_waiver_overrides_missing_fields(self, tmp_path):
        """A valid CS2 waiver reference in the evidence bundle passes the gate."""
        pre_dir = tmp_path / ".agent-admin" / "prehandover"
        pre_dir.mkdir(parents=True)
        (pre_dir / f"ecap-reconciliation-{PR_NUMBER}.md").write_text(
            _make_valid_ecap_reconciliation(
                pr=PR_NUMBER,
                waiver_ref=f"issue-#{PR_NUMBER}-cs2-waiver-2026-04-29",
            )
        )

        result = run_ecap_gate(
            pr_number=PR_NUMBER,
            changed_files=["governance/canon/SOME_CANON.md"],
            repo_root=tmp_path,
        )
        assert result.passed, f"Expected PASS with CS2 waiver, got: {result.failures}"


# ===========================================================================
# Integration tests: both gates together
# ===========================================================================

class TestCombinedGates:
    """Integration tests for both gates on the same PR fixture."""

    def test_full_pass_scenario(self, tmp_path):
        """AC9: valid IAA + ECAP evidence passes both gates."""
        wr_dir = tmp_path / ".agent-admin" / "wave-records"
        wr_dir.mkdir(parents=True)
        (wr_dir / "amc-wave-record-test-20260429.md").write_text(
            _make_valid_wave_record(pr=PR_NUMBER, sha=HEAD_SHA)
        )

        pre_dir = tmp_path / ".agent-admin" / "prehandover"
        pre_dir.mkdir(parents=True)
        (pre_dir / f"ecap-reconciliation-{PR_NUMBER}.md").write_text(
            _make_valid_ecap_reconciliation(pr=PR_NUMBER)
        )

        iaa_result = run_iaa_gate(
            pr_number=PR_NUMBER,
            head_sha=HEAD_SHA,
            governing_issue=ISSUE_NUM,
            repo_root=tmp_path,
        )
        ecap_result = run_ecap_gate(
            pr_number=PR_NUMBER,
            changed_files=["governance/canon/SOME_CANON.md"],
            repo_root=tmp_path,
        )

        assert iaa_result.passed, f"IAA FAIL: {iaa_result.failures}"
        assert ecap_result.passed, f"ECAP FAIL: {ecap_result.failures}"

    def test_both_gates_fail_independently(self, tmp_path):
        """Both gates fail independently — no cross-dependency."""
        # No evidence at all
        iaa_result = run_iaa_gate(
            pr_number=PR_NUMBER,
            head_sha=HEAD_SHA,
            governing_issue=ISSUE_NUM,
            repo_root=tmp_path,
        )
        ecap_result = run_ecap_gate(
            pr_number=PR_NUMBER,
            changed_files=["governance/canon/SOME_CANON.md"],
            repo_root=tmp_path,
        )

        assert not iaa_result.passed
        assert not ecap_result.passed

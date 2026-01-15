# Pre-Implementation Behavior Review Protocol Layer-Down

**Document Type**: Governance Visibility Event  
**Status**: ✅ COMPLETE  
**Created**: 2026-01-14  
**Effective Date**: 2026-01-14  
**Grace Period**: None (immediate enforcement for new enhancement PRs)  
**Authority**: maturion-foreman-governance PR #952

---

## I. Canonical Protocol Summary

**Canonical Authority** established in maturion-foreman-governance:
- Document: `PRE_IMPLEMENTATION_BEHAVIOR_REVIEW_PROTOCOL.md v1.0.0`
- PR: maturion-foreman-governance#952
- Classification: PUBLIC_API (mandatory for all repos)
- Bootstrap Learning: Wave 3.5 Performance & Scalability Validation (this repository)

**Purpose**: Prevent repeated test rework cycles by requiring builders to verify actual current behavior before writing enhancement tests.

---

## II. What This Protocol Requires

### Mandatory 4-Step Process (Enhancement Work Only)

Before writing tests for any enhancement work, builders MUST complete:

1. **Review Current Implementation in Detail**
   - Read complete implementation code
   - Identify all code paths, edge cases, boundaries
   - Review existing tests
   - Document implementation patterns

2. **Document Actual Current Behavior**
   - Execute current implementation and observe behavior
   - Document with GIVEN/WHEN/THEN format
   - Capture happy path, edge cases, error conditions
   - Identify discrepancies between code/tests/docs

3. **Identify Enhancement Delta**
   - Explicitly list PRESERVED behaviors (backward compatibility)
   - Explicitly list CHANGED behaviors (enhancements)
   - Explicitly list NEW behaviors (net-new capabilities)
   - Risk-assess each behavior change

4. **Design Tests Validating Both Preserved and New Behaviors**
   - Write tests for preserved behaviors (regression prevention)
   - Write tests for changed behaviors (enhancement validation)
   - Write tests for new behaviors (new capability validation)
   - Run PRESERVE tests against current implementation (must pass before changes)

### Documentation Requirement

- Create Pre-Implementation Behavior Review Report
- Use template: `governance/templates/PRE_IMPLEMENTATION_BEHAVIOR_REVIEW_REPORT.template.md`
- Include complete evidence for all 4 steps
- Obtain FM/Reviewer approval

---

## III. Applicability

### MANDATORY for:
- Feature enhancements to existing functionality
- Performance optimizations
- Behavior modifications
- API changes
- Database schema enhancements
- UI/UX improvements to existing components
- Refactoring that may affect observable behavior

### NOT REQUIRED for:
- Net-new features with no existing implementation
- Bug fixes where current behavior is explicitly incorrect
- Mechanical refactoring with no behavior changes
- Documentation-only changes

**When uncertain, apply the protocol.**

---

## IV. Enforcement

### Violation Severity
- **MINOR**: Incomplete evidence for one step → Remediation required
- **MODERATE**: Missing entire step → Complete remediation and re-review
- **MAJOR**: No review performed → PR rejected, must restart
- **CATASTROPHIC**: Pattern of repeated violations → Escalation to Maturion, builder retraining

### Gate Integration
- New CI workflow: `.github/workflows/pre-implementation-behavior-review-gate.yml`
- Validates presence and completeness of review report
- Blocks merge if protocol not followed (unless FM exemption granted)

---

## V. Implementation in FM Office App

### Changes Made (2026-01-14)

1. **Canonical Documents Layered Down**
   - `governance/canon/PRE_IMPLEMENTATION_BEHAVIOR_REVIEW_PROTOCOL.md` (399 lines)
   - `governance/templates/PRE_IMPLEMENTATION_BEHAVIOR_REVIEW_REPORT.template.md` (379 lines)

2. **Builder Contracts Updated**
   - All 5 builder agents (ui, api, schema, integration, qa) updated
   - Added protocol binding to governance bindings section
   - Enforcement: MANDATORY
   - Template reference included

3. **FM Contract Updated**
   - Added protocol enforcement responsibilities
   - FM must validate review reports before merge
   - FM can approve exemptions with documented justification

4. **PR Template Enhanced**
   - Added Enhancement Work Identification section
   - Added Pre-Implementation Behavior Review checklist
   - Requires explicit declaration of enhancement vs non-enhancement
   - Provides guidance on protocol compliance

5. **CI Gate Created**
   - New workflow: `pre-implementation-behavior-review-gate.yml`
   - Detects enhancement work from PR description
   - Validates review report presence and completeness
   - Comments on PR with guidance if missing
   - Blocks merge if non-compliant

6. **Build-to-Green Checklist Updated**
   - Added Pre-Implementation Behavior Review section
   - Positioned as first check before QA-to-Red validation
   - Includes exemption process

---

## VI. Transition Guidance

### For Builders

**Immediate (2026-01-14 onwards)**:
- All new enhancement PRs must follow protocol
- Review protocol document: `governance/canon/PRE_IMPLEMENTATION_BEHAVIOR_REVIEW_PROTOCOL.md`
- Use template: `governance/templates/PRE_IMPLEMENTATION_BEHAVIOR_REVIEW_REPORT.template.md`
- Complete 4 steps BEFORE writing enhancement tests

**Training**:
- Read protocol document (complete)
- Review template
- Complete at least one practice review on non-critical component
- Demonstrate protocol application to FM or senior builder

### For FM

**Review Responsibilities**:
- Validate review report exists for all enhancement PRs
- Verify all 4 steps documented with required evidence
- Confirm behavior delta is explicit and risk-assessed
- Validate tests cover preserved, changed, and new behaviors
- Block merge if protocol compliance incomplete

**Exemption Process**:
- Builder requests exemption with justification
- FM evaluates applicability and practicality
- FM grants explicit written exemption if warranted
- Exemption documented in PR description
- Exemptions are rare and require strong justification

---

## VII. Benefits Expected

### Primary Outcomes
- **Reduced Test Rework Cycles**: Fewer enhancement PRs requiring test rework after submission
- **Higher First-Pass Test Success Rate**: More tests passing on first execution
- **Faster Review Time**: Explicit behavior documentation accelerates FM review
- **Increased Builder Confidence**: Clear understanding of current behavior before changes

### Secondary Indicators
- Reduction in test-related escalations
- Reduction in "clarify expected behavior" FM queries
- Increase in reusable behavior documentation
- Improved architectural understanding from systematic review

---

## VIII. Success Metrics (Tracked by FM)

Protocol effectiveness will be measured by:
- Number of enhancement PRs requiring test rework (target: reduction of 70%+)
- First-pass test success rate (target: 85%+)
- Average FM review time for enhancement PRs (target: 30% reduction)
- Builder confidence in test design (qualitative feedback)

---

## IX. References

### Canonical Governance
- **Protocol**: `governance/canon/PRE_IMPLEMENTATION_BEHAVIOR_REVIEW_PROTOCOL.md` v1.0.0
- **Template**: `governance/templates/PRE_IMPLEMENTATION_BEHAVIOR_REVIEW_REPORT.template.md`
- **Source PR**: maturion-foreman-governance#952
- **Upstream Manifest**: Updated with this protocol as PUBLIC_API

### Related Canon
- `BUILD_PHILOSOPHY.md` — One-Time Build philosophy
- `MANDATORY_ENHANCEMENT_CAPTURE_STANDARD.md` — Enhancement capture requirements
- `BUILDER_CONTRACT_BINDING_CHECKLIST.md` — Builder execution discipline
- `COMBINED_TESTING_PATTERN.md` — Strategic integration testing

### Local Implementation
- **CI Gate**: `.github/workflows/pre-implementation-behavior-review-gate.yml`
- **PR Template**: `.github/PULL_REQUEST_TEMPLATE.md` (updated)
- **Build-to-Green Checklist**: `foreman/builder/templates/build-to-green-checklist.md` (updated)
- **All Builder Contracts**: `.github/agents/*.md` (updated)
- **FM Contract**: `.github/agents/ForemanApp-agent.md` (updated)

---

## X. Questions and Escalation

### Frequently Asked Questions

**Q: Is this required for bug fixes?**  
A: No, bug fixes where current behavior is explicitly incorrect do not require review. However, if the bug fix changes observable behavior that other components depend on, behavior review is recommended.

**Q: What if current behavior is undocumented?**  
A: Document actual behavior during Step 2, then escalate to FM. Undocumented current behavior is a governance gap that should be addressed before enhancement proceeds.

**Q: Can I skip if I wrote the original implementation?**  
A: No. Original authors may have implicit assumptions. The protocol requires explicit evidence regardless of author familiarity.

**Q: What if enhancement scope changes during implementation?**  
A: Update the Pre-Implementation Behavior Review Report. Treat it as a living document until PR submission.

### Escalation Path

**For protocol interpretation questions**: Escalate to FM  
**For exemption requests**: Escalate to FM with justification  
**For canonical governance conflicts**: Escalate to Johan/Governance Administrator

---

## XI. Completion Certification

✅ All required artifacts created and in place  
✅ All builder agents updated with protocol binding  
✅ FM agent updated with enforcement responsibilities  
✅ PR template updated with protocol requirements  
✅ CI gate implemented and active  
✅ Build-to-Green checklist updated  
✅ Visibility event documented

**Status**: COMPLETE  
**Effective**: Immediate (2026-01-14)  
**Next Review**: After 10 enhancement PRs using protocol

---

**Document Control**  
**Created**: 2026-01-14 by Governance Liaison Agent  
**Authority**: governance/canon/PRE_IMPLEMENTATION_BEHAVIOR_REVIEW_PROTOCOL.md v1.0.0  
**Status**: Active

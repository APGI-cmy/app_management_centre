# AMC Stage 1-4 Functional Delivery Retrofit Index

**Module**: App Management Centre (AMC)  
**Artifact Type**: Retrofit control index  
**Version**: 1.0  
**Status**: Produced for CS2 review  
**Wave**: amc-stage1-4-functional-delivery-retrofit-20260625  
**Issue**: app_management_centre#1185

---

## 1. Purpose

This index records the AMC Stage 1-4 functional-delivery retrofit artifacts produced under issue #1185.

These artifacts are addenda. They do not replace the original Stage 1-4 artifacts unless CS2 directs that replacement. They must be reviewed as downstream constraints for Stage 5, Stage 5a, Stage 6, Stage 7, and any later Stage 8 planning.

---

## 2. Retrofit Artifact Register

| Stage | Retrofit artifact | Function |
|---|---|---|
| Stage 1 | `modules/amc/00-app-description/functional-delivery-definition.md` | Adds the AMC functional delivery definition and high-risk surface list |
| Stage 2 | `modules/amc/01-ux-workflow-wiring-spec/cta-api-data-audit-contract-matrix.md` | Adds CTA/API/Data/Audit/Degraded/Confirmation/QA mapping |
| Stage 3 | `modules/amc/02-frs/functional-delivery-requirements-addendum.md` | Adds FR-1900 fully functional delivery requirements |
| Stage 4 | `modules/amc/03-trs/functional-delivery-technical-requirements-addendum.md` | Adds TR-1900 fully functional delivery technical requirements |
| PBFAG support | `modules/amc/06-pbfag/stage1-4-functional-delivery-change-propagation-audit.md` | Records the gap audit and downstream propagation requirements |

---

## 3. Tracker Note for Later Incorporation

After CS2 disposition, `modules/amc/BUILD_PROGRESS_TRACKER.md` should record that issue #1185 produced the Stage 1-4 functional-delivery retrofit addenda and the change-propagation audit.

The tracker should also record that Stage 8 remains not started and that downstream Stage 5/5a/6/7 disposition must account for this retrofit before Stage 8 planning is resumed.

---

## 4. Artifact Index Note for Later Incorporation

After CS2 disposition, `modules/amc/AMC_PRE_BUILD_ARTIFACT_INDEX.md` should list the five retrofit artifacts in this index and mark their authority status according to CS2's decision.

---

## 5. Known Follow-Up Items

| Follow-up | Reason |
|---|---|
| Reconcile Stage 2 `wiring-artifact-index.md` header/status | Main Stage 2 spec says approved/harmonized; the index header still says approval pending |
| Update live tracker after CS2 disposition | The tracker is the primary live control document |
| Update artifact index after CS2 disposition | The artifact index must reflect mandatory retrofit addenda |
| Check Stage 5/5a/6/7 imports | The retrofit must propagate downstream before Stage 8 planning |

---

## 6. Current Closure Status

Produced for CS2 review. Not a final approval record.

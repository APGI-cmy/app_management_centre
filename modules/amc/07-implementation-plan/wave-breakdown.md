# Wave Breakdown - Stage 8

**Stage**: 8 - Implementation Plan  
**Module**: App Management Centre (AMC)  
**Version**: 1.0  
**Status**: ✅ CS2 Approved with Conditions  
**Issue**: app_management_centre#1199  
**Disposition**: app_management_centre#1201 / merged PR #1202  
**Wave**: amc-stage8-implementation-plan-20260702

---

## 1. Purpose

This file breaks the AMC delivery plan into governed planning waves.

It is not a builder checklist and does not appoint delivery agents.

---

## 2. Wave Summary

| Wave | Name | Summary | Required evidence later |
|---|---|---|---|
| W1 | Foundation | Repo, runtime, env, CI, preview, secret boundaries | Env contract, CI proof, preview isolation proof |
| W2 | Security and Audit Baseline | Auth, tenancy, authority middleware, audit baseline | Authority proof, RLS/tenant proof, audit proof |
| W3 | Core Surfaces | Material AMC routes and visible actions | Route/action/state/audit/degraded-mode proof |
| W4 | Alerts E2E | First E2E `/alerts` acknowledgement path | UI/API/authority/state/audit/realtime/visible result proof |
| W5 | Executive Workflow | ARC, approvals, interventions, workflow surfaces | ARC model proof, workflow state proof, audit proof |
| W6 | External Integrations | AIMC, AIMCC, KUC, knowledge, Foreman, specialists, push | Service-token proof, dependency readiness, degraded-mode proof |
| W7 | Deployment Execution | Migration, release gates, rollback, health/smoke | Migration command proof, rollback proof, smoke proof |
| W8 | QA Evidence | Red-to-green consolidation and evidence package | QA-FD, QA-DEPLOY, PBFAG proof set |

---

## 3. Wave Ordering

W1 and W2 must complete before material user-action work.

W3 establishes the surface map. W4 proves the first full E2E path. W5 and W6 expand the operating surface and integrations. W7 validates deployment controls. W8 consolidates QA evidence.

---

## 4. Stage 9 Inputs

The Stage 9 Builder Checklist must preserve this wave order and must not weaken the required evidence in this file.

---

## 5. Boundary

This wave breakdown does not start build work.

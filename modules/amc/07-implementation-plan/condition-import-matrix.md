# Condition Import Matrix - Stage 8

**Stage**: 8 - Implementation Plan  
**Module**: App Management Centre (AMC)  
**Issue**: app_management_centre#1199  
**Status**: Produced for CS2 review

---

## Purpose

This matrix maps the CS2-approved Stage 5, 5a, 6, and 7 conditions into Stage 8 planning duties.

---

## Matrix

| Source | Condition | Stage 8 planning destination | Required later evidence |
|---|---|---|---|
| Stage 5 | Route/action/state/audit/degraded-mode map | W3, W4, W5 | Route proof, action proof, state proof, audit proof, degraded-mode proof |
| Stage 5a | CI and preview boundaries | W1, W7 | CI isolation proof, preview isolation proof |
| Stage 5a | Secret and environment separation | W1, W7 | Environment contract, secret boundary proof |
| Stage 5a | Migration command and release controls | W7 | Migration command proof, release gate proof |
| Stage 5a | Rollback planning | W7 | Rollback or recovery proof |
| Stage 5a | Health and smoke validation | W7 | Health endpoint proof, smoke log proof |
| Stage 5a | Dependency readiness | W6, W7 | Dependency status proof, degraded-mode proof |
| Stage 6 | QA-FD rows | W8 | Functional red-to-green proof |
| Stage 6 | QA-DEPLOY rows | W7, W8 | Deployment red-to-green proof |
| Stage 7 | PBFAG-FD rows | W3, W4, W5 | Functional delivery evidence |
| Stage 7 | PBFAG-DEPLOY rows | W1, W7 | Deployment evidence |
| Stage 7 | PBFAG-QA rows | W8 | QA evidence package |
| Stage 7 | PBFAG-TRACK rows | W8 | Tracker/index update proof |
| Stage 7 | PBFAG-STAGE8 rows | All waves | Stage 8 package completeness proof |
| Stage 7 | First E2E `/alerts` acknowledgement path | W4 | UI/API/authority/state/audit/realtime/visible result proof |
| CS2 decision | No placeholder, stub, skipped, todo, or trivial proof | W8 | Real evidence only |

---

## Stage 9 Carry-Forward Rule

A later Stage 9 checklist must import this matrix without reducing the evidence standard.

---

## Boundary

This matrix is planning evidence only and does not start build work.

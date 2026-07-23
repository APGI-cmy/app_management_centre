# AMC Stage 5 Coverage Note

**Status**: ✅ CS2 Approved with Conditions — decision issue #1197 / merged PR #1198.  

Stage: 5 Architecture
Issue: app_management_centre#1187
PR: app_management_centre#1188

This artifact records coverage for the app-description policy rows required by the minimum architecture template.

| Row | Coverage | Status |
|---|---|---|
| 01 Build lifecycle | Tracker and stage notes preserve the 12-stage sequence. | COVERED |
| 02 Derivation chain | App Description, UX/Wiring, FRS, TRS, FR-1900, and TR-1900 are upstream inputs. | COVERED |
| 03 Technology stack | Next.js, React, Supabase, Vercel, Edge Functions, Realtime, and external interfaces are defined. | COVERED |
| 04 Deliverables | Addendum, map, audit, review note, env template, tracker update, and wave record are listed. | COVERED |
| 05 Component completion | Component completion requires UI, service target, state, audit, degraded behavior, and QA mapping. | COVERED |
| 06 Test-first rule | Stage 6 must derive RED tests before planning. | COVERED |
| 07 Physical verification | Later evidence must include running surface, API, persistence, audit, screens where applicable, and test logs. | COVERED |
| 08 PBFAG | Stage 7 must use these architecture controls as gate inputs. | COVERED |
| 09 Authority chain | Foreman, CS2, builder, IAA, and ECAP boundaries are preserved. | COVERED |
| 10 Schema-to-hook | State tables, route handlers, RLS, and UI update paths are mapped. | COVERED |
| 11 Table pathways | Action-to-state and audit mapping records read, write, and projection pathways. | COVERED |
| 12 RLS | Tenant-scoped RLS with organisation_id is architecture-binding. | COVERED |
| 13 Auth wiring | Supabase Auth and server-side checks are architecture-binding. | COVERED |
| 14 AI integration | AIMC-only routing is preserved. | COVERED |
| 15 Edge function registry | Scheduler functions are listed in the Stage 5 Architecture. | COVERED |
| 16 Deployment wave | Stage 5a and Stage 8 must define execution and wave details before later work. | COVERED |
| 17 Env naming | Root `.env.example` defines required names using placeholders only. | COVERED |
| 18 Deployment runbook | Stage 5a must define deployment execution, validation, and rollback. | COVERED |
| 19 Notification and UX patterns | Alert, push, realtime, mobile, degraded, success, and failure states are defined. | COVERED |
| 20 Shared state | Supabase state, Realtime channels, and external projections are mapped. | COVERED |
| 21 API authentication | User and service identity requirements are declared. | COVERED |
| 22 Audit log design | Append-only audit events and action-specific audit families are defined. | COVERED |
| 23 Tracker update | BUILD_PROGRESS_TRACKER updated for issue #1187 / PR #1188. | COVERED |
| 24 State persistence | AMC-owned state, external projections, and transient display state are mapped. | COVERED |

No row is marked as a blocking gap.

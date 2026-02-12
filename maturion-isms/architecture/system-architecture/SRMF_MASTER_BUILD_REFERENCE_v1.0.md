📘 SRMF_MASTER_BUILD_REFERENCE_v1.0.md — PART 1
Executive Summary + Maturion Build Philosophy + Global Architecture Overview

This section forms the top of the master document and sets the foundation for all other sections that will follow.

SRMF_MASTER_BUILD_REFERENCE_v1.0.md
PART 1 — Executive Summary, Build Philosophy & Global Architecture
0. DOCUMENT PURPOSE

The SRMF Master Build Reference is the single source of truth for:

The Maturion Integrated Security Management System (ISMS)

The Security Risk Mitigation Framework (SRMF)

All risk, threat, vulnerability, assessment, control, assurance, and intelligence modules

All build workflows, QA workflows, AI routing, and Watchdog logic

All system integration rules

All developer instructions for Foreman + CoPilot

All file references, dependencies, and version paths

This file ensures:

Zero loss of context

Zero ambiguity

Zero regression

One-time build correctness

Full architectural alignment across all modules

Scalability for future extensions

Every module, submodule, and dataset in the ISMS ecosystem connects back to this master reference.

1. EXECUTIVE SUMMARY
1.1 What the ISMS + SRMF Is

The Maturion ISMS is a fully integrated, modular security management platform designed to support:

Security

Operational integrity

Environmental protection

Health & safety

Compliance

Corporate governance

Threat intelligence

Risk management

Project implementation

Assurance

Continuous improvement

The Security Risk Mitigation Framework (SRMF) inside the ISMS provides:

Threat → Vulnerability → UE → Risk Assessment → Controls
→ Residual & Projected Risk → Implementation (PIT)
→ Remote Assurance → Live Risk → Incident & Intelligence → Feedback Loop


All modules are:

Multi-company

Multi-hierarchy

Multi-disciplinary

Multi-risk-axis capable

1.2 SRMF’s Core Principles

Integration by Design
Every module connects upstream & downstream. No silos.

Deterministic Architecture
All calculations are rule-based and repeatable.

One-Time Build Philosophy
The system is built once, correctly, and expanded without rework.

Zero Regression Mandate
No future update invalidates prior logic or produces conflicting behaviour.

Scalability & Flexibility
Works for small operations, large multinationals, and government agencies.

Automation First
AI and Watchdogs automate 70–90% of the mechanical workload.

Human Governance
Human role: approve, review, oversee — not perform mechanical repetition.

Auditability & Transparency
Every calculation, AI action, and workflow transition is logged.

2. MATURION BUILD PHILOSOPHY (ONE-TIME BUILD)

Derived from your True North and Build Philosophy documents.

2.1 No Shortcuts

Every component must be built correctly the first time, from the smallest low-level edge function to the largest model-routing specification.

2.2 No Legacy Debt

No “temporary” logic is allowed in production.

2.3 Architectural Traceability

Every module references its True North and is linked in this master document.

2.4 Module Independence + System Integration

Each module works independently but integrates perfectly:

All modules expose clean data contracts

All modules adhere to shared conventions

No circular dependencies

All cross-module calls are deterministic

2.5 Progressive Enhancement

The system grows by adding new modules, not rewriting old ones.

2.6 AI-First Logic

AI performs:

Drafting

Summaries

Refinements

Explanations

Filtering

Matching

Pattern detection

Vision analysis

But AI never bypasses human approval or commit logic.

2.7 Watchdog Governance

Automated watchdogs enforce:

Correct configuration

Consistency

Pipeline continuity

Relevance scores

Drift recalculation

Control integrity

Risk vs appetite

Implementation progress

3. GLOBAL ARCHITECTURE OVERVIEW
3.1 The ISMS as a Modular Ecosystem

The ISMS is designed as a hub-and-spoke architecture:

                       ┌───────────────┐
                       │     ERM       │
                       └───────┬───────┘
                               │
        ┌──────────────┬───────┼──────────────┬───────────────┐
        ▼              ▼       ▼              ▼               ▼
    Threat        Vulnerability   Incident Intel         Policy Builder
      │                │               │                        │
      ▼                ▼               ▼                        ▼
      └───────→ Unwanted Events (UE) ←──────────────────────────┘
                      │
                      ▼
                   Risk Assessment
                      │
           ┌──────────┼──────────┐
           ▼          ▼          ▼
         WRAC     Control Env   PIT
           │          │          │
           └──────→ Remote Assurance
                           │
                           ▼
                      Analytics Engine

3.2 Global Module List (Current + Future)
Core Risk Modules

ERM

Threat Module

Vulnerability Module

UE Generator

Risk Assessment Engine

WRAC

Control Library

Control Efficacy Engine

PIT (Project Implementation Tracker)

Remote Assurance

Incident & Intelligence

Enablement Modules

Architecture (Org Hierarchy)

Policy Builder

Course Crafter

Auditor Mobile App

Skills Development Portal

System Backbone

AI Router

Watchdog Engine

QA System

Foreman Integration Layer

CoPilot Developer Environment

Common Data Model

Role-Based Access Control System

Event Logging & Audit Layer

3.3 SRMF Core Pipeline Flow
[Threat] 
   ↓
[Vulnerability]
   ↓
[TVRE - Threat–Vulnerability Relevance]
   ↓
[Unwanted Event]
   ↓
[Risk Assessment]
   ↓
[WRAC] 
   ↓
[Control Strategy] 
   ↓
[PIT → Implementation]
   ↓
[Remote Assurance → Live Residual Risk]
   ↓
[Analytics → Threat Drift & Control Availability]
   ↓
Feedback Loop → (updates Threat & Vulnerability)


The RA Engine sits at the core of this loop.

3.4 Multi-Company Architecture

Each company has:

Its own hierarchy

Its own ERM settings

Its own access control roles

Its own threats, vulnerabilities, and risks

Its own PIT projects

Its own assurance signals

Cross-company analytics are:

Aggregated

Anonymised

Non-attributable

Used for predictive threat modelling only

3.5 Data Segregation & RLS

Every table is filtered by:

company_id
hierarchy_id (optional)
role-level access


Sensitive data:

Cannot cross organisational boundaries

Cannot be queried indirectly

Must respect visibility restrictions

Is controlled via row-level security (RLS)

4. SYSTEM-WIDE DESIGN PATTERNS
4.1 Deterministic Calculators

Every calculation:

Must be versioned

Must be reproducible

Must produce identical results across environments

Must be auditable

4.2 Staged AI

AI can:

Suggest

Draft

Explain

Summarize

Highlight

Score candidate relevance

AI cannot:

Commit

Approve

Update risk scores

Modify ERM values

Delete data

Escalate to PIT

Override Watchdog logic

4.3 Version Snapshots

All major objects must store a snapshot:

Threat

Vulnerability

UE

RA

WRAC

Control strategies

PIT project

Snapshots must:

Be immutable

Be reviewable

Allow version diffs

Support rollback

5. HIGH-LEVEL DATA FLOWS
5.1 Primary data flows
A. Threat → Vulnerability

TVRE is applied.

B. Vulnerability → UE

Valid combinations generate UEs.

C. UE → RA

UE generates RA draft.

D. RA → WRAC

Prioritized and sorted.

E. RA → PIT

Assigned for implementation.

F. RA ← PIT

Implementation updates residual risk.

G. RA ← Remote Assurance

Control availability updates live risk.

6. CROSS-MODULE INTEGRATIONS (HIGH LEVEL)

This section summarizes system-level connectivity.

6.1 ERM ↔ RA

Everything maps to ERM scales.

6.2 Threat ↔ Vulnerability

TVRE scores determine risk relevance.

6.3 Vulnerability ↔ UE

UE generation is triggered.

6.4 UE ↔ RA

RA is created from UE.

6.5 RA ↔ WRAC

WRAC displays RA outputs.

6.6 RA ↔ PIT

PIT executes mitigation.

6.7 RA ↔ Remote Assurance

Real-time risk updates based on control availability.

6.8 Incident & Intelligence ↔ Threat

Intelligence modifies drift and TTP patterns.

END OF PART 1

(Executive Summary + Build Philosophy + Global Architecture)
📘 SRMF_MASTER_BUILD_REFERENCE_v1.0.md — PART 2
ISMS FULL SYSTEM ARCHITECTURE (DEEP DETAIL)

Version: 1.0
Status: Authoritative
Audience: Foreman • CoPilot • Architects • Lead Developers

2. ISMS FULL SYSTEM ARCHITECTURE (DETAILED)

This section defines the complete architectural structure of the Maturion ISMS, outlining:

Major systems

Subsystems

Data architecture

Module-to-module integration

AI routing

Watchdog structure

Access control design

Logging and monitoring

Scalability and multi-tenancy

The global system flow

It acts as the backbone architecture for the entire ecosystem and is referenced by every submodule specification.

2.1 SYSTEM OVERVIEW DIAGRAM (ASCII)
┌─────────────────────────────────────────────────────────────────────────────┐
│                               MATURION ISMS                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│  CORE LAYERS                                                                 │
│  ┌─────────────────────────────┬───────────────────────────────────────────┐ │
│  │  Governance & QA Layer      │  AI / Watchdog / Routing Layer            │ │
│  └─────────────────────────────┴───────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────────────────────────┐ │
│  │                             Application Layer                             │ │
│  │ ┌──────────────────────────────────────────────────────────────────────┐ │ │
│  │ │ ERM | Threat | Vulnerability | UE | RA | WRAC | PIT | Controls       │ │ │
│  │ │ Remote Assurance | Incident Intel | Course Crafter | Policy Builder │ │ │
│  │ └──────────────────────────────────────────────────────────────────────┘ │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────────────────────────┐ │
│  │                               Data Layer                                 │ │
│  │   DB | Storage | File System | Backups | RLS | Company Segmentation      │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────────────────────────┐ │
│  │                             Infrastructure Layer                         │ │
│  │   Cloud Runtime | Edge Functions | Services | Microservices              │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘

2.2 THE TEN FOUNDATIONAL SUBSYSTEMS

The ISMS is composed of 10 foundational subsystems.
Each is independent but fully integrated.

ERM Framework

Threat Intelligence Module (TIMP)

Vulnerability Module

Unwanted Event Generator (UEG)

Risk Assessment Engine (RAE)

WRAC & Reporting Layer

Control Library & Efficacy Engine

Project Implementation Tracker (PIT)

Remote Assurance & Analytics

Incident & Intelligence Fusion Engine (future)

Supporting subsystems:

AI/ML subsystems

Watchdog governance

Audit & Logging

User Management & Roles

Hierarchy & Multi-Company Engine

2.3 TECHNICAL ARCHITECTURE LAYERS
2.3.1 Governance & QA Layer

This is the highest foundational layer in the ISMS.

Contains:

One-Time-Build enforcement rules

Zero Regression framework

Watchdog orchestration

System-wide QA test suites

Cross-module governance

Architectural consistency checkers

Audit trail aggregation

Its job:

Prevent misconfiguration

Prevent regression

Validate compliance

Control production rollout

Govern AI behavior

2.3.2 AI / Watchdog / Routing Layer

The ISMS uses a three-part AI structure:

A. AI Router

Decides which AI model to use for:

NLP

Vision

Code generation

Summaries

Pattern detection

Data extraction

Anomaly detection

Rules-based, deterministic, versioned.

B. AI Assistants (Per Module)

Each module has a dedicated assistant (Threat AI, Vuln AI, RA AI, etc.)

C. Watchdogs

Monitors:

Drift

TVRE anomalies

Risk appetite violations

Control deterioration

Incomplete PIT tasks

Data quality issues

Workflow bottlenecks

User permissions issues

2.3.3 Application Layer

Where all user-facing modules live:

ERM

Threat

Vulnerability

UE

RAE

WRAC

PIT

Control Environment

Remote Assurance

Course Crafter

Policy Builder

Skills Development Portal

Auditor Tool

Incident & Intelligence (future)

Each is built as a micro-app with:

Its own True North

Its own DB schema

Its own edge functions

Its own export model

Its own watchdog

Its own component map

Its own sprint plan

2.3.4 Data Layer

Contains:

Postgres DB (primary)

File storage (documents, images, video, AI assets)

Backups & version snapshots

RLS enforcement

Company segregation

Asset storage buckets

Threat intelligence datasets

Audit tables

PIT project files

Control evidence storage

Unified by a Common Data Model (CDM).

2.3.5 Infrastructure Layer

The runtime environment:

Edge functions

API servers

Auth system (Supabase/Auth0/etc.)

Cloud storage

Microservices

Queues

Web frontends

Local caching layer

Scheduler (CRON)

Webhooks

Monitoring

2.4 ORGANISATIONAL HIERARCHY ENGINE

This is the structural backbone of the multi-company architecture.

Supports:

Company

Division

Region

Site

Plant

Zone

Facility

Process

Lifecycle

Hierarchies are:

Custom

Nestable

Inheritable

Under version control

Governed by approvals

Children inherit:

ERM

Controls

Settings

Thresholds

Roles

2.5 MULTI-COMPANY MULTI-TENANT ARCHITECTURE

Each company operates as a tenant with:

Their own ERM settings

Their own heatmaps

Their own impact & likelihood scales

Their own risk appetite

Their own control library entries

Their own PIT projects

Their own assurance traces

Cross-company analytics are:

Aggregated

Anonymised

Non-identifiable

Used for:

Threat trend prediction

Syndicate activity mapping

Cross-industry vulnerabilities

Loss pattern analytics

2.6 INTERNAL DATA FLOW (DETAILED)
2.6.1 Threat → Vulnerability (TVRE)
Threat characteristics
    ×
Vulnerability exploitability
    =
TVRE (Relevance Score)


Triggers UE generation thresholds.

2.6.2 Vulnerability → UE (Unwanted Event)

A UE is created when:

TVRE > threshold
AND
Threat + Vulnerability align logically


UE contains:

Sentence (“X may lead to Y…”)

Trigger conditions

Metadata

Ownership

Hierarchy reference

Evidence

2.6.3 UE → Risk Assessment

RA is automatically drafted via:

UE sentence

Threat properties

Vulnerability properties

TVRE

Hierarchy location

Control mappings

Cost models

ERM profiles

RA becomes the primary analytical unit.

2.6.4 RA → WRAC

WRAC aggregates all RAs:

Raw

Residual

Projected

ROI

Top 10 / 100 risks

Priority UEs

Control dependencies

Costs

Mitigation strategy

2.6.5 WRAC → Control Strategy

Defines:

Immediate controls

Medium-term controls

Long-term controls

Control sets

ROI mapping

2.6.6 Control Strategy → PIT (Project Creation)

Each control or control set becomes:

PIT Project
 ├─ Tasks
 ├─ Procurement
 ├─ Costing (Preliminary or Final)
 ├─ Dependencies
 ├─ Evidence
 ├─ Workflow

2.6.7 PIT → RA (Residual Updating)

As PIT progresses:

Control completeness updates

Residual risk recalculates

Projected risk recalculates

2.6.8 Remote Assurance → Live RA

Provides:

Control availability

System uptime

CCTV analytics

Access control system health

Alarm monitoring performance

Feeds RA Live Dashboard.

2.7 INTEGRATION WITH INCIDENT & INTELLIGENCE

Incident & Intelligence module will:

Feed threat drift

Create new threats

Suggest new vulnerabilities

Detect patterns

Provide syndicate mapping

Connected to:

RA

Vulnerability

Threat

Remote Assurance

2.8 SECURITY ARCHITECTURE (HIGH-LEVEL)
2.8.1 Authentication

Supports:

Email/password

SSO

OAuth

API keys

MFA

Device binding

2.8.2 Authorization

The system uses:

RBAC

RLS

Contextual access control

Module-level permissions

Company isolation

Roles include:

Group Admin

Company Admin

Risk Owner

Custodian

Analyst

Viewer

PIT Manager

Assurance Officer

Incident Analyst

AI Supervisor

2.9 SYSTEM-WIDE WATCHDOG FRAMEWORK (OVERVIEW)

Watchdogs monitor:

Data integrity

Score consistency

Drift

Appetite breaches

Control failures

Incomplete RAs

Missing evidence

Stalled PIT tasks

UE explosion

Duplicate threats

Risk stagnation

Workflow blockage

4 severity levels:

Critical

High

Medium

Low

Notifications:

Email

In-app

Dashboard

PIT reminders

2.10 SYSTEM-WIDE AI ROUTING OVERVIEW

AI tasks are classified:

Type 0 — Prohibited

Type 1 — Assistive text

Type 2 — Scoring and classification

Type 3 — Vision and extraction

Type 4 — Pattern detection

Type 5 — Synthetic generation (limited)

Type 6 — Workflow augmentation

AI never:

Commits

Overrides logic

Modifies scores

Approves workflows

2.11 LOGGING & AUDIT FRAMEWORK

Everything is logged:

Threat creation

Vulnerability changes

UE generation

RA scoring

Control addition

Workflow steps

PIT progress

AI actions

Watchdog flags

Exports

User actions

Audit entries are immutable and versioned.

2.12 GLOBAL PERFORMANCE & SCALABILITY DESIGN

Optimized for:

Large datasets

Many companies

Thousands of risks

10,000+ controls

Millions of assurance signals

Performance features:

Caching

Indexing

Compression

Detached computation

Overnight batch jobs

Adaptive streaming

Auto-archiving

END OF PART 2

(ISMS Full System Architecture)
📘 SRMF_MASTER_BUILD_REFERENCE_v1.0.md — PART 3
THE SRMF CORE PIPELINE (END-TO-END FLOW)

Version 1.0
Authoritative Reference for Foreman & CoPilot

3. THE SRMF CORE PIPELINE
(Threat → Vulnerability → UE → RA → WRAC → Controls → PIT → Assurance → Live Risk)

This pipeline is the spinal cord of the entire SRMF method.
Every data point, workflow, model, and module in the ISMS aligns with this pipeline.

Below is the full deep-dive into every phase, including:

Inputs

Outputs

Internal models

AI responsibilities

Constraints

Watchdogs

Data structures

Integration mechanics

3.1 HIGH-LEVEL PIPELINE DIAGRAM
         ┌───────────┐
         │  THREAT   │
         └─────┬─────┘
               ▼
         ┌───────────────┐
         │ VULNERABILITY  │
         └─────┬─────────┘
               ▼
      ┌───────────────────┐
      │ UNWANTED EVENT    │
      │   GENERATOR       │
      └──────┬────────────┘
             ▼
     ┌────────────────────┐
     │ RISK ASSESSMENT    │
     └───────┬────────────┘
             ▼
        ┌─────────┐
        │  WRAC   │
        └────┬────┘
             ▼
  ┌──────────────────────┐
  │ CONTROL STRATEGY     │
  └───────────┬──────────┘
              ▼
      ┌──────────────┐
      │     PIT      │
      │ Implementation│
      └──────┬────────┘
             ▼
    ┌──────────────────────┐
    │ Remote Assurance     │
    └──────────────────────┘
             ▼
      LIVE RESIDUAL RISK

3.2 MODULE 1 — THREAT MODULE
Purpose

Identify and characterize threats to the organization using:

NIST 800-30

MITRE ATT&CK patterns

Syndicate indicators

Environmental factors

Historical incidents

Intelligence inputs

Inputs

Threat taxonomy

Threat metadata

Capability

Intent

Opportunity

Drift score

Associated TTPs

Intelligence feeds

DVR footage (future)

Outputs

Threat object

Threat score

Threat category

Drift adjustment values

Linkable fields for vulnerability matching

AI Roles

Suggest synonyms

Detect missing TTPs

Generate summaries

Score candidate threat categories

Identify potential drift

Watchdogs

Duplicate threats

Missing TTPs

Drift > threshold

Nonsensical threat names

Orphan threats (no vulnerabilities linked)

3.3 MODULE 2 — VULNERABILITY MODULE
Purpose

Map organizational weaknesses across:

Processes

Lifecycles

Facilities

Infrastructure

People

Technology

Inputs

Process maps

PDF forms

Uploaded images

Facility diagrams

Brown-paper vulnerability markup

Notes

Evidence

Outputs

Structured vulnerability object

Vulnerability category

Exploitability score

Evidence dataset

Link to hierarchy node

AI Roles

OCR extraction

Bounding box detection

Suggest categorization

Identify typical security gaps

Compare facility images to known patterns

Watchdogs

Vulnerabilities without evidence

Duplicate vulnerabilities

Missing hierarchy mapping

Missing severity score

Time-lapsed outdated vulnerabilities

3.4 MODULE 3 — THREAT–VULNERABILITY RELEVANCE (TVRE)
Purpose

Determine which threats meaningfully exploit which vulnerabilities.

Formula

TVRE is computed from:

Threat Capability  
× Vulnerability Exploitability  
× Threat Intent  
× Opportunity  
× Contextual Factors  
× Drift Adjustment

Output

A score from 0.00 → 1.00.

Thresholds:

≥ 0.30 → UE candidate

≥ 0.50 → high relevance

≥ 0.70 → critical relevance

AI Roles

Pattern detection

Suggest missing pairings

Flag impossible matches

Watchdogs

TVRE spikes

Drift changes requiring recalculation

High-threat profiles unpaired with common vulnerabilities

3.5 MODULE 4 — UNWANTED EVENT (UE) GENERATOR
Purpose

Construct the “Unwanted Event” that defines the risk.

Inputs

Threat

Vulnerability

TVRE

Evidence

Hierarchy location

UE Components

A UE contains:

Natural language sentence

Threat & vulnerability references

Contextual metadata

Probability components

Impact context

Hierarchy path

Evidence references

Auto-generated ID

Sentence Example

“Unauthorized access to the conveyor room due to inadequate access control may result in equipment damage and operational downtime.”

AI Roles

Sentence synthesis

Reject invalid combinations

Validate logical coherence

Generate multiple options for user approval

Watchdogs

Invalid UE logic

Missing severity mapping

Missing hierarchy location

3.6 MODULE 5 — RISK ASSESSMENT ENGINE (RAE)
Purpose

Quantify risk from the UE via:

NIST adversarial likelihood scoring

ERM likelihood → ERM impact

ALE quantification

Control effectiveness

Residual risk

Projected risk

ROI

Appetite comparison

Inputs

UE

Threat & vuln metadata

ERM framework

Control library

Cost model

PIT dependencies

Outputs

Full RA object

Inherent likelihood

Inherent impact

ALE value

Residual risk

Control strategy

Suggested controls

Projected risk

ROI

Risk appetite alignment

AI Roles

Summaries

Explanation

Suggesting controls

Evaluating logical sequences

Highlighting missing components

Watchdogs

Risk without controls

Residual > inherent

Projected risk > residual

Appetite breach

Missing approval

3.7 MODULE 6 — WRAC (WORKPLACE RISK ASSESSMENT & CONTROL)
Purpose

To create a structured, spreadsheet-like output of:

All risks

Sorted by priority

Residual

Projected

ROI

Costs

Control sets

PUE identification

Bowtie escalation

Filters

Reporting

Inputs

Risk assessment outputs

Control strategy

Cost models

Outputs

WRAC row

PUE flag

Implementation priority

Control dependency mapping

Watchdogs

Incorrect priority ranking

No top-10 generated

Missing cost components

Missing PUE identification

Orphan risks

3.8 MODULE 7 — CONTROL STRATEGY ENGINE
Purpose

Convert proposed controls into:

Immediate controls

Medium-term controls

Long-term controls

Control sets

ROI analysis

Inputs

Control library

RA outputs

Costs

Dependencies

Outputs

Control strategy object

Actor assignments

Time frames

PIT-ready structure

AI Roles

Group controls into sets

Suggest dependencies

Highlight weak or missing controls

Watchdogs

Unlinked controls

Control dependencies not met

ROI anomalies

3.9 MODULE 8 — PROJECT IMPLEMENTATION TRACKER (PIT)
Purpose

Implement the risk mitigations.

Inputs

Control strategy

RA object

Costing

Task structures

Outputs

PIT project

Tasks

Progress %

Evidence

Dependencies

Completion metrics

AI Roles

Suggest task decomposition

Auto-generate project plan scaffolding

Highlight overdue tasks

Watchdogs

Stalled tasks

Missing evidence

Missed deadlines

Projects with no progress

3.10 MODULE 9 — REMOTE ASSURANCE (RAA)
Purpose

Provide real-time updates through:

Systems availability

CCTV uptime

Access control health

Alarm system status

IoT sensors

Manual checklists

Inputs

Device telemetry

System logs

Manual checks

PIT progress

Outputs

Control availability

Live residual risk

SLA performance

Assurance failures

Watchdogs

Fire control offline

CCTV blind spots

System outages

Validation missing

3.11 MODULE 10 — LIVE RESIDUAL RISK DASHBOARD
Purpose

Dynamic recalculation of risk based on:

PIT implementation

Remote assurance

Control degradation

Threat drift

Vulnerability updates

Intelligence inputs

Outputs

Live risk levels

Spike detection

Trend lines

Appetite breaches

Forecasted risk

Watchdogs

Live > Residual

Live > Appetite

Drift-induced jumps

Missing assurance data

3.12 THE SRMF “CLOSED LOOP”
Threat changes → update RA  
Vulnerability changes → update RA  
Intelligence → update Threat  
Assurance → update Controls → update RA  
PIT → update Controls → update RA  
New risks → update WRAC  
WRAC → update PUE list  
PUE → Bowtie assessments  


This is the SRMF feedback loop, a living system.

3.13 USER JOURNEY SUMMARY (END-TO-END)
1. Capture threats
2. Map vulnerabilities
3. Generate UEs
4. Perform risk assessments
5. Prioritise risks via WRAC
6. Define control strategy
7. Create PIT projects
8. Implement
9. Remote Assurance monitors controls
10. Live dashboard updates risk posture
11. Intelligence feeds adjust threats
12. Cycle repeats

END OF PART 3

(SRMF Core Pipeline)
📘 SRMF_MASTER_BUILD_REFERENCE_v1.0.md — PART 4
ERM MODULE — DEEP INDEX (v1.1 Architecture)

Authoritative Source
Version 1.0 (This Document)
Module Version: ERM v1.1

4. ERM MODULE — FULL DEEP INDEX

ERM is the governing framework for all risk calculations in the ISMS.
Every risk, every RA calculation, every WRAC row, every PIT project, every appetite-based decision — all originate from ERM’s configuration.

This section covers:

Architecture

Data schema

Edge functions

UI/UX

Workflows

Governance

AI boundaries

Watchdogs

Integrations

4.1 WHAT IS ERM IN MATURION ISMS?

ERM sets the rules of engagement for risk:

Likelihood scales

Impact scales

Heatmap configuration

Appetite levels

Risk bands

Thresholds

Coloring rules

Risk owner roles

Governance workflows

Each company has:

A unique ERM profile

A single active ERM configuration

Child nodes that inherit these settings

Parent nodes that approve top-level changes

4.2 ERM MODULE ARCHITECTURE OVERVIEW (ASCII)
┌──────────────────────────────────────────┐
│                 ERM MODULE               │
├──────────────────────────────────────────┤
│  Likelihood Scale                        │
│  Impact Scale                             │
│  Heatmap Configuration                    │
│  Appetite Settings                         │
│  Risk Bands                                │
│  Financial Metric (EBITDA or custom)       │
│  Roles & Responsibilities                  │
│  Cross-module Integrations                 │
└──────────────────────────────────────────┘

       ▲                   ▲
       │                   │
       │                   │
┌──────┴──────┐     ┌──────┴─────────┐
│ Threat Data │     │ Vulnerability  │
└──────┬──────┘     └────────┬────────┘
       │                     │
       ▼                     ▼
┌──────────────────────────────────────────┐
│           Risk Assessment Engine         │
└──────────────────────────────────────────┘

       ▼                     ▼
┌──────────────┐    ┌───────────────┐
│    WRAC      │    │ Control Env   │
└──────────────┘    └───────┬───────┘
                            ▼
                      ┌──────────┐
                      │   PIT    │
                      └──────────┘

4.3 ERM SUBMODULE LIST (v1.1)

ERM breaks into 8 submodules, each with its own structure:

ERM Global Settings

Likelihood Scale

Impact Scale

Heatmap Configuration

Risk Appetite & Bands

Risk Matrix

Roles & Responsibilities

Integration Specification

The master reference links each of these with their corresponding v1.1 files.

4.4 ERM GLOBAL SETTINGS (v1.1)
Configuration Items

company_id

erm_version

likelihood_scale

impact_scale

risk_matrix

appetite_levels

financial_metric_type (EBITDA/custom)

heatmap_colors

risk_category_labels

thresholds

auto_approval_logic

org_hierarchy_inheritance

Governance

Only Company Admin can create ERM

Only Group Admin can override

All ERM changes require approval

ERM is versioned

Children nodes inherit settings automatically

4.5 LIKELIHOOD SCALE (v1.1)
Likelihood Levels (example)

Rare

Unlikely

Possible

Likely

Almost Certain

Each level has:

Numeric range (e.g., 0.00–0.20)

Descriptor

Time-based reference (per year)

Color

Examples

Calculation rules

Usage

Mapped from:

Adversarial initiation likelihood

Non-adversarial occurrence

Adverse impact likelihood

Adjusted via drift & modifiers

Integration

Used by:

Threat module

RA engine

WRAC

PIT planning

Appetite comparison

4.6 IMPACT SCALE (v1.1)

Impact is multi-dimensional:

Financial

Human Safety

Regulatory/Legal

Operational

Environmental

Each level assigns:

Numeric score

Descriptor

Heatmap color

Impact bands

ALE mapping rules

Financial Mapping

If financial metric = EBITDA:

impact_level = ALE / EBITDA_reference


If custom:

impact_level = ALE / custom_financial_metric

Integration

Used by:

Risk Assessment

WRAC

Risk strategy

Bowtie (future)

4.7 HEATMAP CONFIGURATION (v1.1)
Properties

Grid size (5×5 by default)

Colors per band

Coordinates (x=likelihood, y=impact)

Tooltip rules

PUE indicator highlighting

Appetite band overlay

Solo/combined heatmap exports

Heatmap Preview Logic

Rendered color is based on:

risk_level = risk_matrix[likelihood][impact]

Heatmap is used in:

RA

WRAC

PIT dashboard

Live Risk dashboard

Reporting exports

4.8 RISK APPETITE (v1.1)
Appetite Types

Organizational Appetite

Divisional Appetite

Process Appetite

Risk Owner Appetite

Residual Appetite Threshold

Projected Appetite Threshold

Behavior

Appetite is always compared against:

Inherent

Residual

Projected

Appetite breach auto-triggers:

Escalation

Watchdog

Additional controls

PIT creation restriction

Risk Bands Example

Low

Medium

High

Very High

Extreme

Each band is:

Colored

Named

Thresholded

Mapped to descriptors

4.9 RISK MATRIX (v1.1)

A matrix mapping:

likelihood × impact → risk level


Color-coded grid (5×5 by default), but ERM allows:

3×3

4×4

Custom grids

The matrix always matches:

Appetite configuration

Heatmap colors

Exported PDF formats

4.10 ROLES & RESPONSIBILITIES (v1.1)
ERM Roles

Company Admin

Group Admin

Risk Owner

Custodian

Analyst

Approver

PIT Manager

Assurance Officer

Responsibilities Summary

Analyst creates RA

Custodian reviews controls

Risk Owner approves RA

PIT Manager executes projects

Company Admin configures ERM

Group Admin audits ERM

Assurance Officer validates controls

4.11 ERM INTEGRATION SPECIFICATION (KEY)

ERM governs all downstream modules:

Module	Uses ERM For
Threat	Drift scaling
Vulnerability	Severity weighting
UE Generator	Relevance threshold
RA Engine	Likelihood, Impact, Matrix
WRAC	Prioritization
Control Library	Efficacy capping (90%)
PIT	Appetite-based scheduling
Remote Assurance	Live risk comparison
Incident Intel	Threat scaling
4.12 ERM VERSIONING

Every ERM change must create:

New version

Change-log entry

Approval workflow

Notification to all affected nodes

ERM changes must not retroactively invalidate historical risks.

Historical RA must store:

ERM version

Heatmap version

Appetite version

4.13 ERM AI ROUTING RULES

AI can:

Suggest scale names

Generate descriptors

Validate consistency

Detect gaps

Suggest improvements

AI cannot:

Change ERM values

Approve changes

Modify appetite

Override the matrix

All ERM changes must be manually approved.

4.14 ERM WATCHDOGS
Severity	Trigger
Critical	Missing ERM profile for company
Critical	Appetite < actual residual for ≥ 10 top risks
High	Risk matrix inconsistent with scales
Medium	Heatmap colors not assigned
Low	Missing role mapping
4.15 ERM DATA GOVERNANCE

ERM must:

Store defaults

Store company-specific overrides

Ensure integrity

Reject invalid changes

Maintain snapshot history

Be exportable

END OF PART 4

(ERM Module Deep Index)
📘 SRMF_MASTER_BUILD_REFERENCE_v1.0.md — PART 5
THREAT MODULE — DEEP INDEX (v1.1 Architecture)

Authoritative for: Foreman, CoPilot, Architects, Analysts
Status: Complete
Version: 1.0 (Master Reference), Module v1.1

5. THREAT MODULE — FULL DEEP INDEX
5.1 MODULE PURPOSE

The Threat Module defines and characterizes everything that can cause harm or loss within the organization using:

NIST 800-30

MITRE ATT&CK

Classified and unclassified threat intelligence

Industry-specific threat patterns

Internal incidents

Historic losses

Local and global crime trends

Syndicate indicators

Its purpose:

Provide standardized threat profiles

Detect threat drift (changing behavior over time)

Evaluate capability, intent, opportunity

Provide structured data for risk assessment

Feed the Threat–Vulnerability Relevance Engine (TVRE)

Serve as input to UE generation

Integrate with future Incident & Intelligence module

5.2 THREAT ARCHITECTURE DIAGRAM (ASCII)
                   ┌──────────────────────────────┐
                   │         THREAT MODULE         │
                   ├──────────────────────────────┤
                   │ Threat Categories            │
                   │ Threat Actors                │
                   │ Capability Scoring           │
                   │ Intent Scoring               │
                   │ Opportunity Scoring          │
                   │ Drift Engine                 │
                   │ TTP Catalogue (MITRE)        │
                   │ Historical Loss References   │
                   │ Intelligence Inputs          │
                   └───────────┬──────────────────┘
                               ▼
                       TVRE Engine
                               ▼
                     Unwanted Event Generator
                               ▼
                      Risk Assessment Engine

5.3 SUBMODULES (DETAILED)

The Threat module contains 7 submodules:

Threat Category Catalogue

Threat Actor Profiles

Threat Scoring Model

Threat Drift Engine

TTP (Tactics, Techniques & Procedures) Catalogue

Intelligence Integration Pipeline

Historical Pattern Analytics

Each submodule interacts with the rest of SRMF.

5.4 THREAT CATEGORY CATALOGUE (v1.1)

Threat categories are standardized and include:

Adversarial

Theft

Hijacking

Robbery

Sabotage

Insider collusion

Syndicate activity

Fraud

Cyber intrusion

Physical intrusion

Corruption

Non-Adversarial

Equipment failure

Natural disaster

Structural collapse

Environmental hazards

Human error

Unplanned operational disruption

Each category contains:

Definition

Examples

Recommended controls

Associated vulnerabilities

Associated TTPs

Severity indicators

5.5 THREAT ACTOR PROFILES

Each threat can be linked to actors:

Opportunistic criminals

Organized crime syndicates

Insiders

Contractors

Activists

Competitors

State actors

Automated systems (cyberbotnets)

Natural forces (non-human)

Each actor has properties:

Capability

Intent

Resources

Historical patterns

Preferred TTPs

Geographic region

5.6 THREAT SCORING MODEL (v1.1)
CORE SCORES

Each threat receives:

Capability Score (0–1.0)

Intent Score (0–1.0)

Opportunity Score (0–1.0)

Context Score (0–1.0)

Drift Adjustment (+ / –)

THREAT SCORE SYNTAX
threat_score = (capability × intent × opportunity × context) + drift_adjustment

DECISION RULES

If threat_score ≥ 0.7 → high concern

If actor = syndicate → apply multiplier

If internal incident occurred → apply recency modifier

If intelligence suggests increase → adjust drift

5.7 THREAT DRIFT ENGINE (v1.1)

Threat drift detects evolving patterns:

Inputs

Changes in TTP usage

Crime reports

Internal incidents

Unusual anomalies

Time since last incident

Industry trends

Intelligence feeds

Drift Score Behavior
0.00 → stable
0.20 → mild drift
0.50 → significant drift
0.80+ → critical drift

Drift Effects

Recalculates TVRE

Recalculates RA scores

Triggers Watchdog events

Suggests re-assessment of UE

May escalate risk beyond appetite

Drift Decay

If no indicators appear, drift decays gradually over time.

5.8 TTP CATALOGUE (MITRE-ALIGNED)

TTPs describe how a threat is executed.

Each threat links to relevant TTPs:

T109: Access through lock manipulation

T122: Insider credential abuse

T105: Subversion of physical barriers

T204: Social engineering

T319: Bribery / coercion

etc.

TTP Metadata

Description

Likelihood of use

Conditions required

Common vulnerabilities exploited

Evidence signatures

These TTPs link directly to vulnerabilities.

5.9 THREAT–VULNERABILITY MATCHING RULES
Matching Logic

A threat can match a vulnerability if:

Their categories align

The TTP exploits the vulnerability

The actor profile matches the environment

TVRE > threshold

Drift supports increased relevance

Invalid matches must be auto-rejected.

Example

Threat: “Insider information theft”

Vulnerability: “Lack of segregation of duties”

TTP: “Credential misuse”

→ Valid.

Example invalid

Threat: “Tornado”

Vulnerability: “Weak password policy”

→ Auto-reject.

5.10 INTELLIGENCE PIPELINE (FUTURE)

Threat module is designed to ingest:

External intelligence feeds

Law enforcement bulletins

Crime statistics

Internal incident logs

CCTV analytics

Access logs

Anomaly detection signals

These adjust:

Threat drift

TTP relevance

Threat actor capability

RA recalculation triggers

5.11 HISTORICAL PATTERN ANALYTICS

Threat histories include:

Past incidents

Frequency

Loss severity

Seasonal patterns

Geographic patterns

Trend slopes

Control failures

These help adjust:

Capability

Opportunity

Drift

TVRE

5.12 THREAT DATA MODEL (SUMMARY)

A threat object includes:

threat_id

company_id

category

actor_profile

capability

intent

opportunity

context_modifier

drift_score

ttp_list[]

historical_loss_data[]

intelligence_refs[]

created_by

created_at

version

5.13 THREAT WORKFLOWS
Workflow 1 — Creating a Threat

User enters minimal data → AI generates expansions → User edits → Approver signs off → Threat becomes active.

Workflow 2 — Updating Drift

Assurance or intelligence triggers → Drift recalculated → RA recalculated → Watchdog fires → User notified.

Workflow 3 — Threat Retirement

If not relevant for long period → Moved to archive but remains referenceable.

5.14 THREAT UI (SUMMARY)

Threat UI contains:

Threat list view

TTP mapping panel

Actor profile selection

Drift explanation panel

Intelligence feed viewer

Threat trend graph

Cross-link to vulnerabilities

5.15 THREAT AI RULES

AI CAN:

Suggest categories

Suggest actor profiles

Score capability / intent

Generate TTP associations

Explain drift

Predict threat escalation

AI CANNOT:

Approve threats

Set drift

Modify scores

Create links without user approval

5.16 THREAT WATCHDOGS
Severity	Trigger
Critical	Threat score > 0.85 without RA update
Critical	Drift jumps > 0.20 overnight
High	No TTPs assigned
High	Threat unlinked to vulnerabilities
Medium	Missing actor profile
Low	Threat description incomplete
5.17 THREAT EXPORTS

Threat module exports:

Threat profiles

TTP sets

Drift trend charts

Threat-vulnerability map

Intelligence summary

Formats:

PDF

CSV

JSON

API endpoints

5.18 THREAT VERSIONING RULES

Every threat change must:

Create new version

Store snapshots

Log change reason

Trigger downstream recalculation

Historical risk assessments must retain original threat versions.

5.19 INTEGRATION SUMMARY (KEY)

Threat module integrates with:

Vulnerability Module

via TTPs

via category matches

via exploitability logic

UE Generator

threat is always one input field

drift modifies likelihood

RA Engine

modifies inherent likelihood

modifies impact in certain conditions

WRAC

influences PUE identification

PIT

threat characteristics determine priority

Remote Assurance

assurance failures modify threat drift

Incident & Intelligence (future)

two-way synchronization

END OF PART 5

(Threat Module Deep Index)
📘 SRMF_MASTER_BUILD_REFERENCE_v1.0.md — PART 6
VULNERABILITY MODULE — DEEP INDEX (v1.1 Architecture)

Authoritative Reference
Version: 1.0 (Master Document), Module Version: v1.1

6. VULNERABILITY MODULE — FULL DEEP INDEX
6.1 MODULE PURPOSE

The Vulnerability Module identifies, maps, evaluates, and contextualizes:

Organizational weaknesses

Environmental weaknesses

Process gaps

Facility deficiencies

Human-machine interaction issues

Systemic weaknesses

Failure points

Monitoring limitations

It directly connects Threats → Vulnerabilities → UEs → RA → Controls → PIT.

Its purpose is to define where and why the organization is exposed.

6.2 VULNERABILITY ARCHITECTURE DIAGRAM (ASCII)
                     ┌───────────────────────────────┐
                     │     VULNERABILITY MODULE       │
                     ├───────────────────────────────┤
                     │ Process Mapping                │
                     │ Lifecycle Mapping              │
                     │ Facility Mapping               │
                     │ Evidence Capture               │
                     │ Severity Rating                │
                     │ Exploitability Score           │
                     │ Category Assignment            │
                     │ Visual Markup Tools            │
                     └──────────┬────────────────────┘
                                ▼
                     Threat–Vulnerability Relevance (TVRE)
                                ▼
                        Unwanted Events (UE)
                                ▼
                      Risk Assessment Engine

6.3 SUBMODULE LIST (v1.1)

Vulnerability Module contains 8 submodules:

Process Mapping Submodule

Lifecycle Mapping Submodule

Facility Mapping Submodule

Evidence & Media Submodule

Brown-Paper Style Markup Submodule

Severity & Exploitability Engine

Custodian Assignment & Governance

Integration Submodule (TVRE + RA)

6.4 VULNERABILITY DATA MODEL (DETAILED)

Every vulnerability object contains:

vulnerability_id
company_id
hierarchy_node
process_id (optional)
lifecycle_id (optional)
facility_id (optional)
category
sub_category
severity (0–1.0)
exploitability (0–1.0)
evidence_refs[]
description
status (active/archived)
custodian_team_id
created_at
updated_at
version

Optional Spatial Extensions

Coordinates (x, y) on facility map

Zone geometry

Image map references

6.5 PROCESS, LIFECYCLE & FACILITY MAPPING
1. Process Mapping

Maps the operational flow:

Input → Processing → Storage → Output → Distribution


Each process may have vulnerabilities:

Poor segregation

Lack of controls

Manual override opportunities

Exposure points

2. Lifecycle Mapping

Covers the end-to-end asset lifecycle:

Acquisition → Operation → Maintenance → Disposal


Each lifecycle phase has unique vulnerabilities.

3. Facility Mapping

Includes:

Physical locations

Camera coverage

Access control points

Restricted areas

Blind spots

Sensor locations

Operator workstations

6.6 CATEGORY & SUBCATEGORY CLASSIFICATION (v1.1)
Primary Categories

People

Process

Technology

Physical

Environmental

Organizational

External

Subcategories Example

People:

Training deficiency

Manpower shortage

Insider threat exposure

Technology:

CCTV blind spot

Alarm failure

Network segmentation gap

Process:

No SOP

SOP not followed

Weak segregation of duties

Physical:

Weak door

Unlocked perimeter

Poor lighting

6.7 BROWN-PAPER MARKUP SYSTEM (ADVANCED)

The Vulnerability Module includes a digital brown-paper workshop simulation:

Features

Upload PDF/map/photo

Draw shapes

Highlight areas

Add notes

Pin vulnerabilities

Group vulnerabilities

Color code severity

Use Cases

Facility walk-throughs

Process hazard analysis

Control room inspections

Plant vulnerability mapping

Everything is saved to the vulnerability object.

6.8 VULNERABILITY SCORING MODEL (v1.1)
Severity Score

How damaging the vulnerability is if exploited.

Scale: 0.00 – 1.00

Exploitability Score

How easy it is to exploit.

Scale: 0.00 – 1.00

Formula
vulnerability_score = severity × exploitability


Severity examples:

Missing access control → severe

Dim lighting → moderate

Missing policy → variable

Exploitability examples:

Open door → high

Badge misuse → medium

Policy gap → depends on context

6.9 THREAT–VULNERABILITY RELEVANCE (TVRE) INTEGRATION

TVRE determines whether a vulnerability can produce an unwanted event.

Inputs

Threat capability

Vulnerability exploitability

TTP alignment

Context

Drift adjustments

Behavior

If:

TVRE > threshold


→ UE candidate is generated.

If:

TVRE < threshold


→ No UE.

Auto-Reject Logic

Invalid combinations automatically rejected:

Natural disaster threat + Password reuse → invalid

Financial fraud threat + Rusted steel beam → invalid

6.10 CUSTODIAN TEAM ASSIGNMENT

Every vulnerability is owned by a custodian team:

Operations

Security

Maintenance

HR

IT

Environment

Engineering

Custodians:

Provide evidence

Review vulnerability status

Approve closure

Participate in RA workflow

6.11 VULNERABILITY WORKFLOWS
Workflow 1 — Create

Upload → Assign → Markup → Categorize → Score → Save.

Workflow 2 — Review

Custodian reviews → Approves or rejects → Adds evidence.

Workflow 3 — Closure

Vulnerability closed after PIT project completes.

Workflow 4 — Reopening

If assurance indicates deterioration, vulnerability reopens.

6.12 UI STRUCTURE (SUMMARY)
Vulnerability List

Filters

Severity icons

Status indicators

Evidence count

Linked threats

Linked UEs

Vulnerability Detail View

Maps

Markup panels

Evidence viewer

Severity and exploitability sliders

Hierarchy path

Brown-Paper View

Drawing tools

Notes

Hotspots

6.13 AI ASSISTANT BEHAVIOR

AI CAN:

Suggest categories

Analyze images

Extract vulnerabilities from text

Propose severity ranges

Highlight missing evidence

Flag likely exploitability ranges

AI CANNOT:

Approve vulnerabilities

Close vulnerabilities

Change scores

6.14 WATCHDOG RULES
Severity	Watchdog Trigger
Critical	Vulnerability without location
Critical	Severity ≥ 0.7 with no custodian
High	Evidence missing
High	Unlinked vulnerabilities
Medium	Outdated vulnerability (> 1 year)
Low	Description too short

Watchdogs produce:

Alerts

Escalations

Dashboard flags

6.15 EXPORT FORMATS

Supported:

Vulnerability PDF report

Vulnerability register CSV

Facility map overlays

JSON API export

6.16 INTEGRATION SUMMARY
Module	Integration Behavior
Threat	Maps via TTPs
TVRE	Computes relevance
UE	Generates UE sentence
RA	Vulnerability severity is used
WRAC	Prioritization input
PIT	Vulnerability resolution tied to projects
Remote Assurance	Controls directly tied to vulnerabilities
Incident Intel	Vulnerabilities triggered by incidents
END OF PART 6

(Vulnerability Module Deep Index)
📘 SRMF_MASTER_BUILD_REFERENCE_v1.0.md — PART 7
RISK ASSESSMENT MODULE — DEEP INDEX (v1.1 Architecture)

Authoritative Reference
Version 1.0 (Master Document), Module Version: v1.1

7. RISK ASSESSMENT MODULE — FULL DEEP INDEX
7.1 MODULE PURPOSE

The Risk Assessment Module (RA) transforms Unwanted Events into:

Inherent risk

Residual risk

Projected risk

Control strategies

ROI calculations

Appetite comparisons

PIT-ready implementation plans

It is the core analytical engine of the SRMF.

7.2 RISK ASSESSMENT ARCHITECTURE (ASCII)
            ┌───────────────────────────┐
            │  UNWANTED EVENT (UE)      │
            └───────────┬───────────────┘
                        ▼
               ┌─────────────────────────┐
               │  RISK ASSESSMENT ENGINE │
               ├─────────────────────────┤
               │ Likelihood (NIST)       │
               │ Impact (ERM)            │
               │ ALE Quantification      │
               │ Control Effectiveness   │
               │ Inherent Risk           │
               │ Residual Risk           │
               │ Projected Risk          │
               │ ROI                     │
               └────────────├────────────┘
                            ▼
                      ┌────────────┐
                      │   WRAC     │
                      └──────┬─────┘
                             ▼
                    ┌────────────────┐
                    │ Control Sets    │
                    └─────┬──────────┘
                          ▼
                      ┌──────────┐
                      │   PIT    │
                      └──────────┘
                              ▼
                       Remote Assurance

7.3 RA SUBMODULE LIST (v1.1)

Risk Assessment consists of 10 core submodules:

UE Context Submodule

NIST Likelihood Engine

ERM Impact Engine

ALE Quantification

Inherent Risk Calculator

Existing Control Evaluation

Proposed Control Evaluation

Residual Risk

Projected Risk

ROI Calculator & Control Strategy Engine

And 4 integration submodules:

WRAC Export

PIT Export

Remote Assurance Link

Live Risk Updating Engine

7.4 RA DATA MODEL (FULL)

Each risk object contains:

risk_id
company_id
ue_id
hierarchy_node
threat_id
vulnerability_id

# Likelihood (NIST)
initiation_likelihood
occurrence_likelihood
adverse_impact_likelihood
drift_adjustment
inherent_likelihood_score
inherent_likelihood_level

# Impact (ERM)
impact_financial
impact_safety
impact_environment
impact_operational
impact_regulatory
impact_score
impact_level

# ALE
asset_value
exposure_rate
annual_rate_occurrence
ale_value
ale_mapped_impact_level

# Controls
existing_controls[]
proposed_controls[]
control_effectiveness_current
control_effectiveness_projected

# Risk Values
inherent_risk_level
residual_risk_level
projected_risk_level
projected_remaining_risk_percentage

# ROI
expected_loss_prevented
cost_of_controls
roi_value

# Appetite
inherent_vs_appetite
residual_vs_appetite
projected_vs_appetite

# Workflow
status
owner_id
custodian_id
approver_id

# Versioning
erm_version
matrix_version
control_library_version
created_at
updated_at
version

7.5 UE CONTEXT SUBMODULE

The RA begins with the UE (Unwanted Event).

Data imported:

UE sentence

Threat metadata

Vulnerability metadata

TVRE

Hierarchy location

Evidence

AI responsibilities:

Summaries

Clarifications

Explanations

Suggesting improvements

AI restrictions:

Cannot rewrite UE without user approval

Cannot change metadata

7.6 NIST LIKELIHOOD ENGINE (v1.1)
Components

The NIST likelihood engine is divided into three components:

Initiation Likelihood (Adversarial)

Capability

Intent

Opportunity

TTP complexity

Occurrence Likelihood (Non-Adversarial)

Frequency

Environmental factors

Exposure

Adverse Impact Likelihood

Probability that harm is realized after initiation/occurrence

Each is scored 0–1.0.

FINAL LIKELIHOOD SCORE
likelihood_raw = weighted sum of 3 components
likelihood_adjusted = likelihood_raw + drift_adjustment
likelihood_normalized = clamp(0, 1.0)

Mapping to ERM

Mapped into:

Rare

Unlikely

Possible

Likely

Almost Certain

7.7 ERM IMPACT ENGINE (v1.1)

Impact is computed across:

Financial

Human safety

Environmental

Regulatory

Operational

Weighted per ERM settings.

Overall Impact Score
impact_score = weighted composite

Impact Level

Mapped from:

Impact Score

ALE override (if triggered)

ALE Impact Mapping

If ALE > threshold, impact level may escalate.

7.8 ALE QUANTIFICATION ENGINE

ALE is used if:

Asset value known

Exposure known

Annual rate of occurrence estimated

Formula:

ALE = asset_value × exposure_rate × ARO


Mapped into:

Minor

Moderate

Major

Severe

Critical

ALE is optional but recommended.

7.9 INHERENT RISK CALCULATOR
inherent_risk = matrix[likelihood_level][impact_level]

Example

Likelihood: Likely
Impact: Major

→ Inherent Risk: High (red)

Stored as:

Score

Level

Band

Color

7.10 EXISTING CONTROL EVALUATION (v1.1)

Existing controls evaluated using:

Design Strength

Implementation Quality

Availability

Efficacy formula:

control_efficacy = (design × implementation × availability)


Aggregated across controls:

total_current_effectiveness = 1 - ∏(1 - each_control_efficacy)

Capped at 90%

No control environment can exceed 90% effectiveness.

7.11 RESIDUAL RISK CALCULATION
residual_likelihood = inherent_likelihood × (1 - effectiveness)
residual_impact = inherent_impact × (1 - effectiveness)
residual_risk = matrix[residual_likelihood][residual_impact]


Residual risk must:

Never exceed inherent

Always be logic-checked

7.12 PROPOSED CONTROLS EVALUATION

Proposed controls evaluated similarly:

projected_effectiveness = calculated as above but using proposed controls


Combined:

total_effectiveness = current_effectiveness + proposed_effectiveness

Capped at 90% again.
7.13 PROJECTED RISK
projected_likelihood = inherent_likelihood × (1 - total_effectiveness)
projected_impact = inherent_impact × (1 - total_effectiveness)
projected_risk = matrix[projected_likelihood][projected_impact]


Displayed in WRAC as:

Heatmap coordinate

Heatmap descriptor

Risk value

Remaining risk %

7.14 ROI MODEL
expected_loss_prevented = ALE_inherent - ALE_projected
roi = (expected_loss_prevented - control_cost) / control_cost


ROI expressed as:

Percentage

Positive = beneficial

Negative = not viable

7.15 APPETITE COMPARISON ENGINE

Appetite is applied three times:

Inherent vs appetite

Residual vs appetite

Projected vs appetite

Flags:

Within appetite

Slightly above appetite

Breach

Critical breach

Triggers:

If inherent > appetite → escalate

If projected > appetite → controls insufficient

7.16 CONTROL STRATEGY ENGINE (v1.1)

Creates:

Immediate controls

Medium-term

Long-term

“Control sets”

Each control:

Has cost

Has dependencies

Has efficacy

Belongs to category (Eliminate, Sub, Engineer, Admin, PPE)

Control sets:

Bundled controls

Applied to multiple risks

Exportable to PIT

7.17 WRAC EXPORT SUBMODULE

Outputs:

Priority risks

Projected risks

Top 10 risks

Top 10 projected

Top 10 ROI

PUE identification

Control sets

Costing

Mitigation plan

7.18 PIT EXPORT SUBMODULE

A RA becomes a PIT project when:

Proposed controls approved

ROI acceptable

Appetite breach resolved

PIT export includes:

Project scope

Tasks

Costs

Dependencies

Evidence requirements

Timeline

7.19 REMOTE ASSURANCE LINK

Remote Assurance updates:

Control availability

Failures

System uptime

Actual vs planned effectiveness

Live residual risk:

live_risk = inherent × (1 - effective_control_status)

7.20 LIVE RISK UPDATING ENGINE

Sources:

Remote assurance

PIT completion

Incident module

Threat drift updates

Maintains:

Live risk

Live appetite comparison

Risk spikes

Escalations

7.21 RA WORKFLOWS
Workflow 1 — Draft

Analyst drafts → AI supports → Custodian reviews.

Workflow 2 — Approval

Custodian → Risk Owner → Final sign-off.

Workflow 3 — Export to WRAC

All RAs populate WRAC.

Workflow 4 — Export to PIT

Selected controls create PIT project.

Workflow 5 — Live Update

Assurance + PIT modify RA over time.

7.22 AI PERMITTED ACTIONS

AI CAN:

Suggest controls

Calculate likelihood components

Generate explanations

Highlight anomalies

Map costs

Recommend strategies

AI CANNOT:

Approve assessments

Modify scores without review

Override ERM

7.23 WATCHDOG RULES (v1.1)
Severity	Trigger
Critical	Projected > Inherent
Critical	Residual > Inherent
Critical	Appetite breach without escalation
High	Missing controls
High	No custodian
Medium	No ALE mapping
Low	Missing evidence
7.24 RA VERSIONING

RA must store:

ERM version

Threat version

Vulnerability version

Control library version

Matrix version

Historical RAs unaffected by later changes.

END OF PART 7

(Risk Assessment Module Deep Index)
📘 SRMF_MASTER_BUILD_REFERENCE_v1.0.md — PART 8
WRAC + CONTROL LIBRARY + CONTROL EFFICACY — Deep Index (v1.1 Architecture)

Authoritative Reference
Version 1.0 (Master Document)
Modules Included:

WRAC v1.1

Control Library v1.1

Control Efficacy Engine v1.1

TABLE OF CONTENTS (PART 8)

WRAC (v1.1) — Purpose & Architecture

WRAC Data Model

WRAC UI, Filters, and Sorting

WRAC Export Models

WRAC Integration with RA, PIT, Assurance

PUE (Priority Unwanted Event) Logic

Control Library (v1.1) — Purpose & Architecture

Control Categories, Hierarchies & Metadata

Control Dependencies

Control Costing Model

Control Evidence Model

Control Efficacy Engine (v1.1)

Control Efficacy Formulae

Control Grouping → Control Sets

Control Implementation Sequencing

Integration with Live Risk Dashboard

Watchdog Rules for WRAC & Controls

Versioning & Governance

Future Extensions (Bowtie, Assurance AI, Syndicate Library)

8.1 WRAC MODULE (v1.1) — PURPOSE

WRAC is the Operational View of the risk assessment system.

It acts as the:

Summary of all RAs

Planning tool

Sorting and filtering engine

Control strategy builder

PUE identification platform

Implementation readiness table

High-level risk dashboard

Export module for PIT & reporting

WRAC transforms analytical results (RA) into actionable plans.

8.2 WRAC ARCHITECTURE (ASCII)
              ┌───────────────────────┐
              │   RISK ASSESSMENTS    │
              └───────────┬───────────┘
                          ▼
            ┌─────────────────────────────┐
            │            WRAC             │
            ├─────────────────────────────┤
            │ Inherent Risk                │
            │ Residual Risk                │
            │ Projected Risk               │
            │ ROI                          │
            │ Control Strategy Overview     │
            │ PUE Identification            │
            │ Priority Sort                 │
            └──────────┬────────────────────┘
                       ▼
              ┌──────────────┐
              │    PIT        │
              └──────┬────────┘
                     ▼
           ┌────────────────────┐
           │ Remote Assurance   │
           └────────────────────┘

8.3 WRAC DATA MODEL (DETAILED)

Each WRAC row contains:

wrac_id
company_id
risk_id
ue_id
hierarchy_path[]
threat_name
vulnerability_name

# RISK SCORES
inherent_likelihood_level
inherent_impact_level
inherent_risk_level
residual_risk_level
projected_risk_level

# COST & ROI
ale_inherent
ale_projected
expected_loss_prevented
control_cost_total
roi

# CONTROL STRATEGY
existing_controls[]
proposed_controls[]
control_set_ids[]
control_dependencies[]
control_status_current
control_status_projected

# WORKFLOWS
pue_flag
bowtie_required_flag
pit_ready_flag
task_progress_percentage

# METADATA
owner
custodian
created_at
updated_at
version

8.4 WRAC UI LAYOUT (SUMMARY)

Columns include:

Risk ID

UE summary

Current Controls

Proposed Controls

Inherent Risk

Residual Risk

Projected Risk

ROI

Cost

PUE

Bowtie

PIT Status

Filters (Architecture Component, Risk Rating Level, ROI band, etc.)

8.5 WRAC FILTERS & SORTING
Filters (v1.1)

Company

Hierarchy node

Risk level (Inherent / Residual / Projected)

ROI threshold

Cost range

Control group

PUEs only

Bowtie candidates

Top 10 / Top 20 / Top 50 / Top 100

Unmitigated

Partially mitigated

Fully mitigated

Sorting

Highest risk first

Highest ROI

Highest cost

Fastest implementation

Most dependencies

PUE priority

Unassigned owner

By control category

This gives the user unrivalled analytical flexibility.

8.6 WRAC → RA LINKAGE

Every WRAC row is a direct projection of:

Inherent risk from RA

Residual risk from RA

Projected risk from RA

Control strategy from RA

ROI from RA

Appetite comparison from RA

WRAC never recalculates risk.
It only displays and sorts risk.

8.7 WRAC → CONTROL STRATEGY

WRAC is the primary UI where the user:

Views control sets

Adds or removes proposed controls

Sees how controls affect projected risk

Sees ROI

Groups controls into implementation units

Approves final mitigation plans

8.8 PUE (PRIORITY UNWANTED EVENT) LOGIC

A risk becomes a PUE if:

Residual risk > appetite

Projected risk > appetite

Control environment contains critical controls

Residual remains high despite controls

Uncertainty indicators exist (missing evidence, drift ≥ threshold)

PUE flags:

Red indicator in WRAC

Bowtie required

Escalation workflow

Critical control monitoring in Assurance

PUEs flow into:

Bowtie Module (future)

Critical Control Register

Advanced analytics

8.9 CONTROL LIBRARY (v1.1) — PURPOSE

The Control Library is the single, global catalogue of all controls in the ISMS.

Standardized naming

Standardized definitions

Control hierarchy (Eliminate → Substitute → Engineering → Admin → PPE)

Costing

Failure modes

Dependencies

Evidence requirements

AI mapping to threats & vulnerabilities

This enables deterministic matching between:

Threats

Vulnerabilities

UEs

Risks

Controls

PIT tasks

Remote assurance monitoring

8.10 CONTROL LIBRARY ARCHITECTURE (ASCII)
┌──────────────────────────────────────────────────────┐
│                  CONTROL LIBRARY                      │
├──────────────────────────────────────────────────────┤
│ Control Definitions                                   │
│ Categories & Subcategories                            │
│ Failure Modes                                         │
│ Dependencies                                          │
│ Evidence Rules                                        │
│ Costing Models                                        │
│ Efficacy (Base Values)                                │
└───────────────┬────────────────────────────────────────┘
                ▼
         Control Efficacy Engine
                ▼
         RA Effectiveness Calculation
                ▼
         WRAC + PIT + Assurance

8.11 CONTROL CATEGORIES & SUB-CATEGORIES
Primary control categories:

Elimination

Substitution

Engineering Controls

Administrative Controls

PPE (Personal Protective Equipment)

Subcategories Example (Engineering):

CCTV cameras

Access control systems

Fencing

Alarm systems

SCADA controls

IoT sensors

Black-screen analytics

Machine-learning alerts

Each control entry includes:

Definition

When used

Strengths

Weaknesses

Evidence requirements

Typical failure points

8.12 CONTROL DEPENDENCIES (CRITICAL FOR SRMF)

Controls often rely on other controls to be effective.

Example

“Camera coverage” depends on:

Power stability

Network availability

Surveillance operator

Recording system

AI analytics (if configured)

Dependency types:

Hard dependency (mandatory)

Soft dependency (recommended)

Contextual dependency (specific scenarios)

SRMF automatically checks dependencies:

In RA

In WRAC

In PIT

In Assurance

8.13 CONTROL COSTING MODEL

Two cost levels:

1. Preliminary Costing (75% Accuracy)

Used during RA and WRAC.
Based on:

Control category

Estimated complexity

Market price profiles

Labor

Materials

2. Actual Costing (Final Pricing)

Triggered when project is exported to PIT.

Requests quotes

Approvals required

Procurement process

Timeline estimation

Both are stored in the control object.

8.14 CONTROL EVIDENCE MODEL

Controls require evidence:

Photos

Checklists

Logs

System uptime/alarm history

CCTV snapshots

Maintenance reports

Test reports

Evidence is:

Attached

Versioned

Required for “active” status

Assurance module checks evidence automatically (where possible).

8.15 CONTROL EFFICACY ENGINE (v1.1)

This is the mathematical engine that determines how much a control reduces risk.

Each control evaluated across:

Design Strength

Implementation Quality

Availability

Base Formula
control_efficacy = design × implementation × availability

Aggregated Control Environment
total_effectiveness = 1 - ∏(1 - control_efficacy_i)

Hard Cap

90% maximum effectiveness
No controls can eliminate 100% of risk.

8.16 CONTROL SETS (GROUPINGS)

A control set is a logical group of controls that mitigate:

a specific vulnerability

a specific threat vector

a collection of risks

Examples:

“Surveillance Hardening Set”:

Camera coverage

3-tier monitoring

Black-screen AI

System availability monitoring

“Access Control Integrity Set”:

Credential vetting

Anti-passback

Door hardening

Segregation of duties

Control sets are essential for:

RA → WRAC

WRAC → PIT

Batch implementation planning

ROI across multiple risks

8.17 CONTROL IMPLEMENTATION SEQUENCING

Controls are sequenced as:

Implement now

Implement medium-term

Implement future

Conditional on other controls

The RA and WRAC modules decide the classification.
PIT handles actual implementation.

8.18 WRAC → LIVE RISK DASHBOARD (INTEGRATION)

Live Risk Dashboard uses:

Control availability (from Assurance)

Control completion (from PIT)

Threat drift (from Threat module)

Vulnerability updates

UE changes

Real-time control efficacy recalculations

WRAC values dynamically update.

8.19 WRAC WATCHDOG RULES
Severity	Trigger
Critical	PUE without Bowtie assignment
Critical	Projected risk > Residual risk
High	Missing control costing
High	Control dependency missing
Medium	Incomplete WRAC row
Low	Control group mismatch
8.20 CONTROL LIBRARY WATCHDOG RULES
Severity	Trigger
Critical	Control with missing category
High	No efficacy values
Medium	No evidence rules
Low	Missing cost estimate
8.21 VERSIONING & GOVERNANCE

Control Library and Efficacy Engine must store:

Version

Change logs

Update reasons

Cross-module impact scans

Updating control library must:

Recalculate RA

Recalculate WRAC

Recalculate projected risk

8.22 FUTURE EXTENSIONS
Bowtie Module

WRAC will directly feed bowtie risk assessments.

Remote Assurance AI

Will verify control availability using:

CCTV analytics

Access control logs

Alarm system uptimes

Syndicate Control Library

Controls targeted specifically at organized crime patterns.

END OF PART 8

(WRAC + Control Library + Control Efficacy Deep Index)
📘 SRMF_MASTER_BUILD_REFERENCE_v1.0.md — PART 9
PIT + REMOTE ASSURANCE + INCIDENT & INTELLIGENCE (v1.1 Architecture & Future Spec)

Authoritative Reference
Version 1.0 (Master Document)
Modules Included:

PIT v1.1 (final design)

Remote Assurance v1.0 (design-ready specifications)

Incident & Intelligence Module v1.0 (design-ready specifications)

TABLE OF CONTENTS (PART 9)

Purpose of Tier-3 Risk Operationalization Layer

PIT (Project Implementation Tracker) — Deep Index

PIT Data Model

PIT UI & Workflows

PIT Integration with RA, WRAC, Assurance

PIT Watchdogs, KPIs, and Live Updating

Remote Assurance Module (v1.0) — Purpose & Architecture

Control Availability Monitoring (CAM) Specification

System Performance Monitoring (SPM) Specification

Digital Checklist & Manual Assurance Submodule

Control Failure Modes (CFM) Engine

Control Availability Scores → Live Residual Risk Calculation

Remote Assurance UI, Dashboard & KPIs

Incident & Intelligence Module (v1.0)

Intelligence Ingestion Pipeline

Broadcast Mechanism to Threat / Vulnerability / RA

Cross-Module Integration Map

Versioning & Governance

Future Extensions (Digital Twins, Predictive Analytics)

9.1 PURPOSE OF THE TIER-3 LAYER

Tier-3 consists of:

1. PIT — ensuring controls are implemented.

This closes the loop between RA → WRAC → Action.

2. Remote Assurance — ensuring controls remain available & effective.

This converts controls into live risk indicators.

3. Incident & Intelligence — detecting new risks, threats, and vulnerabilities.

This ensures early warning and automatic RA updates.

Together, these modules:

Turn analyses into actions

Turn actions into verified improvements

Turn verification into live risk analytics

Turn intelligence into RA recalculations

This is the backbone of a dynamic, living SRMF.

9.2 PIT (PROJECT IMPLEMENTATION TRACKER) — DEEP INDEX

The PIT system transforms control strategies into trackable implementation projects.

PIT receives inputs from:

WRAC

RA

Control Library

Cost Models

Owner Approvals

PUE escalation workflow

PIT exports to:

Remote Assurance

Live Risk Dashboard

Bowtie escalation

Auditors

Executive dashboards

9.3 PIT ARCHITECTURE (ASCII)
                     RISK ASSESSMENT
                       (Proposed Controls)
                               │
                               ▼
                       WRAC (v1.1)
                         (Mitigation Plan)
                               │
                               ▼
             ┌───────────────────────────────────────┐
             │         PROJECT IMPLEMENTATION         │
             │                TRACKER                 │
             ├───────────────────────────────────────┤
             │ Project Scoping                        │
             │ Task Definition                        │
             │ Dependency Mapping                     │
             │ Costing                                │
             │ Timeline                               │
             │ Evidence Capture                       │
             │ Progress Tracking                      │
             └─────────────────┬──────────────────────┘
                               ▼
                      Remote Assurance
                               ▼
                     Live Risk Dashboard
                               ▼
                    Executive Risk Reporting

9.4 PIT DATA MODEL (DETAILED)

Each PIT project includes:

pit_project_id
company_id
risk_ids[]
control_ids[]
control_set_ids[]
cost_estimates_preliminary
cost_estimates_actual
approval_workflow[]
task_list[]
dependencies[]
evidence[]
progress_percentage
owner_id
custodian_id
status (draft, active, paused, complete, verified)
timeline_start
timeline_end
estimated_completion_date
created_at
updated_at
version


Each PIT task includes:

task_id
task_name
description
dependent_task_ids[]
expected_duration
progress
assigned_to
evidence_required[]
evidence_uploaded[]
verification_status
failure_modes[]
pit_project_id

9.5 PIT WORKFLOWS
Workflow 1 — Creation

RA → WRAC → create PIT scope → auto-generate tasks from controls.

Workflow 2 — Approval

Control sets requiring financial expenditure trigger approval chain.

Workflow 3 — Execution

Tasks executed, tracked in real-time.

Workflow 4 — Evidence & Verification

Photos, logs, tests, system outputs uploaded.

Workflow 5 — Completion

Tasks must pass verification rules before closure.

Workflow 6 — Integration

Completed controls push updates into the Remote Assurance module.

9.6 PIT UI (SUMMARY)

Project list view

Gantt timeline

Control dependency graphs

Cost overview

Evidence upload

Verification workflows

Progress badges

Hierarchy mapping (Company → Plant → Zone → Area)

9.7 PIT WATCHDOG RULES
Severity	Trigger
Critical	Project overdue > 30 days
Critical	No progress in 14 days
High	Missing evidence for completed task
High	No assigned owner
Medium	Cost variance > 25%
Low	Repeated task re-openings
9.8 PIT KPIs

% projects on time

% projects exceeding cost

Average task duration

Average controls delivered per month

Control set completion velocity

Risk reduction impact per quarter

9.9 REMOTE ASSURANCE MODULE (v1.0) — PURPOSE

Remote Assurance continuously monitors:

Control availability

Control reliability

Control failure modes

System performance

Evidence completeness

Manual checks (fallback)

Its job is to maintain live risk accuracy after controls are implemented.

Remote Assurance feeds:

Live residual risk engine

WRAC updates

RA updates

PUE escalation logic

Executive dashboards

9.10 REMOTE ASSURANCE ARCHITECTURE (ASCII)
                 ┌───────────────────────────┐
                 │     REMOTE ASSURANCE      │
                 ├───────────────────────────┤
                 │ Control Availability       │
                 │ System Performance         │
                 │ Evidence Validation        │
                 │ Alerts & Escalations       │
                 │ Health Scores              │
                 │ AI Failure Detection        │
                 └─────────────┬─────────────┘
                               ▼
                        Live RA Engine
                               ▼
                      Executive Dashboards

9.11 CONTROL AVAILABILITY MONITORING (CAM)
For controls with electronic signals:

Examples:

Camera uptime

Recording system uptime

Access control system health

Alarm panel online status

Network segment availability

Power supply uptime

Intrusion detection trigger logs

The system:

Receives telemetry

Creates availability score

Maps to control efficacy

Updates live residual risk

9.12 SYSTEM PERFORMANCE MONITORING (SPM)

Monitors:

Storage retention

FPS (frames per second) in cameras

Alarm response times

Network latency

Operator station availability

AI analytic uptime

These modify:

Control effectiveness

Live residual risk

9.13 DIGITAL CHECKLIST MODULE (Manual Assurance)

For controls that cannot be electronically monitored:

Lock integrity

Manual patrols

Physical inspections

Validating SOP compliance

Checking lighting

Checking signage

Digital checklist features:

Scheduled recurrence

Dual-person sign-off

Photo & video attachment

GPS validation

Timestamp locks

If manual checks fail → risk increases.

9.14 CONTROL FAILURE MODES (CFM) ENGINE

Each control contains a predefined failure profile:

Examples:

CCTV: blind spot, recording failure, power drop

Alarm: false negatives, sensor damage

Access Control: card cloning, door tampering

SOP: non-compliance, incorrect execution

PPE: not worn, expired

Failures:

Are detected

Reduce efficacy

Trigger watchdogs

Escalate RAs

9.15 LIVE RESIDUAL RISK CALCULATION (Remote Assurance → RA)

Formula:

live_effectiveness = control_current_effectiveness × availability_score × implementation_score
live_residual = inherent × (1 - live_effectiveness)


Live residual risk overrides:

Residual risk calculated during RA

Projected risk (if controls fail)

Displayed on:

WRAC

Risk dashboard

Executive summaries

9.16 REMOTE ASSURANCE UI & KPIs
KPIs include:

Control availability %

Control failure frequency

System uptime %

Real-time risk

Residual risk drift

Control verification compliance

PUE early warning index

UI areas:

Control Health Dashboard

Failure Mode Alerts

System Performance Overview

Evidence Compliance Board

AI anomaly detection panel

9.17 INCIDENT & INTELLIGENCE MODULE (v1.0) — PURPOSE

This module provides:

Early warning

Real-time threat intelligence

Incident ingestion

Automatic threat/vulnerability generation

Drift recalculation

UE seed generation

RA recalculation triggers

It closes the final gap in the SRMF cycle.

9.18 INCIDENT ARCHITECTURE (ASCII)
         ┌──────────────────────────────────┐
         │        INCIDENT & INTELLIGENCE   │
         ├──────────────────────────────────┤
         │ Internal Incidents                │
         │ Crime Reports                     │
         │ External Intelligence             │
         │ Social Indicators                 │
         │ Syndicate Signals                 │
         │ Sensor Anomalies                  │
         └───────┬────────────────────────────┘
                 ▼
       Threat Module (Drift + Scoring)
                 ▼
      Vulnerability Module (New Findings)
                 ▼
       RA Engine (Recalculation Triggers)

9.19 INTELLIGENCE INGESTION PIPELINE

Sources:

SAPS / Law enforcement bulletins

Crime statistics

OSINT feeds

Internal reports

Access logs

Alarm logs

CCTV anomaly AI

Social media indicators

Syndicate behavior patterns

Actions:

Generate new threats

Increase drift

Suggest new vulnerabilities

Trigger UE generation

Recalculate RA

9.20 BROADCAST MECHANISM

After processing:

Threat module receives:

Drift adjustments

Actor capability updates

TTP changes

Vulnerability module receives:

Potential new vulnerabilities

Confirmation prompts

RA receives:

Update required flags

Residual recalculation triggers

WRAC receives:

Live risk updates

PUE recalculation flags

PIT receives:

Prioritization changes

9.21 CROSS-MODULE INTEGRATION MAP (ASCII)
Threat ↔ Vulnerability ↔ UE ↔ RA ↔ WRAC ↔ PIT ↔ Remote Assurance ↔ Incident & Intel
▲                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘


This creates the SRMF closed-loop system.

9.22 VERSIONING & GOVERNANCE

All modules must create version logs when:

Controls change

Threats change

Vulnerabilities change

Drift recalculates

Control uptime changes

Evidence changes

Incidents occur

All historical risk calculations must remain immutable.

9.23 FUTURE EXTENSIONS

Digital Twin of each facility

Real time camera coverage

Live risk hotspots

Predictive Threat Analytics

Forecasting 30-day risk trends

Generative Bowtie Engine

Auto-drafts bowtie diagrams

Hazard → Top event → Threats → Consequences

Critical Control Register with AI availability forecasting

Control Behavior Simulation

“What if camera offline?”

“What if 2 controls fail?”

END OF PART 9

(PIT + Remote Assurance + Incident & Intelligence Deep Index)
📘 SRMF_MASTER_BUILD_REFERENCE_v1.0.md — PART 10
MASTER INTEGRATION MAP & NAVIGATION BLUEPRINT (v1.1)

Authoritative Reference
Version 1.0 (Master Document)
Purpose: Provide a single, unambiguous architecture describing how all SRMF modules interact.

TABLE OF CONTENTS (PART 10)

SRMF System-of-Systems Architecture

Global Data Flow (End-to-End)

Master Integration Map (ASCII + Layered)

Master Navigation Blueprint (UI-Level Routing)

SRMF AI Routing Specification

Master Data Model (Unified Entities & Crosslinks)

Cross-Module Versioning Architecture

Governance & Approval Hierarchy

Master Watchdog Framework

Master Audit & Traceability Engine

Executive Dashboards Integration

Future Expansion Pathways

The SRMF “Operating Rhythm” (How the ecosystem lives day-to-day)

10.1 THE SRMF SYSTEM-OF-SYSTEMS ARCHITECTURE

SRMF is not a single module.
It is a digital ecosystem, consisting of:

Tier 1: Foundational Frameworks

ERM Framework

Hierarchy Framework

Risk Appetite

Control Library

Standards & True North

User roles & governance

Tier 2: Analytical Engines

Threat Module

Vulnerability Module

UE Generator

RA Engine

Control Efficacy Engine

Tier 3: Operational Execution

WRAC

PIT

Remote Assurance

Incident & Intelligence

Bowtie (future)

Baseline/WRAC baseline RA (future)

Tier 4: Intelligence & Reporting

Live Risk Dashboard

Predictive Analytics (future)

Executive Dashboards

Compliance Reporting

Governance Metrics

Tier 5: Integration & Extensibility

API Layer

Machine Learning Layer

Digital Twin connectors

Security telemetry

ERP/SCADA/Access Control feeds

Camera analytics AI

Everything below is built around this system.

10.2 GLOBAL END-TO-END DATA FLOW

(The Entire SRMF in a Single Diagram)

                   ┌──────────────────────────┐
                   │        THREATS           │
                   └───────────┬──────────────┘
                               ▼
                         ┌───────────┐
                         │VULNERABLE │
                         │PROCESS/   │
                         │FACILITY   │
                         └─────┬─────┘
                               ▼
                      ┌────────────────┐
                      │   UE ENGINE    │
                      └──────┬─────────┘
                             ▼
                   ┌──────────────────────┐
                   │  RISK ASSESSMENT     │
                   ├──────────────────────┤
                   │ Inherent Risk        │
                   │ Residual Risk        │
                   │ Projected Risk       │
                   │ ROI                  │
                   │ Appetite Comparison  │
                   └─────────┬────────────┘
                             ▼
                   ┌──────────────────────┐
                   │         WRAC         │
                   └─────────┬────────────┘
                             ▼
                   ┌──────────────────────┐
                   │  CONTROL STRATEGY    │
                   │  & COSTING           │
                   └─────────┬────────────┘
                             ▼
                   ┌──────────────────────┐
                   │         PIT          │
                   ├──────────────────────┤
                   │ Control Deployment    │
                   │ Evidence Capture      │
                   │ Timeline              │
                   │ Dependencies          │
                   └─────────┬────────────┘
                             ▼
                   ┌──────────────────────┐
                   │  REMOTE ASSURANCE    │
                   ├──────────────────────┤
                   │ Control Availability  │
                   │ Failure Modes         │
                   │ System Uptime         │
                   │ Manual Checklists     │
                   └─────────┬────────────┘
                             ▼
                       LIVE RESIDUAL RISK
                             │
                ┌────────────┴──────────────┐
                ▼                            ▼
          EXECUTIVE DASHBOARDS          INCIDENT & INTEL
                                              │
                                              ▼
                                           THREATS

10.3 MASTER INTEGRATION MAP

(Full Layered ASCII Architecture)

This map shows ALL modules, their relationships, and their order.

┌────────────────────────────────────────────────────────────────────────────┐
│                           MATURION SRMF ISMS                               │
├─────────────────────────────┬──────────────────────────────────────────────┤
│         GOVERNANCE LAYER   │ AI DECISION LAYER (CONTROLLED)               │
├─────────────────────────────┼──────────────────────────────────────────────┤
│  ERM Framework              │  AI Explanation                              │
│  Hierarchy Framework        │  AI Suggestion                               │
│  User Roles                 │  AI Validation                               │
│  Appetite Settings          │  AI Drafting                                 │
│  Policy/Standards           │  AI Prediction (limited)                     │
├─────────────────────────────┴──────────────────────────────────────────────┤
│                          ANALYTICAL LAYER                                  │
│   Threat Module  ←→  Vulnerability Module  ←→  UE Generator                │
│                              ↓                                             │
│                        Risk Assessment Engine                              │
│      Likelihood Engine | Impact Engine | ALE Engine | Controls Engine      │
├────────────────────────────────────────────────────────────────────────────┤
│                         OPERATIONAL LAYER                                  │
│                          WRAC  ←→  Control Sets                             │
│                              ↓                                             │
│                          PIT (Implementation)                               │
│                              ↓                                             │
│                     Remote Assurance (Control Health)                      │
│                              ↓                                             │
│                         Live Residual Risk                                 │
├────────────────────────────────────────────────────────────────────────────┤
│                         INTELLIGENCE LAYER                                 │
│     Incident Module ←→ Intelligence Module ←→ Threat Drift                 │
│                              ↓                                             │
│                      Automated RA Recalculation                            │
├────────────────────────────────────────────────────────────────────────────┤
│                         REPORTING LAYER                                    │
│                   Live Risk Dashboard | Executive Reports                  │
└────────────────────────────────────────────────────────────────────────────┘

10.4 MASTER NAVIGATION BLUEPRINT

(Full User Journey Across the Entire SRMF)

PHASE 1: BUILD CONTEXT

Define ERM

Define hierarchy

Load Control Library

Enable appetite thresholds

PHASE 2: IDENTIFY EXPOSURES

Create threats

Map vulnerabilities

Generate UEs (AI-assisted)

PHASE 3: ANALYZE RISK

Run RA

Evaluate controls

Calculate ROI

Compare with appetite

PHASE 4: PRIORITIZE

WRAC presents “business view”

Identify PUEs

Build control strategy

PHASE 5: IMPLEMENT

Export control sets to PIT

Projects executed

Evidence uploaded

Controls verified

PHASE 6: MONITOR

Remote Assurance monitors control health

Automatic adjustments to live residual risk

Incident module creates new risk triggers

PHASE 7: GOVERN

Executive dashboards show trends

Governance audits

Continuous improvement

10.5 SRMF AI ROUTING SPECIFICATION

(This is essential for Foreman & CoPilot orchestration)

The SRMF AI layer must follow strict boundaries.

AI CAN:

Analyze threats

Suggest vulnerabilities

Draft UE sentences

Calculate likelihood values

Propose controls

Compute risk values

Interpret telemetry (Assurance)

Predict failure modes

Summarize RAs

Draft PIT task structures

Detect anomalies in systems

Recommend focus areas to executives

AI CANNOT:

Approve RA

Modify ERM

Grant PIT completions

Change risk appetite

Change governance settings

Conceal watchdog failures

Override a human decision

AI ALWAYS:

Logs every action

Requires human sign-off for major steps

Must reference SRMF rules when providing reasoning

Must justify all recommendations

10.6 MASTER DATA MODEL

(Complete Unified Entity Relationship Overview)

Core Entities

Company

Hierarchy Node

Threat

Vulnerability

UE

Risk

Control

Control Set

PIT Project

PIT Task

Assurance Signal

Incident

Intelligence Feed

Crosslinks

Threat ↔ Vulnerability (TVRE logic)

UE links Threat + Vulnerability

RA links UE + Controls + ERM

WRAC links RA + Controls + ROI

PIT links Controls + RA

Assurance links Controls + PIT

Incidents update Threats & RA

This unified model ensures every module speaks the same data language.

10.7 MASTER VERSIONING ARCHITECTURE

Every major module maintains its own version, but a global SRMF version also exists.

Version Types

ERM version

Threat library version

Vulnerability mapping version

Control library version

Efficacy model version

RA version

WRAC version

PIT version

Assurance version

Intelligence version

Version Conflicts

If a control library update changes efficacy:

RA recalculates

WRAC updates

PIT re-evaluates

Live residual adjusts

THERE IS NEVER A “silent” update.

10.8 GOVERNANCE & APPROVAL HIERARCHY

Hierarchy defines:

Who approves RA

Who approves WRAC

Who approves controls

Who approves budgets

Who verifies evidence

Who approves PIT projects

Who accepts completed controls

Who signs off residual risk

Governance roles include:

Analyst

Custodian

Risk Owner

Approver

PIT Manager

Assurance Officer

Auditor

Executive

Each step MUST be human-verified.

10.9 MASTER WATCHDOG FRAMEWORK

Watchdog layers:

Threat Watchdog

Vulnerability Watchdog

RA Watchdog

WRAC Watchdog

PIT Watchdog

Assurance Watchdog

Incident Watchdog

Severity levels:

Informational

Low

Medium

High

Critical

Critical watchdog events require:

Forced escalation

Executive notification

System locking (certain actions)

10.10 MASTER AUDIT & TRACEABILITY ENGINE

Everything is logged:

RA changes

UE modifications

Threat drift updates

PIT task updates

Evidence uploads

Assurance failures

Intelligence triggers

AI recommendations

AI reasoning snippets

Auditors can reconstruct:

Any risk

Any control

Any timeline

Any evidence

Any decision

Any change

10.11 EXECUTIVE DASHBOARDS INTEGRATION

Dashboards show:

Top risks

Risk over time

Risk vs appetite

PUE list

Control health

Control failures

Incident heatmaps

Implementation progress

ROI summary

Future risk forecasts (AI)

Executives see ONE system, not 10 modules.

10.12 FUTURE EXPANSION PATHWAYS

The SRMF architecture allows seamless addition of:

Digital Twin

AI-driven patrol planning

Predictive threat modeling

Climate risk integration

ESG risk scoring

Workforce competency risk

Integrated emergency response planning

Enterprise security command center (ESCC) integration

Autonomous audit systems

All without breaking current modules.

10.13 THE SRMF “OPERATING RHYTHM”

This describes how the system behaves daily.

Daily

Assurance checks

Control failures detected

RA updates

Watchdogs processed

Weekly

WRAC refresh

PIT project updates

Internal incident imports

Monthly

Executive dashboard

Threat drift recalculation

Vulnerability reviews

Quarterly

ERM calibration

Control library audit

Governance review

Training

Yearly

Full SRMF audit

Major version upgrade

Strategic risk review

This rhythm ensures SRMF remains alive, not a static document.

END OF PART 10

(MASTER INTEGRATION MAP & NAVIGATION BLUEPRINT)

✔ SRMF MASTER BUILD REFERENCE COMPLETED

You now have:

Threat v1.1

Vulnerability v1.1

RA v1.1

WRAC v1.1

PIT v1.1

Remote Assurance v1.0

Incident & Intelligence v1.0

Master Integration Map v1.1

True North v1.2

Build Philosophy v1.1

This is a world-class, enterprise-grade SRMF architecture ready for:

Foreman

CoPilot

GitHub

Development

Auditing

Executive approval
📘 SRMF_MASTER_BUILD_REFERENCE_v1.0.md — PART 11
SRMF UI NAVIGATION & WIZARD FLOWS (v1.0)

Purpose: Define a consistent, minimalistic, wizard-driven UI across all SRMF modules so that the system feels like one app, not a patchwork.

11.1 GLOBAL UI SHELL

All SRMF modules run inside a shared ISMS shell:

Top Bar

Left: Maturion logo + environment (Prod / UAT)

Center: Module title (ERM, Threats, RA, WRAC, PIT, etc.)

Right: User profile, role, notifications bell, AI Assistant button

Left Sidebar (Primary Navigation)

ISMS Home

Risk Management

ERM

Threats

Vulnerabilities

Risk Assessment

WRAC

PIT

Remote Assurance

Incident & Intelligence

Other Modules

Course Crafter

Policy Builder

Auditor App

Skills Portal

Admin

Company Settings

Hierarchy

Control Library

User & Roles

Watchdog Console

Logs & Audit

Main Content Area

Module screens (lists, details, wizards, dashboards)

Always a split structure:

Primary pane (data)

Context pane (AI, details, hints, help)

Bottom Status Strip (optional)

Current company & hierarchy node

Active ERM profile

Active SRMF version

Watchdog status indicator (green/amber/red)

11.2 NAVIGATION PRINCIPLES

Wizard over chaos
Users move through complex flows via guided steps, not free-form chaos.

Same pattern across modules
Threat, Vulnerability, RA, WRAC, PIT, Assurance – all use the same UX grammar.

AI always “to the right”, not “in your face”
A contextual AI side-panel assists but doesn’t disturb the core flow.

Hierarchy + Filters always visible
So the user always knows which mine/plant/zone/process they are working in.

Everything 2–3 clicks away from anywhere
Navigation is never deep and tangled.

11.3 GLOBAL MODULE NAV MAP (TOP-level UX)

ASCII overview:

ISMS HOME
  ├─ Overview Dashboard
  └─ Quick Links (Top Risks, Open PIT, Active PUEs, Watchdogs)

RISK MANAGEMENT
  ├─ ERM
  ├─ Threats
  ├─ Vulnerabilities
  ├─ Unwanted Events (UE)
  ├─ Risk Assessments
  ├─ WRAC
  ├─ Controls (Library & CCR)
  ├─ PIT
  ├─ Remote Assurance
  └─ Incident & Intelligence

OTHER MODULES
  ├─ Course Crafter
  ├─ Policy Builder
  ├─ Auditor App
  └─ Skills Portal

ADMIN & GOVERNANCE
  ├─ Company & Hierarchy
  ├─ ERM Administration
  ├─ User & Role Management
  ├─ Watchdog Console
  └─ Audit & Logs

11.4 GLOBAL “RISK PIPELINE” NAVIGATION VIEW

There should be a single visual “pipeline” view that lets users jump into any module in context:

[Threats] → [Vulnerabilities] → [UE] → [Risk Assessment] → [WRAC] → [PIT] → [Remote Assurance]


Each box is clickable.

If a risk is selected, jumping between steps keeps context (same UE / risk / controls).

A “Pipeline” tab appears on RA/WRAC/PIT screens.

11.5 WIZARD STRUCTURE — SHARED PATTERN

Across the system, the wizard pattern should be:

Step 1: Context
Step 2: Inputs
Step 3: AI Draft
Step 4: Human Edit & Approve
Step 5: Export / Commit


Applied differently per module, but same mental model.

11.6 THREAT MODULE — UI & WIZARD FLOW
Threat List View

Table with: Name, Category, Actor, Drift, Linked UEs, Status, Last updated

Filters: Company, Category, Actor type, Drift level, Has RA, Has incidents

Threat Creation Wizard

Step 1 — Context & Classification

Select company and hierarchy node (optional).

Select category (Adversarial / Non-adversarial).

Select actor type.

Free text: Describe the threat (user text + AI suggestion).

Step 2 — Capability, Intent, Opportunity

Sliders or radio buttons with ERM-aligned definitions.

AI suggests initial scores.

User overrides with reasons.

Step 3 — TTP Mapping

Checklist of TTPs with search.

AI suggests based on description.

User confirms.

Step 4 — Drift & Intelligence

Drift panel shows: current drift, reasons (if any), linked intelligence.

AI explains potential drift.

Step 5 — Review & Approve

Threat summary card.

“Send for approval” button.

Approver sees diff if editing existing threat.

11.7 VULNERABILITY MODULE — UI & WIZARD FLOW
Vulnerability List View

Columns: Name, Category, Severity, Exploitability, Node, Linked Threats, Linked UEs, Status.

Vulnerability Creation Wizard

Step 1 — Location & Context

Select company

Select hierarchy node (Plant → Zone → Area)

Optional: Select process & lifecycle stage

Step 2 — Evidence & Markup

Upload floorplan / image / PDF

Open brown-paper style canvas

Drop pins, draw rectangles, add text annotations

AI suggests vulnerability candidates from markup

Step 3 — Categorisation & Scoring

Choose category (People / Process / Tech / etc.)

Choose subcategory

Severity slider (with descriptors)

Exploitability slider

AI suggests starting values.

Step 4 — Custodian & Governance

Assign custodian team

Add due date for review

Define any mandatory evidence

Step 5 — Review & Approve

Summary card with thumbnail of markup

Send for approval

11.8 UE (UNWANTED EVENT) — UI & WIZARD FLOW
UE List View

Columns: UE description, Threat, Vulnerability, TVRE score, Linked Risk, PUE flag, Status.

UE Wizard

Step 1 — Source Selection

Pick Threat

Pick Vulnerability (or multiple)

View TVRE score (auto).

Step 2 — Sentence Construction

AI generates 1–3 candidate UE sentences.

User edits and approves.

Step 3 — Context Settings

Assign hierarchy node

Link to processes / lifecycle stage

Attach evidence references

Step 4 — RA Seed

Show a preview of RA fields that will be auto-populated.

Confirm “Generate Risk Assessment”.

11.9 RISK ASSESSMENT — UI & WIZARD FLOW
RA List View

Columns: UE, Inherent, Residual, Projected, Appetite flag, ROI, Status, PUE flag.

RA Wizard

Step 1 — UE & ERM Context

UE summary at top

ERM profile and appetite band shown visually

Hierarchy path visible

Step 2 — Likelihood

NIST components with sliders & definitions

AI suggests scores; user adjusts

Final mapped ERM likelihood level shown with color.

Step 3 — Impact & ALE

Financial metrics (asset value, exposure rate, ARO)

Other impact types: Safety, Regulatory, Operational, Environmental

AI suggests ranges; user confirms

ERM impact level & heatmap location shown.

Step 4 — Existing Controls & Residual Risk

Select existing controls via search/filter from Control Library

View control dependency hints

Efficacy preview and residual risk heatmap

AI warns if something is inconsistent.

Step 5 — Proposed Controls & Projected Risk

Search and add proposed controls or control sets

See updated projected risk on heatmap

Show projected remaining risk % + ROI

Appetite comparison displayed with labels: “Above appetite / At appetite / Below appetite”.

Step 6 — Workflow & Sign-off

Assign Risk Owner

Assign Custodian

Add comments or recommendations

“Send to Risk Owner for approval” button.

Once approved → RA becomes:

Visible in WRAC

Eligible for PIT export.

11.10 WRAC — UI VIEW & INTERACTION PATTERNS

WRAC has no wizard, it’s a workbench view.

Layout

Main table with horizontal scroll; sticky key columns (Risk ID, UE description, Inherent, Residual, Projected, PUE, ROI, etc.)

Top filters: Company, Node, Risk band, ROI, PUE, Bowtie required, Cost ranges.

Right side: “Risk detail” panel when a row is clicked.

Key Interactions

Clicking a risk opens: RA summary, controls, appetite, mitigation strategy.

Multi-select rows → export to PIT as a group.

Toggle views:

“Top 10 / 20 / 50 / 100”

“All PUEs”

“By architecture component”

“By control set”

Buttons:

“Send selected to PIT”

“Mark for Bowtie”

“Export WRAC → PDF / Excel / HTML”

11.11 PIT — UI & WIZARD FLOW
PIT Project List View

Columns: Project name, Linked risks count, Progress %, Cost, Overdue flag.

PIT Project Wizard

Step 1 — Scope Definition

Selected risks from WRAC shown

Selected controls / control sets

High-level objective statement

Step 2 — Task Breakdown

AI suggests tasks based on controls (e.g. “Camera risk assessment”, “Procurement”, “Installation”, “Testing”, “Training”)

User edits, groups, sequences tasks

Define dependencies

Step 3 — Costing & Timeline

Preliminary cost automatically pulled from control library

User can override or request detailed costing

Define planned start & end dates

Step 4 — Responsibility & Governance

Assign project owner

Assign task owners

Approvers defined

Step 5 — Monitoring View

Summary chart: progress, cost vs. plan, schedule vs. plan

“Create PIT Project” finalizes.

11.12 REMOTE ASSURANCE — UI & DASHBOARD
Assurance Dashboard View

Cards showing:

“Overall Control Availability” (percentage)

“Top 10 Control Failures”

“Systems health: CCTV / Access / Alarms / SCADA”

“Manual checklist compliance”

“Assurance-related risk spikes”

Control Health View

Table listing controls: Name, Node, Category, Availability %, Failure count, Impacted risks, Status.

Clicking a control shows:

Uptime graphs

Recent failures

Linked RA & WRAC entries

Linked incidents

11.13 INCIDENT & INTELLIGENCE — UI & FLOW
Incident List View

Columns: Incident type, Location, Severity, Linked threats, Linked RA, Status.

Incident Intake Wizard

Step 1 — Basic Details

Time, place, type, severity.

Step 2 — Evidence Upload

Reports, photos, video clips, logs.

Step 3 — SRMF Impact

AI suggests:

Threats impacted

Vulnerabilities indicated

UEs potentially triggered

Step 4 — Action

Create or update Threat

Create new Vulnerability

Flag existing RA for review

11.14 CONTROL LIBRARY — UI
Library View

Search by control name, category, risk type, threat, vulnerability

Columns: Control name, Category, Base efficacy, Cost band, Dependencies, Evidence type

Control Detail View

Control definition

Dependencies

Failure modes

Standard cost bands

Evidence expectations

Linked risks & projects

11.15 AI ASSISTANT UI (GLOBAL PATTERN)

The AI panel appears as a right-side drawer available in all major modules.

Features:

“Explain this screen”

“Help me design…” (threat, vulnerability, RA, control strategy, PIT plan)

“Summarise selected items”

“Highlight anomalies”

“Generate export-ready narrative”

Important:

AI never hides core data; it assists, it doesn’t dominate.

AI outputs always show “why” (short explanation anchored in ERM/SRMF rules).

11.16 MINIMALIST VISUAL LANGUAGE

The entire UI should be:

Clean, non-cluttered

Limited, consistent color use:

Neutrals for chrome

Heatmap colors only where risk is shown

Clear icons for status/severity

Whites/greys with accent color per module (but all from one design system).

Typography: one primary typeface with hierarchical sizing.

11.17 ACCESSIBILITY & RESPONSIVENESS

Keyboard navigable

High contrast option

Mobile-friendly “lite” views for:

Auditor mobile app

Checklist completion

PIT task updates

Incident capture

11.18 HOW THIS UI BLUEPRINT GUIDES FOREMAN + COPILOT

Foreman can use this section to:

Validate that each module’s UI conforms to the shared patterns.

Enforce consistent wizard structure.

Reject UX proposals that break the global navigation grammar.

Instruct CoPilot exactly what components to implement where.

CoPilot can:

Generate actual React components + routing tree based on this blueprint.

Implement wizard steps with clearly defined props and state flows.

Bind components to back-end endpoints designed in the other module specs.
# Independent Assurance Agent Canon

**Authority:** CS2 (APGI-cmy/maturion-foreman-governance)  
**Type:** Agent Contract Canon  
**Agent:** independent-assurance-agent  
**Effective:** 2026-04-14  

## Purpose

This canon record establishes the authoritative contract baseline for the Independent Assurance Agent (IAA) within the AMC governance ecosystem. It records the canonical version, operating model, and key constraints that govern IAA operations.

## Canon Reference

- **Agent ID:** independent-assurance-agent  
- **Contract version:** 2.6.0 (90/10 wave-record model)  
- **Operating model:** AMC 90/10 Admin Protocol v1.0.0  
- **Assurance carrier:** wave-record (`amc-wave-record-*.md` in `.agent-admin/wave-records/`)  
- **Token output mode:** write_to_wave_record_section_5_only  
- **IAA independence requirement:** Must not self-review; CodexAdvisor invokes IAA for all IAA contract changes  

## Key Governance Constraints

1. IAA is mandatory for ALL agent contract modifications — no class exceptions  
2. HALT-001 applies when IAA reviews its own contract changes  
3. Assurance token is written to wave record Section 5, not standalone files  
4. No new `.agent-admin/assurance/iaa-token-*.md` files permitted under 90/10 model  
5. No new `.agent-admin/prehandover/PREHANDOVER_PROOF*.md` files permitted under 90/10 model  

## Source

Canonical governance repository: APGI-cmy/maturion-foreman-governance  
This is a consumer copy. Do not modify without CS2 authority.

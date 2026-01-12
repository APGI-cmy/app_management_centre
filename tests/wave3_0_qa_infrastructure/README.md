# Wave 3.0 QA Infrastructure

This directory contains tests for Wave 3 implementation, focusing on runtime observability, telemetry, and resilience.

## Test Organization

- `test_telemetry_tracer.py` - End-to-end tracing tests (Wave 3.1)
- `test_alert_routing.py` - Alert routing and SLA monitoring (Wave 3.1)

## Wave 3 Scope

Wave 3.1: Runtime Telemetry & Audit Trail Hardening
- End-to-end traces with tenant isolation
- P95/P99 latency metrics
- Audit trail correlation
- Alert routing for SLA breaches

## Markers

Tests use `@pytest.mark.wave3` and `@pytest.mark.subwave_3_X` markers.

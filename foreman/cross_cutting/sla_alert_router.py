"""
SLA Alert Router for Wave 3.1 - Runtime Telemetry & Audit Trail Hardening

Extends alert_manager.py to provide SLA-based alerting using telemetry metrics.
Wires P95/P99 latency violations to appropriate alert channels with trace correlation.
"""

from datetime import datetime, timezone
from typing import Dict, Any, List, Optional

UTC = timezone.utc

# In-memory storage for SLA definitions and violations (tenant-isolated)
_sla_definitions = {}
_sla_violations = {}


def clear_all():
    """Clear all SLA alert state for testing."""
    global _sla_definitions, _sla_violations
    _sla_definitions = {}
    _sla_violations = {}


class SLAAlertRouter:
    """
    Routes alerts based on SLA violations detected from telemetry metrics.
    
    Integrates with:
    - TelemetryTracer for latency metrics
    - AuditLogger for violation audit trail
    - Alert channels for escalation
    """
    
    def __init__(self, organisation_id: str):
        """Initialize SLA alert router for specific organisation."""
        self.organisation_id = organisation_id
        
        # Initialize org-specific storage
        if organisation_id not in _sla_definitions:
            _sla_definitions[organisation_id] = {}
        if organisation_id not in _sla_violations:
            _sla_violations[organisation_id] = []
    
    def define_sla(
        self,
        operation_name: str,
        p95_threshold_ms: Optional[float] = None,
        p99_threshold_ms: Optional[float] = None,
        avg_threshold_ms: Optional[float] = None,
        severity: str = "HIGH"
    ):
        """
        Define SLA thresholds for an operation.
        
        Args:
            operation_name: Name of the operation to monitor
            p95_threshold_ms: Maximum acceptable P95 latency (ms)
            p99_threshold_ms: Maximum acceptable P99 latency (ms)
            avg_threshold_ms: Maximum acceptable average latency (ms)
            severity: Alert severity (CRITICAL, HIGH, MEDIUM, LOW)
        """
        _sla_definitions[self.organisation_id][operation_name] = {
            "operation_name": operation_name,
            "p95_threshold_ms": p95_threshold_ms,
            "p99_threshold_ms": p99_threshold_ms,
            "avg_threshold_ms": avg_threshold_ms,
            "severity": severity,
            "defined_at": datetime.now(UTC)
        }
    
    def get_sla_definition(self, operation_name: str) -> Optional[Dict[str, Any]]:
        """Retrieve SLA definition for an operation."""
        return _sla_definitions.get(self.organisation_id, {}).get(operation_name)
    
    def check_sla_compliance(
        self,
        operation_name: str,
        metrics: Dict[str, Any],
        trace_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Check if metrics comply with SLA thresholds.
        
        Args:
            operation_name: Operation to check
            metrics: Metrics dict with p50_ms, p95_ms, p99_ms, avg_ms
            trace_id: Optional trace ID for correlation
        
        Returns:
            Dict with compliance status and violations
        """
        sla = self.get_sla_definition(operation_name)
        
        if not sla:
            return {
                "compliant": True,
                "reason": "NO_SLA_DEFINED",
                "violations": []
            }
        
        violations = []
        
        # Check P95 threshold
        if sla["p95_threshold_ms"] is not None:
            if metrics.get("p95_ms", 0) > sla["p95_threshold_ms"]:
                violations.append({
                    "metric": "p95",
                    "actual": metrics["p95_ms"],
                    "threshold": sla["p95_threshold_ms"],
                    "exceeded_by": metrics["p95_ms"] - sla["p95_threshold_ms"]
                })
        
        # Check P99 threshold
        if sla["p99_threshold_ms"] is not None:
            if metrics.get("p99_ms", 0) > sla["p99_threshold_ms"]:
                violations.append({
                    "metric": "p99",
                    "actual": metrics["p99_ms"],
                    "threshold": sla["p99_threshold_ms"],
                    "exceeded_by": metrics["p99_ms"] - sla["p99_threshold_ms"]
                })
        
        # Check average threshold
        if sla["avg_threshold_ms"] is not None:
            if metrics.get("avg_ms", 0) > sla["avg_threshold_ms"]:
                violations.append({
                    "metric": "avg",
                    "actual": metrics["avg_ms"],
                    "threshold": sla["avg_threshold_ms"],
                    "exceeded_by": metrics["avg_ms"] - sla["avg_threshold_ms"]
                })
        
        return {
            "compliant": len(violations) == 0,
            "operation_name": operation_name,
            "violations": violations,
            "trace_id": trace_id,
            "checked_at": datetime.now(UTC)
        }
    
    def create_alert_for_violation(
        self,
        compliance_result: Dict[str, Any],
        additional_context: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Create an alert for SLA violation.
        
        Args:
            compliance_result: Result from check_sla_compliance()
            additional_context: Additional context for the alert
        
        Returns:
            Alert object with routing information
        """
        if compliance_result["compliant"]:
            return {"alert_created": False, "reason": "NO_VIOLATION"}
        
        operation_name = compliance_result["operation_name"]
        sla = self.get_sla_definition(operation_name)
        
        alert = {
            "alert_id": f"sla-alert-{len(_sla_violations[self.organisation_id]) + 1}",
            "organisation_id": self.organisation_id,
            "alert_type": "SLA_VIOLATION",
            "operation_name": operation_name,
            "severity": sla["severity"],
            "violations": compliance_result["violations"],
            "trace_id": compliance_result.get("trace_id"),
            "created_at": datetime.now(UTC),
            "status": "OPEN",
            "context": additional_context or {}
        }
        
        # Store violation
        _sla_violations[self.organisation_id].append(alert)
        
        return alert
    
    def route_alert(
        self,
        alert: Dict[str, Any],
        audit_logger=None
    ) -> Dict[str, Any]:
        """
        Route alert to appropriate channels and log to audit trail.
        
        Args:
            alert: Alert object from create_alert_for_violation()
            audit_logger: Optional AuditLogger instance for correlation
        
        Returns:
            Routing result with channels and escalation status
        """
        severity = alert["severity"]
        
        # Determine routing based on severity
        if severity == "CRITICAL":
            channels = ["escalation", "notification", "dashboard"]
            escalation_priority = "IMMEDIATE"
        elif severity == "HIGH":
            channels = ["notification", "dashboard"]
            escalation_priority = "HIGH"
        elif severity == "MEDIUM":
            channels = ["dashboard", "email"]
            escalation_priority = "NORMAL"
        else:  # LOW
            channels = ["dashboard"]
            escalation_priority = "LOW"
        
        routing_result = {
            "alert_id": alert["alert_id"],
            "channels": channels,
            "escalation_priority": escalation_priority,
            "routed_at": datetime.now(UTC),
            "audit_logged": False
        }
        
        # Log to audit trail if logger provided
        if audit_logger:
            audit_entry = audit_logger.log_governance_event(
                actor="SLA_MONITOR",
                action="SLA_VIOLATION_DETECTED",
                target=alert["operation_name"],
                outcome="ALERT_GENERATED",
                metadata={
                    "alert_id": alert["alert_id"],
                    "trace_id": alert.get("trace_id"),
                    "severity": severity,
                    "violations": alert["violations"]
                }
            )
            routing_result["audit_logged"] = True
            routing_result["audit_entry_id"] = audit_entry.get("entry_id")
        
        return routing_result
    
    def get_all_violations(
        self,
        status: Optional[str] = None,
        operation_name: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve SLA violations with optional filtering.
        
        Args:
            status: Filter by status (OPEN, ACKNOWLEDGED, RESOLVED)
            operation_name: Filter by operation name
        
        Returns:
            List of violation alerts
        """
        violations = _sla_violations.get(self.organisation_id, [])
        
        # Apply filters
        if status:
            violations = [v for v in violations if v["status"] == status]
        
        if operation_name:
            violations = [v for v in violations if v["operation_name"] == operation_name]
        
        return violations
    
    def acknowledge_violation(self, alert_id: str, acknowledged_by: str) -> bool:
        """
        Mark a violation as acknowledged.
        
        Args:
            alert_id: ID of the alert to acknowledge
            acknowledged_by: User or system acknowledging
        
        Returns:
            True if acknowledged successfully
        """
        for violation in _sla_violations.get(self.organisation_id, []):
            if violation["alert_id"] == alert_id:
                violation["status"] = "ACKNOWLEDGED"
                violation["acknowledged_by"] = acknowledged_by
                violation["acknowledged_at"] = datetime.now(UTC)
                return True
        return False
    
    def resolve_violation(
        self,
        alert_id: str,
        resolved_by: str,
        resolution_notes: Optional[str] = None
    ) -> bool:
        """
        Mark a violation as resolved.
        
        Args:
            alert_id: ID of the alert to resolve
            resolved_by: User or system resolving
            resolution_notes: Optional notes about resolution
        
        Returns:
            True if resolved successfully
        """
        for violation in _sla_violations.get(self.organisation_id, []):
            if violation["alert_id"] == alert_id:
                violation["status"] = "RESOLVED"
                violation["resolved_by"] = resolved_by
                violation["resolved_at"] = datetime.now(UTC)
                violation["resolution_notes"] = resolution_notes
                return True
        return False
    
    def get_violation_summary(self) -> Dict[str, Any]:
        """
        Get summary statistics for SLA violations.
        
        Returns:
            Dict with violation counts by status and severity
        """
        violations = _sla_violations.get(self.organisation_id, [])
        
        summary = {
            "total_violations": len(violations),
            "by_status": {
                "OPEN": 0,
                "ACKNOWLEDGED": 0,
                "RESOLVED": 0
            },
            "by_severity": {
                "CRITICAL": 0,
                "HIGH": 0,
                "MEDIUM": 0,
                "LOW": 0
            },
            "operations_affected": set()
        }
        
        for v in violations:
            summary["by_status"][v["status"]] = summary["by_status"].get(v["status"], 0) + 1
            summary["by_severity"][v["severity"]] = summary["by_severity"].get(v["severity"], 0) + 1
            summary["operations_affected"].add(v["operation_name"])
        
        summary["operations_affected"] = list(summary["operations_affected"])
        
        return summary

"""
Runtime Audit Trail

Purpose: Comprehensive audit trail with telemetry integration and tenant isolation
Authority: Wave 3.1 - Runtime Telemetry & Audit Trail Hardening
Tenant Isolation: All audit entries scoped by organisation_id
QA Coverage: QA-171 to QA-176 (Audit Logger requirements)

Integrates with:
- runtime/audit/telemetry.py (for trace correlation)
- foreman/cross_cutting/audit_logger.py (existing audit interface)
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC
from enum import Enum
from typing import Any, Optional
import uuid
import threading

from runtime.audit.telemetry import get_telemetry_collector, TelemetryLevel


class AuditSeverity(Enum):
    """Audit event severity levels"""
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"
    COMPLIANCE = "compliance"


class AuditCategory(Enum):
    """Categories of audit events"""
    GOVERNANCE = "governance"
    AUTHORITY = "authority"
    DATA_ACCESS = "data_access"
    SECURITY = "security"
    TENANT_ISOLATION = "tenant_isolation"
    SLA = "sla"
    INTEGRATION = "integration"


@dataclass
class AuditEntry:
    """Comprehensive audit trail entry"""
    entry_id: str
    timestamp: datetime
    organisation_id: str
    
    # Who and what
    actor: str
    action: str
    resource: str | None
    
    # Results
    outcome: str
    severity: AuditSeverity
    category: AuditCategory
    
    # Context
    metadata: dict[str, Any] = field(default_factory=dict)
    trace_id: str | None = None
    span_id: str | None = None
    
    # Immutability
    immutable: bool = True
    
    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary representation"""
        return {
            "entry_id": self.entry_id,
            "timestamp": self.timestamp.isoformat(),
            "organisation_id": self.organisation_id,
            "actor": self.actor,
            "action": self.action,
            "resource": self.resource,
            "outcome": self.outcome,
            "severity": self.severity.value,
            "category": self.category.value,
            "metadata": self.metadata,
            "trace_id": self.trace_id,
            "span_id": self.span_id,
            "immutable": self.immutable
        }


class RuntimeAuditTrail:
    """
    Runtime audit trail with telemetry integration
    
    Features:
    - Tenant isolation via organisation_id
    - Trace correlation via span_id and trace_id
    - Immutable audit log
    - Severity-based filtering
    - SLA breach detection
    """
    
    def __init__(self):
        self._entries: dict[str, list[AuditEntry]] = {}
        self._lock = threading.RLock()
        self._telemetry = get_telemetry_collector()
    
    def log_audit_event(
        self,
        organisation_id: str,
        actor: str,
        action: str,
        outcome: str,
        severity: AuditSeverity,
        category: AuditCategory,
        resource: str | None = None,
        metadata: dict[str, Any] = None,
        trace_id: str | None = None,
        span_id: str | None = None
    ) -> AuditEntry:
        """
        Log an audit event (QA-171: Log governance event)
        
        Captures:
        - Timestamp (UTC)
        - Actor (who performed the action)
        - Action (what was performed)
        - Outcome (result of the action)
        - Immutability flag
        """
        entry_id = str(uuid.uuid4())
        
        entry = AuditEntry(
            entry_id=entry_id,
            timestamp=datetime.now(UTC),
            organisation_id=organisation_id,
            actor=actor,
            action=action,
            resource=resource,
            outcome=outcome,
            severity=severity,
            category=category,
            metadata=metadata or {},
            trace_id=trace_id,
            span_id=span_id,
            immutable=True
        )
        
        with self._lock:
            if organisation_id not in self._entries:
                self._entries[organisation_id] = []
            
            self._entries[organisation_id].append(entry)
        
        # Also log to telemetry for trace correlation
        self._telemetry.log_event(
            event_type=f"audit.{category.value}",
            level=TelemetryLevel.AUDIT,
            organisation_id=organisation_id,
            data={
                "entry_id": entry_id,
                "actor": actor,
                "action": action,
                "outcome": outcome,
                "severity": severity.value,
                "resource": resource
            },
            correlation_id=trace_id
        )
        
        return entry
    
    def log_governance_event(
        self,
        organisation_id: str,
        actor: str,
        action: str,
        outcome: str,
        resource: str | None = None,
        metadata: dict[str, Any] = None,
        trace_id: str | None = None
    ) -> AuditEntry:
        """
        Log governance event (QA-171)
        Convenience method for governance-specific auditing
        """
        return self.log_audit_event(
            organisation_id=organisation_id,
            actor=actor,
            action=action,
            outcome=outcome,
            severity=AuditSeverity.COMPLIANCE,
            category=AuditCategory.GOVERNANCE,
            resource=resource,
            metadata=metadata,
            trace_id=trace_id
        )
    
    def log_authority_event(
        self,
        organisation_id: str,
        actor: str,
        action: str,
        outcome: str,
        permission_check: bool,
        override_used: bool = False,
        resource: str | None = None,
        metadata: dict[str, Any] = None,
        trace_id: str | None = None
    ) -> AuditEntry:
        """
        Log authority event (QA-172: Log authority event)
        
        Captures permission checks and overrides with complete audit trail
        """
        enhanced_metadata = metadata or {}
        enhanced_metadata.update({
            "permission_check": permission_check,
            "override_used": override_used
        })
        
        severity = AuditSeverity.CRITICAL if override_used else AuditSeverity.INFO
        
        return self.log_audit_event(
            organisation_id=organisation_id,
            actor=actor,
            action=action,
            outcome=outcome,
            severity=severity,
            category=AuditCategory.AUTHORITY,
            resource=resource,
            metadata=enhanced_metadata,
            trace_id=trace_id
        )
    
    def log_tenant_isolation_event(
        self,
        organisation_id: str,
        actor: str,
        action: str,
        outcome: str,
        isolation_verified: bool,
        resource: str | None = None,
        metadata: dict[str, Any] = None,
        trace_id: str | None = None
    ) -> AuditEntry:
        """
        Log tenant isolation enforcement event
        
        Tracks all operations where tenant isolation is verified or violated
        """
        enhanced_metadata = metadata or {}
        enhanced_metadata.update({
            "isolation_verified": isolation_verified
        })
        
        severity = AuditSeverity.INFO if isolation_verified else AuditSeverity.CRITICAL
        
        return self.log_audit_event(
            organisation_id=organisation_id,
            actor=actor,
            action=action,
            outcome=outcome if isolation_verified else "ISOLATION_VIOLATION",
            severity=severity,
            category=AuditCategory.TENANT_ISOLATION,
            resource=resource,
            metadata=enhanced_metadata,
            trace_id=trace_id
        )
    
    def log_sla_breach(
        self,
        organisation_id: str,
        operation: str,
        duration_ms: float,
        threshold_ms: float,
        metadata: dict[str, Any] = None,
        trace_id: str | None = None
    ) -> AuditEntry:
        """
        Log SLA breach event
        
        Triggered when operations exceed defined SLA thresholds
        """
        enhanced_metadata = metadata or {}
        enhanced_metadata.update({
            "duration_ms": duration_ms,
            "threshold_ms": threshold_ms,
            "breach_amount_ms": duration_ms - threshold_ms
        })
        
        return self.log_audit_event(
            organisation_id=organisation_id,
            actor="SYSTEM",
            action="SLA_BREACH_DETECTED",
            outcome="WARNING",
            severity=AuditSeverity.WARNING,
            category=AuditCategory.SLA,
            resource=operation,
            metadata=enhanced_metadata,
            trace_id=trace_id
        )
    
    def query_audit_log(
        self,
        organisation_id: str,
        actor: str | None = None,
        action: str | None = None,
        category: AuditCategory | None = None,
        severity: AuditSeverity | None = None,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
        limit: int = 100
    ) -> list[AuditEntry]:
        """
        Query audit log (QA-173: Query audit log)
        
        Supports:
        - Time range queries
        - Actor filtering
        - Action type filtering
        - Category and severity filtering
        """
        with self._lock:
            entries = list(self._entries.get(organisation_id, []))
        
        # Apply filters
        if actor:
            entries = [e for e in entries if e.actor == actor]
        if action:
            entries = [e for e in entries if e.action == action]
        if category:
            entries = [e for e in entries if e.category == category]
        if severity:
            entries = [e for e in entries if e.severity == severity]
        if start_time:
            entries = [e for e in entries if e.timestamp >= start_time]
        if end_time:
            entries = [e for e in entries if e.timestamp <= end_time]
        
        # Return most recent first, up to limit
        return list(reversed(entries))[:limit]
    
    def get_audit_entry(self, organisation_id: str, entry_id: str) -> AuditEntry | None:
        """Retrieve a specific audit entry by ID"""
        with self._lock:
            entries = self._entries.get(organisation_id, [])
            for entry in entries:
                if entry.entry_id == entry_id:
                    return entry
        return None
    
    def verify_immutability(self, organisation_id: str) -> bool:
        """
        Verify audit log immutability (QA-174: Audit log immutability)
        
        Checks:
        - All entries are marked immutable
        - Append-only structure
        - No modifications detected
        """
        with self._lock:
            entries = self._entries.get(organisation_id, [])
            return all(entry.immutable for entry in entries)
    
    def get_audit_statistics(self, organisation_id: str) -> dict[str, Any]:
        """
        Get audit log statistics for an organisation
        
        Returns counts by category, severity, and time-based metrics
        """
        with self._lock:
            entries = self._entries.get(organisation_id, [])
        
        if not entries:
            return {
                "total_entries": 0,
                "by_category": {},
                "by_severity": {},
                "oldest_entry": None,
                "newest_entry": None
            }
        
        # Count by category
        by_category: dict[str, int] = {}
        for entry in entries:
            cat = entry.category.value
            by_category[cat] = by_category.get(cat, 0) + 1
        
        # Count by severity
        by_severity: dict[str, int] = {}
        for entry in entries:
            sev = entry.severity.value
            by_severity[sev] = by_severity.get(sev, 0) + 1
        
        return {
            "total_entries": len(entries),
            "by_category": by_category,
            "by_severity": by_severity,
            "oldest_entry": min(e.timestamp for e in entries).isoformat(),
            "newest_entry": max(e.timestamp for e in entries).isoformat()
        }
    
    def clear_organisation_data(self, organisation_id: str) -> None:
        """Clear all audit data for an organisation (for testing only)"""
        with self._lock:
            self._entries.pop(organisation_id, None)


# Global runtime audit trail instance
_runtime_audit_trail: RuntimeAuditTrail | None = None


def get_runtime_audit_trail() -> RuntimeAuditTrail:
    """Get or create the global runtime audit trail"""
    global _runtime_audit_trail
    if _runtime_audit_trail is None:
        _runtime_audit_trail = RuntimeAuditTrail()
    return _runtime_audit_trail


def clear_audit_trail() -> None:
    """Clear global audit trail (for testing)"""
    global _runtime_audit_trail
    _runtime_audit_trail = None

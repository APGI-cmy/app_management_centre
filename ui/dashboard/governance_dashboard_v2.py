"""
Governance Dashboard V2 - Subwave 3.3

Enhanced governance dashboard with drilldown, multi-criteria filtering,
realtime notifications, and evidence linking.

Architecture: Governance Dashboard V2 (CST-2)
Tenant Isolation: All operations scoped by organisation_id
Authority: WAVE_3_IMPLEMENTATION_PLAN.md, BL-024, BL-026
"""

from typing import Dict, Any, List, Optional, Callable
from datetime import datetime, UTC, timedelta


class GovernanceDashboardV2:
    """
    Governance Dashboard V2 with full drilldown, filtering, realtime, and evidence support.
    
    Features:
    - Domain status management with evidence linking
    - Time-based filtering infrastructure
    - Realtime update integration
    - Multi-criteria data access
    - Tenant-isolated operations
    """
    
    def __init__(self, context: Dict[str, Any], connection=None):
        """
        Initialize Governance Dashboard V2.
        
        Args:
            context: UI context with organisation_id for tenant isolation
            connection: Optional realtime connection for live updates
        """
        self.context = context
        self.organisation_id = context.get("organisation_id")
        self.connection = connection
        
        # Domain status tracking
        self.domain_statuses: Dict[str, Dict[str, Any]] = {}
        
        # Evidence linking
        self.evidence_links: Dict[str, Dict[str, Dict[str, Any]]] = {}
        
        # Refresh handlers
        self.refresh_handlers: List[Callable] = []
        
        # Update timestamps for staleness detection
        self.update_timestamps: Dict[str, datetime] = {}
        
        # Domain registry
        self.domains: List[str] = []
        
        # Register for realtime updates if connection provided
        if connection:
            connection.on_update(self._handle_realtime_update)
    
    def set_domain_status(self, domain: str, status: str, details: Optional[Dict[str, Any]] = None):
        """
        Set status for a governance domain.
        
        Args:
            domain: Domain name (e.g., "Build Execution", "QA Coverage")
            status: Status value (GREEN, AMBER, RED, UNKNOWN)
            details: Optional additional details (root_cause, reason, advisory, etc.)
        """
        if domain not in self.domains:
            self.domains.append(domain)
        
        self.domain_statuses[domain] = {
            "status": status,
            "organisation_id": self.organisation_id,
            "timestamp": datetime.now(UTC).isoformat(),
            **(details or {})
        }
        
        self.update_timestamps[domain] = datetime.now(UTC)
    
    def get_domain_status(self, domain: str) -> Dict[str, Any]:
        """
        Get status for a governance domain.
        
        Args:
            domain: Domain name
            
        Returns:
            Domain status information with tenant isolation
        """
        if domain in self.domain_statuses:
            return self.domain_statuses[domain].copy()
        
        return {
            "status": "UNKNOWN",
            "organisation_id": self.organisation_id
        }
    
    def get_all_domains(self) -> List[str]:
        """
        Get list of all registered domains.
        
        Returns:
            List of domain names
        """
        return self.domains.copy()
    
    def add_evidence_link(self, domain: str, evidence_type: str, evidence_path: str, metadata: Optional[Dict[str, Any]] = None):
        """
        Add evidence link for a domain.
        
        Args:
            domain: Domain name
            evidence_type: Type of evidence (test_results, build_logs, etc.)
            evidence_path: Path to evidence artifact
            metadata: Optional metadata about the evidence
        """
        if domain not in self.evidence_links:
            self.evidence_links[domain] = {}
        
        self.evidence_links[domain][evidence_type] = {
            "path": evidence_path,
            "type": evidence_type,
            "organisation_id": self.organisation_id,
            "timestamp": datetime.now(UTC).isoformat(),
            **({"metadata": metadata} if metadata else {})
        }
    
    def get_evidence_link(self, domain: str) -> Optional[Dict[str, Any]]:
        """
        Get primary evidence link for a domain.
        
        Args:
            domain: Domain name
            
        Returns:
            Evidence link information or None
        """
        if domain in self.evidence_links:
            links = self.evidence_links[domain]
            if links:
                # Return first evidence link
                first_key = next(iter(links))
                return links[first_key]
        
        return None
    
    def get_evidence_links(self, domain: str) -> Dict[str, Dict[str, Any]]:
        """
        Get all evidence links for a domain.
        
        Args:
            domain: Domain name
            
        Returns:
            Dictionary of evidence links by type
        """
        return self.evidence_links.get(domain, {}).copy()
    
    def create_time_filter(self, filter_type: str, start_time: Optional[datetime] = None, end_time: Optional[datetime] = None) -> Dict[str, Any]:
        """
        Create time-based filter configuration.
        
        Args:
            filter_type: Type of filter (last_hour, last_day, last_week, custom)
            start_time: Start time for custom filter
            end_time: End time for custom filter
            
        Returns:
            Filter configuration
        """
        now = datetime.now(UTC)
        
        if filter_type == "last_hour":
            start_time = now - timedelta(hours=1)
            end_time = now
        elif filter_type == "last_day":
            start_time = now - timedelta(days=1)
            end_time = now
        elif filter_type == "last_week":
            start_time = now - timedelta(weeks=1)
            end_time = now
        elif filter_type == "custom":
            if not start_time or not end_time:
                raise ValueError("Custom filter requires start_time and end_time")
        else:
            raise ValueError(f"Unknown filter type: {filter_type}")
        
        return {
            "type": filter_type,
            "start_time": start_time,
            "end_time": end_time
        }
    
    def apply_time_filter(self, data: List[Dict[str, Any]], time_filter: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Apply time filter to data.
        
        Args:
            data: List of data items with timestamps
            time_filter: Filter configuration from create_time_filter
            
        Returns:
            Filtered data within time range
        """
        start_time = time_filter["start_time"]
        end_time = time_filter["end_time"]
        
        filtered = []
        for item in data:
            if "timestamp" not in item:
                continue
            
            # Parse timestamp
            timestamp_str = item["timestamp"]
            try:
                if timestamp_str.endswith('Z'):
                    timestamp_str = timestamp_str[:-1]
                item_time = datetime.fromisoformat(timestamp_str)
                
                # Make timezone-aware if needed
                if item_time.tzinfo is None:
                    item_time = item_time.replace(tzinfo=UTC)
                
                # Check if within range
                if start_time <= item_time <= end_time:
                    filtered.append(item)
            except (ValueError, AttributeError):
                # Skip items with invalid timestamps
                continue
        
        return filtered
    
    def on_refresh(self, handler: Callable):
        """
        Register refresh handler callback.
        
        Args:
            handler: Callback function for refresh events
        """
        self.refresh_handlers.append(handler)
    
    def _handle_realtime_update(self, update: Dict[str, Any]):
        """
        Handle incoming realtime update.
        
        Args:
            update: Update message from realtime connection
        """
        update_type = update.get("type")
        
        if update_type == "status_update":
            domain = update.get("domain")
            new_status = update.get("new_status", update.get("status"))
            timestamp_str = update.get("timestamp")
            
            if domain and new_status:
                # Parse timestamp for staleness check
                update_timestamp = self._parse_timestamp(timestamp_str)
                last_timestamp = self.update_timestamps.get(domain)
                
                # Apply update only if newer
                if last_timestamp is None or update_timestamp > last_timestamp:
                    self.domain_statuses[domain] = {
                        "status": new_status,
                        "organisation_id": self.organisation_id,
                        "timestamp": update_timestamp
                    }
                    self.update_timestamps[domain] = update_timestamp
                    
                    # Trigger refresh
                    for handler in self.refresh_handlers:
                        handler(f"realtime_{update_type}")
        
    def _handle_realtime_update(self, update: Dict[str, Any]):
        """
        Handle incoming realtime update.
        
        Args:
            update: Update message from realtime connection
        """
        update_type = update.get("type")
        
        if update_type == "status_update":
            domain = update.get("domain")
            new_status = update.get("new_status", update.get("status"))
            timestamp_str = update.get("timestamp")
            
            if domain and new_status:
                # Parse timestamp for staleness check
                update_timestamp = self._parse_timestamp(timestamp_str)
                last_timestamp = self.update_timestamps.get(domain)
                
                # Apply update only if newer
                if last_timestamp is None or update_timestamp > last_timestamp:
                    self.domain_statuses[domain] = {
                        "status": new_status,
                        "organisation_id": self.organisation_id,
                        "timestamp": update_timestamp
                    }
                    self.update_timestamps[domain] = update_timestamp
                    
                    # Trigger refresh
                    for handler in self.refresh_handlers:
                        handler(f"realtime_{update_type}")
        
        elif update_type == "domain_added":
            domain = update.get("domain")
            status = update.get("status", "UNKNOWN")
            
            if domain and domain not in self.domains:
                self.domains.append(domain)
                # Extract additional details from update for set_domain_status
                details = {k: v for k, v in update.items() if k not in ["type", "domain", "status", "organisation_id"]}
                self.set_domain_status(domain, status, details if details else None)
        
        elif update_type == "evidence_linked":
            domain = update.get("domain")
            evidence_type = update.get("evidence_type")
            evidence_path = update.get("evidence_path")
            metadata = update.get("metadata")
            
            if domain and evidence_type and evidence_path:
                self.add_evidence_link(domain, evidence_type, evidence_path, metadata)
                
                # Trigger refresh for evidence updates
                for handler in self.refresh_handlers:
                    handler(f"realtime_{update_type}")
    
    def _parse_timestamp(self, timestamp_str: Optional[str]) -> datetime:
        """
        Parse ISO timestamp string.
        
        Args:
            timestamp_str: ISO format timestamp
            
        Returns:
            Parsed datetime object with UTC timezone
        """
        if not timestamp_str:
            return datetime.now(UTC)
        
        if isinstance(timestamp_str, datetime):
            return timestamp_str
        
        try:
            # Remove 'Z' suffix if present
            if timestamp_str.endswith('Z'):
                timestamp_str = timestamp_str[:-1]
            
            dt = datetime.fromisoformat(timestamp_str)
            
            # Make timezone-aware if needed
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=UTC)
            
            return dt
        except (ValueError, AttributeError):
            return datetime.now(UTC)

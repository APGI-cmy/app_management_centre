"""
Query Performance Monitor

Provides query performance monitoring, execution time tracking, and trend analysis.
"""

import time
from typing import Any, Optional
from dataclasses import dataclass, field
from collections import deque


@dataclass
class QueryMetrics:
    """Query performance metrics"""
    query_id: str
    execution_time: float
    timestamp: float = field(default_factory=time.time)
    query_count: int = 1
    
    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary"""
        return {
            'query_id': self.query_id,
            'execution_time': self.execution_time,
            'timestamp': self.timestamp,
            'query_count': self.query_count
        }


class QueryMonitor:
    """
    Query Performance Monitor
    
    Provides:
    - Execution time tracking
    - Query count metrics
    - Alert threshold monitoring
    - Performance trend analysis
    """
    
    def __init__(self, alert_threshold: float = 2.0, max_history: int = 1000):
        """
        Initialize query monitor
        
        Args:
            alert_threshold: Alert threshold in seconds
            max_history: Maximum number of queries to keep in history
        """
        self.alert_threshold = alert_threshold
        self.max_history = max_history
        
        self._metrics: dict[str, QueryMetrics] = {}
        self._history: deque = deque(maxlen=max_history)
        self._alerts: list[dict[str, Any]] = []
        self._total_queries = 0
        self._total_time = 0.0
    
    def track_query(self, query_id: str, execution_time: float) -> QueryMetrics:
        """
        Track query execution
        
        Args:
            query_id: Unique query identifier
            execution_time: Execution time in seconds
        
        Returns:
            Updated query metrics
        """
        # Update total counters
        self._total_queries += 1
        self._total_time += execution_time
        
        # Update or create metrics for this query
        if query_id in self._metrics:
            metrics = self._metrics[query_id]
            metrics.query_count += 1
            metrics.execution_time = (
                (metrics.execution_time * (metrics.query_count - 1) + execution_time) 
                / metrics.query_count
            )
            metrics.timestamp = time.time()
        else:
            metrics = QueryMetrics(
                query_id=query_id,
                execution_time=execution_time
            )
            self._metrics[query_id] = metrics
        
        # Add to history
        self._history.append({
            'query_id': query_id,
            'execution_time': execution_time,
            'timestamp': time.time()
        })
        
        # Check alert threshold
        if execution_time > self.alert_threshold:
            self._create_alert(query_id, execution_time)
        
        return metrics
    
    def _create_alert(self, query_id: str, execution_time: float) -> None:
        """Create performance alert"""
        alert = {
            'type': 'slow_query',
            'query_id': query_id,
            'execution_time': execution_time,
            'threshold': self.alert_threshold,
            'timestamp': time.time()
        }
        self._alerts.append(alert)
    
    def get_metrics(self, query_id: str) -> QueryMetrics | None:
        """Get metrics for specific query"""
        return self._metrics.get(query_id)
    
    def get_all_metrics(self) -> dict[str, QueryMetrics]:
        """Get metrics for all queries"""
        return self._metrics.copy()
    
    def get_alerts(self) -> list[dict[str, Any]]:
        """Get all performance alerts"""
        return self._alerts.copy()
    
    def get_statistics(self) -> dict[str, Any]:
        """
        Get comprehensive performance statistics
        
        Returns:
            Dictionary with performance statistics
        """
        avg_time = self._total_time / self._total_queries if self._total_queries > 0 else 0.0
        
        return {
            'total_queries': self._total_queries,
            'total_time': self._total_time,
            'average_time': avg_time,
            'unique_queries': len(self._metrics),
            'alerts_count': len(self._alerts),
            'alert_threshold': self.alert_threshold
        }
    
    def get_trend_analysis(self, window_size: int = 100) -> dict[str, Any]:
        """
        Analyze performance trends
        
        Args:
            window_size: Number of recent queries to analyze
        
        Returns:
            Trend analysis results
        """
        if not self._history:
            return {
                'trend': 'stable',
                'average_recent': 0.0,
                'average_overall': 0.0
            }
        
        # Get recent queries
        recent_queries = list(self._history)[-window_size:]
        
        # Calculate averages
        recent_avg = sum(q['execution_time'] for q in recent_queries) / len(recent_queries)
        overall_avg = self._total_time / self._total_queries if self._total_queries > 0 else 0.0
        
        # Determine trend
        if recent_avg > overall_avg * 1.2:
            trend = 'degrading'
        elif recent_avg < overall_avg * 0.8:
            trend = 'improving'
        else:
            trend = 'stable'
        
        return {
            'trend': trend,
            'average_recent': recent_avg,
            'average_overall': overall_avg,
            'sample_size': len(recent_queries)
        }
    
    def clear_alerts(self) -> None:
        """Clear all alerts"""
        self._alerts.clear()
    
    def get_percentile(self, percentile: float) -> float:
        """
        Calculate percentile of query execution times
        
        Args:
            percentile: Percentile to calculate (0.0 to 1.0, e.g., 0.95 for P95)
        
        Returns:
            Percentile value in seconds
        """
        if not self._history:
            return 0.0
        
        # Extract execution times from history
        execution_times = [q['execution_time'] for q in self._history]
        execution_times.sort()
        
        # Calculate percentile index
        index = int(len(execution_times) * percentile)
        if index >= len(execution_times):
            index = len(execution_times) - 1
        
        return execution_times[index]
    
    def get_p95_latency(self) -> float:
        """Get P95 latency in seconds"""
        return self.get_percentile(0.95)
    
    def get_p99_latency(self) -> float:
        """Get P99 latency in seconds"""
        return self.get_percentile(0.99)
    
    def get_performance_report(self) -> dict[str, Any]:
        """
        Get comprehensive performance report with percentiles
        
        Returns:
            Performance report with P50, P95, P99 latencies
        """
        stats = self.get_statistics()
        
        return {
            **stats,
            'p50_latency': self.get_percentile(0.50),
            'p95_latency': self.get_p95_latency(),
            'p99_latency': self.get_p99_latency(),
            'p95_target_met': self.get_p95_latency() < 0.180,  # 180ms target
            'p99_target_met': self.get_p99_latency() < 0.230,  # 230ms target
        }
    
    def reset(self) -> None:
        """Reset all monitoring data"""
        self._metrics.clear()
        self._history.clear()
        self._alerts.clear()
        self._total_queries = 0
        self._total_time = 0.0

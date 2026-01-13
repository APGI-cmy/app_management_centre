"""
Conflict Resolution Guard Module

Purpose: Race condition and deadlock prevention for concurrent operations
Authority: Wave 3.4 - Resilience & Failure Mode Expansion
Tenant Isolation: All operations scoped by organisation_id

Capabilities:
- Race condition detection and prevention
- Deadlock detection and avoidance
- Resource locking with timeout
- Conflict resolution strategies
- Concurrent operation coordination
"""

from typing import Any
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, timedelta, UTC
from enum import Enum
import threading
import uuid
import time


class ConflictType(Enum):
    """Types of conflicts"""
    RACE_CONDITION = "race_condition"
    DEADLOCK = "deadlock"
    RESOURCE_CONTENTION = "resource_contention"
    STATE_INCONSISTENCY = "state_inconsistency"


class LockStatus(Enum):
    """Resource lock status"""
    ACQUIRED = "acquired"
    TIMEOUT = "timeout"
    DENIED = "denied"
    RELEASED = "released"


class ResolutionStrategy(Enum):
    """Conflict resolution strategies"""
    FIRST_WINS = "first_wins"  # First operation proceeds, others abort
    LAST_WINS = "last_wins"  # Last operation proceeds, others abort
    MERGE = "merge"  # Attempt to merge conflicting operations
    RETRY = "retry"  # Retry failed operation
    ESCALATE = "escalate"  # Escalate to manual resolution


@dataclass
class ResourceLock:
    """Lock on a resource"""
    lock_id: str
    resource_id: str
    operation_id: str
    acquired_at: datetime
    timeout_seconds: int
    holder_thread_id: int
    organisation_id: str
    
    def is_expired(self) -> bool:
        """Check if lock has expired"""
        return datetime.now(UTC) > self.acquired_at + timedelta(seconds=self.timeout_seconds)


@dataclass
class ConflictDetection:
    """Detected conflict"""
    conflict_id: str
    conflict_type: ConflictType
    detected_at: datetime
    resource_ids: list[str]
    operation_ids: list[str]
    thread_ids: list[int]
    resolution_strategy: ResolutionStrategy
    resolved: bool = False
    resolution_details: dict[str, Any] = field(default_factory=dict)


@dataclass
class DeadlockCycle:
    """Detected deadlock cycle"""
    cycle_id: str
    detected_at: datetime
    cycle: list[str]  # List of resource IDs in cycle
    involved_operations: list[str]
    involved_threads: list[int]
    broken: bool = False
    victim_operation_id: str | None = None


class ConflictResolutionGuard:
    """
    Guards against race conditions and deadlocks
    
    Provides:
    - Resource locking with timeout
    - Race condition detection
    - Deadlock detection and breaking
    - Conflict resolution strategies
    - Concurrent operation coordination
    """
    
    def __init__(self, organisation_id: str):
        """
        Initialize conflict resolution guard
        
        Args:
            organisation_id: Organisation ID for tenant isolation
        """
        self.organisation_id = organisation_id
        self._resource_locks: dict[str, ResourceLock] = {}
        self._operation_resources: dict[str, set[str]] = {}  # operation_id -> resource_ids
        self._resource_waiters: dict[str, list[str]] = {}  # resource_id -> waiting operation_ids
        self._conflicts: dict[str, ConflictDetection] = {}
        self._deadlock_history: list[DeadlockCycle] = []
        self._lock = threading.Lock()
        
        # Start background deadlock detector
        self._stop_detector = threading.Event()
        self._detector_thread = threading.Thread(target=self._deadlock_detector_loop, daemon=True)
        self._detector_thread.start()
    
    def acquire_resource_lock(
        self,
        resource_id: str,
        operation_id: str,
        timeout_seconds: int = 30
    ) -> dict[str, Any]:
        """
        Acquire lock on resource with timeout
        
        Args:
            resource_id: Resource to lock
            operation_id: Operation requesting lock
            timeout_seconds: Lock timeout duration
        
        Returns:
            dict with status and lock_id (if acquired)
        """
        thread_id = threading.get_ident()
        start_time = time.time()
        
        while time.time() - start_time < timeout_seconds:
            with self._lock:
                # Check if resource is locked
                existing_lock = self._resource_locks.get(resource_id)
                
                if existing_lock:
                    # Check if lock expired
                    if existing_lock.is_expired():
                        # Remove expired lock
                        self._remove_lock_internal(existing_lock.lock_id)
                    elif existing_lock.operation_id == operation_id:
                        # Same operation re-acquiring (reentrant)
                        return {
                            "status": LockStatus.ACQUIRED.value,
                            "lock_id": existing_lock.lock_id,
                            "reentrant": True
                        }
                    else:
                        # Resource locked by another operation
                        # Add to waiters
                        if resource_id not in self._resource_waiters:
                            self._resource_waiters[resource_id] = []
                        if operation_id not in self._resource_waiters[resource_id]:
                            self._resource_waiters[resource_id].append(operation_id)
                        
                        # Check for potential deadlock
                        if self._check_deadlock_potential(operation_id, resource_id):
                            return {
                                "status": LockStatus.DENIED.value,
                                "reason": "potential_deadlock_detected",
                                "conflict_id": self._record_conflict(
                                    ConflictType.DEADLOCK,
                                    [resource_id],
                                    [operation_id, existing_lock.operation_id],
                                    [thread_id, existing_lock.holder_thread_id]
                                )
                            }
                else:
                    # Acquire lock
                    lock_id = str(uuid.uuid4())
                    lock = ResourceLock(
                        lock_id=lock_id,
                        resource_id=resource_id,
                        operation_id=operation_id,
                        acquired_at=datetime.now(UTC),
                        timeout_seconds=timeout_seconds,
                        holder_thread_id=thread_id,
                        organisation_id=self.organisation_id
                    )
                    
                    self._resource_locks[resource_id] = lock
                    
                    # Track operation's resources
                    if operation_id not in self._operation_resources:
                        self._operation_resources[operation_id] = set()
                    self._operation_resources[operation_id].add(resource_id)
                    
                    # Remove from waiters if present
                    if resource_id in self._resource_waiters:
                        waiters = self._resource_waiters[resource_id]
                        if operation_id in waiters:
                            waiters.remove(operation_id)
                    
                    return {
                        "status": LockStatus.ACQUIRED.value,
                        "lock_id": lock_id,
                        "acquired_at": lock.acquired_at.isoformat()
                    }
            
            # Wait briefly before retry
            time.sleep(0.1)
        
        # Timeout
        return {
            "status": LockStatus.TIMEOUT.value,
            "timeout_seconds": timeout_seconds,
            "conflict_id": self._record_conflict(
                ConflictType.RESOURCE_CONTENTION,
                [resource_id],
                [operation_id],
                [thread_id]
            )
        }
    
    def release_resource_lock(
        self,
        lock_id: str
    ) -> dict[str, Any]:
        """
        Release acquired lock
        
        Args:
            lock_id: Lock ID to release
        
        Returns:
            dict with status
        """
        with self._lock:
            return self._remove_lock_internal(lock_id)
    
    def _remove_lock_internal(self, lock_id: str) -> dict[str, Any]:
        """Internal lock removal (must be called with _lock held)"""
        # Find lock by ID
        for resource_id, lock in list(self._resource_locks.items()):
            if lock.lock_id == lock_id:
                del self._resource_locks[resource_id]
                
                # Update operation resources
                if lock.operation_id in self._operation_resources:
                    self._operation_resources[lock.operation_id].discard(resource_id)
                    if not self._operation_resources[lock.operation_id]:
                        del self._operation_resources[lock.operation_id]
                
                return {
                    "status": LockStatus.RELEASED.value,
                    "lock_id": lock_id,
                    "resource_id": resource_id,
                    "released_at": datetime.now(UTC).isoformat()
                }
        
        return {
            "status": "not_found",
            "lock_id": lock_id
        }
    
    def release_all_operation_locks(
        self,
        operation_id: str
    ) -> dict[str, Any]:
        """
        Release all locks held by operation
        
        Args:
            operation_id: Operation ID
        
        Returns:
            dict with released count
        """
        released = []
        
        with self._lock:
            # Find all locks for operation
            for resource_id, lock in list(self._resource_locks.items()):
                if lock.operation_id == operation_id:
                    result = self._remove_lock_internal(lock.lock_id)
                    if result["status"] == LockStatus.RELEASED.value:
                        released.append(lock.lock_id)
        
        return {
            "operation_id": operation_id,
            "released_count": len(released),
            "lock_ids": released
        }
    
    def _check_deadlock_potential(
        self,
        requesting_operation: str,
        requested_resource: str
    ) -> bool:
        """
        Check if granting lock would create deadlock
        
        Uses wait-for graph cycle detection
        """
        # Build wait-for graph
        # operation -> resource it's waiting for -> operation holding that resource
        
        def has_cycle(operation: str, visited: set[str], rec_stack: set[str]) -> bool:
            """DFS to detect cycle in wait-for graph"""
            visited.add(operation)
            rec_stack.add(operation)
            
            # Find resources this operation is waiting for
            waiting_for_resources = [
                res_id for res_id, waiters in self._resource_waiters.items()
                if operation in waiters
            ]
            
            # Find operations holding those resources
            for res_id in waiting_for_resources:
                lock = self._resource_locks.get(res_id)
                if lock:
                    holder = lock.operation_id
                    if holder not in visited:
                        if has_cycle(holder, visited, rec_stack):
                            return True
                    elif holder in rec_stack:
                        # Cycle detected
                        return True
            
            rec_stack.remove(operation)
            return False
        
        # Simulate granting the lock
        # Temporarily add to waiters
        if requested_resource not in self._resource_waiters:
            self._resource_waiters[requested_resource] = []
        if requesting_operation not in self._resource_waiters[requested_resource]:
            self._resource_waiters[requested_resource].append(requesting_operation)
        
        visited: set[str] = set()
        rec_stack: set[str] = set()
        
        cycle_exists = has_cycle(requesting_operation, visited, rec_stack)
        
        # Remove from waiters (was temporary)
        self._resource_waiters[requested_resource].remove(requesting_operation)
        
        return cycle_exists
    
    def _deadlock_detector_loop(self) -> None:
        """Background loop to detect and break deadlocks"""
        while not self._stop_detector.is_set():
            time.sleep(5)  # Check every 5 seconds
            
            with self._lock:
                self._detect_and_break_deadlocks()
    
    def _detect_and_break_deadlocks(self) -> None:
        """Detect deadlock cycles and break them"""
        # Build wait-for graph
        visited: set[str] = set()
        
        for operation in self._operation_resources.keys():
            if operation not in visited:
                path: list[str] = []
                if self._detect_cycle_dfs(operation, visited, set(), path):
                    # Cycle detected
                    cycle_id = str(uuid.uuid4())
                    
                    # Find all threads involved
                    involved_threads = []
                    for op in path:
                        resources = self._operation_resources.get(op, set())
                        for res in resources:
                            lock = self._resource_locks.get(res)
                            if lock:
                                involved_threads.append(lock.holder_thread_id)
                    
                    deadlock = DeadlockCycle(
                        cycle_id=cycle_id,
                        detected_at=datetime.now(UTC),
                        cycle=list(self._operation_resources.get(path[0], set())),
                        involved_operations=path,
                        involved_threads=involved_threads
                    )
                    
                    # Break deadlock by choosing victim
                    victim = self._choose_deadlock_victim(path)
                    self.release_all_operation_locks(victim)
                    
                    deadlock.broken = True
                    deadlock.victim_operation_id = victim
                    self._deadlock_history.append(deadlock)
    
    def _detect_cycle_dfs(
        self,
        operation: str,
        visited: set[str],
        rec_stack: set[str],
        path: list[str]
    ) -> bool:
        """DFS to detect cycles in wait-for graph"""
        visited.add(operation)
        rec_stack.add(operation)
        path.append(operation)
        
        # Find resources this operation is waiting for
        waiting_for = [
            res_id for res_id, waiters in self._resource_waiters.items()
            if operation in waiters
        ]
        
        # Find operations holding those resources
        for res_id in waiting_for:
            lock = self._resource_locks.get(res_id)
            if lock:
                holder = lock.operation_id
                if holder not in visited:
                    if self._detect_cycle_dfs(holder, visited, rec_stack, path):
                        return True
                elif holder in rec_stack:
                    # Cycle detected
                    # Trim path to cycle
                    cycle_start = path.index(holder)
                    path[:] = path[cycle_start:]
                    return True
        
        rec_stack.remove(operation)
        path.pop()
        return False
    
    def _choose_deadlock_victim(self, cycle: list[str]) -> str:
        """
        Choose which operation to abort to break deadlock
        
        Strategy: Choose operation with fewest held resources
        """
        min_resources = float('inf')
        victim = cycle[0]
        
        for operation in cycle:
            resource_count = len(self._operation_resources.get(operation, set()))
            if resource_count < min_resources:
                min_resources = resource_count
                victim = operation
        
        return victim
    
    def _record_conflict(
        self,
        conflict_type: ConflictType,
        resource_ids: list[str],
        operation_ids: list[str],
        thread_ids: list[int]
    ) -> str:
        """Record detected conflict"""
        conflict_id = str(uuid.uuid4())
        
        # Determine resolution strategy
        if conflict_type == ConflictType.DEADLOCK:
            strategy = ResolutionStrategy.RETRY
        elif conflict_type == ConflictType.RACE_CONDITION:
            strategy = ResolutionStrategy.FIRST_WINS
        elif conflict_type == ConflictType.RESOURCE_CONTENTION:
            strategy = ResolutionStrategy.RETRY
        else:
            strategy = ResolutionStrategy.ESCALATE
        
        conflict = ConflictDetection(
            conflict_id=conflict_id,
            conflict_type=conflict_type,
            detected_at=datetime.now(UTC),
            resource_ids=resource_ids,
            operation_ids=operation_ids,
            thread_ids=thread_ids,
            resolution_strategy=strategy
        )
        
        self._conflicts[conflict_id] = conflict
        return conflict_id
    
    def detect_race_condition(
        self,
        resource_id: str,
        expected_state: Any,
        actual_state: Any
    ) -> dict[str, Any]:
        """
        Detect race condition on resource state
        
        Args:
            resource_id: Resource being checked
            expected_state: Expected state value
            actual_state: Actual state value
        
        Returns:
            dict with detected flag and conflict_id if detected
        """
        if expected_state != actual_state:
            conflict_id = self._record_conflict(
                ConflictType.RACE_CONDITION,
                [resource_id],
                [],  # Unknown operations
                [threading.get_ident()]
            )
            
            return {
                "detected": True,
                "conflict_id": conflict_id,
                "expected_state": expected_state,
                "actual_state": actual_state,
                "resolution_strategy": ResolutionStrategy.FIRST_WINS.value
            }
        
        return {
            "detected": False
        }
    
    def execute_with_lock(
        self,
        resource_id: str,
        operation_id: str,
        operation: Callable[[], Any],
        timeout_seconds: int = 30
    ) -> dict[str, Any]:
        """
        Execute operation with resource lock (context manager pattern)
        
        Args:
            resource_id: Resource to lock
            operation_id: Operation ID
            operation: Callable to execute while holding lock
            timeout_seconds: Lock timeout
        
        Returns:
            dict with result or error
        """
        # Acquire lock
        lock_result = self.acquire_resource_lock(resource_id, operation_id, timeout_seconds)
        
        if lock_result["status"] != LockStatus.ACQUIRED.value:
            return {
                "success": False,
                "error": "failed_to_acquire_lock",
                "lock_result": lock_result
            }
        
        lock_id = lock_result["lock_id"]
        
        try:
            # Execute operation
            result = operation()
            return {
                "success": True,
                "result": result,
                "lock_id": lock_id
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "exception_type": type(e).__name__
            }
        finally:
            # Always release lock
            self.release_resource_lock(lock_id)
    
    def get_conflict(self, conflict_id: str) -> ConflictDetection | None:
        """Retrieve conflict by ID"""
        with self._lock:
            return self._conflicts.get(conflict_id)
    
    def get_deadlock_history(self) -> list[DeadlockCycle]:
        """Retrieve deadlock detection history"""
        with self._lock:
            return list(self._deadlock_history)
    
    def get_active_locks(self) -> list[ResourceLock]:
        """Get all active resource locks"""
        with self._lock:
            return list(self._resource_locks.values())
    
    def shutdown(self) -> None:
        """Shutdown background detector thread"""
        self._stop_detector.set()
        if self._detector_thread.is_alive():
            self._detector_thread.join(timeout=2.0)

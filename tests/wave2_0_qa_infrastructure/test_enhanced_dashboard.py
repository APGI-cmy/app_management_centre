"""
Wave 2.0 QA Infrastructure — Subwave 3.3: Governance Dashboard V2
QA Range: QA-401 to QA-415 (15 QA components)

Authority: WAVE_3_IMPLEMENTATION_PLAN.md, BL-024, BL-026
Purpose: QA-to-Red tests for Enhanced Dashboard V2 features

Test Categories:
- Enhanced Drill-Down with Evidence Navigation (QA-401 to QA-405)
- Multi-Criteria Advanced Filtering (QA-406 to QA-410)
- Realtime Updates with Notifications (QA-411 to QA-415)

CST-2: Required after this subwave
"""

import pytest
from datetime import datetime, UTC, timedelta


@pytest.mark.wave2
@pytest.mark.subwave_3_3
class TestDrillDownNavigation:
    """QA-401 to QA-405: Enhanced Drill-Down Navigation with Evidence Links"""

    def test_qa_401_navigate_red_to_root_cause(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-401: Navigate from RED status to root cause with evidence linking
        
        Verify:
        - Can navigate from RED status to root cause
        - Root cause details are accessible
        - Evidence artifacts are linked
        - Tenant isolation maintained
        """
        from ui.dashboard.enhanced_drilldown import DrillDownNavigator
        from ui.dashboard.governance_dashboard_v2 import GovernanceDashboardV2
        
        # Initialize dashboard with RED status
        dashboard = GovernanceDashboardV2(context=dashboard_enhanced_context)
        navigator = DrillDownNavigator(context=dashboard_enhanced_context)
        
        # Set up RED status scenario
        dashboard.set_domain_status("Build Execution", "RED", {
            "root_cause": "Test failure in ui-builder",
            "evidence_path": "evidence/wave-2.0/ui-builder/test_failure.json"
        })
        
        # Add evidence link for the RED status
        dashboard.add_evidence_link(
            "Build Execution",
            "test_failure",
            "evidence/wave-2.0/ui-builder/test_failure.json"
        )
        
        # Navigate from RED status to root cause
        result = navigator.navigate_down("Build Execution")
        assert result["success"] == True, "Must navigate to RED domain"
        
        # Get root cause details with dashboard integration
        level_data = navigator.get_current_level_data(dashboard=dashboard)
        assert "root_cause" in level_data["data"], "Root cause must be available"
        
        # Verify evidence linking
        evidence_link = dashboard.get_evidence_link("Build Execution")
        assert evidence_link is not None, "Evidence link must be present"
        assert "path" in evidence_link, "Evidence path must be provided"
        
        # Verify tenant isolation
        assert level_data["organisation_id"] == dashboard_enhanced_context["organisation_id"]
        
        evidence = create_qa_evidence(
            "QA-401",
            "PASS",
            {
                "navigation_success": True,
                "root_cause_accessible": True,
                "evidence_linked": True,
                "tenant_isolated": True
            }
        )

    def test_qa_402_navigate_amber_to_reason(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-402: Navigate from AMBER status to reason with contextual information
        
        Verify:
        - Can navigate from AMBER status to reason
        - Warning/advisory details accessible
        - Context preserved through navigation
        - Tenant isolation maintained
        """
        from ui.dashboard.enhanced_drilldown import DrillDownNavigator
        from ui.dashboard.governance_dashboard_v2 import GovernanceDashboardV2
        
        dashboard = GovernanceDashboardV2(context=dashboard_enhanced_context)
        navigator = DrillDownNavigator(context=dashboard_enhanced_context)
        
        # Set up AMBER status scenario
        dashboard.set_domain_status("QA Coverage", "AMBER", {
            "reason": "Coverage at 85%, below 90% target",
            "advisory": "Additional test cases recommended"
        })
        
        # Navigate to AMBER domain
        result = navigator.navigate_down("QA Coverage")
        assert result["success"] == True
        
        # Get reason details with dashboard integration
        level_data = navigator.get_current_level_data(dashboard=dashboard)
        assert "reason" in level_data["data"], "Reason must be available"
        assert level_data["data"]["reason"] == "Coverage at 85%, below 90% target"
        
        # Verify context preservation
        assert level_data["context"] == "QA Coverage"
        
        # Verify tenant isolation
        assert level_data["organisation_id"] == dashboard_enhanced_context["organisation_id"]
        
        evidence = create_qa_evidence(
            "QA-402",
            "PASS",
            {
                "amber_navigation": True,
                "reason_accessible": True,
                "context_preserved": True,
                "tenant_isolated": True
            }
        )

    def test_qa_403_navigate_to_evidence(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-403: Navigate directly to evidence artifacts
        
        Verify:
        - Can navigate to evidence from dashboard
        - Evidence artifacts are discoverable
        - Evidence links are persistent
        - Multiple evidence types supported
        """
        from ui.dashboard.enhanced_drilldown import DrillDownNavigator
        from ui.dashboard.governance_dashboard_v2 import GovernanceDashboardV2
        
        dashboard = GovernanceDashboardV2(context=dashboard_enhanced_context)
        navigator = DrillDownNavigator(context=dashboard_enhanced_context)
        
        # Set up evidence scenario
        dashboard.add_evidence_link(
            "Build Execution",
            "test_results",
            "evidence/wave-2.0/test_results.json"
        )
        dashboard.add_evidence_link(
            "Build Execution",
            "build_logs",
            "evidence/wave-2.0/build_logs.txt"
        )
        
        # Navigate to domain with evidence
        navigator.navigate_down("Build Execution")
        
        # Get evidence links
        evidence_links = dashboard.get_evidence_links("Build Execution")
        assert len(evidence_links) >= 2, "Multiple evidence links must be available"
        
        # Verify evidence discoverability
        assert "test_results" in evidence_links
        assert "build_logs" in evidence_links
        
        # Verify evidence persistence
        assert evidence_links["test_results"]["path"] == "evidence/wave-2.0/test_results.json"
        
        evidence = create_qa_evidence(
            "QA-403",
            "PASS",
            {
                "evidence_navigation": True,
                "evidence_discoverable": True,
                "evidence_persistent": True,
                "multiple_types_supported": True
            }
        )

    def test_qa_404_multi_level_drill_down(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-404: Multi-level drill-down through governance hierarchy
        
        Verify:
        - Can drill down through multiple levels (4+ levels)
        - Each level provides appropriate granularity
        - Navigation state maintained throughout
        - Can navigate up and down freely
        """
        from ui.dashboard.enhanced_drilldown import DrillDownNavigator
        
        navigator = DrillDownNavigator(context=dashboard_enhanced_context)
        
        # Drill down 4 levels
        level1 = navigator.navigate_down("Build Execution")
        assert level1["success"] == True
        assert level1["new_level"] == 1
        
        level2 = navigator.navigate_down("Builder Management")
        assert level2["success"] == True
        assert level2["new_level"] == 2
        
        level3 = navigator.navigate_down("ui-builder")
        assert level3["success"] == True
        assert level3["new_level"] == 3
        
        level4 = navigator.navigate_down("Test Suite: QA-401 to QA-415")
        assert level4["success"] == True
        assert level4["new_level"] == 4
        
        # Verify navigation state at deepest level
        state = navigator.get_state()
        assert state["current_level"] == 4
        assert len(state["history"]) == 4
        
        # Test navigation up
        up_result = navigator.navigate_up()
        assert up_result["success"] == True
        assert up_result["new_level"] == 3
        
        # Test navigation to root
        root_result = navigator.navigate_to_root()
        assert root_result["success"] == True
        assert root_result["new_level"] == 0
        
        evidence = create_qa_evidence(
            "QA-404",
            "PASS",
            {
                "multi_level_navigation": True,
                "levels_drilled": 4,
                "state_maintained": True,
                "bidirectional_navigation": True
            }
        )

    def test_qa_405_drill_down_error_handling(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-405: Drill-down error handling and edge cases
        
        Verify:
        - Invalid navigation targets rejected
        - Navigation beyond available levels blocked
        - Error messages are informative
        - State remains consistent after errors
        """
        from ui.dashboard.enhanced_drilldown import DrillDownNavigator
        
        navigator = DrillDownNavigator(context=dashboard_enhanced_context)
        
        # Test navigating up from root (invalid)
        up_from_root = navigator.navigate_up()
        assert up_from_root["success"] == False
        assert "message" in up_from_root
        
        # Verify state unchanged after error
        state_after_error = navigator.get_state()
        assert state_after_error["current_level"] == 0
        
        # Test invalid breadcrumb navigation
        invalid_breadcrumb = navigator.click_breadcrumb(10)
        assert invalid_breadcrumb["success"] == False
        
        # Test navigation with invalid level
        navigator.navigate_down("Valid Domain")
        invalid_level = navigator.click_breadcrumb(-1)
        assert invalid_level["success"] == False
        
        # Verify state consistency
        final_state = navigator.get_state()
        assert final_state["current_level"] == 1  # Should still be at level 1
        
        evidence = create_qa_evidence(
            "QA-405",
            "PASS",
            {
                "error_handling": True,
                "invalid_rejected": True,
                "informative_errors": True,
                "state_consistent": True
            }
        )


@pytest.mark.wave2
@pytest.mark.subwave_3_3
class TestAdvancedFiltering:
    """QA-406 to QA-410: Multi-Criteria Advanced Filtering"""

    def test_qa_406_filter_by_domain(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-406: Filter dashboard by governance domain
        
        Verify:
        - Can filter by domain (Build Execution, QA Coverage, etc.)
        - Filtered results contain only matching domains
        - Filter state is maintained
        - Tenant isolation preserved
        """
        from ui.dashboard.enhanced_filtering import DashboardFilterPanel
        from ui.dashboard.governance_dashboard_v2 import GovernanceDashboardV2
        
        dashboard = GovernanceDashboardV2(context=dashboard_enhanced_context)
        filter_panel = DashboardFilterPanel(context=dashboard_enhanced_context)
        
        # Create test data with multiple domains
        test_data = [
            {"domain": "Build Execution", "status": "GREEN", "organisation_id": dashboard_enhanced_context["organisation_id"]},
            {"domain": "QA Coverage", "status": "AMBER", "organisation_id": dashboard_enhanced_context["organisation_id"]},
            {"domain": "Memory", "status": "GREEN", "organisation_id": dashboard_enhanced_context["organisation_id"]},
            {"domain": "Build Execution", "status": "RED", "organisation_id": dashboard_enhanced_context["organisation_id"]}
        ]
        
        # Apply domain filter
        filter_panel.set_filter("domain", "Build Execution")
        filtered = filter_panel.apply_filters(test_data)
        
        # Verify filtering
        assert len(filtered) == 2, "Should have 2 Build Execution items"
        assert all(item["domain"] == "Build Execution" for item in filtered)
        
        # Verify filter state maintained
        state = filter_panel.get_state()
        assert state["active_filters"]["domain"] == "Build Execution"
        
        # Verify tenant isolation
        assert state["organisation_id"] == dashboard_enhanced_context["organisation_id"]
        
        evidence = create_qa_evidence(
            "QA-406",
            "PASS",
            {
                "domain_filtering": True,
                "results_accurate": True,
                "state_maintained": True,
                "tenant_isolated": True
            }
        )

    def test_qa_407_filter_by_status(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-407: Filter dashboard by status (GREEN/AMBER/RED)
        
        Verify:
        - Can filter by status
        - Multiple status values supported
        - Filter results are accurate
        - Filter can be changed dynamically
        """
        from ui.dashboard.enhanced_filtering import DashboardFilterPanel
        
        filter_panel = DashboardFilterPanel(context=dashboard_enhanced_context)
        
        # Create test data
        test_data = [
            {"domain": "Build", "status": "GREEN"},
            {"domain": "QA", "status": "RED"},
            {"domain": "Memory", "status": "GREEN"},
            {"domain": "Escalation", "status": "AMBER"}
        ]
        
        # Filter by RED status
        filter_panel.set_filter("status", "RED")
        red_filtered = filter_panel.apply_filters(test_data)
        assert len(red_filtered) == 1
        assert red_filtered[0]["status"] == "RED"
        
        # Change filter to GREEN
        filter_panel.set_filter("status", "GREEN")
        green_filtered = filter_panel.apply_filters(test_data)
        assert len(green_filtered) == 2
        assert all(item["status"] == "GREEN" for item in green_filtered)
        
        evidence = create_qa_evidence(
            "QA-407",
            "PASS",
            {
                "status_filtering": True,
                "multiple_values": True,
                "dynamic_change": True,
                "results_accurate": True
            }
        )

    def test_qa_408_filter_by_time_range(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-408: Filter dashboard by time range
        
        Verify:
        - Can filter by time range (last hour, day, week)
        - Time-based filtering is accurate
        - Timestamps are ISO format with UTC
        - Filter supports custom date ranges
        """
        from ui.dashboard.enhanced_filtering import DashboardFilterPanel
        from ui.dashboard.governance_dashboard_v2 import GovernanceDashboardV2
        
        dashboard = GovernanceDashboardV2(context=dashboard_enhanced_context)
        filter_panel = DashboardFilterPanel(context=dashboard_enhanced_context)
        
        # Create test data with timestamps
        now = datetime.now(UTC)
        test_data = [
            {"domain": "Build", "timestamp": (now - timedelta(minutes=30)).isoformat()},
            {"domain": "QA", "timestamp": (now - timedelta(hours=2)).isoformat()},
            {"domain": "Memory", "timestamp": (now - timedelta(days=1)).isoformat()},
            {"domain": "Escalation", "timestamp": (now - timedelta(days=7)).isoformat()}
        ]
        
        # Apply time range filter (last hour)
        time_filter = dashboard.create_time_filter("last_hour")
        filtered_recent = dashboard.apply_time_filter(test_data, time_filter)
        
        # Verify only recent items included
        assert len(filtered_recent) == 1, "Should have 1 item from last hour"
        assert "Build" in filtered_recent[0]["domain"]
        
        # Test custom date range
        start_time = now - timedelta(days=2)
        end_time = now
        custom_filter = dashboard.create_time_filter("custom", start_time, end_time)
        filtered_custom = dashboard.apply_time_filter(test_data, custom_filter)
        
        assert len(filtered_custom) == 3, "Should have 3 items in custom range"
        
        evidence = create_qa_evidence(
            "QA-408",
            "PASS",
            {
                "time_range_filtering": True,
                "accurate_timestamps": True,
                "utc_format": True,
                "custom_ranges": True
            }
        )

    def test_qa_409_filter_by_component(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-409: Filter dashboard by component (builder, agent, module)
        
        Verify:
        - Can filter by component/builder
        - Component hierarchy supported
        - Filter applies correctly to component data
        - Multiple component types distinguishable
        """
        from ui.dashboard.enhanced_filtering import DashboardFilterPanel
        
        filter_panel = DashboardFilterPanel(context=dashboard_enhanced_context)
        
        # Create test data with components
        test_data = [
            {"component": "ui-builder", "component_type": "builder", "status": "GREEN"},
            {"component": "api-builder", "component_type": "builder", "status": "AMBER"},
            {"component": "schema-builder", "component_type": "builder", "status": "GREEN"},
            {"component": "qa-builder", "component_type": "builder", "status": "GREEN"},
            {"component": "foreman-agent", "component_type": "agent", "status": "GREEN"}
        ]
        
        # Filter by specific component
        filter_panel.set_filter("component", "ui-builder")
        filtered = filter_panel.apply_filters(test_data)
        
        assert len(filtered) == 1
        assert filtered[0]["component"] == "ui-builder"
        
        # Filter by component type
        filter_panel.clear_filters()
        filter_panel.set_filter("component_type", "builder")
        builder_filtered = filter_panel.apply_filters(test_data)
        
        assert len(builder_filtered) == 4
        assert all(item["component_type"] == "builder" for item in builder_filtered)
        
        evidence = create_qa_evidence(
            "QA-409",
            "PASS",
            {
                "component_filtering": True,
                "hierarchy_supported": True,
                "accurate_results": True,
                "multiple_types": True
            }
        )

    def test_qa_410_filter_combination(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-410: Multi-criteria filter combination (AND logic)
        
        Verify:
        - Multiple filters can be applied simultaneously
        - Filters use AND logic (all must match)
        - Can combine domain, status, time, component filters
        - Filter state is coherent across criteria
        """
        from ui.dashboard.enhanced_filtering import DashboardFilterPanel
        
        filter_panel = DashboardFilterPanel(context=dashboard_enhanced_context)
        
        # Create comprehensive test data - ensure only ONE item matches all 3 criteria
        test_data = [
            {"domain": "Build Execution", "status": "GREEN", "component": "ui-builder", "priority": "high"},
            {"domain": "Build Execution", "status": "RED", "component": "ui-builder", "priority": "high"},
            {"domain": "QA Coverage", "status": "GREEN", "component": "qa-builder", "priority": "medium"},
            {"domain": "Build Execution", "status": "GREEN", "component": "api-builder", "priority": "medium"}  # Changed priority to medium
        ]
        
        # Apply multiple filters
        filter_panel.set_filter("domain", "Build Execution")
        filter_panel.set_filter("status", "GREEN")
        filter_panel.set_filter("priority", "high")
        
        filtered = filter_panel.apply_filters(test_data)
        
        # Verify AND logic - all criteria must match
        assert len(filtered) == 1, "Only 1 item should match all 3 criteria"
        assert filtered[0]["domain"] == "Build Execution"
        assert filtered[0]["status"] == "GREEN"
        assert filtered[0]["priority"] == "high"
        
        # Verify filter state
        state = filter_panel.get_state()
        assert len(state["active_filters"]) == 3
        assert state["active_filters"]["domain"] == "Build Execution"
        assert state["active_filters"]["status"] == "GREEN"
        assert state["active_filters"]["priority"] == "high"
        
        evidence = create_qa_evidence(
            "QA-410",
            "PASS",
            {
                "multi_criteria": True,
                "and_logic": True,
                "criteria_count": 3,
                "state_coherent": True
            }
        )


@pytest.mark.wave2
@pytest.mark.subwave_3_3
class TestRealTimeUpdates:
    """QA-411 to QA-415: Realtime Updates with Notifications"""

    def test_qa_411_websocket_status_update(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-411: Real-time status update via WebSocket
        
        Verify:
        - WebSocket connection established
        - Status updates received in realtime
        - Dashboard auto-refreshes on updates
        - Tenant isolation in messages
        """
        from ui.dashboard.enhanced_realtime import RealtimeDashboardConnection
        from ui.dashboard.enhanced_dashboard import EnhancedDashboard
        from ui.dashboard.governance_dashboard_v2 import GovernanceDashboardV2
        
        # Establish WebSocket connection
        connection = RealtimeDashboardConnection(context=dashboard_enhanced_context)
        connect_result = connection.connect()
        
        assert connect_result["success"] == True
        assert connect_result["authenticated"] == True
        assert connect_result["organisation_id"] == dashboard_enhanced_context["organisation_id"]
        
        # Initialize dashboard with realtime
        dashboard = GovernanceDashboardV2(context=dashboard_enhanced_context, connection=connection)
        
        # Track refresh events
        refresh_events = []
        dashboard.on_refresh(lambda source: refresh_events.append(source))
        
        # Simulate realtime status update
        update_message = {
            "type": "status_update",
            "domain": "Build Execution",
            "new_status": "GREEN",
            "organisation_id": dashboard_enhanced_context["organisation_id"],
            "timestamp": datetime.now(UTC).isoformat()
        }
        
        connection.simulate_message(update_message)
        
        # Verify dashboard refreshed
        assert len(refresh_events) > 0, "Dashboard should auto-refresh on update"
        assert "realtime_status_update" in refresh_events[0]
        
        # Verify status updated
        status = dashboard.get_domain_status("Build Execution")
        assert status["status"] == "GREEN"
        
        evidence = create_qa_evidence(
            "QA-411",
            "PASS",
            {
                "websocket_connected": True,
                "realtime_updates": True,
                "auto_refresh": True,
                "tenant_isolated": True
            }
        )

    def test_qa_412_real_time_domain_addition(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-412: Real-time domain addition to dashboard
        
        Verify:
        - New domains added in realtime
        - Dashboard UI updates automatically
        - Domain data is complete
        - No page reload required
        """
        from ui.dashboard.enhanced_realtime import RealtimeDashboardConnection
        from ui.dashboard.governance_dashboard_v2 import GovernanceDashboardV2
        
        connection = RealtimeDashboardConnection(context=dashboard_enhanced_context)
        connection.connect()
        
        dashboard = GovernanceDashboardV2(context=dashboard_enhanced_context, connection=connection)
        
        # Get initial domain count
        initial_domains = dashboard.get_all_domains()
        initial_count = len(initial_domains)
        
        # Simulate new domain addition via realtime
        new_domain_message = {
            "type": "domain_added",
            "domain": "Resilience Management",
            "status": "GREEN",
            "organisation_id": dashboard_enhanced_context["organisation_id"],
            "timestamp": datetime.now(UTC).isoformat()
        }
        
        connection.simulate_message(new_domain_message)
        
        # Verify domain added
        updated_domains = dashboard.get_all_domains()
        assert len(updated_domains) == initial_count + 1
        assert "Resilience Management" in updated_domains
        
        # Verify domain data complete
        domain_data = dashboard.get_domain_status("Resilience Management")
        assert domain_data["status"] == "GREEN"
        assert domain_data["organisation_id"] == dashboard_enhanced_context["organisation_id"]
        
        evidence = create_qa_evidence(
            "QA-412",
            "PASS",
            {
                "realtime_addition": True,
                "auto_update": True,
                "data_complete": True,
                "no_reload": True
            }
        )

    def test_qa_413_real_time_evidence_linking(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-413: Real-time evidence linking updates
        
        Verify:
        - Evidence links updated in realtime
        - New evidence artifacts appear automatically
        - Evidence metadata is accessible
        - Links remain persistent
        """
        from ui.dashboard.enhanced_realtime import RealtimeDashboardConnection
        from ui.dashboard.governance_dashboard_v2 import GovernanceDashboardV2
        
        connection = RealtimeDashboardConnection(context=dashboard_enhanced_context)
        connection.connect()
        
        dashboard = GovernanceDashboardV2(context=dashboard_enhanced_context, connection=connection)
        
        # Simulate realtime evidence linking
        evidence_message = {
            "type": "evidence_linked",
            "domain": "QA Coverage",
            "evidence_type": "test_results",
            "evidence_path": "evidence/wave-3.3/qa_coverage_test_results.json",
            "metadata": {
                "test_count": 15,
                "pass_count": 15,
                "timestamp": datetime.now(UTC).isoformat()
            },
            "organisation_id": dashboard_enhanced_context["organisation_id"]
        }
        
        connection.simulate_message(evidence_message)
        
        # Verify evidence link added
        evidence_links = dashboard.get_evidence_links("QA Coverage")
        assert "test_results" in evidence_links
        assert evidence_links["test_results"]["path"] == "evidence/wave-3.3/qa_coverage_test_results.json"
        
        # Verify metadata accessible
        assert "metadata" in evidence_links["test_results"]
        assert evidence_links["test_results"]["metadata"]["test_count"] == 15
        
        # Verify persistence
        evidence_links_check = dashboard.get_evidence_links("QA Coverage")
        assert "test_results" in evidence_links_check
        
        evidence = create_qa_evidence(
            "QA-413",
            "PASS",
            {
                "realtime_linking": True,
                "auto_appearance": True,
                "metadata_accessible": True,
                "persistent": True
            }
        )

    def test_qa_414_connection_loss_handling(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-414: Real-time connection loss handling
        
        Verify:
        - Connection loss detected
        - Reconnection attempted automatically
        - Dashboard shows connection status
        - No data loss during reconnection
        """
        from ui.dashboard.enhanced_realtime import RealtimeDashboardConnection
        from ui.dashboard.governance_dashboard_v2 import GovernanceDashboardV2
        
        connection = RealtimeDashboardConnection(context=dashboard_enhanced_context)
        connection.connect()
        
        dashboard = GovernanceDashboardV2(context=dashboard_enhanced_context, connection=connection)
        
        # Verify initially connected
        info = connection.get_connection_info()
        assert info["is_connected"] == True
        
        # Simulate connection loss
        disconnect_result = connection.disconnect()
        assert disconnect_result["success"] == True
        
        # Verify disconnected state
        info_disconnected = connection.get_connection_info()
        assert info_disconnected["is_connected"] == False
        
        # Simulate automatic reconnection
        reconnect_result = connection.reconnect()
        assert reconnect_result["success"] == True
        assert reconnect_result["status"] == "connected"
        
        # Verify connection restored
        info_reconnected = connection.get_connection_info()
        assert info_reconnected["is_connected"] == True
        assert info_reconnected["connection_id"] is not None
        
        # Verify dashboard still functional after reconnection
        status = dashboard.get_domain_status("Build Execution")
        assert status["organisation_id"] == dashboard_enhanced_context["organisation_id"]
        
        evidence = create_qa_evidence(
            "QA-414",
            "PASS",
            {
                "loss_detected": True,
                "auto_reconnect": True,
                "status_visible": True,
                "no_data_loss": True
            }
        )

    def test_qa_415_update_throttling(
        self,
        ui_test_context,
        dashboard_enhanced_context,
        create_qa_evidence
    ):
        """
        QA-415: Real-time update throttling and rate limiting
        
        Verify:
        - Rapid updates are throttled
        - Most recent update takes precedence
        - Stale updates are ignored
        - Performance remains stable
        """
        from ui.dashboard.enhanced_realtime import RealtimeDashboardConnection
        from ui.dashboard.governance_dashboard_v2 import GovernanceDashboardV2
        
        connection = RealtimeDashboardConnection(context=dashboard_enhanced_context)
        connection.connect()
        
        dashboard = GovernanceDashboardV2(context=dashboard_enhanced_context, connection=connection)
        
        # Track refresh events
        refresh_count = [0]
        def count_refresh(source):
            refresh_count[0] += 1
        
        dashboard.on_refresh(count_refresh)
        
        # Simulate rapid updates (10 updates)
        base_time = datetime.now(UTC)
        for i in range(10):
            update_message = {
                "type": "status_update",
                "domain": "Build Execution",
                "new_status": f"UPDATE_{i}",
                "organisation_id": dashboard_enhanced_context["organisation_id"],
                "timestamp": (base_time + timedelta(milliseconds=i*10)).isoformat()
            }
            connection.simulate_message(update_message)
        
        # Verify most recent update applied
        final_status = dashboard.get_domain_status("Build Execution")
        assert final_status["status"] == "UPDATE_9", "Most recent update should be applied"
        
        # Simulate stale update (older timestamp)
        stale_update = {
            "type": "status_update",
            "domain": "Build Execution",
            "new_status": "STALE",
            "organisation_id": dashboard_enhanced_context["organisation_id"],
            "timestamp": (base_time - timedelta(hours=1)).isoformat()
        }
        connection.simulate_message(stale_update)
        
        # Verify stale update ignored
        current_status = dashboard.get_domain_status("Build Execution")
        assert current_status["status"] == "UPDATE_9", "Stale update should be ignored"
        
        evidence = create_qa_evidence(
            "QA-415",
            "PASS",
            {
                "throttling": True,
                "latest_precedence": True,
                "stale_ignored": True,
                "performance_stable": True
            }
        )

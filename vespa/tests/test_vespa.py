from datadog_checks.vespa import VespaCheck
from datadog_checks.errors import CheckException
import os
import json
import pytest
from mock import MagicMock

HERE = os.path.dirname(os.path.abspath(__file__))


def test_no_config_raises():
    check = VespaCheck("vespa", {}, {})
    with pytest.raises(CheckException):
        check.check({})


def test_cannot_connect_is_critical(aggregator):
    check = VespaCheck("vespa", {}, {})
    check.URL = 'http://localhost:19333/state/v1/metrics'
    check.check({'consumer': 'default'})
    aggregator.assert_service_check(check.VESPA_SERVICE_CHECK,
                                    VespaCheck.CRITICAL)


def test_service_reports_down(aggregator):
    check = VespaCheck("vespa", {}, {})
    with open(os.path.join(HERE, 'node_down.json'), 'r') as f:
        check._get_state_metrics = MagicMock(return_value=json.load(f))
    check.check({'consumer': 'default'})
    aggregator.assert_service_check(check.VESPA_SERVICE_CHECK,
                                    VespaCheck.WARNING,
                                    message="Service reports down")


def test_service_reports_unknown(aggregator):
    check = VespaCheck("vespa", {}, {})
    with open(os.path.join(HERE, 'node_unknown.json'), 'r') as f:
        check._get_state_metrics = MagicMock(return_value=json.load(f))
    check.check({'consumer': 'default'})
    aggregator.assert_service_check(check.VESPA_SERVICE_CHECK,
                                    VespaCheck.WARNING,
                                    message="Service reports unknown status")


def test_check_metrics(aggregator):
    check = VespaCheck("vespa", {}, {})
    with open(os.path.join(HERE, 'large_content_metrics.json'), 'r') as f:
        check._get_state_metrics = MagicMock(return_value=json.load(f))

    check.check({'consumer': 'default'})
    aggregator.assert_service_check(check.VESPA_SERVICE_CHECK, VespaCheck.OK)

    aggregator.assert_metric("content.proton.resource_usage.disk",
                             value=0.216666, tags=['documenttype:ad', 'cluster:search'])
    assert 42 == check.count

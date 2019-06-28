from datadog_checks.vespa import VespaCheck
from datadog_checks.errors import CheckException
import os
import json
import pytest
from mock import MagicMock

HERE = os.path.dirname(os.path.abspath(__file__))


def test_no_consumer_raises():
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
    with open(os.path.join(HERE, 'service_down.json'), 'r') as f:
        check._get_metrics_json = MagicMock(return_value=json.load(f))
    check.check({'consumer': 'default'})
    aggregator.assert_service_check(check.VESPA_SERVICE_CHECK,
                                    VespaCheck.WARNING,
                                    count=1,
                                    message='Service vespa.down-service reports down: No response',
                                    tags=['instance:down-service', 'vespaVersion:7.0.0'])
    aggregator.assert_service_check(check.VESPA_SERVICE_CHECK, VespaCheck.OK, count=0)


def test_service_reports_unknown(aggregator):
    check = VespaCheck("vespa", {}, {})
    with open(os.path.join(HERE, 'service_unknown.json'), 'r') as f:
        check._get_metrics_json = MagicMock(return_value=json.load(f))
    check.check({'consumer': 'default'})
    aggregator.assert_service_check(check.VESPA_SERVICE_CHECK,
                                    VespaCheck.WARNING,
                                    count=1,
                                    message='Service vespa.unknown-service reports unknown status: Empty status page',
                                    tags=['instance:unknown-service', 'vespaVersion:7.0.0'])
    aggregator.assert_service_check(check.VESPA_SERVICE_CHECK, VespaCheck.OK, count=0)


def test_down_service_does_not_raise(aggregator):
    check = VespaCheck("vespa", {}, {})
    with open(os.path.join(HERE, 'service_up_and_down.json'), 'r') as f:
        check._get_metrics_json = MagicMock(return_value=json.load(f))
    check.check({'consumer': 'default'})
    aggregator.assert_service_check(check.VESPA_SERVICE_CHECK,
                                    VespaCheck.WARNING,
                                    count=1,
                                    message='Service vespa.down-service reports down: No response',
                                    tags=['instance:down-service', 'vespaVersion:7.0.0'])
    aggregator.assert_service_check(check.VESPA_SERVICE_CHECK,
                                    VespaCheck.OK,
                                    count=1,
                                    message='Service vespa.up-service returns up',
                                    tags=['instance:up-service', 'vespaVersion:7.0.0'])
    assert 3 == check.metric_count


def test_check_metrics(aggregator):
    check = VespaCheck("vespa", {}, {})
    with open(os.path.join(HERE, 'metrics_all.json'), 'r') as f:
        check._get_metrics_json = MagicMock(return_value=json.load(f))

    check.check({'consumer': 'default'})
    aggregator.assert_service_check(check.VESPA_SERVICE_CHECK, VespaCheck.OK, count=7)
    aggregator.assert_service_check(check.VESPA_SERVICE_CHECK, VespaCheck.WARNING, count=0)

    aggregator.assert_metric("vespa.container.http.status.2xx.rate",
                             value=10,
                             tags=['metrictype:standard', 'instance:container', 'scheme:http',
                                   'httpMethod:GET', 'clustername:default', 'vespaVersion:7.0.0'])
    assert 38 == check.metric_count

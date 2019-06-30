import requests
import logging
import sys
from datadog_checks.base import AgentCheck
from datadog_checks.errors import CheckException
from requests.exceptions import Timeout, HTTPError, InvalidURL, ConnectionError
from simplejson import JSONDecodeError


class VespaCheck(AgentCheck):
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    VESPA_METRICS_SERVICE_CHECK = 'vespa.metrics-health'
    VESPA_PROCESS_SERVICE_CHECK = 'vespa.process-health'
    URL = 'http://localhost:19092/metrics/v1/values'
    metric_count = 0
    services_up = 0

    def check(self, instance):
        self.metric_count = 0
        self.services_up = 0

        instance_tags = instance.get('tags', [])
        consumer = instance.get('consumer')
        if not consumer:
            raise CheckException("The consumer must be specified in the configuration.")
        url = self.URL + '?consumer=' + consumer
        try:
            json = self._get_metrics_json(url, 10.0, instance_tags)
            if 'services' not in json:
                self.service_check(self.VESPA_METRICS_SERVICE_CHECK, AgentCheck.WARNING, tags=instance_tags,
                                   message="No services in response from metrics proxy on {}".format(url))
                return

            for service in json['services']:
                service_name = service['name']
                self._report_service_status(instance_tags, service_name, service)
                for metrics in service['metrics']:
                    self._emit_metrics(service_name, metrics, instance_tags)

            self.log.info("Forwarded {} metrics to hq for {} services".format(self.metric_count, self.services_up))
            self.service_check(self.VESPA_METRICS_SERVICE_CHECK, AgentCheck.OK, tags=instance_tags,
                               message="Metrics collected successfully for consumer {}".format(consumer))
        except Timeout as e:
            self.service_check(self.VESPA_METRICS_SERVICE_CHECK, AgentCheck.CRITICAL, tags=instance_tags,
                               message="Request timeout: {}, {}".format(url, e))
        except (HTTPError, InvalidURL, ConnectionError) as e:
            self.service_check(self.VESPA_METRICS_SERVICE_CHECK, AgentCheck.CRITICAL, tags=instance_tags,
                               message="Request failed: {0}, {1}".format(url, e))
        except JSONDecodeError as e:
            self.service_check(self.VESPA_METRICS_SERVICE_CHECK, AgentCheck.CRITICAL, tags=instance_tags,
                               message='JSON Parse failed: {0}, {1}'.format(url, e))
        except Exception as e:
            self.service_check(self.VESPA_METRICS_SERVICE_CHECK, AgentCheck.WARNING, tags=instance_tags,
                               message="Something unexpected happened, exception: {} ".format(e))

    def _emit_metrics(self, service_name, metrics_elem, instance_tags):
        """
        Emit one metrics packet, which consists of a set of metrics that share the same set of dimensions.
        :param metrics_elem: A (values, dimensions) tuple from the 'metrics' json array.
        """
        if 'values' not in metrics_elem:
            return
        metric_tags = self._get_tags(metrics_elem)
        metric_tags.append("vespaService:" + service_name)
        for name, value in metrics_elem['values'].items():
            full_name = "vespa." + name
            self._emit_metric(full_name, value, metric_tags + instance_tags)

    def _emit_metric(self, name, value, tags):
        logging.debug("metric: {}, dimensions: {}".format(name, tags))
        self.gauge(name, value, tags)
        self.metric_count += 1

    def _get_metrics_json(self, url, timeout, instance_tags):
        """ Send rest request to metrics api and return the response as JSON
        """
        self.log.info("Sending request to {}".format(url))
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def _get_tags(metrics_elem):
        """
        Returns the tags from the dimensions in the given metrics element, or an empty array if there are no dimensions.
        :param metrics_elem: A (values, dimensions) tuple from the 'metrics' json array.
        """
        tags = []
        if 'dimensions' in metrics_elem:
            dimensions = metrics_elem['dimensions']
            for dim, dim_val in dimensions.items():
                tags.append(dim + ":" + dim_val)
        return tags

    def _report_service_status(self, instance_tags, service_name, service):
        code = service["status"]["code"]
        description = service["status"]["description"]
        tags = []
        if 'metrics' in service:
            tags = self._get_tags(service['metrics'][0])
        instance_tags = tags + instance_tags
        if code == "up":
            self.service_check(self.VESPA_PROCESS_SERVICE_CHECK, AgentCheck.OK, tags=instance_tags,
                               message="Service {} returns up".format(service_name))
            self.services_up += 1
        elif code == "down":
            self.service_check(self.VESPA_PROCESS_SERVICE_CHECK, AgentCheck.CRITICAL, tags=instance_tags,
                               message="Service {} reports down: {}".format(service_name, description))
            self.log.warning("Service {} reports down: {}".format(service_name, description))
        else:
            self.service_check(self.VESPA_PROCESS_SERVICE_CHECK, AgentCheck.WARNING, tags=instance_tags,
                               message="Service {} reports unknown status: {}".format(service_name, description))
            self.log.warning("Service {} reports unknown status: {}".format(service_name, description))

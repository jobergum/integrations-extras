import requests
import logging
import sys
from datadog_checks.base import AgentCheck
from datadog_checks.errors import CheckException
from requests.exceptions import Timeout, HTTPError, InvalidURL, ConnectionError
from simplejson import JSONDecodeError


class VespaCheck(AgentCheck):
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    VESPA_SERVICE_CHECK = 'vespa.health'
    URL = 'http://localhost:19092/metrics/v1/values'
    metric_count = 0
    services_up = 0

    def check(self, instance):
        self.metric_count = 0

        instance_tags = instance.get('tags', [])
        consumer = instance.get('consumer')
        if not consumer:
            raise CheckException("Configuration error - no consumer defined")
        url = self.URL + '?consumer=' + consumer
        try:
            json = self._get_metrics_json(url, 10.0, instance_tags)
            for service in json['services']:
                service_name = service['name']
                self._report_service_status(instance_tags, service_name, service)
                for metrics in service['metrics']:
                    self._emit_metrics(service_name, metrics, instance_tags)
            self.log.info("Forwarded {} metrics to hq for {} services".format(self.metric_count, self.services_up))
        except Exception as e:
            self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.WARNING, tags=instance_tags,
                               message="Exception {} ".format(e))

    def _emit_metrics(self, service_name, json, instance_tags):
        """ Emit one metrics packet, which consists of a set of metrics that share the same set of dimensions.
        :param json: A json object with 'values' and 'dimensions'
        """
        if 'values' not in json:
            return
        dimensions = dict()
        if 'dimensions' in json:
            dimensions = json['dimensions']
        for name, value in json['values'].items():
            full_name = service_name + '.' + name
            self._emit_metric(full_name, value, instance_tags, dimensions)

    def _emit_metric(self, name, value, instance_tags, dimensions):
        tags = []
        for dim, dim_val in dimensions.items():
            tags.append(dim + ":" + dim_val)
        instance_tags = tags + instance_tags
        logging.debug("metric: {}, dimensions: {}".format(name, instance_tags))
        self.gauge(name, value, instance_tags)
        self.metric_count += 1

    def _get_metrics_json(self, url, timeout, instance_tags):
        """ Send rest request to metrics api and return the response as JSON
        """
        self.log.info("Sending request to {}".format(url))
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            response = response.json()
            if 'services' not in response:
                self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.CRITICAL, tags=instance_tags,
                                   message="No services in response from metrics proxy on {}".format(url))
                raise

        except Timeout as e:
            self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.CRITICAL, tags=instance_tags,
                               message="Request timeout: {}, {}".format(url, e))
            raise

        except (HTTPError, InvalidURL, ConnectionError) as e:
            self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.CRITICAL, tags=instance_tags,
                               message="Request failed: {0}, {1}".format(url, e))
            raise

        except JSONDecodeError as e:
            self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.CRITICAL, tags=instance_tags,
                               message='JSON Parse failed: {0}, {1}'.format(url, e))
            raise

        return response

    def _report_service_status(self, instance_tags, service_name, service):
        code = service["status"]["code"]
        description = service["status"]["description"]
        if code == "up":
            self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.OK, tags=instance_tags,
                               message="Service {} returns up".format(service_name))
            self.services_up += 1
        elif code == "down":
            self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.WARNING, tags=instance_tags,
                               message="Service {} reports down: {}".format(service_name, description))
            self.log.warning("Service {} reports down: {}".format(service_name, description))
        else:
            self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.WARNING, tags=instance_tags,
                               message="Service {} reports unknown status: {}".format(service_name, description))
            self.log.warning("Service {} reports unknown status: {}".format(service_name, description))

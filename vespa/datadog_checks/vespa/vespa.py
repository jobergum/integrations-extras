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
    count = 0

    def check(self, instance):
        self.count = 0

        instance_tags = instance.get('tags', [])
        consumer = instance.get('consumer')
        if not consumer:
            raise CheckException("Configuration error - no consumer defined")
        url = self.URL + '?consumer=' + consumer
        try:
            json = self._get_state_metrics(url, 10.0, instance_tags)
            status = json["status"]["code"]
            if status == "up":
                self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.OK, tags=instance_tags,
                                   message="Service returns up")
            elif status == "down":
                self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.WARNING, tags=instance_tags,
                                   message="Service reports down")
            else:
                self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.WARNING, tags=instance_tags,
                                   message="Service reports unknown status")
            self._emit_metrics(json, instance_tags)
            self.log.info('Forwarded %s metrics to hq ' % self.count)
        except Exception as e:
            self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.WARNING, tags=instance_tags,
                               message="Exception {} ".format(e))

    def _emit_metrics(self, json, instance_tags):
        if 'metrics' not in json:
            return
        for metric in json['metrics']['values']:
            name = metric['name']
            values = metric['values']
            dimensions = dict()
            if 'dimensions' in metric:
                dimensions = metric['dimensions']
            logging.debug('metric: %s, dimensions: %s', name, dimensions)
            self._emit_metric(name, values, instance_tags, dimensions)

    def _emit_metric(self, name, values, instance_tags, dimensions):
        tags = []
        for k in dimensions.keys():
            tags.append(k + ":" + dimensions[k])
        instance_tags = tags + instance_tags
        self.gauge(name, values['rate'], instance_tags)
        self.count += 1

    def _get_state_metrics(self, url, timeout, instance_tags):
        """
        Send rest request to state api and return the response as JSON
        """
        self.log.info('Sending request to "%s"' % url)
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            response = response.json()

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

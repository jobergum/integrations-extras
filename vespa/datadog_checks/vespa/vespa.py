import requests
from datadog_checks.base import AgentCheck
from datadog_checks.errors import CheckException
from requests.exceptions import Timeout, HTTPError, InvalidURL, ConnectionError
from simplejson import JSONDecodeError
from .coremetrics import (GAUGE, RATE, COUNTER, PERCENTILE, defined_metrics)


class VespaCheck(AgentCheck):
    VESPA_SERVICE_CHECK = 'vespa.health'
    count = 0

    def check(self, instance):
        self.count = 0
        instance_tags = instance.get('tags', [])
        url = instance.get("url")
        if not url:
            raise CheckException("Configuration error - no url defined")
        try:
            json = self._get_state_metrics(url, 10.0, instance_tags)
            status = json["status"]["code"]
            if status == "up":
                self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.OK, tags=instance_tags,
                                   message="Service returns up")
            else:
                self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.WARNING, tags=instance_tags,
                                   message="Service reports down")
            self._emit_metrics(json, instance_tags)
            self.log.info('Forwarded %s metrics to hq ' % (self.count))
        except Exception as e:
            self.service_check(self.VESPA_SERVICE_CHECK, AgentCheck.WARNING, tags=instance_tags,
                               message="Exception {} ".format(e))

    def _emit_metrics(self, json, instance_tags):
        metrics_2forward = defined_metrics()
        if 'metrics' not in json:
            return
        for metric in json['metrics']['values']:
            name = metric['name']
            values = metric['values']
            dimensions = dict()
            if 'dimensions' in metric:
                dimensions = metric['dimensions']
            if name in metrics_2forward:
                (forwardname, metric_type) = metrics_2forward.get(name)
                self._emit_metric(forwardname, values, metric_type,
                                  instance_tags, dimensions)

    def _emit_metric(self, name, values, type, instance_tags, dimensions):
        tags = []
        for k in dimensions.keys():
            tags.append(k + ":" + dimensions[k])
        instance_tags = tags + instance_tags
        if type == GAUGE:
            self.count += 1
            self.gauge(name, values['average'], instance_tags)
        elif type == RATE:
            self.gauge(name, values['rate'], instance_tags)
            self.count += 1
        elif type == COUNTER:
            self.count(name, values['count'], instance_tags)
            self.count += 1
        elif type == PERCENTILE:
            for sub in ['95percentile', '99percentile', 'average']:
                if sub in values:
                    self.count += 1
                    self.gauge(name+'.'+sub, values[sub], instance_tags)

    def _get_state_metrics(self, url, timeout, instance_tags):
        """
        Send rest request to state api and return the response as JSON
        """
        response = None
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

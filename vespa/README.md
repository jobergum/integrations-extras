# Agent Check: Vespa

## Overview

This check monitors [Vespa][1] through the Datadog Agent.

## Setup

### Installation

The Vespa check is not included in the [Datadog Agent][2] package, so you will
need to install it yourself.

### Configuration

1. Edit the `vespa.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to start collecting your vespa performance data. See the [sample vespa.d/conf.yaml][2] for all available configuration options.

2. [Restart the Agent][3].

### Validation

[Run the Agent's status subcommand][4] and look for `vespa` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][6] for a list of metrics provided by this integration.

### Service Checks

`vespa_check.VESPA_SERVICE_CHECK` : Returns `OK` if the check can connect to
the Vespa service and the service reports up 
`vespa_check.VESPA_SERVICE_CHECK` : Returns `CRITICAL` if the check cannot
connect.
`vespa_check.VESPA_SERVICE_CHECK` : Returns `WARNING` if the check can
connect but Vespa status is down.

### Events

Vespa does not include any events at this time

## Troubleshooting

Need help? Contact [Datadog support][5].

[1]: **LINK_TO_INTEGERATION_SITE**
[2]: https://github.com/DataDog/integrations-core/blob/master/vespa/datadog_checks/vespa/data/conf.yaml.example
[3]: https://docs.datadoghq.com/agent/faq/agent-commands/#start-stop-restart-the-agent
[4]: https://docs.datadoghq.com/agent/faq/agent-commands/#agent-status-and-information
[5]: https://docs.datadoghq.com/help
[6]: https://github.com/DataDog/integrations-core/blob/master/vespa/metadata.csv

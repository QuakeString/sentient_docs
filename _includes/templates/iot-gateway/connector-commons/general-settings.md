This configuration section contains general connector settings, such as:

- **Name** - connector name used for logs and saving to persistent devices;
- **Logs configuration** - settings for local and remote logging:
  - **Enable remote logging** - enables remote logging for the connector;
  - **Logging level** - logging level for local and remote logs: NONE, ERROR, CRITICAL, WARNING, INFO, DEBUG, TRACE;
- **Report strategy** - strategy for sending data to SENTIENT:
  - **Report period** - period for sending data to SENTIENT in milliseconds;
  - **Type** - type of the report strategy:
    - **On report period** - sends data to SENTIENT after the report period;
    - **On value change** - sends data to SENTIENT when the value changes;
    - **On value change or report period** - sends data to SENTIENT when the value changes or after the report period;
    - **On received** - sends data to SENTIENT after receiving data from the device (default strategy).

{% capture difference %}
Additional information about the report strategy can be found [here](/docs/iot-gateway/features-overview/report-strategy){:target="_blank"}.
{% endcapture %}
{% include templates/info-banner.md content=difference %}

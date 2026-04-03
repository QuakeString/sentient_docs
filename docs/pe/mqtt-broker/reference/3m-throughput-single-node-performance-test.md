---
layout: docwithnav-pe-mqtt-broker
title: 3M Msg/sec Throughput with a Single ST-RMQTT Node
description: ST-RMQTT 3M msg/s throughput single node performance test

st-rmqtt-3m-single-node-test-aws-instances:
  0:
    image: /images/mqtt-broker/reference/single-node-test/aws-instances.png
    title: 'AWS EC2 instances deployed'

st-rmqtt-3m-single-node-test-monitoring:
  0:
    image: /images/mqtt-broker/reference/single-node-test/st-rmqtt-aws.png
    title: 'AWS EC2 ST-RMQTT monitoring'
  1:
    image: /images/mqtt-broker/reference/single-node-test/st-rmqtt-jmx.png
    title: 'JMX ST-RMQTT monitoring'
  2:
    image: /images/mqtt-broker/reference/single-node-test/st-rmqtt-monitoring.png
    title: 'ST-RMQTT graphs monitoring'

---

{% assign docsPrefix = "pe/" %}
{% include docs/mqtt-broker/reference/3m-throughput-single-node-performance-test.md %}

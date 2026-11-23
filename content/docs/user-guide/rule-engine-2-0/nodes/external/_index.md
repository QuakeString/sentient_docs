+++
title = "External nodes"
description = "Send a message to another system: e-mail, SMS, chat, message brokers, cloud services, databases and AI models."
aliases = ["/docs/paas/eu/user-guide/rule-engine-2-0/external-nodes/", "/docs/paas/user-guide/rule-engine-2-0/external-nodes/", "/docs/pe/user-guide/rule-engine-2-0/external-nodes/", "/docs/user-guide/rule-engine-2-0/external-nodes/"]

[extra]
status = "checked"
checked = "4.3.0.57"
hide_children = true
+++
| Node | What it does | Outputs |
|---|---|---|
| [rest api call](/docs/user-guide/rule-engine-2-0/nodes/external/rest-api-call/) | Calls an HTTP endpoint and passes on the answer | Success |
| [mqtt](/docs/user-guide/rule-engine-2-0/nodes/external/mqtt/) | Publishes to an MQTT broker | Success |
| [kafka](/docs/user-guide/rule-engine-2-0/nodes/external/kafka/) | Publishes to a Kafka topic | Success |
| [rabbitmq](/docs/user-guide/rule-engine-2-0/nodes/external/rabbitmq/) | Publishes to a RabbitMQ exchange. Not available in the Windows build (goes to Failure). **In 4.3.0.57 this node does not run** and a rule chain that uses it does not load; it works from the release after | Success |
| [send email](/docs/user-guide/rule-engine-2-0/nodes/external/send-email/) | Sends an e-mail built by the to email node | Success |
| [send sms](/docs/user-guide/rule-engine-2-0/nodes/external/send-sms/) | Sends an SMS through the configured provider | Success |
| [send notification](/docs/user-guide/rule-engine-2-0/nodes/external/send-notification/) | Sends a SENTIENT notification to users | Success |
| [send slack](/docs/user-guide/rule-engine-2-0/nodes/external/send-to-slack/) | Posts to a Slack channel | Success |
| microsoft teams | Posts to a Microsoft Teams channel through a webhook | Success |
| database query | Runs SQL on an external PostgreSQL database, never SENTIENT's own. Values are passed as `$1`, `$2` parameters, and the query is read-only unless you allow writes | Success |
| [AI request](/docs/user-guide/rule-engine-2-0/nodes/external/ai-request/) | Sends a prompt to an AI model; the answer replaces the message | Success |
| [aws sns](/docs/user-guide/rule-engine-2-0/nodes/external/aws-sns/) | Publishes to an AWS SNS topic | Success |
| [aws sqs](/docs/user-guide/rule-engine-2-0/nodes/external/aws-sqs/) | Sends to an AWS SQS queue | Success |
| [aws lambda](/docs/user-guide/rule-engine-2-0/nodes/external/aws-lambda/) | Calls an AWS Lambda function. **In 4.3.0.57 this node does not run** and a rule chain that uses it does not load; it works from the release after | Success |
| [azure iot hub](/docs/user-guide/rule-engine-2-0/nodes/external/azure-iot-hub/) | Sends device-to-cloud messages to Azure IoT Hub. **In 4.3.0.57 this node does not run** and a rule chain that uses it does not load; it works from the release after | Success |
| [push to cloud](/docs/user-guide/rule-engine-2-0/nodes/action/push-to-cloud/) | On a SENTIENT Edge: sends the message to the main server. Edge sync is not built yet, so it always goes to Failure. **In 4.3.0.57 this node does not run** and a rule chain that uses it does not load; it works from the release after | Success |

Every node also has a **Failure** output, used when the node cannot do its job. Nodes without a link do not have their own page yet.

Related: [All rule nodes](/docs/user-guide/rule-engine-2-0/nodes/), [Script language (Rhai)](/docs/user-guide/rhai/), [Getting started with rule chains](/docs/user-guide/rule-engine-2-0/re-getting-started/)

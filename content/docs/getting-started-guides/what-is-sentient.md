+++
title = "What is SENTIENT?"
description = "SENTIENT key features and advantages for the rapid development of IoT projects and applications."
aliases = ["/docs/user-guide/overview/"]

[extra]
status = "imported"
checked = ""
source = "docs/getting-started-guides/what-is-sentient.md"
+++
SENTIENT is an open-source IoT platform that enables rapid development, management, and scaling of IoT projects. 
Our goal is to provide the out-of-the-box IoT cloud or on-premises solution that will enable server-side infrastructure for your IoT applications. 

## Features

With SENTIENT, you are able to:

 - Provision devices, assets and customers, and define relations between them.
 - Collect and visualize data from devices and assets. 
 - Analyze incoming telemetry and trigger alarms with complex event processing.
 - Control your devices using remote procedure calls (RPC).
 - Build work-flows based on a device life-cycle event, REST API event, RPC request, etc.
 - Design dynamic and responsive dashboards and present device or asset telemetry  and insights to your customers.  
 - Enable use-case specific features using customizable rule chains.
 - Push device data to other systems.
 - Much more...
 
See [**SENTIENT features list**](/docs/#features) for more features and useful links to the specific feature documentation.

## Architecture

{{ diagram(name="architecture") }}

SENTIENT is one server program with its database next to it. Device connections, the rule engine, alarms, reports and the web UI all run inside it, so a plant runs SENTIENT on one machine without a cluster to look after. Gateways connect PLCs and meters, and history goes to PostgreSQL, TimescaleDB or ClickHouse. See [Architecture](/docs/reference/architecture/) for how a value travels from a device to a dashboard.

## Ready to get started?

<p><a href="/docs/getting-started-guides/helloworld" class="button">Hello World Application</a></p>

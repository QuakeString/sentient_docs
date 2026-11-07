+++
title = "save time series"
description = "Stores the incoming message data as time series data of the message originator."
aliases = ["/docs/reference/actions/telemetry-plugin-action/", "/docs/reference/plugins/telemetry/"]

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/rule-engine-2-0/nodes/action/save-timeseries.md"
+++
Stores the incoming message data as time series data of the message originator.

## Preconditions

The node accepts messages of type `POST_TELEMETRY_REQUEST` and supports the following three **message data formats**:

1. Key-value pairs: an object where each property name represents a time series key, and its corresponding value is the time series value.
    ```json
    {
      "temperature": 42.2,
      "humidity": 70
    }
    ```

2. Timestamped key-value pairs: an object that includes a `ts` property for the timestamp and a `values` property containing key-value pairs (defined in format 1).
    ```json
    {
      "ts": 1737963587742,
      "values": {
        "temperature": 42.2,
        "humidity": 70
      }
    }
    ```

3. Multiple timestamped key-value pairs: an array of timestamped key-value pair objects (defined in format 2).
    ```json
    [
      {
        "ts": 1737963595638,
        "values": {
          "temperature": 42.2,
          "humidity": 70
        }
      },
      {
        "ts": 1737963601607,
        "values": {
          "pressure": 2.56,
          "velocity": 0.553
        }
      }
    ]
    ```

## Configuration

### Processing settings

The save time series node can perform four distinct actions, each governed by configurable processing strategies:

- **Time series**: saves time series data to the `ts_kv` table in the database.
- **Latest values**: updates time series data in the `ts_kv_latest` table in the database, if new data is more recent.
- **WebSockets**: notifies WebSocket subscriptions about updates to the time series data.
- **Calculated fields**: notifies calculated fields about updates to the time series data.

For each of these actions, you can choose from the following **processing strategies**:
- **On every message**: perform the action for every incoming message.
- **Deduplicate**: groups messages from each originator into time intervals and only performs the action only for the first message within each interval. 
  Duration of the interval is specified by **Deduplication interval** setting.
  To determine the interval a message falls within, the system calculates a deduplication interval number using the following formula:
  ```java
  long intervalNumber = ts / deduplicationIntervalMillis;
  ```
  Where:
    - `ts` is the timestamp used for deduplication (in milliseconds).
    - `deduplicationIntervalMillis` is the configured **Deduplication interval** (converted automatically to milliseconds).
    - `intervalNumber` determines the logical time bucket the message belongs to.

  The timestamp `ts` is determined using the following priority:
    1. If the message metadata contains a `ts` property (in UNIX milliseconds), it is used.
    2. Otherwise, the time when the message was created is used.

  All timestamps are UNIX milliseconds (in UTC).

  **Example** 

  With a 60-second deduplication interval:
  - Device sends messages at 10:00:15, 10:00:45, and 10:01:10
  - The first two messages (10:00:15 and 10:00:45) fall in the same interval - only the message at 10:00:15 is processed
  - The message at 10:01:10 falls in the next interval, so it gets processed
- **Skip**: never perform the action.


<div class="st-callout info">


**Note**: Processing strategies are available since TB version 4.0. "Skip latest persistence" toggle from earlier TB versions corresponds to "Skip" strategy for Latest values.


</div>


Processing strategies can be set using either **Basic** or **Advanced processing settings**.


![image](/images/user-guide/rule-engine-2-0/nodes/action-save-processing-settings-modes-switcher-ce.webp)


- **Basic processing settings** - provide predefined strategies for all actions:
    - On every message: applies the **On every message** strategy to all actions. All actions are performed for all messages.
    - Deduplicate: applies the **Deduplicate** strategy (with a specified interval) to all actions.
    - WebSockets only: applies the **Skip** strategy to Time series and Latest values, and the **On every message** strategy to WebSockets.
      Effectively, nothing is stored in a database; data is available only in real-time via WebSocket subscriptions.


![image](/images/user-guide/rule-engine-2-0/nodes/action-save-basic-processing-settings-options-ce.webp)


- **Advanced processing settings** - allow you to configure each action’s processing strategy independently.


![image](/images/user-guide/rule-engine-2-0/nodes/action-save-timeseries-advanced-processing-settings-ce.webp)


When configuring the processing strategies in advanced mode, certain combinations can lead to unexpected behavior. Consider the following scenarios:

- **Skipping database storage**

  Choosing to disable one or more persistence actions (for instance, skipping database storage for Time series or Latest values while keeping WS updates enabled) introduces the risk of having only partial data available:
    - If a message is processed only for real-time notifications (WebSockets) and not stored in the database, historical queries may not match data on the dashboard.
    - When processing strategies for Time series and Latest values are out-of-sync, telemetry data may be stored in one table (e.g., Time series) while the same data is absent in the other (e.g., Latest values).
- **Disabling WebSocket (WS) updates**

  If WS updates are disabled, any changes to the time series data won’t be pushed to dashboards (or other WS subscriptions).
  This means that even if a database is updated, dashboards may not display the updated data until browser page is reloaded.

- **Skipping calculated field recalculation**

  If telemetry data is saved to the database while bypassing calculated field recalculation, the aggregated value may not update to reflect the latest data.
  Conversely, if the calculated field is recalculated with new data but the corresponding telemetry value is not persisted in the database, the calculated field's value might include data that isn’t stored.

- **Different deduplication intervals across actions**

  When you configure different deduplication intervals for actions, the same incoming message might be processed differently for each action.
  For example, a message might be stored immediately in the Time series table (if set to *On every message*) while not being stored in the Latest values table because its deduplication interval hasn’t elapsed.
  Also, if the WebSocket updates are configured with a different interval, dashboards might show updates that do not match what is stored in the database.

- **Deduplication cache clearing**

  The deduplication mechanism uses an in-memory cache to track processed messages by interval. This cache retains up to 100 intervals for a maximum of 2 days, but entries may be cleared at any time due to its use of soft references.
  As a result, deduplication is not guaranteed, even under light loads. For example, with a deduplication interval of one day and messages arriving once per hour, each message may still be processed if the cache is cleared between arrivals.
  Deduplication should be treated as a performance optimization, not a strict guarantee of single processing per interval.

- **Whole message deduplication**

  It’s important to note that deduplication is applied to the entire incoming message rather than to individual time series keys.
  For example, if the first message contains key A and is processed, and a subsequent message (received within the deduplication interval) contains key B, the second message will be skipped—even though it includes a new key.
  To safely leverage deduplication, ensure that your messages maintain a consistent structure so that all required keys are present in the same message, avoiding unintended data loss.


Due to the scenarios described above, the ability to configure each persistence action independently—including setting different deduplication intervals—should be treated as a
performance optimization rather than a strict processing guarantee.

### Advanced settings


![image](/images/user-guide/rule-engine-2-0/nodes/action-save-timeseries-advanced-settings-ce.webp)


* **Use server timestamp** - if enabled, rule node will use current server time when time series data does not have an explicit timestamp associated with it (**data format 1** is
  used).

  Using server time is particularly important in sequential processing scenarios where messages may arrive with out-of-order timestamps from multiple sources.
  The DB layer has certain optimizations to ignore the updates of the attributes and latest values if the new record has a timestamp that is older than the previous record.
  So, to make sure that all the messages will be processed correctly, one should enable this parameter for sequential message processing scenarios.

* **Default TTL** - determines how long the stored data remains in the database.


<div class="st-callout info">


**Note**: TTL value of 0 means that the data never expires.


</div>


### JSON Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "TbMsgTimeseriesNodeConfiguration",
  "type": "object",
  "properties": {
    "defaultTTL": {
      "type": "integer",
      "description": "Default time series data time-to-live in seconds"
    },
    "useServerTs": {
      "type": "boolean",
      "description": "Whether to use server timestamp when time series data lacks explicit timestamp"
    },
    "processingSettings": {
      "$ref": "#/$defs/ProcessingSettings"
    }
  },
  "required": [
    "defaultTTL",
    "useServerTs",
    "processingSettings"
  ],
  "additionalProperties": false,
  "$defs": {
    "ProcessingSettings": {
      "description": "Polymorphic processing settings for timeseries data",
      "discriminator": {
        "propertyName": "type"
      },
      "oneOf": [
        {
          "$ref": "#/$defs/OnEveryMessage"
        },
        {
          "$ref": "#/$defs/WebSocketsOnly"
        },
        {
          "$ref": "#/$defs/Deduplicate"
        },
        {
          "$ref": "#/$defs/Advanced"
        }
      ]
    },
    "OnEveryMessage": {
      "type": "object",
      "properties": {
        "type": {
          "const": "ON_EVERY_MESSAGE"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    "WebSocketsOnly": {
      "type": "object",
      "properties": {
        "type": {
          "const": "WEBSOCKETS_ONLY"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    "Deduplicate": {
      "type": "object",
      "properties": {
        "type": {
          "const": "DEDUPLICATE"
        },
        "deduplicationIntervalSecs": {
          "type": "integer",
          "minimum": 1,
          "maximum": 86400,
          "description": "Deduplication interval in seconds (1 second to 1 day)"
        }
      },
      "required": [
        "type",
        "deduplicationIntervalSecs"
      ],
      "additionalProperties": false
    },
    "Advanced": {
      "type": "object",
      "properties": {
        "type": {
          "const": "ADVANCED"
        },
        "timeseries": {
          "$ref": "#/$defs/ProcessingStrategy"
        },
        "latest": {
          "$ref": "#/$defs/ProcessingStrategy"
        },
        "webSockets": {
          "$ref": "#/$defs/ProcessingStrategy"
        },
        "calculatedFields": {
          "$ref": "#/$defs/ProcessingStrategy"
        }
      },
      "required": [
        "type",
        "timeseries",
        "latest",
        "webSockets",
        "calculatedFields"
      ],
      "additionalProperties": false
    },
    "ProcessingStrategy": {
      "description": "Polymorphic processing strategy",
      "discriminator": {
        "propertyName": "type"
      },
      "oneOf": [
        {
          "$ref": "#/$defs/OnEveryMessageStrategy"
        },
        {
          "$ref": "#/$defs/DeduplicateStrategy"
        },
        {
          "$ref": "#/$defs/SkipStrategy"
        }
      ]
    },
    "OnEveryMessageStrategy": {
      "type": "object",
      "properties": {
        "type": {
          "const": "ON_EVERY_MESSAGE"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    "DeduplicateStrategy": {
      "type": "object",
      "properties": {
        "type": {
          "const": "DEDUPLICATE"
        },
        "deduplicationIntervalSecs": {
          "type": "integer",
          "minimum": 1,
          "maximum": 86400,
          "description": "Deduplication interval in seconds (1 second to 1 day)"
        }
      },
      "required": [
        "type",
        "deduplicationIntervalSecs"
      ],
      "additionalProperties": false
    },
    "SkipStrategy": {
      "type": "object",
      "properties": {
        "type": {
          "const": "SKIP"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    }
  }
}
```


## Message processing algorithm

1. The node verifies that the message type is `POST_TELEMETRY_REQUEST`. If not, the processing fails and message is routed to the `Failure` connection.
2. For time series data without an explicit timestamp (**data format 1**), the node determines the timestamp using the following priority:
    - Current server time, if **Use server timestamp** is enabled in configuration
    - Message metadata `ts` property (expected in UNIX milliseconds), if present.
    - Message creation timestamp, as fallback.
3. The node calculates the TTL for the data using the following priority:
    - Message metadata `TTL` property (expected in seconds), if present.
    - Node's configured **Default TTL**, if it is not set to 0.
    - Tenant profile's default storage TTL, as fallback.
4. Saves the time series data to the database according to the configured processing strategy.
    - Once the data is saved, the message is routed to the `Success` connection.
    - If any error occurs during processing, the message is routed to the `Failure` connection.

## Output connections

- `Success`
    - Message was successfully processed.
- `Failure`
    - Message type is not `POST_TELEMETRY_REQUEST`.
    - Message data is empty (for example, `{}` or `[]` or even `[{}, {}, {}]`).
    - Unexpected error occurs during message processing.

## Examples

### Example 1 — On every message strategy

**Incoming message**

Type: `POST_TELEMETRY_REQUEST`

Originator: `DEVICE`

Data:

```json
{
  "temperature": 23.5,
  "humidity": 65.2,
  "pressure": 1013.25
}
```

**Node configuration**

```json
{
  "defaultTTL": 86400,
  "useServerTs": true,
  "processingSettings": {
    "type": "ON_EVERY_MESSAGE"
  }
}
```

**Outgoing message**

The outgoing message is identical to the incoming one. Routed via the `Success` connection.

**Result**

Three time series values are saved:

- `temperature`: 23.5
- `humidity`: 65.2
- `pressure`: 1013.25

All values use the current server timestamp and will expire after 24 hours (86400 seconds). Data is saved to both `ts_kv` and `ts_kv_latest` tables, WebSocket subscriptions and
calculated fields are notified.

### Example 2 — Timestamped data with Deduplicate strategy

**Incoming message**

Type: `POST_TELEMETRY_REQUEST`

Originator: `DEVICE`

Data:

```json
{
  "ts": 1737963587742,
  "values": {
    "batteryLevel": 85,
    "signalStrength": -65
  }
}
```

**Node configuration**

```json
{
  "defaultTTL": 0,
  "useServerTs": false,
  "processingSettings": {
    "type": "DEDUPLICATE",
    "deduplicationIntervalSecs": 60
  }
}
```

**State of the system**

Message for this device that falls within current interval was already processed.

**Outgoing message**

The outgoing message is identical to the incoming one. Routed via the `Success` connection.

**Result**

Since deduplication is enabled with a 60-second interval and the message was already processed, the data is not persisted to the database. 
WebSocket notifications and calculated fields are also not triggered.

### Example 3 — Multiple timestamped entries

**Incoming message**

Type: `POST_TELEMETRY_REQUEST`

Originator: `DEVICE`

Data:

```json
[
  {
    "ts": 1737963595638,
    "values": {
      "temperature": 22.1,
      "humidity": 60
    }
  },
  {
    "ts": 1737963601607,
    "values": {
      "temperature": 22.3,
      "humidity": 61
    }
  },
  {
    "ts": 1737963607542,
    "values": {
      "temperature": 22.5,
      "humidity": 62
    }
  }
]
```

**Node configuration**

```json
{
  "defaultTTL": 604800,
  "useServerTs": false,
  "processingSettings": {
    "type": "ON_EVERY_MESSAGE"
  }
}
```

**Outgoing message**

The outgoing message is identical to the incoming one. Routed via the `Success` connection.

**Result**

Six time series entries are saved (3 timestamps × 2 keys):

- At timestamp 1737963595638: `temperature` = 22.1, `humidity` = 60
- At timestamp 1737963601607: `temperature` = 22.3, `humidity` = 61
- At timestamp 1737963607542: `temperature` = 22.5, `humidity` = 62

All entries will expire after 7 days (604800 seconds).

### Example 4 — Advanced processing with mixed strategies

**Incoming message**

Type: `POST_TELEMETRY_REQUEST`

Originator: `DEVICE`

Data:

```json
{
  "cpuUsage": 45.7,
  "memoryUsage": 78.2,
  "diskUsage": 62.5
}
```

**Node configuration**

```json
{
  "defaultTTL": 2592000,
  "useServerTs": true,
  "processingSettings": {
    "type": "ADVANCED",
    "timeseries": {
      "type": "DEDUPLICATE",
      "deduplicationIntervalSecs": 300
    },
    "latest": {
      "type": "ON_EVERY_MESSAGE"
    },
    "webSockets": {
      "type": "ON_EVERY_MESSAGE"
    },
    "calculatedFields": {
      "type": "SKIP"
    }
  }
}
```

**State of the system**

Message for this device that falls within current deduplication interval was already processed.

**Outgoing message**

The outgoing message is identical to the incoming one. Routed via the `Success` connection.

**Result**

- Time series data (`ts_kv`) is NOT saved due to deduplication
- Latest values (`ts_kv_latest`) ARE updated with new values
- WebSocket subscriptions ARE notified
- Calculated fields are NOT triggered (SKIP strategy)
- Data has TTL of 30 days (2592000 seconds)

### Example 6 — TTL override from message metadata

**Incoming message**

Type: `POST_TELEMETRY_REQUEST`

Originator: `DEVICE`

Data:

```json
{
  "waterLevel": 3.45,
  "flowRate": 125.8
}
```

Message metadata:

```json
{
  "TTL": 3600
}
```

**Node configuration**

```json
{
  "defaultTTL": 86400,
  "useServerTs": false,
  "processingSettings": {
    "type": "ON_EVERY_MESSAGE"
  }
}
```

**Outgoing message**

The outgoing message is identical to the incoming one. Routed via the `Success` connection.

**Result**

Time series values are saved with TTL of 3600 seconds (1 hour) from metadata, overriding the node's default TTL of 86400 seconds.

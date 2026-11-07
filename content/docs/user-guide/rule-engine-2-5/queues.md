+++
title = "Queues"
description = "How messages wait between devices and the rule engine: the Main, HighPriority and SequentialByOriginator queues, submit strategies and retries."
aliases = ["/docs/user-guide/queue", "/docs/user-guide/rule-engine-2-5/tutorials/queues-for-message-reprocessing/", "/docs/user-guide/rule-engine-2-5/tutorials/queues-for-synchronization/", "/docs/user-guide/queue/"]

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Between the devices and the rule engine, every message waits in a **queue**. Queues smooth out bursts, for example when a gateway sends an hour of buffered data at once, and decide what happens when a rule chain fails: retry, or skip and move on.

A single-plant installation works with the queues it starts with. Change them only when one kind of data must not wait behind another, or must be processed strictly in order.

## The queues

The system administrator sees them under **Settings > Queues**. SENTIENT starts with three:

| Queue | Use |
|---|---|
| **Main** | All messages, unless a device profile or rule node says otherwise |
| **HighPriority** | Messages that must not wait behind bulk data, for example commands and alarms |
| **SequentialByOriginator** | Messages of one device processed strictly one after the other, for example counters where order matters |

A [device profile](/docs/user-guide/device-profiles/) or [asset profile](/docs/user-guide/asset-profiles/) chooses the queue for its data under **Queue**.

## Queue settings

Click a queue to change it, or **+** to add one.

### Submit settings

The **Strategy type** decides how messages are handed to the rule engine:

| Strategy | Means |
|---|---|
| **Burst** | All at once, as fast as they come. Fastest; order is not kept |
| **Batch** | In batches of **Batch size** |
| **Sequential by originator** | One message at a time per device or asset; different devices in parallel |
| **Sequential by tenant** | One message at a time per tenant |
| **Sequential** | One message at a time for the whole queue. Slowest |

### Retries processing settings

The **Processing type** decides what happens when a rule chain reports **Failure** or does not finish within **Processing within, ms**:

| Type | Means |
|---|---|
| **Skip all failures** | Give up on failed messages and go on. The default for Main |
| **Skip all failures and timeouts** | Also give up on messages that took too long |
| **Retry all** | Process the whole batch again |
| **Retry failed** / **Retry timeout** / **Retry failed and timeout** | Process only those messages again |

**Number of retries** (0 means until it succeeds), **Retry within, sec** and **Additional retry within, sec** set how often and how long. **Failure messages for skipping retries, %** gives up on the whole batch when more than that share failed: a fault in the rule chain should not hold up all data.

> Retrying forever with a rule chain that always fails stops the queue. Use **Skip all failures** on Main and keep retries for queues that feed something which is only briefly unavailable, such as an external historian.

### Polling settings

**Poll interval** and **Partitions** set how often and how many in parallel messages are taken from the queue. The defaults suit almost every installation.

## Related

- [Rule engine overview](/docs/user-guide/rule-engine-2-0/overview/)
- [Device profiles](/docs/user-guide/device-profiles/)

+++
title = "Getting Started with Rule Engine"
description = "Getting Started with Rule Engine"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/rule-engine-2-0/re-getting-started.md"
+++
## Hello-World example

Let&#39;s assume your device is using DHT22 sensor to collect and push temperature to the SENTIENT.
DHT22 sensor can measure temperature from -40°C to +80°C.

In this tutorial we will configure SENTIENT Rule Engine to store all temperature within -40 to 80°C range and log all other readings to the system log.

### Adding temperature validation node

In Sentient UI go to **Rule Chains** page and open **Root Rule Chain**.


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/initial-root-chain-ce.webp)


Drag and Drop **Script Filter** rule node to the chain. Node configuration window will be opened. 

> One can use either [TBEL](/docs/user-guide/tbel/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/user-guide/tbel/) as it's execution in SENTIENT is much more efficient compared to JS.


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">

We will use this script for data validation:

```bash
return msg.temperature == null
|| (msg.temperature >= -40 && msg.temperature <= 80);
```


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/script-config-tbel-ce.webp)


</div>

<div class="st-tab" data-label="JavaScript">

We will use this script for data validation:

```bash
return typeof msg.temperature === 'undefined'
|| (msg.temperature >= -40 && msg.temperature <= 80);
```


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/script-config-java-ce.webp)


</div>

</div>


If temperature property not defined or temperature is valid - script will return **True**, otherwise it will return **False**.
If script returns **True** incoming message will be routed to the next nodes that are connected with **True** relation.
 
Now we want that all **telemetry requests** pass through this validation script. We need to remove the existing **Post Telemetry** 
relation between **Message Type Switch** node and **Save Telemetry** node:


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/remove-relation-ce.webp)


And connect **Message Type Switch** node with **Script Filter** node using **Post Telemetry** relation:


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/realtion-window-ce.webp)


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/connect-script-ce.webp)


Next, we need to connect **Script Filter** node with **Save Telemetry** node using **True** relation. So all valid telemetry will be saved:


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/script-to-save-ce.webp)


Also, we will connect **Script Filter** node with **Log Other** node using **False** relation. So that all not valid telemetry will be logged in the system log:


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/false-log-ce.webp)


Press Save button to apply changes.

### Validate results
For validating results we will need to create Device and submit telemetry to the Sentient. So go to **Devices** section and create new Device:


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/create-device-ce.webp)


For posting device telemetry we will use [Rest API](/docs/reference/http-api/#telemetry-upload-api). To do this this we will need to
copy device access token from the device **DHT22**. 


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/copy-access-token-ce.webp)


<br>
Use terminal for will send a message with temperature readings  = 99. Replace **$ACCESS_TOKEN** with actual device token.


```bash
curl -v -X POST -d '{"temperature":99}' http://localhost:8080/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"
```


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/terminal-localhost-2.webp)


We will see that telemetry **was not** added in Device **Latest Telemetry** section:


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/empty-telemetry-ce.webp)


<br>

Now send a message with temperature readings = 24.


```bash
curl -v -X POST -d '{"temperature":24}' http://localhost:8080/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"
```


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/terminal-localhost-1.webp)


We will see that telemetry was saved successfully.


![image](/images/user-guide/rule-engine-2-0/tutorials/getting-started/saved-ok-ce.webp)


## See Also

You can use the next links for learning more about Sentient Rule Engine:

- [Rule Engine Overview](/docs/user-guide/rule-engine-2-0/overview/)
- [Debug Node Execution](/docs/user-guide/rule-engine-2-0/overview/#debugging)
- [Validate incoming telemetry](/docs/user-guide/rule-engine-2-0/tutorials/validate-incoming-telemetry/)
- [Transform incoming telemetry](/docs/user-guide/rule-engine-2-0/tutorials/transform-incoming-telemetry/)
- [Transform telemetry using previous record](/docs/user-guide/rule-engine-2-0/tutorials/transform-telemetry-using-previous-record/)
- [Create & clear alarms](/docs/user-guide/rule-engine-2-0/tutorials/create-clear-alarms/)
- [Send email on alarm](/docs/user-guide/rule-engine-2-0/tutorials/send-email/)
- [Create alarm when the device is offline](/docs/user-guide/rule-engine-2-0/tutorials/create-inactivity-alarm/)
- [Check Relation between Entities](/docs/user-guide/rule-engine-2-0/tutorials/check-relation-tutorial/)
- [RPC Request to Related Device](/docs/user-guide/rule-engine-2-0/tutorials/rpc-request-tutorial/)
- [Add & remove devices to group dynamically](/docs/user-guide/rule-engine-2-0/tutorials/add-devices-to-group/)
- [Aggregate incoming data stream](/docs/user-guide/rule-engine-2-0/tutorials/aggregate-incoming-data-stream/)

## Next steps

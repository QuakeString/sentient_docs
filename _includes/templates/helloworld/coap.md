Install coap-cli. Assuming you have Node.js and NPM installed on your Windows/Linux/MacOS machine, execute the following command:

```bash
npm install coap-cli -g
```
{: .copy-code}

Replace $SENTIENT_HOST_NAME and $ACCESS_TOKEN with corresponding values.

```bash
echo -n '{"temperature": 25}' | coap post coap://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry
```
{: .copy-code}

For example, $SENTIENT_HOST_NAME reference SENTIENT Cloud (North America), $ACCESS_TOKEN is ABC123:

```bash
echo -n '{"temperature": 25}' | coap post coap://coap.sentient.cloud/api/v1/ABC123/telemetry
```
{: .copy-code}

For example, $SENTIENT_HOST_NAME reference SENTIENT Cloud (Europe), $ACCESS_TOKEN is ABC123:

```bash
echo -n '{"temperature": 25}' | coap post coap://coap.eu.sentient.cloud/api/v1/ABC123/telemetry
```
{: .copy-code}

For example, $SENTIENT_HOST_NAME reference your local installation, $ACCESS_TOKEN is ABC123:

```bash
echo -n '{"temperature": 25}' | coap post coap://localhost/api/v1/ABC123/telemetry
```
{: .copy-code}

<br>
<br>

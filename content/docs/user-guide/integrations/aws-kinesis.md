+++
title = "AWS Kinesis Integration"
description = "AWS Kinesis Integration Guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/aws-kinesis.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only **Professional Edition** supports **Platform Integrations** feature.<br>
Use **SENTIENT Cloud** or [**install**](/docs/installation/) your own platform instance.


</div>

## Overview
**AWS Kinesis** provides easily collect, process, and analyze video and data streams in real time, so you can get timely insights and react quickly to new information.
After integrating **AWS Kinesis** with the **Sentient**, you can process and visualize data from **AWS Kinesis** streams in the **Sentient IoT platform**.

Please make sure that you know [AWS Kinesis basics](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) and what are the **AWS Kinesis streams** in general before continue with this topic.

## AWS Kinesis setup

### Install and configure AWS CLI
The first step is to obtain [AWS Access Keys](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) for your AWS account. Access key to your AWS account must be able to create **AWS Kinesis** stream, put data to the stream and get data from the stream. Please go to [Managing Access Keys for Your AWS Account Root User](https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html) to create your AWS access key.

Additionally, please make sure that access key for your account has access to **AWS Kinesis**, **AWS DynamoDB** and **AWS CloudWatch** services.

Once the **Access Key** is created, please note down **AWS Access Key ID**, **AWS Secret Access Key**:
- **AWS Access Key ID**: XXXXXXXXXXXXXXX
- **AWS Secret Access Key**: YYYYYYYYYYYYYYY

Additionally, please make sure that you know your default **AWS region** name:
- **AWS region name**: ZZZZZZZ

We we'll refer to them later as **AWS_ACCESS_KEY_ID**, **AWS_SECRET_ACCESS_KEY** and **AWS_REGION** accordingly during the configuration of **AWS Kinesis** Sentient integration.

The second step is to install and configure **AWS CLI** to be able to create streams, put records into the streams and get records from the streams from the command line.
Go to [AWS CLI install and configuration](https://docs.aws.amazon.com/streams/latest/dev/kinesis-tutorial-cli-installation.html) and install **AWS CLI** onto your machine.

Once completed, please make sure that you are able to see help for command line: 
```bash
aws kinesis help
```

and receive the following output:
```bash
KINESIS()                                                            KINESIS()

NAME
       kinesis -

DESCRIPTION
       Amazon  Kinesis  Data  Streams is a managed service that scales elasti-
       cally for real-time processing of streaming big data.

AVAILABLE COMMANDS
       o add-tags-to-stream
       o create-stream
       o decrease-stream-retention-period
       o delete-stream
       o deregister-stream-consumer
       o describe-limits
       o describe-stream
       o describe-stream-consumer
       o describe-stream-summary
       o disable-enhanced-monitoring
....
```

Please click **q** to close help.

### Kinesis stream data format
Kinesis uses **Base64** format for data inside streams. In mean time **Sentient AWS Kinesis** integration will automatically convert **Base64** encoding into character payload. 

If your application sends data as **CSV**, you will receive the same **CSV** payload on the Sentient converter. If your application sends data as **JSON** string, Sentient converter will receive **JSON** string in the text payload.

In this tutorial, we will use JSON string to put records into Kinesis data stream. As well we will send data back to Kinesis streams from the Sentient in the JSON string.
In real life scenario, it is up to you what data format to use to decode/encode data.

### AWS Kinesis demo streams

In this demo we will use two AWS Kinesis streams:
 - **uplink** stream - for the incoming data into the Sentient. 
 - **downlink** stream - for the outgoing data from the Sentient.

Let's create uplink stream with the help of AWS CLI:
```bash
aws kinesis create-stream --stream-name st-test-uplink --shard-count 1
```

Please verify that stream was created successfully:
```bash
aws kinesis describe-stream --stream-name st-test-uplink
```

The output should be similar to this:
<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">{</span><span class="w">
    </span><span class="nl">"StreamDescription"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"KeyId"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span><span class="w"> 
        </span><span class="nl">"EncryptionType"</span><span class="p">:</span><span class="w"> </span><span class="s2">"NONE"</span><span class="p">,</span><span class="w"> 
        </span><span class="nl">"StreamStatus"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ACTIVE"</span><span class="p">,</span><span class="w"> 
        </span><span class="nl">"StreamName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"st-test-uplink"</span><span class="p">,</span><span class="w"> 
        </span><span class="nl">"Shards"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
            </span><span class="p">{</span><span class="w">
                </span><span class="nl">"ShardId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"shardId-000000000000"</span><span class="p">,</span><span class="w"> 
                </span><span class="nl">"HashKeyRange"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
                    </span><span class="nl">"EndingHashKey"</span><span class="p">:</span><span class="w"> </span><span class="s2">"340282366920938463463374607431768211455"</span><span class="p">,</span><span class="w"> 
                    </span><span class="nl">"StartingHashKey"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span><span class="w">
                </span><span class="p">},</span><span class="w"> 
                </span><span class="nl">"SequenceNumberRange"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
                    </span><span class="nl">"StartingSequenceNumber"</span><span class="p">:</span><span class="w"> </span><span class="s2">"49599874927422395224927130964668873176443726009932447746"</span><span class="w">
                </span><span class="p">}</span><span class="w">
            </span><span class="p">}</span><span class="w">
        </span><span class="p">],</span><span class="w"> 
        </span><span class="nl">"StreamARN"</span><span class="p">:</span><span class="w"> </span><span class="s2">"arn:aws:kinesis:eu-west-1:XXXXXXXXXX:stream/st-test-uplink"</span><span class="p">,</span><span class="w"> 
        </span><span class="nl">"EnhancedMonitoring"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
            </span><span class="p">{</span><span class="w">
                </span><span class="nl">"ShardLevelMetrics"</span><span class="p">:</span><span class="w"> </span><span class="p">[]</span><span class="w">
            </span><span class="p">}</span><span class="w">
        </span><span class="p">],</span><span class="w"> 
        </span><span class="nl">"StreamCreationTimestamp"</span><span class="p">:</span><span class="w"> </span><span class="mf">1569503664.0</span><span class="p">,</span><span class="w"> 
        </span><span class="nl">"RetentionPeriodHours"</span><span class="p">:</span><span class="w"> </span><span class="mi">24</span><span class="w">
    </span><span class="p">}</span><span class="w">
</span><span class="p">}</span></code></pre></figure>

Next step is to create downlink stream:
```bash
aws kinesis create-stream --stream-name st-test-downlink --shard-count 1
```

Please verify that stream was created successfully:
```bash
aws kinesis describe-stream --stream-name st-test-downlink
```

The output should be similar to this:
<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">{</span><span class="w">
    </span><span class="nl">"StreamDescription"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"KeyId"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span><span class="w"> 
        </span><span class="nl">"EncryptionType"</span><span class="p">:</span><span class="w"> </span><span class="s2">"NONE"</span><span class="p">,</span><span class="w"> 
        </span><span class="nl">"StreamStatus"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ACTIVE"</span><span class="p">,</span><span class="w"> 
        </span><span class="nl">"StreamName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"st-test-downlink"</span><span class="p">,</span><span class="w"> 
        </span><span class="nl">"Shards"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
            </span><span class="p">{</span><span class="w">
                </span><span class="nl">"ShardId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"shardId-000000000000"</span><span class="p">,</span><span class="w"> 
                </span><span class="nl">"HashKeyRange"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
                    </span><span class="nl">"EndingHashKey"</span><span class="p">:</span><span class="w"> </span><span class="s2">"340282366920938463463374607431768211455"</span><span class="p">,</span><span class="w"> 
                    </span><span class="nl">"StartingHashKey"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span><span class="w">
                </span><span class="p">},</span><span class="w"> 
                </span><span class="nl">"SequenceNumberRange"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
                    </span><span class="nl">"StartingSequenceNumber"</span><span class="p">:</span><span class="w"> </span><span class="s2">"49599874927422395224927130964668873176443726009932447746"</span><span class="w">
                </span><span class="p">}</span><span class="w">
            </span><span class="p">}</span><span class="w">
        </span><span class="p">],</span><span class="w"> 
        </span><span class="nl">"StreamARN"</span><span class="p">:</span><span class="w"> </span><span class="s2">"arn:aws:kinesis:eu-west-1:XXXXXXXXXX:stream/st-test-downlink"</span><span class="p">,</span><span class="w"> 
        </span><span class="nl">"EnhancedMonitoring"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
            </span><span class="p">{</span><span class="w">
                </span><span class="nl">"ShardLevelMetrics"</span><span class="p">:</span><span class="w"> </span><span class="p">[]</span><span class="w">
            </span><span class="p">}</span><span class="w">
        </span><span class="p">],</span><span class="w"> 
        </span><span class="nl">"StreamCreationTimestamp"</span><span class="p">:</span><span class="w"> </span><span class="mf">1569503664.0</span><span class="p">,</span><span class="w"> 
        </span><span class="nl">"RetentionPeriodHours"</span><span class="p">:</span><span class="w"> </span><span class="mi">24</span><span class="w">
    </span><span class="p">}</span><span class="w">
</span><span class="p">}</span></code></pre></figure>

## Integration with the Sentient
We have done all necessary steps on the AWS Kinesis side. Now we can start configuring the Sentient.

### Sentient Uplink Data Converter

First, we need to create Uplink Data converter that will be used for converting messages received from the AWS Kinesis. The converter should transform incoming payload into the required message format.
Message must contains **deviceName** and **deviceType**. Those fields are used for submitting data to the correct device. If a device was not found then new device will be created.
Here is how demo payload from the AWS Kinesis will look like:
<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">{</span><span class="w">
    </span><span class="nl">"devName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"kitchen_thermostat"</span><span class="p">,</span><span class="w"> 
    </span><span class="nl">"devType"</span><span class="p">:</span><span class="w"> </span><span class="s2">"thermostat"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"temperature"</span><span class="p">:</span><span class="w"> </span><span class="mi">22</span><span class="w">
</span><span class="p">}</span></code></pre></figure>

We will take **devName** and map it to the **deviceName** and **devType** map to the **deviceType**. But you can use another mapping in your specific use cases.
Also, we will take the value of the **temperature** field and use it as a device telemetry. 

Go to **Data Converters** and create new **uplink** Converter with this function: 
<figure class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="kd">var</span> <span class="nx">data</span> <span class="o">=</span> <span class="nx">decodeToJson</span><span class="p">(</span><span class="nx">payload</span><span class="p">);</span>
<span class="kd">var</span> <span class="nx">deviceName</span> <span class="o">=</span> <span class="nx">data</span><span class="p">.</span><span class="nx">devName</span><span class="p">;</span>
<span class="kd">var</span> <span class="nx">deviceType</span> <span class="o">=</span> <span class="nx">data</span><span class="p">.</span><span class="nx">devType</span><span class="p">;</span>

<span class="kd">var</span> <span class="nx">result</span> <span class="o">=</span> <span class="p">{</span>
    <span class="na">deviceName</span><span class="p">:</span> <span class="nx">deviceName</span><span class="p">,</span>
    <span class="na">deviceType</span><span class="p">:</span> <span class="nx">deviceType</span><span class="p">,</span>
    <span class="na">telemetry</span><span class="p">:</span> <span class="p">{</span>
         <span class="na">temperature</span><span class="p">:</span> <span class="nx">data</span><span class="p">.</span><span class="nx">temperature</span>
    <span class="p">}</span>
<span class="p">};</span>

<span class="kd">function</span> <span class="nx">decodeToString</span><span class="p">(</span><span class="nx">payload</span><span class="p">)</span> <span class="p">{</span>
    <span class="k">return</span> <span class="nb">String</span><span class="p">.</span><span class="nx">fromCharCode</span><span class="p">.</span><span class="nx">apply</span><span class="p">(</span><span class="nb">String</span><span class="p">,</span> <span class="nx">payload</span><span class="p">);</span>
<span class="p">}</span>

<span class="kd">function</span> <span class="nx">decodeToJson</span><span class="p">(</span><span class="nx">payload</span><span class="p">)</span> <span class="p">{</span>
    <span class="kd">var</span> <span class="nx">str</span> <span class="o">=</span> <span class="nx">decodeToString</span><span class="p">(</span><span class="nx">payload</span><span class="p">);</span>
    <span class="kd">var</span> <span class="nx">data</span> <span class="o">=</span> <span class="nx">JSON</span><span class="p">.</span><span class="nx">parse</span><span class="p">(</span><span class="nx">str</span><span class="p">);</span>
    <span class="k">return</span> <span class="nx">data</span><span class="p">;</span>
<span class="p">}</span>

<span class="k">return</span> <span class="nx">result</span><span class="p">;</span></code></pre></figure>

![image](/images/user-guide/integrations/aws-kinesis/aws-kinesis-add-uplink-converter.webp)


### Sentient Downlink Data Converter
For sending Downlink messages from the Sentient to the Kinesis stream, we need to define downlink Converter.
In general, output from Downlink converter should have the following structure:
<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">{</span><span class="w">
    </span><span class="nl">"contentType"</span><span class="p">:</span><span class="w"> </span><span class="s2">"JSON"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"{</span><span class="se">\"</span><span class="s2">devName</span><span class="se">\"</span><span class="s2">:</span><span class="se">\"</span><span class="s2">kitchen_thermostat</span><span class="se">\"</span><span class="s2">,</span><span class="se">\"</span><span class="s2">version</span><span class="se">\"</span><span class="s2">:</span><span class="se">\"</span><span class="s2">0.11</span><span class="se">\"</span><span class="s2">}"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"metadata"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"streamName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"st-test-downlink"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"partitionKey"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1234"</span><span class="w">
    </span><span class="p">}</span><span class="w">
</span><span class="p">}</span></code></pre></figure>

- **contentType** - defines how data will be encoded {TEXT \| JSON \| BINARY}
- **data** - actual data that will be sent to the AWS Kinesis stream. 
- **metadata** - in this object you **must** place correct **streamName** value and **partitionKey** that will be used to identify correct stream in AWS Kinesis and partition key

Go to **Data Converters** and create new **downlink** Converter with this function: 
<figure class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="kd">var</span> <span class="nx">data</span> <span class="o">=</span> <span class="p">{</span>
    <span class="na">devName</span><span class="p">:</span> <span class="dl">"</span><span class="s2">kitchen_thermostat</span><span class="dl">"</span><span class="p">,</span>
    <span class="na">version</span><span class="p">:</span> <span class="nx">msg</span><span class="p">.</span><span class="nx">version</span>
<span class="p">};</span>

<span class="kd">var</span> <span class="nx">result</span> <span class="o">=</span> <span class="p">{</span>
    <span class="na">contentType</span><span class="p">:</span> <span class="dl">"</span><span class="s2">JSON</span><span class="dl">"</span><span class="p">,</span>
    <span class="na">data</span><span class="p">:</span> <span class="nx">JSON</span><span class="p">.</span><span class="nx">stringify</span><span class="p">(</span><span class="nx">data</span><span class="p">),</span>
    <span class="na">metadata</span><span class="p">:</span> <span class="p">{</span>
        <span class="na">streamName</span><span class="p">:</span> <span class="dl">"</span><span class="s2">st-test-downlink</span><span class="dl">"</span><span class="p">,</span>
        <span class="na">partitionKey</span><span class="p">:</span> <span class="dl">"</span><span class="s2">123</span><span class="dl">"</span><span class="p">,</span>
    <span class="p">}</span>

<span class="p">};</span>

<span class="k">return</span> <span class="nx">result</span><span class="p">;</span></code></pre></figure>

This converter will take **version** field from the incoming message and add it as a payload field in the outbound message. Additionally, we will put device name in the outbound message. In this way next applications in our business flow, that will consume messages from the donwlink stream, will be able to identify, that this payload belongs to **kitchen_thermostat** device.

![image](/images/user-guide/integrations/aws-kinesis/aws-kinesis-add-downlink-converter.webp)

### AWS Kinesis Integration

Next we will create Integration with AWS Kinesis inside the Sentient. Open **Integrations** section and add new Integration with type
**AWS Kinesis**

- Name: kinesis_integration
- Type: AWS Kinesis
- Uplink data converter: kinesis_converter
- Downlink data converter: kinesis_downlink_version
- Stream name: st-test-uplink
- Region: **AWS_REGION**
- Access Key Id: **AWS_ACCESS_KEY_ID**
- Access Key: **SECRET_ACCESS_KEY**
- Use credentials from the Amazon EC2 Instance Metadata Service: false (please refer to [IAM Roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) for more details)
- Use Consumers with Enhanced Fan-Out: false (please refer to [Using Consumers with Enhanced Fan-Out](https://docs.aws.amazon.com/streams/latest/dev/introduction-to-enhanced-consumers.html) for more details)

![image](/images/user-guide/integrations/aws-kinesis/aws-kinesis-add-integration_1.webp)

![image](/images/user-guide/integrations/aws-kinesis/aws-kinesis-add-integration_2.webp)

## Validation

### Validate Uplink Messages
Lets verify our integration. First, lets put message into uplink stream, so Sentient will fetch this message. 
Type in the console:
```bash
aws kinesis put-record --stream-name st-test-uplink --partition-key 123 --data '{"devName": "kitchen_thermostat", "devType": "thermostat", "temperature": 22}'
```

Go to **Device Group** -> **All** -> **kitchen_thermostat** - you can see that 

- new device was registered in the sentient
- In the **Latest Telemetry** section you will see that last submitted temperature = 22.

![image](/images/user-guide/integrations/aws-kinesis/aws-kinesis-validate-telemetry.webp)

### Validate Downlink Messages
For testing Downlink Messages, we will update our Root Rule Chain to send downlink message when device attribute is changed.
Open and edit **Root Rule Chain**. Add **Integration Downlink** Action node and connect it with the **Message Type Switch** Node using relation 
**Attributes Updated**
 
![image](/images/user-guide/integrations/aws-kinesis/aws-kinesis-downlink-node.webp)

![image](/images/user-guide/integrations/aws-kinesis/aws-kinesis-node-connected.webp)

Save Changes.

Go to **Device Group** -> **All** -> **kitchen_thermostat** -> attributes section. We will add **Shared attribute** with name **version** and
value **v.0.11**

![image](/images/user-guide/integrations/aws-kinesis/aws-kinesis-shared-attr-updated.webp)

By making this step, we triggered downlink message to the downlink stream **st-test-downlink** and this message should contains device name and version field value. 
Let's use command line AWS CLI tool to validate, that we have received the massage in the downlink stream.
First, we need to get shard iterator for the downlink stream, to get records from the stream:
```bash
aws kinesis get-shard-iterator --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON --stream-name st-test-downlink
```

In the output you will receive ID of the iterator:
<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">{</span><span class="w">
    </span><span class="nl">"ShardIterator"</span><span class="p">:</span><span class="w"> </span><span class="s2">"AAAAAAAAAAHHpat8cWmSZ1LSNg2oOra2yaRN/75ZhdwXFNZjnznXU1BQVjo9B+IVi3Pk6ltKN3V8Vhihi74MtXvG9rKcL9VRP1xRebo/NVjaMWd5FmAcp1rvs/DOahY+0FVm6UC1fKFwUXmgnsCzxkU9V8G9cFyGU/4Vvpf2PcrGsHG/JtNouCYT4wwdoXZ6FIFTuWdW7/Qs48PAZCkSjluwA7K1pld4"</span><span class="w">
</span><span class="p">}</span></code></pre></figure>

Now, let's use the **ShardIterator** from the above JSON in the **get-records** command:
```bash
aws kinesis get-records --shard-iterator **ShardIterator**
```

In our example:
```bash
aws kinesis get-records --shard-iterator AAAAAAAAAAFQtL3oAo74irn+ccC3vghADqqmh2MH+HKI9qYTi1NP957vDe8KyV6VdQ+I4shIP0HIRRVYyTZs0W9v6jaai9LevlJayMw6TgdPkVIGmV5SYZF8sGWgtd0wJuRqB+6QwCAUHQ52dgT4m+lypNSzJJw4Mo6h+9Wdk5fpwQxu/GlM8J+Uqblnq4EEr17FkWLahikaSZXktfLq5dh23+LEIc22
```

In the output you should receive records from the donwlink stream in the JSON format:
<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">{</span><span class="w">
    </span><span class="nl">"Records"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"Data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"eyJkZXZOYW1lIjoia2l0Y2hlbl90aGVybW9zdGF0IiwidmVyc2lvbiI6InYuMC4xMSJ9"</span><span class="p">,</span><span class="w"> 
            </span><span class="nl">"PartitionKey"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1234"</span><span class="p">,</span><span class="w"> 
            </span><span class="nl">"ApproximateArrivalTimestamp"</span><span class="p">:</span><span class="w"> </span><span class="mf">1569609612.27</span><span class="p">,</span><span class="w"> 
            </span><span class="nl">"SequenceNumber"</span><span class="p">:</span><span class="w"> </span><span class="s2">"49599912710236940383450082324919185009278025474345271298"</span><span class="w">
        </span><span class="p">}</span><span class="w">
    </span><span class="p">],</span><span class="w"> 
    </span><span class="nl">"NextShardIterator"</span><span class="p">:</span><span class="w"> </span><span class="s2">"AAAAAAAAAAFQlgSyxBdpKxlRrocJCYT9YDrCi/vxl0sstJgg4CM+pttVsK4AjjQwJ/QJsags5vdpQdopaqk9aKefAUOWobgwHVaZvhI4tdkmHBr45uO0Hq9AxUlKDxfiYbM0qgN33+5SvGxU8gJBUihYFY4ydPWOWdVTf2lOxp0a9X6DFrjsUqwMXR9skLw8/lQkBmHVFBlFURPy+z/AMuYHga5mDch/"</span><span class="p">,</span><span class="w"> 
    </span><span class="nl">"MillisBehindLatest"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="w">
</span><span class="p">}</span></code></pre></figure>

As Kinesis uses **Base64** for data presentation, we need to use some [online Base64 converter tool](https://base64decode.org) to encode from the **Base64** to JSON representative. As a result we will get next JSON payload: 
<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">{</span><span class="w">
    </span><span class="nl">"devName"</span><span class="p">:</span><span class="s2">"kitchen_thermostat"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"version"</span><span class="p">:</span><span class="s2">"v.0.11"</span><span class="w">
</span><span class="p">}</span></code></pre></figure>

Now other application is able to listen to this downlink stream and react accordingly to your business logic.

## See also
With this integration you can also configure Downlink converters and trigger required actions using Rule Engine nodes.

- [Integration Overview](/docs/user-guide/integrations/)
- [Uplink Converters](/docs/user-guide/integrations/#uplink-data-converter)
- [DownLink Converters](/docs/user-guide/integrations/#downlink-data-converter)
- [Rule Engine](/docs/user-guide/rule-engine-2-0/re-getting-started/)


## Next steps

### Monitor the Sentient Java application

To monitor Sentient application we will use the [Visual VM](https://visualvm.github.io/)
The JMX have been enabled in `docker-compose.yml` with this line

```bash
JAVA_OPTS: " -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=9999 -Dcom.sun.management.jmxremote.rmi.port=9999 -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Djava.rmi.server.hostname=127.0.0.1"
```

Let's **forward JMX port** from Sentient instance to the local machine

```bash
ssh -L 9999:127.0.0.1:9999 sentient 
```

Now we can connect with VisualVM to the Sentient application and discover the internals

![Sentient JMX overview with VisualVM](/images/reference/performance-aws-instances/method/chart-examples/performance_test_sentient_jmx_visual_vm_overview.png "Sentient JMX overview with VisualVM")


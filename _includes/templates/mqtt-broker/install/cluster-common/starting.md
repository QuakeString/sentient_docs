Execute the following command to deploy the broker:

```bash
./k8s-deploy-st-rmqtt.sh
```
{: .copy-code}

After a few minutes, you may execute the next command to check the state of all pods.

```bash
kubectl get pods
```
{: .copy-code}

If everything went fine, you should be able to see `st-rmqtt-0` and `st-rmqtt-1` pods. Every pod should be in the `READY` state.

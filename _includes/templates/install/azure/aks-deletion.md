## Cluster deletion

Execute the following command to delete all SENTIENT pods:

```bash
./k8s-delete-resources.sh
```
{: .copy-code}

Execute the following command to delete all SENTIENT pods and configmaps:

```bash
./k8s-delete-all.sh
```
{: .copy-code}

Execute the following command to delete EKS cluster (you should change the name of the cluster and zone):

```bash
az aks delete --resource-group myResourceGroup --name myAKSCluster
```
{: .copy-code}

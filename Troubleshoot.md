## Section 1: Troubleshoot commands for kubernetes:

```
kubectl version
kubectl get pods -n kube-system
kubectl get componentstatus
kubectl get nodes
journalctl -u kubelet
kubectl get pods --all-namespaces
```

## Section 2: Running commands via ansible

### ansible <gcp group> -a '<commands from Section 1>' -b

```
ansible label_type_master -a 'pods -n kube-system' -b
```
# The deployment documents for kubernetes cluster and the api are as under,

## Create the kubernetes nodes
```
cd kube-cluster/ansible
ansible-playbook -i inventories/gcp.yml playbooks/infra.yml -t createmastervm
ansible-playbook -i inventories/gcp.yml playbooks/infra.yml -t createworker1vm
ansible-playbook -i inventories/gcp.yml playbooks/infra.yml -t createworker2vm
```

## Commands to verify the gcp dynamic groups
```
ansible-inventory --graph
ansible all -a 'hostname'
ansible label_type_master -a 'hostname'
ansible label_type_worker -a 'hostname'
```

## Connecting to the newly created instance:
```
cat /dev/null > ~/.ssh/known_hosts
```

## Install kubernetes required components on all nodes
```
ansible-playbook -i inventories/gcp.yml -l all playbooks/kube.yml -t kinstallall -b
```

### Install kubernetes master required component. 
### NOTE: apt install kubectl on all nodes due to dependencies
```
ansible-playbook -i inventories/gcp.yml -l label_type_master playbooks/kube.yml -t kinstallmaster -b 
```

## Configure and initialize kubernetes master
```
ansible-playbook -i inventories/gcp.yml -l label_type_master playbooks/kube.yml -t kconfigmaster -b
```

## Verify if kubernetes master is Ready and all services are in Running status
```
ansible label_type_master -a 'kubectl get pods --all-namespaces' -b
ansible label_type_master -a 'kubectl get componentstatus' -b
ansible label_type_master -a 'kubectl get nodes' -b
ansible label_type_master -a 'journalctl -u kubelet' -b
```

## Configure the token on master and add the nodes to kubernetes master
```
ansible-playbook -i inventories/gcp.yml -l label_type_master playbooks/kube.yml -t kgettoken -b
ansible-playbook -i inventories/gcp.yml -l label_type_worker playbooks/kube.yml -t ksettoken -b 
```

## Check the nodes status again
```
ansible label_type_master -a 'kubectl get nodes' -b
```

## Perform following activities on master
```
ssh ansible@<master0ip> -i ../keys/private.key
```

### Install helm and helm charts as described in helm.md

## Deploy the application as follows,
```
kubectl create -f flask-deployment.yml
kubectl create -f flask-service.yml
kubectl create -f flask-ingress.yml
```

## Remove the vm nodes and save cost
```
ansible-playbook playbooks/infra.yml -t deleteworker2vm
ansible-playbook playbooks/infra.yml -t deleteworker1vm
ansible-playbook playbooks/infra.yml -t deletemastervm
```
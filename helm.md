
##
nginx-ingress controller installed by helm
##
```
curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -
sudo apt-get install apt-transport-https --yes
echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```

```
chmod 600 ~/.kube/config
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm install ingress --namespace ingress --create-namespace --set rbac.create=true,controller.kind=DaemonSet,controller.service.type=ClusterIP,controller.hostNetwork=true ingress-nginx/ingress-nginx
```


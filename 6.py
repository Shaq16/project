# Install Docker
sudo apt update
sudo apt install docker.io -y

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker

# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# Verify kubectl
kubectl version --client

# Install Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Verify Minikube
minikube version

# Start Kubernetes cluster
minikube start --driver=docker

# Check nodes
kubectl get nodes

# Create Pod
kubectl run my-pod --image=nginx --restart=Never

# Get Pods
kubectl get pods

# Describe Pod
kubectl describe pod my-pod

# Expose Pod
kubectl expose pod my-pod --type=NodePort --port=80 --name=my-service

# Access Service
minikube service my-service --url

# Create Deployment
kubectl create deployment my-deployment --image=nginx --replicas=2

# Check Deployments
kubectl get deployments

# Scale Deployment
kubectl scale deployment my-deployment --replicas=5

# Check Pods
kubectl get pods

# Delete Pod
kubectl delete pod pod-name

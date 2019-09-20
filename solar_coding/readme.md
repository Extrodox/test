Start minikube
    
    minikube start
    
execute context

    eval $(minikube docker-env)

To Build Docker image

    docker build --tag=solar_code:v0.0.1 .

To execute docker

    docker run -p 31001:4000 solar_code:v0.0.1

To deploy on kubernetes

    kubectl create -f solar_code.yml


Install requirement to run python client

    pip install requests fire

To execute python client

     python3.6 client.py --url http://localhost:31001 --data Pig

Accessing javascript client

    open client.html in browser
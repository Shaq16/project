# Install Docker
sudo apt update
sudo apt install docker.io -y

# Check Docker
docker --version
sudo systemctl start docker
sudo systemctl enable docker

# Create project
mkdir flaskapp
cd flaskapp

# Create app file
nano new.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask Docker App Running"

app.run(host='0.0.0.0', port=5000)

# Create requirements file
nano requirements.txt

flask

# Create Dockerfile
nano Dockerfile

FROM python:3-alpine3.15

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python3","new.py"]



# Build image
docker build -t newflaskapp .

# Check images
docker images

# Run container
docker run -d -p 5000:5000 newflaskapp

# Check running containers
docker ps

# Stop container
docker stop flaskcontainer


# Install Docker Compose
sudo apt update
sudo apt install docker-compose -y

# Create monitoring folder
mkdir monitoring
cd monitoring

# Create Prometheus config
nano prometheus.yml

# Paste:
# global:
scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

# Create Docker Compose file
nano docker-compose.yml

# Paste:
version: '3'

services:
  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"

# Start Prometheus and Grafana
sudo docker compose up -d

# Check containers
docker ps

# Open Prometheus
# http://localhost:9090

# Prometheus Query
# up

# Open Grafana
# http://localhost:3000

# Login
# Username: admin
# Password: admin

# Add Prometheus Data Source
# Connections -> Data Sources -> Add Data Source -> Prometheus

# URL:
# http://prometheus:9090

# Save & Test

# Create Dashboard
# Dashboards -> Create Dashboard -> Add Visualization

# Select datasource:
# prometheus

# Query:
# process_resident_memory_bytes

# Run Queries
# Apply
# Save Dashboard

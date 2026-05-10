# Create monitoring directory
mkdir monitoring
cd monitoring

# Create Prometheus config
nano prometheus.yml

# Paste:
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

# Run Prometheus
docker run -d \
--name prometheus \
-p 9090:9090 \
-v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
prom/prometheus

# Check container
docker ps

# Open Prometheus
# http://localhost:9090
# Status -> Target Health
# Query -> up -> Execute

# Run Grafana
docker run -d \
--name grafana \
-p 3000:3000 \
grafana/grafana

# Check container
docker ps

# Open Grafana
# http://localhost:3000
# Username: admin
# Password: admin

# Add Prometheus Data Source
# Connections -> Data Sources -> Add Data Source -> Prometheus
# URL:
# http://172.17.0.1:9090
# Save & Test

# Create Dashboard
# Dashboards -> Create Dashboard -> Add Visualization
# Select datasource: prometheus
# Click Code
# Query:
# up
# Run Queries
# Apply
# Save Dashboard

# Sample Queries
# up
# prometheus_build_info
# process_cpu_seconds_total
# process_resident_memory_bytes

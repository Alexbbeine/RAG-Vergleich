FROM neo4j:5.22.0

# -----------------------------
# Install system tools + Python
# -----------------------------
USER root
RUN apt-get update && apt-get install -y \
    python3 python3-pip supervisor git && \
    apt-get clean

# -----------------------------
# Neo4j Plugins (APOC etc.)
# -----------------------------
ENV NEO4JLABS_PLUGINS='["apoc"]'
ENV NEO4J_dbms_security_procedures_unrestricted=apoc.*
ENV NEO4J_AUTH=neo4j/password123

COPY ./plugins/apoc-5.22.0-core.jar /var/lib/neo4j/plugins

# -----------------------------
# Copy Python app
# -----------------------------
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

# -----------------------------
# Supervisor config
# -----------------------------
RUN mkdir -p /etc/supervisor/conf.d
COPY supervisor.conf /etc/supervisor/conf.d/supervisor.conf

# -----------------------------
# Expose Neo4j + your app ports
# -----------------------------
EXPOSE 7474 7687 8000

# -----------------------------
# Start via Supervisor
# -----------------------------
CMD ["supervisord", "-n", "-c", "/etc/supervisor/conf.d/supervisor.conf"]

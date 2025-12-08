FROM neo4j:5.22.0

# -----------------------------
# Neo4j Plugins (APOC etc.)
# -----------------------------
ENV NEO4JLABS_PLUGINS='["apoc"]'
ENV NEO4J_dbms_security_procedures_unrestricted=apoc.*
ENV NEO4J_AUTH=neo4j/ps_neo4jj

COPY ./plugins/apoc-5.22.0-core.jar /var/lib/neo4j/plugins

EXPOSE 7474 7687
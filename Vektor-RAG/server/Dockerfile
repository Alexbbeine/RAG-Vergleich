######## Base / runtime ########
FROM nvidia/cuda:12.4.0-base-ubuntu22.04 AS rag-framework

# 1️⃣ Systempakete + Python
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 2️⃣ Arbeitsverzeichnis
WORKDIR /home/ubuntu/app

# 3️⃣ Projektdateien kopieren
COPY pyproject.toml ./
COPY src ./src

# 4️⃣ Python-Abhängigkeiten direkt global installieren
RUN pip install --upgrade pip \
    && pip install torch==2.6.0 --index-url https://download.pytorch.org/whl/cu124 \
    && pip install .

# 5️⃣ Port freigeben
EXPOSE 8000

# 6️⃣ Startbefehl
CMD ["python3","-u", "./src/examples/seeder.py"]


######## Devcontainer ########
FROM rag-framework AS rag-framework-devcontainer

USER root
WORKDIR /home/ubuntu/app

RUN pip install -e .[development,test]

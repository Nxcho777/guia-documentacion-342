# Imagen educativa de Jenkins con herramientas necesarias para el pipeline.
FROM jenkins/jenkins:lts-jdk21
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    git python3 python3-venv python3-pip doxygen graphviz ca-certificates curl \
    && rm -rf /var/lib/apt/lists/*
USER jenkins

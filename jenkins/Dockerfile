FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    build-essential \
    debhelper \
    devscripts \
    rpm \
    dos2unix \
    curl \
    && curl -fsSL https://get.docker.com/builds/Linux/x86_64/docker-1.13.1.tgz | tar -xzC /usr/local/bin --strip-components=1 docker/docker \
    && rm -rf /var/lib/apt/lists/*

USER jenkins


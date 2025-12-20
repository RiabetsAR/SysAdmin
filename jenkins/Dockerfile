FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    build-essential \
    debhelper \
    devscripts \
    rpm \
    tar \
    dos2unix \
    git \
    wget \
    curl

RUN mkdir -p /var/jenkins_home/rpmbuild/{SOURCES,SPECS,BUILD,RPMS,SRPMS} && \
    chown -R jenkins:jenkins /var/jenkins_home/rpmbuild

USER jenkins

#!/usr/bin/env bash

#############################################
# Push images to the docker repo
# Make sure that you are logged in and/or have the correct repo
# If using AWS ECR make sure you generate the token
#############################################

STACK="nrl-workflows"

# Or quay, ecr, etc

AIRFLOW_VERSION="1.10.10"
REGISTRY="docker.io"
USER="jerowe"
TAG="${AIRFLOW_VERSION}-${GIT_SHA}"

AIRFLOW_REPO="apache-airflow"
AIRFLOW_SCHEDULER_REPO="apache-scheduler"
AIRFLOW_WORKER_REPO="apache-worker"

# or run the ./build-docker-images.sh script
docker-compose stop
docker-compose build

# docker-compose images here will get you the list of images

docker tag ${STACK}_airflow \
    ${REGISTRY}/${USER}/${AIRFLOW_REPO}:${TAG}
docker tag ${STACK}_airflow-worker \
    ${REGISTRY}/${USER}/${AIRFLOW_WORKER_REPO}:${TAG}
docker tag ${STACK}_airflow-scheduler \
    ${REGISTRY}/${USER}/${AIRFLOW_SCHEDULER_REPO}:${TAG}

docker push ${REGISTRY}/${USER}/${AIRFLOW_REPO}:${TAG}
docker push ${REGISTRY}/${USER}/${AIRFLOW_WORKER_REPO}:${TAG}
docker push ${REGISTRY}/${USER}/${AIRFLOW_SCHEDULER_REPO}:${TAG}

#!/usr/bin/env bash

# Make sure to run this from the
# code/docker/bitnami-apache-airflow-1.10.10
# or where your docker-compose stack lives

STACK="nrl-workflows"

docker-compose stop
docker-compose build

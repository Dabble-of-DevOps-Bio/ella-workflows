#!/usr/bin/env bash

STACK="bitnami-apache-airflow-11010"

docker-compose up -d
sleep 60

echo "Running tests!"

docker-compose exec airflow trigger_dag tutorial -c "{}"

docker-compose stop

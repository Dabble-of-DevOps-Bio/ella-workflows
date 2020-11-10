FROM docker.io/bitnami/airflow:1.10.10
# From here - https://github.com/bitnami/bitnami-docker-airflow/blob/master/1/debian-10/Dockerfile

USER root

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y vim && \
    rm -r /var/lib/apt/lists /var/cache/apt/archives

RUN bash -c "source /opt/bitnami/airflow/venv/bin/activate && \
    pip install flask-restful flask-cors && \
    deactivate"


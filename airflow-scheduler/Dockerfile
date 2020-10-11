FROM docker.io/bitnami/airflow-scheduler:1.10.10

USER root

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y vim && \
    rm -r /var/lib/apt/lists /var/cache/apt/archives

RUN bash -c "source /opt/bitnami/airflow/venv/bin/activate && \
    pip install flask-restful && \
    deactivate"

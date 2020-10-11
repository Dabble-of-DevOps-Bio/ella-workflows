# This is the class you derive to create a plugin
from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint, jsonify, request
import json
# from airflow.www.app import csrf
from airflow.www_rbac.app import csrf

# from flask_restful import Api, Resource, url_for


StatusBlueprint = Blueprint(
    'status', __name__,
    url_prefix='/status'
)


@StatusBlueprint.route('/', methods=['GET'])
@csrf.exempt
def status():
    """Adds localhost:8080/status/"""
    return jsonify({
        'hello': 'world',
        'status': 'GREAT',
    })


# Defining the plugin class
class StatusPlugin(AirflowPlugin):
    name = "status_plugin"
    operators = []
    sensors = []
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = [StatusBlueprint]
    menu_links = []

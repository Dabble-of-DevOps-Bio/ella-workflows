# This is the class you derive to create a plugin
from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint, jsonify, request
import json
from airflow.www_rbac.app import csrf

# from flask_restful import Api, Resource, url_for

# Declare blueprint to stick our REST API in

TutorialBlueprint = Blueprint(
    'tutorial', __name__,
    url_prefix='/tutorial'
)


# This will create an api with a prefix /tutorial

@TutorialBlueprint.route('/get_tutorial_data', methods=['POST'])
@csrf.exempt
def get_tutorial_data():
    """Adds localhost:8080/tutorial/get_tutorial_data"""
    request_data = json.loads(request.data.decode('utf-8'))
    results = {'context': request_data}
    return jsonify(results)


# Defining the plugin class
class TutorialPlugin(AirflowPlugin):
    name = "tutorial_plugin"
    operators = []
    sensors = []
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = [TutorialBlueprint]
    menu_links = []

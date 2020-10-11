# This is the class you derive to create a plugin
from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint, jsonify, request
import json
from airflow.www_rbac.app import csrf
from flask_restful import Api, Resource, url_for

# Declare blueprint to stick our REST API in

TodoBlueprint = Blueprint(
    'todo', __name__,
    url_prefix='/todo'
)

api = Api(TodoBlueprint)


class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"', 'id': id}


# This is on the /todo prefix
# localhost:8080/todo/todos/1
api.add_resource(TodoItem, '/todos/<int:id>')


# This is already done for us
# app.register_blueprint(api_bp)

# Defining the plugin class
class TodoPlugin(AirflowPlugin):
    name = "todo_plugin"
    operators = []
    sensors = []
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = [TodoBlueprint]
    menu_links = []

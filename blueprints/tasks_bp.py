from flask import Blueprint, jsonify, request
from pathlib import Path
import json

tasks_bp = Blueprint('tasks_bp', __name__, url_prefix='/api/tasks')
tasks_bp.dir_path = Path(__file__).parent.absolute()


@tasks_bp.route('/', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        with open(tasks_bp.dir_path/'sample_data.json', 'r') as in_file:
            json_data = json.load(in_file)
        task_data = json_data.get('tasks', [])
        return jsonify(task_data)

    elif request.method == 'POST':
        with open(tasks_bp.dir_path/'sample_data.json', 'w') as out_file:
            json.dump({'tasks': request.json}, out_file, indent=2)
        return 'success'

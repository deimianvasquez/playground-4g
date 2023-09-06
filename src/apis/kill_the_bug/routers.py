import os
from flask import Blueprint, request, json, jsonify
from .models import KillTheBug

kill_the_bug = Blueprint('kill-the-bug', __name__)
kill_the_bug_file_path = os.path.join(os.path.dirname(__file__), 'kill_the_bug.json')



@kill_the_bug.route('/pending_attempts/<int:level_id>', methods=['GET'])
def get_pending_attempts(level_id=None):
    if request.method == 'GET':
        if level_id is None or type(level_id) != int:
            return jsonify({"msg": "You must send a level_id"}), 400

        return 'get_pending_attempts'


@kill_the_bug.route('/add_attempt', methods=['POST'])
def add_attempt():
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        
        if data is None:
            return jsonify({"msg": "You must send a data"}), 400

        if 'username' not in data or 'character' not in data or 'level' not in data or 'commands' not in data:
            return jsonify({"msg": "You must send a username, character, level and commands"}), 400
        
        result = KillTheBug.add_attempt(kill_the_bug_file_path, data)

        if result is not None:
         
            
            return response = {
                "data":{
                    "pending_attempts": [result]
                },
                "code": 200
            }, 200

        else:
            return jsonify({"msg": "Internal server error"}), 500

        print(data)
        return 'add_attempt' 
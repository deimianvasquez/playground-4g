import os, json
from .models import Todo
from flask import Blueprint, jsonify, request, render_template


todo = Blueprint('todo', __name__)

todo_path = os.path.join(os.path.dirname(__file__), 'todos.json')


@todo.route('/', methods=['GET'])
def handle_index():
    if request.method == 'GET':
        return render_template('todo.html')


@todo.route('/user', methods=['GET'])
def get_all_users():
    if request.method == 'GET':
        todos = Todo.create_json_file(todo_path)

        if todos is None:
            return jsonify({"msg": "Internal server error"}), 500
        
        if todos is True:
            todos = Todo.get_all_users(todo_path)
            return jsonify(todos), 200


@todo.route('/user/<string:username>', methods=['GET'])
def get_all_todo(username=None):
    if request.method == 'GET':
        if username is None:
            return jsonify({"msg": "bad request"}), 400
        
        todos = Todo.get_all_todo_by_user(todo_path, username)

        if todos is None:
            return jsonify({"msg": f"The user {username} doesn't exists"}), 404
        
        if todos is not None:
            return jsonify(todos), 200
        

@todo.route('/user/<string:username>', methods=['PUT'])
def update_task(username=None):
    if request.method == 'PUT':
        Todo.create_json_file(todo_path)
        if username is None:
            return jsonify({"msg": "You must include a username in the URL of the request"}), 400
        
        todos = Todo.get_all_todo_by_user(todo_path, username)
        if todos is None:
            return jsonify({"msg": f"The user {username} doesn't exists"}), 404
            
        data = request.json
        if type(data) != list:
            return jsonify({"msg": "You must send an array in the body of the request"}), 400

        if len(data) >= 1:
            for task in data:
                if type(task) != dict:
                    return jsonify({"msg": "You must send an array of objects in the body of the request"}), 400
                if set(("label", "done")).issuperset(task):
                    if type(task['label']) != str:
                        return jsonify({"msg": "The label must be a string"}), 400
                    if type(task['done']) != bool:
                        return jsonify({"msg": "The done must be a boolean"}), 400
                else:
                    return jsonify({"msg": "You must send an array of objects with the following properties: label and done"}), 400   
        else:
            return jsonify({"msg": "You must send at least one task"}), 400 
        
        update_todo = Todo.update_all_todos_by_user(todo_path, username, data)
        if update_todo is True:
            return jsonify({"msg": f"{len(data)} tasks were updated successfully"}), 200
        else:
            return jsonify({"msg": "Internal server error"}), 500
    
            
@todo.route('/user/<string:username>', methods=['POST'])
def create_user(username=None):
    Todo.create_json_file(todo_path)
    try:
        data = request.json
    except Exception as error:
        return jsonify({"message": "You must add an empty array in the body of the request"}), 400

    if type(data) == list and len(data) == 0:
        users = Todo.get_all_users(todo_path)
        if username in users:
            return jsonify({"msg": "The user exist"}), 400
        else:
            user = Todo.create_user(todo_path, username)
            if user is True:
                return jsonify({"msg": f"The user {username} has been created successfully"}), 201
            else:
                return jsonify({"msg": "Internal server error"}), 500  
    else:
        return jsonify({"msg": "You must send an empty array in the body of the request"}), 400



@todo.route('/user/<string:username>', methods=['DELETE'])
def delete_task(username=None):
    if username is None:
        return jsonify({"msg": "You must include a username in the URL of the request"}), 400

    users = Todo.get_all_users(todo_path)
    if username not in users:
        return jsonify({"msg": f"The user {username} doesn't exist"}), 404
    else:
        user_delete = Todo.delete_user(todo_path, username)
        if user_delete is None:
            return jsonify({"msg": "Internal server error"}), 500
        return jsonify({"msg": f"The user {username} has been deleted successfully"}), 201
      
    
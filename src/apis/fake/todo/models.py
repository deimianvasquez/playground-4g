import os
import json
from uuid import uuid4 as uuid


class Todo():
    def __init__(self, label, done):
        self.label = label
        self.done = done
        self.id =  uuid().hex

    
    def serialize(self):
        return {
            "id": self.id,
            "label": self.label,
            "done": self.done
        }
        

    def create_json_file(todo_file_path):
        try:
            file = open(todo_file_path)
            file.close()
            return True

        except Exception as error:
            if error.errno == 2:
                with open(todo_file_path, 'w') as file:
                    json.dump([], file, indent=2)
                    file.close()
                    return True
            else:
                return None


    def get_all_users(todo_file_path):
        with open(todo_file_path, 'r') as file:
            data = json.load(file)
            file.close()
            users = []
            for todo in data:
                users.append(todo.get('username'))
            return users
        

    def get_all_todo_by_user(todo_file_path, username=None):
        with open(todo_file_path, 'r') as file:
            data = json.load(file)
            file.close()
           
            if username in Todo.get_all_users(todo_file_path):
                for todo in data:
                    if todo.get('username') == username:
                        return todo.get('todo')
            return None


    def update_all_todos_by_user( todo_file_path, username=None, data=None):
        todos_serialize = list(map(lambda todo: Todo(**todo).serialize(), data))
       
        with open(todo_file_path, 'r') as file:
            todos = json.load(file)
            for todo in todos:
                if todo.get('username') == username:
                    todo['todo'] = todos_serialize
            file.close()

        with open(todo_file_path, 'w') as file:
            json.dump(todos, file, indent=2, ensure_ascii=False)
            file.close()
        return True


    def create_user(todo_file_path, username=None):
        data = Todo(**{"label": "example task", "done": False}).serialize()

        with open(todo_file_path, 'r') as file:
            todos = json.load(file)
            with open(todo_file_path, 'w') as file:
                todos.append({"username": username, "todo": [
                    data
                ]})
                json.dump(todos, file, indent=2)
                file.close()
                return True
       

    def delete_user(todo_file_path, username=None):
        with open(todo_file_path, 'r') as file:
            todos = json.load(file)
            for todo in todos:
                if todo.get('username') == username:
                    todos.remove(todo)
                    with open(todo_file_path, 'w') as file:
                        json.dump(todos, file, indent=2)
                        file.close()
                        return True
            return None


    def add_task(todo_path, username=None, data=None):
        data = Todo(**data).serialize()
        with open(todo_path, 'r') as file:
            todos = json.load(file)
            for todo in todos:
                if todo.get('username') == username:
                    todo['todo'].append(data)
                    with open(todo_path, 'w') as file:
                        json.dump(todos, file, indent=2)
                        file.close()
                        return True
            return None
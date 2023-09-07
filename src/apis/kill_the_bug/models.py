import json
from random import randint
from datetime import datetime

class KillTheBug():
    def __init__(self, username, character, level, commands):
        self.id = randint(0, 100000000000)
        self.username = username
        self.character = character
        self.level = level
        self.commands = commands
        self.create_at = datetime.timestamp(datetime.now())


    def __str__(self):
        return f'{self.id} {self.username} {self.character} {self.level} {self.commands}'

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'character': self.character,
            'level': self.level,
            'commands': self.commands,
            'create_at': self.create_at
        }


    def create_json_file(kill_the_bug_file_path):
        try:
            file = open(kill_the_bug_file_path)
            file.close()
            return True

        except Exception as error:
            if error.errno == 2:
                data = {"data":{"pending_attempts": []}, "code":200}
                with open(kill_the_bug_file_path, 'w') as file:
                    json.dump(data, file, indent=2)
                    file.close()
                    return True
            else:
                return None


    @classmethod
    def add_attempt(cls, kill_the_bug_file_path, data):
        data = cls(**data)
        
        print(data.serialize())
        
        if KillTheBug.create_json_file(kill_the_bug_file_path):
            with open(kill_the_bug_file_path, 'r') as file:
                attempts = json.load(file)
                file.close()
                attempts.get('data').get('pending_attempts').append(data.serialize())
                with open(kill_the_bug_file_path, 'w') as file:
                    json.dump(attempts, file, indent=2)
                    file.close()
                    return data.serialize()
        else:
            return None
        
    def get_levels(kill_the_bug_file_path):
        if KillTheBug.create_json_file(kill_the_bug_file_path):
            with open(kill_the_bug_file_path, 'r') as file:
                attempts = json.load(file)
                file.close()
                return attempts
        else:
            return None
        
    def get_pending_attempts(kill_the_bug_file_path, level_id):
        if KillTheBug.create_json_file(kill_the_bug_file_path):
            with open(kill_the_bug_file_path, 'r') as file:
                attempts = json.load(file)
                file.close()
                pending_attempts = attempts.get('data').get('pending_attempts')
                result = []
                for attempt in pending_attempts:
                    if attempt.get('level') == level_id:
                        result.append(attempt)
                return result
        else:
            return None
import os
import json


class Sound():
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

    
    def get_all_sound(**kwargs):
        try:
            fx_path = kwargs.get('fx')
            sound_path = kwargs.get('sound')
            data = {}
           

            with open(fx_path, 'r') as file:
                fx = json.load(file)
                data.update({"fx": fx})
                file.close()
            
            with open(sound_path, 'r') as file:
                sound = json.load(file)
                data.update({"sound": sound})
                file.close()
            return data

        except Exception as error:
            return None
       

    def get_all_fx(fx_file_path):
        try:
            with open(fx_file_path, 'r') as file:
                fx = json.load(file)
                file.close()
                return fx
        
        except Exception as error:
            return None

    def get_all_songs(sound_file_path):
        try:
            with open(sound_file_path, 'r') as file:
                sound = json.load(file)
                file.close()
                return sound
        
        except Exception as error:
            return None
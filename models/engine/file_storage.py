#!/usr/bin/python3
"""this file aim to manage file storage for our project"""

import json

class FileStorage:
    """we are trying now to manages storage of our project models in JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of models representation of our objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Add a new object"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Save to file (serializes objects to the JSON file)"""
        with open(FileStorage.__file_path, 'w') as file:
            temp = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(temp, file)

    def reload(self):
        """Load from file (deserializes the JSON file to objects)"""
        try:
            print("File path: ", FileStorage.__file_path)
            with open(FileStorage.__file_path, "r") as file:
                loaded_data = json.load(file)

            FileStorage.__objects = {}
            for key, obj_dict in loaded_data.items():
                class_name, obj_id = key.split('.', 1)
                target_class = globals().get(class_name)
                if target_class:
                    obj_instance = target_class(**obj_dict)
                    FileStorage.__objects[key] = obj_instance
                else:
                    print("Class '{class_name}' not found")
        except FileNotFoundError:
            pass
        except Exception as e:
            print("Error reloading: {}".format(str(e)))

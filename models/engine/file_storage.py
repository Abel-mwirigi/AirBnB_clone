#!/usr/bin/python3
"""file to handle storage of objects"""

import json
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel

classes = {"Place": Place,
         "Review": Review,
         "BaseModel": BaseModel,
         "User": User
         "City": City,
         "State": State}

class FileStorage:
    """
    a class  that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """ adds obj in the __objects dict with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            data = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(data, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    clas_name = key.split(".")[0]
                    clas = self.classes[clas_name]
                    FileStorage.__objects[key] = clas(**value)

        except Exception:
            pass


#!/usr/bin/python3
""" This module is a seperate storage management (file storage).
Abstracting this from the BaseModel makes it independent so that we
can easily replace the storage system without re-coding everything everywhere.
"""


import os
import json
import models

class FileStorage:
    """defines a class for data interchange stream.
    Attributes:
        __file_path: path to the JSON file
        __objects - (dictionary): storage for all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Stores the given object in the __objects dictionary, using
        a unique key generated from the object's class name and ID attribute.
        This key is used for easy retrieval of the object later.
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
        """
        all_objs = FileStorage.__objects
        to_dict_repr = {k: v.to_dict() for k, v in all_objs.items()}
        with open(FileStorage.__file_path, "w") as json_stream:
            json.dump(to_dict_repr, json_stream)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path)
        """
        from models.base_model import BaseModel

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as json_file:
                deserialised = json.load(json_file)
                for obj_values in deserialised.values():
                    class_name = obj_values.get("__class__")
                    # validate input to eval() to make sure the evaluated expression is a class
                    if isinstance(class_name, str) and type(eval(class_name)) == type:
                        self.new(eval(class_name)(**obj_values))
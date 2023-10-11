#!/usr/bin/python3
""" This module is a seperate storage management (file storage).
Abstracting this from the BaseModel makes it independent so that we
can easily replace the storage system without re-coding everything everywhere.
"""
from json import dump, load


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
            dump(to_dict_repr, json_stream)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path)
        """
        from models.base_model import BaseModel

        # gate all defined classes mapped to a name str in this name space
        defined_classes = {"BaseModel": BaseModel}

        try:
            with open(FileStorage.__file_path) as json_str:
                deserialised = load(json_str)
                for obj_values in deserialised.values():
                    cls_name = obj_values["__class__"]
                    cls_obj = defined_classes[cls_name]
                    self.new(eval(cls_name)(**obj_values))
        except FileNotFoundError:
            pass




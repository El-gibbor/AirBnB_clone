#!/usr/bin/env python3
"""This module is for the serialization and desirialization of objs"""
from json import dump, load


class FileStorage:
    """defines a class for data interchange stream
    Attributes:
        __file_path: path to the JSON file
        __objects - (dictionary): storage for all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        dict_key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[dict_key] = obj

    def save(self):
        """serializes __objects to the JSON file (__file_path)"""
        object_dict = {}
        for keyz, valz in FileStorage.__objects.items():
            object_dict[keyz] = valz.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as JSONfile:
            dump(object_dict, JSONfile)

    def reload(self):
        from models.base_model import BaseModel
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        """
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as json_to_py:
                dict_objs = load(json_to_py)
                for obj_valz in dict_objs.values():
                    cls_name = obj_valz["__class__"]
                    del obj_valz["__class__"]
                    self.new(eval(cls_name)(**obj_valz))
        except FileNotFoundError:
            pass

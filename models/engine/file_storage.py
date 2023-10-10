#!/usr/bin/python3
""" This module is a seperate storage management (file storage).
Abstracting this from the BaseModel makes it independent so that we
can easily replace the storage system without re-coding everything everywhere.
"""
from json import dump, load
from models.base_model import BaseModel


class FileStorage:
    """ This class serializes instances to a JSON file and deserializes
    JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Stores the given object in the __objects dictionary, using
        a unique key generated from the object's class name and ID attribute.
        This key is used for easy retrieval of the object later.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """

        dict_repr = [value.to_dict for value in FileStorage.__objects.values()]
        with open(FileStorage.__file_path, 'w') as json_stream:
            dump(dict_repr, json_stream)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path)
        """

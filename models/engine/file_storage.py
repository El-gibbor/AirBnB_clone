#!/usr/bin/python3

"""
Module that contains class for storage and persistence between
sessions which is vital for an application such as this
"""

import json
import os


class FileStorage:
    """
    This FileStorage class manages persistency and storage between sessions,
    offering methods for adding JSON objects, saving, and retrieving data.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        simply returns all objects that have been saved in the
        form of a dictionary. useful for passing between sessions.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Create a new dictionary that will most likely be added to the
        __objects dictionary as a whole.
        Args:
            obj: new obj to add which will be converted to a dictionary
        """
        key_name = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key_name] = obj

    def save(self):
        """
        Write the new object to the file that stores all the dictionary
        entries as a way to save items and persistency
        """
        my_dict = {}
        with open(FileStorage.__file_path, "w", encoding="utf8") as file:
            for key, _ in FileStorage.__objects.items():
                my_dict[key] = FileStorage.__objects[key].to_dict()
            json.dump(my_dict, file)

    def reload(self):
        """ Reads serialized objs from a file, converts them from JSON
        format to a dictionary, and assigns the __objects attribute to them.
        If the file doesn't exist, no errors or exceptions are raised.
        """
        # # TODO: FIND A BETTER WAY OF ORGANISING THIS
        # from models.base_model import BaseModel

        # TODO FIX: check the cls_map method below, i created that method
        # so that we could also use it in the console by just caling the method
        # from there instead of re_mapping the classes in the console again.
        # IF it seem good to you, then you clean up this notes and merge.

        # # Store a key-pair value of each class and its string name
        # cls_map = {
        #         "BaseModel" : BaseModel,
        #     }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for objs in data.values():
                    cls_key = objs["__class__"]
        # get cls name from the dictionary of classes returned in cls_map func.
                    cls_name = self.cls_map()[cls_key]
                    self.new(cls_name(**objs))
        else:
            return

    def cls_map(self):
        """
            defines a mapping of class names to their respective class objects
            within the current scope. It allows dynamic association between
            string names representing classes and the actual class objects.
        Returns:
            dict: A dictionary containing class names as keys and the
                    corresponding class objects as its values.
        """
        from models.base_model import BaseModel

        all_classes = {
                "BaseModel" : BaseModel,
            }
        return all_classes

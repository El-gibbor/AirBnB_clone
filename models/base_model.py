#!/usr/bin/python3
""" This module holds a super class that  defines all
    common attributes/methods for other classes (its sub classes)

"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ Defines a class Basemodel from which its subclasses will
    inherit from.
    """
    def __init__(self, *args, **kwargs):
        """ initialises all public instance attributes """

        if kwargs:
            del kwargs["__class__"]
            for keys, val in kwargs.items():
                if "created_at" in keys or "updated_at" in keys:
                    # convert its value (previously a str) to datetime object
                    dt_time = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, keys, dt_time)
                else:
                    setattr(self, keys, val)
        else:
            self.id = "{}".format(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """ returns a string representaion of the class and
        its attr in the below format
        """
        return "[{:s}] ({:s}) {}".format(
            type(self).__name__, self.id, self.__dict__
            )

    def save(self):
        """ updates the public instance attribute 'updated_at'
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns dictionary representation containing all attr of
        an instance. a key __class__ with the class name of the
        obj is added """

        dict_repr = {}
        dict_repr["__class__"] = "{}".format(type(self).__name__)
        for keys, val in self.__dict__.items():
            if "created_at" in keys or "updated_at" in keys:
                dict_repr[keys] = val.isoformat()
            else:
                dict_repr[keys] = val
        return dict_repr

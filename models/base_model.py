#!/usr/bin/python3
""" This module holds a super class that  defines all
    common attributes/methods for other classes (its sub classes)

"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Defines a class Basemodel from which its subclasses will
    inherit from.
    """
    def __init__(self) -> None:
        """ initialises all public instance attributes """

        self.id = "{}".format(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

    def to_dict(self):
        """ returns dictionary representation"""
#!/usr/bin/env python3
"""base class module: This class defines the attribute/method
logic and behaviour of the subclasses
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Base class that defines subclass methods and attr logic"""

    def __init__(self, *args, **kwargs):
        """instantiating public instance attributes
        Args
            args: list of arbitrary positional arguments
            kwargs - (dictionary): arbitrary key-value pair args.
        """

        if kwargs:
            for keyz, valz in kwargs.items():
                if keyz in ("created_at", "updated_at"):
                    valz = datetime.strptime(valz, '%Y-%m-%dT%H:%M:%S.%f')
                if keyz != '__class__':
                    self.__dict__[keyz] = valz
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """print in this format [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates public instance attr "updated_at" with the current d-time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns key-value pair of class instance using __dict__"""
        inst_dict = {}
        for keyz, valz in self.__dict__.items():
            inst_dict["__class__"] = self.__class__.__name__
            if keyz in ("created_at", "updated_at"):
                inst_dict[keyz] = valz.isoformat()
            else:
                inst_dict[keyz] = valz
        return inst_dict

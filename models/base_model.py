#!/usr/bin/env python3
"""base class module: This class defines the attribute/method
logic and behaviour of the subclasses
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """defines the base model class"""

    def __init__(self):
        """instantiating public instance attributes"""

        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self) -> str:
        """prints class name, instance id & instance dict in a given format"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates public instance attr "updated_at" with the current d-time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns key-value pair (dictionary) of __dict__ of class instance"""
        instance_dict = {}
        instance_dict["__class__"] = self.__class__.__name__
        for keyz, valz in self.__dict__.items():
            if keyz in ("created_at", "updated_at"):
                # convert timestamp value pair to ISO format
                timeValue = valz.isoformat()
                instance_dict[keyz] = timeValue
            else:
                instance_dict[keyz] = valz
        return instance_dict

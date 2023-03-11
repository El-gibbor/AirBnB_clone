#!/usr/bin/env python3
"""base class module: This class defines the attribute/method
logic and behaviour of the subclasses
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class that defines subclass methods and attr logic"""

    def __init__(self, *args, **kwargs):
        """instantiating public instance attributes
        Args
            args: list of arbitrary positional arguments
            kwargs - (dictionary): arbitrary key-value pair args.
        """
        # if kwargs:
        #     kwargs.pop("__class__") if "__class__" in kwargs else None
        #     for k, v in kwargs.items():
        #         if k in ("created_at", "updated_at"):
        #             setattr(self, k, datetime.now().isoformat())
        #         else:
        #             setattr(self, k, v)
        # self.id = str(uuid4())
        # self.created_at = self.updated_at = datetime.now()
        #   def __init__(self, *args, **kwargs):
        if kwargs:
            time = None
            kwargs.pop("__class__")
            for key, value in kwargs.items():
                if key in ('created_at','updated_at'):
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, time)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)


    def __str__(self):
        """print in this format [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates public instance attr "updated_at" with the current d-time"""
        self.updated_at = datetime.now()

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

# my_model = BaseModel()
# my_model.name = "My_First_Model"
# my_model.my_number = 89
# print(my_model.id)
# print(my_model)
# print(type(my_model.created_at))
# print("--")
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

# print("--")
# my_new_model = BaseModel(**my_model_json)
# print(my_new_model.id)
# print(my_new_model)
# print(type(my_new_model.created_at))

# print("--")
# print(my_model is my_new_model)

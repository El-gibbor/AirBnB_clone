#!/usr/bin/python3
""" This module holds the user class implementation, a subclass
of BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ a class that defines a new user in the application.
    Args:
        email (str): users email address
        password (str): the users password
        first_name (str): users first name
        last_name (str): the users last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
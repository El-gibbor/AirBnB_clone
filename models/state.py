#!/usr/python3
""" Module defining the State class for representing states in
the Airbnb application.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State class for representing states in the Airbnb application.

    Public class attributes:
        name (str): Empty string by default, representing the state's name.
    """
    name = ""
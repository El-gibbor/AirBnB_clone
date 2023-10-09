#!/usr/bin/python3

from uuid import uuid4
from unittest import TestCase
from models.base_model import BaseModel

class Test_BaseModel(TestCase):
    def test_id_type(self):
        self.base_obj = BaseModel()
        self.assertIsInstance(self.base_obj.id, str)
#!/usr/bin/python3
"""
Unittest for BaseModel Class
"""

import unittest
from uuid import uuid4
from datetime import datetime, timezone
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Class for unittest of BaseModel"""

    @classmethod
    def setUpClass(self):
        self.base1 = BaseModel()
        self.base1.name = "Siphelele"
        self.base1.my_number = 34

    def test_init(self):
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_atritt(self):
        self.assertTrue(hasattr(self.base1, "__init__"))
        self.assertTrue(hasattr(self.base1, "to_dict"))
        self.assertTrue(hasattr(self.base1, "save"))
        self.assertTrue(hasattr(self.base1, "__str__"))

    def test_dict(self):
        my_dict = self.base1.to_dict()
        self.assertEqual(my_dict["id"], self.base1.id)
        self.assertEqual(my_dict["name"], self.base1.name)
        self.assertEqual(my_dict["created_at"], self.base1.created_at.isoformat())
        self.assertEqual(my_dict["updated_at"], self.base1.updated_at.isoformat())
        self.assertEqual(my_dict["__class__"], type(self.base1).__name__)

    def test_save(self):
        beforeUpdated_at = self.base1.updated_at
        beforeCreated_at = self.base1.created_at
        self.base1.save()
        self.assertEqual(self.base1.created_at, beforeCreated_at)
        self.assertNotEqual(self.base1.updated_at, beforeUpdated_at)

if __name__ == "__main__":
    unittest.main()

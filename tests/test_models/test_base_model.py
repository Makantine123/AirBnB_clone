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

    def test_doc(self):
        self.assertNotEqual(len(BaseModel.__doc__), 0)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

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

    def test_instance_creation_kwargs(self):
        "Kwargs dictionary"
        mydict = {"id": "1111111-11111-11111-11111-11111",
                   "created_at": "2023-03-28T21:03:54.053212",
                   "__class__": "BaseModel",
                   "updated_at": "2023-03-28T21:03:54.057521"}
        base2 = BaseModel(**mydict)
        # Check if attributes exists
        self.assertTrue(hasattr(base2, "id"))
        self.assertTrue(hasattr(base2, "created_at"))
        self.assertTrue(hasattr(base2, "updated_at"))
        self.assertTrue(hasattr(base2, "__class__"))
        self.assertTrue(base2.__class__ not in base2.__dict__)
        # Check DateTime formats and Values
        self.assertEqual(base2.id, "1111111-11111-11111-11111-11111")
        self.assertEqual(base2.created_at.isoformat(), "2023-03-28T21:03:54.053212")
        self.assertEqual(base2.updated_at.isoformat(), "2023-03-28T21:03:54.057521")

if __name__ == "__main__":
    unittest.main()

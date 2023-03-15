#!/usr/bin/python3
"""
Unittest for Amenity Class
"""

import unittest
import os
import io

from os import path, remove
from uuid import uuid4
from datetime import datetime, timezone

from models.base_model import BaseModel
from models.amenity import Amenity


class Test_user_instance(unittest.TestCase):
    """
    Test the user instance
    """

    def tearDown(self):
        """
        Tear down all methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """
        Check user imports BaseModel
        """
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))

    def test_instance_args(self):
        """
        Check user args in BaseModel
        """
        amenity = Amenity(123, "Siphelele", ["Makhathini"])
        self.assertTrue(isinstance(amenity, BaseModel))

    def test_instance_kwargs(self):
        """
        Check user kwargs in BaseModel
        """
        args = {"name": "Siphelele"}
        amenity = Amenity(**args)
        self.assertTrue(isinstance(amenity, BaseModel))


class Test_class_amenity_attributes(unittest.TestCase):
    """
    Test User class attributes
    """

    def tearDown(self):
        """
        Tear down all methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def Test_amenity_attributes(self):
        """
        Check if User class contains all attributes
        """
        amenity = Amenity()
        attr = "name"
        ndict = amenity.__dict__
        self.assertTrue(hasattr(amenity, attr))
        self.assertFalse(attr in ndict)
        self.assertEqual(getattr(amenity, attr, False), "")

    def Test_set_amentiy_attributes(self):
        """
        Check is User class can set attributes
        """
        amenity = Amenity()
        attr = "name"
        value = "Siphelele"
        setattr(Amenity, attr, value)
        self.assertEqual(getattr(amenity, attr, False), value)
        self.assertEqual(getattr(amenity.__class__, attr, False), "")


class Test_initAmenity(unittest.TestCase):
    """
    Class for unittest __init__
    """

    def tearDown(self):
        """
        Tear down all methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def Test_attribute_type(self):
        """
        Check the attribute try
        """
        amenity = Amenity()
        self.assertEqual(type(amenity.id), str)
        self.assertEqual(type(amenity.created_at), datetime)
        self.assertEqual(type(amenity.updated_at), datetime)

    def Test_unique_id(self):
        """
        Check if unique id are created
        """
        amenity1 = Amenity()
        amenity2 = Amenity()
        amenity3 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)
        self.assertNotEqual(amenity2.id, amenity3.id)
        self.assertNotEqual(amenity3.id, amenity1.id)

    def Test_attributes_exist(self):
        """
        Check if Amenity attributes exist
        """
        amenity = Amenity()
        amenity.name = "Siphelele"
        self.assertEqual(getattr(amenity, "name", False), "Siphelele")
        self.assertTrue("name" in amenity.__dict__)

    def test_instance_creation_kwarg(self):
        """
        Check creation of user using kwargs
        """
        data = {"id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
                "created_at": "2017-09-28T21:03:54.053212",
                "__class__": "User",
                "updated_at": "2017-09-28T21:03:54.056212"}
        amenity = Amenity(**data)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "__class__"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(amenity.__class__ not in amenity.__dict__)
        self.assertEqual(
                amenity.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(
                amenity.created_at.isoformat(), "2017-09-28T21:03:54.053212")
        self.assertEqual(
                amenity.updated_at.isoformat(), "2017-09-28T21:03:54.056212")

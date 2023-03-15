#!/usr/bin/python3
"""
Unittest for City Class
"""

import unittest
import os
import io

from os import path, remove
from uuid import uuid4
from datetime import datetime, timezone

from models.base_model import BaseModel
from models.city import City


class Test_city_instance(unittest.TestCase):
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
        city = City()
        self.assertTrue(isinstance(city, BaseModel))

    def test_instance_args(self):
        """
        Check user args in BaseModel
        """
        city = City(123, "Siphelele", ["Makhathini"])
        self.assertTrue(isinstance(city, BaseModel))

    def test_instance_kwargs(self):
        """
        Check user kwargs in BaseModel
        """
        args = {"name": "Siphelele"}
        city = City(**args)
        self.assertTrue(isinstance(city, BaseModel))


class Test_class_city_attributes(unittest.TestCase):
    """
    Test City class attributes
    """

    def tearDown(self):
        """
        Tear down all methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def Test_city_attributes(self):
        """
        Check if User class contains all attributes
        """
        city = City()
        attr = ["state_id", "name"]
        ndict = city.__dict__
        for key in attr:
            self.assertTrue(hasattr(city, key))
            self.assertFalse(key in ndict)
            self.assertEqual(getattr(city, key, False), "")

    def Test_set_amentiy_attributes(self):
        """
        Check is User class can set attributes
        """
        city = City()
        attr = ["state_id", "name"]
        value = ["123", "Richards Bay"]
        for key, val in zip(attr, value):
            setattr(City, key, val)
            self.assertEqual(getattr(city, key, False), val)
            self.assertEqual(getattr(city.__class__, key, False), "")


class Test_initCity(unittest.TestCase):
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
        city = City()
        self.assertEqual(type(city.id), str)
        self.assertEqual(type(city.created_at), datetime)
        self.assertEqual(type(city.updated_at), datetime)

    def Test_unique_id(self):
        """
        Check if unique id are created
        """
        city1 = City()
        city2 = City()
        city3 = City()
        self.assertNotEqual(city1.id, city2.id)
        self.assertNotEqual(city2.id, city3.id)
        self.assertNotEqual(city3.id, city1.id)

    def Test_attributes_exist(self):
        """
        Check if City attributes exist
        """
        city = City()
        city.name = "Siphelele"
        self.assertEqual(getattr(city, "name", False), "Siphelele")
        self.assertTrue("name" in city.__dict__)

    def test_instance_creation_kwarg(self):
        """
        Check creation of user using kwargs
        """
        data = {"id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
                "created_at": "2017-09-28T21:03:54.053212",
                "__class__": "User",
                "updated_at": "2017-09-28T21:03:54.056212"}
        city = City(**data)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "__class__"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(city.__class__ not in city.__dict__)
        self.assertEqual(
                city.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(
                city.created_at.isoformat(), "2017-09-28T21:03:54.053212")
        self.assertEqual(
                city.updated_at.isoformat(), "2017-09-28T21:03:54.056212")

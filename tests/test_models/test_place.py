#!/usr/bin/python3
"""
Unittest for Place Class
"""

import unittest
import os
import io

from os import path, remove
from uuid import uuid4
from datetime import datetime, timezone

from models.base_model import BaseModel
from models.place import Place


class Test_place_instance(unittest.TestCase):
    """
    Test the place instance
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
        Check place imports BaseModel
        """
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))

    def test_instance_args(self):
        """
        Check place args in BaseModel
        """
        place = Place(123, "Siphelele", ["Makhathini"])
        self.assertTrue(isinstance(place, BaseModel))

    def test_instance_kwargs(self):
        """
        Check place kwargs in BaseModel
        """
        args = {"name": "Siphelele"}
        place = Place(**args)
        self.assertTrue(isinstance(place, BaseModel))


class Test_class_place_attributes(unittest.TestCase):
    """
    Test Place class attributes
    """

    def tearDown(self):
        """
        Tear down all methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def Test_place_attributes(self):
        """
        Check if User class contains all attributes
        """
        place = Place()
        attr = ["city_id", "user_id", "name", "description", "number_rooms",
                "number_bathrooms", "max_guest", "price_by_night", "latitude",
                "longitude", "amenity_ids"]
        ndict = place.__dict__
        for key in attr:
            self.assertTrue(hasattr(place, key))
            self.assertFalse(key in ndict)
            self.assertEqual(getattr(place, key, False), "")

    def Test_set_place_attributes(self):
        """
        Check is User class can set attributes
        """
        place = Place()
        attr = ["city_id", "user_id", "name", "description", "number_rooms",
                "number_bathrooms", "max_guest", "price_by_night", "latitude",
                "longitude", "amenity_ids"]
        value = ["123", "123", "Sphe", "Test", "5", "2", "10", "1500.00",
                 "125", "125", "123"]
        for key, val in zip(attr, value):
            setattr(Place, key, val)
            self.assertEqual(getattr(place, key, False), val)
            self.assertEqual(getattr(place.__class__, key, False), "")


class Test_initPlace(unittest.TestCase):
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
        place = Place()
        self.assertEqual(type(place.id), str)
        self.assertEqual(type(place.created_at), datetime)
        self.assertEqual(type(place.updated_at), datetime)

    def Test_unique_id(self):
        """
        Check if unique id are created
        """
        place1 = Place()
        place2 = Place()
        place3 = Place()
        self.assertNotEqual(place1.id, place2.id)
        self.assertNotEqual(place2.id, place3.id)
        self.assertNotEqual(place3.id, place1.id)

    def Test_attributes_exist(self):
        """
        Check if Place attributes exist
        """
        place = Place()
        place.name = "Siphelele"
        self.assertEqual(getattr(place, "name", False), "Siphelele")
        self.assertTrue("name" in place.__dict__)

    def test_instance_creation_kwarg(self):
        """
        Check creation of place using kwargs
        """
        data = {"id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
                "created_at": "2017-09-28T21:03:54.053212",
                "__class__": "User",
                "updated_at": "2017-09-28T21:03:54.056212"}
        place = Place(**data)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "__class__"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(place.__class__ not in place.__dict__)
        self.assertEqual(
                place.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(
                place.created_at.isoformat(), "2017-09-28T21:03:54.053212")
        self.assertEqual(
                place.updated_at.isoformat(), "2017-09-28T21:03:54.056212")

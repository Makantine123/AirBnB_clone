#!/usr/bin/python3
"""
Unittest for User Class
"""

import unittest
import os
import io

from os import path, remove
from uuid import uuid4
from datetime import datetime, timezone

from models.base_model import BaseModel
from models.user import User


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
        user = User()
        self.assertTrue(isinstance(user, BaseModel))

    def test_instance_args(self):
        """
        Check user args in BaseModel
        """
        user = User(123, "Siphelele", ["Makhathini"])
        self.assertTrue(isinstance(user, BaseModel))

    def test_instance_kwargs(self):
        """
        Check user kwargs in BaseModel
        """
        args = {"name": "Siphelele"}
        user = User(**args)
        self.assertTrue(isinstance(user, BaseModel))


class Test_class_user_attributes(unittest.TestCase):
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

    def Test_user_attributes(self):
        """
        Check if User class contains all attributes
        """
        user = User()
        attr = ["email", "password", "first_name", "last_name"]
        ndict = user.__dict__
        for i in attr:
            self.assertTrue(hasattr(user, i))
            self.assertFalse(i in ndict)
            self.assertEqual(getattr(user, i, False), "")

    def Test_set_user_attributes(self):
        """
        Check is User class can set attributes
        """
        user = User()
        attr = ["email", "password", "first_name", "last_name"]
        values = ["12345@gmail.com", "password", "Sphe", "Mak"]
        for key, val in zip(attr, values):
            setattr(user, key, val)
            self.assertEqual(getattr(User, key, False), val)
            self.assertEqual(getattr(user.__class__, key, False), "")

    def Test_assign_user_attributes(self):
        """
        Check if values can be assigned to attributes
        """
        user = User()
        user.first_name = "Sphe"
        user.last_name = "Makh"
        user.email = "123@gmail.com"
        user.password = "123"
        self.assertEqual(getattr(user, user.first_name, False), "Sphe")
        self.assertEqual(getattr(user, user.last_name, False), "Makh")
        self.assertEqual(getattr(user, user.email, False), "123@gmail.com")
        self.assertEqual(getattr(user, user.password, False), "123")


class Test_initUser(unittest.TestCase):
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
        user = User()
        self.assertEqual(type(user.id), str)
        self.assertEqual(type(user.created_at), datetime)
        self.assertEqual(type(user.updated_at), datetime)

    def Test_unique_id(self):
        """
        Check if unique id are created
        """
        user1 = User()
        user2 = User()
        user3 = User()
        self.assertNotEqual(user1.id, user2.id)
        self.assertNotEqual(user2.id, user3.id)
        self.assertNotEqual(user3.id, user1.id)

    def Test_attributes_exist(self):
        """
        Check if user attributes exist
        """
        user = User()
        user.first_name = "Siphelele"
        user.last_name = "Makhathini"
        user.email = "siphelele.mlungisi@gmail.com"
        user.password = "12345"
        self.assertEqual(getattr(user, "first_name", False), "Siphelele")
        self.assertEqual(getattr(user, "last_name", False), "Makhathini")
        self.assertEqual(getattr(
            user, "email", False), "siphelele.mlungisi@gmail.com")
        self.assertEqual(getattr(user, "password", False), "12345")
        self.assertTrue("email" in user.__dict__)
        self.assertTrue("password" in user.__dict__)
        self.assertTrue("first_name" in user.__dict__)
        self.assertTrue("last_name" in user.__dict__)

    def test_instance_creation_kwarg(self):
        """
        Check creation of user using kwargs
        """
        data = {"id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
                "created_at": "2017-09-28T21:03:54.053212",
                "__class__": "User",
                "updated_at": "2017-09-28T21:03:54.056212"}
        user = User(**data)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "__class__"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(user.__class__ not in user.__dict__)
        self.assertEqual(
                user.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(
                user.created_at.isoformat(), "2017-09-28T21:03:54.053212")
        self.assertEqual(
                user.updated_at.isoformat(), "2017-09-28T21:03:54.056212")

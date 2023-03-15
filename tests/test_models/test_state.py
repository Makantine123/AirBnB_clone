#!/usr/bin/python3
"""
Unittest for State Class
"""

import unittest
import os
import io

from os import path, remove
from uuid import uuid4
from datetime import datetime, timezone

from models.base_model import BaseModel
from models.state import State


class Test_state_instance(unittest.TestCase):
    """
    Test the state instance
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
        Check state imports BaseModel
        """
        state = State()
        self.assertTrue(isinstance(state, BaseModel))

    def test_instance_args(self):
        """
        Check state args in BaseModel
        """
        state = State(123, "Siphelele", ["Makhathini"])
        self.assertTrue(isinstance(state, BaseModel))

    def test_instance_kwargs(self):
        """
        Check state kwargs in BaseModel
        """
        args = {"name": "Siphelele"}
        state = State(**args)
        self.assertTrue(isinstance(state, BaseModel))


class Test_class_state_attributes(unittest.TestCase):
    """
    Test State class attributes
    """

    def tearDown(self):
        """
        Tear down all methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def Test_state_attributes(self):
        """
        Check if User class contains all attributes
        """
        state = State()
        attr = "name"
        ndict = state.__dict__
        for key in attr:
            self.assertTrue(hasattr(state, key))
            self.assertFalse(key in ndict)
            self.assertEqual(getattr(state, key, False), "")

    def Test_set_state_attributes(self):
        """
        Check is User class can set attributes
        """
        state = State()
        attr = "name"
        value = "Siphelele"
        for key, val in zip(attr, value):
            setattr(State, key, val)
            self.assertEqual(getattr(state, key, False), val)
            self.assertEqual(getattr(state.__class__, key, False), "")


class Test_initState(unittest.TestCase):
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
        state = State()
        self.assertEqual(type(state.id), str)
        self.assertEqual(type(state.created_at), datetime)
        self.assertEqual(type(state.updated_at), datetime)

    def Test_unique_id(self):
        """
        Check if unique id are created
        """
        state1 = State()
        state2 = State()
        state3 = State()
        self.assertNotEqual(state1.id, state2.id)
        self.assertNotEqual(state2.id, state3.id)
        self.assertNotEqual(state3.id, state1.id)

    def Test_attributes_exist(self):
        """
        Check if State attributes exist
        """
        state = State()
        state.name = "Siphelele"
        self.assertEqual(getattr(state, "name", False), "Siphelele")
        self.assertTrue("name" in state.__dict__)

    def test_instance_creation_kwarg(self):
        """
        Check creation of state using kwargs
        """
        data = {"id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
                "created_at": "2017-09-28T21:03:54.053212",
                "__class__": "User",
                "updated_at": "2017-09-28T21:03:54.056212"}
        state = State(**data)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "__class__"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(state.__class__ not in state.__dict__)
        self.assertEqual(
                state.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(
                state.created_at.isoformat(), "2017-09-28T21:03:54.053212")
        self.assertEqual(
                state.updated_at.isoformat(), "2017-09-28T21:03:54.056212")

#!/usr/bin/python3
"""Unnittest for file_storage.py"""
# System Imports
import unittest
import os
import json
# Importing Relative links
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models import storage
# Importing from system imports
from os import path, remove


class Test_all(unittest.TestCase):
    """
    Test for all method FileStorage class
    """

    def setUp(self):
        """
        Set up methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """
        Tear down all methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_empty(self):
        """
        Test empty dictionary
        """
        self.assertEqual(storage.all(), {})

    def test_basemodel(self):
        """
        Test basemodel class
        """
        base = BaseModel()
        name = base.__class__.__name__ + "." + base.id
        ndict = {name: base}
        self.assertEqual(storage.all(), ndict)

    def test_user(self):
        """
        Test user class
        """
        user = User()
        name = user.__class__.__name__ + "." + user.id
        ndict = {name: user}
        self.assertEqual(storage.all(), ndict)


class Test_new(unittest.TestCase):
    """
    Test for new method FileStorage class
    """

    def setUp(self):
        """
        Set up methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass
        self._FileStorage__objects = {}

    def tearDown(self):
        """
        Tear down all methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_no_arg(self):
        """
        Test no arguments
        """
        with self.assertRaises(TypeError):
            storage.new()

    def test_too_many_arg(self):
        """
        Test too many arguments
        """
        base = BaseModel()
        with self.assertRaises(TypeError):
            storage.new(base, base)

    def test_basenew(self):
        """
        Test new BaseModel
        """
        ndict = {"id": "123"}
        base = BaseModel(**ndict)
        key = base.__class__.__name__ + "." + "123"
        dictlist = storage.all()
        self.assertEqual(type(dictlist), dict)
        storage.new(base)
        dictlist = storage.all()
        self.assertEqual(base, dictlist[key])

    def test_baseuser(self):
        """
        Test new User
        """
        ndict = {"first_name": "Siphelele", "last_name:": "Makhathini",\
                 "id": "123"}
        user = User(**ndict)
        key = user.__class__.__name__ + "." + "123"
        dictlist = storage.all()
        self.assertEqual(type(dictlist), dict)
        storage.new(user)
        dictlist = storage.all()
        self.assertEqual(user, dictlist[key])


class Test_save(unittest.TestCase):
    """
    Test for save method FileStorage class
    """

    def setUp(self):
        """
        Set up methods
        """
        try:
            remove("file.json")
        except:
            pass
        self._FileStorage__objects = {}

    def tearDown(self):
        """
        Tear down all methods
        """
        try:
            remove("file.json")
        except:
            pass

    def test_save_base(self):
        """ Save method with base model """
        dic = {"id": "123"}
        b = BaseModel(**dic)
        key = b.__class__.__name__ + '.' + "123"
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.new(b)
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            # self.assertEqual(b.id, pobj[key]["id"])
            # self.assertEqual(b.__class__.__name__, pobj[key]["__class__"])

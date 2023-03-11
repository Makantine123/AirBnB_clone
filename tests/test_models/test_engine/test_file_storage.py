#!/usr/bin/python3
"""Unnittest for file_storage.py"""
# System Imports
import unittest
import os
import json
# Importing Relative links
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
# Importing from system imports
from os import path, remove


class test_Storage(unittest.TestCase):
    """ Unnitest for file_storage module """

    def test_All(self):
        fileStore1 = FileStorage()
        inst_dict = fileStore1.all()
        self.assertIsNotNone(inst_dict)
        self.assertTrue(isinstance(inst_dict, dict))
        self.assertIs(inst_dict, fileStore1._FileStorage__objects)

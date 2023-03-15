#!/usr/bin/python3
"""
Unittest for Review Class
"""

import unittest
import os
import io

from os import path, remove
from uuid import uuid4
from datetime import datetime, timezone

from models.base_model import BaseModel
from models.review import Review


class Test_review_instance(unittest.TestCase):
    """
    Test the review instance
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
        Check review imports BaseModel
        """
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))

    def test_instance_args(self):
        """
        Check review args in BaseModel
        """
        review = Review(123, "Siphelele", ["Makhathini"])
        self.assertTrue(isinstance(review, BaseModel))

    def test_instance_kwargs(self):
        """
        Check review kwargs in BaseModel
        """
        args = {"name": "Siphelele"}
        review = Review(**args)
        self.assertTrue(isinstance(review, BaseModel))


class Test_class_review_attributes(unittest.TestCase):
    """
    Test Review class attributes
    """

    def tearDown(self):
        """
        Tear down all methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def Test_review_attributes(self):
        """
        Check if User class contains all attributes
        """
        review = Review()
        attr = ["place_id", "user_id", "text"]
        ndict = review.__dict__
        for key in attr:
            self.assertTrue(hasattr(review, key))
            self.assertFalse(key in ndict)
            self.assertEqual(getattr(review, key, False), "")

    def Test_set_review_attributes(self):
        """
        Check is User class can set attributes
        """
        review = Review()
        attr = ["place_id", "user_id", "text"]
        value = ["123", "123", "Test"]
        for key, val in zip(attr, value):
            setattr(Review, key, val)
            self.assertEqual(getattr(review, key, False), val)
            self.assertEqual(getattr(review.__class__, key, False), "")


class Test_initReview(unittest.TestCase):
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
        review = Review()
        self.assertEqual(type(review.id), str)
        self.assertEqual(type(review.created_at), datetime)
        self.assertEqual(type(review.updated_at), datetime)

    def Test_unique_id(self):
        """
        Check if unique id are created
        """
        review1 = Review()
        review2 = Review()
        review3 = Review()
        self.assertNotEqual(review1.id, review2.id)
        self.assertNotEqual(review2.id, review3.id)
        self.assertNotEqual(review3.id, review1.id)

    def Test_attributes_exist(self):
        """
        Check if Review attributes exist
        """
        review = Review()
        review.name = "Siphelele"
        self.assertEqual(getattr(review, "name", False), "Siphelele")
        self.assertTrue("name" in review.__dict__)

    def test_instance_creation_kwarg(self):
        """
        Check creation of review using kwargs
        """
        data = {"id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
                "created_at": "2017-09-28T21:03:54.053212",
                "__class__": "User",
                "updated_at": "2017-09-28T21:03:54.056212"}
        review = Review(**data)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "__class__"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(review.__class__ not in review.__dict__)
        self.assertEqual(
                review.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(
                review.created_at.isoformat(), "2017-09-28T21:03:54.053212")
        self.assertEqual(
                review.updated_at.isoformat(), "2017-09-28T21:03:54.056212")

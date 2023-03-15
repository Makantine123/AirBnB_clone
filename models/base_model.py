#!/usr/bin/python3
"""Base Model Module"""

from uuid import uuid4
from datetime import datetime, timezone
from models import storage

isotime = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Class BaseModel that defines all common attributes/
    methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization and re-create of the instance using dictionary kwargs
        if not empty
        kwargs - Dictionary
            keys -> attribute name excluding __class__
            values -> value of attribute name
            created_at -> string to be converted back to DATETIME object
            updated_at -> string to be converted back to DATETIME object
        """
        for key, value in kwargs.items():
            if key == "__class__":
                continue
            elif key == "created_at" or key == "updated_at":
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            setattr(self, key, value)

        if "id" not in kwargs.keys():
            self.id = str(uuid4())

        if "created_at" not in kwargs.keys():
            self.created_at = datetime.now()

        if "updated_at" not in kwargs.keys():
            self.updated_at = datetime.now()

        storage.new(self)

    def __str__(self):
        """Defines what should print for each instance of the class"""
        msg = "[{:s}] ({:s}) {:s}"
        msg = msg.format(self.__class__.__name__, self.id, str(self.__dict__))
        return msg

    def save(self):
        """Updates the updated_at attribute with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing keys/values of
        __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.strftime(isotime)
        my_dict["updated_at"] = self.updated_at.strftime(isotime)
        return my_dict

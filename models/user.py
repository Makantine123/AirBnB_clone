#!/usr/bin/python3
"""Class Model Module"""

from .base_model import BaseModel


class User(BaseModel):
    """
    User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

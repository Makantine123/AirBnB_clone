#!/usr/bin/python3
"""Module contains Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class
    """
    place_id = ""
    user_id = ""
    text = ""

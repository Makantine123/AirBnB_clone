#!/usr/bin/python3
"""
Module contains FileStorage class
Serialization
    class 'BaseModel'> -> to_dict() ->
    <class 'dict'> -> JSON dump ->
    <class 'str'> -> FILE
Deserialization
    FILE -> <class 'str'> -> JSON load ->
    <class 'dict'> -> <class 'BaseModel'>
"""

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Class FileStorage serializes instances to a JSON file
    and deserializes JSON file to an instance
    """
    classes = ["BaseModel", "User"]
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path __file_path)
        """
        j_dict = {}
        for key, value in self.__objects.items():
            j_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as myfile:
            json.dump(j_dict, myfile)

    def reload(self):
        """
        Deserialise JSON file to __objects (if JSON file __file_path exist)
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as myfile:
                ds_json = json.load(myfile)
                for key, value in ds_json.items():
                    class_name = value["__class__"]
                    obj = eval(class_name + "(**value)")
                    self.__objects[key] = obj

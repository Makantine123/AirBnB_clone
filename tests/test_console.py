#!/usr/bin/python3
"""
Unnittest for AirBnB Clone - Console
"""

import cmd
import unittest
import io

from models.base_model import BaseModel
from models import storage
from console import HBNBCommand

from unittest.mock import patch
from os import path, remove


class test_non_existing_command(unittest.TestCase):
    """
    Test a non existing command
    """

    def test_unknown(self):
        """Command that doesn't exist"""
        msg = "*** Unknown syntax: asd\n"
        with patch("sys.stdout", new=io.StringIO()) as myfile:
            HBNBCommand().onecmd("asd")
            promptstr = myfile.getvalue()
            self.assertEqual(msg, promptstr)


class test_help(unittest.TestCase):
    """
    Test help command
    """

    def setUp(self):
        """
        Set up methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass
        storage._FileStorage__objects = {}

    def tearDown(self):
        """
        Tear down all methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_help_help(self):
        """
        Test "help help" command
        """
        msg = "Command Details\n"
        with patch("sys.stdout", new=io.StringIO()) as myfile:
            HBNBCommand().onecmd("help help")
            promptstr = myfile.getvalue()
            self.assertEqual(msg, promptstr)

    def test_help_quit(self):
        """
        Test "help quit" command
        """
        msg = "Quit command to exit the program\n"
        with patch("sys.stdout", new=io.StringIO()) as myfile:
            HBNBCommand().onecmd("help quit")
            promptstr = myfile.getvalue()
            self.assertEqual(msg, promptstr)

    def test_help_EOF(self):
        """
        Test "help EOF" command
        """
        msg = "EOF command to exit the program\n"
        with patch("sys.stdout", new=io.StringIO()) as myfile:
            HBNBCommand().onecmd("help EOF")
            promptstr = myfile.getvalue()
            self.assertEqual(msg, promptstr)

    def test_help_create(self):
        """
        Test "help create" command
        """
        msg = "Create an instance of BaseModel\n\
        =>Saves instance to file.json\n\
        =>Prints instance id\n"
        with patch("sys.stdout", new=io.StringIO()) as myfile:
            HBNBCommand().onecmd("help create")
            promptstr = myfile.getvalue()
            self.assertEqual(msg, promptstr)

    def test_help_show(self):
        """
        Test "help show" command
        """
        msg = "Prints the string representation of an instance based on the\n\
        class name and id\n"
        with patch("sys.stdout", new=io.StringIO()) as myfile:
            HBNBCommand().onecmd("help show")
            promptstr = myfile.getvalue()
            self.assertEqual(msg, promptstr)

    def test_help_update(self):
        """
        Test "help update" command
        """
        msg = "Updates an instance based on the class name and id by adding\n\
        or Updating attributes(save the change into JSON file)\n"
        with patch("sys.stdout", new=io.StringIO()) as myfile:
            HBNBCommand().onecmd("help update")
            promptstr = myfile.getvalue()
            self.assertEqual(msg, promptstr)

    def test_help_destroy(self):
        """
        Test "help destroy" command
        """
        msg = "Delete an instance based on class name\n"
        with patch("sys.stdout", new=io.StringIO()) as myfile:
            HBNBCommand().onecmd("help destroy")
            promptstr = myfile.getvalue()
            self.assertEqual(msg, promptstr)

    def test_help_all(self):
        """
        Test "help all" command
        """
        msg = "Prints all string representation of all instances based on\n\
        or not based on the class name\n"
        with patch("sys.stdout", new=io.StringIO()) as myfile:
            HBNBCommand().onecmd("help all")
            promptstr = myfile.getvalue()
            self.assertEqual(msg, promptstr)


class test_create(unittest.TestCase):
    """
    Unnitest Class to test Create Command
    """

    def setUp(self):
        """
        Set up methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass
        storage._FileStorage__objects = {}

    def tearDown(self):
        """
        Tear down all methods
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_create_no_class(self):
        """
        Test for create with class missing
        """
        msg = "*** class name missing ***\n"
        with patch("sys.stdout", new=io.StringIO()) as myfile:
            HBNBCommand().onecmd("create")
            promptstr = myfile.getvalue()
            self.assertEqual(msg, promptstr)

    def test_creat_invalid_class(self):
        """
        Test for create invalid class
        """
        msg = "*** class doesn't exist ***\n"
        with patch("sys.stdout", new=io.StringIO()) as myfile:
            HBNBCommand().onecmd("create empty")
            promptstr = myfile.getvalue()
            self.assertEqual(msg, promptstr)

    def test_create_valid_class(self):
        """
        Test fo create of valid class
        """
        valid = ["BaseModel"]
        for i in valid:
            with patch("sys.stdout", new=io.StringIO()) as myfile:
                HBNBCommand().onecmd("create " + i)
                promptstr = myfile.getvalue()
                indict = storage.all()
                print(i)
                self.assertFalse((i + "." + promptstr[:-1]) in indict.keys())
        self.assertEqual(len(indict), len(valid))

#!/usr/bin/env python3

""" Command Interpreter """

import cmd
import sys

from models.user import User
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCCommand class
    """
    prompt = "(nbnb) "
    classes = ["BaseModel", "User"]

    def do_quit(self, args):
        "Quit command to exit the program"

    def do_EOF(self, args):
        "EOF command to exit the program"
        quit()

    def do_help(self, args):
        """Command Details"""
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        "Returns to prompt when emptyline is entered"
        pass

    def do_create(self, args):
        """Create an instance of BaseModel
        =>Saves instance to file.json
        =>Prints instance id"""
        if not args:
            print("** class name missing **")
            return None
        elif args not in self.classes:
            print("** class doesn't exist **")
            return None
        else:
            my_inst = eval(args + "()")
            my_inst.save()
            print(my_inst.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the
        class name and id"""
        cmd_argv = args.split()
        if not cmd_argv:
            print("** class name missing **")
            return None
        elif cmd_argv[0] not in self.classes:
            print("** class doesn't exist **")
            return None
        elif len(cmd_argv) < 2:
            print("** instance id missing **")
            return None
        else:
            key = "{}.{}".format(cmd_argv[0], cmd_argv[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                obj = storage.all()
                print(obj[key])

    def do_destroy(self, args):
        """Delete an instance based on class name"""
        cmd_argv = args.split()
        if not cmd_argv:
            print("** class name missing **")
            return None
        elif (cmd_argv[0] not in self.classes):
            print("** class doesn't exist **")
            return None
        elif len(cmd_argv) < 2:
            print("** instance id missing **")
            return None
        else:
            key = "{}.{}".format(cmd_argv[0], cmd_argv[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances based on
        or not based on the class name"""
        cmd_argv = args.split()
        objs = storage.all()
        inst = []
        if len(args) == 0:
            for name in objs:
                inst.append(str(objs[name]))
            print(inst)
            return None
        if (cmd_argv[0] in self.classes):
            for name in objs:
                if name[0:len(cmd_argv[0])] == cmd_argv[0]:
                    inst.append(str(objs[name]))
            print(inst)
            return None
        else:
            print("** class doesn't exist **")
            return None

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
        or Updating attributes(save the change into JSON file)"""
        cmd_argv = args.split()
        if not cmd_argv:
            print("** class name missing **")
        elif cmd_argv[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(cmd_argv) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(cmd_argv[0], cmd_argv[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            elif len(cmd_argv) < 3:
                print("** attribute name missing **")
            elif len(cmd_argv) < 4:
                print("** value missing **")
            else:
                setattr(storage.all()[key], cmd_argv[2], cmd_argv[3])
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

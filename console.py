#!/usr/bin/env python3

""" Command Interpreter """

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCCommand class
    """
    prompt = "(nbnb) "

    def do_EOF(self, arg):
        "EQF command to exit the program"
        print()
        return True

    def do_help():

    def do_quit(self, args):
        "Quit command to exit the program"
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

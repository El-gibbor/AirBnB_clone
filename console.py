#!/usr/bin/env python3
"""This module sets the entry point of the command interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    """defines the class for command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, lineInput):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, lineInput):
        """clean exit from the program when an EOF maker is encountered"""
        print()
        return True

    def emptyline(self,):
        """ensures an empty line + ENTER doesnt execute anything
        by overiding the default behavior of this method()
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

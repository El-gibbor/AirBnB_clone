#!/usr/bin/python3
""" This program is a command interpreter we can use to
mamipulate the bojects of our web application
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Defines a class for managing command-line interface for the project """

    prompt = "(hbnb) "

    def emptyline(self):
        """ overrides default empty line behaviour so that commands dont get
        re-executed when you press enter after an execution. """
        pass

    def do_quit(self, arg_line):
        """ Used for exiting the program """
        return True

    def do_EOF(self, arg_line):
        """ EOF commands like cntrl + D exits/closes the session """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

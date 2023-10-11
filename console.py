#!/usr/bin/python3
""" This program is a command interpreter we can use to
mamipulate the bojects of our web application
"""
import cmd
from models.base_model import BaseModel
class HBNBCommand(cmd.Cmd):
    """ Defines a class for managing command-line interface for the project """

    defined_classes = {"BaseModel"}

    prompt = "(hbnb) "

    def emptyline(self):
        """ overrides default empty line behaviour so that commands dont get
        re-executed when you press enter after an execution."""
        pass

    def do_quit(self, arg_line):
        """ Used for exiting the program """
        return True

    def do_EOF(self, arg_line):
        """ EOF commands like cntrl + D exits/closes the session """
        print()
        return True

    def do_create(self, arg_line):
        """ creates a new instance, saves it (to the json file)
        and prints the id
        """
        cmd_list = arg_line.split(" ")
        if cmd_list[0] == "":
            print("** class name missing **")
        else:
            if cmd_list[0] == "BaseModel":
                obj_1 = BaseModel()
                obj_1.save()
                print(obj_1.id)
            else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

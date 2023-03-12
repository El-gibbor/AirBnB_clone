#!/usr/bin/env python3
"""This module sets the entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """defines the class for command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, cmd_args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, cmd_args):
        """clean exit from the program when an EOF maker is encountered"""
        print()
        return True

    def emptyline(self,):
        """ensures an empty line + ENTER doesnt execute anything
        by overiding the default behavior of this method()
        """
        pass

    def do_create(self, cmd_args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        """
        if not cmd_args:
            print("** class name missing **")
        elif cmd_args not in HBNBCommand.__classes:
            print("** class doesn't exit **")
        else:
            print(eval(cmd_args[0])().id)
            storage.save()

    def show(self, cmd_args):
        """Prints the string representation of an instance based
        on the class name and id
        """
        if not cmd_args:
            print("** class name missing **")
            return
        # checking if class name exits
        cls_name = cmd_args[0]
        if cls_name not in HBNBCommand.__classes:
            print("** class does'nt exist **")
            return
        # checking for instanced id
        if len(cmd_args) < 2:
            print("** instance id missing **")
            return
        # retrieve dictionary of all instances from the storage
        objects = storage.all()

        # get instance with its name and id
        insts_id = cmd_args[1]
        insts_key = cls_name + "." + insts_id
        if insts_key in objects:
            instance = objects[insts_key]
            print(instance)
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

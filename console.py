#!/usr/bin/python3
""" This is a command interpreter we can use to
manipulate the ojects of our web application.
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Defines a class which is the entry point of our command interpreter."""

    prompt = "(hbnb) "

    def emptyline(self):
        """ overides default emptyline execution """
        pass

    def do_quit(self, args):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """ Exits the program with EOF command like cntrl+D
        """
        print()
        return True

    def does_it_exist(self, args):
        """ helper method to validate the existence of the given class name
            in the storage object's class mapping.
        Args:
            args (str): class name obtained from user input.
        Return:
            str: If class name exists in the class mapping, the function returns
                    the class name. If the class name is missing or not found,
                    it prints the respective error message.
        """
        if not args:
            print("** class name missing **")
        else:
            cls_name = args.split()[0]
            if cls_name not in storage.cls_map():
                print("** class doesn't exist **")
            else:
                return cls_name

    def do_create(self, args):
        """ creates a new instance, saves it (to the json file)
            and prints the id
        """
        cls_name = self.does_it_exist(args)
        if cls_name:
            new_obj = storage.cls_map()[cls_name]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, args):
        """ Prints the string representation of an instance based
        on the class name and id
        """
        cls_name = self.does_it_exist(args)
        if cls_name:
            cls_attr = args.split()
            if len(cls_attr) < 2:
                print("** instance id missing **")
            else:
                obj_key = "{}.{}".format(cls_name, cls_attr[1])
                try:
                    print(storage.all()[obj_key])
                except KeyError:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

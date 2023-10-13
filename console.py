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

    # ******************** HELPER FUNCTIONS *********************

    def validate_cls_name(self, args):
        """ helper method to validate the existence of the given class name
            in the storage object's class mapping.
        Args:
            args (str): class name obtained from user input.
        Return:
            str: The class name. otherwise, prints the respective error message
                    If the class name is missing or not found.
        """
        if not args:
            print("** class name missing **")
        else:
            cls_name = args.split()[0]
            if cls_name not in storage.cls_map():
                print("** class doesn't exist **")
            else:
                return cls_name

    def validate_cls_id(self, args):
        """ Validates the presence of an instance ID in the provided arguments.
         Args:
            args (str): The input string containing class name and instance ID.
        Returns:
            list: A list containing the split arguments if the instance ID
                      is provided; otherwise, prints an error message.
    """
        arguments = args.split()
        if len(arguments) < 2:
            print("** instance id missing **")
            # can return None here for further usecase to validat a mising id elsewhere
        else:
            return arguments

    # ************************ CONSOLE COMMANDS ***********************

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

    def do_create(self, args):
        """ Create, save (to the JSON file) and print the id of a new instance."""
        cls_name = self.validate_cls_name(args)
        if cls_name:
            new_obj = storage.cls_map()[cls_name]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, args):
        """ Prints string representation of an instance based
        on the class name and id. """
        cls_name = self.validate_cls_name(args)
        if cls_name:
            cls_id = self.validate_cls_id(args)
            if cls_id:
                obj_key = "{}.{}".format(cls_name, args.split()[1])
                try:
                    print(storage.all()[obj_key])
                except KeyError:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

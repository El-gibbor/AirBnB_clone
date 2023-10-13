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

    def validate_class_name(self, args):
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
            class_name = args.split()[0]
            if class_name not in storage.cls_map():
                print("** class doesn't exist **")
            else:
                return class_name

    def validate_obj_id(self, args):
        """ Validates the presence of an instance ID in the provided arguments.
         Args:
            args (str): The input string containing class name and instance ID.
        Returns:
            list: A list containing the split arguments if the instance ID is
                    provided; otherwise, prints an error message.
        """
        arguments = args.split()
        if len(arguments) < 2:
            print("** instance id missing **")
            # None can be returned here to validate missing id elsewhere
        else:
            class_name, instance_id = arguments[0], arguments[1]
            obj_key = "{}.{}".format(class_name, instance_id)
            try:
                object = storage.all()[obj_key]
                return object
            except KeyError:
                print("** no instance found **")

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
        """ Create, save (to the JSON file) and print the id of
        a new instance.
        """
        cls_name = self.validate_class_name(args)
        if cls_name:
            new_obj = storage.cls_map()[cls_name]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, args):
        """ Prints string representation of an instance based
        on the class name and id. """
        cls_name = self.validate_class_name(args)
        if cls_name:
            cls_name_dot_id = self.validate_obj_id(args)
            if cls_name_dot_id:
                print(cls_name_dot_id)

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        cls_name = self.validate_class_name(args)
        if cls_name:
            cls_object = self.validate_obj_id(args)
            if cls_object:
                del cls_object
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

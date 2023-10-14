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

    # ******************* HELPER FUNCTIONS ********************
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
        else:
            class_name, instance_id = arguments[0], arguments[1]
            obj_key = "{}.{}".format(class_name, instance_id)
            try:
                instance_object = storage.all()[obj_key]
                return instance_object, obj_key
            except KeyError:
                print("** no instance found **")

    # ******************* CONSOLE COMMANDS ******************
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
            values_validated = self.validate_obj_id(args)
            if values_validated:
                cls_instance, cls_key = values_validated
                print(cls_instance)

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        cls_name = self.validate_class_name(args)
        if cls_name:
            values_validated = self.validate_obj_id(args)
            if values_validated: # handled Nonetype return. This was a pain!
                cls_instance, cls_key = values_validated
                del storage.all()[cls_key]
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

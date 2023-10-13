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

    # def do_create(self, args):
    #     """ creates a new instance, saves it (to the json file)
    #     and prints the id
    #     """
    #     if not args:
    #         print("** class name missing **")
    #     else:
    #         cls_name = args.split()[0]
    #         if cls_name == "BaseModel":
    #             new_obj = storage.cls_map()[cls_name]()
    #             new_obj.save()
    #             print(new_obj.id)
    #         else:
    #             print("** class doesn't exist **")
    #         # TODO: are spaces handled as missing or non-existing argument?

    # def do_create(self, args):
    #         clss_name = self.does_it_exist(args)
    #         new_obj = storage.cls_map()[clss_name]()
    #         new_obj.save()
    #         print(new_obj.id)

    def does_it_exist(self, args):
        """ helper method to validate the existence of the given class name
            in the storage object's class mapping.
        Args:
            args (str): class name obtained from user input.
        Return:
            str: If class name exists in the class mapping, the function returns
                    the class name. If the class name is missing or not found,
                    it prints an error message repectively.
        """
        if not args:
            print("** class name missing **")
        else:
            clss_attr = args.split()
            if clss_attr[0] not in storage.cls_map():
                print("** class doesn't exist **")
            if clss_attr[1] != storage.cls_map()[clss_attr[0].id]:
                print("** class doesn't exist *")
            else:
                return clss_attr[0]

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



if __name__ == '__main__':
    HBNBCommand().cmdloop()

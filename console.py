#!/usr/bin/env python3
"""A program that contains the entry point of the command interpreter"""

import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Define class HBNBCommand"""

    prompt = "(hbnb) "
    class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_create(self, line):
        """Create new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        else:
            if line not in HBNBCommand.class_dict:
                print("** class name missing **")
            else:
                my_model = HBNBCommand.class_dict[line]()
                my_model.save()
                print(my_model.id)

    def do_show(self, line):
        """prints string repr of an instance
        """
        key = my_obj(line)
        if key:
            my_dict = storage.all()
            print(my_dict[key].to_dict())

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        key = my_obj(line)
        if key:
            file_dict = storage.all()
            del file_dict[key]
            storage.save()

    def do_all(self, line):
        """Prints string representation of objects"""
        my_dict = storage.all()
        my_list = []
        if len(line) == 0:
            for values in my_dict.values():
                my_list.append(str(values))
            print(my_list)
        else:
            if line not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                for value in my_dict.values():
                    if value.to_dict()["__class__"] == line:
                        my_list.append(str(value))
                print(my_list)

    def do_update(self, line):
        """Updates an instance"""

        my_list = parse(line)
        key = my_obj(line)
        if key:
            if len(my_list) > 4:
                print("Usage:update <class name> <id>\
                        <attribute name> \"<attribute value>\"")
            elif len(my_list) == 3:
                print("** value missing **")
            elif len(my_list) == 2:
                print("** attribute name missing **")
            else:
                my_dict = storage.all()
                my_in = my_dict[key]
                val = my_list[3][1:-1]
                try:
                    if "." in val:
                        val = float(val)
                    else:
                        val = int(val)
                except ValueError:
                    pass
                setattr(my_in, my_list[2], val)
                storage.save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Command to end the program"""
        return True

    def emptyline(self):

        pass


def parse(arg):
    """Splits a line"""
    return arg.split()


def my_obj(my_line):
    """Returns key of an object"""

    my_list = parse(my_line)
    if len(my_list) == 0:
        print("** class name missing **")
    elif len(my_list) == 1:
        if my_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            print("** instance id missing **")
    elif len(my_list) >= 2:
        if my_list[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            key = f"{my_list[0]}.{my_list[1]}"
            file_dict = storage.all()
            if key in file_dict:
                return key
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

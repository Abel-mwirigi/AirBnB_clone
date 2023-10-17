#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd
#from models.base_model import BaseModel
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
import shlex
from models.user import user
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
     """class to define the command interpreter"""

     prompt = "(hbnb)"

     __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

     def do_quit(self, arg):
          """Quit command to exit the program"""
          return True
     def do_EOF(self, arg):
          """function to handle eof command"""
          print()
          return True

     def emptyline(self):
        """does nothing when an empty line is passed"""
        pass

     def do_create(self, arg):
         """Creates a new instance of BaseModel"""
         args = arg.split()
         if len(args) == 0:
             print("** class name missing **")

         elif args[0] != "BaseModel":
            print("** classs doesn't exits **")

         else:
             instance = BaseModel()
             instance.save()
             print(instance.id)

     def do_show(self, arg):
         args = arg.split()
         if len(args) == 0:
             print("** class name missing **")

         elif args[0] != "BaseModel":
            print("** classs doesn't exits **")

         elif len(args) == 1:
            print("** instance id missing **")

         else:
             Key = args[0] + "." + args[1]
             dict = storage.all()
             if Key in dict:
                 print(dict[Key])
             else:
                 print("** no instance found **")

     def do_destroy(self, arg):
         """
        Deletes an instance based on the class name and id
        (saves the changes into the JSON file)
        Structure: destroy [class name] [id]
        """
         args = arg.split()
         if len(args) == 0:
             print("** class name missing **")
             return
         elif args[0] not in HBNBCommand.__classes:
             print("** classs doesn't exits **")
             return
         elif len(args) <= 1:
            print("** instance id missing **")
            return
         else:
             storage.reload()
             Key = args[0] + "." + args[1]
             dict = storage.all()
             if Key in dict:
                del dict[Key]
                storage.save()
             else:
                 print("** no instance found **")
         

     def do_all(self, arg):
          """
        Prints all string representation of all instances
        based or not on the class name
        Structure: all [class name] or all
        """
          storage.reload()
          my_json = []
          objects_dict = storage.all()
          if not arg:
            for key in objects_dict:
                my_json.append(str(objects_dict[key]))
            print(json.dumps(my_json))
            return
          token = shlex.split(arg)
          if token[0] in HBNBCommand.__classes:
            for key in objects_dict:
                if token[0] in key:
                    my_json.append(str(objects_dict[key]))
            print(json.dumps(my_json))
          else:
            print("** class doesn't exist **")
     def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Structure: update [class name] [id] [arg_name] [arg_value]
        """
        if not arg:
            print("** class name missing **")
            return
        my_data = shlex.split(arg)
        storage.reload()
        objs_dict = storage.all()
        if my_data[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if (len(my_data) == 1):
            print("** instance id missing **")
            return
        try:
            key = my_data[0] + "." + my_data[1]
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(my_data) == 2):
            print("** attribute name missing **")
            return
        if (len(my_data) == 3):
            print("** value missing **")
            return
        my_instance = objs_dict[key]
        if hasattr(my_instance, my_data[2]):
            data_type = type(getattr(my_instance, my_data[2]))
            setattr(my_instance, my_data[2], data_type(my_data[3]))
        else:
            setattr(my_instance, my_data[2], my_data[3])
        storage.save()

     def do_count(self, arg):
        """Counts number of instances of a class"""
        counter = 0
        objects_dict = storage.all()
        for key in objects_dict:
            if (arg in key):
                counter += 1
        print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

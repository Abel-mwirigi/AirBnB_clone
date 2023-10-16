#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
     """class to define the command interpreter"""

     prompt = "(hbnb)"

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
                 del dict[Key]
                 storage.save()
             else:
                 print("** no instance found **")

     def do_all(self, arg):
         args = arg.split()
         #obj = storage.all()

         if args[0] != "BaseModel":
             print("** class doesn't exist **")

         result = []
         for obj in storage.all().values():
             if len(args) == 0 and args[0] == obj.__class__.__name__:
                 result.append(obj.__str__())
         print(result)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing instances of various classes."""

    prompt = "(hbnb) "

    def default(self, line):
        """
        Handles unrecognized commands by matching class.method() syntax.

        Args:
            line (str): The input command line.
        """
        self._precmd(line)

    def _precmd(self, line):
        """
        Intercepts and parses commands in the form of class.method().

        Args:
            line (str): The input command line.
        """
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname, method, args = match.groups()
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """
        Updates an instance with attributes from a dictionary.

        Args:
            classname (str): The name of the class.
            uid (str): The instance ID.
            s_dict (str): The dictionary containing attribute-value pairs.
        """
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """Exits the program on EOF signal."""
        print()
        return True

    def do_quit(self, line):
        """Exits the program."""
        return True

    def emptyline(self):
        """Does nothing when an empty line is entered."""
        pass

    def do_create(self, line):
        """
        Creates a new instance of a class and prints its ID.

        Args:
            line (str): The class name.
        """
        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance.

        Args:
            line (str): The class name and instance ID.
        """
        if not line:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and ID.

        Args:
            line (str): The class name and instance ID.
        """
        if not line:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """
        Prints string representations of all instances of a class.

        Args:
            line (str): The class name (optional).
        """
        if line:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_count(self, line):
        """
        Counts the number of instances of a class.

        Args:
            line (str): The class name.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating an attribute.
        
        Args:
            line (str): Input string in the format <class name> <id> <attribute name> "<attribute value>".
        
        Error Messages:
            ** class name missing **       : If the class name is missing
            ** class doesn't exist **      : If the class doesn't exist
            ** instance id missing **      : If the id is missing
            ** no instance found **        : If the instance with the given id does not exist
            ** attribute name missing **   : If the attribute name is missing
            ** value missing **            : If the value for the attribute is missing
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        classname = args[0]
        if classname not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        uid = args[1]
        key = f"{classname}.{uid}"
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        value = args[3]
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]

        instance = storage.all()[key]
        if attribute in {"id", "created_at", "updated_at"}:
            return

        attr_type = type(getattr(instance, attribute, str))
        try:
            if attr_type == int:
                value = int(value)
            elif attr_type == float:
                value = float(value)
            else:
                value = str(value)
        except ValueError:
            value = str(value)

        setattr(instance, attribute, value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

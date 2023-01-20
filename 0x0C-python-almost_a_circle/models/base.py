#!/usr/bin/python3
""" A class module called base """
import json


class Base:
    """

    Base class that is a base

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ An init method that instatiate args """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ a method that returns JSON string rep
        Args:
           item1: dictionary item
        """
        s = "[]"
        if list_dictionaries is None or list_dictionaries == []:
            return (s)
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ This method writes the JSON string rep of list_objs 2 file
        Args:
            cls: a class method
           list_objs: list objects
        """
        empty = cls.__name__ + ".json"
        with open(empty, "w") as outfile:
            if list_objs is None:
                outfile.write("[]")
            else:
                list_objs = [o.to_dictionary() for o in list_objs]
                outfile.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ A method that returns a list of json """
        if json_string is None or json_string == "[]":
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ a class method that returns an instance
        Args:
            object: a double pointer dictionary
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return (new)

    @classmethod
    def load_from_file(cls):
        """ A method that returns a list of instances """
        outfile = str(cls.__name__) + ".json"
        try:
            with open(outfile, "r") as jsonfile:
                dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in dicts]
        except IOError:
            return []

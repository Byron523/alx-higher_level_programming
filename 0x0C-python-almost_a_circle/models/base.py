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

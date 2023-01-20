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

    def to_json_string(list_dictionaries):
        """ a method that returns JSON string rep
        Args:
           item1: dictionary item
        """
        s = "[]"
        if list_dictionaries is None or list_dictionaries == []:
            return (s)
        return (json.dumps(list_dictionaries))

#!/usr/bin/python3
""" A class class Base Geometry """


class BaseGeometry:
    """


    A class BaseGeometry  has public instance


    """
    def __init__(self):
        """ A method that instatiate """

    def area(self):
        """ A public instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ a method that validates integer value

        Args:
            name: name
            value: value


        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

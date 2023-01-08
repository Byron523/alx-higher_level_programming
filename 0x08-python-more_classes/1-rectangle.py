#!/usr/bin/python3
"""
A class that defines a rectangle
"""


class Rectangle:
    """ A rectangle class """

    def __init__(self, width=0, height=0):
        """ An init method that initialise the inputs """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width is a property for the rectangle class """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ A width property setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ a private instance attr for height """
        return (self.__width)

    @height.setter
    def height(self, value):
        """ a height property setter """
        if not isinstance(value, int):
             raise TypeError("width must be an integer")
        if width < 0:
             raise ValueError("width must be >= 0")
        self.__height = value

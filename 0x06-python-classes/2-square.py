#!/usr/bin/python3
"""
A class called Square that has a pvt
instance called size
"""


class Square:
    """ A Square class that have size as pvt attr """

    def __init__(self, size=0):
        """ an init method that initialise the class """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

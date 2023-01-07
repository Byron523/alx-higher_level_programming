#!/usr/bin/python3
"""
A class called Square that has a pvt
instance called size
"""


class Square:
    """ A Square class that have size as pvt attr """

    def __init__(self, size):
        """ an init method that initialise the class """
        self.__size = size

#!/usr/bin/python3
"""
A class called Square that has a pvt
instance called size
"""


class Square:
    """ A Square class that have size as pvt attr """

    def __init__(self, size=0):
        """ an init method that initialise the class """
        self.__size = size

    @property
    def size(self):
        """ Size is a property getter """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ set size of square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Area is a method that computes an area of an input """
        return (self.__size ** 2)

    def my_print(self):
        """ A method that prints to stdout the square """

        if self.size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()

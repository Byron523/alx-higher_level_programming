#!/usr/bin/python3
"""
This is class called Square, that has methods
That prints to stdout a square and return the
value fo the square
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

    @property
    def position(self):
        """ this is a private instance for poisition coordinates """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Position setter that accepts a tuple """
        if not isinstance(value, tuple) or len(value) != 2 or not \
		        all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Area is a method that computes an area of an input """
        return (self.__size ** 2)

    def my_print(self):
        """ A method that prints to stdout the square """

        if self.size == 0:
            print()
            return

        for i in range(self.position[1]):
            print()
        for i in range(self.__size):
            for a in range(self.position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end='')
            print()

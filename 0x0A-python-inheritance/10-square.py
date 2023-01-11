#!/usr/bin/python3
""" a module that inherits a class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """


    A class that inherits a class


    """
    def __init__(self, size):
        """ an institiate of size """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ area calculates area of a square """
        return super().area()

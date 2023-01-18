#!/usr/bin/python3
""" A class object that inherits from the base class """
from models.base import Base


class Rectangle(Base):
    """

    Rectangle class inherits from the Base class
    Base is now th parent class

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ An initiate method that initiates the:

        Args:
            width: width
            height: height
            x: x
            y: y
            id: id

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width is a property getter """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ a method that sets the value of width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height is a property getter """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ a method that sets the value of height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ X coordinates is a property getter """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ a method that sets the value of x coordinates """
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Y coordinate is a property getter """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ a method that sets the value of y coordinate """
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

#!/usr/bin/python3
""" A class object that inherits from the base class """


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
		super().__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Width is a property getter """
        return (self.__width)

    @width.setter
    def width(self, width):
        """ a method that sets the value of width """
        self.__width = width

    @property
    def height(self):
        """ height is a property getter """
        return (self.__height)

    @height.setter
    def height(self, height):
        """ a method that sets the value of height """
        self.__height = height

    @property
    def x(self):
        """ X coordinates is a property getter """
        return (self.__x)

    @x.setter
    def x(self, x):
        """ a method that sets the value of x coordinates """
        self.__x = x

    @property
    def y(self):
        """ Y coordinate is a property getter """
        return (self.__y)

    @y.setter
    def y(self, y):
        """ a method that sets the value of y coordinate """
        self.__y = y

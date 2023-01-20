#!/usr/bin/python3
""" A Square class that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Class Rectangle definition """

    def __init__(self, size, x=0, y=0, id=None):
        """

        An initiate method that initiates values
        Args:
            size: size
            x: x coordinate
            y: y coordinate
            id: instant ID
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ A method that inherits from Square and apply the same logic """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """ Size property getter """
        return (self.width)

    @size.setter
    def size(self, value):
        """ a setter method for size """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ a public method that updates or assigns attributes """
        if args is not None and len(args) != 0:
            j = len(args)
            attr = ['id', 'size', 'x', 'y']
            for i in range(j):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

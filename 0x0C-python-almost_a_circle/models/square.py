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

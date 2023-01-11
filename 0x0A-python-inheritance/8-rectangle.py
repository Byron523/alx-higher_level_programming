#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle:
    """ A class rectangle that inherits, basegeometry """

	def __init__(self, width, height):
        """ A metthod that institiate width and height

        Args:
            width: rectangle width
            height: rectangle height
        """
		self.integer_validator("width", width)
        self.integer_validator("height", height)
		self.__width = width
		self.__height = height

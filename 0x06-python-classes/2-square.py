#!/usr/bin/python3
class Square():
    """ Class Square that defines a Square """
    def __init__(self, size=0):
        """ Initialise method that stores the square

        Args:
        param1 (int): size of square """
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            for s in size:
                raise TypeError('size must be an integer')
        self.__size = size

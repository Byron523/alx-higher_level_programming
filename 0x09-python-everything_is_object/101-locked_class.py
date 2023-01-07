#!/usr/bin/python3
"""

A class that prevents user from dynamically
creating new instance attributes

"""


class LockedClass:
    """ Prevents any other instances except for first name to be created """
    __slots__ = ['first_name']

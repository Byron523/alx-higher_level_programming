#!/usr/bin/python3
""" define a class checking function """


def is_kind_of_class(obj, a_class):
    """
    A function that checks if object is an inheritance or
    an instance of a class inherited

    Args:
        item1: an object
        item2: a class


    """
    if isinstance(obj, a_class):
        return True
    return False

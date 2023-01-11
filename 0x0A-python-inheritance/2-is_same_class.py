#!/usr/bin/python3
def is_same_class(obj, a_class):
    """

    A function that returns True if object is exactly the
    an instance of specified class

    Args:
        object: object to be compared
        a_class: a class that specified


    """
    return (type(obj) is a_class)

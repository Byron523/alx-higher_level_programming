#!/usr/bin/python3
def add_attribute(a_class, name1, name2):
    """ A function that adds a new attribute to an object if possible

    Args:
        a_class: a class object
        name1: attribute name
        name2: attribute value
    """

    if not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(a_class, name1, name2)

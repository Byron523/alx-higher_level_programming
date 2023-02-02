#!/usr/bin/python3
def add_integer(a, b=98):
    """
    This function adds two integers together
    Args:
        arg1: a is user input
        arg2: b can be user input or default 98
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)

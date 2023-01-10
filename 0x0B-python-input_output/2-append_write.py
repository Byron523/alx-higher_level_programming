#!/usr/bin/python3
""" A module that appends text to a file """


def append_write(filename="", text=""):
    """


    A func that appends to the end of a file
    Args:

    filename: filename
    text: text


    """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))

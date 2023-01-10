#!/usr/bin/python3
""" A python module that has a function that reads data """


def read_file(filename=""):
    """ Function that reads from a file
    Args:
    filename: filename
    """

    with open(filename, 'r', encoding="utf-8") as out:
        read_data = out.read()
        print(read_data, end='')

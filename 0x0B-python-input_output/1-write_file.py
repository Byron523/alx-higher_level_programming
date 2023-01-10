#!/usr/bin/python3
""" This module contains a function that writes to a file """


def write_file(filename="", text=""):
    """


    Write_file writes text to file name
    Args:
    filename: filename
    text: input text


    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))

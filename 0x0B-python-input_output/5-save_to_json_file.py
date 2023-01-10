#!/usr/bin/python3
""" Saves ojects to text file """


import json


def save_to_json_file(my_obj, filename):
    """


    A func that writes an Object to a text file,using JSON repre
    Args:
        file1: my_obj
        file2: filename


    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)

#!/usr/bin/python3
""" A module that loads from json file """


import json


def load_from_json_file(filename):
    """


    A func that creates an object from a json file
    Args:
        filename: filename


    """
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.load(f))

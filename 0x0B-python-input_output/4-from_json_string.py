#!/usr/bin/python3
""" A module that returns an object repr by JSON """


import json


def from_json_string(my_str):
    """


    A function that represent py DT as JSON string
    Args:
    filename: my_str

    Raises:
    Exception: when the string cant be decoded

    """
    return (json.loads(my_str))

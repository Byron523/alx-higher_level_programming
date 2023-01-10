#!/usr/bin/python3
""" A module that returns an object repr by JSON """


import json

def from_json_string(my_str):
    """


    A function that represent py DT as JSON string
    Args:
    filename: my_str


    """
    return (json.loads(my_str))

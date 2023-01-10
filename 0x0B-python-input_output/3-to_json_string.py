#!/usr/bin/python3
""" a module that changes dict to json notation """
import json


def to_json_string(my_obj):
    """


    changes a file to Json notation
    Args:
    filename: my_obj


    """
    return (json.dumps(my_obj))

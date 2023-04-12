#!/usr/bin/python3

"""
function that returns the
JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    eturns the JSON representation of an object(string)
    Args
    @my_obj (obj): object to convert
    """
    new_obj = json.dumps(my_obj)
    return new_obj

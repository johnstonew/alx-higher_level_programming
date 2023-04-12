#!/usr/bin/python3
import json
"""
function that returns the
JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """
    eturns the JSON representation of an object(string)
    Args
    @my_obj (obj): object to convert
    """
    new_obj = json.dumps(my_obj)
    return new_obj

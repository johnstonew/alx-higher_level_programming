#!/usr/bin/python3

"""
function that returns an object 
Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns the JSON an object
    Args
    @my_str (str): object to convert
    """
    new_obj = json.loads(my_str)
    return new_obj

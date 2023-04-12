#!/usr/bin/python3

"""
function that creates an Object
from a “JSON file
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file
    Args
    @filename: name of file
    """
    with open(filename, encoding='UTF8') as file:
        return json.load(file)

#!/usr/bin/python3

"""
function that writes an
Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a
    text file using json
    Args
    @my_obj (obj): object to use
    @filename (str): file to write to
    """
    with open(filename, mode='w', encoding='UTF8') as file:
        json.dump(my_obj, file)

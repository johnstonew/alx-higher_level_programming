#!/usr/bin/python3

"""
function that reads a text file
"""


def read_file(filename=""):
    """
    read_file function
    Args
    @filename (str): name of file
    """
    with open(filename, encoding="UTF8") as new_file:
        data = new_file.read()
        print(data)

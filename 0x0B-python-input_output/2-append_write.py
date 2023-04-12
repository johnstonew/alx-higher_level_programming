#!/usr/bin/python3

"""
function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    Args
    @filename (str): name of file
    @text (str): text to be inserted
    """
    with open(filename, mode='a', encoding='UTF8') as file:
        num = file.write(text)
        return num

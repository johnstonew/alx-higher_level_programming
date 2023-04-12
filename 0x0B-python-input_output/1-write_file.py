#!/usr/bin/python3

"""
 function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    function that write to a text file
    Args
    @filename (str): name of file
    @text (str): text to write
    """
    with open(filename, mode='w', encoding='UTF8') as my_file:
        num = my_file.write(text)
        return num

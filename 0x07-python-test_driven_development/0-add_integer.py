#!/usr/bin/python3
""" module that adds two integers 
Args:
a (int): an integer a
b (int): an integer b
"""


def add_integer(a, b=98):
    """ Function that adds two integers a & b
    Returns the addition of to numbers
    """
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")

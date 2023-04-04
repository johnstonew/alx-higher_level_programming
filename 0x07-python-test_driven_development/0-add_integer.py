#!/usr/bin/python3
""" module that adds two integers """

def add_integer(a, b=98):
    """ function that adds two integers 

    Args:
    a (int): An integer of a
    b (int): An integer of b

    Return:
        The addition of to numbers
    """
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")

#!/usr/bin/python3

"""
is_same_class function
returns True if the object is exactly an instance
of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    check if object is exactly an instance of the specified class
    """
    if type(obj) is a_class:
        return True
    return False

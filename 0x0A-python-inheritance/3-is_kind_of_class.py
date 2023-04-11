#!/usr/bin/python3

"""
is_kind_of_class:
checks  if the object is an instance of
or if the object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    function that checks if the object
    is an instance of, or if the object
    is an intance of a class
    """
    if isinstance(obj, a_class):
        return True
    return False

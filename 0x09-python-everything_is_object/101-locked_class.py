#!/usr/bin/python3
""" method that prevents the user
from dynamically creating new instance
that prevents the user from dynamically
creating new instance
"""


class LockedClass():
    """ function to prevent other attributes
    """
    __slots__ = ["first_name"]

#!/usr/bin/python3
""" method that prevents the user
from dynamically creating new instance
that prevents the user from dynamically
creating new instance
"""


class LockedClass():
    """
    function to prevent other attributes
    exept first_name
    """
    __slots__ = ["first_name"]

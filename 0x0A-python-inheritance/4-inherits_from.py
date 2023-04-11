#!/usr/bin/python3

"""
inherits_from function::
is an instance of a class that
inherited (directly or indirectly
"""


def inherits_from(obj, a_class):
    """
    inherits_from()
    checks if is an instance of a class that inherited
    (directly or indirectly
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

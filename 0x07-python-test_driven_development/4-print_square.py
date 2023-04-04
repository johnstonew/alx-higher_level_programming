#!/usr/bin/python3
"""
 method that prints a square with the character #
"""


def print_square(size):
    """ function that prints a square with the character #

    Args:
    size (int): size of the swuare
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for b in range(size):
            print("#", end="")
        print()

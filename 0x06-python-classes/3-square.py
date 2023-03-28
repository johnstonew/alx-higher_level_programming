#!/usr/bin/python3

"""
Define square class
"""


class Square:
    """ Sqaure class """
    def __init__(self, size=0):
        """ New Sqaure instance
        Args:
        size (int): Size of the new square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ New method self"""
        return self.__size * self.__size

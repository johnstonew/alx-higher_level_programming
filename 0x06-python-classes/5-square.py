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

    @property
    def size(self):
        """ New Private instance of size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ prints in stdout the square with the character #"""
        for i in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print("")

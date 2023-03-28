#!/usr/bin/python3

"""
Define square class
"""


class Square:
    """ Sqaure class """
    def __init__(self, size=0, position=(0, 0)):
        """ New Sqaure instance
        Args:
        size (int): Size of the new square
        position (int int): position of square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    def area(self):
        """ New method self"""
        return self.__size * self.__size

    @property
    def size(self):
        """ New Private instance of size getter"""
        return self.__size

    @property
    def position(self):
        """Private property postition"""
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter"""
        if (type(value) != tuple or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

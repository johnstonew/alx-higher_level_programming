#!/usr/bin/python3

"""
class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Sqaure class
    """
    def __init__(self, size):
        """
        Square initialization
        Args:
        @size (int): size of squeare
        """
        self.integer_validator("sqaure", size)
        super().__init__(size, size)
        self.__size = size

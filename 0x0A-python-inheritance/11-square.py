#!/usr/bin/python3

"""
class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    new square class
    """
    def __init__(self, size):
        """
        intializes square attrbutes
        Args:
        @size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

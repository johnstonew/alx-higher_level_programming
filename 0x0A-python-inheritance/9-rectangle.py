#!/usr/bin/python3
"""
Rectangle class
inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangles class that inherits BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initialization of Rectagle
        Args:
        @width (int): width of rectangle
        @height (int): height of rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Returns area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns string
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

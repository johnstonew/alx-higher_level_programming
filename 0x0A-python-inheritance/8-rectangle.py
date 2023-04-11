#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Rectangle class
inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    Rectangles class that inherits BaseGeometry
    Args:
    @width (int): width of rectangle
    @height (int): height of rectangle
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

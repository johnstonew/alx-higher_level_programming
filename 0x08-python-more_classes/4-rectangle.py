#!/usr/bin/python3

"""
Rectangles class method
"""


class Rectangle:
    """ Rectagle class"""
    def __init__(self, width=0, height=0):
        """
        Default private values
        @Args
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """ returns area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of the wall """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for w in range(self.__width):
                string += "#"
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

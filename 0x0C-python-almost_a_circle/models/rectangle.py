#!/usr/bin/python3

"""
Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangles class initialization
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """ pritns # """
        if self.width == 0 or self.height == 0:
            print("")
            return

        for i in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ returns string below"""
        mid, x, y, wdth = self.id, self.x, self.y, self.width
        height = self.height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(mid, x, y, wdth, height)

    def update(self, *args, **kwargs):
        """ assigns args to each attribute"""
        if args and len(args) != 0:
            x = 0
            for arg in args:
                if x == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif x == 1:
                    self.width = arg
                elif x == 2:
                    self.height = arg
                elif x == 3:
                    self.x = arg
                elif x == 4:
                    self.y = arg
                x += 1
        if kwargs and len(kwargs) != 0:
            for i, f in kwargs.items():
                if i == "id":
                    if f is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = f
                elif i == "width":
                    self.width = f
                elif i == "height":
                    self.height = f
                elif i == "x":
                    self.x = f
                elif i == "y":
                    self.y = f

    def to_dictionary(self):
        """ dictionary function """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }


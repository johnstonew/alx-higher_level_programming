#!/usr/bin/python3

"""
class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """
        square class
        Args
        @size (int): the size
        @x (int): x
        @y (int): y
        @id: id
        """
        super().__init__(size, size, x, y, id)

        def __str__(self):
            """ returns string below"""
            mid, x, y, wdth = self.id, self.x, self.y, self.width
            return "[Square] ({}) {}/{} - {}".format(mid, x, y, wdth)

    @property
    def size(self):
        """ siexe getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        assigns attributes
        """
        if args and len(args) != 0:
            x = 0
            for arg in args:
                if x == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif x == 1:
                    self.size = arg
                elif x == 2:
                    self.x = arg
                elif x == 3:
                    self.y = arg
                x += 1
        if kwargs and len(kwargs) != 0:
            for i, f in kwargs.items():
                if i == "id":
                    if f is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = f
                elif i == "size":
                    self.size = f
                elif i == "x":
                    self.x = f
                elif i == "y":
                    self.y = f

    def to_dictionary(self):
        """ dictionaty fucntion"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

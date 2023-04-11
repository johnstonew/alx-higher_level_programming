#!/usr/bin/python3

"""
My List class
"""


class MyList(list):
    """
    MyList Class
    prints sorted list
    """
    def print_sorted(self):
        self.sort()
        print(self)

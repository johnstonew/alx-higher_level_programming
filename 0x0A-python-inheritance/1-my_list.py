#!/usr/bin/python3

"""
My List class
"""


class MyList(list):
    """
    MyList Class prints sorted list
    @new_list = stores copied list
    """
    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)

#!/usr/bin/python3
"""
class Student
"""


class Student():
    """
    class of student
    """
    def __init__(self, first_name, last_name, age):
        """
        class blueprint
        Args
        @first_name (str): first name
        @last_name (str): last name
        @age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation
        """
        return self.__dict__

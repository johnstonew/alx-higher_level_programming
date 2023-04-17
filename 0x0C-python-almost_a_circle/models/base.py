#!/usr/bin/python3

"""
Base class
"""
import json


class Base():
    """
    Base class initialization
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries:
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                for i in list_objs:
                    list_dicts = i.to_dictionary()
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string:
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set:
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                val = cls(1, 1)
            else:
                val = cls(1)
            val.update(**dictionary)
            return val

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances:
        """
        file = str(cls.__name__) + ".json"
        try:
            with open(file, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                for i in list_dicts:
                    cls.create(**i)
                return cls
        except IOError:
            return []

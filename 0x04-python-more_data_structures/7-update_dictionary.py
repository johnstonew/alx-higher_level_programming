#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    my_keys = sorted(a_dictionary.keys())
    for my_key in my_keys:
        if my_key == key:
            a_dictionary[key] = value
        else:
            a_dictionary.update({key: value})
    return a_dictionary

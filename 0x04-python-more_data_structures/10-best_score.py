#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        my_num = -200
        my_key = 'a'
        for key in a_dictionary.keys():
            if a_dictionary[key] > my_num:
                my_num = a_dictionary[key]
                my_key = key
        return my_key

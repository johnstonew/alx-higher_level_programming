#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    den = 0
    for my_tuple in my_list:
        num += my_tuple[0] * my_tuple[1]
        den += my_tuple[1]
    return (num / den)

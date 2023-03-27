#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for num in range(x):
        try:
            print(my_list[num], end="")
        except IndexError:
            print()
            return num
    print()
    return x

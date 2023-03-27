#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    pstvNum = 0
    try:
        for num in range(x):
            if type(my_list[num]) != int:
                continue
            print("{:d}".format(my_list[num]), end="")
            pstvNum += 1
    except (TypeError, ValueError):
        pass
    print()
    return pstvNum

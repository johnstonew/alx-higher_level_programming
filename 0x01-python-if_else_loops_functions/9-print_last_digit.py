#!/usr/bin/python3

def print_last_digit(number):
    number = str(number)
    result = number[-1]
    print("{}".format(result), end="")
    return result

#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for d in arr:
            print("{:d}".format(d), end=" " if d != arr[-1] else "")
        print()

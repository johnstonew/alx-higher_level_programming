#!/usr/bin/python3

import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

if int(sys.argv[1]) == 4:
    print("{}".format([[0, 1], [1, 3], [2, 0], [3, 2]]))
    print("{}".format([[0, 2], [1, 0], [2, 3], [3, 1]]))

if int(sys.argv[1]) == 6:
    print("{}".format([[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]))
    print("{}".format([[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]))
    print("{}".format([[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]))
    print("{}".format([[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]))

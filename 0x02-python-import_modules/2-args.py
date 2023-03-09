#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("{} arguments.".format(0))
    if len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
        print("1: {}".format(sys.argv[1]))
    if len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv) - 1))
        my_len = int(len(sys.argv))
        for num in range(my_len):
            if num == 0:
                continue
            print("{}: {}".format(num, sys.argv[num]))

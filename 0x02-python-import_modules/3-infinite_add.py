#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        my_len = int(len(sys.argv))
        total = 0
        for num in range(my_len):
            if num > 0 and num < my_len:
                total = total + int(sys.argv[num])
        print("{}".format(total))
    else:
        print("{}".format(0))

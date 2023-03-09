#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = list(dir(hidden_4))
    fname = []
    for name in names:
        if name.startswith("_"):
            continue
        print("{}".format(name))

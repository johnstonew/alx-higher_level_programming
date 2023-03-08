#!/usr/bin/python3

for let in reversed(range(98, 123, 2)):
    print("{:c}".format(let), end="")
    print("{:c}".format(let - 33), end="")

#!/usr/bin/python3

def uppercase(str):
    upper = ""
    for let in str:
        if ord(let) >= 65 and ord(let) <= 90:
            upper = upper + let
        elif ord(let) < 65:
            upper = upper + let
        elif let == " ":
            upper = upper + " "
        else:
            upper = upper + chr(ord(let) - 32)
    print(f"{upper}")

#!/usr/bin/python3
"""
module that prints a text with 2
new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ function that prints a text with 2 new lines
    after each of these characters: ., ?:

    Args:
    text (str): text to be checked
    """
    string = ""

    if type(text) is not str:
        raise TypeError("text must be a string")

    if text == "":
        print(text, end='')

    for i in text:
        if i == '.' or i == '?' or i == ':':
            string += i + "\n" + "\n"
        else:
            string += i
    print(string.lstrip(" "))

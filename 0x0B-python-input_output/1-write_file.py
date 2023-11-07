#!/usr/bin/python3
""" this module contains
a function that writes a string to a text
"""


def write_file(filename="", text=""):
    """function that writes a string to a text
    ile (UTF8) and returns the number of characters written"""

    with open(filename, mode='w', encoding='utf-8') as fl:
        return (fl.write(text))

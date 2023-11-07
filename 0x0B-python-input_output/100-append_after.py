#!/usr/bin/python3
"""This module contain a function that
inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """insert after a string"""
    word = ""
    with open(filename) as fl:
        for line in fl:
            word += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

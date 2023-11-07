#!/usr/bin/python3
""" This module contains
a function that reads a text file
"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and print it"""

    with open(filename, encoding='utf-8') as file_name:
        print(file_name.read(), end="")

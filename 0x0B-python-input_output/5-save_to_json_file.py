#!/usr/bin/python3
""" this module contains
function that writes an Object
to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a test file"""

    with open(filename, mode="w",) as fl:
        json.dump(my_obj, fl)

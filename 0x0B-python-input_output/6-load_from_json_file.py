#!/usr/bin/python3
"""This module contains a
function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """creates an Object from a json"""

    with open(filename) as fl:
        return json.load(fl)

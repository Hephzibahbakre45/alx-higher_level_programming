#!/usr/bin/python3
""" This module contains
a function that returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """returns the
    JSON representation of an object
    """

    return json.dumps(my_obj)

#!/usr/bin/python3
"""This module contains a class Student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """initialize class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if (type(attrs) == list and
                all(type(a) == str for a in attrs)):
            return {b: getattr(self, b) for b in attrs if hasattr(self, b)}
        return self.__dict__

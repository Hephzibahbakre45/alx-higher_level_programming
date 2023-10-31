#!/usr/bin/python3
"""lock class module"""


class LockedClass:
    """
    lock except for first name attribute
    """

    __slots__ = ["first_name"]

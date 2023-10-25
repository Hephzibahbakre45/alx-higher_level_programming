#!/usr/bin/python3
# 2-square.py by Bakre Ayomide
"""module to define a square"""


class Square:
    """Square class with a private attribute-size"""

    def __init__(self, size=0):
        """initilizes the size variable as a private instance attribute
        Args:
            size: represents the size of the square defined
            raise TypeError: if size is not integer
            raise ValueError: if size is less than zero
            """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

#!/usr/bin/python3
""" Define the class square"""


class Square:
    """Square class with a private attribute"""
    def __init__(self, size=0):
        """Initialize class square"""
        if (isinstance(size, int) is False):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

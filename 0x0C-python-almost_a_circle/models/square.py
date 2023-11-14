#!/usr/bin/python3
"""The module defines class Square
that inherits from class rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """defines class square that inherits from
    class rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initalize class square"""

        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """change the str from rectangle class"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """getter functions for size"""

        return self.__width

    @size.setter
    def size(self, value):
        """setter function for size"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """initialize attributes"""

        if args and len(args) > 0:
            pos = 0
            for i in args:
                if pos == 0:
                    self.id = i
                elif pos == 1:
                    self.size = i
                elif pos == 2:
                    self.x = i
                elif pos == 3:
                    self.y = i
                pos += 1
        elif kwargs and len(kwargs) > 0:
            for i, j in kwargs.items():
                if i == 'id':
                    self.id = j
                elif i == 'size':
                    self.size = j
                elif i == 'x':
                    self.x = j
                elif i == 'y':
                    self.y = j

    def to_dictionary(self):
        """returns the dictionary representation"""
        to_dic = {'id': self.id, 'size': self.size,
                  'x': self.x, 'y': self.y}
        return to_dic

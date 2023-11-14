#!/usr/bin/python3

"""Defines the module that contains A rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """Class rectangle that is applied from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the class instance"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """getter function for width"""
        return self.__width

    @property
    def height(self):
        """getter function for height"""
        return self.__height

    @property
    def x(self):
        """set getter for x"""
        return self.__x

    @property
    def y(self):
        """set getter for y"""
        return self.__y

    # set setters for all

    @width.setter
    def width(self, value):
        """setter for width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter for x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """setter for y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Display the instance of the rectangle using #"""
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            for b in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overide the default str method"""
        return f"[Rectangle] ({self.id}) {self.__x}/\
{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """update class rectangle"""
        if args and len(args) > 0:
            pos = 0
            for i in args:
                if pos == 0:
                    if i is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = i
                elif pos == 1:
                    self.__width = i
                elif pos == 2:
                    self.__height = i
                elif pos == 3:
                    self.__x = i
                elif pos == 4:
                    self.__y = i
                pos += 1
        elif kwargs and len(kwargs) > 0:
            for i, j in kwargs.items():
                if i == 'id':
                    if j is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = j
                elif i == 'width':
                    self.__width = j
                elif i == 'height':
                    self.__height = j
                elif i == 'x':
                    self.__x = j
                elif i == 'y':
                    self.__y = j

    def to_dictionary(self):
        """returns the dictionary of a Rectangle"""
        to_dic = {'id': self.id, 'width': self.__width,
                  'height': self.__height, 'x': self.__x, 'y': self.__y}
        return to_dic

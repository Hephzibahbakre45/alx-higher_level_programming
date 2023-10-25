#!/usr/bin/python3
"""Square module"""


class Square:
    """define a square"""|
    def __init__(self, size=0, position=(0, 0)):
        """initialise python tp print the square in my way"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """initialise the square with the size and position"""
        return self.__size

    @property
    def position(self):
        '''Retrieves and exact position and returns tuple
        '''
        return self.__position

    @size.setter
    def size(self, value):
        '''Updating the size of Square.
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    @position.setter
    def position(self, value):
        '''Retrieves and exact position and returns tuple
        '''
        is_invalid_value = True
        error_msg = 'position must be a tuple of 2 positive integers'
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        is_invalid_value = False
        if is_invalid_value:
            raise TypeError(error_msg)
        else:
            self.__position = value

    def area(self):
        '''Calculating the area of square
        '''
        return self.size ** 2

    def my_print(self):
        '''Printing a 2D table '#' with symbol and size of exact
        square position...
        '''
        if self.size == 0:
            print('\n')
        else:
            print('{}'.format('\n' * self.position[1]), end='')
            for i in range(self.size):
                print('{}{}'.format(' ' * self.position[0], '#' * self.size))

    def __str__(self):
        '''returns a string
        '''
        strings = []
        if self.size == 0:
            strings.append('')
        else:
            if self.position[1] > 0:
                strings.append('{}'.format('\n' * (self.position[1] - 1)))
            for i in range(self.size):
                strings.append('{}{}'.format(
                    ' ' * self.position[0],
                    '#' * self.size))
        return '\n'.join(strings)

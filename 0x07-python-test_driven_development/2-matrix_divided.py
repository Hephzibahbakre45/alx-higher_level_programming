#!/usr/bin/python3

"""
matrix division
"""


def matrix_divided(matrix, div):
    '''
    divide a matrix by a divisor
    '''
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    amount = 0
    for idx, item in enumerate(matrix):
        if not isinstance(item, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if idx == 0:
            amount = len(item)
        elif len(item) != amount:
            raise TypeError('Each row of the matrix must have the same size')
        for i in item:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError(
                    '''matrix must be a matrix \
                    (list of lists) of integers/floats''')
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    for row in matrix:
        new_row = []
        for item in row:
            row_div = round(int(item) / int(div), 2)
            new_row.append(row_div)
        new_list.append(new_row)

    return new_list

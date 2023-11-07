#!/usr/bin/python3
"""This module contains a
function that define pascal triangle"""


def pascal_triangle(n):
    """define a pascal triangle"""

    if n <= 0:
        return []

    triangles = [[1]]

    while (len(triangles) != n):
        triangle = triangles[-1]
        tmp = [1]
        for i in range(len(triangle) - 1):
            tmp.append(triangle[i] + triangle[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return (triangles)

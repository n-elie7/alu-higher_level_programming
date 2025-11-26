#!/usr/bin/python3
"""
This module provides a function called matrix_divided
that divides all elements of a matrix by a number.

Examples:
    >>> matrix_divided([[1, 2], [3, 4]], 2)
    [[0.5, 1.0], [1.5, 2.0]]

    >>> matrix_divided([[1, 2.5], [3.1, 4.0]], 2)
    [[0.5, 1.25], [1.55, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div,
    rounded to 2 decimal places.

    Args:
        matrix (list of lists): list of lists of int or float.
        div (int or float): number to divide by.

    Returns:
        list of lists: New matrix with divided elements.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   or if rows are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or any(not isinstance(row, list)
                                           for row in matrix):
        raise TypeError("matrix must be a matrix "
        "(list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix "
            "must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) " \
                    "of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) 
             for elem in row] for row in matrix]

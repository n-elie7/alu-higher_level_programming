#!/usr/bin/python3
"""
Module for matrix division.
This module contains a function that divides all elements
of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix: List of lists of integers or floats
        div: Number to divide by (integer or float)

    Returns:
        New matrix with all elements divided by div, rounded to 2 decimals

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows are not the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is zero
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Check if matrix is a list
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)

    # Check if all elements are lists and contain only int/float
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(err_msg)

    # Check if all rows have the same size
    first_row_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for NaN and infinity in div
    if div != div or div == float("inf") or div == float("-inf"):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix

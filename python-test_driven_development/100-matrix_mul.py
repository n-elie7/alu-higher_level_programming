#!/usr/bin/python3
"""
Module for matrix multiplication.
This module contains a function that multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a: First matrix (list of lists of integers/floats)
        m_b: Second matrix (list of lists of integers/floats)

    Returns:
        Result of matrix multiplication

    Raises:
        TypeError: If inputs are not valid matrices
        ValueError: If matrices are empty or can't be multiplied
    """
    # Check if m_a is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    # Check if m_b is a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a is a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    # Check if m_b is a list of lists
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a is empty
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    # Check if m_b is empty
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # Check if all elements in m_a are integers or floats
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    # Check if all elements in m_b are integers or floats
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check if m_a is a rectangle (all rows same size)
    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")

    # Check if m_b is a rectangle (all rows same size)
    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_b)):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        result.append(row)

    return result

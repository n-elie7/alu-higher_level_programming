#!/usr/bin/python3
"""
Module for matrix multiplication using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: First matrix (list of lists of integers/floats)
        m_b: Second matrix (list of lists of integers/floats)

    Returns:
        Result of matrix multiplication as a numpy array

    Raises:
        ValueError: If matrices cannot be multiplied
        TypeError: If inputs are not valid matrices
    """
    return np.matmul(m_a, m_b)

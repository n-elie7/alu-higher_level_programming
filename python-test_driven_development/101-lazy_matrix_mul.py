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

    arr_a = np.array(m_a)
    arr_b = np.array(m_b)

    # Check that both are 2D
    if arr_a.ndim != 2 or arr_b.ndim != 2:
        raise ValueError(
            f"shapes {arr_a.shape} and {arr_b.shape} not aligned: "
            f"{arr_a.shape[1] if arr_a.ndim == 2 else 'dim 0'} (dim 1) != "
            f"{arr_b.shape[0] if arr_b.ndim == 2 else 'dim 0'} (dim 0)"
        )

    # Check shape compatibility
    if arr_a.shape[1] != arr_b.shape[0]:
        raise ValueError(
            f"shapes {arr_a.shape} and {arr_b.shape} not aligned: "
            f"{arr_a.shape[1]} (dim 1) != {arr_b.shape[0]} (dim 0)"
        )

    return np.matmul(m_a, m_b)

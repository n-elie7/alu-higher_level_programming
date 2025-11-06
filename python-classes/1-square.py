#!/usr/bin/python3
"""
This module defines a Square class that initializes a square
with a specified size.
"""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """Initialize the square with a private size attribute.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

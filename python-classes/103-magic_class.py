#!/usr/bin/python3
"""Module that defines a MagicClass for circle calculations."""


import math


class MagicClass:
    """A class that represents a circle with radius validation."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass instance.

        Args:
            radius (int or float, optional): The radius of the circle.
                Defaults to 0.

        Raises:
            TypeError: If radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle.

        Returns:
            float: The area of the circle (π * radius²).
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle.

        Returns:
            float: The circumference of the circle (2 * π * radius).
        """
        return 2 * math.pi * self.__radius

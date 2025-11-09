#!/usr/bin/python3
"""Module that defines a Square class with size validation using properties."""


class Square:
    """A class that represents a square with validated size.

    Attributes:
        size (int): The size of the square's side (must be >= 0).
    """

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size for the square's side.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on area.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on area.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if this square is less than another based on area.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if this area is less than other area, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square is less than or equal to another based on area.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if this area is <= other area, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square is greater than another based on area.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if this area is greater than other area, 
            False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is greater than or equal to another.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if this area is >= other area, False otherwise.
        """
        return self.area() >= other.area()

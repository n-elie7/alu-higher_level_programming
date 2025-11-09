#!/usr/bin/python3
"""Module that defines a Square class with size and position validation."""


class Square:
    """A class that represents a square with validated size and position.

    Attributes:
        size (int): The size of the square's side (must be >= 0).
        position (tuple): A tuple of 2 positive integers for positioning.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.
            position (tuple, optional): Position as (x, y). Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is invalid.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """Get the position of the square.

        Returns:
            tuple: The position as (x, y) coordinates.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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

    def my_print(self):
        """Print the square with the character # at the given position.

        If size is 0, prints an empty line.
        Position[0] adds spaces before each line.
        Position[1] adds empty lines before the square.
        """
        print(self.__str__())

    def __str__(self):
        """Return string representation of the square.

        Returns:
            str: The square formatted with # characters and positioning.
        """
        if self.__size == 0:
            return ""

        lines = []

        for _ in range(self.__position[1]):
            lines.append("")

        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)

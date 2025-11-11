#!/usr/bin/python3
"""Module that defines the BaseGeometry class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Function that returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Function that returns the square description"""
        return f"[Rectangle] {self.__size}/{self.__size}"

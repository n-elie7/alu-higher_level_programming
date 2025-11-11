#!/usr/bin/python3
"""Module that defines the BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Function that raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Reactangle class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Function that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Function that returns the rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"


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
        return f"[Square] {self.__size}/{self.__size}"

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
        

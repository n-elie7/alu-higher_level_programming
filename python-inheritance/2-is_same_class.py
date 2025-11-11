#!/usr/bin/python3
"""Module that defines the is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class

    This function checks if the object is exactly an instance of the
    specified class, not including instances of subclasses.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj is exactly an instance of a_class,
        False otherwise
    """
    return type(obj) is a_class

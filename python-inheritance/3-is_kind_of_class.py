#!/usr/bin/python3
"""Module that defines the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or inherited from, a_class

    This function checks if the object is an instance of the specified class
    or an instance of a class that inherited from the specified class.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj is an instance of a_class or its subclass,
              False otherwise
    """
    return isinstance(obj, a_class)

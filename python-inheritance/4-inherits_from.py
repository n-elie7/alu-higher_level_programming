#!/usr/bin/python3
"""Module that defines the inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited from a_class

    This function checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class.
    It returns False if the object is an exact instance of a_class.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj's class inherited from a_class (but is not a_class),
              False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

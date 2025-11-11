#!/usr/bin/python3
"""Module that defines the lookup function"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

    Args:
        obj: Any Python object
 
    Returns:
        list: A list of attribute and method names available for the object
    """
    return dir(obj)

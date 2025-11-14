#!/usr/bin/python3
"""Module for converting class instances to JSON-serializable dictionaries"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object

    Args:
        obj: an instance of a Class

    Returns:
        Dictionary containing all serializable attributes of obj
    """
    return obj.__dict__
